# TOPIK II Listening — 1–3-savollar: Mos rasm va grafik (그림·그래프), lessons 1–3 (orders 10–12).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_pics_1_3.py \
#            --out examprep/management/commands/audio/pics
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_pics_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/pics

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "1–3-savollar: Mos rasm va grafik (그림·그래프)",
    "summary": "Qisqa dialogni eshitib sahnani (qayerda? kim? nima?) va grafik savolida o'sish-kamayish tilini aniqlash.",
    "icon":    "bi-image",
    "order":   2,
}

LESSONS = [
    # ── Lesson 1 (order 10) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 그림 1: 1–3-savollar bilan tanishuv — sahnani eshitish",
        "summary": "Imtihonning birinchi savollari: qisqa dialogdan uchta narsani ushlash — qayerda, kim bilan, nima bo'lyapti.",
        "order":   10,
        "blocks": [
            {"rich_text": """
<h2>🖼️ 1–3-savollar: eng birinchi audio — sahnani toping</h2>
<p>듣기 bo'limi shu savollar bilan boshlanadi: <strong>ikki-uch replikali qisqa dialog</strong>
eshitiladi, siz unga mos <strong>rasmni</strong> tanlaysiz (3-savolda esa — mos
<strong>grafikni</strong>, keyingi darsda ko'ramiz).</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>1–2.</strong> 다음을 듣고 가장 알맞은 그림을 고르십시오. —
  <em>Eshitib, eng mos rasmni tanlang.</em></p>
</div>
<p>Rasmni tanlash uchun eshitayotganda <strong>uchta savolga</strong> javob toping:</p>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>1. 어디? (Qayerda?)</strong> — joyni ochiq aytishmaydi, lekin
  <em>imzo-iboralar</em> fosh qiladi: 뭘 드릴까요? → do'kon/kafe, 어디가 아프세요? → shifoxona,
  어디까지 가세요? → taksi, 소포를 보내고 싶은데요 → pochta.</p></div>
  <div class="pp-step"><p><strong>2. 누구? (Kim bilan kim?)</strong> — sotuvchi-xaridor?
  Shifokor-bemor? Do'stlar? Buni <em>muomala ohangi</em> aytadi (손님, 어서 오세요 →
  xizmat ko'rsatish).</p></div>
  <div class="pp-step"><p><strong>3. 무엇을? (Nima qilyapti?)</strong> — oxirgi replikaga e'tibor:
  ko'pincha harakat aynan u yerda aniqlashadi (입어 보세요 → kiyib ko'ryapti, 올려 주세요 →
  qo'yyapti).</p></div>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Maslahat:</strong> Audio <strong>bir marta</strong> eshittiriladi (1–20-savollar).
  Shuning uchun audio boshlanishidan OLDIN rasmlarga qarab, ular orasidagi <strong>farqni</strong>
  toping: joy farq qiladimi? Harakat farq qiladimi? Keyin faqat o'sha farqni eshiting.
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Bizning mashqlarda rasm o'rniga <strong>vaziyat tavsiflari</strong>
  beriladi — ko'nikma aynan bir xil: sahnani eshitib aniqlash. Imtihonda shu tavsif sizning
  xayolingizdagi rasm bo'ladi.
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: birga tahlil qilamiz</h3>
<p>Avval audioni <strong>skriptni ochmasdan</strong> eshiting. Uchta savolga javob toping:
qayerda? kim? nima?</p>
""",
             "audio": "topik_l_010_1.mp3",
             "audio_script": [
                 ("여자", "어서 오세요. 뭘 드릴까요?"),
                 ("남자", "사과 다섯 개 주세요. 얼마예요?"),
                 ("여자", "만 원입니다. 봉지에 넣어 드릴게요."),
             ]},
            {"rich_text": """
<p>Endi tahlil: nimalarni eshitdingiz?</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>어디?</strong> — 뭘 드릴까요? + 사과 → meva do'koni/bozor</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>누구?</strong> — 어서 오세요 (xizmat ohangi) → sotuvchi (여자) va xaridor (남자)</p>
  <p style="font-size:1.05em;margin:0;"><strong>무엇을?</strong> — 사과 다섯 개 주세요 → erkak olma sotib olyapti</p>
</div>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 어서 오세요. 뭘 드릴까요?<br>
    <em style="color:#475569;">Xush kelibsiz. Nima beray?</em></p>
    <p><strong>남자:</strong> 사과 다섯 개 주세요. 얼마예요?<br>
    <em style="color:#475569;">Beshta olma bering. Qancha turadi?</em></p>
    <p><strong>여자:</strong> 만 원입니다. 봉지에 넣어 드릴게요.<br>
    <em style="color:#475569;">O'n ming von. Xaltaga solib beraman.</em></p>
  </div>
</details>
<h3>Joy imzo-iboralari lug'ati</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>주문하시겠어요? / 여기 메뉴판이요</strong> → 식당·카페 (restoran/kafe)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>어디가 아프세요? / 처방전</strong> → 병원·약국 (shifoxona/dorixona)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>어디까지 가세요? / 길이 막히네요</strong> → 택시 (taksi)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>소포를 보내고 싶은데요 / 저울</strong> → 우체국 (pochta)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>통장을 만들고 싶은데요 / 번호표</strong> → 은행 (bank)</p>
  <p style="font-size:1.05em;margin:0;"><strong>이 책을 빌리고 싶은데요 / 반납</strong> → 도서관 (kutubxona)</p>
</div>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 듣고 대화에 맞는 상황을 고르십시오.
<em>(Eshitib, dialogga mos vaziyatni tanlang.)</em></p>
""",
             "audio": "topik_l_010_2.mp3",
             "audio_script": [
                 ("남자", "이 소포를 부산으로 보내고 싶은데요."),
                 ("여자", "네, 소포를 저울 위에 올려 주세요."),
                 ("남자", "언제쯤 도착할까요?"),
                 ("여자", "내일 오후에는 도착할 거예요."),
             ],
             "choices": [
                 {"text": "남자가 우체국에서 소포를 보내고 있다. (Erkak pochtada jo'natma yuboryapti.)", "is_correct": True},
                 {"text": "남자가 은행에서 돈을 찾고 있다. (Erkak bankda pul yechyapti.)", "is_correct": False},
                 {"text": "남자가 가게에서 상자를 사고 있다. (Erkak do'konda quti sotib olyapti.)", "is_correct": False},
                 {"text": "남자가 공항에서 비행기를 기다리고 있다. (Erkak aeroportda samolyot kutyapti.)", "is_correct": False},
             ],
             "explanation": """
<p>Kalit qator — birinchi replika: <strong>"소포를 부산으로 보내고 싶은데요"</strong>
(jo'natmani Busanga yubormoqchiman) + <strong>저울</strong> (tarozi) → bu
<mark style="background:#dcfce7;">pochta</mark> ✅. 상자 (quti) eshitilgani uchun ③ tuzoq
bo'lishi mumkin, lekin u SOTIB olinmayapti — yuborilyapti.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 이 소포를 부산으로 보내고 싶은데요.<br>
    <em style="color:#475569;">Bu jo'natmani Busanga yubormoqchi edim.</em></p>
    <p><strong>여자:</strong> 네, 소포를 저울 위에 올려 주세요.<br>
    <em style="color:#475569;">Xo'p, jo'natmani tarozi ustiga qo'ying.</em></p>
    <p><strong>남자:</strong> 언제쯤 도착할까요?<br>
    <em style="color:#475569;">Qachonlarda yetib boradi?</em></p>
    <p><strong>여자:</strong> 내일 오후에는 도착할 거예요.<br>
    <em style="color:#475569;">Ertaga tushdan keyin yetib boradi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 듣고 대화에 맞는 상황을 고르십시오.</p>
""",
             "audio": "topik_l_010_3.mp3",
             "audio_script": [
                 ("여자", "머리가 아프고 열이 나요."),
                 ("남자", "언제부터 그러셨어요?"),
                 ("여자", "어제저녁부터요. 목도 좀 아파요."),
                 ("남자", "감기인 것 같네요. 약을 처방해 드릴게요."),
             ],
             "choices": [
                 {"text": "여자가 병원에서 진료를 받고 있다. (Ayol shifoxonada ko'rikdan o'tyapti.)", "is_correct": True},
                 {"text": "여자가 약국에서 약을 사고 있다. (Ayol dorixonada dori sotib olyapti.)", "is_correct": False},
                 {"text": "여자가 집에서 쉬고 있다. (Ayol uyda dam olyapti.)", "is_correct": False},
                 {"text": "여자가 체육관에서 운동하고 있다. (Ayol sport zalida shug'ullanyapti.)", "is_correct": False},
             ],
             "explanation": """
<p>Imzo-iboralar: <strong>어디가 아프세요?</strong> turidagi savol-javob (아프고 열이 나요 —
og'riq va isitma) + oxirida <strong>약을 처방해 드릴게요</strong> (dori yozib beraman —
faqat SHIFOKOR shunday deydi!) → <mark style="background:#dcfce7;">shifoxona, ko'rik</mark> ✅.
② tuzoq: 약 so'zi eshitildi, lekin dori endi yozilyapti — hali sotib olinmayapti.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 머리가 아프고 열이 나요.<br>
    <em style="color:#475569;">Boshim og'riyapti va isitmam bor.</em></p>
    <p><strong>남자:</strong> 언제부터 그러셨어요?<br>
    <em style="color:#475569;">Qachondan beri shunday?</em></p>
    <p><strong>여자:</strong> 어제저녁부터요. 목도 좀 아파요.<br>
    <em style="color:#475569;">Kecha kechqurundan beri. Tomog'im ham biroz og'riyapti.</em></p>
    <p><strong>남자:</strong> 감기인 것 같네요. 약을 처방해 드릴게요.<br>
    <em style="color:#475569;">Shamollaganga o'xshaysiz. Dori yozib beraman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">소포</div><div class="pp-card-back">jo'natma, posilka</div></div>
  <div class="pp-card"><div class="pp-card-front">저울</div><div class="pp-card-back">tarozi</div></div>
  <div class="pp-card"><div class="pp-card-front">열이 나다</div><div class="pp-card-back">isitmasi chiqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">처방하다</div><div class="pp-card-back">(dori) yozib bermoq</div></div>
  <div class="pp-card"><div class="pp-card-front">주문하다</div><div class="pp-card-back">buyurtma bermoq</div></div>
  <div class="pp-card"><div class="pp-card-front">도착하다</div><div class="pp-card-back">yetib bormoq</div></div>
  <div class="pp-card"><div class="pp-card-front">진료를 받다</div><div class="pp-card-back">ko'rikdan o'tmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">봉지</div><div class="pp-card-back">xalta, paket</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Eshitayotganda uch savol: <strong>어디? 누구? 무엇을?</strong></li>
  <li>Joyni imzo-iboralar fosh qiladi (처방 → shifokor, 저울 → pochta, 어디까지 가세요 → taksi).</li>
  <li>Audio boshlanishidan oldin variantlar orasidagi <strong>farqni</strong> toping va faqat o'shani eshiting.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 11) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 그림 2: Grafikni quloq bilan o'qish (3-savol)",
        "summary": "3-savol: statistika matnini eshitib mos grafikni tanlash — o'sish, kamayish, ikki baravar, eng ko'p tili.",
        "order":   11,
        "blocks": [
            {"rich_text": """
<h2>📊 3-savol: grafik tili — 늘다, 줄다, 두 배</h2>
<p>3-savolda qisqa <strong>yangilik/statistika matni</strong> eshitiladi va unga mos
<strong>grafikni</strong> tanlaysiz. Grafiklar odatda ikki narsada farqlanadi:
<strong>yo'nalish</strong> (o'syaptimi, kamayayaptimi?) va <strong>tartib</strong>
(qaysi eng ko'p, qaysi keyingi?).</p>
<h3>O'sish–kamayish lug'ati</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>늘다 / 증가하다</strong> — ko'paymoq ↗ &nbsp;|&nbsp; <strong>줄다 / 감소하다</strong> — kamaymoq ↘</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>꾸준히</strong> — barqaror, to'xtovsiz &nbsp;|&nbsp; <strong>급격히 / 크게</strong> — keskin</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>두 배가 되다</strong> — ikki baravar bo'lmoq &nbsp;|&nbsp; <strong>절반</strong> — yarmi</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>가장 많다 / 1위를 차지하다</strong> — eng ko'p / 1-o'rinni egallamoq</p>
  <p style="font-size:1.05em;margin:0;"><strong>이어서 / 그 뒤를 잇다</strong> — undan keyin / ketidan kelmoq (2-, 3-o'rin!)</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> Raqamlar kelganda ularni <strong>yozib oling</strong> (10% → 20%).
  Tartib kelganda birinchi aytilgani — <strong>1-o'rin</strong>, 이어서dan keyingilari —
  2- va 3-o'rin. Grafik variantlari ko'pincha aynan shu tartibni almashtirib tuzoq qo'yadi.
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna: eshitib grafikni tasavvur qiling</h3>
<p>Skriptni ochmasdan eshiting. Savol: nima o'zgardi va qancha?</p>
""",
             "audio": "topik_l_011_1.mp3",
             "audio_script": [
                 ("남자", "지난해 자전거로 출근하는 사람이 크게 늘었습니다. 2020년에는 전체의 10퍼센트였지만 지난해에는 20퍼센트로 두 배가 되었습니다. 전문가들은 이런 변화가 계속될 것으로 보고 있습니다."),
             ]},
            {"rich_text": """
<p>Eshitdingizmi? <strong>10% → 20%, 두 배</strong> (ikki baravar) — demak to'g'ri grafik:
pastdan yuqoriga <strong>ko'tarilgan</strong> chiziq, oxirgi ustun avvalgisidan ikki marta baland.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 지난해 자전거로 출근하는 사람이 크게 늘었습니다. 2020년에는 전체의
    10퍼센트였지만 지난해에는 20퍼센트로 두 배가 되었습니다. 전문가들은 이런 변화가 계속될
    것으로 보고 있습니다.<br>
    <em style="color:#475569;">O'tgan yili velosipedda ishga boradiganlar keskin ko'paydi.
    2020-yilda ular jami odamlarning 10 foizi edi, o'tgan yili esa 20 foizga yetib, ikki baravar
    bo'ldi. Mutaxassislar bu o'zgarish davom etadi deb hisoblashmoqda.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 1.</strong> 다음을 듣고 내용과 맞는 것을 고르십시오.
<em>(Eshitib, mazmunga mos grafikni tanlang.)</em></p>
""",
             "audio": "topik_l_011_2.mp3",
             "audio_script": [
                 ("여자", "최근 조사에 따르면 대학생들이 여가 시간에 가장 많이 하는 활동은 게임으로 나타났습니다. 이어서 운동이 2위, 여행이 3위를 차지했습니다."),
             ],
             "choices": [
                 {"text": "1위 게임, 2위 운동, 3위 여행 (1-o'rin o'yin, 2-o'rin sport, 3-o'rin sayohat)", "is_correct": True},
                 {"text": "1위 운동, 2위 게임, 3위 여행 (1-o'rin sport, 2-o'rin o'yin, 3-o'rin sayohat)", "is_correct": False},
                 {"text": "1위 여행, 2위 운동, 3위 게임 (1-o'rin sayohat, 2-o'rin sport, 3-o'rin o'yin)", "is_correct": False},
                 {"text": "1위 게임, 2위 여행, 3위 운동 (1-o'rin o'yin, 2-o'rin sayohat, 3-o'rin sport)", "is_correct": False},
             ],
             "explanation": """
<p>Tartib tili: <strong>가장 많이 하는 활동은 게임</strong> (eng ko'p — o'yin, 1-o'rin),
keyin <strong>이어서</strong> signali: 운동이 <strong>2위</strong>, 여행이 <strong>3위</strong> →
✅ ①. Imtihonda grafik variantlari aynan shu tartibning almashtirilgan versiyalari bo'ladi —
이어서dan keyingi ketma-ketlikni aniq yozib oling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 최근 조사에 따르면 대학생들이 여가 시간에 가장 많이 하는 활동은
    게임으로 나타났습니다. 이어서 운동이 2위, 여행이 3위를 차지했습니다.<br>
    <em style="color:#475569;">So'nggi so'rovga ko'ra, talabalar bo'sh vaqtida eng ko'p
    shug'ullanadigan mashg'ulot o'yin ekani ma'lum bo'ldi. Undan keyin sport 2-o'rinni,
    sayohat 3-o'rinni egalladi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2.</strong> 다음을 듣고 내용과 맞는 것을 고르십시오.</p>
""",
             "audio": "topik_l_011_3.mp3",
             "audio_script": [
                 ("남자", "종이 신문을 읽는 사람은 해마다 꾸준히 줄고 있습니다. 반면에 스마트폰으로 뉴스를 보는 사람은 급격히 늘어서 지난해에는 전체의 절반을 넘었습니다."),
             ],
             "choices": [
                 {"text": "종이 신문은 꾸준히 줄고, 스마트폰 뉴스는 절반을 넘게 늘었다. (Qog'oz gazeta barqaror kamaygan, smartfon yangiliklari yarmidan oshib ketgan.)", "is_correct": True},
                 {"text": "종이 신문과 스마트폰 뉴스가 모두 줄고 있다. (Ikkalasi ham kamaymoqda.)", "is_correct": False},
                 {"text": "종이 신문을 읽는 사람이 절반을 넘었다. (Qog'oz gazeta o'quvchilari yarmidan oshgan.)", "is_correct": False},
                 {"text": "스마트폰 뉴스는 천천히 늘고 있다. (Smartfon yangiliklari sekin o'smoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Ikki chiziqli grafik: 종이 신문 → <strong>꾸준히 줄고</strong> (barqaror pasayish ↘),
스마트폰 → <strong>급격히 늘어</strong> + <strong>절반을 넘었습니다</strong> (keskin o'sish,
50%dan yuqori ↗) → ✅ ①. <strong>반면에</strong> (aksincha) signali ikki qarama-qarshi
yo'nalishni bog'laydi — uni eshitsangiz, grafikda bir chiziq tushib, biri ko'tarilishi kerak.
④ tuzoq: o'sish bor, lekin 급격히 ≠ sekin.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 종이 신문을 읽는 사람은 해마다 꾸준히 줄고 있습니다. 반면에
    스마트폰으로 뉴스를 보는 사람은 급격히 늘어서 지난해에는 전체의 절반을 넘었습니다.<br>
    <em style="color:#475569;">Qog'oz gazeta o'qiydiganlar yildan-yilga barqaror kamaymoqda.
    Aksincha, smartfonda yangilik ko'radiganlar keskin ko'payib, o'tgan yili jami odamlarning
    yarmidan oshdi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">늘다 / 증가하다</div><div class="pp-card-back">ko'paymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">줄다 / 감소하다</div><div class="pp-card-back">kamaymoq</div></div>
  <div class="pp-card"><div class="pp-card-front">꾸준히</div><div class="pp-card-back">barqaror, to'xtovsiz</div></div>
  <div class="pp-card"><div class="pp-card-front">급격히</div><div class="pp-card-back">keskin</div></div>
  <div class="pp-card"><div class="pp-card-front">두 배가 되다</div><div class="pp-card-back">ikki baravar bo'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">절반을 넘다</div><div class="pp-card-back">yarmidan oshmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">1위를 차지하다</div><div class="pp-card-back">1-o'rinni egallamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">반면에</div><div class="pp-card-back">aksincha, buning teskarisi</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Grafik savolida ikki narsani ushlang: <strong>yo'nalish</strong> (늘다/줄다) va <strong>tartib</strong> (가장 → 이어서).</li>
  <li>Raqamlarni yozib oling; 두 배 / 절반 nisbatlarga aylantiring.</li>
  <li>반면에 = grafikda ikki qarama-qarshi chiziq.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 12) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 그림 3: To'liq amaliyot — imtihon formatida",
        "summary": "1–3-savollar to'liq to'plami imtihondagidek: ikki sahna dialogi + bitta grafik matni, har biri bir marta eshitiladi.",
        "order":   12,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 1, 2, 3-savollar ketma-ket</h2>
<p>Endi imtihondagidek ishlaymiz: uchta savol, har audioni <strong>faqat bir marta</strong>
eshiting (haqiqiy imtihonda qayta eshittirilmaydi!). Har savoldan oldin variantlarni o'qib,
<strong>farqlarni</strong> belgilang — keyin play tugmasini bosing.</p>
"""},
            {"rich_text": """
<p><strong>1-savol.</strong> 다음을 듣고 대화에 맞는 상황을 고르십시오.</p>
""",
             "audio": "topik_l_012_1.mp3",
             "audio_script": [
                 ("여자", "손님, 이 옷 한번 입어 보세요. 요즘 인기가 많아요."),
                 ("남자", "음, 저한테는 좀 큰 것 같은데요. 작은 사이즈 있어요?"),
                 ("여자", "네, 있어요. 잠시만 기다리세요."),
             ],
             "choices": [
                 {"text": "남자가 옷 가게에서 옷을 입어 보고 있다. (Erkak kiyim do'konida kiyim kiyib ko'ryapti.)", "is_correct": True},
                 {"text": "남자가 세탁소에 옷을 맡기고 있다. (Erkak kimyoviy tozalashga kiyim topshiryapti.)", "is_correct": False},
                 {"text": "여자가 시장에서 옷을 팔고 있지만 손님이 없다. (Ayol bozorda kiyim sotyapti, lekin xaridor yo'q.)", "is_correct": False},
                 {"text": "남자가 집에서 옷장을 정리하고 있다. (Erkak uyda shkafini tartiblayapti.)", "is_correct": False},
             ],
             "explanation": """
<p>Imzo-iboralar: <strong>손님</strong> (mijoz!) + <strong>입어 보세요</strong> (kiyib
ko'ring) + <strong>작은 사이즈 있어요?</strong> → kiyim do'koni, erkak kiyim o'lchayapti ✅.
③ tuzoq emas — ayol sotuvchi, LEKIN xaridor bor (남자). Harakatni oxirgi replika
tasdiqlaydi: 잠시만 기다리세요 — kichik o'lcham olib kelinyapti.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 손님, 이 옷 한번 입어 보세요. 요즘 인기가 많아요.<br>
    <em style="color:#475569;">Mijoz, bu kiyimni bir kiyib ko'ring. Hozir juda ommabop.</em></p>
    <p><strong>남자:</strong> 음, 저한테는 좀 큰 것 같은데요. 작은 사이즈 있어요?<br>
    <em style="color:#475569;">Hm, menga biroz kattaga o'xshayapti. Kichikroq o'lchami bormi?</em></p>
    <p><strong>여자:</strong> 네, 있어요. 잠시만 기다리세요.<br>
    <em style="color:#475569;">Ha, bor. Bir oz kuting.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>2-savol.</strong> 다음을 듣고 대화에 맞는 상황을 고르십시오.</p>
""",
             "audio": "topik_l_012_2.mp3",
             "audio_script": [
                 ("남자", "어서 오세요. 어디까지 가세요?"),
                 ("여자", "시청역까지 가 주세요. 오늘따라 길이 많이 막히네요."),
                 ("남자", "네, 퇴근 시간이라서요. 그래도 삼십 분이면 도착할 거예요."),
             ],
             "choices": [
                 {"text": "여자가 택시를 타고 시청역으로 가고 있다. (Ayol taksida Sichhon bekati tomon ketyapti.)", "is_correct": True},
                 {"text": "여자가 지하철을 기다리고 있다. (Ayol metro kutyapti.)", "is_correct": False},
                 {"text": "남자가 버스를 운전해서 공항으로 가고 있다. (Erkak avtobus haydab aeroportga ketyapti.)", "is_correct": False},
                 {"text": "두 사람이 시청에서 회의를 하고 있다. (Ikki kishi hokimiyatda majlis qilyapti.)", "is_correct": False},
             ],
             "explanation": """
<p><strong>어디까지 가세요?</strong> — taksi haydovchisining imzo-savoli! + <strong>가
주세요</strong> (…gacha olib boring) + 길이 막히네요 (yo'l tiqilinch) → taksi ✅.
② tuzoq: 시청<strong>역</strong> (bekat) eshitildi, lekin ayol metroDA emas — bekatGAcha
taksida ketyapti. Joy nomi eshitilishi hali javob emas — <strong>harakat</strong> hal qiladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 어서 오세요. 어디까지 가세요?<br>
    <em style="color:#475569;">Keling. Qayergacha borasiz?</em></p>
    <p><strong>여자:</strong> 시청역까지 가 주세요. 오늘따라 길이 많이 막히네요.<br>
    <em style="color:#475569;">Sichhon bekatigacha olib boring. Bugun negadir yo'l juda tiqilinch.</em></p>
    <p><strong>남자:</strong> 네, 퇴근 시간이라서요. 그래도 삼십 분이면 도착할 거예요.<br>
    <em style="color:#475569;">Ha, ishdan qaytish vaqti-da. Shunday bo'lsa ham o'ttiz daqiqada yetib boramiz.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>3-savol.</strong> 다음을 듣고 내용과 맞는 것을 고르십시오.</p>
""",
             "audio": "topik_l_012_3.mp3",
             "audio_script": [
                 ("여자", "한 조사에 따르면 혼자 사는 사람이 해마다 늘고 있습니다. 나이별로 보면 20대가 가장 많았고, 30대와 60대가 그 뒤를 이었습니다."),
             ],
             "choices": [
                 {"text": "혼자 사는 사람이 늘고 있으며 20대가 가장 많다. (Yolg'iz yashovchilar ko'paymoqda, eng ko'pi 20 yoshlilar.)", "is_correct": True},
                 {"text": "혼자 사는 사람이 해마다 줄고 있다. (Yolg'iz yashovchilar yildan-yilga kamaymoqda.)", "is_correct": False},
                 {"text": "혼자 사는 사람 중에 60대가 가장 많다. (Yolg'iz yashovchilar orasida eng ko'pi 60 yoshlilar.)", "is_correct": False},
                 {"text": "30대는 혼자 사는 사람이 거의 없다. (30 yoshlilar orasida yolg'iz yashovchi deyarli yo'q.)", "is_correct": False},
             ],
             "explanation": """
<p>Yo'nalish: <strong>해마다 늘고</strong> (yildan-yilga ko'paymoqda ↗) — ② darhol yo'qoladi.
Tartib: <strong>20대가 가장 많았고</strong> (1-o'rin!), 그 뒤를 이었습니다 → 30대, 60대 (2-,
3-o'rin) → ✅ ①. ③ tartibni teskari qilgan tuzoq, ④ matnda umuman yo'q. 6 ta savoldan
nechtasini bir eshitishda oldingiz? Barchasini olgan bo'lsangiz — bu blok sizniki! 🎉</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 한 조사에 따르면 혼자 사는 사람이 해마다 늘고 있습니다. 나이별로
    보면 20대가 가장 많았고, 30대와 60대가 그 뒤를 이었습니다.<br>
    <em style="color:#475569;">Bir so'rovga ko'ra, yolg'iz yashovchilar yildan-yilga ko'paymoqda.
    Yosh bo'yicha qaralsa, 20 yoshlilar eng ko'p bo'lgan, ularning ketidan 30 va 60 yoshlilar
    kelgan.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">입어 보다</div><div class="pp-card-back">kiyib ko'rmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">사이즈</div><div class="pp-card-back">o'lcham</div></div>
  <div class="pp-card"><div class="pp-card-front">길이 막히다</div><div class="pp-card-back">yo'l tiqilinch bo'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">퇴근 시간</div><div class="pp-card-back">ishdan qaytish vaqti</div></div>
  <div class="pp-card"><div class="pp-card-front">혼자 살다</div><div class="pp-card-back">yolg'iz yashamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">나이별로</div><div class="pp-card-back">yosh bo'yicha</div></div>
  <div class="pp-card"><div class="pp-card-front">그 뒤를 잇다</div><div class="pp-card-back">ketidan kelmoq (keyingi o'rin)</div></div>
  <div class="pp-card"><div class="pp-card-front">조사에 따르면</div><div class="pp-card-back">so'rovga ko'ra</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Sahna savoli: <strong>어디? 누구? 무엇을?</strong> — imzo-iboralarni tinglang.</li>
  <li>So'z eshitilishi ≠ javob: 시청역 eshitildi, lekin harakat taksida! Har doim <strong>harakatni</strong> tekshiring.</li>
  <li>Grafik: yo'nalish (늘다/줄다) + tartib (가장 → 이어서 → 그 뒤를 이었습니다).</li>
  <li>Har audio faqat <strong>bir marta</strong> — variantlardagi farqni oldindan belgilang.</li>
</ul>
"""},
        ],
    },
]
