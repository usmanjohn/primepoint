# TOPIK II Listening — 21–24-savollar: Juft savollar I (중심 생각·하는 일 + 내용), lessons 1–3 (orders 60–62).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_pair_1_3.py \
#            --out examprep/management/commands/audio/pair
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_pair_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/pair

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "21–24-savollar: Juft savollar I (중심 생각·하는 일 + 내용)",
    "summary": "Bitta suhbat — ikkita savol: birinchi eshitishda fikr yoki harakatni, ikkinchisida faktlarni ushlash.",
    "icon":    "bi-collection",
    "order":   7,
}

LESSONS = [
    # ── Lesson 1 (order 60) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 짝 문제 1: 21–24-savollar bilan tanishuv — bitta audio, ikki savol",
        "summary": "Juft savollar davri boshlanadi: audio ikki marta eshittiriladi — har eshitishga o'z vazifasini bering.",
        "order":   60,
        "blocks": [
            {"rich_text": """
<h2>👯 21-savoldan boshlab hammasi juft-juft</h2>
<p>Bu yerdan imtihonning qolgan qismi (21–50) bir xil qolipda: <strong>bitta matn — ikkita
savol</strong>, va audio endi <strong>IKKI marta</strong> eshittiriladi. Bu yaxshi yangilik —
lekin faqat reja bilan ishlasangiz:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>21.</strong> 남자의 중심 생각으로 알맞은 것을 고르십시오. — <em>erkakning asosiy fikri (tanish!).</em></p>
  <p style="font-size:1.08em;margin:0;"><strong>22.</strong> 들은 내용과 같은 것을 고르십시오. — <em>mazmun mosligi (tanish!).</em></p>
</div>
<h3>Ikki eshitish — ikki vazifa</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step"><p><strong>Audio boshlanishidan oldin:</strong> IKKALA savolning variantlarini
  o'qing. 21 uchun fikr so'zlarini, 22 uchun fakt farqlarini (raqam, kim, qachon) belgilang.</p></div>
  <div class="pp-step"><p><strong>Birinchi eshitish:</strong> faqat <strong>1-savol</strong>ga quloq
  soling — erkakning fikri (-는 게 좋다, -아야 하다…). Topganingizni darhol belgilang.</p></div>
  <div class="pp-step"><p><strong>Ikkinchi eshitish:</strong> endi faqat <strong>2-savol</strong> —
  variantlarni birma-bir faktlar bilan solishtirib, zidlarini chizing (소거법).</p></div>
</div>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Eng katta xato — ikkala eshitishda ham "umuman" tinglash:
  natijada ikkala savol ham chala qoladi. Har eshitishga <strong>bitta aniq vazifa</strong>
  bering. Mashqlarimizda ham audioni ikki marta eshiting — imtihondagidek!
</div>
"""},
            {"rich_text": """
<h3>🎧 Namuna juftlik: birga ishlaymiz</h3>
<p>Quyida bitta suhbat va ikkita savol. Avval ikkala savolning variantlarini o'qing, keyin
audioni <strong>birinchi marta</strong> eshiting — faqat erkakning fikri uchun.</p>
<p><strong>21-savol.</strong> 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_060_1.mp3",
             "audio_script": [
                 ("여자", "요즘은 물건을 안 사고 빌려 쓰는 사람이 많대요. 카메라나 캠핑용품도 빌릴 수 있고요."),
                 ("남자", "네, 저도 지난 여행 때 카메라를 빌려서 썼는데 아주 좋았어요. 가끔 쓰는 물건은 사는 것보다 빌리는 게 경제적인 것 같아요."),
                 ("여자", "맞아요. 안 쓸 때 보관할 곳을 찾지 않아도 되고요."),
             ],
             "choices": [
                 {"text": "가끔 쓰는 물건은 빌리는 것이 경제적이다. (Ahyon-ahyonda ishlatiladigan narsani ijaraga olgan tejamli.)", "is_correct": True},
                 {"text": "카메라는 꼭 사서 써야 한다. (Kamerani albatta sotib olib ishlatish kerak.)", "is_correct": False},
                 {"text": "여행을 자주 가는 것이 좋다. (Tez-tez sayohatga borgan yaxshi.)", "is_correct": False},
                 {"text": "물건을 보관할 곳이 많아야 한다. (Narsalarni saqlash joyi ko'p bo'lishi kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Fikr tugallanmasi: 빌리는 게 <strong>경제적인 것 같아요</strong> → ✅ ①. Sayohatdagi
kamera — bu FIKR emas, uni qo'llovchi <strong>misol</strong> (③ o'sha misolni fikr qilib
ko'rsatgan tor tuzoq). ④ ayolning gapidan yasalgan, ustiga buzib (saqlash joyi kerak
<strong>emas</strong>ligi afzallik edi!). Endi audioni <strong>ikkinchi marta</strong>
eshiting — pastdagi 22-savol uchun faktlarni tering.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 요즘은 물건을 안 사고 빌려 쓰는 사람이 많대요. 카메라나 캠핑용품도 빌릴 수 있고요.<br>
    <em style="color:#475569;">Hozir narsalarni sotib olmasdan ijaraga olib ishlatadiganlar ko'p ekan. Kamera va kemping jihozlarini ham ijaraga olsa bo'larkan.</em></p>
    <p><strong>남자:</strong> 네, 저도 지난 여행 때 카메라를 빌려서 썼는데 아주 좋았어요. 가끔 쓰는 물건은 사는 것보다 빌리는 게 경제적인 것 같아요.<br>
    <em style="color:#475569;">Ha, men ham o'tgan sayohatda kamerani ijaraga olib ishlatgandim, juda yaxshi bo'ldi. Ahyon-ahyonda ishlatiladigan narsani sotib olishdan ko'ra ijaraga olgan tejamli-ov.</em></p>
    <p><strong>여자:</strong> 맞아요. 안 쓸 때 보관할 곳을 찾지 않아도 되고요.<br>
    <em style="color:#475569;">To'g'ri. Ishlatilmayotganda saqlaydigan joy qidirish ham shart emas.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>22-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida — ikkinchi
marta eshiting)</em></p>
""",
             "choices": [
                 {"text": "남자는 여행 때 카메라를 빌려서 사용했다. (Erkak sayohatda kamerani ijaraga olib ishlatgan.)", "is_correct": True},
                 {"text": "남자는 여행 때 카메라를 새로 샀다. (Erkak sayohatda yangi kamera sotib olgan.)", "is_correct": False},
                 {"text": "캠핑용품은 빌릴 수 없다. (Kemping jihozlarini ijaraga olib bo'lmaydi.)", "is_correct": False},
                 {"text": "물건을 빌리면 보관할 곳이 필요하다. (Narsani ijaraga olsangiz, saqlash joyi kerak bo'ladi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② asosiy fe'l almashtirilgan (<strong>빌려서</strong> 썼어요 — ijaraga olgan,
sotib olmagan!), ③ teskari (빌릴 수 <strong>있고요</strong>), ④ teskari (찾지 않아도
<strong>되고요</strong> — kerak emas!). ✅ ①. Ko'rdingizmi: birinchi eshitishda fikr,
ikkinchisida faktlar — ikkala savol ham to'liq yig'ildi. Bu reja endi 50-savolgacha
sizning asosiy qurolingiz.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">빌리다</div><div class="pp-card-back">ijaraga olmoq, vaqtincha olmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">캠핑용품</div><div class="pp-card-back">kemping jihozlari</div></div>
  <div class="pp-card"><div class="pp-card-front">경제적</div><div class="pp-card-back">tejamli, iqtisodiy</div></div>
  <div class="pp-card"><div class="pp-card-front">보관하다</div><div class="pp-card-back">saqlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">가끔</div><div class="pp-card-back">ahyon-ahyonda</div></div>
  <div class="pp-card"><div class="pp-card-front">~는 것 같아요</div><div class="pp-card-back">…ga o'xshaydi (yumshoq fikr)</div></div>
  <div class="pp-card"><div class="pp-card-front">~대요 / ~래요</div><div class="pp-card-back">…ekan (eshitgan gap)</div></div>
  <div class="pp-card"><div class="pp-card-front">짝 문제</div><div class="pp-card-back">juft savol</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>21-savoldan boshlab: bitta audio (ikki marta) — ikkita savol.</li>
  <li>Har eshitishga bitta vazifa: 1-eshitish → fikr/harakat, 2-eshitish → faktlar (소거법).</li>
  <li>Audio oldidan IKKALA savolning variantlarini o'qib qo'ying.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 61) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 짝 문제 2: U nima qilyapti? (하는 일) — telefon suhbatlari",
        "summary": "23–24-savollar: qatnashchi NIMA QILAYOTGANINI aytish (문의·신청·항의·변경) — xizmat telefon suhbatlari tili.",
        "order":   61,
        "blocks": [
            {"rich_text": """
<h2>📞 23–24-savollar: harakatni bitta ot bilan ayting</h2>
<p>23-savol yangi narsani so'raydi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>23.</strong> 남자는/여자는 무엇을 하고 있는지 고르십시오. —
  <em>Erkak/ayol NIMA QILYAPTI?</em> (24 — odatdagi 내용 일치.)</p>
</div>
<p>Bu suhbatlar deyarli doim <strong>telefon qo'ng'irog'i</strong>: mijoz xizmatga
qo'ng'iroq qiladi. Variantlar esa harakat otlari — ularni bilsangiz, javob o'zi ko'rinadi:</p>
<h3>Harakat fe'llari lug'ati</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>문의하다</strong> — so'rab-surishtirmoq (ma'lumot so'rash)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>신청하다</strong> — ariza bermoq, yozilmoq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>예약하다 / 변경하다 / 취소하다</strong> — band qilmoq / o'zgartirmoq / bekor qilmoq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>항의하다 / 불만을 말하다</strong> — norozilik bildirmoq</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>교환/환불을 요구하다</strong> — almashtirish/pulni qaytarishni talab qilmoq</p>
  <p style="font-size:1.05em;margin:0;"><strong>확인하다 / 부탁하다</strong> — aniqlamoq / iltimos qilmoq</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> Qo'ng'iroq qilgan odamning <strong>birinchi replikasi</strong> —
  maqsadning uyi: "~고 싶은데요 / ~아 주세요" qolipida keladi. Qolgan suhbat — tafsilotlar
  (24-savol uchun!). Demak: 1-eshitishda birinchi replika → 23-savol; 2-eshitishda qolgani →
  24-savol.
</div>
"""},
            {"rich_text": """
<p><strong>Juftlik A — 23-savol.</strong> 남자는 무엇을 하고 있는지 고르십시오.</p>
""",
             "audio": "topik_l_061_1.mp3",
             "audio_script": [
                 ("남자", "여보세요, 문화 센터지요? 요리 수업을 신청하고 싶은데 아직 자리가 있어요?"),
                 ("여자", "죄송합니다. 이번 달 요리 수업은 벌써 마감됐어요. 다음 달 수업은 다음 주 월요일부터 신청을 받아요."),
                 ("남자", "그럼 월요일에 홈페이지에서 신청하면 돼요?"),
                 ("여자", "네, 홈페이지나 전화로 하시면 됩니다."),
             ],
             "choices": [
                 {"text": "요리 수업 신청에 대해 문의하고 있다. (Pazandalik kursiga yozilish haqida so'rab-surishtirmoqda.)", "is_correct": True},
                 {"text": "요리 수업을 취소하고 있다. (Pazandalik kursini bekor qilmoqda.)", "is_correct": False},
                 {"text": "요리 방법을 배우고 있다. (Ovqat tayyorlashni o'rganmoqda.)", "is_correct": False},
                 {"text": "수업 시간에 대해 항의하고 있다. (Dars vaqti haqida norozilik bildirmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi replika — maqsad: 신청하고 <strong>싶은데</strong> 자리가 있어요? — yozilmoqchi
va so'rayapti → <mark style="background:#dcfce7;">문의하고 있다</mark> ✅ (hali yozilgani
yo'q — savol so'rayapti, shuning uchun 신청하고 있다 emas, 문의!). ④ norozilik ohang yo'q —
muloyim suhbat. Harakat otini tanlaganda <strong>ohang</strong>ni ham tekshiring: 항의 uchun
norozi ohang shart.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 여보세요, 문화 센터지요? 요리 수업을 신청하고 싶은데 아직 자리가 있어요?<br>
    <em style="color:#475569;">Allo, madaniyat markazimi? Pazandalik kursiga yozilmoqchi edim, hali joy bormi?</em></p>
    <p><strong>여자:</strong> 죄송합니다. 이번 달 요리 수업은 벌써 마감됐어요. 다음 달 수업은 다음 주 월요일부터 신청을 받아요.<br>
    <em style="color:#475569;">Uzr. Bu oygi pazandalik kursi allaqachon to'lgan. Kelasi oy kursiga kelasi hafta dushanbadan ariza qabul qilamiz.</em></p>
    <p><strong>남자:</strong> 그럼 월요일에 홈페이지에서 신청하면 돼요?<br>
    <em style="color:#475569;">Unda dushanba kuni saytdan yozilsam bo'ladimi?</em></p>
    <p><strong>여자:</strong> 네, 홈페이지나 전화로 하시면 됩니다.<br>
    <em style="color:#475569;">Ha, sayt yoki telefon orqali qilsangiz bo'ladi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Juftlik A — 24-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "다음 달 수업은 월요일부터 신청할 수 있다. (Kelasi oy kursiga dushanbadan yozilsa bo'ladi.)", "is_correct": True},
                 {"text": "이번 달 수업에는 아직 자리가 있다. (Bu oygi kursda hali joy bor.)", "is_correct": False},
                 {"text": "신청은 전화로만 할 수 있다. (Faqat telefon orqali yozilish mumkin.)", "is_correct": False},
                 {"text": "남자는 지난달에 요리 수업을 들었다. (Erkak o'tgan oy kursda qatnashgan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (벌써 <strong>마감됐어요</strong> — to'lgan!), ③ cheklov qo'shilgan
(홈페이지<strong>나</strong> 전화로 — ikkalasi ham bo'ladi; ~만 "faqat" tuzog'i o'qishdan
tanish!), ④ yo'q ma'lumot. ✅ ①: 월요일부터 신청을 받아요 → yozilsa bo'ladi. ~(이)나 =
"yoki" — tanlov borligini bildiradi, uni "faqat"ga aylantirgan variant doim tuzoq.</p>
"""},
            {"rich_text": """
<p><strong>Juftlik B — 23-savol.</strong> 여자는 무엇을 하고 있는지 고르십시오.</p>
""",
             "audio": "topik_l_061_2.mp3",
             "audio_script": [
                 ("여자", "여보세요. 지난주에 주문한 책상이 어제 왔는데 다리에 흠집이 있어요. 새 제품으로 바꿔 주세요."),
                 ("남자", "불편을 드려서 죄송합니다, 고객님. 흠집 부분의 사진을 먼저 보내 주시면 확인 후에 바로 교환해 드리겠습니다."),
                 ("여자", "알겠어요. 지금 바로 찍어서 보낼게요."),
             ],
             "choices": [
                 {"text": "제품 교환을 요구하고 있다. (Mahsulotni almashtirishni talab qilmoqda.)", "is_correct": True},
                 {"text": "책상을 새로 주문하고 있다. (Yangi stol buyurtma qilmoqda.)", "is_correct": False},
                 {"text": "배달 시간을 문의하고 있다. (Yetkazib berish vaqtini so'ramoqda.)", "is_correct": False},
                 {"text": "주문을 취소하고 있다. (Buyurtmani bekor qilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi replika oxiri — maqsad: 새 제품으로 <strong>바꿔 주세요</strong> (yangisiga
almashtirib bering) → <mark style="background:#dcfce7;">교환을 요구하고 있다</mark> ✅
(바꾸다 = 교환하다 — paraphrase!). ② yangi buyurtma emas — borini almashtirish; ④ bekor
qilish ham emas (mahsulot unga kerak). Muammo + "bering/qiling" = 요구 (talab); shunchaki
savol = 문의. Farqni his qiling.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 여보세요. 지난주에 주문한 책상이 어제 왔는데 다리에 흠집이 있어요. 새 제품으로 바꿔 주세요.<br>
    <em style="color:#475569;">Allo. O'tgan hafta buyurtma qilgan stolim kecha keldi, lekin oyog'ida tirnalgan joyi bor. Yangi mahsulotga almashtirib bering.</em></p>
    <p><strong>남자:</strong> 불편을 드려서 죄송합니다, 고객님. 흠집 부분의 사진을 먼저 보내 주시면 확인 후에 바로 교환해 드리겠습니다.<br>
    <em style="color:#475569;">Noqulaylik uchun uzr, mijoz. Tirnalgan joy suratini avval yuborsangiz, tekshirgach darhol almashtirib beramiz.</em></p>
    <p><strong>여자:</strong> 알겠어요. 지금 바로 찍어서 보낼게요.<br>
    <em style="color:#475569;">Tushunarli. Hozir suratga olib yuboraman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>Juftlik B — 24-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "여자는 흠집 사진을 보낼 것이다. (Ayol tirnalgan joy suratini yuboradi.)", "is_correct": True},
                 {"text": "책상은 지난달에 주문한 것이다. (Stol o'tgan oy buyurtma qilingan.)", "is_correct": False},
                 {"text": "남자는 교환을 거절했다. (Erkak almashtirishni rad etdi.)", "is_correct": False},
                 {"text": "책상 다리가 부러져 있었다. (Stolning oyog'i singan edi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② vaqt (지난<strong>주</strong> — o'tgan hafta!), ③ teskari (바로 교환해
<strong>드리겠습니다</strong> — almashtirib beradi!), ④ daraja oshirilgan (<strong>흠집</strong>
— tirnalgan iz; 부러지다 — sinmoq: boshqa-boshqa!). ✅ ①: 지금 바로 찍어서 보낼게요.
Daraja tuzog'i yangi: yengil muammoni og'ir qilib ko'rsatish (tirnalgan → singan) — quloqda
sezish oson, so'zlarni bilsangiz.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">문의하다</div><div class="pp-card-back">so'rab-surishtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">신청하다</div><div class="pp-card-back">yozilmoq, ariza bermoq</div></div>
  <div class="pp-card"><div class="pp-card-front">마감되다</div><div class="pp-card-back">to'lmoq, yopilmoq (qabul)</div></div>
  <div class="pp-card"><div class="pp-card-front">흠집</div><div class="pp-card-back">tirnalgan iz, nuqson</div></div>
  <div class="pp-card"><div class="pp-card-front">교환하다</div><div class="pp-card-back">almashtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">환불</div><div class="pp-card-back">pulni qaytarish</div></div>
  <div class="pp-card"><div class="pp-card-front">요구하다</div><div class="pp-card-back">talab qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">부러지다</div><div class="pp-card-back">sinmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>23-savol javobi — qo'ng'iroq qilganning <strong>birinchi replikasida</strong> (~고 싶은데요 / ~아 주세요).</li>
  <li>Harakat otlari: 문의 (so'rash) ≠ 신청 (yozilish) ≠ 요구 (talab) ≠ 항의 (norozilik) — ohang farqlaydi.</li>
  <li>24-savol tuzoqlari: "faqat" cheklovi (~만), daraja oshirish (흠집→부러짐), vaqt almashinuvi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 62) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 짝 문제 3: To'liq amaliyot — ikki juftlik imtihondagidek",
        "summary": "21–24 to'liq to'plami: fikr juftligi (tushlikdan keyingi sayr) va harakat juftligi (mehmonxona bronini o'zgartirish).",
        "order":   62,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 21–22 va 23–24 juftliklari</h2>
<p>Imtihondagidek ishlang: ikkala savolning variantlarini o'qing → birinchi eshitish =
1-savol → ikkinchi eshitish = 2-savol. Fikr juftligida fikr tugallanmalarini, harakat
juftligida birinchi replikani oving.</p>
"""},
            {"rich_text": """
<p><strong>21-savol.</strong> 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_062_1.mp3",
             "audio_script": [
                 ("여자", "요즘 점심을 먹고 나면 오후 내내 너무 졸려요."),
                 ("남자", "그럼 식사 후에 저랑 회사 근처 공원을 걸어요. 저는 산책을 시작하고 나서 오후에 훨씬 집중이 잘돼요. 밥 먹고 바로 앉아 있는 것보다 몸에도 좋고요."),
                 ("여자", "좋네요. 그럼 내일부터 같이 걸어요."),
             ],
             "choices": [
                 {"text": "식사 후 산책은 집중력과 건강에 좋다. (Ovqatdan keyingi sayr diqqat va salomatlikka foydali.)", "is_correct": True},
                 {"text": "점심을 먹지 않는 것이 좋다. (Tushlik qilmagan ma'qul.)", "is_correct": False},
                 {"text": "졸리면 커피를 마셔야 한다. (Uyqu kelsa kofe ichish kerak.)", "is_correct": False},
                 {"text": "공원은 회사에서 멀수록 좋다. (Bog' ishxonadan qancha uzoq bo'lsa, shuncha yaxshi.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkakning ikki dalili bitta soyabon ostida: 집중이 잘돼요 (diqqat) + 몸에도 좋고요
(salomatlik) → ✅ ① ikkalasini ham yopadi. ②③ aytilmagan yechimlar, ④ mavzudan tashqari.
Yechim + ikki foyda strukturasi — 21-savolning sevimli shakli: to'g'ri variant odatda
<strong>ikkala foydani ham</strong> o'z ichiga oladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 요즘 점심을 먹고 나면 오후 내내 너무 졸려요.<br>
    <em style="color:#475569;">Keyingi paytlarda tushlikdan keyin kun bo'yi uyqum kelaveradi.</em></p>
    <p><strong>남자:</strong> 그럼 식사 후에 저랑 회사 근처 공원을 걸어요. 저는 산책을 시작하고
    나서 오후에 훨씬 집중이 잘돼요. 밥 먹고 바로 앉아 있는 것보다 몸에도 좋고요.<br>
    <em style="color:#475569;">Unda ovqatdan keyin men bilan ishxona yaqinidagi bog'da yuring.
    Men sayr boshlaganimdan beri tushdan keyin diqqatim ancha yaxshi jamlanadi. Ovqatdan keyin
    darrov o'tiraverishdan ko'ra tanaga ham foydali.</em></p>
    <p><strong>여자:</strong> 좋네요. 그럼 내일부터 같이 걸어요.<br>
    <em style="color:#475569;">Yaxshi ekan. Unda ertagadan birga yuramiz.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>22-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "두 사람은 내일부터 같이 산책할 것이다. (Ikkalasi ertagadan birga sayr qiladi.)", "is_correct": True},
                 {"text": "여자는 오전에 졸음이 온다. (Ayolning tushgacha uyqusi keladi.)", "is_correct": False},
                 {"text": "남자는 산책을 아직 시작하지 않았다. (Erkak sayrni hali boshlamagan.)", "is_correct": False},
                 {"text": "공원은 회사에서 아주 멀다. (Bog' ishxonadan juda uzoq.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② vaqt almashtirilgan (졸림 — <strong>점심 먹고 나면</strong>, ya'ni tushdan
keyin!), ③ teskari (산책을 시작하고 <strong>나서</strong> — allaqachon boshlagan va natija
ko'rgan!), ④ teskari (회사 <strong>근처</strong> — yaqinida). ✅ ①: 내일부터 같이 걸어요.
Suhbat oxiridagi kelishuv (그럼 ~아요!) — 22-savolning tez-tez to'g'ri javobi.</p>
"""},
            {"rich_text": """
<p><strong>23-savol.</strong> 남자는 무엇을 하고 있는지 고르십시오.</p>
""",
             "audio": "topik_l_062_2.mp3",
             "audio_script": [
                 ("남자", "여보세요, 이번 주 금요일에 예약한 방을 일요일로 바꾸고 싶은데요."),
                 ("여자", "네, 확인해 보겠습니다. 일요일은 빈방이 있어서 변경해 드렸습니다. 다만 일요일은 주말 요금이라서 만 원을 더 내셔야 하는데 괜찮으시겠어요?"),
                 ("남자", "네, 괜찮아요. 감사합니다."),
             ],
             "choices": [
                 {"text": "호텔 예약 날짜를 변경하고 있다. (Mehmonxona bronining sanasini o'zgartirmoqda.)", "is_correct": True},
                 {"text": "호텔 방을 처음 예약하고 있다. (Mehmonxona xonasini birinchi marta band qilmoqda.)", "is_correct": False},
                 {"text": "예약을 취소하고 환불을 받고 있다. (Bronni bekor qilib, pulini qaytarib olmoqda.)", "is_correct": False},
                 {"text": "방 요금에 대해 항의하고 있다. (Xona narxi haqida norozilik bildirmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi replika: 예약한 방을 일요일로 <strong>바꾸고 싶은데요</strong> — bor bronni
boshqa kunga ko'chirish → <mark style="background:#dcfce7;">변경하고 있다</mark> ✅.
② yangi bron emas (예약<strong>한</strong> 방 — allaqachon band qilingan!), ④ narx haqida
gap bor, lekin erkak <strong>괜찮아요</strong> dedi — norozilik yo'q. 변경 (o'zgartirish)
so'zining o'zi ham audioda keldi: 변경해 드렸습니다.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 여보세요, 이번 주 금요일에 예약한 방을 일요일로 바꾸고 싶은데요.<br>
    <em style="color:#475569;">Allo, shu hafta jumaga band qilgan xonamni yakshanbaga o'zgartirmoqchi edim.</em></p>
    <p><strong>여자:</strong> 네, 확인해 보겠습니다. 일요일은 빈방이 있어서 변경해 드렸습니다.
    다만 일요일은 주말 요금이라서 만 원을 더 내셔야 하는데 괜찮으시겠어요?<br>
    <em style="color:#475569;">Xo'p, tekshirib ko'raman. Yakshanbada bo'sh xona bor ekan,
    o'zgartirib qo'ydim. Faqat yakshanba dam olish kuni tarifi bo'lgani uchun o'n ming von
    ko'proq to'laysiz, mayli bo'ladimi?</em></p>
    <p><strong>남자:</strong> 네, 괜찮아요. 감사합니다.<br>
    <em style="color:#475569;">Ha, mayli. Rahmat.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>24-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "남자는 요금을 만 원 더 내야 한다. (Erkak o'n ming von ko'proq to'lashi kerak.)", "is_correct": True},
                 {"text": "일요일에는 빈방이 없다. (Yakshanbada bo'sh xona yo'q.)", "is_correct": False},
                 {"text": "남자는 원래 일요일에 예약했다. (Erkak asli yakshanbaga band qilgan edi.)", "is_correct": False},
                 {"text": "여자는 변경을 해 주지 않았다. (Ayol o'zgartirib bermadi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (빈방이 <strong>있어서</strong>), ③ yo'nalish almashtirilgan (asli
<strong>금요일</strong>ga band qilingan, yakshanbaga o'tyapti!), ④ teskari (변경해
<strong>드렸습니다</strong>). ✅ ①: 만 원을 더 내셔야 — erkak rozi bo'ldi. Mavzu yakunlandi:
juft savollar rejasi qo'lingizda — keyingi bekat: intervyu bloki (25–30)! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">졸리다</div><div class="pp-card-back">uyqusi kelmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">집중이 잘되다</div><div class="pp-card-back">diqqat yaxshi jamlanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">변경하다</div><div class="pp-card-back">o'zgartirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">빈방</div><div class="pp-card-back">bo'sh xona</div></div>
  <div class="pp-card"><div class="pp-card-front">요금</div><div class="pp-card-back">tarif, to'lov</div></div>
  <div class="pp-card"><div class="pp-card-front">다만</div><div class="pp-card-back">faqat, biroq (istisno)</div></div>
  <div class="pp-card"><div class="pp-card-front">~고 나서</div><div class="pp-card-back">…gandan keyin</div></div>
  <div class="pp-card"><div class="pp-card-front">내내</div><div class="pp-card-back">davomida, boshdan-oxir</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Juft savol rejasi: variantlar oldindan → 1-eshitish = fikr/harakat → 2-eshitish = faktlar.</li>
  <li>Harakat savolida birinchi replika (~고 싶은데요), fikr savolida oxirgi dalillar hal qiladi.</li>
  <li>다만 (faqat…) dan keyingi istisno — 24-turdagi savollarning sevimli javob joyi.</li>
</ul>
"""},
        ],
    },
]
