# TOPIK II Listening — 47–50-savollar: Eng qiyin juftliklar (110–112) + Yakuniy takror (120).
# Ikki TOPIC bitta faylda (o'qishdagi _order_1_5.py uslubi).
# Audio: python manage.py gen_examprep_audio examprep/management/commands/_lessons_topik_listening_final_1_4.py \
#            --out examprep/management/commands/audio/final
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_final_1_4.py \
#            --author=prime --audio-dir=examprep/management/commands/audio/final

TRACK = {
    "name":    "TOPIK",
    "summary": "Koreys tili darajasini aniqlash imtihoniga tayyorgarlik.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
}

TOPIC_HARD = {
    "title":   "47–50-savollar: Eng qiyin juftliklar (대담·강연: 태도)",
    "summary": "Imtihonning so'nggi to'rt savoli: rasmiy 대담 va murakkab ma'ruzada mazmun + so'zlovchining munosabati (태도).",
    "icon":    "bi-award",
    "order":   12,
}

TOPIC_REVIEW = {
    "title":   "Yakuniy takror (총정리)",
    "summary": "Butun 듣기 kursi bo'yicha katta aralash mashq: har savol guruhidan bittadan, vaqt bosimi ostida.",
    "icon":    "bi-trophy",
    "order":   13,
}

