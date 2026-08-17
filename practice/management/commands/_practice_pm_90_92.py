# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-90, PM-91, PM-92 (ish va unumdorlik;
aralashma va foizli masalalar; narx, miqdor, qiymat).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-90 — butun ish = 1, unumdorlik 1/t, birgalikda ishlash.
     ⛔ Hovuzdan suv ketishi YOʻQ;
   • PM-91 — sof modda = massa × foiz; aralashtirish, suyultirish,
     bugʻlatish. ⛔ Uch komponentli qotishma YOʻQ;
   • PM-92 — birlik narx va taqqoslash.
⚠️ Distraktorlar — haqiqiy xatolar: vaqtlarni qoʻshish (6+12=18),
   vaqtlarning oʻrtachasi, unumdorlikni javob deb olish, kasr
   qoʻshishda maxrajni ham qoʻshish, foizlarni qoʻshish (20+45=65),
   foizni oʻnlik kasrga oʻgirmaslik, birlik narx oʻrniga umumiy
   narxni solishtirish, g va kg ni aralashtirish.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_90_92.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Matematika",
    "description": "Matematika — Prime Math darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#f59e0b",
}

DEFAULTS = {
    "level":                "hard",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# PM-90 — ish va unumdorlik
# =====================================================================

Q_PM90 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Usta ishni 8 kunda "
                "bitiradi.</p><p><strong>Bir kunda ishning qanday qismini "
                "bajaradi?</strong></p>",
        "choices": ["1/8 qismini", "1/4 qismini", "8 qismini",
                    "Aniqlab boʻlmaydi"],
        "correct": "1/8 qismini",
        "explanation": "<p><strong>1/8 qismini.</strong> Butun ish 1 deb "
                       "olinadi, unumdorlik esa 1 ÷ 8 = 1/8. Ishning "
                       "haqiqiy hajmini (nechta gʻisht, necha metr) "
                       "bilish shart emas — u javobga taʼsir "
                       "qilmaydi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>Ish "
                "masalalarida butun ish ___ deb olinadi.</strong></p>",
        "choices": ["0", "1", "100", "Ishning haqiqiy hajmi"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Bitta devor, bitta hovuz, "
                       "bitta buyurtma — hammasi 1. Shunda har kimning "
                       "bir kunlik hissasi oddiy kasr bilan "
                       "yoziladi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Ishchining unumdorligi 1/5 ga "
                "teng.</p><p><strong>U ishni necha kunda "
                "bitiradi?</strong></p>",
        "choices": ["1/5 kunda", "1 kunda", "5 kunda", "25 kunda"],
        "correct": "5 kunda",
        "explanation": "<p><strong>5 kunda.</strong> Vaqt — unumdorlikning "
                       "teskarisi: 1 ÷ 1/5 = 5. <strong>1/5 kun</strong> "
                       "— unumdorlikni javob deb olganda chiqadigan eng "
                       "koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>Ikki ishchining har biri ishni "
                "12 kunda bitiradi.</p><p><strong>Birga necha kunda "
                "bitirishadi?</strong></p>",
        "choices": ["6 kunda", "12 kunda", "18 kunda", "24 kunda"],
        "correct": "6 kunda",
        "explanation": "<p><strong>6 kunda.</strong> 1/12 + 1/12 = 2/12 = "
                       "1/6, demak 6 kun. Bir xil tezlikdagi ikki kishi "
                       "ishni roppa-rosa ikki barobar tez bitiradi. "
                       "<strong>24</strong> — vaqtlar qoʻshilganda "
                       "chiqadi va u mantiqan mumkin emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Birga "
                "ishlaganda nima qoʻshiladi?</strong></p>",
        "choices": [
            "Vaqtlar",
            "Unumdorliklar",
            "Vaqtlarning oʻrtachasi olinadi",
            "Hech narsa qoʻshilmaydi",
        ],
        "correct": "Unumdorliklar",
        "explanation": "<p><strong>Unumdorliklar.</strong> Bir kunda kim "
                       "qanchasini bajarsa, oʻshalar qoʻshiladi. "
                       "Vaqtlarni qoʻshish yordamchi kelganda ish "
                       "sekinlashadi degani boʻlardi — bu "
                       "maʼnosiz.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Bir usta ishni 6 kunda, "
                "ikkinchisi 3 kunda bitiradi.</p><p><strong>Birga necha "
                "kunda bitirishadi?</strong></p>",
        "choices": ["2 kunda", "3 kunda", "4,5 kunda", "9 kunda"],
        "correct": "2 kunda",
        "explanation": "<p><strong>2 kunda.</strong> 1/6 + 1/3 = 1/6 + 2/6 "
                       "= 3/6 = 1/2, demak 2 kun. Javob eng tez "
                       "ishlovchining vaqtidan (3 kun) kichik ✓ "
                       "<strong>4,5</strong> — vaqtlarning oʻrtachasi, "
                       "<strong>9</strong> — ularning "
                       "yigʻindisi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikki truba hovuzni alohida-"
                "alohida 5 va 20 soatda toʻldiradi.</p><p><strong>Birga "
                "necha soatda toʻldirishadi?</strong></p>",
        "choices": ["4 soatda", "10 soatda", "12,5 soatda", "25 soatda"],
        "correct": "4 soatda",
        "explanation": "<p><strong>4 soatda.</strong> 1/5 + 1/20 = 4/20 + "
                       "1/20 = 5/20 = 1/4, demak 4 soat. 4 &lt; 5 — eng "
                       "tez trubadan ham kam ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ishchi ishni 20 kunda "
                "bitiradi. U 5 kun ishladi.</p><p><strong>Ishning qanday "
                "qismi qoldi?</strong></p>",
        "choices": ["1/4 qismi", "1/2 qismi", "3/4 qismi", "4/5 qismi"],
        "correct": "3/4 qismi",
        "explanation": "<p><strong>3/4 qismi.</strong> Bajargani "
                       "5 × 1/20 = 1/4. Qolgani 1 − 1/4 = 3/4. "
                       "<strong>1/4</strong> — bajarilgan qism, savol "
                       "esa qolganini soʻragan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir usta ishni 15 kunda "
                "bitiradi. Ikkovi birga 6 kunda bitiradi.</p>"
                "<p><strong>Ikkinchi usta yolgʻiz necha kunda "
                "bitiradi?</strong></p>",
        "choices": ["9 kunda", "10 kunda", "21 kunda", "90 kunda"],
        "correct": "10 kunda",
        "explanation": "<p><strong>10 kunda.</strong> Birgalikdagi "
                       "unumdorlik 1/6. Undan birinchisiniki ayiriladi: "
                       "1/6 − 1/15 = 5/30 − 2/30 = 3/30 = 1/10, demak "
                       "10 kun. Tekshirish: 1/15 + 1/10 = 2/30 + 3/30 = "
                       "1/6 ✓ <strong>9</strong> — 15 − 6 qilinganda "
                       "chiqadi; vaqtlar ayirilmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Uch ishchining har biri ishni "
                "12 kunda bitiradi.</p><p><strong>Uchalasi birga necha "
                "kunda bitirishadi?</strong></p>",
        "choices": ["3 kunda", "4 kunda", "6 kunda", "36 kunda"],
        "correct": "4 kunda",
        "explanation": "<p><strong>4 kunda.</strong> 1/12 × 3 = 3/12 = 1/4, "
                       "demak 4 kun. Uch barobar koʻp kuch — uch barobar "
                       "tez. <strong>36</strong> — vaqtlar "
                       "qoʻshilganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir brigada ishni 4 kunda, "
                "ikkinchisi 6 kunda bajaradi.</p><p><strong>Birga necha "
                "kunda bajarishadi?</strong></p>",
        "choices": ["2 kunda", "2,4 kunda", "5 kunda", "10 kunda"],
        "correct": "2,4 kunda",
        "explanation": "<p><strong>2,4 kunda.</strong> 1/4 + 1/6 = 3/12 + "
                       "2/12 = 5/12. Vaqt — teskarisi: 12/5 = 2,4 kun. "
                       "Javob butun son chiqmasligi mumkin, bu normal. "
                       "2,4 &lt; 4 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ishchi ishni 12 kunda "
                "bitiradi. U 8 kun ishladi, qolgan ishni esa ikkinchi "
                "ishchi 2 kunda tugatdi.</p><p><strong>Ikkinchi ishchi "
                "yolgʻiz necha kunda bitirardi?</strong></p>",
        "choices": ["4 kunda", "6 kunda", "9 kunda", "12 kunda"],
        "correct": "6 kunda",
        "explanation": "<p><strong>6 kunda.</strong> Birinchisi "
                       "8 × 1/12 = 2/3 qismini bajardi, qolgani 1/3. "
                       "Ikkinchisi buni 2 kunda qildi, demak uning "
                       "unumdorligi 1/3 ÷ 2 = 1/6 va yolgʻiz 6 kunda "
                       "bitirardi. Tekshirish: 2 × 1/6 = 1/3 ✓</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki usta ishni 6 va "
                "9 kunda bitiradi.</p><p><strong>Birgalikdagi javob qaysi "
                "oraliqda boʻlishi shart?</strong></p>",
        "choices": [
            "6 kundan kichik",
            "6 va 9 orasida",
            "9 kundan katta",
            "15 kunga teng",
        ],
        "correct": "6 kundan kichik",
        "explanation": "<p><strong>6 kundan kichik.</strong> Yordamchi "
                       "kelganda ish faqat tezlashadi, shuning uchun "
                       "javob eng tez ishlovchining vaqtidan ham kam "
                       "boʻladi. Bu — javobni bir soniyada tekshirish "
                       "usuli (haqiqiy javob 3,6 kun).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Nima uchun "
                "birgalikda ishlashda vaqtlar qoʻshilmaydi?</strong></p>",
        "choices": [
            "Chunki vaqt har xil birlikda oʻlchanadi",
            "Chunki yordamchi kelganda ish tezlashadi, sekinlashmaydi",
            "Chunki vaqt manfiy boʻlishi mumkin emas",
            "Chunki ishchilar teng ishlamaydi",
        ],
        "correct": "Chunki yordamchi kelganda ish tezlashadi, sekinlashmaydi",
        "explanation": "<p><strong>Yordamchi kelganda ish "
                       "tezlashadi.</strong> 6 + 12 = 18 degan javob "
                       "ishning uch barobar sekinlashganini bildiradi — "
                       "maʼnosiz. Qoʻshiladigan narsa bir kunlik "
                       "ulush, ya'ni unumdorlik.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Masalada birgalikdagi "
                "unumdorlik 1/4 deb topildi.</p><p><strong>Javob "
                "nima?</strong></p>",
        "choices": ["1/4 kun", "4 kun", "0,25 kun", "8 kun"],
        "correct": "4 kun",
        "explanation": "<p><strong>4 kun.</strong> 1/4 — bir kunda "
                       "bajariladigan ulush, javob emas. Vaqtni topish "
                       "uchun uni teskari qilish kerak: "
                       "1 ÷ 1/4 = 4.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1/6 + 1/12 = ?</strong></p>",
        "choices": ["1/4", "2/18", "1/9", "2/6"],
        "correct": "1/4",
        "explanation": "<p><strong>1/4.</strong> Umumiy maxraj 12: "
                       "2/12 + 1/12 = 3/12 = 1/4. <strong>2/18</strong> "
                       "— surat va maxraj alohida qoʻshilganda "
                       "chiqadigan klassik xato (PM-17): maxrajlar "
                       "qoʻshilmaydi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>Bir usta ishni "
                "6 kunda, ikkinchisi 12 kunda bitiradi. Birga necha "
                "kunda?</strong></p>",
        "choices": [
            "6 + 12 = 18 kun",
            "(6 + 12) ÷ 2 = 9 kun",
            "1/6 + 1/12 = 1/4 → 4 kun",
            "12 − 6 = 6 kun",
        ],
        "correct": "1/6 + 1/12 = 1/4 → 4 kun",
        "explanation": "<p><strong>1/6 + 1/12 = 1/4 → 4 kun.</strong> "
                       "Unumdorliklar qoʻshiladi, keyin natija teskari "
                       "qilinadi. Birinchi ikki variant 6 dan katta "
                       "javob beradi — ular allaqachon mantiqan "
                       "notoʻgʻri.</p>",
    },
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Oʻquvchi yozdi: "
                "«1/8 + 1/24 = 2/32 = 1/16, demak 16 kun».</p>"
                "<p><strong>Xato qaysi qadamda?</strong></p>",
        "choices": [
            "Unumdorliklarni qoʻshgani notoʻgʻri",
            "Kasrlarni qoʻshishda maxrajlar ham qoʻshilgan",
            "Oxirida teskari qilish unutilgan",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Kasrlarni qoʻshishda maxrajlar ham qoʻshilgan",
        "explanation": "<p><strong>Maxrajlar ham qoʻshilgan.</strong> "
                       "Toʻgʻrisi: umumiy maxraj 24, ya'ni "
                       "3/24 + 1/24 = 4/24 = 1/6 → 6 kun. "
                       "Unumdorliklarni qoʻshish gʻoyasi toʻgʻri edi, "
                       "faqat kasr amali buzilgan (PM-17).</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Bir brigada uyni 10 kunda "
                "boʻyaydi, ikkinchisi xuddi shu uyni 40 kunda "
                "boʻyaydi.</p><p><strong>Birga necha kunda "
                "boʻyashadi?</strong></p>",
        "choices": ["8 kunda", "20 kunda", "25 kunda", "50 kunda"],
        "correct": "8 kunda",
        "explanation": "<p><strong>8 kunda.</strong> 1/10 + 1/40 = 4/40 + "
                       "1/40 = 5/40 = 1/8, demak 8 kun. Ikkinchi brigada "
                       "juda sekin, shuning uchun tejash kichik — atigi "
                       "2 kun. 8 &lt; 10 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir usta ishni 8 kunda "
                "bitiradi. U 2 kun yolgʻiz ishladi, keyin yana bir usta "
                "qoʻshildi — u ham ishni yolgʻiz 8 kunda bitiradi. Ish "
                "oxirigacha birga davom etdi.</p><p><strong>Ish jami "
                "necha kunda tugadi?</strong></p>",
        "choices": ["4 kunda", "5 kunda", "6 kunda", "7 kunda"],
        "correct": "5 kunda",
        "explanation": "<p><strong>5 kunda.</strong> Birinchi bosqichda "
                       "2 × 1/8 = 1/4 bajarildi, qolgani 3/4. "
                       "Birgalikdagi unumdorlik 1/8 + 1/8 = 1/4, demak "
                       "qolgan 3/4 uchun 3/4 ÷ 1/4 = 3 kun kerak. Jami "
                       "2 + 3 = 5 kun. Tekshirish: birinchisi 5 kun "
                       "(5/8), ikkinchisi 3 kun (3/8); "
                       "5/8 + 3/8 = 1 ✓</p>",
    },
]


