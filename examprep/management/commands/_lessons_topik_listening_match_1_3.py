# TOPIK II Listening — 13–16-savollar: Mazmun mosligi (내용 일치), lessons 1–3 (orders 40–42).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_match_1_3.py \
#            --out examprep/management/commands/audio/match
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_match_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/match

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "13–16-savollar: Mazmun mosligi (내용 일치)",
    "summary": "To'rt xil manba — suhbat, e'lon, yangilik, intervyu — eshitilganini variantlar bilan solishtirib, 소거법 bilan yakka to'g'risini qoldirish.",
    "icon":    "bi-check2-square",
    "order":   5,
}

LESSONS = [
    # ── Lesson 1 (order 40) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 1: 13–16-savollar bilan tanishuv — quloq bilan 소거법",
        "summary": "내용 일치 savolining usuli: to'rt manba turi (대화·안내방송·뉴스·인터뷰) va eshitib yo'q qilish metodi.",
        "order":   40,
        "blocks": [
            {"rich_text": """
<h2>✅ 13–16-savollar: eshitilganga MOS gapni toping</h2>
<p>O'qish bo'limidagi eski tanishimiz — 내용 일치 (mazmun mosligi) endi quloq uchun:
matnni eshitasiz va to'rt gapdan <strong>eshitilganga mosini</strong> tanlaysiz.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>13–16.</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오. —
  <em>Eshitib, eshitilgan mazmun bilan bir xil gapni tanlang.</em></p>
</div>
<h3>To'rt manba — to'rt savol</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>13 — 대화</strong> (suhbat): ikki kishining kundalik dialogi.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>14 — 안내방송</strong> (e'lon): do'kon, metro, aeroport, turar-joy radiosi.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>15 — 뉴스·보도</strong> (yangilik): diktor matni, ob-havo, hodisa.</p>
  <p style="font-size:1.05em;margin:0;"><strong>16 — 인터뷰</strong> (intervyu): boshlovchi savol beradi, mehmon javob beradi.</p>
</div>
<h3>Quloq bilan 소거법 (yo'q qilish metodi)</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1-qadam.</strong> Audio boshlanishidan oldin to'rt variantni o'qing —
  ularda nima <strong>farq qilishini</strong> (raqam? kim? qachon?) belgilang.</p></div>
  <div class="pp-step"><p><strong>2-qadam.</strong> Eshitayotganda har variantni tekshirib boring:
  eshitilganga <strong>zid</strong> chiqqanini darhol chizib tashlang. Noto'g'ri variantlar
  odatda bitta aniq gapga qarshi keladi.</p></div>
  <div class="pp-step"><p><strong>3-qadam.</strong> To'g'ri javob deyarli hech qachon audio so'zlarini
  aynan takrorlamaydi — u <strong>boshqacha aytilgan</strong> (paraphrase) bo'ladi. "So'zma-so'z
  tanish" variant ko'pincha tuzoq!</p></div>
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: birga tekshiramiz</h3>
<p>Eshiting va to'rtta faktni ushlang: qayerga borgan? ob-havo? nima qilgan? nima qilolmagan?</p>
""",
             "audio": "topik_l_040_1.mp3",
             "audio_script": [
                 ("여자", "지난 주말에 제주도 여행은 잘 다녀왔어요?"),
                 ("남자", "네, 그런데 비가 와서 바다에는 못 들어갔어요. 대신 박물관 구경을 많이 했어요."),
                 ("여자", "그래도 재미있었겠네요."),
             ]},
            {"rich_text": """
<p>Faktlar ro'yxati — xuddi shu to'rttadan variantlar yasaladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;">✅ Erkak <strong>o'tgan hafta oxiri</strong> Jeju safarida bo'lgan.</p>
  <p style="font-size:1.05em;margin:0 0 6px;">✅ <strong>Yomg'ir yog'gan</strong> → dengizga tusholmagan (비가 와서 못 들어갔어요).</p>
  <p style="font-size:1.05em;margin:0;">✅ Buning o'rniga (대신) <strong>muzeylarni</strong> ko'p aylangan.</p>
</div>
<p>Tuzoqlar shunday tug'iladi: "dengizda cho'mildi" (teskari!), "ob-havo yaxshi edi"
(teskari!), "muzeyga kirolmadi" (almashtirilgan!). <strong>대신</strong> (buning o'rniga)
so'zi — bu guruhning muhim signali: A bo'lmadi → o'rniga B bo'ldi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 지난 주말에 제주도 여행은 잘 다녀왔어요?<br>
    <em style="color:#475569;">O'tgan dam olish kunlari Jeju safaridan yaxshi qaytdingizmi?</em></p>
    <p><strong>남자:</strong> 네, 그런데 비가 와서 바다에는 못 들어갔어요. 대신 박물관 구경을 많이 했어요.<br>
    <em style="color:#475569;">Ha, lekin yomg'ir yog'ib, dengizga tusha olmadik. Buning o'rniga muzeylarni ko'p aylandik.</em></p>
    <p><strong>여자:</strong> 그래도 재미있었겠네요.<br>
    <em style="color:#475569;">Baribir qiziqarli bo'lgandir.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (14-tur: 안내방송).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_040_2.mp3",
             "audio_script": [
                 ("여자", "고객 여러분께 안내 말씀드립니다. 저희 백화점은 오늘 밤 여덟 시까지 영업합니다. 지금 삼 층 행사장에서는 겨울 옷을 최대 오십 퍼센트 할인된 가격으로 판매하고 있습니다. 많은 이용 바랍니다."),
             ],
             "choices": [
                 {"text": "백화점은 오늘 저녁 8시까지 문을 연다. (Savdo markazi bugun kechki 8 gacha ishlaydi.)", "is_correct": True},
                 {"text": "겨울 옷을 최대 30% 할인하고 있다. (Qishki kiyimlar maksimal 30% chegirmada.)", "is_correct": False},
                 {"text": "할인 행사장은 1층에 있다. (Chegirma maydoni 1-qavatda.)", "is_correct": False},
                 {"text": "여름 옷을 할인해서 팔고 있다. (Yozgi kiyimlar chegirmada sotilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② raqam almashtirilgan (<strong>오십</strong> 퍼센트 = 50%, 30 emas!), ③ qavat
almashtirilgan (<strong>삼 층</strong> = 3-qavat), ④ fasl almashtirilgan (<strong>겨울</strong>
옷 = qishki). Qoladi ①: 밤 여덟 시까지 영업합니다 →
<mark style="background:#dcfce7;">8 gacha ishlaydi</mark> ✅ (영업하다 = 문을 열다 —
paraphrase!). E'lonlarda tuzoq deyarli doim <strong>raqam va joyda</strong>.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 고객 여러분께 안내 말씀드립니다. 저희 백화점은 오늘 밤 여덟 시까지
    영업합니다. 지금 삼 층 행사장에서는 겨울 옷을 최대 오십 퍼센트 할인된 가격으로 판매하고
    있습니다. 많은 이용 바랍니다.<br>
    <em style="color:#475569;">Hurmatli mijozlar, e'tiboringizga e'lon. Savdo markazimiz bugun
    kechki soat sakkizgacha ishlaydi. Hozir 3-qavatdagi aksiya maydonida qishki kiyimlar maksimal
    50 foizgacha chegirma bilan sotilmoqda. Marhamat, foydalaning.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (15-tur: 뉴스).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_040_3.mp3",
             "audio_script": [
                 ("남자", "다음은 생활 뉴스입니다. 요즘 아침저녁으로 기온이 크게 떨어지면서 감기 환자가 늘고 있습니다. 병원을 찾는 환자가 지난달보다 두 배 가까이 많아졌는데요. 의사들은 외출 후에 손을 깨끗이 씻는 것이 가장 중요하다고 말합니다."),
             ],
             "choices": [
                 {"text": "감기 환자가 지난달보다 많아졌다. (Shamollagan bemorlar o'tgan oyga qaraganda ko'paygan.)", "is_correct": True},
                 {"text": "요즘 기온이 점점 올라가고 있다. (Keyingi paytlarda harorat ko'tarilmoqda.)", "is_correct": False},
                 {"text": "병원을 찾는 환자가 절반으로 줄었다. (Shifoxonaga boruvchilar yarmiga kamaygan.)", "is_correct": False},
                 {"text": "의사들은 약을 먼저 먹으라고 말한다. (Shifokorlar avval dori ichishni aytishadi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (기온이 <strong>떨어지면서</strong> — tushmoqda!), ③ teskari yo'nalish
(두 배 가까이 <strong>많아졌</strong>는데요 — ikki baravarga yaqin ko'paygan, kamaymagan!),
④ almashtirilgan maslahat (shifokorlar <strong>qo'l yuvishni</strong> aytgan, dori emas).
✅ ①: 늘고 있습니다 + 많아졌는데요 → ko'paygan. Yangiliklarda ↗/↘ yo'nalish so'zlari
(늘다/줄다/떨어지다) — birinchi tekshiruv nuqtangiz.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 다음은 생활 뉴스입니다. 요즘 아침저녁으로 기온이 크게 떨어지면서
    감기 환자가 늘고 있습니다. 병원을 찾는 환자가 지난달보다 두 배 가까이 많아졌는데요.
    의사들은 외출 후에 손을 깨끗이 씻는 것이 가장 중요하다고 말합니다.<br>
    <em style="color:#475569;">Navbatda turmush yangiliklari. Keyingi paytlarda ertalab-kechqurun
    harorat keskin tushishi bilan shamollagan bemorlar ko'paymoqda. Shifoxonaga murojaat
    qilayotganlar o'tgan oyga qaraganda qariyb ikki baravar ko'paygan. Shifokorlar ko'chadan
    qaytgach qo'lni toza yuvish eng muhim, deyishmoqda.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">내용 일치</div><div class="pp-card-back">mazmun mosligi</div></div>
  <div class="pp-card"><div class="pp-card-front">안내방송</div><div class="pp-card-back">radio-e'lon</div></div>
  <div class="pp-card"><div class="pp-card-front">영업하다</div><div class="pp-card-back">ishlamoq (do'kon/xizmat)</div></div>
  <div class="pp-card"><div class="pp-card-front">할인</div><div class="pp-card-back">chegirma</div></div>
  <div class="pp-card"><div class="pp-card-front">기온이 떨어지다</div><div class="pp-card-back">harorat tushmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">환자</div><div class="pp-card-back">bemor</div></div>
  <div class="pp-card"><div class="pp-card-front">대신</div><div class="pp-card-back">buning o'rniga</div></div>
  <div class="pp-card"><div class="pp-card-front">외출</div><div class="pp-card-back">ko'chaga chiqish</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>To'rt manba: 대화 (13), 안내방송 (14), 뉴스 (15), 인터뷰 (16).</li>
  <li>Quloq bilan 소거법: variantlarni oldindan o'qing, zidlarini chizib tashlang.</li>
  <li>To'g'ri javob — paraphrase (영업하다 = 문을 열다); so'zma-so'z tanish variant — tuzoq bo'lishi mumkin.</li>
  <li>Tuzoqlarning uyi: raqam, joy, yo'nalish (늘다/줄다) va 대신 almashinuvi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 41) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 2: E'lon va ob-havo tili — 안내방송·일기예보",
        "summary": "14–15-savollarning maxsus tili: e'lon qoliplari (안내 말씀드립니다, 이용해 주시기 바랍니다) va ob-havo lug'ati (맑다, 영하, 미세 먼지).",
        "order":   41,
        "blocks": [
            {"rich_text": """
<h2>📢 E'lonlar hamma joyda bir xil gapiradi</h2>
<p>안내방송 (radio-e'lon) — imtihonning eng "qoliplashgan" matni. Boshlanishi va tugashini
oldindan bilasiz, faqat o'rtasidagi faktlarni ushlash qoladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>Ochilish:</strong> 고객/승객/주민 여러분께 안내 말씀드립니다 — mijozlar/yo'lovchilar/aholi, e'tiboringizga e'lon.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>Mag'iz:</strong> vaqt + joy + nima bo'ladi (공사 — ta'mirlash, 행사 — aksiya, 점검 — texnik ko'rik).</p>
  <p style="font-size:1.05em;margin:0;"><strong>Yopilish:</strong> ~해 주시기 바랍니다 (iltimos qilamiz), 불편을 드려서 죄송합니다 (noqulaylik uchun uzr).</p>
</div>
<p>Joyni birinchi so'zdan aniqlang: 고객 (mijoz) → do'kon; 승객 (yo'lovchi) → metro/avtobus/samolyot;
주민 (aholi) → turar-joy.</p>
<h3>🌦️ Ob-havo (일기예보) lug'ati — 15-savolning sevimlisi</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>맑다 / 맑겠습니다</strong> — ochiq (bo'ladi) &nbsp;|&nbsp; <strong>흐리다</strong> — bulutli</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>비가 오다 / 눈이 오다</strong> — yomg'ir / qor yog'moq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>기온</strong> — harorat &nbsp;|&nbsp; <strong>영하</strong> — noldan past (−!)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>전국</strong> — butun mamlakat &nbsp;|&nbsp; <strong>대체로</strong> — asosan</p>
  <p style="font-size:1.05em;margin:0;"><strong>미세 먼지</strong> — mayda chang (havo ifloslanishi)</p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Ob-havo matni doim <strong>vaqt bo'yicha bo'linadi</strong>: ertalab
  bir xil, kunduzi boshqa, kechqurun yana boshqa (아침에는… 낮에는… 저녁부터는…). Tuzoq —
  bitta bo'lakning holatini butun kunga yoyish!
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1 (metro e'loni).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_041_1.mp3",
             "audio_script": [
                 ("여자", "승객 여러분께 안내 말씀드립니다. 오늘 오후 두 시부터 네 시까지 시설 점검 공사로 이 역의 삼 번 출구를 이용하실 수 없습니다. 사 번 출구를 이용해 주시기 바랍니다. 불편을 드려서 죄송합니다."),
             ],
             "choices": [
                 {"text": "오후 2시부터 4시까지 3번 출구를 이용할 수 없다. (Tushdan keyin 2 dan 4 gacha 3-chiqishdan foydalanib bo'lmaydi.)", "is_correct": True},
                 {"text": "지하철이 두 시간 동안 운행하지 않는다. (Metro ikki soat qatnamaydi.)", "is_correct": False},
                 {"text": "4번 출구가 공사 때문에 닫혀 있다. (4-chiqish ta'mirlash sababli yopiq.)", "is_correct": False},
                 {"text": "공사는 이미 어제 끝났다. (Ta'mirlash kecha tugagan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② kengaytirish tuzog'i — yopilgani <strong>bitta chiqish</strong>, metro emas!
③ raqam almashtirilgan (yopiq — <strong>삼 번</strong>/3-chiqish; <strong>사 번</strong>/4-chiqish
esa taklif qilinayotgan yo'l), ④ zamon (오늘 오후 — bugun, hali oldinda). ✅ ①: 이용하실 수
없습니다 → foydalanib bo'lmaydi. E'londa <strong>ikkita raqam</strong> yonma-yon kelsa
(3-chiqish yopiq, 4-dan yuring) — savol aynan shularni almashtiradi!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 승객 여러분께 안내 말씀드립니다. 오늘 오후 두 시부터 네 시까지 시설
    점검 공사로 이 역의 삼 번 출구를 이용하실 수 없습니다. 사 번 출구를 이용해 주시기 바랍니다.
    불편을 드려서 죄송합니다.<br>
    <em style="color:#475569;">Hurmatli yo'lovchilar, e'tiboringizga e'lon. Bugun tushdan keyin
    soat ikkidan to'rtgacha texnik ko'rik ishlari sababli bekatning 3-chiqishidan foydalanib
    bo'lmaydi. 4-chiqishdan foydalanishingizni so'raymiz. Noqulaylik uchun uzr.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (ob-havo).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_041_2.mp3",
             "audio_script": [
                 ("남자", "날씨를 알려 드리겠습니다. 내일은 전국이 대체로 맑겠습니다. 하지만 아침 기온이 영하로 떨어져서 춥겠습니다. 낮에는 기온이 조금 올라가겠지만 저녁부터는 다시 추워지겠습니다. 외출하실 때 따뜻한 옷을 준비하시기 바랍니다."),
             ],
             "choices": [
                 {"text": "내일 아침 기온은 영하로 떨어진다. (Ertaga ertalab harorat noldan pastga tushadi.)", "is_correct": True},
                 {"text": "내일은 전국에 비가 내린다. (Ertaga butun mamlakatda yomg'ir yog'adi.)", "is_correct": False},
                 {"text": "낮에도 기온이 계속 떨어진다. (Kunduzi ham harorat tushishda davom etadi.)", "is_correct": False},
                 {"text": "저녁부터 날씨가 따뜻해진다. (Kechqurundan havo isiy boshlaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Vaqt bo'laklari: ertalab — <strong>영하, 춥겠습니다</strong> (✅ ①); kunduzi — 조금
<strong>올라가겠지만</strong> (③ ga zid); kechqurun — 다시 <strong>추워지겠습니다</strong>
(④ ga zid — teskari!). ② esa umuman boshqa hodisa (맑겠습니다 — ochiq, yomg'ir yo'q).
Ob-havoda uch vaqt bo'lagini alohida yozib oling: 아침 / 낮 / 저녁 — javob har doim
shularning birida.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 날씨를 알려 드리겠습니다. 내일은 전국이 대체로 맑겠습니다. 하지만
    아침 기온이 영하로 떨어져서 춥겠습니다. 낮에는 기온이 조금 올라가겠지만 저녁부터는 다시
    추워지겠습니다. 외출하실 때 따뜻한 옷을 준비하시기 바랍니다.<br>
    <em style="color:#475569;">Ob-havo ma'lumoti. Ertaga butun mamlakatda asosan ochiq bo'ladi.
    Biroq ertalab harorat noldan pastga tushib, sovuq bo'ladi. Kunduzi harorat biroz ko'tarilsa-da,
    kechqurundan yana soviydi. Ko'chaga chiqqaningizda issiq kiyim tayyorlab qo'ying.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3 (yo'qolgan buyum e'loni).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_041_3.mp3",
             "audio_script": [
                 ("여자", "잠시 안내 말씀드리겠습니다. 조금 전 일 층 안내 데스크에 어린이 가방이 접수되었습니다. 파란색 가방이고 안에 동화책이 들어 있습니다. 가방을 잃어버리신 분은 일 층 안내 데스크로 와 주시기 바랍니다."),
             ],
             "choices": [
                 {"text": "가방을 잃어버린 사람은 1층 안내 데스크로 가면 된다. (Sumkasini yo'qotgan kishi 1-qavatdagi ma'lumot stoliga borsa bo'ladi.)", "is_correct": True},
                 {"text": "어린이가 길을 잃어버렸다. (Bola adashib qolgan.)", "is_correct": False},
                 {"text": "가방은 2층에서 발견되었다. (Sumka 2-qavatda topilgan.)", "is_correct": False},
                 {"text": "가방 안에는 지갑이 들어 있다. (Sumka ichida hamyon bor.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② mavzuni almashtirgan tuzoq — yo'qolgani <strong>bolaning sumkasi</strong>, bola
emas (어린이 가방 — "bolalar sumkasi"!); ③ qavat (일 층 = 1-qavat); ④ ichidagi narsa
(동화책 — ertak kitobi, hamyon emas). ✅ ①: 와 주시기 바랍니다 → borsa bo'ladi. Ikki ot
yonma-yon kelganda (어린이+가방) qaysi biri asosiy ekanini adashtirmang — bu ham sevimli
tuzoq.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 잠시 안내 말씀드리겠습니다. 조금 전 일 층 안내 데스크에 어린이 가방이
    접수되었습니다. 파란색 가방이고 안에 동화책이 들어 있습니다. 가방을 잃어버리신 분은 일 층
    안내 데스크로 와 주시기 바랍니다.<br>
    <em style="color:#475569;">E'tiboringizga qisqa e'lon. Hozirgina 1-qavatdagi ma'lumot stoliga
    bolalar sumkasi topshirildi. Ko'k rangli sumka, ichida ertak kitobi bor. Sumkasini yo'qotgan
    kishi 1-qavatdagi ma'lumot stoliga kelishini so'raymiz.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">승객</div><div class="pp-card-back">yo'lovchi</div></div>
  <div class="pp-card"><div class="pp-card-front">점검 / 공사</div><div class="pp-card-back">texnik ko'rik / ta'mirlash ishi</div></div>
  <div class="pp-card"><div class="pp-card-front">출구</div><div class="pp-card-back">chiqish (eshigi)</div></div>
  <div class="pp-card"><div class="pp-card-front">맑다 / 흐리다</div><div class="pp-card-back">ochiq / bulutli</div></div>
  <div class="pp-card"><div class="pp-card-front">영하</div><div class="pp-card-back">noldan past (harorat)</div></div>
  <div class="pp-card"><div class="pp-card-front">잃어버리다</div><div class="pp-card-back">yo'qotib qo'ymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">접수되다</div><div class="pp-card-back">qabul qilinmoq (topshirilmoq)</div></div>
  <div class="pp-card"><div class="pp-card-front">동화책</div><div class="pp-card-back">ertak kitobi</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>E'lon qolipi: murojaat (고객/승객/주민) → vaqt+joy+hodisa → iltimos. Birinchi so'z joyni aytadi.</li>
  <li>Ob-havo uch bo'lak: 아침 / 낮 / 저녁 — har birining holatini alohida ushlang.</li>
  <li>Tuzoqlar: raqam-qavat almashinuvi, bo'lak holatini butunga yoyish, qo'shni otni asosiy qilib ko'rsatish.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 42) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 내용 일치 3: To'liq amaliyot — to'rt manba ketma-ket",
        "summary": "13–16-savollar to'liq to'plami imtihondagidek: suhbat, turar-joy e'loni, yangilik va intervyu — har biri bir marta.",
        "order":   42,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 13, 14, 15, 16-savollar</h2>
<p>To'rt savol — to'rt manba, imtihondagi tartibda: <strong>대화 → 안내방송 → 뉴스 →
인터뷰</strong>. Har audiodan oldin variantlarni o'qib, farq nuqtalarini belgilang;
eshitayotganda zid variantlarni chizib tashlang.</p>
"""},
            {"rich_text": """
<p><strong>13-savol (대화).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_042_1.mp3",
             "audio_script": [
                 ("여자", "요즘 운동을 시작했다면서요?"),
                 ("남자", "네, 집 근처 수영장에 다녀요. 일주일에 세 번, 아침에 가요."),
                 ("여자", "저도 수영을 배우고 싶었는데 같이 다닐까요?"),
                 ("남자", "좋아요. 그럼 내일 같이 등록하러 가요."),
             ],
             "choices": [
                 {"text": "남자는 일주일에 세 번 수영장에 간다. (Erkak haftasiga uch marta suzish havzasiga boradi.)", "is_correct": True},
                 {"text": "여자는 이미 수영을 배우고 있다. (Ayol allaqachon suzishni o'rganmoqda.)", "is_correct": False},
                 {"text": "남자는 저녁마다 운동한다. (Erkak har kuni kechqurun shug'ullanadi.)", "is_correct": False},
                 {"text": "두 사람은 오늘 등록하러 간다. (Ikkalasi bugun ro'yxatdan o'tgani boradi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② zamon tuzog'i — ayol <strong>배우고 싶었는데</strong> (o'rgangisi kelgan edi) —
hali boshlamagan!; ③ vaqt almashtirilgan (<strong>아침에</strong> — ertalab); ④ kun
almashtirilgan (<strong>내일</strong> — ertaga). ✅ ①: 일주일에 세 번 aynan eshitildi —
lekin e'tibor bering: bu safar to'g'ri javob so'zma-so'z ham bo'lishi mumkin, faqat
qolgan uchtasining "buzilgan" joyini aniq topganingizga ishonch hosil qiling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 요즘 운동을 시작했다면서요?<br>
    <em style="color:#475569;">Yaqinda sport boshlabsiz deb eshitdim?</em></p>
    <p><strong>남자:</strong> 네, 집 근처 수영장에 다녀요. 일주일에 세 번, 아침에 가요.<br>
    <em style="color:#475569;">Ha, uy yaqinidagi suzish havzasiga qatnayapman. Haftasiga uch marta, ertalab boraman.</em></p>
    <p><strong>여자:</strong> 저도 수영을 배우고 싶었는데 같이 다닐까요?<br>
    <em style="color:#475569;">Men ham suzishni o'rgangim kelgan edi, birga qatnaymizmi?</em></p>
    <p><strong>남자:</strong> 좋아요. 그럼 내일 같이 등록하러 가요.<br>
    <em style="color:#475569;">Yaxshi. Unda ertaga birga ro'yxatdan o'tgani boramiz.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>14-savol (안내방송).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_042_2.mp3",
             "audio_script": [
                 ("남자", "주민 여러분께 안내 말씀드립니다. 내일 오전 아홉 시부터 열두 시까지 아파트 물탱크 청소가 있을 예정입니다. 이 시간 동안에는 물이 나오지 않으니 필요한 물을 미리 받아 두시기 바랍니다. 협조해 주셔서 감사합니다."),
             ],
             "choices": [
                 {"text": "내일 오전에는 물을 사용할 수 없다. (Ertaga tushgacha suvdan foydalanib bo'lmaydi.)", "is_correct": True},
                 {"text": "물탱크 청소는 오늘 저녁에 한다. (Suv omborini tozalash bugun kechqurun bo'ladi.)", "is_correct": False},
                 {"text": "청소는 열두 시에 시작된다. (Tozalash soat o'n ikkida boshlanadi.)", "is_correct": False},
                 {"text": "물을 미리 받아 둘 필요는 없다. (Suvni oldindan olib qo'yish shart emas.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② kun (내일 <strong>오전</strong> — ertaga tushgacha!), ③ 9 va 12 almashtirilgan
(아홉 시<strong>부터</strong> — 9 da <strong>boshlanadi</strong>, 12 da tugaydi), ④ e'lonning
teskarisi (미리 받아 두시기 <strong>바랍니다</strong> — aynan olib qo'yish so'ralyapti!).
✅ ①: 물이 나오지 않으니 → suv bo'lmaydi. ~부터/~까지 juftligini eshitganda qaysi
raqam boshi, qaysi oxiri ekanini yozib oling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 주민 여러분께 안내 말씀드립니다. 내일 오전 아홉 시부터 열두 시까지
    아파트 물탱크 청소가 있을 예정입니다. 이 시간 동안에는 물이 나오지 않으니 필요한 물을 미리
    받아 두시기 바랍니다. 협조해 주셔서 감사합니다.<br>
    <em style="color:#475569;">Hurmatli aholi, e'tiboringizga e'lon. Ertaga ertalab soat
    to'qqizdan o'n ikkigacha binoning suv ombori tozalanadi. Bu vaqt davomida suv bo'lmaydi,
    kerakli suvni oldindan olib qo'yishingizni so'raymiz. Hamkorligingiz uchun rahmat.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>15-savol (뉴스).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_042_3.mp3",
             "audio_script": [
                 ("여자", "사건 소식입니다. 오늘 새벽 시내의 한 도로에서 눈길에 차가 미끄러지는 사고가 있었습니다. 다행히 다친 사람은 없었지만 이 사고로 출근 시간에 두 시간 가까이 길이 막혔습니다. 경찰은 눈이 올 때는 속도를 줄여서 운전해 달라고 당부했습니다."),
             ],
             "choices": [
                 {"text": "사고로 다친 사람은 없었다. (Falokatda jarohatlanganlar bo'lmagan.)", "is_correct": True},
                 {"text": "사고는 어제 오후에 일어났다. (Falokat kecha tushdan keyin yuz bergan.)", "is_correct": False},
                 {"text": "길이 삼십 분 정도 막혔다. (Yo'l o'ttiz daqiqacha tiqilib qolgan.)", "is_correct": False},
                 {"text": "경찰은 빨리 운전하라고 당부했다. (Politsiya tez haydashni so'ragan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② vaqt (<strong>오늘 새벽</strong> — bugun tong sahar!), ③ davomiylik
(<strong>두 시간 가까이</strong> — qariyb ikki soat, 30 daqiqa emas), ④ teskari maslahat
(속도를 <strong>줄여서</strong> — tezlikni KAMAYTIRIB!). ✅ ①: 다행히 다친 사람은
없었지만 → jarohatlanganlar yo'q. <strong>다행히</strong> (xayriyat) so'zi yangiliklarda
deyarli doim "yomon bo'lishi mumkin edi, lekin bo'lmadi" faktini boshlaydi — to'g'ri javob
ko'pincha shu yerda!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 사건 소식입니다. 오늘 새벽 시내의 한 도로에서 눈길에 차가 미끄러지는
    사고가 있었습니다. 다행히 다친 사람은 없었지만 이 사고로 출근 시간에 두 시간 가까이 길이
    막혔습니다. 경찰은 눈이 올 때는 속도를 줄여서 운전해 달라고 당부했습니다.<br>
    <em style="color:#475569;">Hodisalar xabari. Bugun tong saharda shahar yo'llaridan birida
    qorli yo'lda mashina sirpanib ketishi oqibatida falokat yuz berdi. Xayriyat, jarohatlanganlar
    bo'lmadi, ammo bu falokat tufayli ishga qatnov vaqtida yo'l qariyb ikki soat tiqilib qoldi.
    Politsiya qor yog'ayotganda tezlikni kamaytirib haydashni so'radi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>16-savol (인터뷰).</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_042_4.mp3",
             "audio_script": [
                 ("남자", "오늘은 이십 년째 빵을 만들고 계신 분을 모셨습니다. 맛있는 빵의 비결이 무엇입니까?"),
                 ("여자", "저는 좋은 재료가 가장 중요하다고 생각합니다. 그래서 저희 가게는 매일 아침 농장에서 바로 온 우유와 계란만 사용합니다. 값이 조금 비싸지만 손님들이 그 맛을 알아주시니까요."),
             ],
             "choices": [
                 {"text": "여자는 좋은 재료가 가장 중요하다고 생각한다. (Ayol eng muhimi sifatli masalliq deb hisoblaydi.)", "is_correct": True},
                 {"text": "여자는 빵을 만든 지 십 년이 되었다. (Ayol non yopishni boshlaganiga o'n yil bo'lgan.)", "is_correct": False},
                 {"text": "가게는 일주일에 한 번 재료를 받는다. (Do'kon masalliqni haftasiga bir marta oladi.)", "is_correct": False},
                 {"text": "가게의 재료 값은 아주 싸다. (Do'kon masalliqlari juda arzon.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② raqam (<strong>이십 년째</strong> — yigirma yildan beri!), ③ chastota
(<strong>매일 아침</strong> — har kuni ertalab!), ④ teskari (값이 조금 <strong>비싸지만</strong>
— biroz qimmat!). ✅ ①: 좋은 재료가 가장 중요하다고 생각합니다 — aynan aytilgan. Intervyuda
boshlovchining kirish gapi (이십 년째…) ham savolga kiradi — faqat mehmonning gapini emas,
<strong>ikkalasini</strong> eshiting. To'rt manbani ham yengdingiz! 🎉</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 오늘은 이십 년째 빵을 만들고 계신 분을 모셨습니다. 맛있는 빵의 비결이 무엇입니까?<br>
    <em style="color:#475569;">Bugun yigirma yildan beri non yopib kelayotgan insonni taklif qildik. Mazali nonning siri nimada?</em></p>
    <p><strong>여자:</strong> 저는 좋은 재료가 가장 중요하다고 생각합니다. 그래서 저희 가게는 매일
    아침 농장에서 바로 온 우유와 계란만 사용합니다. 값이 조금 비싸지만 손님들이 그 맛을 알아주시니까요.<br>
    <em style="color:#475569;">Menimcha, eng muhimi — sifatli masalliq. Shuning uchun do'konimiz
    har kuni ertalab fermadan to'g'ridan-to'g'ri kelgan sut va tuxumdan foydalanadi. Narxi biroz
    qimmat, lekin mijozlar o'sha ta'mni qadrlashadi-da.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">등록하다</div><div class="pp-card-back">ro'yxatdan o'tmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">물탱크</div><div class="pp-card-back">suv ombori</div></div>
  <div class="pp-card"><div class="pp-card-front">미리 받아 두다</div><div class="pp-card-back">oldindan olib qo'ymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">미끄러지다</div><div class="pp-card-back">sirpanib ketmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">다행히</div><div class="pp-card-back">xayriyat</div></div>
  <div class="pp-card"><div class="pp-card-front">당부하다</div><div class="pp-card-back">qat'iy iltimos qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">비결</div><div class="pp-card-back">sir, muvaffaqiyat siri</div></div>
  <div class="pp-card"><div class="pp-card-front">재료</div><div class="pp-card-back">masalliq, xomashyo</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>To'rt manbaning har biri o'z qolipiga ega — qolipni bilsangiz, faktlar o'zi ajralib turadi.</li>
  <li>Doimiy tuzoqlar: raqam/vaqt almashinuvi, teskari yo'nalish, "istagan" ≠ "qilgan" (배우고 싶었는데!).</li>
  <li>다행히 / 대신 / ~부터 ~까지 — javob yashiringan signal so'zlar.</li>
</ul>
"""},
        ],
    },
]
