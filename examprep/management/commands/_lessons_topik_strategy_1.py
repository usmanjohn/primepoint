# TOPIK II Strategiya (전략) darsi 1 — "Bittani mukammal o'rganing" + tayyorgarlik jadvali.
# Foydalanuvchining maslahati asosida. Til: O'zbekcha + Koreyscha, rangli styling bilan.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_strategy_1.py --author=prime
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
    {
        "skill":   "strategy",
        "title":   "TOPIK Strategy 1: Ko'p emas — bittani mukammal o'rganing",
        "summary": "200 dan ortiq shablonni emas, bittasini tanlab mukammal egallang; "
                   "imtihongacha faqat o'qing, oxirgi oyda yozishni boshlang.",
        "order":   1,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Strategy 1: Ko'p emas — bittani mukammal o'rganing</h2>
<p><span style="background:#f59e0b;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">전략</span>
&nbsp;<span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">reja · vaqt</span></p>
<p>Darslarda <strong>200 dan ortiq</strong> namuna va shablon bor. Hammasini o'rganishga
urinmang — bu <mark>eng katta xato</mark>. Bu darsda to'g'ri strategiyani ko'ramiz.</p>
""",
            },
            {
                "rich_text": """
<h3>Muammo — hammasini o'rganmang</h3>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> Har bir shablonni yodlashga <mark style="background:#fee2e2;">ko'p vaqt
  sarflamang.</mark> Hammasini yuzaki bilish — imtihonda chalkashlik, ikkilanish va xatoga olib keladi.
</div>
<h3>Yechim — bittasini tanlang va mukammal egallang</h3>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Qoida:</strong> Har bir qism uchun <strong>faqat bitta shablonni</strong> tanlang
  va uni <mark style="background:#dcfce7;">mukammal darajada</mark> o'zlashtiring. Bitta ishonchli
  shablon — imtihonda avtomatik, xatosiz va tez ishlaydi.
</div>
""",
            },
            {
                "rich_text": """
<h3>Nega bitta yetarli? — bitta shablon, ko'p mavzu</h3>
<p>Bitta yaxshi 서론 (kirish) shablonini tanlasangiz, uni <strong>istalgan mavzuga</strong>
moslay olasiz. Masalan, bitta shablon:</p>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>Shablon:</strong> <em>현대 사회에서 [주제]은/는 점점 더 중요한 문제가 되고 있다.</em><br>
  <span style="color:#475569;">Zamonaviy jamiyatda [mavzu] tobora muhim masalaga aylanmoqda.</span>
</div>
<p>Endi shu bitta shablon 3 xil mavzuda:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
  <p style="margin:0 0 4px;"><strong>🌱 환경:</strong> 현대 사회에서 <u>환경 오염</u>은 점점 더 중요한 문제가 되고 있다.</p>
  <p style="color:#475569;margin:0;"><em>Zamonaviy jamiyatda atrof-muhit ifloslanishi tobora muhim masalaga aylanmoqda.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
  <p style="margin:0 0 4px;"><strong>📚 교육:</strong> 현대 사회에서 <u>조기 교육</u>은 점점 더 중요한 문제가 되고 있다.</p>
  <p style="color:#475569;margin:0;"><em>Zamonaviy jamiyatda erta ta'lim tobora muhim masalaga aylanmoqda.</em></p>
</div>
<div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
  <p style="margin:0 0 4px;"><strong>🤖 과학:</strong> 현대 사회에서 <u>인공지능</u>은 점점 더 중요한 문제가 되고 있다.</p>
  <p style="color:#475569;margin:0;"><em>Zamonaviy jamiyatda sun'iy intellekt tobora muhim masalaga aylanmoqda.</em></p>
</div>
<p>Ko'rdingizmi? <mark>Bitta shablon</mark> + almashadigan <mark style="background:#dbeafe;">[주제]</mark>
= har qanday mavzuga tayyor kirish.</p>
""",
            },
            {
                "rich_text": """
<h3>Tayyorgarlik jadvali — qachon o'qish, qachon yozish</h3>
<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:stretch;margin:14px 0;">
  <div style="flex:2 1 280px;background:#eff6ff;border-left:4px solid #3b82f6;padding:14px 16px;border-radius:8px;">
    <strong>1-bosqich — Imtihongacha (uzoq davr)</strong><br>
    <span style="color:#475569;">Faqat <strong>o'qing va o'rganing</strong> (input). Namunalarni
    o'qing, bitta shablonni tanlab mustahkamlang. Hali to'liq javob yozmang.</span>
  </div>
  <div style="display:flex;align-items:center;justify-content:center;font-size:1.6em;color:#94a3b8;">→</div>
  <div style="flex:2 1 280px;background:#ecfdf5;border-left:4px solid #10b981;padding:14px 16px;border-radius:8px;">
    <strong>2-bosqich — Imtihondan ~1 oy oldin</strong><br>
    <span style="color:#475569;">Endi <strong>1–2 savolga</strong> to'liq yozib javob bering
    (output). Vaqt bilan mashq qiling. Oldin o'qiganlaringiz shu yerda ishga tushadi.</span>
  </div>
</div>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:12px 0;">
  <strong>📌 Eslatma:</strong> Yozishni juda erta boshlash shart emas. Avval yetarlicha
  <strong>o'qing (input)</strong>, keyin oxirgi oyda <strong>yozing (output)</strong> — bu tartib
  vaqtni tejaydi va natijani oshiradi.
</div>
""",
            },
            {
                "rich_text": """
<h3>Nega bu strategiya ishlaydi?</h3>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 200px;background:#faf5ff;border-left:4px solid #a855f7;padding:12px 14px;border-radius:8px;">
    <strong>⚡ Avtomatik</strong><br>Bitta shablon esda mustahkam — o'ylab o'tirmaysiz.
  </div>
  <div style="flex:1 1 200px;background:#ecfdf5;border-left:4px solid #10b981;padding:12px 14px;border-radius:8px;">
    <strong>✅ Xatosiz</strong><br>Mukammal bilgan shabloningizda xato bo'lmaydi.
  </div>
  <div style="flex:1 1 200px;background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 14px;border-radius:8px;">
    <strong>⏱️ Tez</strong><br>Vaqt tig'izligida ikkilanmaysiz, tez yozasiz.
  </div>
</div>
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>전략</strong> — strategiya</li>
  <li><strong>주제</strong> — mavzu</li>
  <li><strong>서론</strong> — kirish</li>
  <li><strong>연습</strong> — mashq</li>
  <li><strong>현대 사회</strong> — zamonaviy jamiyat</li>
  <li><strong>점점 더</strong> — tobora ko'proq</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>200+ shablonni emas — bittasini tanlab mukammal o'rganing.</li>
    <li>Bitta shablon [주제] ni almashtirib, har mavzuga yetadi.</li>
    <li>Imtihongacha o'qing; oxirgi ~1 oyda 1–2 savolga yozib mashq qiling.</li>
  </ul>
</div>
""",
            },
            {
                "rich_text": "<p><strong>Amaliyot 1.</strong> 200 dan ortiq shablon bilan nima "
                             "qilish to'g'ri?</p>",
                "choices": [
                    {"text": "Hammasini yodlashga harakat qilaman.", "is_correct": False},
                    {"text": "Bittasini tanlab, uni mukammal egallayman.", "is_correct": True},
                    {"text": "Hech birini o'rganmayman, imtihonda o'ylab topaman.", "is_correct": False},
                    {"text": "Har kuni yangi 10 tasini o'zgartiraman.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>bittasini tanlab, mukammal egallash</strong>. "
                               "Bitta ishonchli shablon imtihonda avtomatik, xatosiz va tez ishlaydi; "
                               "hammasini yuzaki bilish esa chalkashlik keltiradi.</p>",
            },
            {
                "rich_text": "<p><strong>Amaliyot 2.</strong> To'liq javob yozib mashq qilishni "
                             "qachon boshlash ma'qul?</p>",
                "choices": [
                    {"text": "Tayyorgarlikning eng boshidan.", "is_correct": False},
                    {"text": "Imtihondan taxminan 1 oy oldin (till then — faqat o'qib-o'rganish).", "is_correct": True},
                    {"text": "Imtihondan bir kun oldin.", "is_correct": False},
                    {"text": "Hech qachon — faqat o'qish yetarli.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — imtihondan <strong>~1 oy oldin</strong>. Unga qadar "
                               "faqat o'qing va o'rganing (input); oxirgi oyda 1–2 savolga yozib "
                               "(output) mashq qiling. Bu tartib vaqtni tejaydi.</p>",
            },
        ],
    },
]