LESSONS = [
    # ── Lesson 1 (order 110) ──────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC_HARD,
        "title":   "TOPIK 태도 1: 47–48-savollar — rasmiy suhbatda munosabat",
        "summary": "대담 juftligi: ijtimoiy masala bo'yicha mutaxassis suhbati — mazmun (47) + so'zlovchining munosabati (48, 태도).",
        "order":   110,
        "blocks": [
            {"rich_text": """
<h2>🏔️ 47–50: imtihonning eng baland cho'qqisi</h2>
<p>So'nggi to'rt savol — eng uzun va rasmiy matnlar: <strong>대담</strong> (ijtimoiy masala
bo'yicha suhbat, 47–48) va <strong>강연</strong> (ilmiy ma'ruza, 49–50). Juftlikning
ikkinchi savoli endi doim <strong>태도</strong> (munosabat) bo'ladi:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.08em;margin:0;"><strong>48/50.</strong> 남자의 태도로 가장 알맞은 것을 고르십시오. —
  <em>so'zlovchi mavzuga QANDAY qaraydi?</em></p>
</div>
<p>O'qishdagi 46–47-savollarni eslaysizmi? Xuddi o'sha lug'at — endi quloq uchun:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>우려하고 있다</strong> — xavotirda → belgi: 문제입니다, 심각합니다, ~ㄹ 수 있습니다 (salbiy oqibat)</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>높이 평가하고 있다</strong> — yuqori baholaydi → belgi: 다행입니다, 인상적입니다, 의미가 큽니다</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>경계하고 있다</strong> — ehtiyotkor → belgi: 조심해야 합니다, 서두르면 안 됩니다</p>
  <p style="font-size:1.05em;margin:0 0 6px;"><strong>촉구하고 있다</strong> — chorlaydi → belgi: 시급합니다, 서둘러 ~아야 합니다</p>
  <p style="font-size:1.05em;margin:0;"><strong>전망하고 있다 / 기대하고 있다</strong> — bashorat/umid → belgi: ~ㄹ 것입니다, ~기를 바랍니다</p>
</div>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Usul:</strong> <strong>Baho so'zlarini</strong> oving (심각하다, 다행이다,
  시급하다…) — ular munosabat fe'liga to'g'ridan-to'g'ri ko'rsatadi. Ikki ohang aralashsa
  (tan oladi + xavotir), <strong>그러나/다만dan keyingisi</strong> — asosiy munosabat.
  O'qishdagi qoida — aynan!
</div>
"""},
            {"rich_text": """
<p><strong>47-savol.</strong> 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_110_1.mp3",
             "audio_script": [
                 ("여자", "최근 배달 음식이 늘면서 일회용 플라스틱 쓰레기도 크게 늘었다고요?"),
                 ("남자", "네, 배달 한 번에 플라스틱 용기가 보통 네다섯 개씩 나옵니다. 문제는 이 용기의 상당수가 음식물이 묻어 있어서 재활용되지 못하고 그냥 버려진다는 겁니다. 몇몇 업체가 다회용기 서비스를 시작한 것은 다행이지만, 아직 참여 업체가 너무 적습니다. 정부가 지원을 늘려서 이 서비스를 서둘러 확대해야 합니다."),
             ],
             "choices": [
                 {"text": "음식물이 묻은 용기는 재활용되지 못한다. (Ovqat yuqi qolgan idishlar qayta ishlanmaydi.)", "is_correct": True},
                 {"text": "배달 음식은 점점 줄고 있다. (Yetkazib berish taomlar kamaymoqda.)", "is_correct": False},
                 {"text": "모든 업체가 다회용기를 쓰고 있다. (Hamma korxona ko'p martalik idish ishlatmoqda.)", "is_correct": False},
                 {"text": "배달 한 번에 용기가 한 개만 나온다. (Bir yetkazishda faqat bitta idish chiqadi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (배달이 <strong>늘면서</strong>!), ③ "hamma" kengaytmasi (<strong>몇몇</strong>
업체 — bir nechtasi, va 참여가 너무 <strong>적습니다</strong>!), ④ raqam (<strong>네다섯
개씩</strong>!). ✅ ①: 음식물이 묻어 있어서 재활용되지 못하고 — aynan aytilgan. Uzun
matnlarda ham tuzoqlar o'sha-o'sha: yo'nalish, "hamma/faqat", raqam.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 최근 배달 음식이 늘면서 일회용 플라스틱 쓰레기도 크게 늘었다고요?<br>
    <em style="color:#475569;">So'nggi paytlarda yetkazib berish taomlari ko'payishi bilan bir
    martalik plastik chiqindi ham keskin oshgan ekan-a?</em></p>
    <p><strong>남자:</strong> 네, 배달 한 번에 플라스틱 용기가 보통 네다섯 개씩 나옵니다. 문제는
    이 용기의 상당수가 음식물이 묻어 있어서 재활용되지 못하고 그냥 버려진다는 겁니다. 몇몇
    업체가 다회용기 서비스를 시작한 것은 다행이지만, 아직 참여 업체가 너무 적습니다. 정부가
    지원을 늘려서 이 서비스를 서둘러 확대해야 합니다.<br>
    <em style="color:#475569;">Ha, bir yetkazishda odatda to'rt-beshta plastik idish chiqadi.
    Muammo shundaki, bu idishlarning ko'pchiligida ovqat yuqi qolgani uchun qayta ishlanmasdan
    shunchaki tashlab yuboriladi. Ba'zi korxonalar ko'p martalik idish xizmatini boshlagani
    xayrli, ammo qatnashayotgan korxonalar hali juda oz. Hukumat yordamni oshirib, bu xizmatni
    tezroq kengaytirishi zarur.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>48-savol.</strong> 남자의 태도로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida — ikkinchi marta eshiting)</em></p>
""",
             "choices": [
                 {"text": "문제 해결을 위한 지원 확대를 촉구하고 있다. (Muammo yechimi uchun yordamni kengaytirishga chorlamoqda.)", "is_correct": True},
                 {"text": "현재 상황을 낙관적으로만 보고 있다. (Hozirgi holatga faqat optimistik qaramoqda.)", "is_correct": False},
                 {"text": "다회용기 서비스를 비판하고 있다. (Ko'p martalik idish xizmatini tanqid qilmoqda.)", "is_correct": False},
                 {"text": "배달 음식을 금지하자고 주장하고 있다. (Yetkazib berish taomlarini taqiqlashni talab qilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Baho so'zlari zanjiri: 문제는… (xavotir) → <strong>다행이지만</strong> (qisman ijobiy!) →
아직 너무 적습니다 → <strong>서둘러 확대해야 합니다</strong> (chorlov!) →
<mark style="background:#dcfce7;">촉구하고 있다</mark> ✅. Ikki ohang bor edi — 지만dan
keyingisi g'olib. ③ teskari: xizmatning o'zini <strong>다행</strong> dedi — u KO'PAYISHINI
so'rayapti. "faqat optimistik/butunlay qarshi" kabi keskin variantlar — odatdagi tuzoq.</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">일회용 / 다회용</div><div class="pp-card-back">bir martalik / ko'p martalik</div></div>
  <div class="pp-card"><div class="pp-card-front">용기</div><div class="pp-card-back">idish (kontener)</div></div>
  <div class="pp-card"><div class="pp-card-front">재활용</div><div class="pp-card-back">qayta ishlash</div></div>
  <div class="pp-card"><div class="pp-card-front">업체</div><div class="pp-card-back">korxona</div></div>
  <div class="pp-card"><div class="pp-card-front">확대하다</div><div class="pp-card-back">kengaytirmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">시급하다</div><div class="pp-card-back">kechiktirib bo'lmas, dolzarb</div></div>
  <div class="pp-card"><div class="pp-card-front">촉구하다</div><div class="pp-card-back">chorlamoq, talab qilmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">경계하다</div><div class="pp-card-back">ehtiyot bo'lmoq, hushyor turmoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>태도 savolida baho so'zlarini oving: 심각하다→우려, 다행이다→긍정, 서둘러야→촉구.</li>
  <li>Ikki ohangda 지만/그러나dan keyingisi — asosiy munosabat.</li>
  <li>Keskin variantlar (faqat, butunlay, taqiqlash) — muvozanatli notiqlarga yot.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 2 (order 111) ──────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC_HARD,
        "title":   "TOPIK 태도 2: 49–50-savollar — murakkab ma'ruzada munosabat",
        "summary": "강연 juftligi: tarixiy-ilmiy ma'ruzada mazmun (49) va ma'ruzachining munosabati (50) — yuqori baho, tanqid yoki ehtiyot.",
        "order":   111,
        "blocks": [
            {"rich_text": """
<h2>🎓 49–50: so'nggi juftlik qanday ko'rinadi</h2>
<p>49–50 — imtihonning yakuniy juftligi: eng murakkab <strong>ma'ruza</strong> (tarix,
ilm-fan, jamiyat). 49 — 내용 일치, 50 — ma'ruzachining <strong>태도</strong>si. Ma'ruzachining
munosabati ko'pincha <strong>oxirgi jumlada</strong> ochiladi: u faktlarni aytib bo'lib,
o'z bahosini beradi (의미가 큽니다 / 아쉬운 일입니다 / 주목해야 합니다).</p>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> 50-savolda variantlar odatda "munosabat fe'li + nimaga
  nisbatan" dan iborat (기술의 발전을 높이 평가하고 있다). <strong>Ikkala qismi ham</strong>
  to'g'ri bo'lishi shart: fe'l to'g'ri-yu ob'ekt xato bo'lsa — tuzoq!
</div>
"""},
            {"rich_text": """
<p><strong>49-savol.</strong> 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_111_1.mp3",
             "audio_script": [
                 ("여자", "조선 시대의 기록 문화를 보여 주는 대표적인 예가 바로 조선왕조실록입니다. 실록은 왕이 하루 동안 한 말과 행동을 사관이 그대로 기록한 것인데요. 놀라운 것은 왕조차 자신에 대한 기록을 마음대로 볼 수도, 고칠 수도 없었다는 점입니다. 이 원칙 덕분에 실록은 오백 년 역사를 담은 정직한 기록으로 남을 수 있었습니다. 권력 앞에서도 사실을 지키려 했던 이 정신은 오늘날의 언론에도 시사하는 바가 큽니다."),
             ],
             "choices": [
                 {"text": "왕도 실록을 마음대로 고칠 수 없었다. (Podshoh ham yilnomani xohlaganicha o'zgartira olmagan.)", "is_correct": True},
                 {"text": "실록은 왕이 직접 쓴 일기이다. (Yilnoma — podshoh o'zi yozgan kundalik.)", "is_correct": False},
                 {"text": "실록은 백 년의 역사만 담고 있다. (Yilnoma faqat yuz yillik tarixni qamragan.)", "is_correct": False},
                 {"text": "사관은 왕의 명령대로 기록을 바꿨다. (Solnomachi podshoh buyrug'i bilan yozuvni o'zgartirgan.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② muallif almashtirilgan (<strong>사관이</strong> 기록한 — solnomachi yozgan,
podshoh emas!), ③ raqam (<strong>오백 년</strong>!), ④ butun g'oyaga zid (고칠 수도
<strong>없었다</strong>!). ✅ ①: 왕조차 볼 수도, 고칠 수도 없었다 (조차 = "hatto…ham").
놀라운 것은… bilan boshlangan jumla — ma'ruzaning yuragi, savol ko'pincha aynan o'sha
yerdan keladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 조선 시대의 기록 문화를 보여 주는 대표적인 예가 바로 조선왕조실록입니다.
    실록은 왕이 하루 동안 한 말과 행동을 사관이 그대로 기록한 것인데요. 놀라운 것은 왕조차
    자신에 대한 기록을 마음대로 볼 수도, 고칠 수도 없었다는 점입니다. 이 원칙 덕분에 실록은
    오백 년 역사를 담은 정직한 기록으로 남을 수 있었습니다. 권력 앞에서도 사실을 지키려 했던
    이 정신은 오늘날의 언론에도 시사하는 바가 큽니다.<br>
    <em style="color:#475569;">Choson davri yozuv madaniyatining yorqin namunasi — Choson
    sulolasi yilnomasi. Yilnomada podshohning bir kun davomidagi so'zlari va xatti-harakatlarini
    solnomachi aynan yozib borgan. Hayratlanarlisi — hatto podshoh ham o'zi haqidagi yozuvni
    xohlaganicha ko'ra olmagan, o'zgartira ham olmagan. Shu tamoyil tufayli yilnoma besh yuz
    yillik tarixni qamragan halol yozuv bo'lib qoldi. Hokimiyat oldida ham haqiqatni asrashga
    intilgan bu ruh bugungi matbuotga ham katta saboq beradi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>50-savol.</strong> 여자의 태도로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "실록의 기록 정신을 높이 평가하고 있다. (Yilnomaning yozuv ruhini yuqori baholamoqda.)", "is_correct": True},
                 {"text": "실록의 내용을 의심하고 있다. (Yilnoma mazmuniga shubha qilmoqda.)", "is_correct": False},
                 {"text": "오늘날의 언론을 높이 평가하고 있다. (Bugungi matbuotni yuqori baholamoqda.)", "is_correct": False},
                 {"text": "기록 문화가 사라지는 것을 우려하고 있다. (Yozuv madaniyati yo'qolishidan xavotirda.)", "is_correct": False},
             ],
             "explanation": """
<p>Baho so'zlari: <strong>놀라운</strong> 것은 + <strong>정직한</strong> 기록 + 시사하는
바가 <strong>큽니다</strong> → hayrat va hurmat →
<mark style="background:#dcfce7;">높이 평가하고 있다</mark> ✅. ③ — aytganimiz "ob'ekt
tuzog'i": fe'l to'g'ri (높이 평가), ob'ekt xato — u <strong>yilnomani</strong> baholayapti,
bugungi matbuotga esa "saboq" deyapti xolos. Fe'l + ob'ekt: ikkalasini ham tekshiring!</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">실록</div><div class="pp-card-back">yilnoma</div></div>
  <div class="pp-card"><div class="pp-card-front">기록하다</div><div class="pp-card-back">yozib bormoq, qayd etmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">~조차</div><div class="pp-card-back">hatto … ham</div></div>
  <div class="pp-card"><div class="pp-card-front">원칙</div><div class="pp-card-back">tamoyil, qoida</div></div>
  <div class="pp-card"><div class="pp-card-front">정직하다</div><div class="pp-card-back">halol, rostgo'y</div></div>
  <div class="pp-card"><div class="pp-card-front">권력</div><div class="pp-card-back">hokimiyat, kuch</div></div>
  <div class="pp-card"><div class="pp-card-front">언론</div><div class="pp-card-back">matbuot, OAV</div></div>
  <div class="pp-card"><div class="pp-card-front">높이 평가하다</div><div class="pp-card-back">yuqori baholamoq</div></div>
</div>
<h3>Xulosa</h3>
<ul>
  <li>Ma'ruzachining munosabati oxirgi jumlada ochiladi (의미가 큽니다 / 시사하는 바가 큽니다).</li>
  <li>50-variant = fe'l + ob'ekt: ikkalasi ham to'g'ri bo'lsin (ob'ekt tuzog'i!).</li>
  <li>놀라운 것은… jumlasi — 49-savolning eng ehtimolli manbasi.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 3 (order 112) ──────────────────────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC_HARD,
        "title":   "TOPIK 태도 3: To'liq amaliyot — sun'iy intellekt bahsi",
        "summary": "47–50 to'liq mashqi: AI tarjimonlari haqida 대담 (mazmun+munosabat) — ehtiyotkor optimizm ohangini ushlash.",
        "order":   112,
        "blocks": [
            {"rich_text": """
<h2>🏁 To'liq amaliyot: eng qiyin juftlik</h2>
<p>Bitta uzun 대담 — to'rt savolli blokning yakuniy mashqi. Birinchi eshitishda baho
so'zlarini belgilang, ikkinchisida faktlarni tering. Nozik ohang: so'zlovchi texnologiyani
inkor ham, olqish ham qilmaydi — <strong>chegara chizadi</strong>.</p>
"""},
            {"rich_text": """
<p><strong>49-savol.</strong> 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_112_1.mp3",
             "audio_script": [
                 ("여자", "요즘 인공지능 번역기가 빠르게 발전하면서 외국어를 배울 필요가 없다는 말까지 나오는데요. 박사님은 어떻게 보십니까?"),
                 ("남자", "인공지능 번역은 분명 놀랍게 발전했습니다. 여행이나 간단한 업무에서는 이미 충분히 유용하지요. 하지만 언어는 단순한 정보 전달의 도구가 아닙니다. 상대의 문화를 이해하고 마음을 나누는 일은 번역기가 대신할 수 없습니다. 그러니까 기계에 모든 것을 맡기기보다는, 번역기를 잘 활용하면서도 언어 공부를 계속하는 것이 바람직하다고 봅니다."),
             ],
             "choices": [
                 {"text": "번역기는 여행에서 이미 유용하게 쓰인다. (Tarjimon dastur sayohatda allaqachon foydali ishlatilmoqda.)", "is_correct": True},
                 {"text": "인공지능 번역은 전혀 발전하지 못했다. (Sun'iy intellekt tarjimasi umuman rivojlanmagan.)", "is_correct": False},
                 {"text": "번역기는 문화 이해까지 대신해 준다. (Tarjimon dastur madaniyatni tushunishni ham bajarib beradi.)", "is_correct": False},
                 {"text": "남자는 외국어 공부가 필요 없다고 본다. (Erkak chet tili o'rganish keraksiz deb hisoblaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② teskari (<strong>놀랍게 발전했습니다</strong>!), ③ teskari (대신할 수
<strong>없습니다</strong>!), ④ teskari (공부를 <strong>계속하는 것이 바람직</strong>!).
✅ ①: 여행이나 간단한 업무에서는 이미 충분히 유용하지요. E'tibor: uchala noto'g'ri variant
ham "teskari" turida — uzun matnlarda inkorlarni (없습니다/않습니다) aniq eshitish hal
qiluvchi ko'nikma.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 요즘 인공지능 번역기가 빠르게 발전하면서 외국어를 배울 필요가 없다는
    말까지 나오는데요. 박사님은 어떻게 보십니까?<br>
    <em style="color:#475569;">Hozir sun'iy intellekt tarjimonlari tez rivojlanib, chet tili
    o'rganish shart emas degan gaplar ham chiqyapti. Doktor, siz bunga qanday qaraysiz?</em></p>
    <p><strong>남자:</strong> 인공지능 번역은 분명 놀랍게 발전했습니다. 여행이나 간단한 업무에서는
    이미 충분히 유용하지요. 하지만 언어는 단순한 정보 전달의 도구가 아닙니다. 상대의 문화를
    이해하고 마음을 나누는 일은 번역기가 대신할 수 없습니다. 그러니까 기계에 모든 것을
    맡기기보다는, 번역기를 잘 활용하면서도 언어 공부를 계속하는 것이 바람직하다고 봅니다.<br>
    <em style="color:#475569;">Sun'iy intellekt tarjimasi, shubhasiz, hayratlanarli rivojlandi.
    Sayohat va oddiy yumushlarda allaqachon yetarlicha foydali. Lekin til — shunchaki axborot
    yetkazish quroli emas. Suhbatdosh madaniyatini tushunish va ko'ngil bo'lishishni tarjimon
    dastur bajarib bera olmaydi. Shuning uchun hamma narsani mashinaga topshirishdan ko'ra,
    tarjimondan unumli foydalangan holda til o'rganishni davom ettirish maqsadga muvofiq deb
    bilaman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><strong>50-savol.</strong> 남자의 태도로 가장 알맞은 것을 고르십시오. <em>(audio yuqorida)</em></p>
""",
             "choices": [
                 {"text": "번역기의 발전을 인정하면서도 언어 공부의 가치를 강조하고 있다. (Tarjimon rivojini tan olgan holda til o'rganish qadrini ta'kidlamoqda.)", "is_correct": True},
                 {"text": "인공지능 기술을 강하게 반대하고 있다. (Sun'iy intellekt texnologiyasiga keskin qarshi.)", "is_correct": False},
                 {"text": "번역기가 언어 공부를 완전히 대신할 것이라고 낙관하고 있다. (Tarjimon til o'rganishni butunlay almashtiradi deb optimist.)", "is_correct": False},
                 {"text": "외국어 교육 정책을 비판하고 있다. (Chet tili ta'limi siyosatini tanqid qilmoqda.)", "is_correct": False},
             ],
             "explanation": """
<p>Chegara chizildi: 분명 발전했습니다 (tan olish) + <strong>하지만</strong> + 대신할 수
없습니다 + 계속하는 것이 <strong>바람직합니다</strong> →
<mark style="background:#dcfce7;">tan olish + ta'kid</mark> ✅. ②③ ikki qarama-qarshi
keskinlik — muvozanatli notiq ikkalasiga ham bormaydi. "A하면서도 B" (A qilgan holda B) —
50-savol javoblarining eng oltin qolipi. Blok yakunlandi: endi katta final! 🎉</p>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">인공지능</div><div class="pp-card-back">sun'iy intellekt</div></div>
  <div class="pp-card"><div class="pp-card-front">번역기</div><div class="pp-card-back">tarjimon dastur</div></div>
  <div class="pp-card"><div class="pp-card-front">유용하다</div><div class="pp-card-back">foydali</div></div>
  <div class="pp-card"><div class="pp-card-front">전달</div><div class="pp-card-back">yetkazish, uzatish</div></div>
  <div class="pp-card"><div class="pp-card-front">마음을 나누다</div><div class="pp-card-back">ko'ngil bo'lishmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">활용하다</div><div class="pp-card-back">unumli foydalanmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">바람직하다</div><div class="pp-card-back">maqsadga muvofiq</div></div>
  <div class="pp-card"><div class="pp-card-front">~(으)면서도</div><div class="pp-card-back">…gan holda ham</div></div>
</div>
<h3>Xulosa — butun mavzu bo'yicha</h3>
<ul>
  <li>47–50 matnlari uzun, lekin tuzoqlar o'sha-o'sha: inkor, "hamma/faqat", raqam, ob'ekt almashinuvi.</li>
  <li>태도 formulasi: tan olish + 하지만 + asosiy pozitsiya; javob "A하면서도 B" qolipida.</li>
  <li>Baho so'zlari lug'atingiz — o'qish 46–47 bilan umumiy: bir o'rganib, ikki joyda ishlating.</li>
</ul>
"""},
        ],
    },

    # ── Lesson 4 (order 120) — Grand review ──────────────────────────────
    {
        "skill":   "listening",
        "topic":   TOPIC_REVIEW,
        "title":   "TOPIK 총정리: Katta aralash takror — mini tinglash bo'limi",
        "summary": "Butun 듣기 kursi bo'yicha yakuniy mashq: 6 xil savol turi ketma-ket, har audio bir marta — haqiqiy imtihon ritmida.",
        "order":   120,
        "blocks": [
            {"rich_text": """
<h2>🏆 Yakuniy dars: mini tinglash bo'limi</h2>
<p>Tabriklaymiz — TOPIK II tinglash bo'limining <strong>barcha savol turlarini</strong>
o'rgandingiz! Yakuniy sinov: 6 ta savol, har biri boshqa guruhdan, osondan qiyinga.
Qoida — imtihondagidek: har audioni <strong>faqat bir marta</strong> eshiting, javobni
darhol belgilang, keyingisiga o'ting.</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma — kursning uch oltin qoidasi:</strong><br>
  1) Variantlarni <strong>oldindan o'qing</strong> — farq nuqtalarini belgilang.<br>
  2) Har eshitishga <strong>bitta vazifa</strong> — fikr yoki faktlar, ikkalasi emas.<br>
  3) Signal so'zlar hal qiladi: 하지만/그러니까/덕분에/~기 때문에/~시기 바랍니다.
</div>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">4–8-tur · 이어질 말</span></p>
<p><strong>1-savol.</strong> 다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.</p>
""",
             "audio": "topik_l_120_1.mp3",
             "audio_script": [
                 ("여자", "주말에 이사하는데 혹시 시간 있으면 좀 도와줄 수 있어요?"),
                 ("남자", "토요일은 안 되지만 일요일은 괜찮아요."),
             ],
             "choices": [
                 {"text": "그럼 일요일에 부탁할게요. (Unda yakshanba kuni iltimos qilaman.)", "is_correct": True},
                 {"text": "그럼 토요일에 만나요. (Unda shanba kuni ko'rishamiz.)", "is_correct": False},
                 {"text": "이사는 벌써 끝났어요. (Ko'chish allaqachon tugadi.)", "is_correct": False},
                 {"text": "새 집이 어디인지 모르겠어요. (Yangi uy qayerdaligini bilmayman.)", "is_correct": False},
             ],
             "explanation": """
<p>Oxirgi gap — shartli rozilik: shanba yo'q, <strong>yakshanba mumkin</strong>. Tabiiy javob —
mos kunni qabul qilish: ✅ ①. ② eshitmaganlik tuzog'i (토요일은 <strong>안 되지만</strong>!).
20-darsdagi qoida: radning ichidagi "mumkin" qismini oving.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 주말에 이사하는데 혹시 시간 있으면 좀 도와줄 수 있어요?<br>
    <em style="color:#475569;">Dam olish kunlari ko'chyapman, mabodo vaqtingiz bo'lsa yordam bera olasizmi?</em></p>
    <p><strong>남자:</strong> 토요일은 안 되지만 일요일은 괜찮아요.<br>
    <em style="color:#475569;">Shanba bo'lmaydi-yu, lekin yakshanba mayli.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">9–12-tur · 이어질 행동</span></p>
<p><strong>2-savol.</strong> 다음 대화를 잘 듣고 <u>여자가</u> 이어서 할 행동으로 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_120_2.mp3",
             "audio_script": [
                 ("여자", "회의 자료 복사 다 했어요. 이제 뭘 하면 될까요?"),
                 ("남자", "그럼 음료수 좀 준비해 줄래요? 저는 마이크를 확인할게요."),
                 ("여자", "네, 알겠습니다."),
             ],
             "choices": [
                 {"text": "음료수를 준비한다. (Ichimliklarni tayyorlaydi.)", "is_correct": True},
                 {"text": "마이크를 확인한다. (Mikrofonni tekshiradi.)", "is_correct": False},
                 {"text": "회의 자료를 복사한다. (Majlis materialini nusxalaydi.)", "is_correct": False},
                 {"text": "회의실 문을 잠근다. (Majlis xonasi eshigini qulflaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Taqsimot: 음료수 준비 — <strong>~아 줄래요?</strong> bilan ayolga yuklandi (va u rozi:
알겠습니다) ✅ ①; mikrofon — <strong>저는 ~할게요</strong> bilan erkakniki (② boshqa odam
tuzog'i); nusxalash — allaqachon <strong>bo'lgan ish</strong> (다 했어요! — ③). Uch tuzoq
bitta savolda — 31-dars formulasi to'liq ishladi.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 회의 자료 복사 다 했어요. 이제 뭘 하면 될까요?<br>
    <em style="color:#475569;">Majlis materiallarini nusxalab bo'ldim. Endi nima qilay?</em></p>
    <p><strong>남자:</strong> 그럼 음료수 좀 준비해 줄래요? 저는 마이크를 확인할게요.<br>
    <em style="color:#475569;">Unda ichimliklarni tayyorlab berasizmi? Men mikrofonni tekshiraman.</em></p>
    <p><strong>여자:</strong> 네, 알겠습니다.<br>
    <em style="color:#475569;">Xo'p, tushundim.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">13–16-tur · 내용 일치</span></p>
<p><strong>3-savol.</strong> 다음을 듣고 들은 내용과 같은 것을 고르십시오.</p>
""",
             "audio": "topik_l_120_3.mp3",
             "audio_script": [
                 ("남자", "주민 여러분께 알려 드립니다. 이번 주 토요일 아침 열 시부터 아파트 앞마당에서 나눔 장터가 열립니다. 안 쓰는 물건을 팔거나 바꿀 수 있으니 많이 참여해 주시기 바랍니다. 판매 수익금의 절반은 이웃 돕기에 쓰일 예정입니다."),
             ],
             "choices": [
                 {"text": "장터는 토요일 오전에 열린다. (Yarmarka shanba kuni tushdan oldin ochiladi.)", "is_correct": True},
                 {"text": "장터는 일요일 저녁에 열린다. (Yarmarka yakshanba kechqurun ochiladi.)", "is_correct": False},
                 {"text": "수익금은 전부 이웃 돕기에 쓰인다. (Daromadning hammasi hojatmandlarga beriladi.)", "is_correct": False},
                 {"text": "새 물건만 팔 수 있다. (Faqat yangi buyum sotish mumkin.)", "is_correct": False},
             ],
             "explanation": """
<p>소거법: ② kun-vaqt (토요일 <strong>아침 열 시</strong>!), ③ miqdor (수익금의
<strong>절반</strong> — yarmi, hammasi emas!), ④ teskari (<strong>안 쓰는</strong> 물건 —
ishlatilmayotgan!). ✅ ①: 아침 열 시 = 오전 (paraphrase). E'lon savolining uch klassigi:
vaqt, miqdor, teskari sifat.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>남자:</strong> 주민 여러분께 알려 드립니다. 이번 주 토요일 아침 열 시부터 아파트
    앞마당에서 나눔 장터가 열립니다. 안 쓰는 물건을 팔거나 바꿀 수 있으니 많이 참여해 주시기
    바랍니다. 판매 수익금의 절반은 이웃 돕기에 쓰일 예정입니다.<br>
    <em style="color:#475569;">Hurmatli aholi, e'lon qilamiz. Shu hafta shanba kuni ertalab
    soat o'ndan binoning old maydonida ulashish yarmarkasi ochiladi. Ishlatilmayotgan
    buyumlarni sotish yoki almashish mumkin — faol qatnashing. Savdo daromadining yarmi
    hojatmand qo'shnilarga yordamga sarflanadi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">17–20-tur · 중심 생각</span></p>
<p><strong>4-savol.</strong> 다음을 듣고 남자의 중심 생각으로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_120_4.mp3",
             "audio_script": [
                 ("여자", "새로 나온 휴대폰으로 바꾸려고 해요. 지금 것도 잘 되긴 하는데요."),
                 ("남자", "잘 되는데 왜 바꿔요? 새 모델이 나올 때마다 바꾸는 건 낭비예요. 고장 났을 때 바꿔도 늦지 않아요."),
             ],
             "choices": [
                 {"text": "잘 되는 물건을 자주 바꾸는 것은 낭비다. (Yaxshi ishlayotgan narsani tez-tez almashtirish — isrof.)", "is_correct": True},
                 {"text": "새 모델이 나오면 바로 사야 한다. (Yangi model chiqsa darhol olish kerak.)", "is_correct": False},
                 {"text": "휴대폰은 이 년마다 바꿔야 한다. (Telefonni ikki yilda almashtirib turish kerak.)", "is_correct": False},
                 {"text": "고장 난 물건은 버리면 안 된다. (Buzilgan narsani tashlamaslik kerak.)", "is_correct": False},
             ],
             "explanation": """
<p>Fikr so'zi ochiq keldi: 바꾸는 건 <strong>낭비예요</strong> + muqobil (고장 났을 때
바꿔도 <strong>늦지 않아요</strong>) → ✅ ①. ② teskari, ④ u aytmagan kengaytma. Erkakning
savoli (왜 바꿔요?) — ritorik: bu ham fikr belgisi (50-darsdagi ~잖아요 oilasi).</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 새로 나온 휴대폰으로 바꾸려고 해요. 지금 것도 잘 되긴 하는데요.<br>
    <em style="color:#475569;">Yangi chiqqan telefonga almashtirmoqchiman. Hozirgisi ham yaxshi ishlayapti-yu.</em></p>
    <p><strong>남자:</strong> 잘 되는데 왜 바꿔요? 새 모델이 나올 때마다 바꾸는 건 낭비예요. 고장 났을 때 바꿔도 늦지 않아요.<br>
    <em style="color:#475569;">Yaxshi ishlayotgan bo'lsa nega almashtirasiz? Har yangi model chiqqanda almashtirish — isrof. Buzilganda almashtirsangiz ham kech bo'lmaydi.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">25–30-tur · 인터뷰/직업</span></p>
<p><strong>5-savol.</strong> 남자는 누구인지 고르십시오.</p>
""",
             "audio": "topik_l_120_5.mp3",
             "audio_script": [
                 ("여자", "일하시면서 가장 신경 쓰시는 부분이 무엇인가요?"),
                 ("남자", "빵은 온도와 시간이 생명입니다. 그래서 저는 새벽 네 시에 나와서 반죽을 시작해요. 매일 같은 시간에 오븐에 넣어야 같은 맛이 나오거든요. 손님들이 갓 구운 빵 냄새에 이끌려 들어오실 때 가장 행복합니다."),
             ],
             "choices": [
                 {"text": "제빵사 (novvoy)", "is_correct": True},
                 {"text": "요리 선생님 (pazandalik o'qituvchisi)", "is_correct": False},
                 {"text": "카페 손님 (kafe mijozi)", "is_correct": False},
                 {"text": "농부 (dehqon)", "is_correct": False},
             ],
             "explanation": """
<p>Belgilar: <strong>빵</strong> + <strong>반죽</strong> (xamir) + <strong>오븐</strong> +
갓 구운 (endigina yopilgan) + 손님들이 들어오다 → <mark style="background:#dcfce7;">novvoy</mark>
✅. ② o'rgatish belgisi yo'q, ③ mijoz o'zi xizmat qilmaydi. Ob'ekt+fe'l formulasi:
빵을 굽다 → 제빵사. To'liq 71-dars uslubida.</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 일하시면서 가장 신경 쓰시는 부분이 무엇인가요?<br>
    <em style="color:#475569;">Ishlaganda eng ko'p e'tibor beradigan jihatingiz nima?</em></p>
    <p><strong>남자:</strong> 빵은 온도와 시간이 생명입니다. 그래서 저는 새벽 네 시에 나와서
    반죽을 시작해요. 매일 같은 시간에 오븐에 넣어야 같은 맛이 나오거든요. 손님들이 갓 구운 빵
    냄새에 이끌려 들어오실 때 가장 행복합니다.<br>
    <em style="color:#475569;">Non uchun harorat va vaqt — hayot-mamot masalasi. Shuning uchun
    tong saharda soat to'rtda kelib xamir qorishni boshlayman. Har kuni bir xil vaqtda tandirga
    solinsagina bir xil ta'm chiqadi-da. Mijozlar endigina yopilgan non hidiga ergashib
    kirganlarida eng baxtli bo'laman.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">47–50-tur · 태도</span></p>
<p><strong>6-savol.</strong> 여자의 태도로 가장 알맞은 것을 고르십시오.</p>
""",
             "audio": "topik_l_120_6.mp3",
             "audio_script": [
                 ("여자", "최근 청소년들의 스마트폰 사용 시간이 하루 평균 다섯 시간을 넘었습니다. 스마트폰이 학습에 도움이 되는 부분도 분명히 있습니다. 하지만 수면 부족과 운동 부족으로 이어지는 지금의 상황은 결코 가볍게 볼 일이 아닙니다. 가정과 학교가 함께 사용 규칙을 만드는 일이 시급합니다."),
             ],
             "choices": [
                 {"text": "청소년의 스마트폰 사용 문제를 우려하며 대책 마련을 촉구하고 있다. (O'smirlarning telefon ishlatishidan xavotirda va chora ko'rishga chorlamoqda.)", "is_correct": True},
                 {"text": "스마트폰의 교육 효과를 높이 평가하기만 한다. (Telefonning ta'lim samarasini yuqori baholayapti xolos.)", "is_correct": False},
                 {"text": "청소년에게 스마트폰을 더 많이 주자고 제안하고 있다. (O'smirlarga telefonni ko'proq beraylik deb taklif qilmoqda.)", "is_correct": False},
                 {"text": "지금 상황에 아무 문제가 없다고 본다. (Hozirgi holatda hech muammo yo'q deb hisoblaydi.)", "is_correct": False},
             ],
             "explanation": """
<p>Formula so'nggi marta: tan olish (도움이 되는 부분<strong>도</strong> 있습니다) +
<strong>하지만</strong> + baho so'zlari (결코 가볍게 볼 일이 <strong>아닙니다</strong> +
<strong>시급합니다</strong>) → <mark style="background:#dcfce7;">우려 + 촉구</mark> ✅.
6 tadan nechta to'g'ri? 5–6 bo'lsa — 듣기 bo'limiga tayyorsiz! Endi mock testlarda vaqt
bilan ishlang (모의고사 — exam bo'limida). Butun kurs yakunlandi — 화이팅! 🏆</p>
<details style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">📜 Skript va tarjima — bosing</summary>
  <div style="margin-top:10px;">
    <p><strong>여자:</strong> 최근 청소년들의 스마트폰 사용 시간이 하루 평균 다섯 시간을 넘었습니다.
    스마트폰이 학습에 도움이 되는 부분도 분명히 있습니다. 하지만 수면 부족과 운동 부족으로
    이어지는 지금의 상황은 결코 가볍게 볼 일이 아닙니다. 가정과 학교가 함께 사용 규칙을 만드는
    일이 시급합니다.<br>
    <em style="color:#475569;">So'nggi ma'lumotlarga ko'ra, o'smirlarning telefon ishlatish vaqti
    kuniga o'rtacha besh soatdan oshdi. Telefonning o'qishga yordam beradigan jihatlari ham,
    shubhasiz, bor. Lekin uyqu va harakat yetishmasligiga olib borayotgan hozirgi holatga aslo
    yengil qarab bo'lmaydi. Oila va maktab birgalikda foydalanish qoidalarini ishlab chiqishi
    kechiktirib bo'lmas masala.</em></p>
  </div>
</details>
"""},
            {"rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<div class="pp-flashcards" data-pp-flashcards>
  <div class="pp-card"><div class="pp-card-front">이사하다</div><div class="pp-card-back">ko'chmoq</div></div>
  <div class="pp-card"><div class="pp-card-front">나눔 장터</div><div class="pp-card-back">ulashish yarmarkasi</div></div>
  <div class="pp-card"><div class="pp-card-front">수익금</div><div class="pp-card-back">daromad (tushum)</div></div>
  <div class="pp-card"><div class="pp-card-front">낭비</div><div class="pp-card-back">isrof</div></div>
  <div class="pp-card"><div class="pp-card-front">반죽</div><div class="pp-card-back">xamir</div></div>
  <div class="pp-card"><div class="pp-card-front">갓 구운</div><div class="pp-card-back">endigina yopilgan (pishgan)</div></div>
  <div class="pp-card"><div class="pp-card-front">평균</div><div class="pp-card-back">o'rtacha</div></div>
  <div class="pp-card"><div class="pp-card-front">결코 ~이 아니다</div><div class="pp-card-back">aslo … emas</div></div>
</div>
<h3>Xulosa — butun 듣기 kursi bo'yicha 🏆</h3>
<ul>
  <li><strong>Uch oltin qoida:</strong> variantlarni oldindan o'qish · har eshitishga bitta vazifa · signal so'zlarni ovlash.</li>
  <li><strong>Doimiy tuzoqlar:</strong> boshqa odamning ishi, bo'lgan/uzoq ish, teskari yo'nalish, "hamma/faqat", raqam-vaqt almashinuvi, teskari his-tuyg'u, ob'ekt almashinuvi.</li>
  <li><strong>Endi nima?</strong> Podkast metodini davom ettiring (60/30/10!) va imtihonga ~1 oy qolganda mock testlarda vaqt mashqini boshlang.</li>
  <li>Omad, kelajak topikchilari! 화이팅! 💪🏆</li>
</ul>
"""},
        ],
    },
]
