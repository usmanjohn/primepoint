# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-1 … SAT-5 (ifoda, chiziqli tenglama, matndan tenglama,
modul, qiyalik).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

Ramp: 1–4 warm-up · 5–10 exam shape · 11–14 context & interpretation ·
      15–16 trap-spotting · 17–18 Module 2 level · 19–20 word problems (har doim ikkita).

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA. Son: 3.5 va 1,200 (SAT konvensiyasi).
⚠️ Subject `Math` — Telegram uni "Matematika (SAT)" deb koʻrsatadi. `Matematika` EMAS.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_01_05.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "Math",
    "description": "SAT Math — Prime SAT darslarining mashqlari",
    "icon":        "bi-calculator",
    "color":       "#4f46e5",
}

DEFAULTS = {
    "level":                "easy",
    "is_free":              True,
    "is_published":         True,
    "is_available_for_all": True,
    "pass_score":           60,
    "max_attempts":         0,
    "show_answers_after":   True,
    "time_limit":           None,
}


# =====================================================================
# SAT-1 — variable & combining like terms
# =====================================================================

Q_SAT1 = [
    # ── 1–4 warm-up ──────────────────────────────────────────────────
    {
        "text": "<p>Which expression is equivalent to 4<i>x</i> + 6<i>x</i>?</p>",
        "choices": ["10<i>x</i>", "10<i>x</i><sup>2</sup>", "24<i>x</i>", "24<i>x</i><sup>2</sup>"],
        "correct": "10<i>x</i>",
        "explanation": "<p><strong>10x.</strong> Oʻxshash hadlar qoʻshilganda faqat "
                       "koeffitsientlar qoʻshiladi: 4 + 6 = 10, harf qismi oʻzgarmaydi.</p>"
                       "<p><strong>24x</strong> — qoʻshish oʻrniga koʻpaytirilgan, "
                       "<strong>10x<sup>2</sup></strong> esa qoʻshganda daraja koʻtarilgan. "
                       "Daraja faqat koʻpaytirganda oʻzgaradi.</p>",
    },
    {
        "text": "<p>In the expression 7 − 3<i>x</i>, what is the coefficient of <i>x</i>?</p>",
        "choices": ["−3", "3", "4", "7"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> Hadning ishorasi oldidagi belgi bilan birga "
                       "yuradi, shuning uchun koeffitsient −3.</p>"
                       "<p><strong>3</strong> — ishorani tashlab ketgan javob; "
                       "<strong>4</strong> — 7 − 3 ni hisoblab yuborgan javob, lekin 7 va 3x "
                       "oʻxshash hadlar emas.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 5<i>x</i> + 2 + 3<i>x</i> + 6?</p>",
        "choices": ["8<i>x</i> + 8", "8<i>x</i> + 12", "11<i>x</i> + 6", "16<i>x</i>"],
        "correct": "8<i>x</i> + 8",
        "explanation": "<p><strong>8x + 8.</strong> 5x + 3x = 8x va 2 + 6 = 8. Harfli hadlar "
                       "harfli hadlar bilan, sonlar sonlar bilan qoʻshiladi.</p>"
                       "<p><strong>16x</strong> — hamma sonni oʻxshash had deb qoʻshib "
                       "yuborgan javob (5 + 2 + 3 + 6). Son va harfli had hech qachon "
                       "qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Which of the following is a like term with 5<i>x</i><sup>2</sup>?</p>",
        "choices": ["10", "2<i>x</i>", "2<i>x</i><sup>2</sup>", "<i>x</i><sup>3</sup>"],
        "correct": "2<i>x</i><sup>2</sup>",
        "explanation": "<p><strong>2x<sup>2</sup>.</strong> Oʻxshash hadlarning harf qismi "
                       "butunlay bir xil boʻlishi kerak — bir xil harf <em>va</em> bir xil "
                       "daraja.</p>"
                       "<p><strong>2x</strong> — harfi bir xil, lekin darajasi boshqa; "
                       "x va x<sup>2</sup> turli miqdorlar, ularni qoʻshib boʻlmaydi.</p>",
    },
    # ── 5–10 exam shape ──────────────────────────────────────────────
    {
        "text": "<p>Which expression is equivalent to 3(<i>x</i> + 4) − 2<i>x</i>?</p>",
        "choices": ["<i>x</i> + 4", "<i>x</i> + 12", "5<i>x</i> + 4", "5<i>x</i> + 12"],
        "correct": "<i>x</i> + 12",
        "explanation": "<p><strong>x + 12.</strong> Avval qavs: 3x + 12. Keyin 3x − 2x = x.</p>"
                       "<p><strong>5x + 12</strong> — ayirish oʻrniga qoʻshgan javob; "
                       "<strong>x + 4</strong> — 3 ni faqat x ga koʻpaytirib, 4 ni "
                       "tegmasdan qoldirgan javob.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 9<i>x</i> − (4<i>x</i> − 7)?</p>",
        "choices": ["5<i>x</i> − 7", "5<i>x</i> + 7", "13<i>x</i> − 7", "13<i>x</i> + 7"],
        "correct": "5<i>x</i> + 7",
        "explanation": "<p><strong>5x + 7.</strong> Qavs oldidagi minus ichkaridagi ikkala "
                       "hadning ham ishorasini almashtiradi: −4x va <b>+7</b>. Keyin "
                       "9x − 4x = 5x.</p>"
                       "<p><strong>5x − 7</strong> — minusni faqat birinchi hadga qoʻllagan "
                       "javob. Bu SAT'dagi eng koʻp uchraydigan bitta xato.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 2(3<i>x</i> − 1) + 4(<i>x</i> + 2)?</p>",
        "choices": ["10<i>x</i> − 10", "10<i>x</i> + 6", "10<i>x</i> + 10", "14<i>x</i> + 6"],
        "correct": "10<i>x</i> + 6",
        "explanation": "<p><strong>10x + 6.</strong> 6x − 2 + 4x + 8 → 6x + 4x = 10x va "
                       "−2 + 8 = 6.</p>"
                       "<p><strong>10x + 10</strong> — −2 ni +2 deb olgan; "
                       "<strong>14x + 6</strong> — 4 ni qavs ichidagi 2 ga ham koʻpaytirib, "
                       "uni harfli had deb hisoblagan javob.</p>",
    },
    {
        "text": "<p>The expression 6<i>x</i> + 5 − 2(<i>x</i> + 3) is equivalent to "
                "<i>ax</i> + <i>b</i>, where <i>a</i> and <i>b</i> are constants. "
                "What is the value of <i>a</i>?</p>",
        "choices": ["−1", "4", "8", "11"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 6x + 5 − 2x − 6 = 4x − 1, demak a = 4.</p>"
                       "<p><strong>−1</strong> — bu <i>b</i>, <i>a</i> emas: savolning "
                       "oxirgi harfiga qarang. <strong>8</strong> — ayirish oʻrniga "
                       "qoʻshgan javob (6 + 2).</p>",
    },
    {
        "text": "<p>A rectangle has a length of 3<i>x</i> + 1 and a width of <i>x</i> + 4. "
                "Its perimeter can be written as <i>ax</i> + <i>b</i>. "
                "What is the value of <i>a</i> + <i>b</i>?</p>",
        "choices": ["8", "9", "10", "18"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Perimetr = 2(uzunlik + eni) = "
                       "2((3x + 1) + (x + 4)) = 2(4x + 5) = 8x + 10. Demak a = 8, b = 10 "
                       "va a + b = 18.</p>"
                       "<p><strong>9</strong> — ikkiga koʻpaytirishni unutgan javob "
                       "(4 + 5). Perimetr toʻrt tomonning yigʻindisi.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to −(2<i>x</i> − 5) + 3<i>x</i>?</p>",
        "choices": ["<i>x</i> − 5", "<i>x</i> + 5", "5<i>x</i> − 5", "5<i>x</i> + 5"],
        "correct": "<i>x</i> + 5",
        "explanation": "<p><strong>x + 5.</strong> Qavs oldidagi minus «−1 ga koʻpaytirish» "
                       "degani: −2x + 5. Keyin −2x + 3x = x.</p>"
                       "<p><strong>x − 5</strong> — −1 × (−5) ni −5 deb olgan javob. "
                       "Ikki minus har doim plyus beradi.</p>",
    },
    # ── 11–14 context & interpretation ───────────────────────────────
    {
        "text": "<p>A pen costs <i>p</i> dollars. A notebook costs $3 more than a pen. "
                "Which expression represents the total cost of 2 pens and 1 notebook?</p>",
        "choices": ["2<i>p</i> + 3", "3<i>p</i> + 3", "3<i>p</i> + 9", "6<i>p</i> + 3"],
        "correct": "3<i>p</i> + 3",
        "explanation": "<p><strong>3p + 3.</strong> Ikkita ruchka — 2p, daftar — "
                       "(p + 3). Jami: 2p + p + 3 = 3p + 3.</p>"
                       "<p><strong>2p + 3</strong> — daftarning narxidagi <i>p</i> ni "
                       "unutgan javob: daftar $3 emas, ruchkadan $3 qimmat.</p>",
    },
    {
        "text": "<p>A print shop charges a setup fee plus a fixed amount for each shirt. "
                "The total cost, in dollars, for <i>n</i> shirts is 8<i>n</i> + 25. "
                "Which of the following is the best interpretation of the number 8?</p>",
        "choices": ["The setup fee is $8.",
                    "The cost of each shirt is $8.",
                    "A total of 8 shirts were printed.",
                    "The total cost is $8."],
        "correct": "The cost of each shirt is $8.",
        "explanation": "<p><strong>Har bir futbolka $8.</strong> 8 soni <i>n</i> bilan "
                       "birga turibdi, demak u har bir futbolkaga tegishli.</p>"
                       "<p><strong>«The setup fee is $8»</strong> — notoʻgʻri: bir martalik "
                       "toʻlov harfsiz turadi, u — 25. Qoida: harf bilan turgan son "
                       "«har bir … uchun», yolgʻiz turgan son «bir marta».</p>",
    },
    {
        "text": "<p>Maria has <i>x</i> books. Her friend has 5 fewer books than Maria. "
                "Which expression represents the number of books her friend has?</p>",
        "choices": ["5 − <i>x</i>", "5<i>x</i>", "<i>x</i> − 5", "<i>x</i> + 5"],
        "correct": "<i>x</i> − 5",
        "explanation": "<p><strong>x − 5.</strong> «5 fewer than Maria» — Mariyanikidan "
                       "5 ta kam, yaʼni x dan 5 ni ayiramiz.</p>"
                       "<p><strong>5 − x</strong> — ingliz tilida 5 oldin aytilgani uchun "
                       "uni oldin yozib yuborgan javob. <em>fewer/less than</em> ayirmani "
                       "har doim teskari tartibda yozadi.</p>",
    },
    {
        "text": "<p>A technician's pay, in dollars, for <i>h</i> hours of work is given by "
                "12<i>h</i> + 40. What is the pay for 3 hours of work?</p>",
        "choices": ["$40", "$52", "$76", "$156"],
        "correct": "$76",
        "explanation": "<p><strong>$76.</strong> h = 3 ni qoʻyamiz: 12 × 3 + 40 = 36 + 40 = 76.</p>"
                       "<p><strong>$52</strong> — bir soatlik toʻlov (h = 1); "
                       "<strong>$156</strong> — bir soatlik toʻlovni uchga koʻpaytirgan "
                       "javob, lekin unda $40 uch marta hisoblanadi.</p>",
    },
    # ── 15–16 trap-spotting ──────────────────────────────────────────
    {
        "text": "<p>The expression 4<i>x</i> + 3 − <i>x</i> + 7 is equivalent to "
                "<i>ax</i> + <i>b</i>, where <i>a</i> and <i>b</i> are constants. "
                "What is the value of <i>a</i> · <i>b</i>?</p>",
        "choices": ["13", "21", "30", "40"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> Ifoda 3x + 10 ga teng, demak a = 3, b = 10 "
                       "va a · b = 30.</p>"
                       "<p><strong>13</strong> — a + b hisoblangan, koʻpaytma emas: savol "
                       "belgisini oʻqing. <strong>40</strong> — 4 ni koeffitsient deb olgan "
                       "javob (−x ni ayirishni unutgan).</p>",
    },
    {
        "text": "<p>Which of the following is <b>NOT</b> equivalent to 6<i>x</i> + 12?</p>",
        "choices": ["2(3<i>x</i> + 6)", "3(2<i>x</i> + 4)", "6(<i>x</i> + 2)", "6(<i>x</i> + 12)"],
        "correct": "6(<i>x</i> + 12)",
        "explanation": "<p><strong>6(x + 12).</strong> Ochsak 6x + 72 chiqadi — bu 6x + 12 "
                       "emas.</p>"
                       "<p>Qolgan uchtasi ochilganda aynan 6x + 12 beradi. <b>NOT</b> soʻzi "
                       "bor savolda javob — «notoʻgʻri» variant; SAT bu soʻzni qalin qilib "
                       "yozadi, chunki oʻquvchilar uni oʻqimasdan oʻtib ketadi.</p>",
    },
    # ── 17–18 Module 2 level ─────────────────────────────────────────
    {
        "text": "<p>The expression 5(2<i>x</i> − 3) − 2(3<i>x</i> − 4) is equivalent to "
                "<i>ax</i> + <i>b</i>, where <i>a</i> and <i>b</i> are constants. "
                "What is the value of <i>a</i> + <i>b</i>?</p>",
        "choices": ["−11", "−7", "−3", "4"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> 10x − 15 − 6x + 8 = 4x − 7, demak "
                       "a = 4, b = −7 va a + b = −3.</p>"
                       "<p><strong>−11</strong> — −2 × (−4) ni hisobga olmagan javob "
                       "(4 − 15). <strong>−7</strong> — faqat b, <strong>4</strong> — "
                       "faqat a.</p>",
    },
    {
        "text": "<p>Which expression is equivalent to 3(<i>x</i> + 2<i>y</i>) − "
                "2(2<i>x</i> − <i>y</i>)?</p>",
        "choices": ["−<i>x</i> + 4<i>y</i>", "−<i>x</i> + 8<i>y</i>",
                    "<i>x</i> + 8<i>y</i>", "7<i>x</i> + 4<i>y</i>"],
        "correct": "−<i>x</i> + 8<i>y</i>",
        "explanation": "<p><strong>−x + 8y.</strong> 3x + 6y − 4x + 2y → 3x − 4x = −x va "
                       "6y + 2y = 8y.</p>"
                       "<p><strong>x + 8y</strong> — 3x − 4x ni +x deb olgan javob: "
                       "kichikdan kattani ayirganda natija manfiy. <strong>−x + 4y</strong> "
                       "— −2 × (−y) ni hisobga olmagan javob.</p>",
    },
    # ── 19–20 word problems ──────────────────────────────────────────
    {
        "text": "<p>A photography club charges a $30 registration fee plus $8 for each event "
                "a member attends. Which expression represents the total cost, in dollars, "
                "for a member who attends <i>e</i> events?</p>",
        "choices": ["8(<i>e</i> + 30)", "8<i>e</i> + 30", "30<i>e</i> + 8", "38<i>e</i>"],
        "correct": "8<i>e</i> + 30",
        "explanation": "<p><strong>8e + 30.</strong> $8 har bir tadbir uchun, demak "
                       "tadbirlar soniga koʻpayadi; $30 bir marta toʻlanadi va yolgʻiz "
                       "turadi.</p>"
                       "<p><strong>38e</strong> — ikkala toʻlovni ham har safar hisoblagan "
                       "javob. <strong>30e + 8</strong> — ikki sonni almashtirib "
                       "yuborgan javob.</p>",
    },
    {
        "text": "<p>Tickets to a school play cost $12 for an adult and $8 for a child. "
                "Which expression represents the total cost, in dollars, for "
                "<i>a</i> adults and 3 children?</p>",
        "choices": ["12<i>a</i> + 8", "12<i>a</i> + 24", "20<i>a</i>", "36<i>a</i>"],
        "correct": "12<i>a</i> + 24",
        "explanation": "<p><strong>12a + 24.</strong> Kattalar: 12a. Bolalar: 3 × 8 = 24 — "
                       "soni maʼlum, shuning uchun bu oddiy son.</p>"
                       "<p><strong>12a + 8</strong> — bitta bola hisoblangan; "
                       "<strong>20a</strong> — ikki narxni qoʻshib, ikkalasini ham "
                       "kattalar soniga koʻpaytirgan javob.</p>",
    },
]


# =====================================================================
# SAT-2 — solving single-variable linear equations
# =====================================================================

Q_SAT2 = [
    # ── 1–4 warm-up ──────────────────────────────────────────────────
    {
        "text": "<p>If 3<i>x</i> = 21, what is the value of <i>x</i>?</p>",
        "choices": ["7", "18", "24", "63"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Ikkala tomonni 3 ga boʻldik: 21 ÷ 3 = 7.</p>"
                       "<p><strong>18</strong> — boʻlish oʻrniga 3 ni ayirgan javob. "
                       "3<i>x</i> «3 koʻpaytiruv x» degani, shuning uchun teskari amal — "
                       "<b>boʻlish</b>.</p>",
    },
    {
        "text": "<p>If <i>x</i> + 9 = 4, what is the value of <i>x</i>?</p>",
        "choices": ["−13", "−5", "5", "13"],
        "correct": "−5",
        "explanation": "<p><strong>−5.</strong> Ikkala tomondan 9 ni ayirdik: 4 − 9 = −5.</p>"
                       "<p><strong>5</strong> — 9 − 4 hisoblangan javob: ayirish tartibi "
                       "muhim. <strong>13</strong> — ayirish oʻrniga qoʻshgan javob.</p>",
    },
    {
        "text": "<p>If <i>x</i> ÷ 4 = 6, what is the value of <i>x</i>?</p>",
        "choices": ["1.5", "2", "10", "24"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> Boʻlishning teskarisi — koʻpaytirish: "
                       "6 × 4 = 24.</p>"
                       "<p><strong>1.5</strong> — yana bir marta boʻlgan javob (6 ÷ 4); "
                       "<strong>10</strong> — qoʻshgan javob. Amalning teskarisini toʻgʻri "
                       "tanlash — butun mavzuning kaliti.</p>",
    },
    {
        "text": "<p>If 2<i>x</i> − 5 = 11, what is the value of <i>x</i>?</p>",
        "choices": ["3", "8", "16", "32"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 2<i>x</i> = 16, keyin 2 ga boʻlamiz: x = 8.</p>"
                       "<p><strong>16</strong> — bitta qadam yetmay toʻxtagan javob "
                       "(2x = 16 topilgan, boʻlinmagan). SAT bu «yarim yoʻldagi» sonni "
                       "deyarli har doim javoblar orasiga qoʻyadi.</p>",
    },
    # ── 5–10 exam shape ──────────────────────────────────────────────
    {
        "text": "<p>If 4(<i>x</i> − 2) = 12, what is the value of <i>x</i>?</p>",
        "choices": ["1", "3", "5", "14"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Ikkala tomonni 4 ga boʻlamiz: x − 2 = 3, "
                       "demak x = 5. (Yoki qavsni ochib: 4x − 8 = 12 → 4x = 20.)</p>"
                       "<p><strong>1</strong> — 3 dan 2 ni ayirgan javob: x − 2 = 3 dan "
                       "x = 3 + 2 chiqadi, 3 − 2 emas.</p>",
    },
    {
        "text": "<p>If 6<i>x</i> + 4 = 2<i>x</i> + 20, what is the value of <i>x</i>?</p>",
        "choices": ["2", "3", "4", "6"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 2x ni ayiramiz: 4x + 4 = 20; 4 ni ayiramiz: "
                       "4x = 16; 4 ga boʻlamiz: x = 4.</p>"
                       "<p><strong>3</strong> — 2x ni ayirish oʻrniga qoʻshgan javob "
                       "(8x = 24). Harfli hadni oʻtkazganda ishorasi almashadi.</p>",
    },
    {
        "text": "<p>If 3(<i>x</i> + 2) = 2(<i>x</i> + 5), what is the value of <i>x</i>?</p>",
        "choices": ["−16", "3", "4", "16"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 3x + 6 = 2x + 10 → x = 4.</p>"
                       "<p><strong>3</strong> — qavsni faqat birinchi hadga ochgan javob "
                       "(3x + 2 = 2x + 5). Qavs oldidagi son <b>ichidagi hamma hadga</b> "
                       "koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>If 0.5<i>x</i> + 3 = 8, what is the value of <i>x</i>?</p>",
        "choices": ["2.5", "5", "10", "22"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 0.5x = 5, keyin 0.5 ga boʻlamiz: "
                       "5 ÷ 0.5 = 10. (0.5 ga boʻlish — ikkiga koʻpaytirish bilan bir xil.)</p>"
                       "<p><strong>5</strong> — bitta qadam yetmay toʻxtagan javob; "
                       "<strong>2.5</strong> — boʻlish oʻrniga 0.5 ga koʻpaytirgan javob.</p>",
    },
    {
        "text": "<p>If <i>x</i> ÷ 3 + 2 = 7, what is the value of <i>x</i>?</p>",
        "choices": ["5", "15", "21", "27"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Avval 2 ni ayiramiz: x ÷ 3 = 5, keyin "
                       "3 ga koʻpaytiramiz: x = 15.</p>"
                       "<p><strong>21</strong> — 2 ni ayirishni unutib, darhol 7 × 3 "
                       "hisoblagan javob. Tartib muhim: avval qoʻshiluvchidan, keyin "
                       "koʻpaytuvchidan qutuling.</p>",
    },
    {
        "text": "<p>If 2(3<i>x</i> − 1) = 4<i>x</i> + 8, what is the value of <i>x</i>?</p>",
        "choices": ["1", "4.5", "5", "10"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 6x − 2 = 4x + 8 → 2x = 10 → x = 5.</p>"
                       "<p><strong>1</strong> — 4x ni ayirish oʻrniga qoʻshgan javob "
                       "(10x = 10). <strong>10</strong> — 2x = 10 da toʻxtab qolgan javob.</p>",
    },
    # ── 11–14 context & interpretation ───────────────────────────────
    {
        "text": "<p>A repair shop charges a fixed fee plus an hourly rate. The total cost of "
                "a repair is modeled by the equation 45 + 12<i>h</i> = 105. "
                "What does <i>h</i> represent?</p>",
        "choices": ["The total cost of the repair",
                    "The fixed fee, in dollars",
                    "The hourly rate, in dollars",
                    "The number of hours worked"],
        "correct": "The number of hours worked",
        "explanation": "<p><strong>Ishlangan soatlar soni.</strong> 12 — bir soatlik narx, "
                       "shuning uchun uning yonidagi harf soatlar sonini bildiradi.</p>"
                       "<p><strong>«The hourly rate»</strong> — bu 12 ning oʻzi, h emas. "
                       "Harf bilan turgan son «har bir … uchun», harfning oʻzi esa "
                       "«nechta» degan savolga javob.</p>",
    },
    {
        "text": "<p>A tank is being drained. The number of liters left after <i>m</i> minutes "
                "is 500 − 12<i>m</i>. Which of the following is the best interpretation of "
                "the number 12?</p>",
        "choices": ["The tank starts with 12 liters.",
                    "The tank drains 12 liters each minute.",
                    "The tank is empty after 12 minutes.",
                    "The tank holds 12 liters at the end."],
        "correct": "The tank drains 12 liters each minute.",
        "explanation": "<p><strong>Har daqiqada 12 litr kamayadi.</strong> 12 soni <i>m</i> "
                       "bilan turibdi va oldida minus bor — demak har daqiqada shuncha "
                       "<b>kamayadi</b>.</p>"
                       "<p><strong>«Starts with 12»</strong> — notoʻgʻri: boshlangʻich "
                       "hajm 500, u harfsiz turgan son.</p>",
    },
    {
        "text": "<p>The cost <i>C</i>, in dollars, of a party for <i>n</i> guests is given by "
                "<i>C</i> = 25 + 15<i>n</i>. What is the cost of a party for 10 guests?</p>",
        "choices": ["$40", "$150", "$175", "$250"],
        "correct": "$175",
        "explanation": "<p><strong>$175.</strong> n = 10: 25 + 15 × 10 = 25 + 150 = 175.</p>"
                       "<p><strong>$150</strong> — bir martalik $25 ni unutgan javob; "
                       "<strong>$250</strong> — 25 ni mehmonlar soniga koʻpaytirgan javob, "
                       "lekin u faqat bir marta toʻlanadi.</p>",
    },
    {
        "text": "<p>A phone bill is $40 per month plus $0.05 for each minute of calls. "
                "One month the bill was $58. How many minutes of calls were made?</p>",
        "choices": ["18", "36", "360", "1,160"],
        "correct": "360",
        "explanation": "<p><strong>360.</strong> 40 + 0.05<i>m</i> = 58 → 0.05<i>m</i> = 18 "
                       "→ <i>m</i> = 18 ÷ 0.05 = 360.</p>"
                       "<p><strong>1,160</strong> — oylik $40 ni ayirishni unutgan javob "
                       "(58 ÷ 0.05). <strong>18</strong> — bitta qadam yetmay toʻxtagan "
                       "javob: $18 — bu daqiqalar uchun toʻlangan pul, daqiqalar soni emas.</p>",
    },
    # ── 15–16 trap-spotting ──────────────────────────────────────────
    {
        "text": "<p>If 3<i>x</i> − 7 = 14, what is the value of <i>x</i> + 5?</p>",
        "choices": ["7", "12", "19", "26"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> 3x = 21 → x = 7, keyin savol soʻragan "
                       "narsani hisoblaymiz: 7 + 5 = 12.</p>"
                       "<p><strong>7</strong> — x ning oʻzi: SAT'da eng koʻp yoʻqotiladigan "
                       "ochko shu yerda. Savolning oxirgi jumlasini har doim ikki marta "
                       "oʻqing.</p>",
    },
    {
        "text": "<p>4(<i>x</i> + <i>c</i>) = 4<i>x</i> + 20</p>"
                "<p>In the equation above, <i>c</i> is a constant. If the equation has "
                "infinitely many solutions, what is the value of <i>c</i>?</p>",
        "choices": ["4", "5", "16", "20"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Chapni ochamiz: 4x + 4c = 4x + 20. 4x ikkala "
                       "tomonda bir xil — qisqaradi, demak 4c = 20 va c = 5.</p>"
                       "<p><strong>20</strong> — qavsni ochmasdan c ni 20 deb olgan javob; "
                       "<strong>16</strong> — boʻlish oʻrniga 4 ni ayirgan javob.</p>",
    },
    # ── 17–18 Module 2 level ─────────────────────────────────────────
    {
        "text": "<p>If (2<i>x</i> + 1) ÷ 3 = (<i>x</i> + 5) ÷ 2, what is the value "
                "of <i>x</i>?</p>",
        "choices": ["1.75", "13", "15", "17"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> Kesishtirib koʻpaytiramiz: "
                       "2(2x + 1) = 3(x + 5) → 4x + 2 = 3x + 15 → x = 13.</p>"
                       "<p><strong>1.75</strong> — kesishtirishni teskari tomonga qilgan "
                       "javob (3(2x + 1) = 2(x + 5)). Har bir surat <b>qarama-qarshi</b> "
                       "maxrajga koʻpaytiriladi.</p>",
    },
    {
        "text": "<p>2<i>x</i> + 5 = <i>kx</i> + 9</p>"
                "<p>In the equation above, <i>k</i> is a constant. For what value of "
                "<i>k</i> does the equation have no solution?</p>",
        "choices": ["−2", "0", "2", "4"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> «Yechim yoʻq» boʻlishi uchun x lar qisqarishi, "
                       "lekin sonlar teng boʻlmasligi kerak. k = 2 boʻlsa: 2x + 5 = 2x + 9 → "
                       "5 = 9, yolgʻon — demak yechim yoʻq.</p>"
                       "<p><strong>4</strong> — 9 − 5 hisoblangan javob; k sonlar bilan "
                       "emas, <b>x ning koeffitsienti</b> bilan solishtiriladi.</p>",
    },
    # ── 19–20 word problems ──────────────────────────────────────────
    {
        "text": "<p>A gym charges a one-time $45 joining fee plus $15 per month. A member "
                "has paid $195 in total. For how many months has the member belonged to "
                "the gym?</p>",
        "choices": ["10", "13", "16", "150"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 45 + 15m = 195 → 15m = 150 → m = 10.</p>"
                       "<p><strong>13</strong> — bir martalik $45 ni ayirishni unutgan javob "
                       "(195 ÷ 15). <strong>150</strong> — oxirgi qadamni qilmagan javob: "
                       "$150 — oylik toʻlovlarning jami, oylar soni emas.</p>",
    },
    {
        "text": "<p>A number is multiplied by 4, and then 6 is subtracted from the result. "
                "The final result is 26. What is the number?</p>",
        "choices": ["5", "8", "20", "32"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> 4n − 6 = 26 → 4n = 32 → n = 8.</p>"
                       "<p><strong>32</strong> — 4 ga boʻlishni unutgan javob; "
                       "<strong>5</strong> — amallarni teskari tartibda bajargan javob "
                       "((26 − 6) ÷ 4). Teskari yurganda 6 <b>qoʻshiladi</b>, ayrilmaydi.</p>",
    },
]


# =====================================================================
# SAT-3 — setting up linear equations from word problems
# =====================================================================

Q_SAT3 = [
    # ── 1–4 warm-up ──────────────────────────────────────────────────
    {
        "text": "<p>Which expression represents «7 more than <i>x</i>»?</p>",
        "choices": ["7 − <i>x</i>", "7<i>x</i>", "<i>x</i> − 7", "<i>x</i> + 7"],
        "correct": "<i>x</i> + 7",
        "explanation": "<p><strong>x + 7.</strong> <em>more than</em> — qoʻshish.</p>"
                       "<p>Qoʻshishda tartib muhim emas (x + 7 = 7 + x), lekin "
                       "<em>less than</em> da muhim — keyingi savolga qarang.</p>",
    },
    {
        "text": "<p>Which expression represents «3 less than twice a number <i>n</i>»?</p>",
        "choices": ["2(<i>n</i> − 3)", "2<i>n</i> − 3", "3 − 2<i>n</i>", "3<i>n</i> − 2"],
        "correct": "2<i>n</i> − 3",
        "explanation": "<p><strong>2n − 3.</strong> Avval «twice a number» = 2n, keyin "
                       "«3 less than» uni 3 ga kamaytiradi.</p>"
                       "<p><strong>3 − 2n</strong> — ingliz tilida 3 oldin aytilgani uchun "
                       "uni oldin yozib yuborgan javob. <em>less than</em> ayirmani "
                       "<b>teskari</b> tartibda yozadi.</p>",
    },
    {
        "text": "<p>A worker earns $9 per hour. Which expression represents the amount "
                "earned in <i>h</i> hours?</p>",
        "choices": ["9 + <i>h</i>", "9 − <i>h</i>", "9<i>h</i>", "<i>h</i> ÷ 9"],
        "correct": "9<i>h</i>",
        "explanation": "<p><strong>9h.</strong> <em>per</em> — har doim koʻpaytirish: har "
                       "soat uchun $9, demak soatlar soniga koʻpayadi.</p>"
                       "<p><strong>9 + h</strong> — «per» ni qoʻshish deb tushungan javob. "
                       "Testda <em>per</em> soʻzini koʻrsangiz, darhol × belgisini "
                       "oʻylang.</p>",
    },
    {
        "text": "<p>Which expression represents «the product of 5 and (<i>x</i> + 2)»?</p>",
        "choices": ["(<i>x</i> + 2) ÷ 5", "5 + 2<i>x</i>", "5(<i>x</i> + 2)", "5<i>x</i> + 2"],
        "correct": "5(<i>x</i> + 2)",
        "explanation": "<p><strong>5(x + 2).</strong> <em>product</em> — koʻpaytma, va "
                       "koʻpaytiriladigan narsa butun (x + 2) ifodasi, shuning uchun qavs "
                       "shart.</p>"
                       "<p><strong>5x + 2</strong> — qavssiz yozilgan javob; unda 5 faqat "
                       "x ga koʻpaytiriladi va maʼno oʻzgaradi.</p>",
    },
    # ── 5–10 exam shape ──────────────────────────────────────────────
    {
        "text": "<p>A pool contains 800 gallons of water and is being drained at a constant "
                "rate of 25 gallons per minute. Which equation gives the number of gallons "
                "<i>W</i> remaining after <i>m</i> minutes?</p>",
        "choices": ["<i>W</i> = 25(800 − <i>m</i>)", "<i>W</i> = 25<i>m</i> − 800",
                    "<i>W</i> = 800 + 25<i>m</i>", "<i>W</i> = 800 − 25<i>m</i>"],
        "correct": "<i>W</i> = 800 − 25<i>m</i>",
        "explanation": "<p><strong>W = 800 − 25m.</strong> Boshlangʻich hajm 800, har daqiqada "
                       "25 gallon <b>kamayadi</b> — shuning uchun minus.</p>"
                       "<p><strong>W = 800 + 25m</strong> — <em>draining</em> soʻzini "
                       "eʼtiborsiz qoldirgan javob. Bitta inglizcha soʻz butun ishorani hal "
                       "qiladi.</p>",
    },
    {
        "text": "<p>A cell plan costs $30 per month plus $0.20 for each gigabyte of data "
                "used. Which equation gives the total monthly cost <i>C</i>, in dollars, "
                "when <i>g</i> gigabytes are used?</p>",
        "choices": ["<i>C</i> = 0.20 + 30<i>g</i>", "<i>C</i> = 30 + 0.20<i>g</i>",
                    "<i>C</i> = 30(0.20<i>g</i>)", "<i>C</i> = 30.20<i>g</i>"],
        "correct": "<i>C</i> = 30 + 0.20<i>g</i>",
        "explanation": "<p><strong>C = 30 + 0.20g.</strong> $30 oyiga bir marta — yolgʻiz "
                       "turadi; $0.20 har gigabayt uchun — <i>g</i> ga koʻpayadi.</p>"
                       "<p><strong>C = 30.20g</strong> — ikkala toʻlovni ham har gigabaytga "
                       "hisoblagan javob. 10 GB bilan tekshiring: toʻgʻri javob $32, bu "
                       "javob esa $302.</p>",
    },
    {
        "text": "<p>Sara is 4 years older than twice Ben's age. If Ben is <i>b</i> years old, "
                "which expression represents Sara's age?</p>",
        "choices": ["2(<i>b</i> + 4)", "2<i>b</i> + 4", "4<i>b</i> + 2", "<i>b</i> + 4"],
        "correct": "2<i>b</i> + 4",
        "explanation": "<p><strong>2b + 4.</strong> Avval «twice Ben's age» = 2b, keyin "
                       "«4 years older» = +4.</p>"
                       "<p><strong>2(b + 4)</strong> — avval 4 qoʻshib, keyin ikkilantirgan "
                       "javob; bu 2b + 8 ga teng. Jumladagi <b>tartib</b> qavsni qayerga "
                       "qoʻyishni hal qiladi.</p>",
    },
    {
        "text": "<p>Which equation could be used to find three consecutive integers whose "
                "sum is 72, where <i>n</i> is the smallest integer?</p>",
        "choices": ["3<i>n</i> = 72", "3<i>n</i> + 6 = 72",
                    "<i>n</i> + (<i>n</i> + 1) + (<i>n</i> + 2) = 72",
                    "<i>n</i>(<i>n</i> + 1)(<i>n</i> + 2) = 72"],
        "correct": "<i>n</i> + (<i>n</i> + 1) + (<i>n</i> + 2) = 72",
        "explanation": "<p><strong>n + (n + 1) + (n + 2) = 72.</strong> Ketma-ket butun "
                       "sonlar bir-biridan 1 ga farq qiladi va «sum» — ularning "
                       "yigʻindisi.</p>"
                       "<p><strong>3n + 6 = 72</strong> — bu yigʻindining soddalashtirilgan "
                       "shakli emas: n + (n+1) + (n+2) = 3n + <b>3</b>, 3n + 6 emas.</p>",
    },
    {
        "text": "<p>A print shop charges a $15 setup fee plus $0.40 per page. What is the "
                "total cost of printing 60 pages?</p>",
        "choices": ["$24", "$39", "$75", "$900"],
        "correct": "$39",
        "explanation": "<p><strong>$39.</strong> 15 + 0.40 × 60 = 15 + 24 = 39.</p>"
                       "<p><strong>$24</strong> — bir martalik $15 ni qoʻshishni unutgan "
                       "javob; <strong>$900</strong> — 15 ni sahifalar soniga koʻpaytirgan "
                       "javob, lekin u faqat bir marta olinadi.</p>",
    },
    {
        "text": "<p>Which equation represents «the sum of a number and its double is 36»?</p>",
        "choices": ["2<i>n</i> = 36", "<i>n</i> + 2 = 36", "<i>n</i> + 2<i>n</i> = 36",
                    "<i>n</i> · 2<i>n</i> = 36"],
        "correct": "<i>n</i> + 2<i>n</i> = 36",
        "explanation": "<p><strong>n + 2n = 36.</strong> «its double» — oʻsha sonning ikki "
                       "barobari, yaʼni 2n; «the sum of» esa ikkalasini qoʻshadi.</p>"
                       "<p><strong>n · 2n = 36</strong> — <em>sum</em> (yigʻindi) va "
                       "<em>product</em> (koʻpaytma) ni adashtirgan javob.</p>",
    },
    # ── 11–14 context & interpretation ───────────────────────────────
    {
        "text": "<p>An electricity bill is modeled by <i>C</i> = 0.12<i>m</i> + 45, where "
                "<i>m</i> is the number of kilowatt-hours used. Which of the following is "
                "the best interpretation of the number 45?</p>",
        "choices": ["The cost of each kilowatt-hour is $45.",
                    "The customer used 45 kilowatt-hours.",
                    "The fixed monthly charge is $45.",
                    "The total bill is $45."],
        "correct": "The fixed monthly charge is $45.",
        "explanation": "<p><strong>Oylik doimiy toʻlov $45.</strong> 45 harfsiz turibdi — "
                       "demak u hech narsaga bogʻliq emas, har oy shunday toʻlanadi.</p>"
                       "<p><strong>«The total bill is $45»</strong> — notoʻgʻri: jami hisob "
                       "0.12m ga ham bogʻliq va har oy oʻzgaradi.</p>",
    },
    {
        "text": "<p>In the same equation <i>C</i> = 0.12<i>m</i> + 45, which of the following "
                "is the best interpretation of the number 0.12?</p>",
        "choices": ["The bill increases by $0.12 for each kilowatt-hour used.",
                    "The customer pays $0.12 each month.",
                    "The minimum bill is $0.12.",
                    "The customer used 0.12 kilowatt-hours."],
        "correct": "The bill increases by $0.12 for each kilowatt-hour used.",
        "explanation": "<p><strong>Har bir kilovatt-soat hisobni $0.12 ga oshiradi.</strong> "
                       "0.12 soni <i>m</i> bilan turibdi, demak u «har bir birlik uchun» "
                       "degan son.</p>"
                       "<p>Qoida: harf bilan turgan son — oʻzgarish tezligi; yolgʻiz turgan "
                       "son — boshlangʻich qiymat.</p>",
    },
    {
        "text": "<p>A school sells tickets for $5 each to adults and $3 each to students. "
                "Which expression represents the total revenue, in dollars, from "
                "<i>a</i> adult tickets and <i>s</i> student tickets?</p>",
        "choices": ["5<i>a</i> + 3<i>s</i>", "5<i>s</i> + 3<i>a</i>", "8(<i>a</i> + <i>s</i>)",
                    "15<i>as</i>"],
        "correct": "5<i>a</i> + 3<i>s</i>",
        "explanation": "<p><strong>5a + 3s.</strong> Har bir narx oʻz chiptalari soniga "
                       "koʻpaytiriladi, keyin qoʻshiladi.</p>"
                       "<p><strong>8(a + s)</strong> — ikki narxni qoʻshib, hamma chiptaga "
                       "bir xil narx qoʻygan javob. Bu faqat chiptalar soni teng boʻlganda "
                       "tasodifan toʻgʻri chiqadi.</p>",
    },
    {
        "text": "<p>Maria has $250 and spends $18 each week. Which equation gives the amount "
                "of money <i>M</i>, in dollars, she has left after <i>w</i> weeks?</p>",
        "choices": ["<i>M</i> = 18<i>w</i> − 250", "<i>M</i> = 250 + 18<i>w</i>",
                    "<i>M</i> = 250 − 18<i>w</i>", "<i>M</i> = 250<i>w</i> − 18"],
        "correct": "<i>M</i> = 250 − 18<i>w</i>",
        "explanation": "<p><strong>M = 250 − 18w.</strong> $250 boshlangʻich pul, har hafta "
                       "$18 <b>kamayadi</b>.</p>"
                       "<p><strong>M = 18w − 250</strong> — ayirmani teskari yozgan javob; "
                       "u birinchi haftadayoq manfiy son beradi, bu esa maʼnosiz.</p>",
    },
    # ── 15–16 trap-spotting ──────────────────────────────────────────
    {
        "text": "<p>Twice the sum of a number and 5 is 26. What is the number?</p>",
        "choices": ["8", "10.5", "13", "16"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> «Twice the sum of a number and 5» = 2(n + 5), "
                       "demak 2(n + 5) = 26 → n + 5 = 13 → n = 8.</p>"
                       "<p><strong>10.5</strong> — 2 ni faqat n ga koʻpaytirgan javob "
                       "(2n + 5 = 26). <strong>13</strong> — n + 5 da toʻxtab qolgan javob: "
                       "u sonning oʻzi emas, yigʻindi.</p>",
    },
    {
        "text": "<p>Which expression represents «6 less than the product of 4 and <i>x</i>»?</p>",
        "choices": ["4(<i>x</i> − 6)", "4<i>x</i> − 6", "4<i>x</i> + 6", "6 − 4<i>x</i>"],
        "correct": "4<i>x</i> − 6",
        "explanation": "<p><strong>4x − 6.</strong> Avval «the product of 4 and x» = 4x, "
                       "keyin undan 6 ni ayiramiz.</p>"
                       "<p><strong>6 − 4x</strong> — <em>less than</em> ning teskari tartibi "
                       "tuzogʻi; <strong>4(x − 6)</strong> — 6 ni koʻpaytirishdan oldin "
                       "ayirgan javob.</p>",
    },
    # ── 17–18 Module 2 level ─────────────────────────────────────────
    {
        "text": "<p>A tank contains 60 liters of water. Water flows in at 5 liters per minute "
                "and drains out at 2 liters per minute. After how many minutes will the tank "
                "contain 105 liters?</p>",
        "choices": ["9", "15", "21", "35"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Har daqiqada sof oʻzgarish 5 − 2 = 3 litr. "
                       "60 + 3t = 105 → 3t = 45 → t = 15.</p>"
                       "<p><strong>9</strong> — chiqayotgan suvni hisobga olmagan javob "
                       "(45 ÷ 5). Ikki qarama-qarshi tezlik berilganda avval "
                       "<b>ayirmasini</b> toping.</p>",
    },
    {
        "text": "<p>The sum of three consecutive even integers is 90. What is the largest "
                "of the three integers?</p>",
        "choices": ["28", "30", "32", "34"],
        "correct": "32",
        "explanation": "<p><strong>32.</strong> n + (n + 2) + (n + 4) = 90 → 3n + 6 = 90 → "
                       "n = 28. Sonlar: 28, 30, 32 — eng kattasi 32.</p>"
                       "<p><strong>28</strong> — eng kichigi, <strong>30</strong> — "
                       "oʻrtadagisi. Uchalasi ham javoblar orasida turibdi: savol qaysi "
                       "birini soʻraganini oʻqing.</p>",
    },
    # ── 19–20 word problems ──────────────────────────────────────────
    {
        "text": "<p>A book club charges a $16 membership fee plus $8 for each book ordered. "
                "Nia paid $72 in total. How many books did she order?</p>",
        "choices": ["7", "9", "11", "56"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 16 + 8b = 72 → 8b = 56 → b = 7.</p>"
                       "<p><strong>9</strong> — aʼzolik toʻlovini ayirishni unutgan javob "
                       "(72 ÷ 8). <strong>56</strong> — bitta qadam yetmay toʻxtagan javob: "
                       "$56 — kitoblarga toʻlangan pul, kitoblar soni emas.</p>",
    },
    {
        "text": "<p>A car rental costs $40 per day plus a one-time insurance fee of $80. "
                "A customer paid $360 in total. For how many days was the car rented?</p>",
        "choices": ["7", "9", "11", "280"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> 40d + 80 = 360 → 40d = 280 → d = 7.</p>"
                       "<p><strong>9</strong> — sugʻurta toʻlovini ayirmagan javob "
                       "(360 ÷ 40); <strong>11</strong> — uni ayirish oʻrniga qoʻshgan "
                       "javob (440 ÷ 40). <em>one-time</em> soʻzi bitta ayirishni "
                       "buyuradi.</p>",
    },
]


# =====================================================================
# SAT-4 — absolute value equations
# =====================================================================

Q_SAT4 = [
    # ── 1–4 warm-up ──────────────────────────────────────────────────
    {
        "text": "<p>What is the value of |−12|?</p>",
        "choices": ["−12", "0", "12", "24"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Modul — noldan uzoqlik, uzoqlik esa manfiy "
                       "boʻlmaydi. −12 noldan 12 qadam narida.</p>"
                       "<p><strong>−12</strong> — modul belgisini oddiy qavs deb oʻqigan "
                       "javob. Modul ishorani <b>olib tashlaydi</b>.</p>",
    },
    {
        "text": "<p>What are all the solutions to |<i>x</i>| = 5?</p>",
        "choices": ["−5 only", "5 only", "5 and −5", "No solution"],
        "correct": "5 and −5",
        "explanation": "<p><strong>5 va −5.</strong> Noldan 5 qadam uzoqlikda ikkita son "
                       "bor: oʻngda 5, chapda −5.</p>"
                       "<p><strong>«5 only»</strong> — bitta javob bilan toʻxtash bu "
                       "mavzudagi eng koʻp uchraydigan xato. Modul bor joyda «ikkita» deb "
                       "oʻylang.</p>",
    },
    {
        "text": "<p>How many solutions does |<i>x</i> − 3| = 0 have?</p>",
        "choices": ["None", "One", "Two", "Infinitely many"],
        "correct": "One",
        "explanation": "<p><strong>Bitta.</strong> Faqat 0 noldan nol qadam uzoqlikda, "
                       "shuning uchun x − 3 = 0 va x = 3 — yagona yechim.</p>"
                       "<p><strong>«Two»</strong> — «modul bor, demak ikkita» deb avtomatik "
                       "javob bergan variant. Oʻng tomonda 0 turgani bu qoidani buzadi.</p>",
    },
    {
        "text": "<p>How many solutions does |<i>x</i>| = −2 have?</p>",
        "choices": ["None", "One", "Two", "Infinitely many"],
        "correct": "None",
        "explanation": "<p><strong>Bittasi ham yoʻq.</strong> Modul uzoqlikni bildiradi, "
                       "uzoqlik esa hech qachon manfiy boʻlmaydi.</p>"
                       "<p><strong>«Two»</strong> — hisoblab oʻtirgan javob: 2 va −2. "
                       "Bu savolda umuman hisoblash kerak emas, faqat oʻng tomonning "
                       "ishorasiga qarash kerak.</p>",
    },
    # ── 5–10 exam shape ──────────────────────────────────────────────
    {
        "text": "<p>If |<i>x</i> + 4| = 9, what is the positive value of <i>x</i>?</p>",
        "choices": ["−13", "5", "9", "13"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> x + 4 = 9 → x = 5; x + 4 = −9 → x = −13. "
                       "Savol musbat qiymatni soʻradi.</p>"
                       "<p><strong>13</strong> — 9 + 4 hisoblangan javob: qoʻshiluvchi "
                       "4 ni <b>ayirish</b> kerak, chunki u chap tomonda qoʻshilyapti.</p>",
    },
    {
        "text": "<p>If |2<i>x</i>| = 14, what is the negative value of <i>x</i>?</p>",
        "choices": ["−14", "−7", "7", "14"],
        "correct": "−7",
        "explanation": "<p><strong>−7.</strong> 2x = 14 → x = 7; 2x = −14 → x = −7.</p>"
                       "<p><strong>−14</strong> — 2 ga boʻlishni unutgan javob. Modulni "
                       "ochgandan keyin ham oddiy tenglama qoladi va uni oxirigacha yechish "
                       "kerak.</p>",
    },
    {
        "text": "<p>Which of the following is a solution to |<i>x</i> − 6| = 2?</p>",
        "choices": ["2", "3", "8", "12"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> x − 6 = 2 → x = 8; x − 6 = −2 → x = 4. "
                       "Javoblar orasida 8 bor, 4 yoʻq.</p>"
                       "<p><strong>2</strong> — oʻng tomondagi sonni javob deb belgilagan "
                       "variant; <strong>12</strong> — 6 × 2 hisoblangan javob.</p>",
    },
    {
        "text": "<p>If |3<i>x</i> − 6| = 9, what is the positive value of <i>x</i>?</p>",
        "choices": ["−1", "1", "5", "15"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 3x − 6 = 9 → 3x = 15 → x = 5; "
                       "3x − 6 = −9 → 3x = −3 → x = −1.</p>"
                       "<p><strong>15</strong> — bitta qadam yetmay toʻxtagan javob "
                       "(3x = 15). <strong>1</strong> — ikkinchi holda ishorani "
                       "adashtirgan javob.</p>",
    },
    {
        "text": "<p>If 2|<i>x</i>| = 18, what is the sum of all possible values "
                "of <i>x</i>?</p>",
        "choices": ["0", "9", "18", "36"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> |x| = 9, demak x = 9 yoki x = −9, "
                       "va 9 + (−9) = 0.</p>"
                       "<p><strong>18</strong> — ikkala yechimni ham musbat deb qoʻshgan "
                       "javob. Yechimlar noldan bir xil uzoqlikda, lekin qarama-qarshi "
                       "tomonda.</p>",
    },
    {
        "text": "<p>If |<i>x</i> + 2| = 7, what is the sum of all possible values "
                "of <i>x</i>?</p>",
        "choices": ["−9", "−4", "5", "14"],
        "correct": "−4",
        "explanation": "<p><strong>−4.</strong> x = 5 yoki x = −9, va 5 + (−9) = −4.</p>"
                       "<p>Tez yoʻl: |x − a| = b da yechimlar yigʻindisi har doim 2a. "
                       "Bu yerda ifoda x + 2, yaʼni a = −2, demak yigʻindi 2 × (−2) = −4.</p>",
    },
    # ── 11–14 context & interpretation ───────────────────────────────
    {
        "text": "<p>A machine cuts rods to a target length of 40 cm. A rod is at the limit of "
                "acceptability when |<i>L</i> − 40| = 0.5, where <i>L</i> is its length in "
                "centimeters. What are the two limit lengths?</p>",
        "choices": ["0.5 cm and 40 cm", "39.5 cm and 40.5 cm",
                    "39.5 cm and 40 cm", "40 cm and 80 cm"],
        "correct": "39.5 cm and 40.5 cm",
        "explanation": "<p><strong>39.5 va 40.5 cm.</strong> L − 40 = 0.5 → L = 40.5; "
                       "L − 40 = −0.5 → L = 39.5.</p>"
                       "<p>Modul amaliy masalada deyarli har doim «meʼyordan chetlanish» "
                       "maʼnosini beradi: 40 — meʼyor, 0.5 — ruxsat etilgan chetlanish.</p>",
    },
    {
        "text": "<p>A thermostat is described by the equation |<i>T</i> − 20| = 3, where "
                "<i>T</i> is the temperature in degrees Celsius. Which of the following is "
                "the best interpretation of the number 20?</p>",
        "choices": ["The largest allowed temperature",
                    "The smallest allowed temperature",
                    "The target temperature",
                    "The size of the allowed change"],
        "correct": "The target temperature",
        "explanation": "<p><strong>Moʻljaldagi harorat.</strong> Modul ichidan ayriladigan "
                       "son — bu <b>markaz</b>: ikkala yechim ham undan bir xil uzoqlikda "
                       "turadi.</p>"
                       "<p><strong>«The size of the allowed change»</strong> — bu 3, "
                       "20 emas. Ichidagi son markazni, oʻng tomondagi son uzoqlikni "
                       "bildiradi.</p>",
    },
    {
        "text": "<p>Which equation states that the distance between <i>x</i> and 7 is 4?</p>",
        "choices": ["|7 − 4| = <i>x</i>", "|<i>x</i> − 4| = 7", "|<i>x</i> − 7| = 4",
                    "|<i>x</i> + 7| = 4"],
        "correct": "|<i>x</i> − 7| = 4",
        "explanation": "<p><strong>|x − 7| = 4.</strong> «Distance between x and 7» — "
                       "ikkisining ayirmasining moduli; «is 4» esa oʻng tomon.</p>"
                       "<p><strong>|x − 4| = 7</strong> — ikki sonni almashtirib yuborgan "
                       "javob. SAT modulni koʻpincha belgisiz, faqat <em>distance</em> "
                       "soʻzi bilan soʻraydi.</p>",
    },
    {
        "text": "<p>The equation |<i>x</i> − 5| = 3 has two solutions. Both solutions are "
                "the same distance from which number?</p>",
        "choices": ["3", "4", "5", "8"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Yechimlar 2 va 8; ikkalasi ham 5 dan 3 qadam "
                       "narida. Modul ichidan ayriladigan son har doim markaz.</p>"
                       "<p><strong>3</strong> — uzoqlik, markaz emas; <strong>8</strong> — "
                       "yechimlardan biri.</p>",
    },
    # ── 15–16 trap-spotting ──────────────────────────────────────────
    {
        "text": "<p>If |2<i>x</i> − 5| = 11, what is the negative value of <i>x</i>?</p>",
        "choices": ["−8", "−3", "3", "8"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> 2x − 5 = −11 → 2x = −6 → x = −3.</p>"
                       "<p><strong>8</strong> — musbat yechim, u ham toʻgʻri hisoblangan, "
                       "lekin savol <b>manfiy</b>ini soʻradi. Ikki yechimli savolda oxirgi "
                       "soʻz eng muhim soʻz.</p>",
    },
    {
        "text": "<p>How many solutions does |<i>x</i> + 1| = 0 have?</p>",
        "choices": ["None", "One", "Two", "Infinitely many"],
        "correct": "One",
        "explanation": "<p><strong>Bitta.</strong> x + 1 = 0 → x = −1. Nolga teng modul "
                       "faqat bitta yechim beradi.</p>"
                       "<p><strong>«None»</strong> — oʻng tomonda 0 ni koʻrib, «manfiy "
                       "boʻlsa yechim yoʻq» qoidasini notoʻgʻri qoʻllagan javob. "
                       "0 manfiy emas.</p>",
    },
    # ── 17–18 Module 2 level ─────────────────────────────────────────
    {
        "text": "<p>If 3|<i>x</i> − 2| = 12, what is the sum of all possible values "
                "of <i>x</i>?</p>",
        "choices": ["4", "6", "8", "12"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Avval izolyatsiya: |x − 2| = 4. Keyin x = 6 "
                       "yoki x = −2, va 6 + (−2) = 4.</p>"
                       "<p><strong>6</strong> — faqat bitta yechim; <strong>8</strong> — "
                       "2 × 4 hisoblangan javob (markaz 2, uzoqlik 4 — yigʻindi 2 × markaz "
                       "= 4).</p>",
    },
    {
        "text": "<p>If 4|<i>x</i> + 3| − 5 = 7, what is the sum of all possible values "
                "of <i>x</i>?</p>",
        "choices": ["−6", "−3", "0", "3"],
        "correct": "−6",
        "explanation": "<p><strong>−6.</strong> 4|x + 3| = 12 → |x + 3| = 3 → x = 0 yoki "
                       "x = −6, va 0 + (−6) = −6.</p>"
                       "<p><strong>0</strong> — yechimlardan biri; <strong>−3</strong> — "
                       "markaz. Modulni <b>butunlay</b> yolgʻiz qoldirmasdan ikkiga "
                       "ajratish bu savoldagi asosiy xato.</p>",
    },
    # ── 19–20 word problems ──────────────────────────────────────────
    {
        "text": "<p>A thermostat is set to 68°F. The system switches on or off when the "
                "temperature differs from 68°F by exactly 4 degrees. At which two "
                "temperatures does the system switch?</p>",
        "choices": ["4°F and 68°F", "64°F and 68°F", "64°F and 72°F", "68°F and 72°F"],
        "correct": "64°F and 72°F",
        "explanation": "<p><strong>64°F va 72°F.</strong> |T − 68| = 4 → T = 72 yoki "
                       "T = 64.</p>"
                       "<p><strong>«64 va 68»</strong> — faqat bir tomonga qaragan javob. "
                       "«Differs by» ikkala tomonni ham bildiradi: yuqoriga ham, pastga "
                       "ham.</p>",
    },
    {
        "text": "<p>Along a straight highway, a destination is exactly 12 miles from mile "
                "marker 30. Which two mile markers could be the destination?</p>",
        "choices": ["12 and 30", "18 and 30", "18 and 42", "30 and 42"],
        "correct": "18 and 42",
        "explanation": "<p><strong>18 va 42.</strong> |m − 30| = 12 → m = 42 yoki "
                       "m = 18.</p>"
                       "<p><strong>«30 va 42»</strong> — faqat oldinga yurgan javob. "
                       "Yoʻl ikki tomonga ketadi, shuning uchun ikkala nuqta ham "
                       "hisobga olinadi.</p>",
    },
]


# =====================================================================
# SAT-5 — the concept of slope
# =====================================================================

Q_SAT5 = [
    # ── 1–4 warm-up ──────────────────────────────────────────────────
    {
        "text": "<p>What is the slope of the line that passes through (0, 0) and (3, 6)?</p>",
        "choices": ["1/2", "2", "3", "6"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> rise = 6 − 0 = 6, run = 3 − 0 = 3, "
                       "m = 6 ÷ 3 = 2.</p>"
                       "<p><strong>1/2</strong> — nisbat teskari olingan (run ÷ rise). "
                       "Ustida har doim <b>y</b> lar turadi.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (1, 4) and (3, 10)?</p>",
        "choices": ["1/3", "2", "3", "6"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> rise = 10 − 4 = 6, run = 3 − 1 = 2, "
                       "m = 6 ÷ 2 = 3.</p>"
                       "<p><strong>6</strong> — faqat rise hisoblangan, run ga boʻlinmagan "
                       "javob. Qiyalik — koʻtarilishning oʻzi emas, uning nisbati.</p>",
    },
    {
        "text": "<p>What is the slope of a horizontal line?</p>",
        "choices": ["−1", "0", "1", "Undefined"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Gorizontal chiziqda <i>y</i> umuman "
                       "oʻzgarmaydi, demak rise = 0 va 0 ÷ run = 0.</p>"
                       "<p><strong>Undefined</strong> — vertikal chiziqniki. Nol — «tekis "
                       "yoʻl», undefined — «devor».</p>",
    },
    {
        "text": "<p>What is the slope of a vertical line?</p>",
        "choices": ["−1", "0", "1", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined (aniqlanmagan).</strong> Vertikal chiziqda "
                       "run = 0, nolga boʻlish esa aniqlanmagan.</p>"
                       "<p><strong>0</strong> — gorizontal chiziqniki. Bu ikkisi doim "
                       "adashtiriladi, shuning uchun SAT ularni bitta savolning javoblari "
                       "qilib qoʻyadi.</p>",
    },
    # ── 5–10 exam shape ──────────────────────────────────────────────
    {
        "text": "<p>What is the slope of the line that passes through (2, 5) and (6, 1)?</p>",
        "choices": ["−1", "−1/4", "1/4", "1"],
        "correct": "−1",
        "explanation": "<p><strong>−1.</strong> rise = 1 − 5 = −4, run = 6 − 2 = 4, "
                       "m = −4 ÷ 4 = −1.</p>"
                       "<p><strong>1</strong> — ishorani tashlab ketgan javob. <i>y</i> "
                       "kamayganda qiyalik manfiy boʻladi — chiziq oʻngga qarab "
                       "pasayadi.</p>",
    },
    {
        "text": "<p>What is the slope of the line <i>y</i> = 4<i>x</i> + 7?</p>",
        "choices": ["1/4", "4", "7", "11"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> <i>y</i> = <i>mx</i> + <i>b</i> koʻrinishida "
                       "qiyalik — <i>x</i> oldidagi son.</p>"
                       "<p><strong>7</strong> — bu <i>b</i>, chiziqning <i>y</i> oʻqini "
                       "kesib oʻtish nuqtasi (SAT-7). Qiyalik har doim harf bilan "
                       "turadi.</p>",
    },
    {
        "text": "<p>A table shows a linear relationship: when <i>x</i> is 1, 2, 3, "
                "<i>y</i> is 10, 7, 4. What is the slope?</p>",
        "choices": ["−3", "−1/3", "1/3", "3"],
        "correct": "−3",
        "explanation": "<p><strong>−3.</strong> <i>x</i> har safar 1 ga ortganda <i>y</i> "
                       "3 ga kamayadi: −3 ÷ 1 = −3.</p>"
                       "<p><strong>3</strong> — ishorani unutgan javob. Jadvalda <i>y</i> "
                       "kamayib borsa, qiyalik albatta manfiy.</p>",
    },
    {
        "text": "<p>Which of the following lines has the greatest slope?</p>",
        "choices": ["<i>y</i> = −7<i>x</i>", "<i>y</i> = 0.5<i>x</i> + 9",
                    "<i>y</i> = 2<i>x</i> + 1", "<i>y</i> = 5<i>x</i> − 3"],
        "correct": "<i>y</i> = 5<i>x</i> − 3",
        "explanation": "<p><strong>y = 5x − 3.</strong> Qiyaliklar: −7, 0.5, 2, 5. Eng "
                       "kattasi — 5.</p>"
                       "<p><strong>y = −7x</strong> — eng <b>tik</b> chiziq, lekin qiyaligi "
                       "−7, yaʼni eng <b>kichigi</b>. «Greatest slope» — eng katta son, eng "
                       "tik chiziq emas.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (−2, 1) and (2, 9)?</p>",
        "choices": ["1/2", "2", "4", "8"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> rise = 9 − 1 = 8, run = 2 − (−2) = 4, "
                       "m = 8 ÷ 4 = 2.</p>"
                       "<p><strong>4</strong> — run ni 2 − 2 = 0 emas, 4 emas deb "
                       "adashgan javob: manfiy sondan ayirganda qoʻshiladi, "
                       "2 − (−2) = 4.</p>",
    },
    {
        "text": "<p>A line passes through the point (3, 7) and has a slope of 0. "
                "What is the value of <i>y</i> when <i>x</i> = 10?</p>",
        "choices": ["0", "3", "7", "10"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Qiyaligi 0 boʻlgan chiziq gorizontal — "
                       "<i>y</i> hech qachon oʻzgarmaydi, demak u har doim 7.</p>"
                       "<p><strong>0</strong> — qiyalikning oʻzini javob deb belgilagan "
                       "variant. Qiyalik 0 boʻlishi <i>y</i> = 0 degani emas.</p>",
    },
    # ── 11–14 context & interpretation ───────────────────────────────
    {
        "text": "<p>The cost <i>C</i>, in dollars, of renting a car for <i>m</i> miles is "
                "<i>C</i> = 25 + 0.15<i>m</i>. Which of the following is the best "
                "interpretation of 0.15?</p>",
        "choices": ["The rental costs $0.15 in total.",
                    "The cost increases by $0.15 for each mile driven.",
                    "The car can be driven 0.15 miles.",
                    "The initial rental fee is $0.15."],
        "correct": "The cost increases by $0.15 for each mile driven.",
        "explanation": "<p><strong>Har bir mil narxni $0.15 ga oshiradi.</strong> 0.15 soni "
                       "<i>m</i> bilan turibdi — demak u qiyalik, «har bir mil uchun».</p>"
                       "<p><strong>«The initial rental fee»</strong> — bu 25: boshlangʻich "
                       "qiymat har doim harfsiz turadi.</p>",
    },
    {
        "text": "<p>A person's weight, in pounds, after <i>t</i> weeks of training is given "
                "by <i>W</i> = 150 − 2<i>t</i>. Which of the following is the best "
                "interpretation of −2?</p>",
        "choices": ["The person loses 2 pounds each week.",
                    "The person weighs 2 pounds.",
                    "The person trained for 2 weeks.",
                    "The person's starting weight was 2 pounds."],
        "correct": "The person loses 2 pounds each week.",
        "explanation": "<p><strong>Har hafta 2 funt kamayadi.</strong> Manfiy qiyalik — "
                       "kamayish; 2 esa har haftadagi oʻzgarish miqdori.</p>"
                       "<p>Boshlangʻich ogʻirlik 150 — u yolgʻiz turgan son. Bu ikkisining "
                       "vazifasini adashtirmang.</p>",
    },
    {
        "text": "<p>On the same graph, the line showing Ann's savings is steeper than the "
                "line showing Bo's savings. Which statement must be true?</p>",
        "choices": ["Ann started with more money than Bo.",
                    "Ann saves money at a faster rate than Bo.",
                    "Ann has saved more money in total than Bo.",
                    "Ann saved for more weeks than Bo."],
        "correct": "Ann saves money at a faster rate than Bo.",
        "explanation": "<p><strong>Ann tezroq jamgʻaradi.</strong> Tiklik — qiyalik, "
                       "qiyalik esa oʻzgarish <b>tezligi</b>.</p>"
                       "<p><strong>«Started with more money»</strong> — bu boshlangʻich "
                       "qiymat, u chiziqning <b>qayerdan</b> boshlanishi bilan bogʻliq, "
                       "tikligi bilan emas.</p>",
    },
    {
        "text": "<p>A candle burns at a constant rate. Its height is 20 cm at 0 minutes and "
                "14 cm at 3 minutes. What is the rate of change of the height, in "
                "centimeters per minute?</p>",
        "choices": ["−6", "−2", "2", "6"],
        "correct": "−2",
        "explanation": "<p><strong>−2.</strong> (14 − 20) ÷ (3 − 0) = −6 ÷ 3 = −2, "
                       "yaʼni har daqiqada 2 cm kamayadi.</p>"
                       "<p><strong>−6</strong> — faqat balandlikning oʻzgarishi, uni "
                       "vaqtga boʻlish kerak. «Per minute» soʻzi boʻlishni buyuradi.</p>",
    },
    # ── 15–16 trap-spotting ──────────────────────────────────────────
    {
        "text": "<p>What is the slope of the line that passes through (2, 3) and (5, 3)?</p>",
        "choices": ["0", "1", "3", "Undefined"],
        "correct": "0",
        "explanation": "<p><strong>0.</strong> Ikkala nuqtaning <i>y</i> qiymati bir xil, "
                       "demak rise = 0 va chiziq gorizontal.</p>"
                       "<p><strong>Undefined</strong> — <i>x</i> lar bir xil boʻlganda "
                       "boʻladi, <i>y</i> lar emas. Qaysi koordinata takrorlanayotganiga "
                       "diqqat qiling.</p>",
    },
    {
        "text": "<p>What is the slope of the line that passes through (4, 1) and (4, 7)?</p>",
        "choices": ["0", "1", "6", "Undefined"],
        "correct": "Undefined",
        "explanation": "<p><strong>Undefined.</strong> run = 4 − 4 = 0, nolga boʻlish esa "
                       "aniqlanmagan — chiziq vertikal.</p>"
                       "<p><strong>6</strong> — rise ning oʻzi (7 − 1), lekin uni 0 ga "
                       "boʻlib boʻlmaydi. Bir oldingi savol bilan solishtiring: u yerda "
                       "<i>y</i> lar, bu yerda <i>x</i> lar bir xil edi.</p>",
    },
    # ── 17–18 Module 2 level ─────────────────────────────────────────
    {
        "text": "<p>A line passes through the points (1, 2) and (5, <i>k</i>), and its slope "
                "is 3. What is the value of <i>k</i>?</p>",
        "choices": ["12", "14", "15", "17"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> run = 5 − 1 = 4, qiyalik 3 boʻlgani uchun "
                       "rise = 3 × 4 = 12, demak k = 2 + 12 = 14.</p>"
                       "<p><strong>12</strong> — koʻtarilishning oʻzi, boshlangʻich "
                       "<i>y</i> = 2 ga qoʻshilmagan. <strong>17</strong> — run ni 5 deb "
                       "olgan javob (1 dan boshlanishini unutgan).</p>",
    },
    {
        "text": "<p>A linear function <i>f</i> satisfies <i>f</i>(2) = 5 and "
                "<i>f</i>(6) = 17. What is the rate of change of <i>f</i>?</p>",
        "choices": ["1/3", "3", "4", "12"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> (17 − 5) ÷ (6 − 2) = 12 ÷ 4 = 3. "
                       "<em>Rate of change</em> — qiyalikning boshqa nomi.</p>"
                       "<p><strong>12</strong> — faqat <i>y</i> ning oʻzgarishi; "
                       "<strong>4</strong> — faqat <i>x</i> ning oʻzgarishi. Javob "
                       "ularning nisbati.</p>",
    },
    # ── 19–20 word problems ──────────────────────────────────────────
    {
        "text": "<p>A pool is filled at a constant rate. After 2 hours it contains 300 liters, "
                "and after 5 hours it contains 750 liters. How many liters are added "
                "each hour?</p>",
        "choices": ["90", "150", "250", "450"],
        "correct": "150",
        "explanation": "<p><strong>150.</strong> (750 − 300) ÷ (5 − 2) = 450 ÷ 3 = 150.</p>"
                       "<p><strong>450</strong> — faqat hajmning oʻzgarishi, vaqtga "
                       "boʻlinmagan; <strong>250</strong> — 750 ni 3 ga boʻlgan javob, "
                       "lekin 750 litr 5 soatda yigʻilgan, 3 soatda emas.</p>",
    },
    {
        "text": "<p>A delivery service charges a fixed fee plus an amount per mile. A 4-mile "
                "delivery costs $14 and a 10-mile delivery costs $26. What is the charge "
                "per mile?</p>",
        "choices": ["$2.00", "$2.60", "$3.50", "$12.00"],
        "correct": "$2.00",
        "explanation": "<p><strong>$2.00.</strong> (26 − 14) ÷ (10 − 4) = 12 ÷ 6 = 2 — bu "
                       "qiyalik, yaʼni har bir mil uchun toʻlov.</p>"
                       "<p><strong>$3.50</strong> — 14 ÷ 4: bu butun narxni masofaga "
                       "boʻlish, lekin narx ichida bir martalik toʻlov ham bor. Shuning "
                       "uchun har doim <b>ikki nuqtaning ayirmasi</b> olinadi.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-1 Practice: Introduction to the Variable and Combining Like Terms",
        "description": "20 ta SAT uslubidagi savol — had va koeffitsient, oʻxshash hadlar, "
                       "qavs ochish va qavs oldidagi minus.",
        "tutorial":    "SAT-1:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT1,
    },
    {
        "title":       "SAT-2 Practice: Solving Single-Variable Linear Equations",
        "description": "20 ta SAT uslubidagi savol — teskari amallar, ikki tomonda x, "
                       "kasrli tenglama, yechimsiz va cheksiz koʻp yechimli hollar.",
        "tutorial":    "SAT-2:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT2,
    },
    {
        "title":       "SAT-3 Practice: Setting Up Linear Equations from Word Problems",
        "description": "20 ta SAT uslubidagi savol — inglizcha iborani tenglamaga "
                       "aylantirish, «less than» tuzogʻi, boshlangʻich toʻlov modeli.",
        "tutorial":    "SAT-3:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT3,
    },
    {
        "title":       "SAT-4 Practice: Understanding Absolute Value Equations",
        "description": "20 ta SAT uslubidagi savol — modulni ikkiga ajratish, izolyatsiya, "
                       "yechimlar yigʻindisi va yechimsiz hol.",
        "tutorial":    "SAT-4:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT4,
    },
    {
        "title":       "SAT-5 Practice: The Concept of Slope: Steepness and Direction",
        "description": "20 ta SAT uslubidagi savol — rise ÷ run, ishora va yoʻnalish, "
                       "jadvaldan qiyalik va kontekstdagi maʼnosi.",
        "tutorial":    "SAT-5:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT5,
    },
]
