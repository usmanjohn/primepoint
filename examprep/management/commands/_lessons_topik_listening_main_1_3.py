# TOPIK II Listening — 17–20-savollar: Asosiy fikr (중심 생각), lessons 1–3 (orders 50–52).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_main_1_3.py \
#            --out examprep/management/commands/audio/main
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_main_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/main

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "17–20-savollar: Asosiy fikr (중심 생각)",
    "summary": "Erkakning ASOSIY fikrini topish: fikr qoliplari (-는 게 좋다, -아야 하다) va misol-tafsilotni fikrdan ajratish.",
    "icon":    "bi-bullseye",
    "order":   6,
}

LESSONS = [
    # ── Lesson 1 (order 50) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 중심 생각 1: 17–20-savollar bilan tanishuv — erkakning fikri",
        "summary": "중심 생각 savolining tuzilishi: deyarli doim ERKAKNING fikri so'raladi; fikrni fosh qiluvchi tugallanmalar lug'ati.",
        "order":   50,
        "blocks": [
            {"rich_text": """
<h2>🎯 17–20-savollar: erkak aslida nima demoqchi?</h2>
<p>Bu guruhda qisqa suhbat eshitiladi va savol shunday bo'ladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>17–20.</strong> 다음을 듣고 <u>남자의</u> 중심 생각으로
  가장 알맞은 것을 고르십시오. — <em>Eshitib, ERKAKNING asosiy fikrini tanlang.</em></p>
</div>
<p>E'tibor bering: deyarli har doim <strong>남자 (erkak)</strong>ning fikri so'raladi! Odatiy
ssenariy: ayol biror narsa qiladi yoki aytadi → erkak bunga <strong>o'z qarashini</strong>
bildiradi. Ayolning gapi — sahna, erkakning gapi — javob.</p>
<h3>Fikrni fosh qiluvchi tugallanmalar</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>-는 게 좋아요 / -는 게 좋을 것 같아요</strong> — …gan yaxshi (yumshoq maslahat)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>-아/어야 해요 / -아/어야지요</strong> — …ish kerak (qat'iy fikr)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>제 생각에는 / 저는 ~다고 생각해요</strong> — mening fikrimcha</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>-으면 좋겠어요</strong> — …sa yaxshi bo'lardi (istak)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>-을 필요는 없어요</strong> — …ish shart emas (rad fikri)</p>
  <p style="font-size:1.05em;margin:0;"><strong>왜 ~지 않아요? / ~잖아요</strong> — nega …masiz? / axir …ku (bilvosita fikr)</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Fikr ko'pincha erkakning <strong>oxirgi replikasida</strong>,
  ko'pincha <strong>그래도/하지만</strong>dan keyin turadi. Erkak avval rozi bo'lib (맞아요,
  편리하지요) keyin "lekin" desa — asosiy fikr aynan "lekin"dan keyingisi. Bu sizga
  o'qishdagi 중심 생각 usulini eslatadimi? Xuddi o'sha — faqat quloq bilan!
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: birga tahlil qilamiz</h3>
<p>Eshiting va erkakning gapidan <strong>fikr tugallanmasini</strong> ushlang.</p>
""",
             "audio": "topik_l_050_1.mp3",
             "audio_script": [
                 ("여자", "이 옷 어제 샀는데 벌써 단추가 떨어졌어요. 그냥 입을까 봐요."),
                 ("남자", "산 지 하루밖에 안 됐잖아요. 가게에 가서 바꿔 달라고 하는 게 좋을 것 같아요."),
             ]},
            {"rich_text": """
<p>Erkakning replikasini ikkiga bo'lamiz:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;">산 지 하루밖에 안 됐<strong>잖아요</strong> — "axir olganingga bir kun bo'ldi-ku" (asos)</p>
  <p style="font-size:1.05em;margin:0;">바꿔 달라고 하는 <strong>게 좋을 것 같아요</strong> — "almashtirib berishlarini so'ragan yaxshi" (FIKR ✅)</p>
</div>
<p>Asosiy fikr: <strong>kiyimni almashtirishga borish kerak</strong>. "Tugma tushib qoldi"
(fakt) yoki "kiyim kecha olingan" (asos) — fikr emas, ular fikrni <strong>qo'llab-quvvatlaydi</strong>.
Variantlarda ana shular ham turadi — adashtirmang!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 이 옷 어제 샀는데 벌써 단추가 떨어졌어요. 그냥 입을까 봐요.<br>
    <em style="color:#475569;">Bu kiyimni kecha olgandim, tugmasi allaqachon tushib qoldi. Shundayligicha kiyaversam devdim.</em></p>
    <p><strong>남자:</strong> 산 지 하루밖에 안 됐잖아요. 가게에 가서 바꿔 달라고 하는 게 좋을 것 같아요.<br>
    <em style="color:#475569;">Axir olganingizga bir kun ham bo'lmadi-ku. Do'konga borib, almashtirib berishlarini so'ragan ma'qul.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_050_2.mp3",
             "audio_script": [
                 ("남자", "요즘도 밤늦게까지 회사에 남아서 일해요?"),
                 ("여자", "네, 할 일이 많아서 어쩔 수 없어요."),
                 ("남자", "그래도 건강이 먼저지요. 일도 중요하지만 쉬는 시간이 꼭 필요해요."),
             ],
             "choices": [
                 {"text": "일보다 건강과 휴식이 먼저다. (Ishdan ko'ra sog'liq va dam olish muhimroq.)", "is_correct": True},
                 {"text": "밤늦게까지 일해야 성공할 수 있다. (Muvaffaqiyat uchun yarim tungacha ishlash kerak.)", "is_correct": False},
                 {"text": "할 일이 많으면 쉬면 안 된다. (Ish ko'p bo'lsa dam olmaslik kerak.)", "is_correct": False},
                 {"text": "여자는 일을 그만둬야 한다. (Ayol ishdan ketishi kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Fikr qolipi ikki marta: 건강이 <strong>먼저지요</strong> + 쉬는 시간이 꼭
<strong>필요해요</strong> → <mark style="background:#dcfce7;">sog'liq va dam olish
birinchi</mark> ✅. Erkak <strong>그래도</strong> bilan boshladi — ayolning "iloj yo'q"iga
e'tiroz. ②③ — erkak fikrining teskarisi, ④ — haddan oshirilgan: u dam olishni aytdi,
ishdan ketishni emas ("keskin" variantlar bu yerda ham tuzoq!).</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 요즘도 밤늦게까지 회사에 남아서 일해요?<br>
    <em style="color:#475569;">Hali ham yarim tungacha ishxonada qolib ishlayapsizmi?</em></p>
    <p><strong>여자:</strong> 네, 할 일이 많아서 어쩔 수 없어요.<br>
    <em style="color:#475569;">Ha, ish ko'p, ilojim yo'q.</em></p>
    <p><strong>남자:</strong> 그래도 건강이 먼저지요. 일도 중요하지만 쉬는 시간이 꼭 필요해요.<br>
    <em style="color:#475569;">Baribir sog'liq birinchi-da. Ish ham muhim, lekin dam olish vaqti albatta kerak.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_050_3.mp3",
             "audio_script": [
                 ("여자", "아이 생일 선물로 뭘 사 줘야 할지 모르겠어요."),
                 ("남자", "물건을 먼저 고르지 말고 아이한테 뭘 갖고 싶은지 물어보세요. 아이의 생각을 듣는 게 제일 중요하니까요."),
             ],
             "choices": [
                 {"text": "아이에게 먼저 물어보는 것이 중요하다. (Avval bolaning o'zidan so'rash muhim.)", "is_correct": True},
                 {"text": "생일 선물은 비쌀수록 좋다. (Tug'ilgan kun sovg'asi qanchalik qimmat bo'lsa, shuncha yaxshi.)", "is_correct": False},
                 {"text": "아이에게 선물을 사 줄 필요가 없다. (Bolaga sovg'a olib berish shart emas.)", "is_correct": False},
                 {"text": "부모가 선물을 정하는 것이 빠르다. (Sovg'ani ota-ona belgilagani tezroq.)", "is_correct": False},
             ],
             "explanation": """
<p>Fikr qolipi oxirida: 아이의 생각을 듣는 게 <strong>제일 중요하니까요</strong> →
<mark style="background:#dcfce7;">bolaning fikrini eshitish eng muhim</mark> ✅. Struktura
klassik: ayolda muammo → erkakda yechim + sabab (~니까요). ④ erkak aytganining aynan
teskarisi (물건을 먼저 고르지 <strong>말고</strong> — buyumni avval tanlamang!). ~지 말고
(…mang, buning o'rniga) eshitilsa — fikr undan keyingi qismda.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 아이 생일 선물로 뭘 사 줘야 할지 모르겠어요.<br>
    <em style="color:#475569;">Bolamning tug'ilgan kuniga nima olib berishni bilmayapman.</em></p>
    <p><strong>남자:</strong> 물건을 먼저 고르지 말고 아이한테 뭘 갖고 싶은지 물어보세요. 아이의 생각을 듣는 게 제일 중요하니까요.<br>
    <em style="color:#475569;">Avval buyum tanlamang, bolaning o'zidan nimani xohlashini so'rang. Eng muhimi — bolaning fikrini eshitish-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">중심 생각</div><div class="pp-card-back">asosiy fikr</div></div>
  <div class="pp-card"><div class="pp-card-front">단추가 떨어지다</div><div class="pp-card-back">tugma tushib qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">바꿔 달라고 하다</div><div class="pp-card-back">almashtirib berishni so'ramoq</div></div>
  <div class="pp-card"><div class="pp-card-front">어쩔 수 없다</div><div class="pp-card-back">iloji yo'q</div></div>
  <div class="pp-card"><div class="pp-card-front">건강이 먼저다</div><div class="pp-card-back">sog'liq birinchi</div></div>
  <div class="pp-card"><div class="pp-card-front">~지 말고</div><div class="pp-card-back">…mang, buning o'rniga</div></div>
  <div class="pp-card"><div class="pp-card-front">~(으)니까요</div><div class="pp-card-back">chunki …-da (sabab)</div></div>
  <div class="pp-card"><div class="pp-card-front">~잖아요</div><div class="pp-card-back">axir …ku</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>17–20 da deyarli doim <strong>erkakning</strong> fikri so'raladi; ayolning gapi — sahna.</li>
  <li>Fikr tugallanmalari: -는 게 좋다, -아야 하다, 제일 중요하다, -으면 좋겠다, -을 필요는 없다.</li>
  <li>그래도/하지만/-지 말고 dan keyingi qism — fikrning uyi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 51) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 중심 생각 2: Fikr va misolni ajratish — soyabon testi quloqda",
        "summary": "Noto'g'ri variantlar qayerdan keladi: tafsilot (tor), erkak tan olgan yon fikr, haddan oshirilgan xulosa — va soyabon testi.",
        "order":   51,
        "blocks": [
            {"rich_text": """
<h2>☂️ Soyabon testi — endi quloq uchun</h2>
<p>O'qishdagi qoidani eslaysizmi? Asosiy fikr — erkak aytgan <strong>hamma narsani</strong>
yopadigan soyabon. Variantni tekshiring: erkakning butun gapini qamraydimi, yo faqat bitta
bo'lagini?</p>
<h3>Noto'g'ri variantlarning uch turi</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>① Tafsilot (tor).</strong> Erkak keltirgan
  misol yoki fakt — to'g'ri eshitilgan, lekin bu FIKR emas. Misollar 예를 들면 / 저도 ~ㄴ 적이
  있어요 bilan keladi.</p>
  <p style="font-size:1.05em;margin:0 0 8px;"><strong>② Tan olingan yon fikr.</strong> Erkak avval
  rozi bo'ladi (맞아요, 편리하지요 — to'g'ri, qulay-ku) — bu uning asosiy fikri EMAS!
  Asosiysi 하지만dan keyin keladi.</p>
  <p style="font-size:1.05em;margin:0;"><strong>③ Haddan oshirilgan xulosa.</strong> Erkak "kamroq
  qiling" desa, variant "umuman qilmang" deydi — keskinlik qo'shilgan. 절대/무조건 turdagi
  so'zlarga hushyor bo'ling.</p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Savol 남자 haqida ekanini unutmang — <strong>ayolning
  fikri</strong>ni beruvchi variant ham doimiy mehmon. Ayol nima demasin, u faqat fon.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_051_1.mp3",
             "audio_script": [
                 ("여자", "요즘은 스마트폰으로 책을 읽는 사람이 많던데요."),
                 ("남자", "편리하긴 하지요. 하지만 저는 종이책으로 읽어야 내용이 오래 기억에 남는 것 같아요. 그래서 중요한 책은 꼭 종이책으로 사요."),
             ],
             "choices": [
                 {"text": "중요한 내용은 종이책으로 읽는 것이 좋다. (Muhim narsani qog'oz kitobdan o'qigan yaxshi.)", "is_correct": True},
                 {"text": "스마트폰 독서는 편리해서 제일 좋다. (Smartfonda o'qish qulay, shuning uchun eng zo'ri.)", "is_correct": False},
                 {"text": "스마트폰으로 책을 읽으면 절대 안 된다. (Smartfonda kitob o'qish mutlaqo mumkin emas.)", "is_correct": False},
                 {"text": "책을 많이 사는 것이 중요하다. (Kitobni ko'p sotib olish muhim.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkak avval tan oldi: 편리하<strong>긴 하지요</strong> ("qulayligini qulay-ku") — bu ②
tuzoqning manbai, lekin yon fikr! Asosiysi <strong>하지만</strong>dan keyin: 종이책으로
읽어야 기억에 남는다 + 꼭 종이책으로 사요 → ✅ ①. ③ haddan oshirilgan (taqiq yo'q,
shaxsiy afzallik bor — <strong>절대</strong> so'zi qo'shildi!). Formula: 긴 하지요 +
하지만 = fikr keyingisida.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 요즘은 스마트폰으로 책을 읽는 사람이 많던데요.<br>
    <em style="color:#475569;">Hozir smartfonda kitob o'qiydiganlar ko'p ekan.</em></p>
    <p><strong>남자:</strong> 편리하긴 하지요. 하지만 저는 종이책으로 읽어야 내용이 오래 기억에
    남는 것 같아요. 그래서 중요한 책은 꼭 종이책으로 사요.<br>
    <em style="color:#475569;">Qulayligini qulay-ku. Lekin menimcha, qog'oz kitobdan o'qisagina
    mazmun uzoq esda qoladi. Shuning uchun muhim kitoblarni albatta qog'oz variantida olaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_051_2.mp3",
             "audio_script": [
                 ("남자", "마트에 갈 때 왜 항상 장바구니를 가지고 가요?"),
                 ("여자", "비닐봉지를 쓰지 않으려고요. 작은 일이지만요."),
                 ("남자", "멋진데요? 저도 그렇게 해야겠어요. 그런 작은 습관이 환경을 지키는 데 큰 도움이 되니까요."),
             ],
             "choices": [
                 {"text": "작은 습관이 환경을 지키는 데 도움이 된다. (Kichik odat atrof-muhitni asrashga yordam beradi.)", "is_correct": True},
                 {"text": "장바구니를 들고 다니는 것은 불편하다. (Xarid xaltasini olib yurish noqulay.)", "is_correct": False},
                 {"text": "비닐봉지가 더 싸고 편리하다. (Polietilen paket arzonroq va qulayroq.)", "is_correct": False},
                 {"text": "마트에 자주 가지 않는 것이 좋다. (Do'konga kam borgan ma'qul.)", "is_correct": False},
             ],
             "explanation": """
<p>Bu safar ayol qiladi, erkak <strong>xulosa chiqaradi</strong>: 그런 작은 습관이 환경을
지키는 데 큰 도움이 <strong>되니까요</strong> → ✅ ①. E'tibor bering: "저도 그렇게
해야겠어요" (men ham shunday qilaman) — bu qaror, lekin asosiy fikr emas; fikr — NEGA
shunday qilishida (~니까요 sababida). ②③ matnga zid, ④ umuman boshqa mavzu. Soyabon
testi: ① erkakning qarorini ham, sababini ham yopadi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 마트에 갈 때 왜 항상 장바구니를 가지고 가요?<br>
    <em style="color:#475569;">Do'konga borganda nega doim xarid xaltasini olib yurasiz?</em></p>
    <p><strong>여자:</strong> 비닐봉지를 쓰지 않으려고요. 작은 일이지만요.<br>
    <em style="color:#475569;">Polietilen paket ishlatmaslik uchun. Kichik ish bo'lsa ham.</em></p>
    <p><strong>남자:</strong> 멋진데요? 저도 그렇게 해야겠어요. 그런 작은 습관이 환경을 지키는 데 큰 도움이 되니까요.<br>
    <em style="color:#475569;">Zo'r-ku? Men ham shunday qilishim kerak ekan. Bunday kichik odatlar atrof-muhitni asrashga katta yordam beradi-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_051_3.mp3",
             "audio_script": [
                 ("여자", "운동을 시작해도 항상 며칠 못 하고 그만두게 돼요."),
                 ("남자", "처음부터 힘든 운동을 하니까 그래요. 가벼운 산책부터 시작해서 조금씩 늘려 가는 게 좋아요."),
             ],
             "choices": [
                 {"text": "운동은 쉬운 것부터 조금씩 시작하는 것이 좋다. (Sportni yengilidan boshlab, asta-sekin oshirgan yaxshi.)", "is_correct": True},
                 {"text": "운동은 처음부터 힘들게 해야 효과가 있다. (Sport boshidanoq og'ir bo'lsagina foyda beradi.)", "is_correct": False},
                 {"text": "산책은 운동이라고 할 수 없다. (Piyoda yurishni sport deb bo'lmaydi.)", "is_correct": False},
                 {"text": "여자는 운동을 그만두는 것이 좋다. (Ayol sportni tashlagani ma'qul.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkak avval <strong>sababni</strong> aytdi (처음부터 힘든 운동을 하니까 그래요 — diagnostika),
keyin <strong>fikrni</strong>: 산책부터 시작해서 조금씩 늘려 가는 <strong>게 좋아요</strong> →
✅ ①. ② erkak aytganining teskarisi, ③ u aytmagan gap (aksincha, piyoda yurishni sport
sifatida taklif qildi!), ④ absurd. Diagnostika + maslahat strukturasi 17–20 ning eng
sevimli qolipi: javob doim <strong>maslahat</strong> qismida.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 운동을 시작해도 항상 며칠 못 하고 그만두게 돼요.<br>
    <em style="color:#475569;">Sport boshlasam ham har doim bir necha kundan keyin tashlab qo'yaman.</em></p>
    <p><strong>남자:</strong> 처음부터 힘든 운동을 하니까 그래요. 가벼운 산책부터 시작해서 조금씩 늘려 가는 게 좋아요.<br>
    <em style="color:#475569;">Boshdanoq og'ir mashq qilganingiz uchun shunday. Yengil piyoda yurishdan boshlab, asta-sekin oshirib borgan yaxshi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">~긴 하지요</div><div class="pp-card-back">…ligini …-ku (tan olish)</div></div>
  <div class="pp-card"><div class="pp-card-front">기억에 남다</div><div class="pp-card-back">esda qolmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">장바구니</div><div class="pp-card-back">xarid xaltasi</div></div>
  <div class="pp-card"><div class="pp-card-front">비닐봉지</div><div class="pp-card-back">polietilen paket</div></div>
  <div class="pp-card"><div class="pp-card-front">습관</div><div class="pp-card-back">odat</div></div>
  <div class="pp-card"><div class="pp-card-front">환경을 지키다</div><div class="pp-card-back">atrof-muhitni asramoq</div></div>
  <div class="pp-card"><div class="pp-card-front">그만두다</div><div class="pp-card-back">tashlab qo'ymoq, to'xtatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">조금씩 늘리다</div><div class="pp-card-back">asta-sekin oshirmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Uch tuzoq: tafsilot (tor), tan olingan yon fikr (긴 하지요…), haddan oshirilgan xulosa (절대!).</li>
  <li>Soyabon testi: to'g'ri variant erkakning butun gapini yopadi, bitta bo'lagini emas.</li>
  <li>Diagnostika + maslahat qolipida javob — maslahatda (-는 게 좋아요).</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 52) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 중심 생각 3: To'liq amaliyot — to'rtta suhbat imtihondagidek",
        "summary": "17–20-savollar to'liq to'plami: xarid, uyqu, ish o'rgatish va oilaviy tajriba mavzularida erkakning fikrini toping.",
        "order":   52,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 17, 18, 19, 20-savollar</h2>
<p>To'rt suhbat — to'rtta fikr. Har birida: fikr tugallanmasini ushlang (-는 게 좋다,
-아야 하다, 필요는 없다…), 하지만/그래도 burilishini kuzating, soyabon testini qo'llang.
Har audio <strong>bir marta</strong>!</p>
"""},
            {"rich_text": """
<p><strong>17-savol.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_052_1.mp3",
             "audio_script": [
                 ("여자", "어제 세일해서 티셔츠를 다섯 장이나 샀어요."),
                 ("남자", "싸다고 많이 사면 안 입는 옷만 늘어요. 필요한 것만 사는 게 진짜 절약이지요."),
             ],
             "choices": [
                 {"text": "필요한 물건만 사는 것이 진짜 절약이다. (Faqat kerakli narsani olish — haqiqiy tejamkorlik.)", "is_correct": True},
                 {"text": "세일 때 많이 사 두면 이득이다. (Chegirma paytida ko'p olib qo'yish foyda.)", "is_correct": False},
                 {"text": "티셔츠는 다섯 장쯤 있어야 한다. (Futbolka beshta atrofida bo'lishi kerak.)", "is_correct": False},
                 {"text": "옷은 세일 때만 사야 한다. (Kiyimni faqat chegirmada olish kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Fikr tugallanmasi: 필요한 것만 사는 게 진짜 절약<strong>이지요</strong> → ✅ ①. Oldingi
gap — asos: 싸다고 많이 사면 안 입는 옷만 늘어요 (arzon deb ko'p olsang, kiyilmaydigan
kiyim ko'payadi). ② ayol qilgan ishning oqlanishi — erkak aynan shunga e'tiroz bildiryapti!
Ayol tarafdagi variant — 17–20 ning doimiy tuzog'i.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 어제 세일해서 티셔츠를 다섯 장이나 샀어요.<br>
    <em style="color:#475569;">Kecha chegirma bo'lgani uchun beshta futbolka sotib oldim.</em></p>
    <p><strong>남자:</strong> 싸다고 많이 사면 안 입는 옷만 늘어요. 필요한 것만 사는 게 진짜 절약이지요.<br>
    <em style="color:#475569;">Arzon deb ko'p olaversangiz, kiyilmaydigan kiyimlar ko'payadi xolos. Faqat keragini olish — haqiqiy tejamkorlik-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>18-savol.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_052_2.mp3",
             "audio_script": [
                 ("남자", "왜 이렇게 피곤해 보여요?"),
                 ("여자", "어젯밤에 드라마를 보느라 세 시간밖에 못 잤어요."),
                 ("남자", "드라마는 주말에 몰아서 봐도 되잖아요. 잠을 줄이면서까지 볼 필요는 없어요."),
             ],
             "choices": [
                 {"text": "잠을 줄이면서까지 드라마를 볼 필요는 없다. (Uyquni qisqartirib drama ko'rishga hojat yo'q.)", "is_correct": True},
                 {"text": "드라마는 매일 봐야 재미있다. (Drama har kuni ko'rilsagina qiziq.)", "is_correct": False},
                 {"text": "세 시간 자면 충분하다. (Uch soat uxlash yetarli.)", "is_correct": False},
                 {"text": "주말에는 드라마를 보면 안 된다. (Dam olish kunlari drama ko'rmaslik kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Rad fikri qolipi: 볼 <strong>필요는 없어요</strong> → ✅ ①. Yechim ham taklif qilindi:
주말에 몰아서 <strong>봐도 되잖아요</strong> (dam olish kuni yig'ib ko'rsa bo'ladi-ku) —
demak ④ teskari (drama ko'rishga qarshi emas, vaqtiga qarshi!). 몰아서 보다 (yig'ib,
ketma-ket ko'rmoq) — zamonaviy suhbatlarning tez-tez mehmoni.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 왜 이렇게 피곤해 보여요?<br>
    <em style="color:#475569;">Nega bunchalik charchagan ko'rinasiz?</em></p>
    <p><strong>여자:</strong> 어젯밤에 드라마를 보느라 세 시간밖에 못 잤어요.<br>
    <em style="color:#475569;">Kecha drama ko'raman deb uch soatgina uxladim.</em></p>
    <p><strong>남자:</strong> 드라마는 주말에 몰아서 봐도 되잖아요. 잠을 줄이면서까지 볼 필요는 없어요.<br>
    <em style="color:#475569;">Dramani dam olish kuni yig'ib ko'rsa ham bo'ladi-ku. Uyquni qisqartirgunchalik ko'rishga hojat yo'q.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>19-savol.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_052_3.mp3",
             "audio_script": [
                 ("여자", "부장님, 신입 사원 교육을 또 해요? 지난달에 했잖아요."),
                 ("남자", "한 번으로는 부족해요. 새로운 일을 배울 때는 여러 번 반복해야 실수가 줄어들지요."),
             ],
             "choices": [
                 {"text": "교육은 여러 번 반복해야 한다. (O'qitishni bir necha marta takrorlash kerak.)", "is_correct": True},
                 {"text": "신입 사원 교육은 한 번이면 충분하다. (Yangi xodim o'qitishga bir marta yetadi.)", "is_correct": False},
                 {"text": "신입 사원은 실수를 하지 않는다. (Yangi xodimlar xato qilmaydi.)", "is_correct": False},
                 {"text": "교육보다 쉬는 것이 중요하다. (O'qitishdan ko'ra dam olish muhim.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkak (boshliq) ayolning e'tiroziga javob berdi: 한 번으로는 <strong>부족해요</strong> +
여러 번 반복<strong>해야</strong> 실수가 줄어들지요 → ✅ ①. ② — <strong>ayolning</strong>
pozitsiyasi (지난달에 했잖아요 — o'tgan oy qildik-ku!) — savol erkak haqida! Ish
suhbatlarida (부장님…) fikr odatda kattaroq lavozim egasining og'zida bo'ladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 부장님, 신입 사원 교육을 또 해요? 지난달에 했잖아요.<br>
    <em style="color:#475569;">Boshliq, yangi xodimlar o'qitishini yana qilamizmi? O'tgan oy qilgandik-ku.</em></p>
    <p><strong>남자:</strong> 한 번으로는 부족해요. 새로운 일을 배울 때는 여러 번 반복해야 실수가 줄어들지요.<br>
    <em style="color:#475569;">Bir martasi kam. Yangi ishni o'rganayotganda bir necha marta takrorlansagina xatolar kamayadi-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>20-savol.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_052_4.mp3",
             "audio_script": [
                 ("여자", "주말 농장을 신청했다면서요? 채소는 그냥 사 먹는 게 더 싸지 않아요?"),
                 ("남자", "돈으로 보면 그렇지요. 하지만 아이들이 채소가 어떻게 자라는지 직접 보고 배우잖아요. 그런 경험이 돈보다 훨씬 값지다고 생각해요."),
             ],
             "choices": [
                 {"text": "직접 보고 배우는 경험이 돈보다 값지다. (O'z ko'zi bilan ko'rib o'rganish tajribasi puldan qimmatroq.)", "is_correct": True},
                 {"text": "채소는 사 먹는 것이 더 경제적이다. (Sabzavotni sotib olgan tejamliroq.)", "is_correct": False},
                 {"text": "주말 농장은 돈이 너무 많이 든다. (Dam olish kuni fermasi juda qimmatga tushadi.)", "is_correct": False},
                 {"text": "아이들에게 채소를 많이 먹여야 한다. (Bolalarga sabzavotni ko'p yedirish kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Klassik formula to'liq ishladi: tan olish (돈으로 보면 <strong>그렇지요</strong> — pul
jihatidan shunday) + <strong>하지만</strong> + fikr (경험이 돈보다 훨씬 <strong>값지다고
생각해요</strong>) → ✅ ①. ② — ayolning pozitsiyasi + erkak tan olgan yon fikr — ikki
tuzoq bitta variantda! To'rt savolda ham formula bir xil edi: buni endi imtihonda ham
ko'rasiz. 값지다 (qimmatli, qadrli) — 중심 생각 savollarining oltin so'zi. 🎉</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 주말 농장을 신청했다면서요? 채소는 그냥 사 먹는 게 더 싸지 않아요?<br>
    <em style="color:#475569;">Dam olish kuni fermasiga yozilibsiz deb eshitdim? Sabzavotni shunchaki sotib olgan arzonroq emasmi?</em></p>
    <p><strong>남자:</strong> 돈으로 보면 그렇지요. 하지만 아이들이 채소가 어떻게 자라는지 직접
    보고 배우잖아요. 그런 경험이 돈보다 훨씬 값지다고 생각해요.<br>
    <em style="color:#475569;">Pul tomondan qarasa shunday-da. Lekin bolalar sabzavot qanday
    o'sishini o'z ko'zi bilan ko'rib o'rganishadi-ku. Bunday tajriba puldan ancha qimmatli deb
    o'ylayman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">절약</div><div class="pp-card-back">tejamkorlik</div></div>
  <div class="pp-card"><div class="pp-card-front">몰아서 보다</div><div class="pp-card-back">yig'ib (ketma-ket) ko'rmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">신입 사원</div><div class="pp-card-back">yangi xodim</div></div>
  <div class="pp-card"><div class="pp-card-front">반복하다</div><div class="pp-card-back">takrorlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">부족하다</div><div class="pp-card-back">yetarli emas, kam</div></div>
  <div class="pp-card"><div class="pp-card-front">주말 농장</div><div class="pp-card-back">dam olish kuni fermasi</div></div>
  <div class="pp-card"><div class="pp-card-front">값지다</div><div class="pp-card-back">qimmatli, qadrli</div></div>
  <div class="pp-card"><div class="pp-card-front">경험</div><div class="pp-card-back">tajriba</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Formula: (tan olish 그렇지요/긴 하지요) + 하지만 + <strong>FIKR</strong> (-는 게 좋다 / -아야 하다 / 필요는 없다 / 값지다).</li>
  <li>Ayolning pozitsiyasi va erkak tan olgan yon fikr — eng ko'p ishlaydigan ikki tuzoq.</li>
  <li>Soyabon testi quloqda ham ishlaydi: variant butun gapni yopsin, bir bo'lagini emas.</li>
</ul>
"""},
        ],
    },
]
