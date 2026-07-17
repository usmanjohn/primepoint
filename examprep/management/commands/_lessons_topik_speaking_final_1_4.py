# TOPIK 말하기 (Speaking) — 6-savol: 의견 제시하기 (60–62) + Yakuniy takror (70).
# Ikki TOPIC bitta faylda (listening final uslubi).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_speaking_final_1_4.py \
#            --out examprep/management/commands/audio/speaking_final
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_speaking_final_1_4.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/speaking_final

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC_Q6 = {
    "title":   "6-savol: Fikr bildirish (의견 제시하기)",
    "summary": "Ijtimoiy mavzuda 2–3 daqiqalik og'zaki insho — og'zaki 쓰기 54: bitta mukammal shablon + [주제] almashtirish metodi.",
    "icon":    "bi-megaphone",
    "order":   7,
}

TOPIC_REVIEW = {
    "title":   "Yakuniy takror (총정리)",
    "summary": "Barcha 6 topshiriq ketma-ket — imtihon ritmida yakuniy mashq va kursning uch oltin qoidasi.",
    "icon":    "bi-trophy",
    "order":   8,
}

LESSONS = [
    # ── Lesson 1 (order 60) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC_Q6,
        "title":   "TOPIK 말하기 Q6-1: Bitta shablon — hamma mavzu",
        "summary": "6-topshiriq bilan tanishuv: og'zaki 쓰기 54; KIRISH → 1-DALIL → 2-DALIL → XULOSA skeleti va [주제] almashtirish metodi.",
        "order":   60,
        "blocks": [
            {"rich_text": """
<h2>🏔️ 6-topshiriq: imtihonning eng baland cho'qqisi</h2>
<p>Kompyuter sizga <strong>ijtimoiy mavzu</strong> beradi (예: "erta chet tili ta'limi
haqida qanday fikrdasiz?") va siz 2–3 daqiqa davomida <strong>asoslangan fikr</strong>
aytasiz. Bu — og'zaki 쓰기 54. Va yozishdagi qoidangiz shu yerda ham oltin:
<strong>hamma shablonni chala bilguncha, BITTA shablonni mukammal biling</strong>
(우물을 파도 한 우물을 파라 — esladingizmi? 😄).</p>
<h3>Sizning BITTA shabloningiz</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi bo'g'in ▸">
  <div class="pp-step"><p><strong>1. KIRISH (입장).</strong><br>
  요즘 [주제]에 대한 관심이 높아지고 있습니다. 저는 [주제]에 대해 긍정적으로/부정적으로
  생각합니다. — mavzuni ochish + pozitsiya. [주제] o'rniga istalgan mavzu!</p></div>
  <div class="pp-step"><p><strong>2. 1-DALIL.</strong><br>
  첫째, ~기 때문입니다. 예를 들어... — birinchi sabab + misol.</p></div>
  <div class="pp-step"><p><strong>3. 2-DALIL (+ muvozanat).</strong><br>
  둘째, ~기 때문입니다. 물론 ~는 점도 있지만, ~라고 생각합니다. — ikkinchi sabab +
  qarshi tomonni tan olib qaytarish (baholovchining sevimlisi!).</p></div>
  <div class="pp-step"><p><strong>4. XULOSA.</strong><br>
  그래서 저는 [주제]이/가 ~아야 한다고 생각합니다. — pozitsiyani mustahkam yopish.</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 [주제] almashtirish metodi (yozishdan tanish):</strong> shu skelet 환경 (ekologiya),
  교육 (ta'lim), 기술 (texnologiya), 건강 — HAR mavzuga tushadi. Skeletni bir marta mukammal
  yodlang, imtihonda faqat mavzu so'zini va dalillarni almashtirasiz. 200 ta shablon emas —
  bitta chuqur quduq!
</div>
"""},
            {"rich_text": """
<h3>🎧 Shablon ishda: to'liq namuna</h3>
<p>Mavzu: 어린이의 스마트폰 사용 (bolalarning telefon ishlatishi). Skelet bo'g'inlarini
sanab eshiting:</p>
""",
             "audio": "topik_s_060_1.mp3",
             "audio_script": [
                 ("남자", "요즘 어린이의 스마트폰 사용에 대한 관심이 높아지고 있습니다. 저는 어린이가 스마트폰을 너무 일찍 사용하는 것에 대해 부정적으로 생각합니다. 첫째, 눈 건강에 나쁘기 때문입니다. 예를 들어 제 조카는 하루에 네 시간씩 스마트폰을 보다가 일곱 살에 안경을 쓰게 되었습니다. 둘째, 아이들이 밖에서 뛰어놀면서 배우는 것들을 놓치기 때문입니다. 물론 교육용 프로그램도 있다는 점은 인정합니다. 하지만 어린 시절에는 화면보다 실제 경험이 더 중요하다고 생각합니다. 그래서 저는 어린이의 스마트폰 사용은 부모가 시간을 정해서 관리해야 한다고 생각합니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — avval o'zingiz aytib ko'ring!</summary>
  <div style="margin-top:10px;">
    <p><strong>요즘 어린이의 스마트폰 사용에 대한 관심이 높아지고 있습니다. 저는 ... 부정적으로 생각합니다.</strong> <span style="background:#dbeafe;padding:1px 8px;border-radius:999px;font-size:.8em;">KIRISH</span><br>
    <em style="color:#475569;">Hozir bolalarning telefon ishlatishiga e'tibor ortmoqda. Men bunga salbiy qarayman.</em></p>
    <p><strong>첫째, 눈 건강에 나쁘기 때문입니다. 예를 들어 제 조카는...</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">1-DALIL</span><br>
    <em style="color:#475569;">Birinchidan, ko'z salomatligiga zarar. Masalan, jiyanim kuniga to'rt soat qarab, yetti yoshida ko'zoynak taqadigan bo'ldi.</em></p>
    <p><strong>둘째, ... 놓치기 때문입니다. 물론 교육용 프로그램도 있다는 점은 인정합니다. 하지만...</strong> <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.8em;">2-DALIL+MUVOZANAT</span><br>
    <em style="color:#475569;">Ikkinchidan, tashqarida o'ynab o'rganadigan narsalarni boy beradi. Albatta, ta'limiy dasturlar borligini tan olaman. Lekin bolalikda ekran emas, jonli tajriba muhimroq.</em></p>
    <p><strong>그래서 저는 ... 부모가 시간을 정해서 관리해야 한다고 생각합니다.</strong> <span style="background:#fae8ff;padding:1px 8px;border-radius:999px;font-size:.8em;">XULOSA</span><br>
    <em style="color:#475569;">Shuning uchun bolaning telefon vaqtini ota-ona belgilab boshqarishi kerak deb o'ylayman.</em></p>
  </div>
</details>
<p>Sanang: 9 jumla, 4 bo'g'in, bitta jonli misol (조카 — jiyan!), bitta muvozanat burilishi.
Bu — 6-topshiriqning to'liq bal qolipi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> "물론 ~는 점도 있지만" jumlasi javobga nima beradi?</p>
""",
             "choices": [
                 {"text": "Qarshi tomonni ham ko'rganingizni ko'rsatadi — fikr yetuk eshitiladi", "is_correct": True},
                 {"text": "Pozitsiyani o'zgartiradi", "is_correct": False},
                 {"text": "Vaqtni to'ldiradi xolos", "is_correct": False},
                 {"text": "Savolni takrorlaydi", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: bir tomonlama fikr — boshlang'ich daraja; qarshi dalilni tan olib, baribir o'z
pozitsiyasida qolgan fikr — yuqori daraja. O'qish 태도 va tinglash 47–50 darslaridagi
"muvozanatli notiq"ning og'zaki versiyasi. Bitta jumla — bir daraja yuqoriga.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">관심이 높아지다</div><div class="pp-card-back">e'tibor ortmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">긍정적/부정적</div><div class="pp-card-back">ijobiy/salbiy</div></div>
  <div class="pp-card"><div class="pp-card-front">놓치다</div><div class="pp-card-back">boy bermoq, qo'ldan chiqarmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">인정하다</div><div class="pp-card-back">tan olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">조카</div><div class="pp-card-back">jiyan</div></div>
  <div class="pp-card"><div class="pp-card-front">교육용</div><div class="pp-card-back">ta'limga mo'ljallangan</div></div>
  <div class="pp-card"><div class="pp-card-front">경험</div><div class="pp-card-back">tajriba</div></div>
  <div class="pp-card"><div class="pp-card-front">관리하다</div><div class="pp-card-back">boshqarmoq, nazorat qilmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Q6 = og'zaki 쓰기 54: KIRISH → 1-DALIL → 2-DALIL+muvozanat → XULOSA.</li>
  <li>Bitta shablon + [주제] almashtirish — 200 emas, BIR chuqur quduq.</li>
  <li>물론 ~지만 muvozanati — darajani ko'taradigan bitta jumla.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 61) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC_Q6,
        "title":   "TOPIK 말하기 Q6-2: Dalillar ombori — to'rt universal kalit",
        "summary": "Deyarli har mavzuga tushadigan dalil turlari: salomatlik, munosabatlar, vaqt-pul, kelajak — va ikkinchi to'liq namuna.",
        "order":   61,
        "blocks": [
            {"rich_text": """
<h2>🧱 Dalillar ombori: to'rt universal kalit</h2>
<p>Skeletingiz bor. Endi eng qiyin savol: imtihonda dalil qayerdan topiladi? Sir: ijtimoiy
mavzularning 90% i shu <strong>to'rt dalil turi</strong>dan ochiladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>💪 SALOMATLIK:</strong> ~은/는 건강에 좋은/나쁜 영향을 줍니다. — deyarli hamma narsa salomatlikka tegadi!</p>
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>🤝 MUNOSABATLAR:</strong> ~(으)면 가족/친구와 보내는 시간이 늘어납니다/줄어듭니다.</p>
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>⏰ VAQT-PUL:</strong> ~은/는 시간과 돈을 아낄 수 있게 해 줍니다. / ~에는 비용이 많이 듭니다.</p>
  <p style="font-size:1.05em;margin:0;"><strong>🌱 KELAJAK:</strong> 지금 ~지 않으면 미래에 더 큰 문제가 될 수 있습니다.</p>
</div>
<p>Mavzu qanday bo'lmasin — 재택근무 (uydan ishlash), 일회용품 (bir martalik idishlar),
조기 교육 — to'rt kalitdan kamida ikkitasi eshikni ochadi. Tayyorlanish vaqtida o'zingizga
savol bering: <strong>"salomatlik? munosabat? vaqt-pul? kelajak?"</strong> — ikkitasini
tanlang, dalillar tayyor.</p>
"""},
            {"rich_text": """
<h3>🎧 Ikkinchi namuna: 재택근무 (uydan ishlash)</h3>
<p>Qaysi ikki kalit ishlatilganini toping:</p>
""",
             "audio": "topik_s_061_1.mp3",
             "audio_script": [
                 ("남자", "요즘 재택근무에 대한 관심이 높아지고 있습니다. 저는 재택근무에 대해 긍정적으로 생각합니다. 첫째, 출퇴근 시간을 아낄 수 있기 때문입니다. 왕복 두 시간을 아끼면 그 시간에 운동도 하고 가족과 저녁도 먹을 수 있습니다. 둘째, 스트레스가 줄어서 건강에 좋기 때문입니다. 만원 버스와 지하철은 생각보다 사람을 지치게 합니다. 물론 집에서 일하면 동료와의 소통이 어려워진다는 점도 있습니다. 하지만 화상 회의 기술이 발전해서 이 문제는 점점 해결되고 있다고 생각합니다. 그래서 저는 회사들이 재택근무를 더 많이 도입해야 한다고 생각합니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>첫째, 출퇴근 시간을 아낄 수 있기 때문입니다.</strong> <span style="background:#fef3c7;padding:1px 8px;border-radius:999px;font-size:.8em;">⏰ VAQT</span><br>
    <em style="color:#475569;">Birinchidan, qatnov vaqtini tejash mumkin. Borish-kelishdagi ikki soatda sport ham, oila bilan kechki ovqat ham bo'ladi (🤝 munosabat bonusi!).</em></p>
    <p><strong>둘째, 스트레스가 줄어서 건강에 좋기 때문입니다.</strong> <span style="background:#dcfce7;padding:1px 8px;border-radius:999px;font-size:.8em;">💪 SALOMATLIK</span><br>
    <em style="color:#475569;">Ikkinchidan, stress kamayib, salomatlikka foyda. Tiqilinch avtobus-metro odamni o'ylagandan ko'proq charchatadi.</em></p>
    <p><strong>물론 동료와의 소통이 어려워진다는 점도 있습니다. 하지만 화상 회의 기술이 발전해서...</strong><br>
    <em style="color:#475569;">Albatta, hamkasblar bilan muloqot qiyinlashadi degan jihat bor. Lekin videokonferensiya rivojlanib, bu muammo hal bo'lmoqda (muvozanat + yechim!).</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Pro-daraja:</strong> muvozanat jumlasiga <strong>yechim</strong> qo'shildi
  (기술이 발전해서 해결되고 있다) — qarshi dalilni tan olish + uni yumshatish. Bu
  6-topshiriqning eng baland pilotaji.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> Mavzu: 일회용품 사용 (bir martalik idishlar). To'rt kalitdan qaysi juftlik eng tabiiy?</p>
""",
             "choices": [
                 {"text": "Kelajak (미래에 더 큰 문제) + vaqt-pul (편리하지만 환경 비용)", "is_correct": True},
                 {"text": "Munosabatlar + salomatlik faqat", "is_correct": False},
                 {"text": "Hech qaysi kalit tushmaydi", "is_correct": False},
                 {"text": "To'rttasini ham bitta javobda ishlatish shart", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: ekologik mavzuga "kelajak" kaliti eng kuchli (지금 줄이지 않으면 미래에...) +
qulaylik-narx muvozanati. ④ — yo'q: 2–3 daqiqaga IKKITA dalil ideal; to'rttasini tiqish —
sayoz quduqlar. Tanlang, chuqur qazing.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">재택근무</div><div class="pp-card-back">uydan ishlash</div></div>
  <div class="pp-card"><div class="pp-card-front">출퇴근</div><div class="pp-card-back">ishga qatnov</div></div>
  <div class="pp-card"><div class="pp-card-front">왕복</div><div class="pp-card-back">borish-kelish</div></div>
  <div class="pp-card"><div class="pp-card-front">지치게 하다</div><div class="pp-card-back">charchatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">소통</div><div class="pp-card-back">muloqot</div></div>
  <div class="pp-card"><div class="pp-card-front">화상 회의</div><div class="pp-card-back">videokonferensiya</div></div>
  <div class="pp-card"><div class="pp-card-front">도입하다</div><div class="pp-card-back">joriy etmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">일회용품</div><div class="pp-card-back">bir martalik buyumlar</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>To'rt universal kalit: salomatlik · munosabatlar · vaqt-pul · kelajak.</li>
  <li>Ikkita kalit tanlang — to'rttasini emas: chuqurlik kenglikdan qimmat.</li>
  <li>Pro-daraja: muvozanat + yechim (물론 ~지만, 기술이 발전해서...).</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 62) ───────────────────────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC_Q6,
        "title":   "TOPIK 말하기 Q6-3: To'liq amaliyot — ikki katta mavzu",
        "summary": "Ikki imtihon mavzusi: SNS ning yoshlarga ta'siri va konvert-kitob (종이책 vs 전자책) — o'zingiz gapirasiz, keyin namuna.",
        "order":   62,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: minbar sizniki</h2>
<p>Tartib: mavzuni o'qing → 60–90 soniya reja (skelet + ikki kalit) → yozib 2 daqiqa
gapiring → namunani eshitib soya qiling.</p>
<h3>1-mavzu</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>SNS(소셜 미디어)가 청소년에게 주는 영향에 대해
  어떻게 생각합니까?</strong> — Ijtimoiy tarmoqlarning o'smirlarga ta'siri haqida fikringiz?</p>
</div>
<p>Avval o'zingiz — 2 daqiqa! Keyin namuna:</p>
""",
             "audio": "topik_s_062_1.mp3",
             "audio_script": [
                 ("남자", "요즘 청소년의 SNS 사용에 대한 관심이 높아지고 있습니다. 저는 SNS가 청소년에게 나쁜 영향을 더 많이 준다고 생각합니다. 첫째, 다른 사람과 자신을 비교하게 되기 때문입니다. SNS에는 행복한 모습만 올라오기 때문에, 그것을 보는 청소년은 자기 생활이 초라하다고 느끼기 쉽습니다. 둘째, 잠을 자야 할 시간을 빼앗기 때문입니다. 밤늦게까지 짧은 영상을 보다 보면 수면이 부족해져서 건강과 공부에 모두 나쁜 영향을 줍니다. 물론 SNS로 새로운 정보를 얻고 친구를 사귈 수 있다는 점도 인정합니다. 하지만 청소년 시기에는 잃는 것이 더 많다고 생각합니다. 그래서 저는 청소년의 SNS 사용 시간을 스스로 정하는 교육이 필요하다고 생각합니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>첫째, 다른 사람과 자신을 비교하게 되기 때문입니다.</strong><br><em style="color:#475569;">Birinchidan, o'zini boshqalar bilan solishtiradigan bo'lib qoladi. Tarmoqda faqat baxtli lahzalar chiqadi — ko'rgan o'smir o'z hayotini bechora his qilishi oson.</em></p>
    <p><strong>둘째, 잠을 자야 할 시간을 빼앗기 때문입니다.</strong><br><em style="color:#475569;">Ikkinchidan, uyqu vaqtini o'g'irlaydi. Yarim tungacha kalta videolar ko'raverib, uyqu kamayadi — salomatlikka ham, o'qishga ham zarar (💪 kalit!).</em></p>
    <p><strong>물론 ... 인정합니다. 하지만 청소년 시기에는 잃는 것이 더 많다고 생각합니다.</strong><br><em style="color:#475569;">Albatta, yangi ma'lumot va do'stlar borligini tan olaman. Lekin o'smirlikda yo'qotish ko'proq deb o'ylayman.</em></p>
    <p><strong>그래서 저는 ... 스스로 정하는 교육이 필요하다고 생각합니다.</strong><br><em style="color:#475569;">Shuning uchun o'smir o'z vaqtini O'ZI belgilashga o'rgatadigan ta'lim kerak deb hisoblayman (taqiq emas — tarbiya: Q4 dagi "금지보다 약속"ning katta akasi!).</em></p>
  </div>
</details>
<h3>2-mavzu</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>종이책과 전자책 중 무엇이 더 좋다고 생각합니까?</strong>
  — Qog'oz kitob va elektron kitobdan qaysi biri yaxshiroq deb o'ylaysiz?</p>
</div>
<p>Yana avval o'zingiz! Keyin namuna:</p>
""",
             "audio": "topik_s_062_2.mp3",
             "audio_script": [
                 ("남자", "요즘 전자책을 읽는 사람이 많아지면서 종이책과 전자책에 대한 이야기가 자주 나옵니다. 저는 종이책이 더 좋다고 생각합니다. 첫째, 내용이 기억에 더 오래 남기 때문입니다. 종이를 넘기면서 읽으면 손과 눈이 함께 기억해서, 시험공부를 할 때도 종이책이 더 효과적이었습니다. 둘째, 눈이 덜 피곤하기 때문입니다. 하루 종일 화면을 보는 우리에게 종이책은 눈이 쉬는 시간이 됩니다. 물론 전자책은 가지고 다니기 편하고 가격도 싸다는 장점이 있습니다. 하지만 저에게 책을 읽는 시간은 화면에서 벗어나는 소중한 시간입니다. 그래서 저는 전자책 시대에도 종이책은 계속 사랑받을 것이라고 생각합니다."),
             ]},
            {"rich_text": """
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima</summary>
  <div style="margin-top:10px;">
    <p><strong>첫째, 내용이 기억에 더 오래 남기 때문입니다.</strong><br><em style="color:#475569;">Birinchidan, mazmun xotirada uzoqroq qoladi — varaqlab o'qiganda qo'l va ko'z birga eslaydi (shaxsiy tajriba misoli bilan!).</em></p>
    <p><strong>둘째, 눈이 덜 피곤하기 때문입니다.</strong><br><em style="color:#475569;">Ikkinchidan, ko'z kamroq charchaydi. Kun bo'yi ekranga qaraydigan bizga qog'oz kitob — ko'z dam oladigan vaqt.</em></p>
    <p><strong>물론 전자책은 가지고 다니기 편하고 가격도 싸다는 장점이 있습니다. 하지만...</strong><br><em style="color:#475569;">Albatta, e-kitob qulay va arzon. Lekin men uchun kitob o'qish — ekrandan qutuladigan qadrli vaqt.</em></p>
  </div>
</details>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Sezdingizmi?</strong> Bu mavzu 중심 생각 tinglash darsidagi suhbatning o'zi
  (종이책으로 읽어야 기억에 남는다!) — kurs bo'ylab bilimlar bir-birini quvvatlayapti.
  O'qigan, eshitgan, yozgan narsangiz endi og'zingizdan chiqyapti. Bu — chuqur quduq!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot.</strong> Q6 javobingizni tekshiradigan BESH savol qaysi qatorda?</p>
""",
             "choices": [
                 {"text": "Pozitsiya aniqmi? Ikki dalil bormi? Misol keltirdimmi? Muvozanat jumlasi bormi? Xulosa pozitsiyani yopdimi?", "is_correct": True},
                 {"text": "Uzun gapirdimmi? Qiyin so'z ishlatdimmi? Tez gapirdimmi? Baland gapirdimmi? Chiroyli gapirdimmi?", "is_correct": False},
                 {"text": "Mavzu kimniki? Savol nechanchi? Ball qancha? Vaqt qancha? Xona qayerda?", "is_correct": False},
                 {"text": "Hammaga yoqdimi? To'g'ri javob qaysi? G'olib kim? Statistika qani? Manba qani?", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: beshta katak — skeletning o'zi. Muhimi: Q6 da "to'g'ri javob" YO'Q — qaysi
pozitsiyani olsangiz ham, uni aniq, asosli va muvozanatli aytsangiz — ball sizniki.
Q6 tayyor: oxirgi bekat — katta final! 🏆</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">비교하다</div><div class="pp-card-back">solishtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">초라하다</div><div class="pp-card-back">bechorahol, arzimas</div></div>
  <div class="pp-card"><div class="pp-card-front">빼앗다</div><div class="pp-card-back">tortib olmoq, o'g'irlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">스스로</div><div class="pp-card-back">o'zi, mustaqil</div></div>
  <div class="pp-card"><div class="pp-card-front">종이책 / 전자책</div><div class="pp-card-back">qog'oz / elektron kitob</div></div>
  <div class="pp-card"><div class="pp-card-front">장점</div><div class="pp-card-back">afzallik</div></div>
  <div class="pp-card"><div class="pp-card-front">벗어나다</div><div class="pp-card-back">qutulmoq, chiqib ketmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">사랑받다</div><div class="pp-card-back">sevilmoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Q6 da to'g'ri javob yo'q — aniq pozitsiya + ikki dalil + muvozanat = ball.</li>
  <li>Shaxsiy misol (조카, 시험공부...) statistikadan kuchli — sizning hayotingiz yetarli manba.</li>
  <li>Skeletni har hafta bitta yangi mavzuga qo'llang — imtihongacha quduq chuqurlashadi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 70) — Grand review ───────────────────────────────
    {
        "skill":   "speaking",
        "topic":   TOPIC_REVIEW,
        "title":   "TOPIK 말하기 총정리: Katta final — olti topshiriq ketma-ket",
        "summary": "Yakuniy simulyatsiya: barcha olti topshiriq imtihon tartibida — har biriga formula eslatmasi va namunaviy javob.",
        "order":   70,
        "blocks": [
            {"rich_text": """
<h2>🏆 Katta final: to'liq imtihon simulyatsiyasi</h2>
<p>Barcha olti topshiriq — imtihondagi tartibda. Har birida: topshiriqni o'qing/eshiting →
formulani eslang → yozib gapiring → namuna bilan solishtiring. Hammasi tugagach, o'zingizga
haqiqat bilan baho bering: qaysi topshiriqda qoqildingiz? O'sha topic darsiga qayting.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Olti formula — bir qarashda:</strong><br>
  <strong>Q1</strong> javob→sabab→misol · <strong>Q2</strong> murojaat→vaziyat→iltimos→detal ·
  <strong>Q3</strong> sahna→그런데→그래서→his · <strong>Q4</strong> tan ol→fikr→sabab→taklif ·
  <strong>Q5</strong> kirish→raqamlar→sabab/istiqbol · <strong>Q6</strong> pozitsiya→2 dalil→muvozanat→xulosa
</div>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Q1 · 질문에 대답하기</span></p>
""",
             "audio": "topik_s_070_1.mp3",
             "audio_script": [
                 ("여자", "일 년 중에서 언제를 가장 좋아합니까? 이야기해 보세요."),
                 ("남자", "저는 삼월을 가장 좋아합니다. 새 학기가 시작되어서 새로운 사람들을 만날 수 있기 때문입니다. 작년 삼월에는 지금 제일 친한 친구를 처음 만났습니다. 그래서 저에게 삼월은 시작의 달입니다."),
             ]},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Q2 · 역할 수행하기</span> — 도서관에서 책을 못 찾았습니다. 사서에게 부탁해 보세요.</p>
""",
             "audio": "topik_s_070_2.mp3",
             "audio_script": [
                 ("남자", "저기요, 안녕하세요. 책을 한 권 찾고 있는데요. 컴퓨터에는 있다고 나오는데 책장에서 못 찾겠어요. 제목은 한국어 문법 사전이고요. 혹시 어디에 있는지 확인해 주시겠어요? 네, 감사합니다!"),
             ]},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Q3 · 그림 보고 이야기하기</span></p>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 140px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:10px;text-align:center;"><div style="font-size:1.8em;">🎂🛒</div><p style="margin:4px 0 0;font-size:.8em;"><strong>①</strong> 케이크를 샀어요</p></div>
  <div style="flex:1 1 140px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:10px;text-align:center;"><div style="font-size:1.8em;">🚌💨</div><p style="margin:4px 0 0;font-size:.8em;"><strong>②</strong> 버스를 놓쳤어요</p></div>
  <div style="flex:1 1 140px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:10px;text-align:center;"><div style="font-size:1.8em;">🏃🎂</div><p style="margin:4px 0 0;font-size:.8em;"><strong>③</strong> 뛰어갔어요</p></div>
  <div style="flex:1 1 140px;background:#fffbeb;border:1px solid #fde68a;border-radius:12px;padding:10px;text-align:center;"><div style="font-size:1.8em;">🎉😅</div><p style="margin:4px 0 0;font-size:.8em;"><strong>④</strong> 늦었지만 도착했어요</p></div>
</div>
""",
             "audio": "topik_s_070_3.mp3",
             "audio_script": [
                 ("남자", "어느 날 저녁, 유진 씨는 친구의 생일 파티에 가려고 케이크를 샀습니다. 그런데 케이크를 사는 동안 버스가 떠나 버렸습니다. 다음 버스는 삼십 분 후에 있어서 유진 씨는 케이크를 들고 뛰어가기 시작했습니다. 결국 파티에 조금 늦었지만, 친구는 땀을 흘리며 도착한 유진 씨를 보고 크게 웃으며 고마워했습니다. 유진 씨는 힘들었지만 마음이 따뜻해졌습니다."),
             ]},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Q4 · 대화 완성하기</span></p>
""",
             "audio": "topik_s_070_4.mp3",
             "audio_script": [
                 ("여자", "저는 여행 갈 때 계획을 세우지 않고 그냥 떠나는 게 좋아요. 계획을 세우면 일하는 것 같잖아요."),
                 ("남자", "아, 그런 여행도 매력이 있지요. 그런데 저는 조금 다르게 생각해요. 왜냐하면 계획이 없으면 유명한 곳을 예약하지 못해서 시간을 낭비할 수 있기 때문이에요. 실제로 저는 예약을 안 하고 갔다가 두 시간을 줄에서 서 있었던 적이 있어요. 그러니까 큰 계획만 세우고 나머지는 자유롭게 다니는 게 어떨까요?"),
             ]},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Q5 · 자료 해석하기</span></p>
<div style="background:#fff;border:1px solid #e2e8f0;border-radius:12px;padding:16px;margin:12px 0;">
  <p style="font-weight:700;text-align:center;margin:0 0 10px;">외국인 관광객 수의 변화</p>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2020년</span><div style="height:22px;background:#93c5fd;border-radius:4px;width:20%;"></div><span style="font-size:.85em;">200만 명</span></div>
  <div style="display:flex;align-items:baseline;gap:6px;margin:4px 0;"><span style="width:70px;font-size:.85em;">2025년</span><div style="height:22px;background:#3b82f6;border-radius:4px;width:80%;"></div><span style="font-size:.85em;">800만 명</span></div>
  <p style="font-size:.8em;color:#64748b;margin:10px 0 0;">원인: ① 한류 인기 ② 항공 노선 확대</p>
</div>
""",
             "audio": "topik_s_070_5.mp3",
             "audio_script": [
                 ("남자", "이 자료는 외국인 관광객 수의 변화를 조사한 것입니다. 외국인 관광객은 이천이십 년에 이백만 명이었는데, 이천이십오 년에는 팔백만 명으로 네 배나 증가했습니다. 이러한 변화의 원인은 두 가지입니다. 첫째, 한류가 세계적으로 인기를 얻었기 때문입니다. 둘째, 항공 노선이 확대되었기 때문입니다. 앞으로도 관광객 수는 계속 늘어날 것으로 보입니다."),
             ]},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">Q6 · 의견 제시하기</span> — 주제: 아르바이트를 하면서 공부하는 것 (o'qish bilan birga ishlash)</p>
""",
             "audio": "topik_s_070_6.mp3",
             "audio_script": [
                 ("남자", "요즘 아르바이트를 하면서 공부하는 학생이 많아지고 있습니다. 저는 이것에 대해 긍정적으로 생각합니다. 첫째, 돈의 소중함을 배울 수 있기 때문입니다. 직접 번 돈은 쉽게 쓰지 않게 됩니다. 둘째, 사회 경험을 쌓을 수 있기 때문입니다. 손님을 대하면서 배우는 것은 교과서에 없는 공부입니다. 물론 아르바이트 때문에 공부할 시간이 줄어든다는 점도 있습니다. 하지만 시간을 잘 관리하면 두 가지를 모두 잘할 수 있다고 생각합니다. 그래서 저는 학생 시절의 아르바이트는 좋은 경험이 된다고 생각합니다."),
             ]},
            {"rich_text": """
<p><strong>Yakuniy amaliyot.</strong> Butun kurs bo'yicha: gapirish imtihonining uch oltin qoidasi qaysi?</p>
""",
             "choices": [
                 {"text": "Hech qachon jim qolma · formulaga tayan · yodlangan jumlani og'iz bilan mashq qil", "is_correct": True},
                 {"text": "Tez gapir · qiyin so'z ishlat · uzun javob ber", "is_correct": False},
                 {"text": "Faqat rost gapir · statistika keltir · baholovchini kuldir", "is_correct": False},
                 {"text": "Bir uslubda gapir · savolni takrorla · oxirida uzr so'ra", "is_correct": False},
             ],
             "explanation": """
<p>✅ ①: kursning uch ustuni. Oqim uzilmasin (sodda bo'lsa ham gapir!), har topshiriqning
formulasi bor (o'ylash emas — to'ldirish!), va og'iz mashq qilgan jumla o'zi chiqadi
(soya + 3 kun metodi). Imtihonda ko'rishguncha — 화이팅, kelajak topikchi! 🏆🎤</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">사서</div><div class="pp-card-back">kutubxonachi</div></div>
  <div class="pp-card"><div class="pp-card-front">땀을 흘리다</div><div class="pp-card-back">terlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">낭비하다</div><div class="pp-card-back">isrof qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">한류</div><div class="pp-card-back">hallyu (koreys madaniyati to'lqini)</div></div>
  <div class="pp-card"><div class="pp-card-front">항공 노선</div><div class="pp-card-back">aviaqatnov yo'nalishi</div></div>
  <div class="pp-card"><div class="pp-card-front">소중함</div><div class="pp-card-back">qadr-qimmat</div></div>
  <div class="pp-card"><div class="pp-card-front">경험을 쌓다</div><div class="pp-card-back">tajriba to'plamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">대하다</div><div class="pp-card-back">muomala qilmoq</div></div>
</div>
<h3>Xulosa — BUTUN KURS bo'yicha 🏆</h3>
<ul>
  <li><strong>Olti topshiriq — olti formula:</strong> hammasi yodingizda bo'lsin (yuqoridagi eslatma-kartani saqlang!).</li>
  <li><strong>Kunlik mashq:</strong> kuniga 3 jumla soya (3 kun × 3 marta) + haftasiga bitta to'liq topshiriq yozib solishtirish.</li>
  <li><strong>Kurs xaritasi:</strong> o'qish shablonlari → yozishda, yozish shablonlari → gapirishda, tinglash quloq mashqi → soya metodida. Hammasi bitta chuqur quduq: koreys tili. 💧</li>
  <li>화이팅, chempion! 🎤🇰🇷</li>
</ul>
"""},
        ],
    },
]
