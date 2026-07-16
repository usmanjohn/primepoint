# TOPIK II Listening — 4–8-savollar: Keyingi replika (이어질 말), lessons 1–3 (orders 20–22).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_reply_1_3.py \
#            --out examprep/management/commands/audio/reply
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_reply_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/reply

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "4–8-savollar: Keyingi replika (이어질 말)",
    "summary": "Dialogning oxirgi gapiga mos javob replikasini tanlash: savolga — javob, iltimosga — rozilik/rad, xabarga — munosabat.",
    "icon":    "bi-chat-dots",
    "order":   3,
}

LESSONS = [
    # ── Lesson 1 (order 20) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 이어질 말 1: 4–8-savollar bilan tanishuv — oxirgi gap hal qiladi",
        "summary": "이어질 말 savolining mantig'i: dialog oxirgi replikada 'ochiq' qoladi — uning turini (savol/iltimos/xabar) aniqlab, mos javobni tanlaysiz.",
        "order":   20,
        "blocks": [
            {"rich_text": """
<h2>💬 4–8-savollar: suhbatni kim davom ettiradi?</h2>
<p>Bu guruhda qisqa dialog eshitiladi va u <strong>"ochiq" tugaydi</strong> — oxirgi gapga
javob berilmaydi. Sizning vazifangiz: suhbatni tabiiy davom ettiradigan replikani tanlash.</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>4–8.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오. —
  <em>Dialogni eshitib, keyin kelishi mumkin bo'lgan gapni tanlang.</em></p>
</div>
<h3>Butun sir — OXIRGI GAPDA</h3>
<p>Dialogda nima bo'lganidan qat'i nazar, javobni <strong>faqat oxirgi replika</strong>
belgilaydi. Uni eshitgan zahoti turini aniqlang:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>① Savol (질문)</strong> — 언제/어디/뭐/몇…? → javob <strong>aynan so'ralgan narsa</strong> haqida bo'ladi.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>② Iltimos / taklif (부탁·제안)</strong> — ~아 주세요, ~을래요?, 같이 ~을까요? → javob: <strong>rozilik yoki muloyim rad</strong>.</p>
  <p style="font-size:1.05em;margin:0;"><strong>③ Xabar / his-tuyg'u (소식·감정)</strong> — yangilik, shikoyat, quvonch → javob: <strong>mos munosabat</strong> (tabrik, achinish, tasalli).</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Noto'g'ri variantlar ko'pincha dialogdagi <strong>so'zlarni
  takrorlaydi</strong>, lekin oxirgi gapning turiga mos kelmaydi (savolga savol bilan javob
  beradi, iltimosga aloqasiz fakt aytadi). So'z tanishligiga emas, <strong>suhbat
  mantig'iga</strong> qarang.
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: birga tahlil qilamiz</h3>
<p>Avval audioni eshiting. Oxirgi gap nima edi — savolmi, iltimosmi, xabarmi?</p>
""",
             "audio": "topik_l_020_1.mp3",
             "audio_script": [
                 ("여자", "어제 산 가방인데 지퍼가 벌써 고장 났어요."),
                 ("남자", "죄송합니다, 손님. 영수증을 가지고 오셨어요?"),
             ]},
            {"rich_text": """
<p>Oxirgi gap: <strong>영수증을 가지고 오셨어요?</strong> (Chek olib keldingizmi?) — bu
<strong>savol</strong>, demak javob <strong>chek haqida</strong> bo'lishi shart: bor/yo'q.
"Sumka qachon olingani" yoki "kechirim" emas — aynan chek!</p>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 Namuna javob:</strong> 네, 여기 있어요. — <em>Ha, mana.</em> &nbsp;yoki&nbsp;
  아니요, 집에 두고 왔는데 어떡하죠? — <em>Yo'q, uyda qoldirib kelibman, endi nima qilamiz?</em>
</div>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 어제 산 가방인데 지퍼가 벌써 고장 났어요.<br>
    <em style="color:#475569;">Kecha olgan sumkam edi, zamog'i allaqachon buzildi.</em></p>
    <p><strong>남자:</strong> 죄송합니다, 손님. 영수증을 가지고 오셨어요?<br>
    <em style="color:#475569;">Uzr, mijoz. Chekni olib keldingizmi?</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_020_2.mp3",
             "audio_script": [
                 ("남자", "내일 친구들하고 등산 갈 건데 같이 갈래요?"),
                 ("여자", "가고 싶은데 내일은 약속이 있어요."),
             ],
             "choices": [
                 {"text": "그럼 다음에 같이 가요. (Unda keyingi safar birga boramiz.)", "is_correct": True},
                 {"text": "네, 그럼 내일 아침에 만나요. (Xo'p, unda ertaga ertalab ko'rishamiz.)", "is_correct": False},
                 {"text": "등산화를 새로 샀어요. (Yangi tog' poyabzali sotib oldim.)", "is_correct": False},
                 {"text": "약속 시간에 늦으면 안 돼요. (Uchrashuvga kechikmaslik kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi gap turi: <strong>muloyim rad</strong> (가고 싶은데… 약속이 있어요 — borgim bor,
lekin band). Radga tabiiy javob — <mark style="background:#dcfce7;">boshqa vaqtga
taklif</mark>: 그럼 다음에 같이 가요 ✅. ② rad etilganini eshitmagan odamning javobi —
tuzoq! ④ dialogdagi 약속 so'zini takrorlaydi, lekin suhbatga ulanmaydi. So'z emas —
mantiq!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 내일 친구들하고 등산 갈 건데 같이 갈래요?<br>
    <em style="color:#475569;">Ertaga do'stlar bilan toqqa chiqamiz, birga borasizmi?</em></p>
    <p><strong>여자:</strong> 가고 싶은데 내일은 약속이 있어요.<br>
    <em style="color:#475569;">Borgim bor edi-yu, ertaga uchrashuvim bor.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_020_3.mp3",
             "audio_script": [
                 ("여자", "이 서류를 오늘까지 부장님께 드려야 하는데 부장님이 자리에 안 계시네요."),
                 ("남자", "부장님은 지금 회의 중이세요. 한 시간 후에 끝날 거예요."),
             ],
             "choices": [
                 {"text": "그럼 이따가 다시 올게요. (Unda birozdan keyin yana kelaman.)", "is_correct": True},
                 {"text": "회의가 벌써 끝났군요. (Majlis allaqachon tugabdi-da.)", "is_correct": False},
                 {"text": "서류를 어디에서 사요? (Hujjatni qayerdan sotib olsa bo'ladi?)", "is_correct": False},
                 {"text": "부장님이 정말 친절하시네요. (Bo'lim boshlig'i juda mehribon ekan.)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi gap turi: <strong>xabar</strong> (boshliq majlisda, bir soatdan keyin bo'shaydi).
Bu ma'lumotga tabiiy munosabat — <mark style="background:#dcfce7;">rejani moslash</mark>:
이따가 다시 올게요 ✅ (keyinroq qaytaman). ② eshitilganning teskarisi (회의 <strong>중</strong>
— hali tugamagan!), ③ 서류 so'zini takrorlagan ma'nosiz tuzoq. 이따가 (birozdan keyin) —
bu guruhning sevimli so'zi, yodlab oling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 이 서류를 오늘까지 부장님께 드려야 하는데 부장님이 자리에 안 계시네요.<br>
    <em style="color:#475569;">Bu hujjatni bugungacha bo'lim boshlig'iga berishim kerak edi, lekin u kishi joyida yo'q ekan.</em></p>
    <p><strong>남자:</strong> 부장님은 지금 회의 중이세요. 한 시간 후에 끝날 거예요.<br>
    <em style="color:#475569;">Boshliq hozir majlisda. Bir soatdan keyin tugaydi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">이어질 말</div><div class="pp-card-back">keyin keladigan gap</div></div>
  <div class="pp-card"><div class="pp-card-front">지퍼</div><div class="pp-card-back">zamok (molniya)</div></div>
  <div class="pp-card"><div class="pp-card-front">영수증</div><div class="pp-card-back">chek</div></div>
  <div class="pp-card"><div class="pp-card-front">약속이 있다</div><div class="pp-card-back">uchrashuvi bor (band)</div></div>
  <div class="pp-card"><div class="pp-card-front">서류</div><div class="pp-card-back">hujjat</div></div>
  <div class="pp-card"><div class="pp-card-front">자리에 안 계시다</div><div class="pp-card-back">joyida yo'q (hurmat shakli)</div></div>
  <div class="pp-card"><div class="pp-card-front">회의 중</div><div class="pp-card-back">majlisda (majlis davomida)</div></div>
  <div class="pp-card"><div class="pp-card-front">이따가</div><div class="pp-card-back">birozdan keyin</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Javobni <strong>oxirgi replika</strong> belgilaydi — turini aniqlang: savol / iltimos-taklif / xabar.</li>
  <li>Savolga — aynan so'ralgan narsa; taklifga — rozilik yoki muloyim rad; xabarga — mos munosabat.</li>
  <li>Dialog so'zini takrorlagan, lekin mantiqqa ulanmagan variant — tuzoq.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 21) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 이어질 말 2: Javob replikalari lug'ati — rozilik, rad, munosabat",
        "summary": "Eng ko'p uchraydigan javob qoliplari: 그럼요/좋아요 (rozilik), 죄송하지만 (rad), 축하해요/아쉽네요/다행이네요 (his-tuyg'u).",
        "order":   21,
        "blocks": [
            {"rich_text": """
<h2>🗂️ Javob replikalari lug'ati</h2>
<p>4–8-savollarning variantlari deyarli doim shu to'rt guruhdan chiqadi. Ularni oldindan
bilsangiz, to'g'ri javob audio tugamasidanoq "ko'rinib" turadi.</p>
<h3>① Rozilik / qabul qilish</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>그럼요. / 물론이죠.</strong> — Albatta-da.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>좋아요. 그렇게 해요.</strong> — Yaxshi, shunday qilamiz.</p>
  <p style="font-size:1.05em;margin:0;"><strong>네, 그러세요.</strong> — Ha, bemalol (ruxsat).</p>
</div>
<h3>② Muloyim rad etish</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>죄송하지만 안 될 것 같아요.</strong> — Uzr, bo'lmasa kerak.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>미안하지만 선약이 있어서요.</strong> — Kechirasiz, oldindan va'dam bor edi.</p>
  <p style="font-size:1.05em;margin:0;"><strong>다음에 하면 안 될까요?</strong> — Keyingi safar qilsak bo'lmaydimi?</p>
</div>
<h3>③ His-tuyg'uga munosabat</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>축하해요!</strong> — Tabriklayman! (yaxshi yangilikka)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>아쉽네요.</strong> — Afsus-da. (rejaning buzilishiga)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>저런, 힘들겠어요.</strong> — Voy, qiyin bo'lyapti-da. (muammoga achinish)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>다행이네요.</strong> — Yaxshiyam-a / xayriyat. (yomondan qutulganga)</p>
  <p style="font-size:1.05em;margin:0;"><strong>걱정하지 마세요.</strong> — Xavotir olmang. (tasalli)</p>
</div>
<h3>④ Taklif-maslahatga javob</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>좋은 생각이에요.</strong> — Yaxshi fikr.</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>한번 해 볼게요.</strong> — Bir urinib ko'raman.</p>
  <p style="font-size:1.05em;margin:0;"><strong>글쎄요, 잘 모르겠는데요.</strong> — Bilmadim-ov… (ikkilanish)</p>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Eng xavfli tuzoq — <strong>teskari his-tuyg'u</strong>: yomon
  xabarga 다행이네요 (xayriyat!) yoki yaxshi xabarga 아쉽네요 (afsus). Avval xabarning
  <strong>rangini</strong> aniqlang: yaxshimi, yomonmi? Keyin mos munosabatni tanlang.
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_021_1.mp3",
             "audio_script": [
                 ("여자", "저 다음 달에 결혼해요. 청첩장 여기 있어요."),
                 ("남자", "와, 정말요?"),
             ],
             "choices": [
                 {"text": "축하해요! 결혼식이 며칠이에요? (Tabriklayman! To'y qaysi kuni?)", "is_correct": True},
                 {"text": "아쉽네요. 다음에 봐요. (Afsus. Keyin ko'rishamiz.)", "is_correct": False},
                 {"text": "걱정하지 마세요. 금방 나을 거예요. (Xavotir olmang, tez tuzalib ketasiz.)", "is_correct": False},
                 {"text": "글쎄요, 잘 모르겠는데요. (Bilmadim-ov.)", "is_correct": False},
             ],
             "explanation": """
<p>Xabar rangi: <strong>yaxshi</strong> (결혼해요 — turmush quraman + taklifnoma!). Yaxshi
yangilikka mos munosabat — <mark style="background:#dcfce7;">tabrik</mark>: 축하해요! ✅,
ustiga tabiiy davom savoli (며칠이에요?). ② teskari rang, ③ kasal odamga aytiladigan
tasalli — bu yerda mutlaqo yotmaydi. His-tuyg'u savollarida avval rang, keyin javob!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 저 다음 달에 결혼해요. 청첩장 여기 있어요.<br>
    <em style="color:#475569;">Men kelasi oy turmush quraman. Mana taklifnoma.</em></p>
    <p><strong>남자:</strong> 와, 정말요?<br>
    <em style="color:#475569;">Voy, rostdanmi?</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_021_2.mp3",
             "audio_script": [
                 ("남자", "감기에 심하게 걸려서 오늘 모임에 못 갈 것 같아요."),
                 ("여자", "그래요? 목소리가 정말 안 좋네요."),
             ],
             "choices": [
                 {"text": "네, 약 먹고 푹 쉬어야겠어요. (Ha, dori ichib yaxshilab dam olsam kerak.)", "is_correct": True},
                 {"text": "모임이 정말 재미있었어요. (Yig'ilish juda qiziqarli bo'ldi.)", "is_correct": False},
                 {"text": "다행이네요. 빨리 오세요. (Xayriyat. Tezroq keling.)", "is_correct": False},
                 {"text": "저도 결혼식에 갈 거예요. (Men ham to'yga boraman.)", "is_correct": False},
             ],
             "explanation": """
<p>Bu safar oxirgi gap ayolniki: "ovozingiz juda yomon eshitilyapti" — <strong>hamdardlik</strong>.
Kasal odamning tabiiy javobi — <mark style="background:#dcfce7;">holatini tasdiqlab, rejasini
aytish</mark>: 약 먹고 푹 쉬어야겠어요 ✅. ② o'tmagan yig'ilish haqida o'tgan zamonda —
mantiqsiz; ③ 다행이네요 — teskari rang tuzog'i (kasallikka "xayriyat" deb bo'lmaydi!).
푹 쉬다 (miriqib dam olmoq) — kasallik dialoglarining doimiy mehmoni.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 감기에 심하게 걸려서 오늘 모임에 못 갈 것 같아요.<br>
    <em style="color:#475569;">Qattiq shamollab qoldim, bugungi yig'ilishga borolmasam kerak.</em></p>
    <p><strong>여자:</strong> 그래요? 목소리가 정말 안 좋네요.<br>
    <em style="color:#475569;">Shundaymi? Ovozingiz rostdan ham yomon eshitilyapti.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 3.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_021_3.mp3",
             "audio_script": [
                 ("여자", "이번 주말에 새로 나온 영화 같이 볼래요?"),
                 ("남자", "미안해요. 주말에는 고향에 내려가야 해요."),
             ],
             "choices": [
                 {"text": "그럼 다음 주에 같이 봐요. (Unda kelasi haftada birga ko'ramiz.)", "is_correct": True},
                 {"text": "그럼 주말에 극장 앞에서 만나요. (Unda dam olish kuni kinoteatr oldida ko'rishamiz.)", "is_correct": False},
                 {"text": "고향이 정말 아름답겠어요? (Yurtingiz juda go'zaldir-a?)", "is_correct": False},
                 {"text": "영화표가 얼마인지 아세요? (Kino chiptasi qancha turishini bilasizmi?)", "is_correct": False},
             ],
             "explanation": """
<p>Taklif → <strong>muloyim rad</strong> (미안해요 + sabab). Rad etilgan taklifning egasi
nima deydi? <mark style="background:#dcfce7;">Yangi vaqt taklif qiladi</mark>: 그럼 다음
주에 같이 봐요 ✅. ② radni eshitmaganday dam olish kuniga chaqiryapti — 20-darsdagi
tuzoqning aynan o'zi! ③ 고향 so'zini ilib olgan chalg'itish. Qoida ishladi: rad → 그럼
다음에/다음 주에…</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 이번 주말에 새로 나온 영화 같이 볼래요?<br>
    <em style="color:#475569;">Shu dam olish kunida yangi chiqqan kinoni birga ko'ramizmi?</em></p>
    <p><strong>남자:</strong> 미안해요. 주말에는 고향에 내려가야 해요.<br>
    <em style="color:#475569;">Kechirasiz. Dam olish kunlari yurtimga (qishlog'imga) tushishim kerak.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">그럼요 / 물론이죠</div><div class="pp-card-back">albatta-da</div></div>
  <div class="pp-card"><div class="pp-card-front">선약이 있다</div><div class="pp-card-back">oldindan va'dasi bor</div></div>
  <div class="pp-card"><div class="pp-card-front">축하해요</div><div class="pp-card-back">tabriklayman</div></div>
  <div class="pp-card"><div class="pp-card-front">아쉽네요</div><div class="pp-card-back">afsus-da</div></div>
  <div class="pp-card"><div class="pp-card-front">다행이네요</div><div class="pp-card-back">xayriyat, yaxshiyam</div></div>
  <div class="pp-card"><div class="pp-card-front">청첩장</div><div class="pp-card-back">to'y taklifnomasi</div></div>
  <div class="pp-card"><div class="pp-card-front">푹 쉬다</div><div class="pp-card-back">miriqib dam olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">고향에 내려가다</div><div class="pp-card-back">yurtiga (qishlog'iga) tushmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Javoblar 4 guruhdan: rozilik, muloyim rad, his-tuyg'u munosabati, taklif reaksiyasi.</li>
  <li>Avval xabar <strong>rangini</strong> aniqlang — teskari his-tuyg'u (kasalga 다행이네요) doimiy tuzoq.</li>
  <li>Rad etilgan taklifdan keyin — deyarli doim <strong>그럼 다음에…</strong></li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 22) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 이어질 말 3: To'liq amaliyot — beshta dialog imtihondagidek",
        "summary": "4–8-savollar to'liq to'plami: beshta mini-dialog, har biri bir marta eshitiladi — restoran, yo'l so'rash, ish, taklif, iltimos.",
        "order":   22,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 4, 5, 6, 7, 8-savollar</h2>
<p>Imtihondagi to'liq guruh — beshta qisqa dialog. Qoidalarni eslang: har audioni
<strong>bir marta</strong> eshiting, avval oxirgi gapning <strong>turini</strong> aniqlang
(savol / iltimos-taklif / xabar), keyin javobni tanlang. Boshladik!</p>
"""},
            {"rich_text": """
<p><strong>4-savol.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_022_1.mp3",
             "audio_script": [
                 ("여자", "손님, 주문하시겠어요?"),
                 ("남자", "네, 비빔밥 하나 주세요. 시간이 얼마나 걸려요?"),
             ],
             "choices": [
                 {"text": "십 분쯤 걸려요. (O'n daqiqacha ketadi.)", "is_correct": True},
                 {"text": "비빔밥은 팔천 원이에요. (Bibimbap sakkiz ming von.)", "is_correct": False},
                 {"text": "여기에서 드시고 가세요? (Shu yerda yeb ketasizmi?)", "is_correct": False},
                 {"text": "저도 비빔밥을 좋아해요. (Men ham bibimbapni yaxshi ko'raman.)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi gap — savol: <strong>시간이 얼마나 걸려요?</strong> (qancha VAQT ketadi?). Javob
aynan vaqt haqida: <mark style="background:#dcfce7;">십 분쯤 걸려요</mark> ✅. ② narx —
so'ralmagan (얼마예요? emas, 얼마나 걸려요? — farqiga e'tibor!). ③ savolga savol,
④ ofitsiant aytmaydigan gap. 얼마예요 (narx) ⇄ 얼마나 걸려요 (vaqt) juftligini
adashtirmang.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 손님, 주문하시겠어요?<br>
    <em style="color:#475569;">Mijoz, buyurtma berasizmi?</em></p>
    <p><strong>남자:</strong> 네, 비빔밥 하나 주세요. 시간이 얼마나 걸려요?<br>
    <em style="color:#475569;">Ha, bitta bibimbap bering. Qancha vaqt ketadi?</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>5-savol.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_022_2.mp3",
             "audio_script": [
                 ("남자", "실례합니다. 이 근처에 은행이 있어요?"),
                 ("여자", "네, 저기 사거리에서 왼쪽으로 가면 바로 보여요."),
             ],
             "choices": [
                 {"text": "감사합니다. 생각보다 가깝네요. (Rahmat. O'ylaganimdan yaqin ekan.)", "is_correct": True},
                 {"text": "은행이 벌써 문을 닫았어요. (Bank allaqachon yopilibdi.)", "is_correct": False},
                 {"text": "사거리가 어디에 있는지 모르겠어요? (Chorraha qayerdaligini bilmayapsizmi?)", "is_correct": False},
                 {"text": "저는 오른쪽 길로 갈게요. (Men o'ng tomondagi yo'ldan boraman.)", "is_correct": False},
             ],
             "explanation": """
<p>Yo'l ko'rsatildi (savol → javob allaqachon berildi!). Endi so'ragan odam nima deydi?
<mark style="background:#dcfce7;">Minnatdorchilik</mark>: 감사합니다 ✅ + tabiiy izoh
(가깝네요). ④ tushuntirishga teskari boradi (왼쪽 deyildi-ku!) — eshitmaganlik tuzog'i.
Yo'l so'rash dialoglari deyarli doim 감사합니다 bilan yopiladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 실례합니다. 이 근처에 은행이 있어요?<br>
    <em style="color:#475569;">Kechirasiz. Shu atrofda bank bormi?</em></p>
    <p><strong>여자:</strong> 네, 저기 사거리에서 왼쪽으로 가면 바로 보여요.<br>
    <em style="color:#475569;">Ha, anavi chorrahadan chapga yursangiz, darrov ko'rinadi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>6-savol.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_022_3.mp3",
             "audio_script": [
                 ("여자", "발표 자료 준비 다 됐어요?"),
                 ("남자", "아직요. 그래도 오늘 안에는 끝낼 수 있을 것 같아요."),
             ],
             "choices": [
                 {"text": "그럼 끝나는 대로 저한테 보내 주세요. (Unda tugashi bilan menga yuboring.)", "is_correct": True},
                 {"text": "발표가 정말 훌륭했어요. (Taqdimot juda zo'r bo'ldi.)", "is_correct": False},
                 {"text": "왜 벌써 다 끝냈어요? (Nega allaqachon tugatib qo'ydingiz?)", "is_correct": False},
                 {"text": "자료는 제가 어제 버렸어요. (Materiallarni kecha men tashlab yuborganman.)", "is_correct": False},
             ],
             "explanation": """
<p>Xabar: ish <strong>hali tugamagan</strong>, lekin bugun tugaydi. Boshliq/hamkasbning
tabiiy javobi — <mark style="background:#dcfce7;">keyingi qadamni belgilash</mark>:
끝나는 대로 보내 주세요 ✅ (~는 대로 = …shi bilanoq). ② va ③ hali bo'lmagan ishni
bo'lgan deb gapiradi — zamon tuzog'i: 아직 (hali) so'zini eshitgan odam bunga tushmaydi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 발표 자료 준비 다 됐어요?<br>
    <em style="color:#475569;">Taqdimot materiallari tayyor bo'ldimi?</em></p>
    <p><strong>남자:</strong> 아직요. 그래도 오늘 안에는 끝낼 수 있을 것 같아요.<br>
    <em style="color:#475569;">Hali yo'q. Shunday bo'lsa ham bugun ichida tugatsam kerak.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>7-savol.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_022_4.mp3",
             "audio_script": [
                 ("남자", "어제 간 콘서트 어땠어요?"),
                 ("여자", "정말 좋았어요. 다음에는 꼭 같이 가요."),
             ],
             "choices": [
                 {"text": "좋아요. 표 예매할 때 저한테도 알려 주세요. (Yaxshi. Chipta band qilganda menga ham ayting.)", "is_correct": True},
                 {"text": "저도 어제 콘서트에 갔어요. (Men ham kecha konsertga borganman.)", "is_correct": False},
                 {"text": "콘서트가 재미없었다니 아쉽네요. (Konsert qiziqmagan ekan, afsus.)", "is_correct": False},
                 {"text": "그럼 어제 왜 안 왔어요? (Unda kecha nega kelmadingiz?)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi gap — <strong>taklif</strong>: 다음에는 꼭 같이 가요 (keyingi safar albatta birga
boraylik). Taklifga javob — <mark style="background:#dcfce7;">rozilik + amaliy davom</mark>:
좋아요, 표 예매할 때 알려 주세요 ✅. ② mantiqsiz (birga bormagan edi-ku), ③ teskari rang
(정말 좋았어요 deyildi — 재미없었다 emas!). Taklifni eshitganda javobingiz 좋아요/그럼요
oilasidan boshlanishi tabiiy.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 어제 간 콘서트 어땠어요?<br>
    <em style="color:#475569;">Kecha borgan konsertingiz qanday bo'ldi?</em></p>
    <p><strong>여자:</strong> 정말 좋았어요. 다음에는 꼭 같이 가요.<br>
    <em style="color:#475569;">Juda zo'r bo'ldi. Keyingi safar albatta birga boraylik.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>8-savol.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_022_5.mp3",
             "audio_script": [
                 ("여자", "죄송한데 에어컨 좀 꺼 주시겠어요? 너무 추워서요."),
                 ("남자", "아, 그러셨어요? 몰랐네요."),
             ],
             "choices": [
                 {"text": "네, 바로 꺼 드릴게요. (Xo'p, hoziroq o'chirib beraman.)", "is_correct": True},
                 {"text": "네, 에어컨을 더 세게 틀게요. (Xo'p, konditsionerni yanada kuchaytiraman.)", "is_correct": False},
                 {"text": "날씨가 정말 덥네요. (Havo juda issiq-a.)", "is_correct": False},
                 {"text": "에어컨이 얼마인지 물어볼게요. (Konditsioner narxini so'rab ko'raman.)", "is_correct": False},
             ],
             "explanation": """
<p>Iltimos: 꺼 주시겠어요? (o'chirib bera olasizmi — 끄다 = o'chirmoq). Rozilikdan keyingi
tabiiy davom — <mark style="background:#dcfce7;">iltimosni bajarish</mark>: 바로 꺼 드릴게요 ✅
(~아/어 드릴게요 — hurmat bilan "qilib beraman"). ② teskari harakat (sovqotayotgan odamga
kuchaytirish!), ③ vaziyatga zid (추워서요 — sovuq deyildi). Iltimos fe'lini aniq ushlang:
끄다 (o'chirmoq) ≠ 켜다 (yoqmoq) — talaffuzi yaqin, ma'nosi qarama-qarshi!</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 죄송한데 에어컨 좀 꺼 주시겠어요? 너무 추워서요.<br>
    <em style="color:#475569;">Kechirasiz, konditsionerni o'chirib bera olasizmi? Juda sovqotib ketdim.</em></p>
    <p><strong>남자:</strong> 아, 그러셨어요? 몰랐네요.<br>
    <em style="color:#475569;">Voy, shundaymidi? Bilmabman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">얼마나 걸려요?</div><div class="pp-card-back">qancha vaqt ketadi?</div></div>
  <div class="pp-card"><div class="pp-card-front">사거리</div><div class="pp-card-back">chorraha</div></div>
  <div class="pp-card"><div class="pp-card-front">~는 대로</div><div class="pp-card-back">…shi bilanoq</div></div>
  <div class="pp-card"><div class="pp-card-front">표를 예매하다</div><div class="pp-card-back">chiptani oldindan band qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">끄다 / 켜다</div><div class="pp-card-back">o'chirmoq / yoqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~아/어 드릴게요</div><div class="pp-card-back">(hurmat bilan) qilib beraman</div></div>
  <div class="pp-card"><div class="pp-card-front">아직</div><div class="pp-card-back">hali (bo'lgani yo'q)</div></div>
  <div class="pp-card"><div class="pp-card-front">실례합니다</div><div class="pp-card-back">kechirasiz (murojaat)</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Oxirgi gap turi → javob turi: savol → aynan javob, iltimos/taklif → rozilik yoki rad, xabar → mos rang.</li>
  <li>Doimiy tuzoqlar: teskari his-tuyg'u, zamon xatosi (아직!), eshitilgan so'zni takrorlagan mantiqsiz variant.</li>
  <li>얼마예요 (narx) ≠ 얼마나 걸려요 (vaqt); 끄다 ≠ 켜다 — o'xshash juftlarga hushyor bo'ling.</li>
  <li>5 tadan 5 chiqdimi? Keyingi mavzu — 이어질 행동 (keyingi harakat)!</li>
</ul>
"""},
        ],
    },
]
