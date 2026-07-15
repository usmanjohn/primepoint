# TOPIK II Reading — 44–45-savollar: Bo'sh joy + mavzu (빈칸·주제), lessons 1–2 (orders 150–151).
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_combo_1_2.py --author=prime

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "44–45-savollar: Bo'sh joy + mavzu (빈칸·주제)",
    "summary": "Bitta murakkab matnda ikki ko'nikma birga: bo'sh joyni to'ldirish va mavzuni topish.",
    "icon":    "bi-diagram-2",
    "order":   17,
}

LESSONS = [
    # ── Lesson 1 (order 150) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 빈칸·주제 1: 44–45-savollar bilan tanishuv — ikki qurol birga",
        "summary": "Bitta og'ir matnga bo'sh joy (28–31 usuli) va mavzu (35–38 usuli) savollari birga keladi.",
        "order":   150,
        "blocks": [
            {"rich_text": """
<h2>🔗 44–45-savollar: eski ikki do'stning uchrashuvi</h2>
<p>Yangi hech narsa o'rganmaysiz — bu blok ikkita tanish ko'nikmani <strong>bitta og'ir
matnda</strong> birlashtiradi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>44.</strong> (        )에 들어갈 말로 가장 알맞은 것 — <em>28–31-savollar quroli: javob matn ichida, parallelizm, ikki tomonlama tekshiruv.</em></p>
  <p style="font-size:1.08em;margin:0;"><strong>45.</strong> 이 글의 주제로 가장 알맞은 것 — <em>35–38-savollar quroli: soyabon testi, xulosa gapi, tor/keng tuzoqlar.</em></p>
</div>
<h3>Eng samarali tartib</h3>
<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">
  <div class="pp-step">
    <p><strong>1-qadam — matnni bir marta to'liq o'qing</strong> va o'qib bo'lgach o'zingizga
    bir jumlada ayting: "bu matn ... demoqchi". Bu jumla — 45-savolning xomaki javobi.</p>
  </div>
  <div class="pp-step">
    <p><strong>2-qadam — 44 (bo'sh joy):</strong> bo'sh joyli gapning vazifasini toping,
    atrofdagi gaplardan paraphrase qidiring, variantni qo'yib ikki tomonga tekshiring.</p>
  </div>
  <div class="pp-step">
    <p><strong>3-qadam — 45 (mavzu):</strong> 1-qadamdagi jumlangizga eng yaqin variantni
    tanlab, soyabon testidan o'tkazing. Sirli bog'lanish: <strong>to'g'ri to'ldirilgan bo'sh
    joy ko'pincha mavzuning o'zagida turadi</strong> — 44 to'g'ri bo'lsa, 45 osonlashadi!</p>
  </div>
</div>
"""},
            {"rich_text": """
<h3>To'liq matn — birga yechamiz</h3>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">판소리는 한 명의 소리꾼이 북 장단에
  맞춰 긴 이야기를 노래로 풀어내는 우리 전통 공연이다. 소리꾼은 몇 시간 동안 혼자서 여러
  인물을 연기하며 무대를 이끌어야 한다. 그래서 한 명의 소리꾼이 완성되기까지는 (        )
  필요하다. 옛 명창들은 폭포 앞에서 목소리를 단련하며 수십 년을 보냈다고 한다. 이처럼
  판소리는 한 사람의 목소리에 평생의 노력이 담긴 예술이다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Pansori — bitta xonanda nog'ora usuliga mos qilib
  uzun hikoyani qo'shiq bilan ochib beradigan an'anaviy tomoshamiz. Xonanda bir necha soat davomida
  yolg'iz o'zi bir nechta qahramonni ijro etib, sahnani olib borishi kerak. Shuning uchun bitta xonanda
  yetishib chiqquncha (        ) zarur. Qadimgi ustoz xonandalar sharshara oldida ovozini chiniqtirib,
  o'nlab yillarni o'tkazgan ekan. Shunday qilib, pansori — bir inson ovoziga bir umrlik mehnat
  singdirilgan san'atdir.</em></p>
</div>
<p><strong>Amaliyot 1 (44-tur).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
""",
             "choices": [
                 {"text": "오랜 훈련의 시간이 (uzoq mashq yillari)", "is_correct": True},
                 {"text": "화려한 무대 장치가 (hashamatli sahna jihozi)", "is_correct": False},
                 {"text": "많은 공연 참가자가 (ko'p tomosha ishtirokchisi)", "is_correct": False},
                 {"text": "비싼 전통 악기가 (qimmat an'anaviy cholg'u)", "is_correct": False},
             ],
             "explanation": """
<p>28–31 quroli: bo'sh joyli gap 그래서 bilan — oldingi gap sabab ("soatlab yolg'iz sahna
olib borishi kerak"), keyingi gap esa paraphrase-dalil: "폭포 앞에서 <strong>수십 년</strong>"
(o'nlab yillar!) → <mark style="background:#dcfce7;">오랜 훈련의 시간</mark> ✅.
③ tuzoq: matn aynan "혼자서" (yolg'iz!) deydi — ko'p ishtirokchi parallelizmga zid.
②④ matnda izi yo'q.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (45-tur).</strong> 이 글의 주제로 가장 알맞은 것을 고르십시오. (matn yuqorida)</p>
""",
             "choices": [
                 {"text": "판소리는 오랜 수련으로 완성되는 예술이다. (Pansori — uzoq mashq bilan kamolga yetadigan san'at.)", "is_correct": True},
                 {"text": "판소리 공연장은 시설이 좋아야 한다. (Pansori tomoshaxonasi jihozli bo'lishi kerak.)", "is_correct": False},
                 {"text": "폭포 앞은 목소리 훈련에 좋지 않다. (Sharshara oldi ovoz mashqiga yomon.)", "is_correct": False},
                 {"text": "전통 공연은 요즘 인기가 없다. (An'anaviy tomoshalar hozir ommabop emas.)", "is_correct": False},
             ],
             "explanation": """
<p>35–38 quroli: xulosa gapi <strong>이처럼</strong> bilan — "bir umrlik mehnat singdirilgan
san'at" → ① ✅. Soyabon testi: yolg'iz ijro ✔, uzoq tayyorgarlik ✔, sharshara misoli ✔ —
hammasi sig'adi. Va sirli bog'lanish ishladi: 44dagi javob (오랜 훈련) — mavzuning o'zagi!
② matnda yo'q, ③ teskari, ④ matndan tashqarida.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">전통 공연</div><div class="pp-card-back">an'anaviy tomosha</div></div>
  <div class="pp-card"><div class="pp-card-front">단련하다</div><div class="pp-card-back">chiniqtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">수련</div><div class="pp-card-back">mashq, tayyorgarlik (uzoq)</div></div>
  <div class="pp-card"><div class="pp-card-front">이끌다</div><div class="pp-card-back">olib bormoq, boshqarmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">담기다</div><div class="pp-card-back">singdirilgan bo'lmoq, jo bo'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">평생</div><div class="pp-card-back">bir umr</div></div>
  <div class="pp-card"><div class="pp-card-front">예술</div><div class="pp-card-back">san'at</div></div>
  <div class="pp-card"><div class="pp-card-front">명창</div><div class="pp-card-back">ustoz xonanda</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>44–45 = 28–31 (bo'sh joy) + 35–38 (mavzu) bitta matnda — yangi usul kerak emas!</li>
  <li>O'qib bo'lgach bir jumlalik xulosangizni ayting — bu 45ning xomaki javobi.</li>
  <li>To'g'ri to'ldirilgan bo'sh joy ko'pincha mavzu o'zagida — ikkovini bir-biriga tekshiring.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 151) ───────────────────────────────────────────────
    {
        "skill":   "reading",
        "topic":   TOPIC,
        "title":   "TOPIK 빈칸·주제 2: To'liq amaliyot — axborot davri matni",
        "summary": "Yana bir imtihon formatidagi matn: tanqidiy fikrlash mavzusida bo'sh joy va mavzu savollari.",
        "order":   151,
        "blocks": [
            {"rich_text": """
<h2>🏁 Mustaqil mashq</h2>
<p>Endi to'liq mustaqil: avval matnni o'qib, bir jumlalik xulosangizni ayting, keyin ikkala
savolni yeching. Mavzu — 44–45-savollarning sevimlisi: zamonaviy jamiyat muammosi.</p>
<div style="background:#f8fafc;border:2px solid #cbd5e1;border-radius:10px;padding:16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;line-height:1.9;">현대인은 하루에도 수많은 정보를
  접하며 산다. 그러나 그 모든 정보가 사실인 것은 아니다. 인터넷에서는 확인되지 않은 소문이
  마치 사실처럼 빠르게 퍼지기도 한다. 따라서 정보를 접할 때는 그것이 (        ) 태도가
  필요하다. 이 정보가 어디에서 나왔는지, 믿을 만한 다른 곳에서도 같은 내용을 전하고 있는지
  확인하는 작은 습관이 그 시작이 될 수 있다.</p>
  <p style="color:#475569;margin:8px 0 0;"><em>Zamonaviy inson bir kunning o'zida son-sanoqsiz
  axborotga duch keladi. Lekin bu axborotlarning hammasi ham haqiqat emas. Internetda tasdiqlanmagan
  mish-mish xuddi haqiqatdek tez tarqalishi ham mumkin. Shuning uchun axborotga duch kelganda uni
  (        ) munosabat zarur. Bu axborot qayerdan chiqqani, ishonchli boshqa manbalar ham xuddi shu
  mazmunni berayotganini tekshirish kichik odati — buning boshlanishi bo'la oladi.</em></p>
</div>
<p><strong>Amaliyot 1 (44-tur).</strong> (        )에 들어갈 말로 가장 알맞은 것을 고르십시오.</p>
""",
             "choices": [
                 {"text": "믿을 만한 것인지 따져 보는 (ishonsa bo'ladimi-yo'qmi — sinchiklab tekshiradigan)", "is_correct": True},
                 {"text": "친구들에게 빨리 전달하는 (do'stlarga tez yetkazadigan)", "is_correct": False},
                 {"text": "재미있게 바꿔서 이야기하는(qiziqarli qilib o'zgartirib aytadigan)", "is_correct": False},
                 {"text": "하나도 빠짐없이 외우는 (bittasini ham qoldirmay yodlaydigan)", "is_correct": False},
             ],
             "explanation": """
<p>Bo'sh joyli gap 따라서 bilan — oldingi gaplar sabab: "hammasi haqiqat emas + mish-mish
tez tarqaladi". Keyingi gap esa to'ldirilgan bo'sh joyning <strong>izohi</strong>: "qayerdan
chiqqani ... tekshirish" → <mark style="background:#dcfce7;">믿을 만한 것인지 따져 보는</mark> ✅
(따지다 — sinchiklab surishtirmoq). ② aksincha — tarqatish muammoning o'zi! Ikkala tomonga
tekshiruv usuli yana g'alaba qildi.</p>
"""},
            {"rich_text": """
<p><strong>Amaliyot 2 (45-tur).</strong> 이 글의 주제로 가장 알맞은 것을 고르십시오. (matn yuqorida)</p>
""",
             "choices": [
                 {"text": "정보를 비판적으로 확인하는 태도가 필요하다. (Axborotni tanqidiy tekshiradigan munosabat zarur.)", "is_correct": True},
                 {"text": "인터넷은 되도록 사용하지 않는 것이 좋다. (Internetni iloji boricha ishlatmagan ma'qul.)", "is_correct": False},
                 {"text": "소문은 인터넷에서 빠르게 퍼진다. (Mish-mish internetda tez tarqaladi.)", "is_correct": False},
                 {"text": "현대인은 정보가 부족해서 어려움을 겪는다. (Zamonaviy inson axborot yetishmasligidan qiynaladi.)", "is_correct": False},
             ],
             "explanation": """
<p>Talab-gap: "...따져 보는 태도가 <strong>필요하다</strong>" → mavzu ① ✅. Tuzoqlarni
nomlaymiz (35–38 laboratoriyasi): ② matndan <strong>kuchliroq</strong> talab (matn
"ishlatma" demaydi — "tekshir" deydi); ③ <strong>tor</strong> — 3-gapning o'zi, soyabon
emas; ④ <strong>teskari</strong> — muammo axborot <em>ko'pligi</em>da, kamligida emas.
44dagi javob (따져 보는) yana mavzuning yuragida!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">접하다</div><div class="pp-card-back">duch kelmoq (axborotga)</div></div>
  <div class="pp-card"><div class="pp-card-front">소문</div><div class="pp-card-back">mish-mish</div></div>
  <div class="pp-card"><div class="pp-card-front">확인되지 않다</div><div class="pp-card-back">tasdiqlanmagan bo'lmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">따지다</div><div class="pp-card-back">sinchiklab surishtirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">출처</div><div class="pp-card-back">manba (axborot chiqqan joy)</div></div>
  <div class="pp-card"><div class="pp-card-front">믿을 만하다</div><div class="pp-card-back">ishonsa arziydigan</div></div>
  <div class="pp-card"><div class="pp-card-front">비판적</div><div class="pp-card-back">tanqidiy</div></div>
  <div class="pp-card"><div class="pp-card-front">태도</div><div class="pp-card-back">munosabat, yondashuv</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Tartib: matn → bir jumlalik xulosa → 44 (bo'sh joy, ikki tomonlama tekshiruv) → 45 (soyabon testi).</li>
  <li>44 va 45 bir-birini tekshiradi: bo'sh joy javobi mavzu o'zagida bo'lishi kerak.</li>
  <li>Mavzu tuzoqlari o'sha-o'sha: kuchliroq talab, tor detal, teskari fikr.</li>
</ul>
"""},
        ],
    },
]
