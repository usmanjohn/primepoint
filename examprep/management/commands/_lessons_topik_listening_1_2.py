# TOPIK II Tinglash (듣기) darslari 1–2 — Podkast metodi. Foydalanuvchining maslahati asosida.
# Til: O'zbekcha + Koreyscha, rangli styling bilan.
#
# >>> HAVOLA: quyida __PODCAST_URL__ — foydalanuvchi keyin haqiqiy URL bilan almashtiradi.
#     Find-replace: __PODCAST_URL__  ->  https://...   (keyin --republish bilan qayta import).
#
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_listening_1_2.py --author=prime
# (mavjudini yangilash uchun --republish qo'shing).

TRACK = {
    "name":    "TOPIK",
    "summary": "TOPIK II Koreys tili imtihoniga bosqichma-bosqich tayyorgarlik — "
               "O'qish, Yozish va Tinglash bo'yicha strategiya va amaliyot.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

LESSONS = [
    # ══════════════════════════════════════════════════════════════════════
    # 1-DARS — Nega podkast?
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "listening",
        "title":   "TOPIK Listening 1: Nega podkast eng yaxshi mashq",
        "summary": "Tinglashni musiqa yoki drama emas, podkast orqali rivojlantiring — "
                   "tavsiya: 빅데이터로 보는 세상.",
        "order":   1,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Listening 1: Nega podkast eng yaxshi mashq</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">듣기</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">팟캐스트 metodi</span></p>
<p>듣기 bo'limida audiolar ko'p, lekin ko'pchiligi <mark>bir xil va zerikarli</mark>.
Tinglashni haqiqatan rivojlantirishning eng yaxshi yo'li — <strong>podkast</strong>. Keling,
nega ekanini ko'ramiz.</p>
""",
            },
            {
                "rich_text": """
<h3>Nega musiqa va drama emas?</h3>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Koreyscha musiqa tinglash yoki drama ko'rish tinglashni
  <strong>unchalik yaxshilamaydi</strong>:
  <ul style="margin:8px 0 0;">
    <li>juda <mark style="background:#fee2e2;">ko'p vaqt</mark> oladi;</li>
    <li>ular TOPIK tinglash <strong>dialoglari turiga to'g'ri kelmaydi.</strong></li>
  </ul>
</div>
""",
            },
            {
                "rich_text": """
<h3>Eng yaxshi tavsiya — 빅데이터로 보는 세상</h3>
<p>Men eshitgan eng zo'r podkast seriyasi — <strong>빅데이터로 보는 세상</strong>
(<em>“Katta ma'lumotlar orqali dunyoga nazar”</em>).</p>
<div style="background:#f1f5f9;border-radius:10px;padding:16px;margin:12px 0;text-align:center;">
  <p style="font-size:1.15em;margin:0 0 4px;"><strong>🎧 빅데이터로 보는 세상</strong></p>
  <p style="color:#475569;margin:0 0 12px;"><em>Mavzularga shu yerdan kirishingiz mumkin:</em></p>
  <a href="__PODCAST_URL__" target="_blank" rel="noopener"
     style="display:inline-block;background:#3b82f6;color:#fff;text-decoration:none;padding:10px 22px;border-radius:8px;font-weight:600;">
     Podkast mavzulariga o'tish →</a>
  <p style="color:#94a3b8;font-size:0.85em;margin:10px 0 0;">(havola tez orada qo'shiladi)</p>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Bu podkastdagi deyarli barcha mavzular Tinglash imtihonida
  uchrashi mumkin — <strong>yangiliklarga oid (뉴스)</strong> savollar va undan
  <strong>murakkabroq</strong> savollar ham.
</div>
""",
            },
            {
                "rich_text": """
<h3>Podkast bir vaqtning o'zida 4 narsani beradi</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 200px;background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 14px;border-radius:8px;">
    <strong>👂 Tinglash</strong><br>Haqiqiy, tabiiy koreyscha nutq.
  </div>
  <div style="flex:1 1 200px;background:#faf5ff;border-left:4px solid #a855f7;padding:12px 14px;border-radius:8px;">
    <strong>🧠 Mantiq</strong><br>Fikrlash va dalil keltirishni o'rgatadi.
  </div>
  <div style="flex:1 1 200px;background:#ecfdf5;border-left:4px solid #10b981;padding:12px 14px;border-radius:8px;">
    <strong>🇰🇷 Koreyscha tafakkur</strong><br>Koreyslarning yashash va fikrlash tarziga moslashasiz.
  </div>
  <div style="flex:1 1 200px;background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 14px;border-radius:8px;">
    <strong>✍️ Yozish uchun fikr</strong><br>Mavzular 쓰기 (54) da ham juda asqotadi.
  </div>
</div>
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>듣기</strong> — tinglash</li>
  <li><strong>팟캐스트</strong> — podkast</li>
  <li><strong>뉴스</strong> — yangiliklar</li>
  <li><strong>빅데이터</strong> — katta ma'lumotlar</li>
  <li><strong>세상</strong> — dunyo</li>
  <li><strong>대화</strong> — dialog / suhbat</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>Musiqa/drama emas — podkast eng yaxshi tinglash mashqi.</li>
    <li>Tavsiya: 빅데이터로 보는 세상 — mavzulari imtihonga mos.</li>
    <li>Podkast bir vaqtda tinglash, mantiq, tafakkur va yozish fikrlarini beradi.</li>
  </ul>
</div>
""",
            },
            {
                "rich_text": "<p><strong>Amaliyot.</strong> Maslahatga ko'ra, tinglashni "
                             "rivojlantirish uchun eng yaxshi vosita qaysi?</p>",
                "choices": [
                    {"text": "Koreyscha qo'shiqlarni tinglash", "is_correct": False},
                    {"text": "Drama va kinolarni ko'rish", "is_correct": False},
                    {"text": "Podkast (masalan, 빅데이터로 보는 세상)", "is_correct": True},
                    {"text": "Faqat mock testlarni qayta-qayta yechish", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>podkast</strong>. Musiqa va drama ko'p "
                               "vaqt oladi va TOPIK dialog turiga mos kelmaydi; podkast esa "
                               "imtihonga mos mavzularni tabiiy nutq bilan beradi.</p>",
            },
        ],
    },
    # ══════════════════════════════════════════════════════════════════════
    # 2-DARS — Podkastni qanday tinglash
    # ══════════════════════════════════════════════════════════════════════
    {
        "skill":   "listening",
        "title":   "TOPIK Listening 2: Podkastni qanday tinglash kerak",
        "summary": "Podkast tinglash qoidalari — yozmang, tarjima qilmang, yurib-ishlab tinglang — "
                   "va 60/30/10 mashq nisbati.",
        "order":   2,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Listening 2: Podkastni qanday tinglash kerak</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">듣기</span>
&nbsp;<span style="background:#ef4444;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">주의 — qoidalar</span></p>
<p>Podkast foyda berishi uchun uni <mark>to'g'ri tinglash</mark> kerak. Quyidagi oddiy
qoidalarga amal qiling.</p>
""",
            },
            {
                "rich_text": """
<h3>⚠️ Qilmaslik kerak</h3>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <ul style="margin:0;">
    <li><strong>Skriptni yozishga urinmang</strong> (받아쓰기 qilmang).</li>
    <li><strong>Tarjima qilmang.</strong></li>
    <li>Bo'sh vaqtingizni faqat tinglashga sarflamang.</li>
  </ul>
</div>
<h3>✅ Qanday tinglash</h3>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <ul style="margin:0;">
    <li><strong>Yurganda, ovqat pishirganda, ovqatlanganda, ishlaganda</strong> tinglang —
        ya'ni boshqa ish bilan <mark style="background:#dcfce7;">bir vaqtda.</mark></li>
    <li>Podkastlar <strong>tartibi muhim emas</strong> — istalganidan boshlang.</li>
    <li><strong>Tushunmasangiz ham tinglayvering</strong> — quloq asta-sekin o'rganadi.</li>
  </ul>
</div>
""",
            },
            {
                "rich_text": """
<h3>Eshitgan fikrlarni eslab qoling — 쓰기 uchun</h3>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eslatma:</strong> Iloji bo'lsa, podkastdan eshitgan <strong>g'oyalarni</strong>
  eslab qoling — ularni <strong>Yozish (54)</strong> inshosida ham ishlatishingiz mumkin.
  Shunday qilib tinglash ham, yozish ham bir vaqtda rivojlanadi.
</div>
""",
            },
            {
                "rich_text": """
<h3>Mashq nisbati — 60 / 30 / 10</h3>
<p>Tinglash mashqlaringizni shunday taqsimlang:</p>
<div style="display:flex;height:30px;border-radius:8px;overflow:hidden;margin:14px 0;font-size:0.78em;color:#fff;text-align:center;line-height:30px;font-weight:600;">
  <div style="width:60%;background:#3b82f6;">60% 팟캐스트</div>
  <div style="width:30%;background:#a855f7;">30% kitob</div>
  <div style="width:10%;background:#f59e0b;">10% mock</div>
</div>
<ul>
  <li><strong>60%</strong> — podkast (asosiy mashq).</li>
  <li><strong>30%</strong> — boshqa kitoblardagi tinglash materiallari.</li>
  <li><strong>10%</strong> — mock (sinov) testlar.</li>
</ul>
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>받아쓰기</strong> — diktant (skript yozish)</li>
  <li><strong>번역</strong> — tarjima</li>
  <li><strong>동시에</strong> — bir vaqtning o'zida</li>
  <li><strong>순서</strong> — tartib</li>
  <li><strong>모의고사</strong> — sinov (mock) test</li>
  <li><strong>생각</strong> — fikr / g'oya</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>Yozmang, tarjima qilmang — shunchaki tinglang.</li>
    <li>Boshqa ish bilan bir vaqtda tinglang; tartib muhim emas.</li>
    <li>Eshitgan g'oyalarni 쓰기 uchun eslab qoling.</li>
    <li>Nisbat: 60% podkast, 30% kitob, 10% mock.</li>
  </ul>
</div>
""",
            },
            {
                "rich_text": "<p><strong>Amaliyot.</strong> Maslahatga ko'ra, podkast tinglash "
                             "mashqlarining qancha qismini tashkil etishi kerak?</p>",
                "choices": [
                    {"text": "10%", "is_correct": False},
                    {"text": "30%", "is_correct": False},
                    {"text": "60%", "is_correct": True},
                    {"text": "100%", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>60%</strong>. Qolgan 30% boshqa "
                               "kitoblardan, 10% esa mock testlardan bo'lishi tavsiya etiladi. "
                               "Podkast — asosiy, lekin yagona mashq emas.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot 2.</strong> Podkastni qanday tinglagan "
                             "ma'qul?</p>",
                "choices": [
                    {"text": "Har bir gapni eshitib, skriptini yozaman.", "is_correct": False},
                    {"text": "Yurganda yoki ish qilganda, tushunmasam ham tinglayveraman.", "is_correct": True},
                    {"text": "Har bir so'zni darrov tarjima qilaman.", "is_correct": False},
                    {"text": "Faqat bo'sh vaqtimda, jim o'tirib tinglayman.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — boshqa ish bilan <strong>bir vaqtda</strong>, "
                               "tushunmasangiz ham tinglash. Skript yozish va tarjima qilish vaqtni "
                               "behuda oladi va tabiiy tinglashga xalaqit beradi.</p>",
            },
        ],
    },
]
