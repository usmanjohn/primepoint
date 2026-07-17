# TOPIK 말하기 (Speaking) — 4-savol: 대화 완성하기, lessons 1–3 (orders 40–42).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_q4_1_3.py \
#            --out examprep/management/commands/audio/speaking_q4
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_q4_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_q4

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "4-savol: Dialogni yakunlash (대화 완성하기)",
    "summary": "Dialogni eshitib, qatnashchilardan biri bo'lib o'z fikringiz bilan davom ettirish: muloyim rozilik, rad va taklif qoliplari.",
    "icon":    "bi-chat-dots",
    "order":   5,
}

LESSONS = [
    # ── Lesson 1 (order 40) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q4-1: Dialogga kirish — tan ol, fikr ayt, asosla",
        "summary": "4-topshiriq bilan tanishuv: suhbatning bir tomoni bo'lib fikr bildirish; TAN OLISH → FIKR → SABAB → TAKLIF formulasi.",
        "order":   40,
        "blocks": [
            {"rich_text": """
<h2>💬 4-topshiriq: suhbatga siz qo'shilasiz</h2>
<p>Ikki kishining <strong>muhokamasi</strong> eshitiladi (masalan: jamoat joyida telefon,
onlayn darslar, uy hayvoni...). Oxirgi replika sizga savol yoki fikr tashlaydi — va siz
<strong>qatnashchilardan biri bo'lib</strong> suhbatni davom ettirasiz: o'z fikringizni
aytasiz va asoslaysiz. Bu 1-topshiriqdan farqli: endi shunchaki savolga javob emas —
<strong>suhbatdoshning gapiga munosabat</strong> kerak.</p>
<h3>Oltin formula: 4 bo'g'in</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi bo'g'in ▸">
  <div class="pp-step"><p><strong>1. TAN OLISH.</strong> Suhbatdosh gapini bir jumla bilan qabul
  qiling: 네, 그 말도 맞아요. / 그럴 수도 있겠네요. — bu muloyimlik ko'prigi.</p></div>
  <div class="pp-step"><p><strong>2. FIKR.</strong> O'z pozitsiyangiz: 그런데 저는 ~다고 생각해요 /
  제 생각에는 ~는 것 같아요.</p></div>
  <div class="pp-step"><p><strong>3. SABAB.</strong> 왜냐하면 ~기 때문이에요 — yoki misol:
  실제로 제 친구도...</p></div>
  <div class="pp-step"><p><strong>4. TAKLIF/YAKUN.</strong> Yechim yoki yumshoq xulosa:
  그러니까 ~는 게 어떨까요? / ~면 좋을 것 같아요.</p></div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Fikringiz suhbatdoshnikiga qarshi bo'lsa ham — hujum qilmang!
  "아니에요, 틀렸어요" (yo'q, xato!) — ball yeydi. Koreys muloqotida qarshi fikr doim
  <strong>yumshatib</strong> aytiladi: 그럴 수도 있지만... (shunday ham bo'lishi mumkin-u, lekin...).
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: dialogni eshiting</h3>
<p>Mavzu: kafelarda uzoq o'tirib o'qish. Dialog + sizning o'rningizdagi namunaviy davom:</p>
""",
             "audio": "topik_s_040_1.mp3",
             "audio_script": [
                 ("여자", "요즘 카페에서 하루 종일 공부하는 사람들이 많잖아요. 커피 한 잔 시키고 여섯 시간씩 앉아 있는 건 좀 아닌 것 같아요."),
                 ("남자", "음, 그 말도 맞아요. 하지만 저는 조금 다르게 생각해요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy davom</strong> (siz — 남자):</p>
""",
             "audio": "topik_s_040_2.mp3",
             "audio_script": [
                 ("남자", "그 말도 맞아요. 카페는 장사를 하는 곳이니까요. 그런데 저는 학생들의 마음도 이해가 돼요. 왜냐하면 집에서는 집중이 잘 안 되고, 도서관은 자리를 구하기 어렵기 때문이에요. 그러니까 손님이 많은 시간에는 두세 시간만 있다가 자리를 비켜 주는 게 어떨까요? 서로 조금씩 배려하면 좋을 것 같아요."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring!</summary>
  <div style="margin-top:10px;">
    <p><strong>그 말도 맞아요. 카페는 장사를 하는 곳이니까요.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">1 TAN OLISH</span><br>
    <em style="color:#475569;">Gapingiz ham to'g'ri. Kafe — savdo qiladigan joy-da.</em></p>
    <p><strong>그런데 저는 학생들의 마음도 이해가 돼요.</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">2 FIKR</span><br>
    <em style="color:#475569;">Lekin men talabalarning holatini ham tushunaman.</em></p>
    <p><strong>왜냐하면 집에서는 집중이 잘 안 되고, 도서관은 자리를 구하기 어렵기 때문이에요.</strong> <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.8em;">3 SABAB</span><br>
    <em style="color:#475569;">Chunki uyda diqqat jamlanmaydi, kutubxonada esa joy topish qiyin.</em></p>
    <p><strong>그러니까 ... 자리를 비켜 주는 게 어떨까요? 서로 조금씩 배려하면 좋을 것 같아요.</strong> <span style="background:#fae8ff;padding:1px 8px;border-radius:999px;font-size:.8em;">4 TAKLIF</span><br>
    <em style="color:#475569;">Shuning uchun gavjum paytda ikki-uch soatdan keyin joy bo'shatib bersa-chi? Bir-birini ozgina o'ylasa, yaxshi bo'lardi.</em></p>
  </div>
</details>
<p>Kuzating: qarama-qarshi fikr, lekin birorta qattiq so'z yo'q — tan olish ko'prigi,
yumshoq qoliplar, ikki tomonga ham adolatli taklif. Bu — to'liq ball ovozi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Suhbatdosh fikriga qarshisiz. Qaysi boshlanish to'g'ri?</p>
""",
             "choices": [
                 {"text": "그럴 수도 있지만, 저는 조금 다르게 생각해요.", "is_correct": True},
                 {"text": "아니에요. 그건 틀린 생각이에요.", "is_correct": False},
                 {"text": "무슨 말인지 모르겠어요.", "is_correct": False},
                 {"text": "(jim turish)", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: yumshatish + o'z pozitsiya — koreys muloqot madaniyatining qolipi. ② hujum
(muloyimlik bali ketadi), ③ tushunmaganlik e'lon qilish, ④ eng yomoni — jimlik.
Qarshi fikr = ko'prik so'z (그럴 수도 있지만 / 그 말도 맞지만) + 저는...</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">그 말도 맞아요</div><div class="pp-card-back">gapingiz ham to'g'ri</div></div>
  <div class="pp-card"><div class="pp-card-front">그럴 수도 있지만</div><div class="pp-card-back">shunday bo'lishi ham mumkin-u, lekin</div></div>
  <div class="pp-card"><div class="pp-card-front">왜냐하면 -기 때문이에요</div><div class="pp-card-back">chunki ... sababli</div></div>
  <div class="pp-card"><div class="pp-card-front">-는 게 어떨까요?</div><div class="pp-card-back">...sa qanday bo'larkin?</div></div>
  <div class="pp-card"><div class="pp-card-front">배려하다</div><div class="pp-card-back">o'zgani o'ylamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">자리를 비키다</div><div class="pp-card-back">joy bo'shatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">이해가 되다</div><div class="pp-card-back">tushunsa bo'ladi</div></div>
  <div class="pp-card"><div class="pp-card-front">장사</div><div class="pp-card-back">savdo, tijorat</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Formula: TAN OLISH → FIKR → SABAB → TAKLIF.</li>
  <li>Qarshi fikr — faqat ko'prik so'z bilan: 그럴 수도 있지만...</li>
  <li>Yakuningiz ikki tomonga adolatli bo'lsa — eng baland ball.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 41) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q4-2: Fikr yumshatgichlari — rozilik va rad banki",
        "summary": "Rozilik, qisman rozilik va muloyim rad qoliplari banki + ikkinchi to'liq namuna (onlayn dars mavzusi).",
        "order":   41,
        "blocks": [
            {"rich_text": """
<h2>🧰 Fikr yumshatgichlari banki</h2>
<p>4-topshiriqda fikringiz uch holatdan birida bo'ladi. Har holatga tayyor qoliplar:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>✅ To'liq rozilik:</strong> 맞아요, 저도 그렇게 생각해요. 게다가 (ustiga-ustak) ~기도 하고요.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>🌗 Qisman rozilik:</strong> 그 말도 맞지만, 저는 ~라고 생각해요. / 물론 ~지요. 하지만...</p>
  <p style="font-size:1.05em;margin:0;"><strong>❌ Muloyim qarshilik:</strong> 글쎄요, 저는 조금 다르게 생각해요. 왜냐하면...</p>
</div>
<p>Va uchta kuchaytirgich — sababdan keyin qo'shsangiz, javob professional eshitiladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>실제로 제 경우에도...</strong> — haqiqatan, o'zimda ham... (shaxsiy misol)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>게다가 ~기도 해요</strong> — ustiga-ustak ... ham (ikkinchi sabab)</p>
  <p style="font-size:1.05em;margin:0;"><strong>물론 ~는 점도 있지만</strong> — albatta ...degan jihat ham bor-u (muvozanat — 태도 darslaridan tanish!)</p>
</div>
"""},
            {"rich_text": """
<h3>🎧 Ikkinchi namuna: onlayn dars yaxshimi?</h3>
""",
             "audio": "topik_s_041_1.mp3",
             "audio_script": [
                 ("남자", "요즘 학원에 안 가고 인터넷 강의로만 공부하는 학생들이 많던데요. 저는 온라인 수업이 더 좋은 것 같아요. 시간을 아낄 수 있잖아요."),
                 ("여자", "네, 그 말도 맞아요. 그런데 저는 조금 걱정되는 부분도 있어요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy davom</strong> (siz — 여자; bu safar ayol qatnashchi bo'lib davom
ettirasiz — imtihonda qaysi rol berilsa, o'shani olasiz):</p>
""",
             "audio": "topik_s_041_2.mp3",
             "audio_script": [
                 ("여자", "물론 온라인 수업은 시간을 아낄 수 있어서 좋지요. 그런데 저는 집에서 혼자 공부하면 게을러지기 쉽다고 생각해요. 실제로 제 경우에도 온라인 강의를 신청해 놓고 절반도 못 들었어요. 게다가 모르는 것이 있을 때 바로 질문할 수 없기도 하고요. 그러니까 자기 관리를 잘하는 사람에게는 온라인이 좋지만, 그렇지 않으면 학원이 더 나을 것 같아요."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>물론 온라인 수업은 시간을 아낄 수 있어서 좋지요.</strong><br><em style="color:#475569;">Albatta, onlayn dars vaqtni tejagani uchun yaxshi-da.</em></p>
    <p><strong>그런데 저는 집에서 혼자 공부하면 게을러지기 쉽다고 생각해요.</strong><br><em style="color:#475569;">Lekin menimcha, uyda yolg'iz o'qisang, dangasalashib ketish oson.</em></p>
    <p><strong>실제로 제 경우에도 온라인 강의를 신청해 놓고 절반도 못 들었어요.</strong><br><em style="color:#475569;">Haqiqatan, o'zim ham onlayn kursga yozilib, yarmini ham eshitmaganman.</em></p>
    <p><strong>게다가 모르는 것이 있을 때 바로 질문할 수 없기도 하고요.</strong><br><em style="color:#475569;">Ustiga-ustak, tushunmagan narsang bo'lsa, darhol so'ray olmaysan ham.</em></p>
    <p><strong>그러니까 자기 관리를 잘하는 사람에게는 온라인이 좋지만, 그렇지 않으면 학원이 더 나을 것 같아요.</strong><br><em style="color:#475569;">Shuning uchun o'zini boshqara oladiganga onlayn yaxshi-yu, unday bo'lmasa kurs afzalroq shekilli.</em></p>
  </div>
</details>
<p>Bank ishlayapti: 물론...지요 → 그런데 저는 → <strong>실제로 제 경우에도</strong>
(shaxsiy misol — eng ishonarli dalil!) → <strong>게다가 ~기도 하고요</strong> → shartli,
adolatli yakun. Sanoqli qoliplar — cheksiz mavzular.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> "실제로 제 경우에도..." jumlasi javobga nima beradi?</p>
""",
             "choices": [
                 {"text": "Shaxsiy tajriba — eng ishonarli va tabiiy dalil turi", "is_correct": True},
                 {"text": "Hech narsa, shunchaki vaqt to'ldiradi", "is_correct": False},
                 {"text": "Suhbatdoshni ayblaydi", "is_correct": False},
                 {"text": "Statistik ma'lumot beradi", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: abstrakt fikrni ("dangasalashish oson") jonli isbot bilan mustahkamlaydi ("o'zim
yarmini eshitmaganman"). Shaxsiy misol — 4-topshiriqning eng oson va eng kuchli dalili:
statistika shart emas, hayotingiz yetadi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> Namunadagi yakun nega kuchli?</p>
""",
             "choices": [
                 {"text": "Ikkala tomonga ham shart qo'yib, adolatli xulosa chiqargani uchun", "is_correct": True},
                 {"text": "Onlayn darsni butunlay taqiqlagani uchun", "is_correct": False},
                 {"text": "Javob bermay qo'ygani uchun", "is_correct": False},
                 {"text": "Eng uzun jumla bo'lgani uchun", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: "o'zini boshqarganga onlayn, bo'lmasa kurs" — ikkala variantning ham o'z o'rni
borligini ko'rsatadi. Muvozanatli yakun (물론 A지만 B) — 47–50 tinglash darslaridagi
"balanced notiq" ohangining og'zaki egizi. Baholovchilar buni juda qadrlaydi.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">인터넷 강의</div><div class="pp-card-back">onlayn dars (kurs)</div></div>
  <div class="pp-card"><div class="pp-card-front">게을러지다</div><div class="pp-card-back">dangasalashmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">실제로</div><div class="pp-card-back">haqiqatan, amalda</div></div>
  <div class="pp-card"><div class="pp-card-front">게다가</div><div class="pp-card-back">ustiga-ustak</div></div>
  <div class="pp-card"><div class="pp-card-front">자기 관리</div><div class="pp-card-back">o'z-o'zini boshqarish</div></div>
  <div class="pp-card"><div class="pp-card-front">-기 쉽다</div><div class="pp-card-back">...ishi oson (xavf)</div></div>
  <div class="pp-card"><div class="pp-card-front">-아/어 놓고</div><div class="pp-card-back">...b qo'yib (keyin aksini qilish)</div></div>
  <div class="pp-card"><div class="pp-card-front">더 낫다</div><div class="pp-card-back">afzalroq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Uch holat — uch qolip: to'liq rozilik / qisman / muloyim qarshilik.</li>
  <li>Kuchaytirgichlar: 실제로 제 경우에도 · 게다가 ~기도 하고요 · 물론 ~지만.</li>
  <li>Adolatli, shartli yakun — baholovchining sevimlisi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 42) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC,
        "title":   "TOPIK 말하기 Q4-3: To'liq amaliyot — ikki munozara",
        "summary": "Ikki dialog: uy hayvonlari ijara uyida va bolalarga telefon — o'zingiz davom ettirasiz, keyin namuna bilan solishtirasiz.",
        "order":   42,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: suhbatga kirishing!</h2>
<p>Tartib: dialogni eshiting → 30–40 soniya reja (4 bo'g'in: tan olish? fikr? sabab?
taklif?) → yozib gapiring (~1 daqiqa) → namunani eshitib soya qiling.</p>
<h3>1-dialog</h3>
""",
             "audio": "topik_s_042_1.mp3",
             "audio_script": [
                 ("여자", "우리 아파트에서 강아지 키우는 집이 많아졌잖아요. 밤에 짖는 소리 때문에 잠을 못 잘 때도 있어요. 아파트에서는 동물을 키우면 안 된다고 생각해요."),
                 ("남자", "아, 많이 불편하셨겠네요. 그런데 저는 생각이 조금 달라요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy davom</strong> (siz — 남자):</p>
""",
             "audio": "topik_s_042_2.mp3",
             "audio_script": [
                 ("남자", "밤에 잠을 못 주무셨다니 정말 불편하셨겠네요. 그런데 저는 무조건 금지하는 것은 답이 아니라고 생각해요. 왜냐하면 혼자 사는 사람들에게 반려동물은 가족과 같기 때문이에요. 문제는 동물이 아니라 관리를 안 하는 주인이지요. 그러니까 키우는 것을 금지하지 말고, 소음이나 산책 규칙을 함께 만드는 게 어떨까요?"),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>밤에 잠을 못 주무셨다니 정말 불편하셨겠네요.</strong><br><em style="color:#475569;">Kechasi uxlolmagan bo'lsangiz, rostdan noqulay bo'lgandir. (Hamdardlik — tan olishning eng iliq shakli!)</em></p>
    <p><strong>그런데 저는 무조건 금지하는 것은 답이 아니라고 생각해요.</strong><br><em style="color:#475569;">Lekin menimcha, butunlay taqiqlash — yechim emas.</em></p>
    <p><strong>왜냐하면 혼자 사는 사람들에게 반려동물은 가족과 같기 때문이에요. 문제는 동물이 아니라 관리를 안 하는 주인이지요.</strong><br><em style="color:#475569;">Chunki yolg'iz yashovchilarga uy hayvoni — oiladek. Muammo hayvonda emas, qaramaydigan egasida-da.</em></p>
    <p><strong>그러니까 키우는 것을 금지하지 말고, 소음이나 산책 규칙을 함께 만드는 게 어떨까요?</strong><br><em style="color:#475569;">Shuning uchun boqishni taqiqlamasdan, shovqin va sayr qoidalarini birga ishlab chiqsak-chi?</em></p>
  </div>
</details>
<p>Yangi g'isht: <strong>문제는 A가 아니라 B</strong> (muammo A emas, B da) — bahsni bir
zarbda hal qiladigan qolip. O'qishdagi tanish struktura endi munozara quroli!</p>
<h3>2-dialog</h3>
""",
             "audio": "topik_s_042_3.mp3",
             "audio_script": [
                 ("남자", "요즘 초등학생들도 다 스마트폰이 있더라고요. 저는 너무 이르다고 생각해요. 눈도 나빠지고 공부에도 방해가 되잖아요."),
                 ("여자", "네, 걱정되는 건 사실이에요. 하지만 저는 조금 다르게 봐요."),
             ]},
            {"rich_text": """
<p><strong>Namunaviy davom</strong> (siz — 여자):</p>
""",
             "audio": "topik_s_042_4.mp3",
             "audio_script": [
                 ("여자", "맞아요, 눈 건강이 걱정되는 건 사실이에요. 하지만 요즘은 학교 숙제도 인터넷으로 하고, 부모와 연락할 때도 휴대폰이 필요하잖아요. 무조건 못 쓰게 하면 아이가 친구들 사이에서 소외감을 느낄 수도 있고요. 그러니까 스마트폰을 주되, 하루 사용 시간을 정하고 밤에는 거실에 두게 하는 게 어떨까요? 금지보다 약속이 더 효과적인 것 같아요."),
             ],
             "explanation": ""},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>맞아요, 눈 건강이 걱정되는 건 사실이에요.</strong><br><em style="color:#475569;">To'g'ri, ko'z salomatligi xavotirli ekani rost.</em></p>
    <p><strong>하지만 요즘은 학교 숙제도 인터넷으로 하고, 부모와 연락할 때도 휴대폰이 필요하잖아요.</strong><br><em style="color:#475569;">Lekin hozir maktab vazifasi ham internetda, ota-ona bilan aloqa uchun ham telefon kerak-ku.</em></p>
    <p><strong>무조건 못 쓰게 하면 아이가 친구들 사이에서 소외감을 느낄 수도 있고요.</strong><br><em style="color:#475569;">Butunlay taqiqlansa, bola do'stlar orasida chetda qolgandek his qilishi ham mumkin.</em></p>
    <p><strong>그러니까 스마트폰을 주되, 하루 사용 시간을 정하고 밤에는 거실에 두게 하는 게 어떨까요? 금지보다 약속이 더 효과적인 것 같아요.</strong><br><em style="color:#475569;">Shuning uchun telefonni bering-u, kunlik vaqtini belgilab, kechasi mehmonxonada qoldirtirsak-chi? Taqiqdan ko'ra kelishuv samaraliroq shekilli.</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Ikkala namunaning umumiy siri:</strong> hech biri "taqiqlaymiz/erkin qo'yamiz"
  qutbiga bormadi — ikkalasi ham <strong>QOIDA/KELISHUV</strong> taklif qildi. O'rta yo'l +
  aniq taklif = 4-topshiriqning oltin yakuni.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> O'z yozuvingizni tekshiring: Q4 ning to'rt nazorat savoli qaysi?</p>
""",
             "choices": [
                 {"text": "Tan oldimmi? Fikrimni aytdimmi? Sabab/misol keltirdimmi? Taklif bilan yopdimmi?", "is_correct": True},
                 {"text": "Baland gapirdimmi? G'olib bo'ldimmi? Suhbatdoshni yengdimmi? Oxirgi so'z menikimi?", "is_correct": False},
                 {"text": "Necha daqiqa? Necha jumla? Necha grammatika? Necha so'z?", "is_correct": False},
                 {"text": "Dialog kim haqida? Qayerda yozilgan? Kim yozgan? Nechanchi savol?", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: to'rt bo'g'inning o'zi — bu nazorat ro'yxati. ② — munozara g'alaba emas,
<strong>muloqot</strong>: baholovchi yengishni emas, madaniy fikr almashishni o'lchaydi.
Q4 tayyor — endi grafik gapiradi (Q5)! 📊</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">반려동물</div><div class="pp-card-back">uy hayvoni (hamroh jonivor)</div></div>
  <div class="pp-card"><div class="pp-card-front">짖다</div><div class="pp-card-back">hurmoq (it)</div></div>
  <div class="pp-card"><div class="pp-card-front">무조건</div><div class="pp-card-back">so'zsiz, mutlaqo</div></div>
  <div class="pp-card"><div class="pp-card-front">금지하다</div><div class="pp-card-back">taqiqlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">소외감을 느끼다</div><div class="pp-card-back">chetda qolgandek his qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">-되</div><div class="pp-card-back">...gan holda, lekin shart bilan</div></div>
  <div class="pp-card"><div class="pp-card-front">효과적</div><div class="pp-card-back">samarali</div></div>
  <div class="pp-card"><div class="pp-card-front">문제는 A가 아니라 B</div><div class="pp-card-back">muammo A emas, B da</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Formula har mavzuda ishlaydi: tan ol → fikr → sabab → taklif.</li>
  <li>Kuchli g'ishtlar: 문제는 A가 아니라 B · -되 (shartli ruxsat) · 금지보다 약속.</li>
  <li>Munozarada g'alaba yo'q — madaniy muloqot bor. O'rta yo'l + aniq taklif = ball.</li>
</ul>
"""},
        ],
    },
]
