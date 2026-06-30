# TOPIK II O'qish (읽기) darsi 4 — "Ko'p o'qing, kam tarjima qiling" metodi.
# Foydalanuvchining maslahati asosida. Til: O'zbekcha + Koreyscha, rangli styling bilan.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_4.py --author=prime
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
        "skill":   "reading",
        "title":   "TOPIK Reading 4: Ko'p o'qing, kam tarjima qiling",
        "summary": "So'z o'rganishning tabiiy metodi — ko'zni mashq qildiring, qo'lni emas — "
                   "va o'qishda topgan jumlalarni Yozish bo'limida ishlatish.",
        "order":   4,
        "blocks": [
            # ── 1. Kirish ────────────────────────────────────────────────
            {
                "rich_text": """
<h2>TOPIK Reading 4: Ko'p o'qing, kam tarjima qiling</h2>
<p><span style="background:#3b82f6;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">읽기</span>
&nbsp;<span style="background:#a855f7;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">어휘 metodi</span>
&nbsp;<span style="background:#10b981;color:#fff;padding:2px 10px;border-radius:999px;font-size:0.85em;">읽기 → 쓰기</span></p>
<p>So'zlarni yodlash emas, balki <mark>tabiiy ravishda o'zlashtirish</mark> haqida. Bu metod
o'qishni tezlashtiradi va undan topilgan jumlalar Yozish (쓰기) bo'limida ham qo'l keladi.</p>
""",
            },
            # ── 2. Asosiy tamoyil ────────────────────────────────────────
            {
                "rich_text": """
<h3>Asosiy tamoyil — ko'zni mashq qildiring</h3>
<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>💡 Qoida:</strong> So'zni <mark style="background:#dcfce7;">ko'rganda tushunish</mark>
  — uni yozib yodlashdan muhimroq. Shuning uchun <strong>ko'zingizni mashq qildiring,
  qo'lingizni emas.</strong> Ko'p o'qing, kam tarjima qiling.
</div>
<p>Imtihonda sizdan so'zni yozish emas, <strong>ko'rib tushunish</strong> talab qilinadi.
Demak, mashq ham shunga mos bo'lishi kerak.</p>
""",
            },
            # ── 3. Tarjima qilsangiz ham ─────────────────────────────────
            {
                "rich_text": """
<h3>Agar tarjima qilsangiz ham...</h3>
<ul>
  <li>So'zning <strong>o'zini qog'ozga ko'chirib</strong>, undan yodlamang.</li>
  <li>Buning o'rniga <mark style="background:#dbeafe;">bir-ikki kundan keyin butun matnni
      qaytadan o'qing</mark> — shunda o'rgangan so'zlaringiz xotirada mustahkamlanadi.</li>
</ul>
<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>⚠️ Diqqat:</strong> So'zlar ro'yxatini yodlash tez unutiladi. <strong>Matn ichida</strong>
  qayta uchratish — eslab qolishning eng tabiiy yo'li.
</div>
""",
            },
            # ── 4. Qaysi so'zlarni ────────────────────────────────────────
            {
                "rich_text": """
<h3>Qaysi so'zlarni ko'proq o'rganish kerak?</h3>
<p>Ko'pchilik <strong>otlarni (명사)</strong> yodlaydi, lekin javoblarni ko'pincha
<mark>sifat, ravish va fe'llar</mark> hal qiladi. Shularga e'tibor bering:</p>
<div style="display:flex;flex-wrap:wrap;gap:10px;margin:12px 0;">
  <div style="flex:1 1 200px;background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 14px;border-radius:8px;">
    <strong>형용사 — Sifat</strong><br>
    합리적이다 — oqilona<br>효율적이다 — samarali<br>자연스럽다 — tabiiy
  </div>
  <div style="flex:1 1 200px;background:#faf5ff;border-left:4px solid #a855f7;padding:12px 14px;border-radius:8px;">
    <strong>부사 — Ravish</strong><br>자연스럽게 — tabiiy ravishda<br>꾸준히 — muntazam<br>효율적으로 — samarali tarzda
  </div>
  <div style="flex:1 1 200px;background:#ecfdf5;border-left:4px solid #10b981;padding:12px 14px;border-radius:8px;">
    <strong>동사 — Fe'l</strong><br>동참하다 — qatnashmoq<br>이루다 — erishmoq<br>존중하다 — hurmat qilmoq
  </div>
</div>
<p><em>Nega? Chunki sifat, ravish va fe'llar gapning ma'nosini va savol javobini ko'proq belgilaydi.</em></p>
""",
            },
            # ── 5. Jumlalarni yig'ing (ko'prik 쓰기 ga) ──────────────────
            {
                "rich_text": """
<h3>Yaxshi jumlalarni yozib boring — Yozish uchun</h3>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Eng muhim odat:</strong> O'qiyotganda <strong>ajoyib jumla</strong> uchratsangiz
  (so'z yoki paragraf emas — <mark style="background:#dcfce7;">aynan jumla</mark>), uni yozib qo'ying.
  Keyin uni <strong>쓰기 (Yozish)</strong> bo'limida ishlatasiz.
</div>
<p>Mana foydalanuvchi bergan namuna — eslab qolish oson, ko'p mavzuga mos:</p>
<div style="background:#f1f5f9;border-radius:10px;padding:14px 16px;margin:10px 0;">
  <p style="font-size:1.12em;margin:0 0 6px;"><strong>합리적 소비를 하면 자연스럽게 사회 활동에도 동참할 수 있다.</strong></p>
  <p style="color:#475569;margin:0;"><em>Oqilona iste'mol qilsangiz, tabiiy ravishda ijtimoiy faoliyatda ham qatnasha olasiz.</em></p>
</div>
""",
            },
            # ── 6. Ko'p namuna (dropdown) ────────────────────────────────
            {
                "rich_text": """
<h3>📂 Yig'ib qo'yiladigan ajoyib jumlalar</h3>
<details open style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin:12px 0;">
  <summary style="cursor:pointer;font-weight:600;">Eslab qolish oson, ko'p mavzuga mos jumlalar (bosing)</summary>
  <div style="margin-top:10px;">
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>꾸준히 노력하면 누구나 목표를 이룰 수 있다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Muntazam harakat qilsa, har kim maqsadiga erisha oladi.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>작은 습관이 큰 변화를 만든다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Kichik odat katta o'zgarish yaratadi.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>다른 사람의 의견을 존중하는 태도가 중요하다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Boshqalarning fikrini hurmat qilish muhim.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>환경을 보호하는 것은 우리 모두의 책임이다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Atrof-muhitni asrash — barchamizning mas'uliyatimiz.</em></p>
    </div>
    <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:8px 0;">
      <p style="margin:0 0 4px;"><strong>시간을 효율적으로 사용하는 것이 성공의 열쇠이다.</strong></p>
      <p style="color:#475569;margin:0;"><em>Vaqtni samarali ishlatish — muvaffaqiyat kaliti.</em></p>
    </div>
  </div>
</details>
""",
            },
            # ── 7. Yozishda ishlatish (use cases) ────────────────────────
            {
                "rich_text": """
<h3>Yozishda qanday ishlatamiz? (쓰기 use case)</h3>
<p>Yig'ilgan jumlani 쓰기 54 inshosida <strong>tayanch fikr</strong> qilib oling, atrofini
o'zingiz to'ldiring. Misol:</p>
<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📝 Namuna — bitta jumladan abzas:</strong>
  <div style="background:#f1f5f9;border-radius:10px;padding:12px 14px;margin:10px 0 0;">
    <p style="margin:0 0 4px;"><strong>합리적 소비를 하면 자연스럽게 사회 활동에도 동참할 수 있다.</strong>
    예를 들어, 필요한 물건만 사는 사람은 돈과 자원을 아낄 수 있다. 따라서 합리적 소비는 개인과 사회 모두에게 도움이 된다.</p>
    <p style="color:#475569;margin:0;"><em>Oqilona iste'mol qilsangiz, tabiiy ravishda ijtimoiy
    faoliyatda ham qatnasha olasiz. Masalan, faqat kerakli narsani sotib oladigan inson pul va
    resurslarni tejaydi. Shuning uchun oqilona iste'mol ham shaxsga, ham jamiyatga foyda keltiradi.</em></p>
  </div>
</div>
<p>Ko'rib turganingizdek: <mark>1 yig'ilgan jumla</mark> + <mark style="background:#dbeafe;">1 misol</mark>
+ <mark style="background:#dcfce7;">1 xulosa</mark> = tayyor abzas. Vaqt tejaladi, xato kamayadi.</p>
""",
            },
            # ── 8. Kalit so'zlar + Xulosa ────────────────────────────────
            {
                "rich_text": """
<h3>Kalit so'zlar — 핵심 단어</h3>
<ul>
  <li><strong>어휘</strong> — so'z boyligi (leksika)</li>
  <li><strong>형용사</strong> — sifat</li>
  <li><strong>부사</strong> — ravish</li>
  <li><strong>동사</strong> — fe'l</li>
  <li><strong>명사</strong> — ot</li>
  <li><strong>합리적이다</strong> — oqilona</li>
  <li><strong>자연스럽게</strong> — tabiiy ravishda</li>
  <li><strong>동참하다</strong> — qatnashmoq</li>
</ul>
<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;border-radius:8px;margin:16px 0;">
  <strong>📌 Xulosa</strong>
  <ul style="margin:8px 0 0;">
    <li>Ko'p o'qing, kam tarjima qiling — ko'zni mashq qildiring, qo'lni emas.</li>
    <li>Tarjima qilsangiz ham, matnni bir-ikki kundan keyin qayta o'qing.</li>
    <li>Sifat, ravish, fe'llarni otdan ko'ra ko'proq o'rganing.</li>
    <li>Ajoyib jumlalarni yozib boring va 쓰기 da tayanch fikr qiling.</li>
  </ul>
</div>
""",
            },
            # ── 9. Amaliyot 1 ────────────────────────────────────────────
            {
                "rich_text": "<p><strong>Amaliyot 1.</strong> Metodga ko'ra, javoblarni "
                             "ko'proq hal qiladigan, shuning uchun birinchi o'rganiladigan "
                             "so'z turlari qaysi?</p>",
                "choices": [
                    {"text": "Otlar (명사)", "is_correct": False},
                    {"text": "Sifat, ravish va fe'llar (형용사·부사·동사)", "is_correct": True},
                    {"text": "Sonlar (숫자)", "is_correct": False},
                    {"text": "Bog'lovchilar (접속사)", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>sifat, ravish va fe'llar</strong>. "
                               "Ular gapning ma'nosini va savol javobini otlarga qaraganda ko'proq "
                               "belgilaydi, shuning uchun avval shularni o'rganish foydaliroq.</p>",
            },
            # ── 10. Amaliyot 2 ───────────────────────────────────────────
            {
                "rich_text": "<p><strong>Amaliyot 2.</strong> O'qiyotganda ajoyib bir "
                             "<strong>jumla</strong> uchratdingiz. Metodga ko'ra nima qilasiz?</p>",
                "choices": [
                    {"text": "Faqat noma'lum so'zni qog'ozga ko'chirib yodlayman.", "is_correct": False},
                    {"text": "Jumlani yozib qo'yaman va keyin 쓰기 bo'limida ishlataman.", "is_correct": True},
                    {"text": "E'tibor bermay, o'qishda davom etaman.", "is_correct": False},
                    {"text": "Butun paragrafni yod olaman.", "is_correct": False},
                ],
                "explanation": "<p>To'g'ri javob — <strong>jumlani yozib qo'yish</strong>. So'z yoki "
                               "butun paragraf emas, aynan ajoyib jumlalar yig'iladi; ular keyin "
                               "Yozish (쓰기) inshosida tayyor tayanch fikr bo'lib xizmat qiladi.</p>",
            },
        ],
    },
]
