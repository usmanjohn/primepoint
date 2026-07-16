# TOPIK II Listening — 31–36-savollar: Munozara va rasmiy nutq (토론·공식 말하기), lessons 1–3 (orders 80–82).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_debate_1_3.py \
#            --out examprep/management/commands/audio/debate
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_debate_1_3.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/debate

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC = {
    "title":   "31–36-savollar: Munozara va rasmiy nutq (토론·공식 말하기)",
    "summary": "Munozarada erkakning pozitsiyasi va bahs uslubi (태도), ma'ruza mavzusi hamda rasmiy nutqning maqsadi.",
    "icon":    "bi-people",
    "order":   9,
}

LESSONS = [
    # ── Lesson 1 (order 80) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 토론 1: 31–32-savollar — pozitsiya va bahs uslubi",
        "summary": "Munozara juftligi: erkak NIMA deyapti (생각) va QANDAY bahslashyapti (태도) — dalil, tan olish, taklif.",
        "order":   80,
        "blocks": [
            {"rich_text": """
<h2>⚖️ 31–32-savollar: bahsda ikki savol</h2>
<p>Bu juftlikda ikki kishi biror masalani <strong>muhokama qiladi</strong> (ko'pincha yig'ilish
yoki jamoat masalasi). Savollar:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0 0 6px;"><strong>31.</strong> 남자의 생각으로 맞는 것을 고르십시오. — <em>erkakning POZITSIYASI (nima deyapti?).</em></p>
  <p style="font-size:1.08em;margin:0;"><strong>32.</strong> 남자의 태도로 알맞은 것을 고르십시오. — <em>bahs USLUBI (qanday deyapti?).</em></p>
</div>
<h3>32-savolning tayyor javob qoliplari</h3>
<p>Bu savolning variantlari deyarli doim shu ro'yxatdan chiqadi — yodlab oling:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>근거를 들어 주장하고 있다</strong> — dalil keltirib fikrini himoya qilyapti (belgi: 실제로, 예를 들어)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>해결 방안을 제시하고 있다</strong> — yechim taklif qilyapti (belgi: ~는 게 어떨까요, ~면 됩니다)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>상대방의 의견을 일부 인정하고 있다</strong> — raqib fikrini qisman tan olyapti (belgi: 그렇긴 하지만, 물론)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>상대방의 의견에 동의하고 있다</strong> — to'liq qo'shilyapti (belgi: 맞습니다, 저도 그렇게 생각해요)</p>
  <p style="font-size:1.05em;margin:0;"><strong>상황을 비판하고 있다 / 우려하고 있다</strong> — tanqid / xavotir (belgi: 문제입니다, 걱정입니다)</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> 31 uchun erkakning <strong>xulosa jumlasi</strong>ni (odatda oxirida),
  32 uchun uning <strong>qurollarini</strong> sanang: dalil keltirdimi? Misol aytdimi? Yechim
  taklif qildimi? Ikkalasini bir vaqtda emas — ikki eshitishga bo'ling!
</div>
"""},
            {"rich_text": """
<p><strong>31-savol.</strong> 남자의 생각으로 맞는 것을 고르십시오.</p>
""",
             "audio": "topik_l_080_1.mp3",
             "audio_script": [
                 ("여자", "아파트 단지 안의 놀이터를 없애고 주차장을 만들자는 의견이 많던데요."),
                 ("남자", "저는 반대합니다. 주차 문제도 중요하지만 아이들이 안전하게 놀 공간은 꼭 필요합니다. 실제로 놀이터를 없앤 아파트에서는 아이들이 주차장에서 놀다가 다치는 일도 있었고요."),
                 ("여자", "그렇긴 하지만 주민들의 불편도 생각해야지요."),
                 ("남자", "그래서 놀이터는 그대로 두고, 단지 옆 공터를 주차장으로 만드는 게 어떨까 합니다."),
             ],
             "choices": [
                 {"text": "아이들의 놀 공간을 지키면서 주차 문제를 풀어야 한다. (Bolalar maydonchasini saqlagan holda avtoturargoh muammosini yechish kerak.)", "is_correct": True},
                 {"text": "놀이터보다 주차장이 더 필요하다. (Maydonchadan ko'ra avtoturargoh muhimroq.)", "is_correct": False},
                 {"text": "아이들은 집 안에서 노는 것이 안전하다. (Bolalar uy ichida o'ynagani xavfsiz.)", "is_correct": False},
                 {"text": "주민들의 불편은 중요하지 않다. (Aholining noqulayligi muhim emas.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkakning pozitsiyasi ikki qismda: 반대합니다 (maydonchani yo'q qilishga qarshi) + oxirida
yechim: 놀이터는 그대로 두고 공터를 주차장으로 → ✅ ① ikkalasini yopadi. ② raqib
pozitsiya, ④ u aytmagan — aksincha, aholiga ham yechim topdi (공터!). Bahsda pozitsiya =
<strong>qarshilik + taklif</strong> yig'indisi, faqat bittasi emas.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 아파트 단지 안의 놀이터를 없애고 주차장을 만들자는 의견이 많던데요.<br>
    <em style="color:#475569;">Turar-joy massivi ichidagi bolalar maydonchasini olib tashlab, avtoturargoh quraylik degan fikrlar ko'p ekan.</em></p>
    <p><strong>남자:</strong> 저는 반대합니다. 주차 문제도 중요하지만 아이들이 안전하게 놀 공간은
    꼭 필요합니다. 실제로 놀이터를 없앤 아파트에서는 아이들이 주차장에서 놀다가 다치는 일도 있었고요.<br>
    <em style="color:#475569;">Men qarshiman. Avtoturargoh muammosi ham muhim, lekin bolalar
    xavfsiz o'ynaydigan joy albatta kerak. Haqiqatan ham maydonchasi olib tashlangan binolarda
    bolalar avtoturargohda o'ynab jarohat olgan hollar bo'lgan.</em></p>
    <p><strong>여자:</strong> 그렇긴 하지만 주민들의 불편도 생각해야지요.<br>
    <em style="color:#475569;">Shunday-ku, lekin aholining noqulayligini ham o'ylash kerak-da.</em></p>
    <p><strong>남자:</strong> 그래서 놀이터는 그대로 두고, 단지 옆 공터를 주차장으로 만드는 게 어떨까 합니다.<br>
    <em style="color:#475569;">Shuning uchun maydonchani joyida qoldirib, massiv yonidagi bo'sh maydonni avtoturargoh qilsak-chi deyman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>32-savol.</strong> 남자의 태도로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida — ikkinchi marta eshiting)</em></p>
""",
             "choices": [
                 {"text": "근거를 들어 반대하며 해결 방안을 제시하고 있다. (Dalil keltirib qarshi chiqmoqda va yechim taklif qilmoqda.)", "is_correct": True},
                 {"text": "상대방의 의견에 전적으로 동의하고 있다. (Suhbatdosh fikriga to'la qo'shilmoqda.)", "is_correct": False},
                 {"text": "문제를 다른 사람에게 미루고 있다. (Muammoni boshqaga surmoqda.)", "is_correct": False},
                 {"text": "결정을 서두르자고 재촉하고 있다. (Qarorni tezlashtirishga undamoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Erkakning qurollarini sanaymiz: <strong>실제로</strong> + jarohat misoli = dalil (근거);
<strong>~는 게 어떨까 합니다</strong> = yechim taklifi (해결 방안 제시) → ✅ ①. U qisman
tan ham oldi (주차 문제<strong>도</strong> 중요하지만) — lekin "to'la qo'shilish" emas.
32-savolda variantdagi <strong>har bir fe'l</strong> audioda o'z belgisiga ega bo'lishi
kerak: 근거 → 실제로 ✔, 제시 → 어떨까 합니다 ✔.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">토론</div><div class="pp-card-back">munozara, bahs</div></div>
  <div class="pp-card"><div class="pp-card-front">반대하다</div><div class="pp-card-back">qarshi chiqmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">근거를 들다</div><div class="pp-card-back">dalil keltirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">해결 방안</div><div class="pp-card-back">yechim yo'li</div></div>
  <div class="pp-card"><div class="pp-card-front">제시하다</div><div class="pp-card-back">taklif etmoq, ko'rsatmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">공터</div><div class="pp-card-back">bo'sh maydon</div></div>
  <div class="pp-card"><div class="pp-card-front">그렇긴 하지만</div><div class="pp-card-back">shunday-ku, lekin (qisman tan olish)</div></div>
  <div class="pp-card"><div class="pp-card-front">인정하다</div><div class="pp-card-back">tan olmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>31 = pozitsiya (qarshilik/yoqlash + taklif); 32 = uslub (qurollar ro'yxati).</li>
  <li>32 variantidagi har fe'lni audiodagi belgisi bilan tasdiqlang: 근거→실제로, 제시→어떨까요.</li>
  <li>"전적으로/무조건" turdagi keskin uslub variantlari — odatdagidek tuzoq.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 81) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 토론 2: Ma'ruza mavzusi (33) va rasmiy nutq (35)",
        "summary": "33–34: ma'ruzaning mavzusini bir ot-ibora bilan aytish; 35–36: tabrik/ochilish nutqida so'zlovchi nima qilyapti.",
        "order":   81,
        "blocks": [
            {"rich_text": """
<h2>🎓 Ikki yangi format: ma'ruza va rasmiy nutq</h2>
<h3>33–34: ma'ruza — mavzu savoli</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>33.</strong> 무엇에 대한 내용인지 알맞은 것을 고르십시오. —
  <em>Bu NIMA HAQIDA? (variantlar — ot-iboralar: ~의 효과, ~의 방법, ~의 역사…)</em></p>
</div>
<p>Usul — soyabon testi: ma'ruzachi aytgan <strong>hamma faktni</strong> yopadigan ot-iborani
tanlang. Bitta misolga yopishgan variant — tor tuzoq.</p>
<h3>35–36: rasmiy nutq — "u nima qilyapti?"</h3>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>35.</strong> 남자는 무엇을 하고 있는지 고르십시오. —
  <em>marosimdagi nutqning MAQSADI.</em></p>
</div>
<p>Marosim turini ochilish jumlasidan aniqlang: 문을 열게 되어 (ochilish — 개관/개업),
졸업을 축하합니다 (bitiruv), 상을 주셔서 (mukofot — 수상 소감), 그동안 감사했습니다
(xayrlashuv — 퇴임). Variantlar: 개관을 축하하고 있다, 수상 소감을 말하고 있다,
감사 인사를 하고 있다, 행사 일정을 안내하고 있다…</p>
"""},
            {"rich_text": """
<p><strong>33-savol.</strong> 무엇에 대한 내용인지 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_081_1.mp3",
             "audio_script": [
                 ("여자", "여러분, 웃음은 단순히 기분을 좋게 하는 데서 끝나지 않습니다. 웃을 때 우리 몸에서는 통증을 줄여 주는 물질이 나옵니다. 또 크게 웃으면 몸속 근육이 움직여서 가벼운 운동을 한 것과 같은 효과가 있지요. 그래서 요즘 병원에서는 환자들에게 웃음 치료를 하기도 합니다."),
             ],
             "choices": [
                 {"text": "웃음이 몸에 주는 효과 (Kulgining tanaga ta'siri)", "is_correct": True},
                 {"text": "웃음을 참는 방법 (Kulguni tiyish usullari)", "is_correct": False},
                 {"text": "병원에서 일하는 방법 (Shifoxonada ishlash yo'llari)", "is_correct": False},
                 {"text": "운동을 잘하는 방법 (Sportda yaxshi bo'lish yo'llari)", "is_correct": False},
             ],
             "explanation": """
<p>Soyabon testi: faktlar — og'riqni kamaytiruvchi modda, mushak harakati, 웃음 치료.
Hammasini yopadigan ot-ibora: <mark style="background:#dcfce7;">웃음의 효과</mark> ✅.
④ bitta faktga (운동 효과) yopishgan tor variant, ③ misolning joyiga (병원) yopishgan.
Mavzu savolida variant qancha keng bo'lsa, tekshiruv shuncha muhim: "hamma fakt shu
soyabon ostidami?"</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 여러분, 웃음은 단순히 기분을 좋게 하는 데서 끝나지 않습니다. 웃을 때
    우리 몸에서는 통증을 줄여 주는 물질이 나옵니다. 또 크게 웃으면 몸속 근육이 움직여서 가벼운
    운동을 한 것과 같은 효과가 있지요. 그래서 요즘 병원에서는 환자들에게 웃음 치료를 하기도 합니다.<br>
    <em style="color:#475569;">Azizlar, kulgi shunchaki kayfiyatni ko'tarish bilan tugamaydi.
    Kulganimizda tanamizda og'riqni kamaytiradigan modda ajraladi. Qattiq kulganda esa ichki
    mushaklar harakatlanib, yengil mashq qilgandek samara beradi. Shuning uchun hozir
    shifoxonalarda bemorlarga kulgi terapiyasi ham qilinadi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>34-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "웃을 때 통증을 줄여 주는 물질이 나온다. (Kulganda og'riqni kamaytiradigan modda ajraladi.)", "is_correct": True},
                 {"text": "웃음은 기분을 좋게 할 뿐이다. (Kulgi faqat kayfiyatni ko'taradi xolos.)", "is_correct": False},
                 {"text": "크게 웃으면 몸에 해롭다. (Qattiq kulish tanaga zararli.)", "is_correct": False},
                 {"text": "웃음 치료를 하는 병원은 없다. (Kulgi terapiyasini qiladigan shifoxona yo'q.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② birinchi jumlaga zid (~에서 끝나지 <strong>않습니다</strong> — "faqat" emas!),
③ teskari (운동을 한 것과 같은 <strong>효과</strong> — foyda!), ④ teskari (병원에서
치료를 하기도 <strong>합니다</strong>). ✅ ①: aynan aytilgan. ~ㄹ 뿐이다 ("faqat xolos")
variantlari — ma'ruzalarning "단순히 ~않습니다" jumlasiga qarshi klassik tuzoq.</p>
"""},
            {"rich_text": """
<p><strong>35-savol.</strong> 남자는 무엇을 하고 있는지 고르십시오.</p>
""",
             "audio": "topik_l_081_2.mp3",
             "audio_script": [
                 ("남자", "오늘 우리 마을에 이렇게 훌륭한 도서관이 문을 열게 되어 정말 기쁩니다. 이 도서관은 삼 년 동안 주민 여러분의 관심과 도움으로 완성되었습니다. 앞으로 이곳이 아이부터 어른까지 누구나 책과 가까워지는 공간이 되기를 바랍니다. 도움을 주신 모든 분께 진심으로 감사드립니다."),
             ],
             "choices": [
                 {"text": "도서관 개관을 축하하며 감사 인사를 하고 있다. (Kutubxona ochilishini tabriklab, minnatdorchilik bildirmoqda.)", "is_correct": True},
                 {"text": "도서관 이용 규칙을 설명하고 있다. (Kutubxonadan foydalanish qoidalarini tushuntirmoqda.)", "is_correct": False},
                 {"text": "새로 나온 책을 소개하고 있다. (Yangi chiqqan kitobni tanishtirmoqda.)", "is_correct": False},
                 {"text": "도서관 공사 계획을 발표하고 있다. (Kutubxona qurilishi rejasini e'lon qilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Ochilish jumlasi marosimni aytdi: <strong>문을 열게 되어</strong> 기쁩니다 → 개관 (ochilish)!
Yopilishi esa maqsadni: 진심으로 <strong>감사드립니다</strong> → ✅ ①. ④ zamon tuzog'i:
qurilish <strong>tugagan</strong> (완성되었습니다), reja emas. Rasmiy nutqda birinchi va
oxirgi jumla — ikkita eng katta signal.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 오늘 우리 마을에 이렇게 훌륭한 도서관이 문을 열게 되어 정말 기쁩니다.
    이 도서관은 삼 년 동안 주민 여러분의 관심과 도움으로 완성되었습니다. 앞으로 이곳이 아이부터
    어른까지 누구나 책과 가까워지는 공간이 되기를 바랍니다. 도움을 주신 모든 분께 진심으로
    감사드립니다.<br>
    <em style="color:#475569;">Bugun mahallamizda shunday ajoyib kutubxona ochilayotganidan juda
    xursandman. Bu kutubxona uch yil davomida aholining e'tibori va yordami bilan bunyod etildi.
    Kelgusida bu maskan boladan kattagacha har kim kitobga yaqinlashadigan makon bo'lishini
    istayman. Yordam bergan barchaga chin dildan minnatdorchilik bildiraman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>36-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "도서관은 삼 년에 걸쳐 완성되었다. (Kutubxona uch yil davomida bunyod etilgan.)", "is_correct": True},
                 {"text": "도서관은 아직 문을 열지 않았다. (Kutubxona hali ochilmagan.)", "is_correct": False},
                 {"text": "도서관은 어른만 이용할 수 있다. (Kutubxonadan faqat kattalar foydalana oladi.)", "is_correct": False},
                 {"text": "주민들은 도서관 건립에 반대했다. (Aholi kutubxona qurilishiga qarshi chiqqan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② bugun ochilyapti (문을 <strong>열게 되어</strong>), ③ teskari (아이부터
어른까지 <strong>누구나</strong>!), ④ teskari (주민 여러분의 관심과 <strong>도움으로</strong>).
✅ ①: 삼 년 동안 완성되었습니다 = 삼 년에 걸쳐 (~에 걸쳐 — davomida: paraphrase!).
Rasmiy nutqning faktlari oz, lekin hammasi savolga kiradi — diqqat bilan.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">통증</div><div class="pp-card-back">og'riq</div></div>
  <div class="pp-card"><div class="pp-card-front">물질</div><div class="pp-card-back">modda</div></div>
  <div class="pp-card"><div class="pp-card-front">치료</div><div class="pp-card-back">davolash, terapiya</div></div>
  <div class="pp-card"><div class="pp-card-front">개관</div><div class="pp-card-back">ochilish (kutubxona/muzey)</div></div>
  <div class="pp-card"><div class="pp-card-front">완성되다</div><div class="pp-card-back">bunyod etilmoq, tugallanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~에 걸쳐</div><div class="pp-card-back">…davomida</div></div>
  <div class="pp-card"><div class="pp-card-front">수상 소감</div><div class="pp-card-back">mukofot olgandagi nutq</div></div>
  <div class="pp-card"><div class="pp-card-front">진심으로</div><div class="pp-card-back">chin dildan</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>33 (mavzu): hamma faktni yopadigan ot-ibora; bitta misolga yopishgan variant — tor tuzoq.</li>
  <li>35 (rasmiy nutq): birinchi jumla marosimni, oxirgisi maqsadni aytadi.</li>
  <li>~ㄹ 뿐이다 ("faqat xolos") va zamon tuzoqlari (reja ⇄ tugagan) — bu guruhning sevimlilari.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 82) ───────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC,
        "title":   "TOPIK 토론 3: To'liq amaliyot — yig'ilish va bitiruv nutqi",
        "summary": "31–36 to'liq mashqi: ofisdagi qog'oz stakan bahsi (pozitsiya+uslub) va bitiruv marosimi nutqi (maqsad+mazmun).",
        "order":   82,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: 31–32 va 35–36 juftliklari</h2>
<p>Ikkala format ham imtihondagidek: munozarada pozitsiya va uslubni ajrating, rasmiy nutqda
birinchi-oxirgi jumlalarni oving. Har juftlikni ikki marta eshiting.</p>
"""},
            {"rich_text": """
<p><strong>31-savol.</strong> 남자의 생각으로 맞는 것을 고르십시오.</p>
""",
             "audio": "topik_l_082_1.mp3",
             "audio_script": [
                 ("남자", "다음 달부터 사무실에서 종이컵을 없애는 게 어떨까요? 하루에 버려지는 종이컵이 몇백 개나 됩니다."),
                 ("여자", "취지는 좋지만 손님들이 오셨을 때 불편하지 않을까요?"),
                 ("남자", "손님용 유리컵을 따로 준비하면 됩니다. 쓰레기도 줄이고 컵을 사는 비용도 아낄 수 있으니 한번 해 볼 만합니다."),
             ],
             "choices": [
                 {"text": "종이컵을 없애면 쓰레기와 비용을 줄일 수 있다. (Qog'oz stakandan voz kechilsa, chiqindi va xarajat kamayadi.)", "is_correct": True},
                 {"text": "손님에게는 종이컵이 더 편하다. (Mehmonlarga qog'oz stakan qulayroq.)", "is_correct": False},
                 {"text": "종이컵을 지금보다 더 많이 사야 한다. (Qog'oz stakanni hozirgidan ko'proq sotib olish kerak.)", "is_correct": False},
                 {"text": "사무실에 손님이 오면 안 된다. (Ofisga mehmon kelmasligi kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Pozitsiya taklif shaklida boshlanib (없애는 게 <strong>어떨까요?</strong>), sabablar bilan
yopiladi: 쓰레기도 줄이고 비용도 아낄 수 <strong>있으니</strong> → ✅ ①. ② ayolning
xavotiri edi — va erkak unga yechim berdi (유리컵), demak bu uning fikri emas. Taklif +
ikki foyda — 31-savolning eng tipik javob shakli.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 다음 달부터 사무실에서 종이컵을 없애는 게 어떨까요? 하루에 버려지는 종이컵이 몇백 개나 됩니다.<br>
    <em style="color:#475569;">Kelasi oydan ofisda qog'oz stakanlardan voz kechsak-chi? Kuniga bir necha yuztasi tashlab yuborilyapti.</em></p>
    <p><strong>여자:</strong> 취지는 좋지만 손님들이 오셨을 때 불편하지 않을까요?<br>
    <em style="color:#475569;">Maqsad yaxshi-yu, mehmonlar kelganda noqulay bo'lmasmikan?</em></p>
    <p><strong>남자:</strong> 손님용 유리컵을 따로 준비하면 됩니다. 쓰레기도 줄이고 컵을 사는 비용도 아낄 수 있으니 한번 해 볼 만합니다.<br>
    <em style="color:#475569;">Mehmonlar uchun alohida shisha stakan tayyorlab qo'ysak bo'ladi. Chiqindi ham kamayadi, stakan sotib olish xarajati ham tejaladi — bir urinib ko'rishga arziydi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>32-savol.</strong> 남자의 태도로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "상대방의 걱정에 해결 방안을 제시하며 제안하고 있다. (Suhbatdosh xavotiriga yechim ko'rsatib, taklif qilmoqda.)", "is_correct": True},
                 {"text": "상대방의 의견을 무시하고 있다. (Suhbatdosh fikrini mensimayapti.)", "is_correct": False},
                 {"text": "과거의 결정을 후회하고 있다. (O'tmishdagi qarordan afsuslanmoqda.)", "is_correct": False},
                 {"text": "문제의 원인을 상대방에게 돌리고 있다. (Muammo sababini suhbatdoshga ag'darmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Uslub zanjiri: taklif (어떨까요) → ayolning xavotiri → <strong>yechim</strong> (유리컵을
준비하면 됩니다) → foyda dalillari → ✅ ①. Erkak xavotirni e'tiborsiz qoldirmadi — unga
javob berdi, demak ② noto'g'ri. 32-turdagi savolda suhbatning <strong>harakat xaritasi</strong>ni
chizing: kim nima dedi, ikkinchisi bunga qanday javob qaytardi?</p>
"""},
            {"rich_text": """
<p><strong>35-savol.</strong> 여자는 무엇을 하고 있는지 고르십시오.</p>
""",
             "audio": "topik_l_082_2.mp3",
             "audio_script": [
                 ("여자", "졸업생 여러분, 진심으로 축하합니다. 여러분은 지난 사 년 동안 실패를 두려워하지 않고 도전하는 법을 배웠습니다. 이제 학교 밖에서도 그 용기를 잊지 마십시오. 여러분이 어디에 있든 우리는 언제나 여러분을 응원하겠습니다."),
             ],
             "choices": [
                 {"text": "졸업을 축하하며 졸업생들을 격려하고 있다. (Bitiruvni tabriklab, bitiruvchilarni ruhlantirmoqda.)", "is_correct": True},
                 {"text": "신입생들에게 학교를 소개하고 있다. (Yangi talabalarga maktabni tanishtirmoqda.)", "is_correct": False},
                 {"text": "시험 일정을 안내하고 있다. (Imtihon jadvalini e'lon qilmoqda.)", "is_correct": False},
                 {"text": "학생들의 실수를 지적하고 있다. (O'quvchilar xatosini ko'rsatmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Birinchi jumla marosimni aytdi: <strong>졸업생 여러분, 축하합니다</strong> → bitiruv!
Davomi — dalda: 용기를 잊지 마십시오 + 응원하겠습니다 →
<mark style="background:#dcfce7;">축하 + 격려</mark> ✅. ② tuzoq: maktab haqida gap bor,
lekin tinglovchi — <strong>bitiruvchilar</strong>, yangi talabalar emas. Murojaat so'zi
(졸업생/신입생/주민 여러분) — auditoriyani birinchi soniyada aytadi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 졸업생 여러분, 진심으로 축하합니다. 여러분은 지난 사 년 동안 실패를
    두려워하지 않고 도전하는 법을 배웠습니다. 이제 학교 밖에서도 그 용기를 잊지 마십시오.
    여러분이 어디에 있든 우리는 언제나 여러분을 응원하겠습니다.<br>
    <em style="color:#475569;">Aziz bitiruvchilar, chin dildan tabriklayman. Siz o'tgan to'rt yil
    davomida mag'lubiyatdan qo'rqmasdan intilishni o'rgandingiz. Endi maktab tashqarisida ham o'sha
    jasoratni unutmang. Qayerda bo'lmang, biz sizni doim qo'llab-quvvatlaymiz.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>36-savol.</strong> 들은 내용과 같은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "여자는 졸업생들을 계속 응원할 것이다. (Ayol bitiruvchilarni doim qo'llab-quvvatlaydi.)", "is_correct": True},
                 {"text": "졸업생들은 일 년 동안 공부했다. (Bitiruvchilar bir yil o'qigan.)", "is_correct": False},
                 {"text": "여자는 실패하면 안 된다고 말했다. (Ayol xato qilmaslik kerak dedi.)", "is_correct": False},
                 {"text": "이 행사는 입학식이다. (Bu tadbir — o'qishga kirish marosimi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② raqam (<strong>사 년</strong> — to'rt yil!), ③ nozik buzish: u "xato qilmang"
demadi — "실패를 <strong>두려워하지 않고</strong>" (mag'lubiyatdan QO'RQMASLIKNI) o'rgandingiz
dedi — ma'no teskarisiga o'girilgan!, ④ marosim almashtirilgan (졸업 ≠ 입학). ✅ ①:
언제나 응원하겠습니다. Mavzu yakun: munozara ham, minbar ham endi sizniki! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">취지</div><div class="pp-card-back">maqsad, mohiyat</div></div>
  <div class="pp-card"><div class="pp-card-front">아끼다</div><div class="pp-card-back">tejamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">해 볼 만하다</div><div class="pp-card-back">urinib ko'rishga arziydi</div></div>
  <div class="pp-card"><div class="pp-card-front">졸업 / 입학</div><div class="pp-card-back">bitiruv / o'qishga kirish</div></div>
  <div class="pp-card"><div class="pp-card-front">도전하다</div><div class="pp-card-back">intilmoq, jur'at qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">용기</div><div class="pp-card-back">jasorat</div></div>
  <div class="pp-card"><div class="pp-card-front">응원하다</div><div class="pp-card-back">qo'llab-quvvatlamoq</div></div>
  <div class="pp-card"><div class="pp-card-front">격려하다</div><div class="pp-card-back">ruhlantirmoq, dalda bermoq</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>Munozara: pozitsiya = qarshilik/yoqlash + taklif; uslub = qurollar (근거/제시/인정).</li>
  <li>Rasmiy nutq: murojaat so'zi auditoriyani, birinchi jumla marosimni, oxirgisi maqsadni aytadi.</li>
  <li>Ma'no o'girish tuzog'i: "qo'rqmang" ≠ "qilmang" — inkorning o'rnini aniq eshiting.</li>
</ul>
"""},
        ],
    },
]