# =====================================================================
# PM-91 — aralashma va foizli masalalar
# =====================================================================

Q_PM91 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>300 g eritmada 20% tuz bor.</p>"
                "<p><strong>Sof tuz necha gramm?</strong></p>",
        "choices": ["15 g", "20 g", "60 g", "6000 g"],
        "correct": "60 g",
        "explanation": "<p><strong>60 g.</strong> 300 × 0,2 = 60 g. "
                       "<strong>6000</strong> — foizni oʻnlik kasrga "
                       "oʻgirmay 300 × 20 qilinganda chiqadi; sof modda "
                       "eritmadan ogʻir boʻlishi mumkin emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>400 g eritmada 50 g tuz bor.</p>"
                "<p><strong>Eritma necha foizli?</strong></p>",
        "choices": ["8%", "12,5%", "20%", "50%"],
        "correct": "12,5%",
        "explanation": "<p><strong>12,5%.</strong> 50 ÷ 400 = 0,125 = "
                       "12,5%. Foiz har doim <strong>butun</strong> "
                       "massadan olinadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Ikki eritma "
                "aralashtirilganda nima qoʻshiladi?</strong></p>",
        "choices": [
            "Foizlar",
            "Sof modda va massa",
            "Faqat foizlarning oʻrtachasi olinadi",
            "Faqat massa",
        ],
        "correct": "Sof modda va massa",
        "explanation": "<p><strong>Sof modda va massa.</strong> Ikkalasi "
                       "ham oddiy ogʻirlik — ularni qoʻshsa boʻladi. "
                       "Foiz esa nisbat, uni qoʻshib boʻlmaydi; yangi "
                       "foiz oxirida hisoblanadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Eritmaga toza suv "
                "qoʻshildi.</p><p><strong>Sof modda bilan nima "
                "boʻladi?</strong></p>",
        "choices": [
            "Ortadi",
            "Kamayadi",
            "Oʻzgarmaydi",
            "Ikki barobar boʻladi",
        ],
        "correct": "Oʻzgarmaydi",
        "explanation": "<p><strong>Oʻzgarmaydi.</strong> Suvda tuz yoʻq — "
                       "uning foizi 0. Faqat umumiy massa ortadi, "
                       "shuning uchun foiz tushadi. Bu — "
                       "suyultirish.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>200 g 30% li eritmada sof "
                "modda necha gramm?</strong></p>",
        "choices": ["30 g", "60 g", "70 g", "600 g"],
        "correct": "60 g",
        "explanation": "<p><strong>60 g.</strong> 200 × 0,3 = 60 g. "
                       "Qolgan 140 g — suv.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>100 g 10% li eritmaga 100 g "
                "30% li eritma qoʻshildi.</p><p><strong>Yangi eritma necha "
                "foizli?</strong></p>",
        "choices": ["15%", "20%", "40%", "45%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Sof modda: 10 + 30 = 40 g. "
                       "Massa: 200 g. 40 ÷ 200 = 0,2 = 20%. Bu safar "
                       "massalar teng, shuning uchun javob roppa-rosa "
                       "oʻrtachaga tushdi. <strong>40%</strong> — "
                       "foizlar qoʻshilganda.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>200 g 15% li eritmaga 300 g "
                "25% li eritma qoʻshildi.</p><p><strong>Yangi eritma necha "
                "foizli?</strong></p>",
        "choices": ["18%", "20%", "21%", "40%"],
        "correct": "21%",
        "explanation": "<p><strong>21%.</strong> Sof modda: 30 + 75 = "
                       "105 g. Massa: 500 g. 105 ÷ 500 = 0,21 = 21%. "
                       "<strong>20%</strong> — oddiy oʻrtacha; u bu "
                       "yerda notoʻgʻri, chunki massalar teng emas va "
                       "javob koʻproq eritma (25%) tomoniga "
                       "tortiladi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>500 g 20% li eritmaga 500 g "
                "toza suv qoʻshildi.</p><p><strong>Yangi eritma necha "
                "foizli?</strong></p>",
        "choices": ["5%", "10%", "15%", "20%"],
        "correct": "10%",
        "explanation": "<p><strong>10%.</strong> Sof modda "
                       "500 × 0,2 = 100 g va u oʻzgarmaydi. Yangi massa "
                       "1000 g. 100 ÷ 1000 = 0,1 = 10%. Massa ikki "
                       "barobar ortdi — foiz ikki barobar tushdi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>400 g 10% li eritmadan 200 g "
                "suv bugʻlatildi.</p><p><strong>Yangi eritma necha "
                "foizli?</strong></p>",
        "choices": ["5%", "10%", "20%", "40%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Sof modda "
                       "400 × 0,1 = 40 g, oʻzgarmaydi. Yangi massa "
                       "400 − 200 = 200 g. 40 ÷ 200 = 0,2 = 20%. Suv "
                       "uchdi, tuz qoldi — foiz ortdi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>600 g 20% li eritmaga necha "
                "gramm suv qoʻshilsa, 15% li boʻladi?</p><p><strong>Javobni "
                "tanlang.</strong></p>",
        "choices": ["120 g", "150 g", "200 g", "800 g"],
        "correct": "200 g",
        "explanation": "<p><strong>200 g.</strong> Sof modda "
                       "600 × 0,2 = 120 g va oʻzgarmaydi. 15% boʻlishi "
                       "uchun kerakli massa: 120 ÷ 0,15 = 800 g. Demak "
                       "qoʻshiladigan suv 800 − 600 = 200 g. "
                       "<strong>800</strong> — kerakli umumiy massa, "
                       "qoʻshiladigan suv emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>300 g 40% li eritmaga 100 g "
                "suv qoʻshildi.</p><p><strong>Yangi eritma necha "
                "foizli?</strong></p>",
        "choices": ["10%", "20%", "30%", "35%"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> Sof modda "
                       "300 × 0,4 = 120 g. Yangi massa 400 g. "
                       "120 ÷ 400 = 0,3 = 30%.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>200 g 5% li eritmaga 25% li "
                "eritmadan qoʻshib, 15% li eritma olindi.</p>"
                "<p><strong>25% li eritmadan necha gramm "
                "qoʻshilgan?</strong></p>",
        "choices": ["100 g", "150 g", "200 g", "400 g"],
        "correct": "200 g",
        "explanation": "<p><strong>200 g.</strong> 10 + 0,25x = "
                       "0,15(200 + x) → 10 + 0,25x = 30 + 0,15x → "
                       "0,1x = 20 → x = 200. Tekshirish: sof modda "
                       "10 + 50 = 60 g, massa 400 g, "
                       "60 ÷ 400 = 0,15 ✓ 15% roppa-rosa 5 va 25 ning "
                       "oʻrtasida, shuning uchun massalar ham teng "
                       "chiqdi.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>10% li va 30% li "
                "eritmalar aralashtirildi.</p><p><strong>Natija qaysi "
                "oraliqda boʻlishi shart?</strong></p>",
        "choices": [
            "10% dan kichik",
            "10% va 30% orasida",
            "Roppa-rosa 20%",
            "30% dan katta",
        ],
        "correct": "10% va 30% orasida",
        "explanation": "<p><strong>10% va 30% orasida.</strong> Aralashma "
                       "hech qachon eng kuchlisidan kuchli yoki eng "
                       "kuchsizidan kuchsiz boʻlmaydi. "
                       "<strong>Roppa-rosa 20%</strong> faqat massalar "
                       "teng boʻlgandagina toʻgʻri boʻladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qachon ikki "
                "foizning oddiy oʻrtachasi toʻgʻri javob "
                "beradi?</strong></p>",
        "choices": [
            "Massalar teng boʻlganda",
            "Foizlar teng boʻlganda",
            "Har doim",
            "Hech qachon",
        ],
        "correct": "Massalar teng boʻlganda",
        "explanation": "<p><strong>Massalar teng boʻlganda.</strong> Shunda "
                       "ikkala eritma natijaga bir xil «ogʻirlik» bilan "
                       "taʼsir qiladi. Massalar har xil boʻlsa, javob "
                       "koʻproq eritma tomoniga tortiladi — xuddi "
                       "PM-88 dagi oʻrtacha tezlik kabi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Toza suvni "
                "jadvalga qanday yozish kerak?</strong></p>",
        "choices": [
            "0% li eritma sifatida",
            "100% li eritma sifatida",
            "50% li eritma sifatida",
            "Suvni jadvalga yozib boʻlmaydi",
        ],
        "correct": "0% li eritma sifatida",
        "explanation": "<p><strong>0% li eritma sifatida.</strong> Suvda "
                       "sof modda yoʻq. Uni 0% qatori qilib yozsangiz, "
                       "suyultirish masalasi oddiy aralashtirish "
                       "masalasi bilan bir xil yoʻldan yechiladi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Eritmadan bir qism suv "
                "bugʻlatildi.</p><p><strong>Foiz bilan nima "
                "boʻladi?</strong></p>",
        "choices": ["Ortadi", "Kamayadi", "Oʻzgarmaydi", "Nolga aylanadi"],
        "correct": "Ortadi",
        "explanation": "<p><strong>Ortadi.</strong> Sof modda oʻsha-oʻsha "
                       "qoladi, umumiy massa esa kamayadi. Kasrning "
                       "maxraji kichrayganda qiymati ortadi — eritma "
                       "quyuqlashadi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>300 g 20% li va "
                "200 g 45% li eritmalar aralashtirildi. Natija necha "
                "foizli?</strong></p>",
        "choices": [
            "20 + 45 = 65%",
            "(20 + 45) ÷ 2 = 32,5%",
            "(60 + 90) ÷ 500 = 30%",
            "(300 + 200) ÷ 45 ≈ 11%",
        ],
        "correct": "(60 + 90) ÷ 500 = 30%",
        "explanation": "<p><strong>(60 + 90) ÷ 500 = 30%.</strong> Avval "
                       "sof modda: 300 × 0,2 = 60 va 200 × 0,45 = 90. "
                       "Keyin yigʻindini yangi massaga boʻlamiz. "
                       "<strong>65%</strong> — foizlar qoʻshilgan; "
                       "<strong>32,5%</strong> — oʻrtacha olingan, lekin "
                       "massalar teng emas.</p>",
    },
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Oʻquvchi yozdi: «200 g "
                "eritmaning 10% i = 200 × 10 = 2000 g tuz».</p>"
                "<p><strong>Nima notoʻgʻri?</strong></p>",
        "choices": [
            "Foiz oʻnlik kasrga oʻgirilmagan",
            "Koʻpaytirish oʻrniga boʻlish kerak edi",
            "Massa notoʻgʻri olingan",
            "Xato yoʻq, javob toʻgʻri",
        ],
        "correct": "Foiz oʻnlik kasrga oʻgirilmagan",
        "explanation": "<p><strong>Foiz oʻnlik kasrga oʻgirilmagan.</strong> "
                       "10% = 0,1, demak 200 × 0,1 = 20 g. Javobning "
                       "mantiqsizligi darrov koʻrinib turibdi: sof tuz "
                       "(2000 g) eritmaning oʻzidan (200 g) ogʻir "
                       "chiqdi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Oshxonada 800 g sharbat bor, "
                "uning 25% i shakar. Sharbatga 200 g suv "
                "qoʻshildi.</p><p><strong>Yangi sharbatda necha foiz "
                "shakar bor?</strong></p>",
        "choices": ["15%", "20%", "22%", "25%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Sof shakar "
                       "800 × 0,25 = 200 g va suv qoʻshilganda "
                       "oʻzgarmaydi. Yangi massa 800 + 200 = 1000 g. "
                       "200 ÷ 1000 = 0,2 = 20%. Suv shakar qoʻshmaydi — "
                       "u faqat maxrajni kattalashtiradi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ustaxonada 400 g qotishma bor, "
                "uning 30% i mis. Unga 70% mis boʻlgan qotishmadan "
                "qoʻshib, 50% li qotishma olmoqchi.</p><p><strong>70% li "
                "qotishmadan necha gramm qoʻshish kerak?</strong></p>",
        "choices": ["200 g", "300 g", "400 g", "800 g"],
        "correct": "400 g",
        "explanation": "<p><strong>400 g.</strong> 120 + 0,7x = "
                       "0,5(400 + x) → 120 + 0,7x = 200 + 0,5x → "
                       "0,2x = 80 → x = 400. Tekshirish: sof mis "
                       "120 + 280 = 400 g, massa 800 g, "
                       "400 ÷ 800 = 0,5 ✓ 50% roppa-rosa 30 va 70 ning "
                       "oʻrtasida, shuning uchun massalar teng "
                       "chiqdi.</p>",
    },
]


# =====================================================================
# PM-92 — narx, miqdor, qiymat
# =====================================================================

Q_PM92 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>Kilosi 9 000 soʻmdan 5 kg "
                "shakar necha soʻm turadi?</strong></p>",
        "choices": ["1 800 soʻm", "14 000 soʻm", "45 000 soʻm",
                    "90 000 soʻm"],
        "correct": "45 000 soʻm",
        "explanation": "<p><strong>45 000 soʻm.</strong> qiymat = narx × "
                       "miqdor = 9 000 × 5. <strong>14 000</strong> — "
                       "narx bilan miqdor qoʻshib yuborilganda "
                       "chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>4 kg kartoshka 52 000 soʻm "
                "turdi.</p><p><strong>Bir kilosi necha soʻm?</strong></p>",
        "choices": ["11 000 soʻm", "13 000 soʻm", "48 000 soʻm",
                    "208 000 soʻm"],
        "correct": "13 000 soʻm",
        "explanation": "<p><strong>13 000 soʻm.</strong> narx = qiymat ÷ "
                       "miqdor = 52 000 ÷ 4. <strong>208 000</strong> — "
                       "boʻlish oʻrniga koʻpaytirilganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>84 000 soʻmga kilosi "
                "14 000 soʻmdan necha kg goʻsht olish mumkin?</strong></p>",
        "choices": ["6 kg", "7 kg", "70 kg", "98 kg"],
        "correct": "6 kg",
        "explanation": "<p><strong>6 kg.</strong> miqdor = qiymat ÷ narx = "
                       "84 000 ÷ 14 000 = 6.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Birlik narx "
                "nima uchun kerak?</strong></p>",
        "choices": [
            "Umumiy summani tez hisoblash uchun",
            "Har xil miqdordagi paketlarni solishtirish uchun",
            "Chegirmani hisoblash uchun",
            "Qoldiq pulni topish uchun",
        ],
        "correct": "Har xil miqdordagi paketlarni solishtirish uchun",
        "explanation": "<p><strong>Har xil miqdordagi paketlarni "
                       "solishtirish uchun.</strong> 400 g bilan 1 kg ni "
                       "umumiy narx boʻyicha taqqoslab boʻlmaydi. "
                       "Ikkalasini bir kilogrammga keltirgandan keyin "
                       "esa oddiy son bilan solishtiriladi.</p>",
    },
    {
        "text": "<p>Boʻsh joyga nima tushadi?</p><p><strong>600 g — bu "
                "___ kg.</strong></p>",
        "choices": ["0,06", "0,6", "6", "60"],
        "correct": "0,6",
        "explanation": "<p><strong>0,6.</strong> 600 ÷ 1000 = 0,6 kg. "
                       "Birlik narxni hisoblashdan oldin bu almashtirish "
                       "shart — aks holda javob grammga chiqadi va uni "
                       "kilogrammlik narx bilan solishtirib "
                       "boʻlmaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>250 g choy 5 000 soʻm turadi.</p>"
                "<p><strong>Bir kilogrammi necha soʻm?</strong></p>",
        "choices": ["1 250 soʻm", "12 500 soʻm", "20 000 soʻm",
                    "25 000 soʻm"],
        "correct": "20 000 soʻm",
        "explanation": "<p><strong>20 000 soʻm.</strong> 250 g = 0,25 kg, "
                       "demak 5 000 ÷ 0,25 = 20 000 soʻm/kg. "
                       "<strong>1 250</strong> — 5 000 ni 4 ga "
                       "boʻlish oʻrniga 4 ga koʻpaytirmay, teskari amal "
                       "qilinganda chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>1,2 kg guruch 30 000 soʻm turdi.</p>"
                "<p><strong>Bir kilogrammi necha soʻm?</strong></p>",
        "choices": ["25 000 soʻm", "28 000 soʻm", "30 000 soʻm",
                    "36 000 soʻm"],
        "correct": "25 000 soʻm",
        "explanation": "<p><strong>25 000 soʻm.</strong> 30 000 ÷ 1,2 = "
                       "25 000. Tekshirish: 25 000 × 1,2 = 30 000 ✓ "
                       "<strong>36 000</strong> — boʻlish oʻrniga "
                       "koʻpaytirilganda chiqadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Un: 500 g li paket "
                "11 000 soʻm, 2 kg li paket 46 000 soʻm.</p>"
                "<p><strong>Qaysi biri arzon?</strong></p>",
        "choices": [
            "500 g li — kilosi 22 000 soʻm",
            "2 kg li — kilosi 23 000 soʻm",
            "500 g li — kilosi 11 000 soʻm",
            "Ikkalasi bir xil",
        ],
        "correct": "500 g li — kilosi 22 000 soʻm",
        "explanation": "<p><strong>500 g li.</strong> 11 000 ÷ 0,5 = "
                       "22 000 soʻm/kg; 46 000 ÷ 2 = 23 000 soʻm/kg. "
                       "Kichik paket kilosiga 1 000 soʻm arzon — «katta "
                       "paket har doim tejamkor» degan fikr yana "
                       "ishlamadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p>2 litr sut 24 000 soʻm turadi.</p>"
                "<p><strong>Bir litri necha soʻm?</strong></p>",
        "choices": ["6 000 soʻm", "12 000 soʻm", "22 000 soʻm",
                    "48 000 soʻm"],
        "correct": "12 000 soʻm",
        "explanation": "<p><strong>12 000 soʻm.</strong> 24 000 ÷ 2 = "
                       "12 000 soʻm/litr.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Kilosi 10 000 soʻmdan 3 kg "
                "olma va kilosi 15 000 soʻmdan 2 kg nok olindi.</p>"
                "<p><strong>Jami qancha toʻlanadi?</strong></p>",
        "choices": ["25 000 soʻm", "50 000 soʻm", "60 000 soʻm",
                    "75 000 soʻm"],
        "correct": "60 000 soʻm",
        "explanation": "<p><strong>60 000 soʻm.</strong> Olma "
                       "10 000 × 3 = 30 000; nok 15 000 × 2 = 30 000; "
                       "jami 60 000. <strong>25 000</strong> — narxlar "
                       "qoʻshilganda chiqadi, lekin narxlar "
                       "qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sherbekda 200 000 soʻm bor. U "
                "kilosi 45 000 soʻmdan 3 kg goʻsht oldi.</p>"
                "<p><strong>Qancha pul qoldi?</strong></p>",
        "choices": ["55 000 soʻm", "65 000 soʻm", "135 000 soʻm",
                    "155 000 soʻm"],
        "correct": "65 000 soʻm",
        "explanation": "<p><strong>65 000 soʻm.</strong> Goʻsht "
                       "45 000 × 3 = 135 000 soʻm. Qoldi: "
                       "200 000 − 135 000 = 65 000. "
                       "<strong>135 000</strong> — sarflangan pul, savol "
                       "esa qolganini soʻragan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>40 000 soʻmlik mahsulotga 25% "
                "chegirma eʼlon qilindi.</p><p><strong>Yangi narx necha "
                "soʻm?</strong></p>",
        "choices": ["10 000 soʻm", "15 000 soʻm", "30 000 soʻm",
                    "50 000 soʻm"],
        "correct": "30 000 soʻm",
        "explanation": "<p><strong>30 000 soʻm.</strong> Chegirma "
                       "40 000 × 0,25 = 10 000 soʻm, yangi narx "
                       "40 000 − 10 000 = 30 000 (PM-26). "
                       "<strong>10 000</strong> — chegirmaning oʻzi, "
                       "yangi narx emas.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Birlik narx "
                "qaysi amal bilan topiladi?</strong></p>",
        "choices": [
            "qiymat × miqdor",
            "qiymat ÷ miqdor",
            "miqdor ÷ qiymat",
            "qiymat − miqdor",
        ],
        "correct": "qiymat ÷ miqdor",
        "explanation": "<p><strong>qiymat ÷ miqdor.</strong> Bu — S = v × t "
                       "dagi v = S ÷ t va ish = u × t dagi u = ish ÷ t "
                       "bilan bir xil amal. Uchala darsda ham oʻrtadagi "
                       "kattalik «bitta birlikka toʻgʻri keladigan "
                       "miqdor» degani.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>«Katta paket "
                "har doim arzonroq» degan fikr toʻgʻrimi?</strong></p>",
        "choices": [
            "Ha, har doim toʻgʻri",
            "Yoʻq — har safar birlik narxni hisoblash kerak",
            "Faqat oziq-ovqat uchun toʻgʻri",
            "Faqat chegirma boʻlmaganda toʻgʻri",
        ],
        "correct": "Yoʻq — har safar birlik narxni hisoblash kerak",
        "explanation": "<p><strong>Yoʻq.</strong> Bu qoida emas, taxmin. "
                       "Koʻpincha rost, lekin har doim emas — baʼzan "
                       "katta paket kilogrammiga qimmatroq chiqadi. "
                       "Bitta boʻlish daʼvoni tekshiradi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Bir necha xil mahsulot "
                "olindi.</p><p><strong>Jadvalda nima "
                "qoʻshiladi?</strong></p>",
        "choices": [
            "Narxlar",
            "Qiymatlar",
            "Miqdorlar va narxlar",
            "Birlik narxlarning oʻrtachasi olinadi",
        ],
        "correct": "Qiymatlar",
        "explanation": "<p><strong>Qiymatlar.</strong> Har bir mahsulot "
                       "uchun toʻlangan pul qoʻshiladi. Narxlarni "
                       "qoʻshish — PM-88 dagi «tezliklarni qoʻshish» "
                       "xatosining oʻzi: hosil boʻlgan son hech "
                       "narsani anglatmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Oʻquvchi 900 g li "
                "paketni 900 ga boʻldi, 1,5 kg li paketni esa 1,5 ga.</p>"
                "<p><strong>Natijalar bilan nima "
                "qilib boʻlmaydi?</strong></p>",
        "choices": [
            "Ularni solishtirib boʻlmaydi — birliklari har xil",
            "Ularni qoʻshib boʻlmaydi, lekin solishtirsa boʻladi",
            "Hech qanday muammo yoʻq",
            "Ikkalasini ham 1000 ga koʻpaytirish kerak",
        ],
        "correct": "Ularni solishtirib boʻlmaydi — birliklari har xil",
        "explanation": "<p><strong>Solishtirib boʻlmaydi.</strong> Birinchi "
                       "natija bir <strong>gramm</strong>ning narxi, "
                       "ikkinchisi bir <strong>kilogramm</strong>niki. "
                       "Avval 900 g ni 0,9 kg ga oʻgirish kerak edi — "
                       "PM-88 dagi minut va soat xatosining "
                       "oʻzi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato qilingan?</p><p>Oʻquvchi yozdi: «Kichik "
                "paket 21 000 soʻm, katta paket 111 000 soʻm. Demak "
                "kichik paket arzon».</p><p><strong>Nima "
                "notoʻgʻri?</strong></p>",
        "choices": [
            "Miqdorlar hisobga olinmagan",
            "Narxlar notoʻgʻri oʻqilgan",
            "Chegirma hisobga olinmagan",
            "Xato yoʻq, xulosa toʻgʻri",
        ],
        "correct": "Miqdorlar hisobga olinmagan",
        "explanation": "<p><strong>Miqdorlar hisobga olinmagan.</strong> "
                       "Katta paketda koʻproq mahsulot bor. Solishtirish "
                       "uchun birlik narx kerak: 21 000 ÷ 0,6 = "
                       "35 000 va 111 000 ÷ 3 = 37 000 soʻm/kg. Xulosa "
                       "tasodifan toʻgʻri chiqdi, lekin yoʻl "
                       "notoʻgʻri — boshqa sonlarda javob ham xato "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Qaysi yechim toʻgʻri?</p><p><strong>900 g li paket "
                "27 000 soʻm. Bir kilogrammi necha soʻm?</strong></p>",
        "choices": [
            "27 000 ÷ 900 = 30 soʻm",
            "27 000 ÷ 0,9 = 30 000 soʻm",
            "27 000 × 0,9 = 24 300 soʻm",
            "27 000 × 900 = 24 300 000 soʻm",
        ],
        "correct": "27 000 ÷ 0,9 = 30 000 soʻm",
        "explanation": "<p><strong>27 000 ÷ 0,9 = 30 000 soʻm.</strong> "
                       "Avval 900 g ni 0,9 kg ga oʻgiramiz, keyin "
                       "boʻlamiz. <strong>27 000 ÷ 900 = 30</strong> "
                       "ham hisob sifatida toʻgʻri, lekin u bir "
                       "grammning narxi — kilogrammlik narxlar bilan "
                       "solishtirib boʻlmaydi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Bekzod bozorga 120 000 soʻm "
                "bilan bordi. Kilosi 14 000 soʻmdan 2 kg guruch va kilosi "
                "7 000 soʻmdan 4 kg kartoshka oldi. Qolgan pulga kilosi "
                "16 000 soʻmdan olma olmoqchi.</p><p><strong>Necha kg olma "
                "olishi mumkin?</strong></p>",
        "choices": ["2 kg", "3 kg", "4 kg", "5 kg"],
        "correct": "4 kg",
        "explanation": "<p><strong>4 kg.</strong> Guruch "
                       "14 000 × 2 = 28 000; kartoshka "
                       "7 000 × 4 = 28 000; sarflandi 56 000 soʻm. "
                       "Qoldi: 120 000 − 56 000 = 64 000. Olma: "
                       "64 000 ÷ 16 000 = 4 kg. Tekshirish: "
                       "28 000 + 28 000 + 64 000 = 120 000 ✓</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir doʻkonda 1,5 kg yuvish "
                "kukuni 36 000 soʻm, boshqasida 800 g li paketi "
                "20 000 soʻm.</p><p><strong>Qaysi doʻkon arzon va "
                "kilogrammiga qancha farq bor?</strong></p>",
        "choices": [
            "Birinchisi, 500 soʻm farq",
            "Birinchisi, 1 000 soʻm farq",
            "Ikkinchisi, 1 000 soʻm farq",
            "Ikkinchisi, 16 000 soʻm farq",
        ],
        "correct": "Birinchisi, 1 000 soʻm farq",
        "explanation": "<p><strong>Birinchisi, 1 000 soʻm farq.</strong> "
                       "Birinchi doʻkon: 36 000 ÷ 1,5 = 24 000 soʻm/kg. "
                       "Ikkinchisi: 800 g = 0,8 kg, "
                       "20 000 ÷ 0,8 = 25 000 soʻm/kg. Farq "
                       "25 000 − 24 000 = 1 000 soʻm. Umumiy narxga "
                       "qarasak (36 000 va 20 000) notoʻgʻri xulosa "
                       "chiqarardik.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-90 Mashq: Ish va unumdorlik",
        "tutorial":    "PM-90:",
        "description": (
            "Butun ish = 1, unumdorlik 1/t, birgalikda ishlash va "
            "bosqichli ish. 20 savol."
        ),
        "questions":   Q_PM90,
        **DEFAULTS,
    },
    {
        "title":       "PM-91 Mashq: Aralashma va foizli masalalar",
        "tutorial":    "PM-91:",
        "description": (
            "Sof modda, ikki eritmani aralashtirish, suyultirish va "
            "bugʻlatish. 20 savol."
        ),
        "questions":   Q_PM91,
        **DEFAULTS,
    },
    {
        "title":       "PM-92 Mashq: Narx, miqdor, qiymat",
        "tutorial":    "PM-92:",
        "description": (
            "Savdo uchligi, birlik narx bilan taqqoslash va koʻp "
            "mahsulotli xarid jadvali. 20 savol."
        ),
        "questions":   Q_PM92,
        **DEFAULTS,
    },
]
