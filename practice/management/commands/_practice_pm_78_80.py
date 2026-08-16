# -*- coding: utf-8 -*-
"""Prime Math mashqlar — PM-78, PM-79, PM-80 (oʻrta arifmetik, mediana va
moda, tarqoqlik).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PM_PRACTICE.md · lesson list in toc_pm_practices.txt
Ramp: 1–5 tanish · 6–12 qoʻllash · 13–16 farqlash · 17–18 xato topish ·
      19–20 matnli masala (har doim ikkita).

Level: uchalasi ham `hard`.

⚠️ `choices` EKRANLANADI — HTML teg yoʻq.
⚠️ Kumulyativ:
   • PM-78 — faqat oʻrta arifmetik. ⛔ MEDIANA va MODA soʻzlari YOʻQ;
   • PM-79 — mediana, moda va uchalasini taqqoslash;
   • PM-80 — tarqoqlik; oʻrtacha va mediana bemalol ishlatiladi.
   ⛔ Aldamchi diagramma (PM-81) va ehtimollik (PM-83/84) yoʻq.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pm_78_80.py --master=prime \\
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
# PM-78 — oʻrta arifmetik
# =====================================================================

Q_PM78 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>4, 6 va 8 sonlarining oʻrta "
                "arifmetigi qancha?</strong></p>",
        "choices": ["4", "6", "9", "18"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 4 + 6 + 8 = 18, va "
                       "18 ÷ 3 = 6. <strong>18</strong> — boʻlish qadami "
                       "tushib qolgan; oʻrtacha eng katta sondan katta "
                       "boʻlolmaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2, 4, 6 va 8 sonlarining "
                "oʻrtachasi qancha?</strong></p>",
        "choices": ["4", "5", "6", "20"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 2 + 4 + 6 + 8 = 20, va "
                       "20 ÷ 4 = 5. Diqqat: bu yerda toʻrtta son bor, "
                       "shuning uchun 4 ga boʻlinadi — 3 ga emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p><strong>Uchta sonning oʻrtachasi "
                "7. Ularning yigʻindisi qancha?</strong></p>",
        "choices": ["3", "7", "10", "21"],
        "correct": "21",
        "explanation": "<p><strong>21.</strong> Yigʻindi = oʻrtacha × sonlar "
                       "soni = 7 × 3 = 21. Teskari masalada "
                       "<em>koʻpaytiriladi</em>; boʻlish teskari yoʻnalish "
                       "boʻlardi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Oʻrta arifmetik "
                "qanday topiladi?</strong></p>",
        "choices": [
            "Yigʻindini sonlar soniga boʻlib",
            "Eng katta va eng kichikni qoʻshib",
            "Oʻrtadagi sonni olib",
            "Eng koʻp uchraganini olib",
        ],
        "correct": "Yigʻindini sonlar soniga boʻlib",
        "explanation": "<p><strong>Yigʻindini sonlar soniga boʻlib.</strong> "
                       "Maʼnosi: agar hammasi baravar taqsimlanganda har "
                       "biriga qancha tushardi. Boshqa variantlar boshqa "
                       "kattaliklarni tasvirlaydi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10, 20, 30, 40 va 50 "
                "sonlarining oʻrtachasi qancha?</strong></p>",
        "choices": ["25", "30", "35", "150"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> Yigʻindi 150, va "
                       "150 ÷ 5 = 30. Sonlar bir tekis joylashganda oʻrtacha "
                       "aynan oʻrtadagi songa toʻgʻri keladi — lekin buni "
                       "faqat hisob tasdiqlaydi.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p><strong>Beshta sonning oʻrtachasi "
                "12. Ularning yigʻindisi qancha?</strong></p>",
        "choices": ["2,4", "17", "60", "72"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> Yigʻindi = 12 × 5 = 60. "
                       "<strong>2,4</strong> — koʻpaytirish oʻrniga "
                       "boʻlingan (12 ÷ 5). <strong>17</strong> — "
                       "qoʻshilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Toʻrtta sonning oʻrtachasi 9. "
                "Ulardan uchtasi 7, 8 va 12.</p><p><strong>Toʻrtinchisi "
                "qancha?</strong></p>",
        "choices": ["6", "9", "12", "27"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Butun yigʻindi: 9 × 4 = 36. "
                       "Maʼlum uchtasi: 7 + 8 + 12 = 27. Toʻrtinchisi: "
                       "36 − 27 = 9. <strong>27</strong> — uchtasining "
                       "yigʻindisi, javob emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>6, 7, 8, 9 va 10 sonlarining "
                "oʻrtachasi qancha?</strong></p>",
        "choices": ["7", "7,5", "8", "40"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Yigʻindi 40, va 40 ÷ 5 = 8. "
                       "<strong>7,5</strong> — oxirgi son (10) tashlab "
                       "yuborilganda chiqadi: (6 + 7 + 8 + 9) ÷ 4 = 7,5. "
                       "Sonlarni sanashni har doim ikki marta "
                       "tekshiring.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Sherbek uch kun kitob oʻqidi: "
                "12, 15 va 18 sahifa.</p><p><strong>Kuniga oʻrtacha necha "
                "sahifa oʻqidi?</strong></p>",
        "choices": ["12", "15", "18", "45"],
        "correct": "15",
        "explanation": "<p><strong>15 sahifa.</strong> 12 + 15 + 18 = 45, va "
                       "45 ÷ 3 = 15. <strong>45</strong> — uch kunlik "
                       "jami, bir kunlik emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>Baholar: 5, 5, 4, 3 va 3. "
                "Oʻrtacha baho qancha?</strong></p>",
        "choices": ["3", "4", "4,5", "20"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 5 + 5 + 4 + 3 + 3 = 20, va "
                       "20 ÷ 5 = 4. Oʻrtacha eng kichik (3) va eng katta (5) "
                       "orasida chiqdi — javobni shu bilan tekshiring.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Ikkita sonning oʻrtachasi 10, "
                "ulardan biri 6.</p><p><strong>Ikkinchisi qancha?</strong></p>",
        "choices": ["4", "8", "14", "16"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Yigʻindi: 10 × 2 = 20. "
                       "Ikkinchisi: 20 − 6 = 14. Tekshirish: "
                       "(6 + 14) ÷ 2 = 10 ✓ <strong>16</strong> — "
                       "oʻrtachaga 6 qoʻshilgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Dilnoza bir hafta davomida kuniga "
                "oʻrtacha 40 daqiqa sport bilan shugʻullandi.</p><p><strong>Bir "
                "haftada jami qancha vaqt sarfladi?</strong></p>",
        "choices": ["4 soat", "4 soat 40 daqiqa", "5 soat", "280 soat"],
        "correct": "4 soat 40 daqiqa",
        "explanation": "<p><strong>4 soat 40 daqiqa.</strong> Jami: "
                       "40 × 7 = 280 daqiqa. Soatga oʻgiramiz: "
                       "280 ÷ 60 = 4 soat va 40 daqiqa qoldiq. "
                       "<strong>280 soat</strong> — daqiqa soat deb yozib "
                       "yuborilgan.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Oʻrtacha "
                "maʼlumotdagi eng katta sondan katta boʻlishi "
                "mumkinmi?</strong></p>",
        "choices": [
            "Yoʻq — u har doim eng kichik va eng katta orasida boʻladi",
            "Ha, agar sonlar koʻp boʻlsa",
            "Ha, agar sonlar orasida nol boʻlsa",
            "Faqat manfiy sonlarda mumkin",
        ],
        "correct": "Yoʻq — u har doim eng kichik va eng katta orasida boʻladi",
        "explanation": "<p><strong>Yoʻq.</strong> Oʻrtacha — «baravar "
                       "boʻlinganda» degani, shuning uchun u eng kichikdan "
                       "kichik ham, eng kattadan katta ham boʻlolmaydi. Bu "
                       "javobni tekshirishning eng tez usuli.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Karim aka birinchi 3 kunda kuniga "
                "oʻrtacha 10 ming, keyingi 2 kunda kuniga oʻrtacha 20 ming "
                "soʻm topdi.</p><p><strong>Besh kunlik oʻrtacha daromadi "
                "qancha?</strong></p>",
        "choices": ["12 ming", "14 ming", "15 ming", "30 ming"],
        "correct": "14 ming",
        "explanation": "<p><strong>14 ming.</strong> Ikki oʻrtachani "
                       "qoʻshib ikkiga boʻlib boʻlmaydi. Butun yigʻindini "
                       "toping: 3 × 10 = 30 va 2 × 20 = 40, jami 70; keyin "
                       "70 ÷ 5 = 14. <strong>15 ming</strong> — aynan oʻsha "
                       "xato yoʻl ((10 + 20) ÷ 2).</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>5, 7 va 9 sonlarining oʻrtachasi 7 "
                "edi. Toʻplamga 0 qoʻshildi.</p><p><strong>Yangi oʻrtacha "
                "qancha?</strong></p>",
        "choices": ["5,25", "5,5", "7", "8,25"],
        "correct": "5,25",
        "explanation": "<p><strong>5,25.</strong> Yigʻindi oʻzgarmadi "
                       "(21 + 0 = 21), lekin sonlar soni 4 ta boʻldi: "
                       "21 ÷ 4 = 5,25. Nol «hech nima» emas — u ham bitta "
                       "qiymat va oʻrtachani pastga tortadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Toʻplamdagi eng katta son "
                "yanada kattalashtirildi, qolganlari oʻzgarmadi."
                "</p><p><strong>Oʻrtacha nima boʻladi?</strong></p>",
        "choices": [
            "Oshadi",
            "Kamayadi",
            "Oʻzgarmaydi",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "Oshadi",
        "explanation": "<p><strong>Oshadi.</strong> Yigʻindi oshdi, sonlar "
                       "soni esa oʻzgarmadi — demak boʻlinma ham oshadi. "
                       "Oʻrtacha har bir qiymatga bogʻliq, shuning uchun "
                       "bitta katta son uni oʻziga tortib ketadi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>Baholar: 5, 4, 5, 3, 4.<br>Yechim: "
                "<strong>5 + 4 + 5 + 3 + 4 = 21, oʻrtacha 21</strong></p>",
        "choices": [
            "Boʻlish tushib qolgan; toʻgʻrisi 21 ÷ 5 = 4,2",
            "Yigʻindi notoʻgʻri; toʻgʻrisi 20",
            "Toʻrtga boʻlish kerak edi; toʻgʻrisi 5,25",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Boʻlish tushib qolgan; toʻgʻrisi 21 ÷ 5 = 4,2",
        "explanation": "<p><strong>Boʻlish tushib qolgan.</strong> "
                       "21 ÷ 5 = 4,2. Javobni darrov tekshirish mumkin edi: "
                       "oʻrtacha 5 dan katta boʻlolmaydi, chunki eng katta "
                       "baho ham 5.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Toʻrtta sonning oʻrtachasi 6, "
                "yigʻindisi soʻralmoqda.<br>Yechim: <strong>6 ÷ 4 = "
                "1,5</strong></p>",
        "choices": [
            "Boʻlingan; toʻgʻrisi 6 × 4 = 24",
            "Toʻrt oʻrniga besh olingan; toʻgʻrisi 1,2",
            "Yigʻindi 6 ning oʻzi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Boʻlingan; toʻgʻrisi 6 × 4 = 24",
        "explanation": "<p><strong>Boʻlingan.</strong> Yigʻindi = oʻrtacha × "
                       "sonlar soni = 24. Mantiqqa soling: toʻrtta son "
                       "oʻrtacha 6 dan boʻlsa, ularning yigʻindisi 6 dan "
                       "kichik boʻlishi mumkin emas.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Karim aka taksi haydaydi. Besh "
                "kunlik daromadi (ming soʻmda): 100, 90, 120, 80 va "
                "110.</p><p><strong>Bir kunlik oʻrtacha daromadi "
                "qancha?</strong></p>",
        "choices": ["80 ming", "100 ming", "110 ming", "500 ming"],
        "correct": "100 ming",
        "explanation": "<p><strong>100 ming soʻm.</strong> Yigʻindi: "
                       "100 + 90 + 120 + 80 + 110 = 500. Oʻrtacha: "
                       "500 ÷ 5 = 100 ming. <strong>500 ming</strong> — "
                       "besh kunlik jami, bir kunlik emas.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Dilnozaning toʻrtta testdagi "
                "ballari: 70, 85, 75 va 90.</p><p><strong>Beshinchi testda "
                "necha ball olsa, oʻrtachasi 82 boʻladi?</strong></p>",
        "choices": ["82 ball", "84 ball", "90 ball", "96 ball"],
        "correct": "90 ball",
        "explanation": "<p><strong>90 ball.</strong> Beshta testning "
                       "yigʻindisi 82 × 5 = 410 boʻlishi kerak. Hozirgi "
                       "yigʻindi: 70 + 85 + 75 + 90 = 320. Demak beshinchisi "
                       "410 − 320 = 90. <strong>82 ball</strong> — kerakli "
                       "oʻrtachaning oʻzi; u yangi ballga teng emas, chunki "
                       "hozirgi oʻrtacha (80) 82 dan past.</p>",
    },
]


# =====================================================================
# PM-79 — mediana va moda
# =====================================================================

Q_PM79 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>1, 3, 5, 7, 9 sonlarining "
                "medianasi qancha?</strong></p>",
        "choices": ["3", "4", "5", "25"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Sonlar allaqachon saralangan "
                       "va beshta — demak oʻrtadagisi uchinchisi, yaʼni 5. "
                       "<strong>25</strong> — yigʻindi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2, 4, 6, 8 sonlarining medianasi "
                "qancha?</strong></p>",
        "choices": ["4", "5", "6", "20"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Sonlar juft, oʻrtada ikkitasi "
                       "qoladi: 4 va 6. Ularning oʻrta arifmetigi: "
                       "(4 + 6) ÷ 2 = 5. Mediana maʼlumotdagi sonlardan biri "
                       "boʻlishi shart emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>4, 4, 5, 6 sonlarining modasi "
                "qancha?</strong></p>",
        "choices": ["4", "4,5", "5", "6"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> U ikki marta uchradi, qolgani "
                       "bir martadan. <strong>4,5</strong> — bu mediana "
                       "((4 + 5) ÷ 2), moda emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Medianani topishda "
                "birinchi qadam nima?</strong></p>",
        "choices": [
            "Sonlarni oʻsish tartibida saralash",
            "Sonlarni qoʻshish",
            "Eng koʻp uchraganini topish",
            "Sonlar sonini ikkiga boʻlish",
        ],
        "correct": "Sonlarni oʻsish tartibida saralash",
        "explanation": "<p><strong>Saralash.</strong> «Oʻrtadagi son» degani "
                       "roʻyxatdagi emas, <em>saralangan qatordagi</em> "
                       "oʻrtadagi. Saralamasdan olingan javob deyarli har "
                       "doim notoʻgʻri chiqadi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>3, 7 va 5 sonlarining medianasi "
                "qancha?</strong></p>",
        "choices": ["3", "5", "7", "15"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Saralaymiz: 3, 5, 7. "
                       "Oʻrtadagisi — 5. <strong>7</strong> — saralashsiz "
                       "«oʻrtada turgan» son, yaʼni klassik xato.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>7, 2, 9, 4, 5 sonlarining "
                "medianasi qancha?</strong></p>",
        "choices": ["4", "5", "7", "9"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Saralaymiz: 2, 4, 5, 7, 9 — "
                       "oʻrtadagisi 5. <strong>9</strong> — saralanmagan "
                       "roʻyxatning oʻrtasi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10, 20, 30, 40 sonlarining "
                "medianasi qancha?</strong></p>",
        "choices": ["20", "25", "30", "100"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Juft son: oʻrtadagilari 20 va "
                       "30, demak (20 + 30) ÷ 2 = 25. Faqat bittasini olish "
                       "(20 yoki 30) — juft holatdagi asosiy xato.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>5, 3, 5, 2, 5, 1 sonlarining "
                "modasi qancha?</strong></p>",
        "choices": ["3", "4", "5", "6"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> U uch marta uchradi. "
                       "<strong>3</strong> — necha marta uchraganining soni "
                       "(chastota), moda esa qiymatning oʻzi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1, 2, 3, 4, 100 sonlarining "
                "medianasi qancha?</strong></p>",
        "choices": ["3", "10", "22", "100"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> Beshta son, oʻrtadagisi "
                       "uchinchisi — 3. Chetki 100 medianaga umuman taʼsir "
                       "qilmadi. <strong>22</strong> — bu oʻrta "
                       "arifmetik.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>1, 2, 3, 4, 100 sonlarining "
                "oʻrta arifmetigi qancha?</strong></p>",
        "choices": ["3", "10", "22", "110"],
        "correct": "22",
        "explanation": "<p><strong>22.</strong> Yigʻindi: "
                       "1 + 2 + 3 + 4 + 100 = 110, va 110 ÷ 5 = 22. Beshta "
                       "sondan toʻrttasi 22 dan kichik — bu chetki sonning "
                       "ishi. Medianasi esa atigi 3.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2, 3, 3, 4, 4, 10 sonlarining "
                "medianasi qancha?</strong></p>",
        "choices": ["3", "3,5", "4", "26"],
        "correct": "3,5",
        "explanation": "<p><strong>3,5.</strong> Oltita son — oʻrtadagilari "
                       "uchinchi va toʻrtinchi, yaʼni 3 va 4: "
                       "(3 + 4) ÷ 2 = 3,5. Sonlar allaqachon saralangan "
                       "boʻlsa ham, sanashni chetdan boshlang.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>2, 4, 6, 8, 10 "
                "sonlarining modasi qancha?</strong></p>",
        "choices": ["2", "6", "10", "Moda yoʻq"],
        "correct": "Moda yoʻq",
        "explanation": "<p><strong>Moda yoʻq.</strong> Hamma son bir martadan "
                       "uchragan, demak eng koʻp uchragani yoʻq. Bu xato "
                       "emas — maʼlumotning xossasi. <strong>6</strong> — "
                       "mediana, moda emas.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Qaysi kattalik "
                "chetki songa eng sezgir?</strong></p>",
        "choices": ["Oʻrta arifmetik", "Mediana", "Moda", "Uchalasi ham teng"],
        "correct": "Oʻrta arifmetik",
        "explanation": "<p><strong>Oʻrta arifmetik.</strong> U yigʻindidan "
                       "hisoblanadi, shuning uchun har bir qiymat, ayniqsa "
                       "juda katta yoki juda kichigi, unga taʼsir qiladi. "
                       "Mediana faqat oʻrtadagi songa qaraydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Sinfda sevimli rang "
                "soʻraldi: koʻk, qizil, koʻk, yashil, koʻk.</p><p><strong>Qaysi "
                "kattalikni hisoblash mumkin?</strong></p>",
        "choices": [
            "Faqat modani",
            "Faqat oʻrta arifmetikni",
            "Faqat medianani",
            "Uchalasini ham",
        ],
        "correct": "Faqat modani",
        "explanation": "<p><strong>Faqat modani.</strong> Ranglarni qoʻshib "
                       "boʻlmaydi va saralab ham boʻlmaydi, shuning uchun "
                       "oʻrtacha ham, mediana ham maʼnosiz. Modani esa "
                       "sanash bilan topsa boʻladi: koʻk (uch marta).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Korxonada oltita ishchi "
                "3 million, direktor esa 30 million oladi.</p><p><strong>Ish "
                "qidirayotgan odamga qaysi son halolroq maʼlumot "
                "beradi?</strong></p>",
        "choices": [
            "Mediana",
            "Oʻrta arifmetik",
            "Eng katta maosh",
            "Maoshlarning yigʻindisi",
        ],
        "correct": "Mediana",
        "explanation": "<p><strong>Mediana.</strong> Oʻrtacha "
                       "(6 × 3 + 30) ÷ 7 = 48 ÷ 7 ≈ 6,9 million chiqadi, "
                       "lekin yettitadan oltitasi atigi 3 million oladi. "
                       "Mediana 3 million — kelgan odam haqiqatan nima "
                       "kutishini shu koʻrsatadi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Birinchi toʻplam: "
                "1, 2, 3, 4, 5. Ikkinchisi: 1, 2, 3, 4, 90.</p><p><strong>Qaysi "
                "kattalik ikkalasida ham bir xil?</strong></p>",
        "choices": ["Mediana", "Oʻrta arifmetik", "Tarqoqlik", "Yigʻindi"],
        "correct": "Mediana",
        "explanation": "<p><strong>Mediana — ikkalasida ham 3.</strong> "
                       "Oʻrtacha esa keskin farq qiladi: birinchisida 3, "
                       "ikkinchisida (1+2+3+4+90) ÷ 5 = 20. Aynan shu "
                       "medianani chetki son bor joyda ishonchli qiladi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>7, 2, 9, 4, 5 sonlarining "
                "medianasi topilmoqda.<br>Yechim: <strong>oʻrtada 9 turibdi, "
                "demak mediana 9</strong></p>",
        "choices": [
            "Saralanmagan; saralab, mediana 5 boʻladi",
            "Oʻrtadagi emas, eng kattasi olinishi kerak edi",
            "Beshta emas, toʻrtta son bor",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Saralanmagan; saralab, mediana 5 boʻladi",
        "explanation": "<p><strong>Saralanmagan.</strong> Saralagach: "
                       "2, 4, 5, 7, 9 — oʻrtadagisi 5. Mediana har doim "
                       "saralangan qatordan olinadi; roʻyxatdagi joylashuv "
                       "hech qanday maʼnoga ega emas.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>3, 3, 3, 7, 9 sonlarining modasi "
                "topilmoqda.<br>Yechim: <strong>moda 3 marta</strong></p>",
        "choices": [
            "Moda — qiymatning oʻzi, yaʼni 3",
            "Moda 7, chunki u oʻrtada turibdi",
            "Bu toʻplamda moda yoʻq",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Moda — qiymatning oʻzi, yaʼni 3",
        "explanation": "<p><strong>Moda — qiymatning oʻzi.</strong> «Uch "
                       "marta» degani chastota (PM-75), moda esa eng koʻp "
                       "uchragan <em>son</em>. Bu yerda ikkalasi ham 3 "
                       "boʻlgani tasodif va shuning uchun ham chalkashish "
                       "oson.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Kichik firmada toʻqqiz kishi "
                "ishlaydi. Oylik maoshlari (million soʻmda): 4, 4, 4, 5, 5, "
                "6, 6, 7 va 49.</p><p><strong>Maoshlarning medianasi "
                "qancha?</strong></p>",
        "choices": ["4 million", "5 million", "6 million", "10 million"],
        "correct": "5 million",
        "explanation": "<p><strong>5 million.</strong> Sonlar saralangan va "
                       "toʻqqizta, demak oʻrtadagisi beshinchisi: "
                       "4, 4, 4, <strong>5</strong>, 5, 6, 6, 7, 49. "
                       "<strong>10 million</strong> — bu oʻrta arifmetik, "
                       "uni bitta katta maosh koʻtarib yuborgan.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Oʻsha firma ish eʼloniga «bizda "
                "oʻrtacha maosh yuqori» deb yozmoqchi. Toʻqqiz kishining "
                "maoshlari: 4, 4, 4, 5, 5, 6, 6, 7 va 49 million "
                "soʻm.</p><p><strong>Eʼlonga yoziladigan oʻrta arifmetik "
                "qancha chiqadi?</strong></p>",
        "choices": ["5 million", "6 million", "10 million", "90 million"],
        "correct": "10 million",
        "explanation": "<p><strong>10 million.</strong> Yigʻindi: "
                       "4+4+4+5+5+6+6+7+49 = 90, va 90 ÷ 9 = 10. Diqqat: "
                       "toʻqqiztadan <em>sakkiztasi</em> 10 milliondan kam "
                       "oladi — «oʻrtacha maosh 10 million» degan eʼlon "
                       "shuning uchun chalgʻitadi.</p>",
    },
]


# =====================================================================
# PM-80 — tarqoqlik
# =====================================================================

Q_PM80 = [
    # ── 1–5 tanish ────────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p><strong>3, 8, 5, 12, 7 sonlarining "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["5", "7", "9", "35"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Eng katta 12, eng kichik 3: "
                       "12 − 3 = 9. <strong>35</strong> — yigʻindi; "
                       "tarqoqlik qoʻshish emas, ayirish.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>10, 10, 10 sonlarining "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["0", "1", "10", "30"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> 10 − 10 = 0. Hamma qiymat bir "
                       "xil boʻlgani uchun maʼlumot umuman yoyilmagan. "
                       "Tarqoqlik 0 boʻlishi mumkin — bu xato emas.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tarqoqlik qanday "
                "topiladi?</strong></p>",
        "choices": [
            "Eng katta qiymatdan eng kichigini ayirib",
            "Hamma qiymatni qoʻshib",
            "Yigʻindini sonlar soniga boʻlib",
            "Saralab, oʻrtadagini olib",
        ],
        "correct": "Eng katta qiymatdan eng kichigini ayirib",
        "explanation": "<p><strong>Eng katta − eng kichik.</strong> Unga "
                       "faqat ikkita son kerak. «Yigʻindini soniga boʻlib» — "
                       "oʻrta arifmetik, «saralab oʻrtadagini» — "
                       "mediana.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>2, 3, 3, 3, 4 sonlarining "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["1", "2", "3", "15"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> 4 − 2 = 2. Qiymatlar bir-biriga "
                       "juda yaqin — kichik tarqoqlik barqarorlikni "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>0, 1, 3, 5, 6 sonlarining "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["3", "5", "6", "15"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> 6 − 0 = 6. Bu toʻplamning "
                       "oʻrtachasi ham 3 — oldingi savoldagidek, lekin "
                       "tarqoqligi uch barobar katta.</p>",
    },

    # ── 6–12 qoʻllash ─────────────────────────────────────────────
    {
        "text": "<p>Hisoblang.</p><p>Bir haftalik harorat: −5, 0, 3 va "
                "8 gradus.</p><p><strong>Tarqoqlik qancha?</strong></p>",
        "choices": ["3", "8", "13", "16"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> 8 − (−5) = 8 + 5 = 13 "
                       "(PM-10). Manfiy sondan ayirganda ishora almashadi. "
                       "<strong>3</strong> — 8 dan 5 ayirilgan, minus "
                       "eʼtiborsiz qoldirilgan.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>−10, −3 va 5 sonlarining "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["5", "8", "15", "18"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Eng katta 5, eng kichik −10: "
                       "5 − (−10) = 15. Manfiy sonlar orasida «eng kichik» — "
                       "noldan eng uzoqdagi manfiy son.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>4, 6, 5, 7 toʻplamiga 20 soni "
                "qoʻshildi.</p><p><strong>Tarqoqlik nechaga "
                "oʻzgardi?</strong></p>",
        "choices": ["3 dan 16 ga", "3 dan 20 ga", "7 dan 16 ga", "Oʻzgarmadi"],
        "correct": "3 dan 16 ga",
        "explanation": "<p><strong>3 dan 16 ga.</strong> Avval: 7 − 4 = 3. "
                       "Keyin: 20 − 4 = 16. Bitta chetki son tarqoqlikni "
                       "besh barobardan koʻproq kattalashtirdi — oʻrtachani "
                       "buzgani kabi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Toʻplamning tarqoqligi 12, eng "
                "kichik qiymati 5.</p><p><strong>Eng katta qiymati "
                "qancha?</strong></p>",
        "choices": ["7", "12", "17", "60"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> Tarqoqlik = eng katta − eng "
                       "kichik, demak eng katta = 12 + 5 = 17. "
                       "<strong>7</strong> — ayirilgan (12 − 5).</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tarqoqlik 0 "
                "boʻlishi nimani anglatadi?</strong></p>",
        "choices": [
            "Hamma qiymat bir xil",
            "Maʼlumot yoʻq",
            "Oʻrtacha ham 0",
            "Bunday boʻlishi mumkin emas",
        ],
        "correct": "Hamma qiymat bir xil",
        "explanation": "<p><strong>Hamma qiymat bir xil.</strong> Eng katta "
                       "bilan eng kichik teng boʻlgani uchun farq nol. "
                       "Oʻrtacha esa oʻsha qiymatning oʻzi boʻladi — "
                       "0 emas.</p>",
    },
    {
        "text": "<p>Hisoblang.</p><p><strong>78, 80, 80, 82, 80 ballarning "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["2", "4", "80", "400"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 82 − 78 = 4. Juda kichik "
                       "tarqoqlik: bu oʻquvchi har safar deyarli bir xil "
                       "natija koʻrsatadi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Bir doʻkonda non 4000–4200 soʻm, "
                "ikkinchisida 3500–5000 soʻm turadi.</p><p><strong>Qaysi "
                "doʻkonning narxi barqarorroq va uning tarqoqligi "
                "qancha?</strong></p>",
        "choices": [
            "Birinchisi, 200 soʻm",
            "Birinchisi, 500 soʻm",
            "Ikkinchisi, 1500 soʻm",
            "Ikkinchisi, 3500 soʻm",
        ],
        "correct": "Birinchisi, 200 soʻm",
        "explanation": "<p><strong>Birinchisi, 200 soʻm.</strong> "
                       "4200 − 4000 = 200, ikkinchisida esa "
                       "5000 − 3500 = 1500 soʻm. Kichik tarqoqlik — narxni "
                       "oldindan aytsa boʻladi degani.</p>",
    },

    # ── 13–16 farqlash ────────────────────────────────────────────
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>Ikki toʻplamning oʻrtachasi "
                "bir xil, tarqoqligi esa har xil.</p><p><strong>Ular bir xil "
                "toʻplammi?</strong></p>",
        "choices": [
            "Yoʻq — oʻrtacha teng boʻlsa ham qiymatlar boshqacha yoyilgan",
            "Ha — oʻrtachasi teng boʻlsa, toʻplamlar teng",
            "Faqat sonlar soni teng boʻlsa",
            "Aniqlab boʻlmaydi",
        ],
        "correct": ("Yoʻq — oʻrtacha teng boʻlsa ham qiymatlar boshqacha "
                    "yoyilgan"),
        "explanation": "<p><strong>Yoʻq.</strong> 2, 3, 3, 3, 4 va "
                       "0, 1, 3, 5, 6 ning oʻrtachasi ham 3, lekin birinchisi "
                       "tiqilgan, ikkinchisi yoyilgan. Bitta son maʼlumotni "
                       "toʻliq tasvirlay olmaydi.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p><strong>Tarqoqlik manfiy "
                "boʻlishi mumkinmi?</strong></p>",
        "choices": [
            "Yoʻq — eng kattadan eng kichigi ayiriladi",
            "Ha, agar qiymatlar manfiy boʻlsa",
            "Ha, agar oʻrtacha manfiy boʻlsa",
            "Faqat harorat maʼlumotida",
        ],
        "correct": "Yoʻq — eng kattadan eng kichigi ayiriladi",
        "explanation": "<p><strong>Yoʻq.</strong> Katta sondan kichigini "
                       "ayirganda natija hech qachon manfiy boʻlmaydi. "
                       "Manfiy chiqsa, tartib teskari qilingan. Qiymatlarning "
                       "oʻzi manfiy boʻlishi esa buni oʻzgartirmaydi: "
                       "−3 − (−10) = 7.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Toʻplam: 3, 3, 3, 3, 20."
                "</p><p><strong>Tarqoqlik qancha va u maʼlumotni toʻgʻri "
                "tasvirlaydimi?</strong></p>",
        "choices": [
            "17 — lekin toʻgʻri tasvirlamaydi, chunki faqat bitta chetki son bor",
            "17 — va maʼlumot haqiqatan bir tekis yoyilgan",
            "0 — chunki koʻpchilik qiymat bir xil",
            "20 — chunki eng katta qiymat 20",
        ],
        "correct": ("17 — lekin toʻgʻri tasvirlamaydi, chunki faqat bitta "
                    "chetki son bor"),
        "explanation": "<p><strong>17, lekin toʻgʻri tasvirlamaydi.</strong> "
                       "20 − 3 = 17. Tarqoqlik faqat ikkita chekka songa "
                       "qaraydi va oʻrtadagi toʻrtta bir xil qiymatni "
                       "koʻrmaydi. Shuning uchun diagrammaga ham qarash "
                       "kerak.</p>",
    },
    {
        "text": "<p>Toʻgʻri javobni tanlang.</p><p>A jamoa: 2, 3, 3, 3, 4 gol. "
                "B jamoa: 0, 1, 3, 5, 6 gol.</p><p><strong>Muhim oʻyinda "
                "ishonchli natija kerak boʻlsa, qaysi jamoa "
                "maʼqul?</strong></p>",
        "choices": [
            "A — tarqoqligi kichik, natijasi barqaror",
            "B — tarqoqligi katta, koʻproq gol urishi mumkin",
            "Farqi yoʻq — oʻrtachalari bir xil",
            "Aniqlab boʻlmaydi",
        ],
        "correct": "A — tarqoqligi kichik, natijasi barqaror",
        "explanation": "<p><strong>A.</strong> Uning tarqoqligi 2 (4 − 2), "
                       "yaʼni har oʻyinda 2–4 gol uradi. B ning tarqoqligi 6: "
                       "u 6 gol ham urishi, hech gol urmasligi ham mumkin. "
                       "Katta natija kerak boʻlganda esa aynan B "
                       "tanlanardi.</p>",
    },

    # ── 17–18 xato topish ─────────────────────────────────────────
    {
        "text": "<p>Qayerda xato bor?</p><p>2, 3, 3, 3, 4 sonlarining "
                "tarqoqligi topilmoqda.<br>Yechim: <strong>2 + 3 + 3 + 3 + 4 = "
                "15</strong></p>",
        "choices": [
            "Qoʻshilgan; tarqoqlik ayirish bilan topiladi: 4 − 2 = 2",
            "Beshga boʻlish kerak edi; toʻgʻrisi 3",
            "Faqat uchta son olinishi kerak edi",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Qoʻshilgan; tarqoqlik ayirish bilan topiladi: 4 − 2 = 2",
        "explanation": "<p><strong>Qoʻshilgan.</strong> 15 — bu yigʻindi, "
                       "undan oʻrta arifmetik topiladi (15 ÷ 5 = 3). "
                       "Tarqoqlik esa faqat ikkita songa qaraydi: "
                       "4 − 2 = 2.</p>",
    },
    {
        "text": "<p>Qayerda xato bor?</p><p>Toʻplam: 4, 7, 2, 5.<br>Yechim: "
                "<strong>2 − 7 = −5</strong></p>",
        "choices": [
            "Tartib teskari; toʻgʻrisi 7 − 2 = 5",
            "Eng katta son 5 edi; toʻgʻrisi 3",
            "Hamma sonni qoʻshish kerak edi; toʻgʻrisi 18",
            "Xato yoʻq, yechim toʻgʻri",
        ],
        "correct": "Tartib teskari; toʻgʻrisi 7 − 2 = 5",
        "explanation": "<p><strong>Tartib teskari.</strong> Eng kattadan "
                       "(7) eng kichigi (2) ayiriladi: 7 − 2 = 5. Manfiy "
                       "javob chiqishi — tartibni almashtirib yuborganingizni "
                       "bildiruvchi belgi.</p>",
    },

    # ── 19–20 matnli masala ───────────────────────────────────────
    {
        "text": "<p>Masalani yeching.</p><p>Olimpiadaga bitta oʻquvchi "
                "yuboriladi. Afsonaning ballari: 78, 80, 80, 82, 80. "
                "Jasurniki: 55, 70, 80, 95, 100.</p><p><strong>Jasurning "
                "tarqoqligi qancha?</strong></p>",
        "choices": ["4 ball", "20 ball", "45 ball", "80 ball"],
        "correct": "45 ball",
        "explanation": "<p><strong>45 ball.</strong> 100 − 55 = 45. "
                       "Afsonaniki esa atigi 82 − 78 = 4. Ikkalasining "
                       "oʻrtachasi ham 80 (yigʻindisi 400), lekin Jasurdan "
                       "nima kutishni bilib boʻlmaydi.</p>",
    },
    {
        "text": "<p>Masalani yeching.</p><p>Nodira opa ikkita ishchidan birini "
                "tanlaydi. Birinchisi besh kunda 18, 20, 19, 21, 22 dona "
                "mahsulot tayyorladi; ikkinchisi 10, 25, 15, 30, 20 "
                "dona.</p><p><strong>Ikkinchi ishchining tarqoqligi "
                "qancha?</strong></p>",
        "choices": ["4 dona", "10 dona", "20 dona", "30 dona"],
        "correct": "20 dona",
        "explanation": "<p><strong>20 dona.</strong> 30 − 10 = 20. "
                       "Birinchisiniki esa 22 − 18 = 4. Ikkalasining "
                       "yigʻindisi ham 100, oʻrtachasi ham 20 dona — lekin "
                       "birinchisi har kuni deyarli bir xil ishlaydi, "
                       "ikkinchisidan nima kutishni bilib boʻlmaydi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "PM-78 Mashq: Oʻrta arifmetik",
        "tutorial":    "PM-78:",
        "description": (
            "Oʻrtachani topish, yigʻindini tiklash, yetishmayotgan qiymatni "
            "hisoblash va chetki sonning taʼsiri. 20 savol."
        ),
        "questions":   Q_PM78,
        **DEFAULTS,
    },
    {
        "title":       "PM-79 Mashq: Mediana va moda",
        "tutorial":    "PM-79:",
        "description": (
            "Medianani saralab topish, juft holat, moda hamda uchala "
            "markaziy oʻlchovni taqqoslash. 20 savol."
        ),
        "questions":   Q_PM79,
        **DEFAULTS,
    },
    {
        "title":       "PM-80 Mashq: Tarqoqlik",
        "tutorial":    "PM-80:",
        "description": (
            "Tarqoqlikni topish, manfiy sonlar bilan ishlash, bir xil "
            "oʻrtachali toʻplamlarni ajratish. 20 savol."
        ),
        "questions":   Q_PM80,
        **DEFAULTS,
    },
]
