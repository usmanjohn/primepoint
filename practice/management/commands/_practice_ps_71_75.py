# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-71 … SAT-75.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_71_75.py --master=prime \\
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
# SAT-71 — 45-45-90
# =====================================================================

Q_SAT71 = [
    {
        "text": "<p>A 45-45-90 triangle has legs of 9. What is the hypotenuse?</p>",
        "choices": ["9√2", "18", "9√3", "9 ÷ √2"],
        "correct": "9√2",
        "explanation": "<p><strong>9√2.</strong> Nisbat x : x : x√2.</p>"
                       "<p><strong>18</strong> — katetlar qoʻshilgan.</p>",
    },
    {
        "text": "<p>A 45-45-90 triangle has a hypotenuse of 8√2. What is each leg?</p>",
        "choices": ["8", "16", "4√2", "8√2"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Gipotenuza √2 ga boʻlinadi.</p>",
    },
    {
        "text": "<p>A square has sides of 7. What is the length of its diagonal?</p>",
        "choices": ["7√2", "14", "7√3", "49"],
        "correct": "7√2",
        "explanation": "<p><strong>7√2.</strong> Diagonal kvadratni ikkita "
                       "45-45-90 ga boʻladi.</p>",
    },
    {
        "text": "<p>A square has a diagonal of 12. What is the length of each side?</p>",
        "choices": ["6√2", "12√2", "6", "24"],
        "correct": "6√2",
        "explanation": "<p><strong>6√2.</strong> 12 ÷ √2, maxrajni "
                       "tozalagandan keyin.</p>"
                       "<p><strong>12√2</strong> — koʻpaytirilgan; tomon "
                       "diagonaldan qisqa boʻlishi kerak.</p>",
    },
    {
        "text": "<p>What are the two acute angles in an isosceles right triangle?</p>",
        "choices": ["45° each", "30° and 60°", "45° and 90°", "They vary"],
        "correct": "45° each",
        "explanation": "<p><strong>45° dan.</strong> Katetlar teng, demak "
                       "burchaklar teng; 180 − 90 ni ikkiga boʻling.</p>",
    },
    {
        "text": "<p>A 45-45-90 triangle has legs of 6. What is its area?</p>",
        "choices": ["18", "36", "18√2", "12"],
        "correct": "18",
        "explanation": "<p><strong>18.</strong> Katetlar asos va balandlik: "
                       "6 × 6 ÷ 2.</p>"
                       "<p>Gipotenuza yuzaga kirmaydi.</p>",
    },
    {
        "text": "<p>A square has a diagonal of 10. What is its area?</p>",
        "choices": ["50", "100", "25√2", "70.7"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> Tomoni 10 ÷ √2 = 5√2, va "
                       "uning kvadrati 50.</p>"
                       "<p>Tez yoʻl: kvadrat yuzasi diagonal kvadratining "
                       "yarmi.</p>",
    },
    {
        "text": "<p>A 45-45-90 triangle has legs of 5. What is its perimeter?</p>",
        "choices": ["10 + 5√2", "15", "5 + 5√2", "10√2"],
        "correct": "10 + 5√2",
        "explanation": "<p><strong>10 + 5√2.</strong> Ikki katet va "
                       "gipotenuza.</p>"
                       "<p>Taxminan 17.07.</p>",
    },
    {
        "text": "<p>Approximately how much longer is the hypotenuse than a leg in a "
                "45-45-90 triangle?</p>",
        "choices": ["About 1.41 times", "About 1.73 times", "Twice", "About 1.15 times"],
        "correct": "About 1.41 times",
        "explanation": "<p><strong>Taxminan 1.41 barobar.</strong> √2 ≈ "
                       "1.414.</p>"
                       "<p><strong>1.73</strong> — bu √3, 30-60-90 niki.</p>",
    },
    {
        "text": "<p>Does every rectangle's diagonal create a 45-45-90 triangle?</p>",
        "choices": ["No — only if the rectangle is a square",
                    "Yes, always", "Yes, if the diagonal is long enough",
                    "No, never"],
        "correct": "No — only if the rectangle is a square",
        "explanation": "<p><strong>Faqat kvadratda.</strong> Katetlar teng "
                       "boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A 45-45-90 triangle has a hypotenuse of 10. What is its area?</p>",
        "choices": ["25", "50", "25√2", "100"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Katet 10 ÷ √2 = 5√2, va yuza "
                       "(5√2)(5√2) ÷ 2 = 50 ÷ 2.</p>",
    },
    {
        "text": "<p>A square tile has a diagonal of 6√2 centimetres. What is its "
                "perimeter?</p>",
        "choices": ["24 cm", "24√2 cm", "6 cm", "36 cm"],
        "correct": "24 cm",
        "explanation": "<p><strong>24 sm.</strong> Tomoni 6, va perimetr "
                       "4 × 6.</p>",
    },
    {
        "text": "<p>Where is the 45-45-90 triangle hidden in a square?</p>",
        "choices": ["The diagonal creates two of them",
                    "The sides form one",
                    "It is not present",
                    "Only in a square with side 1"],
        "correct": "The diagonal creates two of them",
        "explanation": "<p><strong>Diagonal ikkitasini hosil qiladi.</strong> "
                       "Ikkala tomon katet boʻlib qoladi.</p>",
    },
    {
        "text": "<p>A right triangle has legs of 4 and 4. What is the measure of its "
                "smallest angle?</p>",
        "choices": ["45°", "30°", "60°", "90°"],
        "correct": "45°",
        "explanation": "<p><strong>45°.</strong> Ikki oʻtkir burchak teng, va "
                       "ikkalasi ham 90 dan kichik.</p>",
    },
    {
        "text": "<p>A student says a 45-45-90 triangle with legs of 7 has a hypotenuse "
                "of 14. What is correct?</p>",
        "choices": ["7√2", "14", "7√3", "49"],
        "correct": "7√2",
        "explanation": "<p><strong>7√2 ≈ 9.9.</strong> Gipotenuza katetlar "
                       "yigʻindisidan kichik boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A student converts a diagonal of 8 into a side by multiplying by √2. "
                "What is the correct side?</p>",
        "choices": ["4√2", "8√2", "8", "16"],
        "correct": "4√2",
        "explanation": "<p><strong>4√2.</strong> Gipotenuzadan katetga "
                       "<b>boʻlinadi</b>.</p>"
                       "<p>Oʻquvchining javobi diagonaldan uzun chiqadi — "
                       "mantiqan imkonsiz.</p>",
    },
    {
        "text": "<p>Two squares have sides 3 and 6. What is the ratio of their "
                "diagonals?</p>",
        "choices": ["1 to 2", "1 to 4", "1 to √2", "1 to 2√2"],
        "correct": "1 to 2",
        "explanation": "<p><strong>1 dan 2 gacha.</strong> Diagonal uzunlik — "
                       "u masshtab bilan chiziqli oʻzgaradi (SAT-74).</p>",
    },
    {
        "text": "<p>A 45-45-90 triangle has an area of 32. What is the length of each "
                "leg?</p>",
        "choices": ["8", "16", "8√2", "4"],
        "correct": "8",
        "explanation": "<p><strong>8.</strong> Yuza katet kvadratining yarmi: "
                       "x² ÷ 2 = 32 → x² = 64.</p>",
    },
    {
        "text": "<p>A square courtyard measures 20 metres on each side. How much shorter "
                "is the diagonal walk than going round two sides?</p>",
        "choices": ["About 11.7 metres", "About 8.3 metres", "20 metres",
                    "About 28.3 metres"],
        "correct": "About 11.7 metres",
        "explanation": "<p><strong>Taxminan 11.7 metr.</strong> Diagonal "
                       "20√2 ≈ 28.3, ikki tomon 40, farqi 11.7.</p>",
    },
    {
        "text": "<p>A square picture frame has a diagonal brace of 30 centimetres. What "
                "is the area of the frame?</p>",
        "choices": ["450 square cm", "900 square cm", "225 square cm",
                    "450√2 square cm"],
        "correct": "450 square cm",
        "explanation": "<p><strong>450 kv. sm.</strong> Tomoni 30 ÷ √2, va "
                       "yuza uning kvadrati: 900 ÷ 2.</p>"
                       "<p>Tez yoʻl: diagonal kvadratining yarmi.</p>",
    },
]


# =====================================================================
# SAT-72 — 30-60-90
# =====================================================================

Q_SAT72 = [
    {
        "text": "<p>In a 30-60-90 triangle, the short leg is 5. What is the "
                "hypotenuse?</p>",
        "choices": ["10", "5√3", "5√2", "2.5"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> Gipotenuza qisqa katetning ikki "
                       "barobari.</p>",
    },
    {
        "text": "<p>In a 30-60-90 triangle, the short leg is 5. What is the long "
                "leg?</p>",
        "choices": ["5√3", "10", "5√2", "15"],
        "correct": "5√3",
        "explanation": "<p><strong>5√3.</strong> Uzun katet 60° ga qarshi "
                       "turadi.</p>",
    },
    {
        "text": "<p>The hypotenuse of a 30-60-90 triangle is 18. What is the short "
                "leg?</p>",
        "choices": ["9", "36", "9√3", "6"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Gipotenuza ikkiga boʻlinadi.</p>",
    },
    {
        "text": "<p>The long leg of a 30-60-90 triangle is 7√3. What is the short "
                "leg?</p>",
        "choices": ["7", "7√3", "14", "21"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> Uzun katet √3 ga boʻlinadi.</p>",
    },
    {
        "text": "<p>An equilateral triangle has sides of 10. What is its altitude?</p>",
        "choices": ["5√3", "10√3", "5", "5√2"],
        "correct": "5√3",
        "explanation": "<p><strong>5√3.</strong> Balandlik ikkita 30-60-90 "
                       "hosil qiladi; gipotenuza 10, demak x = 5.</p>",
    },
    {
        "text": "<p>An equilateral triangle has sides of 6. What is its area?</p>",
        "choices": ["9√3", "18√3", "9", "36"],
        "correct": "9√3",
        "explanation": "<p><strong>9√3.</strong> Balandlik 3√3, va yuza "
                       "6 × 3√3 ÷ 2.</p>",
    },
    {
        "text": "<p>Which side of a 30-60-90 triangle is opposite the 60° angle?</p>",
        "choices": ["The long leg", "The short leg", "The hypotenuse",
                    "It depends on the drawing"],
        "correct": "The long leg",
        "explanation": "<p><strong>Uzun katet.</strong> Katta burchakka uzunroq "
                       "tomon qarshi turadi.</p>",
    },
    {
        "text": "<p>Approximately how much longer is the long leg than the short leg in "
                "a 30-60-90 triangle?</p>",
        "choices": ["About 1.73 times", "About 1.41 times", "Twice",
                    "About 2.24 times"],
        "correct": "About 1.73 times",
        "explanation": "<p><strong>Taxminan 1.73 barobar.</strong> √3 ≈ "
                       "1.732.</p>"
                       "<p><strong>1.41</strong> — bu √2, boshqa maxsus "
                       "uchburchakniki.</p>",
    },
    {
        "text": "<p>In a 30-60-90 triangle the short leg is 3. What is its area?</p>",
        "choices": ["4.5√3", "9√3", "3√3", "9"],
        "correct": "4.5√3",
        "explanation": "<p><strong>4.5√3.</strong> Katetlar 3 va 3√3, va yuza "
                       "ularning koʻpaytmasining yarmi.</p>",
    },
    {
        "text": "<p>A 30-60-90 triangle has a hypotenuse of 20. What is its perimeter?</p>",
        "choices": ["30 + 10√3", "20 + 10√3", "30√3", "40"],
        "correct": "30 + 10√3",
        "explanation": "<p><strong>30 + 10√3.</strong> Tomonlar 10, 10√3 va "
                       "20.</p>"
                       "<p>Taxminan 47.32.</p>",
    },
    {
        "text": "<p>Where does the 30-60-90 triangle come from?</p>",
        "choices": ["Half of an equilateral triangle",
                    "Half of a square",
                    "A quarter of a circle",
                    "It has no simple source"],
        "correct": "Half of an equilateral triangle",
        "explanation": "<p><strong>Teng tomonli uchburchakning yarmi.</strong> "
                       "Balandlik uni ikkiga boʻladi.</p>",
    },
    {
        "text": "<p>In a 30-60-90 triangle, which is longer: the side opposite 60° or the "
                "hypotenuse?</p>",
        "choices": ["The hypotenuse", "The side opposite 60°", "They are equal",
                    "It depends on the size"],
        "correct": "The hypotenuse",
        "explanation": "<p><strong>Gipotenuza.</strong> 2 va √3 ≈ 1.73 ni "
                       "solishtiring.</p>"
                       "<p>Gipotenuza har doim eng uzun tomon.</p>",
    },
    {
        "text": "<p>An equilateral triangle has an altitude of 9. What is the length of "
                "each side?</p>",
        "choices": ["6√3", "9√3", "18", "4.5"],
        "correct": "6√3",
        "explanation": "<p><strong>6√3.</strong> Balandlik uzun katet: "
                       "x√3 = 9 → x = 3√3, va tomon 2x.</p>"
                       "<p>Taxminan 10.39.</p>",
    },
    {
        "text": "<p>In a 30-60-90 triangle, the short leg is <i>a</i>. What is the "
                "perimeter in terms of <i>a</i>?</p>",
        "choices": ["3a + a√3", "2a + a√3", "a + a√3", "6a"],
        "correct": "3a + a√3",
        "explanation": "<p><strong>3a + a√3.</strong> a + a√3 + 2a.</p>",
    },
    {
        "text": "<p>A student uses √2 for a 30-60-90 triangle with short leg 6, giving a "
                "hypotenuse of 6√2. What is correct?</p>",
        "choices": ["12", "6√3", "6√2", "3"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> √2 — 45-45-90 niki. Bu "
                       "uchburchakda gipotenuza qisqa katetning ikki "
                       "barobari.</p>",
    },
    {
        "text": "<p>A student says the altitude of an equilateral triangle with side 12 "
                "is 6. What is correct?</p>",
        "choices": ["6√3", "6", "12√3", "6√2"],
        "correct": "6√3",
        "explanation": "<p><strong>6√3.</strong> Oʻquvchi asosning yarmini "
                       "javob deb olgan.</p>"
                       "<p>Balandlik uzun katet — u 60° ga qarshi.</p>",
    },
    {
        "text": "<p>A regular hexagon is divided into six equilateral triangles of side "
                "8. What is the distance from the centre to the middle of one edge?</p>",
        "choices": ["4√3", "8", "4", "8√3"],
        "correct": "4√3",
        "explanation": "<p><strong>4√3.</strong> Bu teng tomonli uchburchak "
                       "balandligi: tomoni 8, demak x = 4.</p>"
                       "<p>Taxminan 6.93.</p>",
    },
    {
        "text": "<p>A ramp makes a 30° angle with the ground and is 24 metres long along "
                "the slope. How high does it rise?</p>",
        "choices": ["12 metres", "12√3 metres", "24 metres", "8 metres"],
        "correct": "12 metres",
        "explanation": "<p><strong>12 metr.</strong> Balandlik 30° ga qarshi — "
                       "qisqa katet, gipotenuzaning yarmi.</p>",
    },
    {
        "text": "<p>For that same ramp, what horizontal distance does it cover?</p>",
        "choices": ["12√3 metres", "12 metres", "24 metres", "6√3 metres"],
        "correct": "12√3 metres",
        "explanation": "<p><strong>12√3 metr.</strong> Gorizontal masofa 60° ga "
                       "qarshi — uzun katet.</p>"
                       "<p>Taxminan 20.78.</p>",
    },
    {
        "text": "<p>A triangular roof panel is half of an equilateral triangle with side "
                "16. What is the area of the panel?</p>",
        "choices": ["32√3", "64√3", "16√3", "128"],
        "correct": "32√3",
        "explanation": "<p><strong>32√3.</strong> Katetlar 8 va 8√3, va yuza "
                       "ularning koʻpaytmasining yarmi.</p>"
                       "<p>Taxminan 55.4.</p>",
    },
]


# =====================================================================
# SAT-73 — triangle inequality and similarity
# =====================================================================

Q_SAT73 = [
    {
        "text": "<p>Can a triangle have sides 4, 5 and 10?</p>",
        "choices": ["No — 4 + 5 is less than 10", "Yes", "Only if it is obtuse",
                    "It cannot be determined"],
        "correct": "No — 4 + 5 is less than 10",
        "explanation": "<p><strong>Yoʻq.</strong> 9 &lt; 10 — uchburchak "
                       "yopilmaydi.</p>",
    },
    {
        "text": "<p>Can a triangle have sides 6, 8 and 14?</p>",
        "choices": ["No — the sum equals the third side", "Yes",
                    "Yes, it is a right triangle", "It cannot be determined"],
        "correct": "No — the sum equals the third side",
        "explanation": "<p><strong>Yoʻq.</strong> 6 + 8 = 14 — uchta nuqta bir "
                       "chiziqda yotadi.</p>"
                       "<p>Shart qatʼiy: yigʻindi <b>katta</b> boʻlishi "
                       "kerak.</p>",
    },
    {
        "text": "<p>Two sides of a triangle are 6 and 9. The third side must be between "
                "which values?</p>",
        "choices": ["3 and 15", "6 and 9", "0 and 15", "3 and 9"],
        "correct": "3 and 15",
        "explanation": "<p><strong>3 va 15 orasida.</strong> Ayirmadan "
                       "yigʻindigacha, chegaralar kirmaydi.</p>",
    },
    {
        "text": "<p>Two sides of a triangle are 10 and 10. What is the largest possible "
                "whole-number third side?</p>",
        "choices": ["19", "20", "10", "21"],
        "correct": "19",
        "explanation": "<p><strong>19.</strong> Uchinchi tomon 20 dan kichik "
                       "boʻlishi kerak.</p>"
                       "<p><strong>20</strong> — aynan yigʻindi, va u ishlamaydi.</p>",
    },
    {
        "text": "<p>Two triangles have angles 50° and 60°. Are they similar?</p>",
        "choices": ["Yes, by AA", "No", "Only if a side matches",
                    "It cannot be determined"],
        "correct": "Yes, by AA",
        "explanation": "<p><strong>Ha, AA boʻyicha.</strong> Ikki burchak teng "
                       "boʻlsa yetarli.</p>"
                       "<p>Uchinchisi 70° dan boʻladi — avtomatik.</p>",
    },
    {
        "text": "<p>Similar triangles have corresponding sides 5 and 20. What is the "
                "scale factor from the smaller to the larger?</p>",
        "choices": ["4", "15", "0.25", "100"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 20 ÷ 5.</p>"
                       "<p><strong>15</strong> — farq, koeffitsient emas.</p>",
    },
    {
        "text": "<p>Triangles ABC and DEF are similar with AB = 4, DE = 10 and BC = 6. "
                "What is EF?</p>",
        "choices": ["15", "12", "16", "2.4"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> Nisbat 2.5, va 6 × 2.5.</p>"
                       "<p><strong>12</strong> — farq qoʻshilgan (6 + 6).</p>",
    },
    {
        "text": "<p>Triangles are similar with sides 9 and 3 corresponding. If another "
                "side of the larger is 15, what is its match in the smaller?</p>",
        "choices": ["5", "9", "45", "12"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Nisbat 3, va 15 ÷ 3.</p>"
                       "<p>Kichik uchburchakda hamma tomon kichikroq boʻlishi "
                       "kerak.</p>",
    },
    {
        "text": "<p>Are all equilateral triangles similar to one another?</p>",
        "choices": ["Yes — every angle is 60°", "No", "Only if the sides match",
                    "Only if they are congruent"],
        "correct": "Yes — every angle is 60°",
        "explanation": "<p><strong>Ha.</strong> Burchaklar bir xil, demak AA "
                       "bajariladi.</p>",
    },
    {
        "text": "<p>Are all isosceles triangles similar to one another?</p>",
        "choices": ["No — their apex angles can differ", "Yes",
                    "Only if they are right triangles", "Only if the bases match"],
        "correct": "No — their apex angles can differ",
        "explanation": "<p><strong>Yoʻq.</strong> Uchidagi burchak 20° ham, "
                       "100° ham boʻlishi mumkin.</p>"
                       "<p>Teng tomonlida esa burchaklar qatʼiy 60°.</p>",
    },
    {
        "text": "<p>A line parallel to one side of a triangle cuts the other two sides. "
                "What is true of the small triangle formed?</p>",
        "choices": ["It is similar to the original", "It is congruent to the original",
                    "It has the same area", "Nothing can be said"],
        "correct": "It is similar to the original",
        "explanation": "<p><strong>Oʻxshash.</strong> Parallellik mos "
                       "burchaklarni teng qiladi (SAT-67), va uchidagi burchak "
                       "umumiy.</p>",
    },
    {
        "text": "<p>Two similar triangles have a scale factor of 3. If a side of the "
                "small one is 7, what is its match?</p>",
        "choices": ["21", "10", "7/3", "49"],
        "correct": "21",
        "explanation": "<p><strong>21.</strong> 7 × 3.</p>",
    },
    {
        "text": "<p>Which set of sides forms a valid triangle?</p>",
        "choices": ["7, 9, 12", "2, 3, 6", "1, 1, 3", "4, 5, 9"],
        "correct": "7, 9, 12",
        "explanation": "<p><strong>7, 9, 12.</strong> 7 + 9 = 16 &gt; 12 ✓</p>"
                       "<p>Qolganlarida ikki qisqa tomon yigʻindisi yetmaydi.</p>",
    },
    {
        "text": "<p>Is SAS a valid test for similarity?</p>",
        "choices": ["Yes — two sides in proportion with the included angle equal",
                    "No, only AA works",
                    "Yes, but only for right triangles",
                    "No, SAS is only for congruence"],
        "correct": "Yes — two sides in proportion with the included angle equal",
        "explanation": "<p><strong>Ha.</strong> Ikki tomon nisbati teng va "
                       "oradagi burchak teng boʻlsa yetarli.</p>",
    },
    {
        "text": "<p>A student says a triangle with sides 3, 4 and 7 exists. What is the "
                "problem?</p>",
        "choices": ["3 + 4 equals 7, so the points lie on a line",
                    "The sides are too small",
                    "It would be obtuse",
                    "There is no problem"],
        "correct": "3 + 4 equals 7, so the points lie on a line",
        "explanation": "<p><strong>Aynan teng.</strong> Uchburchak hosil "
                       "boʻlmaydi.</p>",
    },
    {
        "text": "<p>A student finds a matching side in similar triangles by adding the "
                "difference: 5 → 12 means 8 → 15. What is correct?</p>",
        "choices": ["19.2", "15", "8", "12"],
        "correct": "19.2",
        "explanation": "<p><strong>19.2.</strong> Nisbat 12 ÷ 5 = 2.4, va "
                       "8 × 2.4.</p>"
                       "<p>Oʻxshashlikda koʻpaytiriladi, qoʻshilmaydi.</p>",
    },
    {
        "text": "<p>Two sides of a triangle are 12 and 5. How many whole-number values "
                "are possible for the third side?</p>",
        "choices": ["9", "10", "8", "17"],
        "correct": "9",
        "explanation": "<p><strong>9 ta.</strong> Uchinchi tomon 7 dan katta va "
                       "17 dan kichik — 8 dan 16 gacha.</p>"
                       "<p>16 − 8 + 1 = 9.</p>",
    },
    {
        "text": "<p>A tree casts a shadow of 12 metres while a 2-metre pole casts a "
                "shadow of 3 metres at the same time. How tall is the tree?</p>",
        "choices": ["8 metres", "18 metres", "6 metres", "24 metres"],
        "correct": "8 metres",
        "explanation": "<p><strong>8 metr.</strong> Uchburchaklar oʻxshash: "
                       "2 ÷ 3 = h ÷ 12.</p>"
                       "<p>Quyosh nuri bir xil burchak ostida tushadi — AA.</p>",
    },
    {
        "text": "<p>A photograph 6 cm wide is enlarged so its width becomes 21 cm. If "
                "its height was 4 cm, what is the new height?</p>",
        "choices": ["14 cm", "19 cm", "12 cm", "8 cm"],
        "correct": "14 cm",
        "explanation": "<p><strong>14 sm.</strong> Nisbat 3.5, va 4 × 3.5.</p>"
                       "<p><strong>19</strong> — farq qoʻshilgan (4 + 15).</p>",
    },
    {
        "text": "<p>A surveyor uses similar triangles: a 1.5-metre stick casts a shadow "
                "of 2 metres, and a tower's shadow is 36 metres. How tall is the "
                "tower?</p>",
        "choices": ["27 metres", "48 metres", "24 metres", "54 metres"],
        "correct": "27 metres",
        "explanation": "<p><strong>27 metr.</strong> 1.5 ÷ 2 = h ÷ 36.</p>"
                       "<p>Tekshiruv: 27 ÷ 36 = 0.75 = 1.5 ÷ 2 ✓</p>",
    },
]


# =====================================================================
# SAT-74 — congruence and scaling
# =====================================================================

Q_SAT74 = [
    {
        "text": "<p>A shape is enlarged by a scale factor of 5. How many times greater "
                "is its area?</p>",
        "choices": ["25", "5", "10", "125"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Yuza k kvadrat boʻyicha "
                       "oshadi.</p>",
    },
    {
        "text": "<p>A cube's side is tripled. How many times greater is its volume?</p>",
        "choices": ["27", "9", "3", "81"],
        "correct": "27",
        "explanation": "<p><strong>27.</strong> Hajm k kub boʻyicha oshadi.</p>",
    },
    {
        "text": "<p>A shape is enlarged by a scale factor of 6. How many times greater "
                "is its perimeter?</p>",
        "choices": ["6", "36", "12", "216"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Perimetr uzunlik — u chiziqli "
                       "oshadi.</p>"
                       "<p><strong>36</strong> — bu yuza koeffitsienti.</p>",
    },
    {
        "text": "<p>Two similar shapes have areas 9 and 49. What is the ratio of their "
                "lengths?</p>",
        "choices": ["3 to 7", "9 to 49", "3 to 49", "81 to 2401"],
        "correct": "3 to 7",
        "explanation": "<p><strong>3 dan 7 gacha.</strong> Yuzalar nisbatidan "
                       "ildiz olinadi.</p>",
    },
    {
        "text": "<p>Two similar triangles have perimeters 15 and 45. What is the ratio "
                "of their areas?</p>",
        "choices": ["1 to 9", "1 to 3", "1 to 27", "3 to 1"],
        "correct": "1 to 9",
        "explanation": "<p><strong>1 dan 9 gacha.</strong> Uzunlik nisbati 3, "
                       "va yuza uning kvadrati.</p>",
    },
    {
        "text": "<p>A shape is reduced to half its size. What happens to its area?</p>",
        "choices": ["It becomes a quarter", "It halves", "It becomes an eighth",
                    "It stays the same"],
        "correct": "It becomes a quarter",
        "explanation": "<p><strong>Chorakka tushadi.</strong> 0.5 kvadrat "
                       "0.25.</p>",
    },
    {
        "text": "<p>What does congruent mean?</p>",
        "choices": ["Same shape and same size", "Same shape only",
                    "Same area only", "Same perimeter only"],
        "correct": "Same shape and same size",
        "explanation": "<p><strong>Bir xil shakl va bir xil oʻlcham.</strong> "
                       "Masshtab koeffitsienti 1.</p>",
    },
    {
        "text": "<p>Which is <u>not</u> a valid test for triangle congruence?</p>",
        "choices": ["SSA", "SSS", "SAS", "ASA"],
        "correct": "SSA",
        "explanation": "<p><strong>SSA.</strong> Ikki tomon va ular orasida "
                       "boʻlmagan burchakdan ikki xil uchburchak chiqishi "
                       "mumkin.</p>",
    },
    {
        "text": "<p>Two congruent triangles are compared. What is the scale factor "
                "between them?</p>",
        "choices": ["1", "2", "0", "It varies"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Tenglik — nisbati bir boʻlgan "
                       "oʻxshashlik.</p>",
    },
    {
        "text": "<p>A model car is built at a scale of 1 to 20. How many times greater "
                "is the real car's surface area?</p>",
        "choices": ["400", "20", "8,000", "40"],
        "correct": "400",
        "explanation": "<p><strong>400.</strong> Sirt yuzasi — ikki oʻlchovli: "
                       "20 kvadrat.</p>",
    },
    {
        "text": "<p>For that same model, how many times greater is the real car's "
                "volume?</p>",
        "choices": ["8,000", "400", "20", "60"],
        "correct": "8,000",
        "explanation": "<p><strong>8,000.</strong> Hajm — uch oʻlchovli: "
                       "20 kub.</p>",
    },
    {
        "text": "<p>A rectangle's length only is doubled, its width unchanged. How many "
                "times greater is its area?</p>",
        "choices": ["2", "4", "1", "8"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Bu masshtab emas — shakl "
                       "oʻzgardi.</p>"
                       "<p>k kvadrat qoidasi faqat <b>oʻxshash</b> shakllarga "
                       "tegishli.</p>",
    },
    {
        "text": "<p>Two similar shapes have volumes 8 and 216. What is the ratio of "
                "their lengths?</p>",
        "choices": ["1 to 3", "1 to 27", "2 to 6", "1 to 9"],
        "correct": "1 to 3",
        "explanation": "<p><strong>1 dan 3 gacha.</strong> Hajmlar nisbati 27, "
                       "va uning kub ildizi 3.</p>",
    },
    {
        "text": "<p>What stays unchanged when a shape is scaled?</p>",
        "choices": ["Its angles", "Its area", "Its perimeter", "Its volume"],
        "correct": "Its angles",
        "explanation": "<p><strong>Burchaklari.</strong> Shakl oʻzgarmaydi, "
                       "faqat oʻlcham.</p>"
                       "<p>Shuning uchun sinus va kosinus ham oʻzgarmaydi "
                       "(SAT-75).</p>",
    },
    {
        "text": "<p>A student says doubling a shape doubles its area. What is "
                "correct?</p>",
        "choices": ["The area becomes four times greater", "The area doubles",
                    "The area becomes eight times greater", "The area is unchanged"],
        "correct": "The area becomes four times greater",
        "explanation": "<p><strong>Toʻrt barobar.</strong> Yuza ikkita "
                       "uzunlikdan tuzilgan.</p>",
    },
    {
        "text": "<p>A student says two shapes with an area ratio of 16 have a length "
                "ratio of 16. What is correct?</p>",
        "choices": ["4", "16", "256", "8"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Yuzadan uzunlikka ildiz "
                       "olinadi.</p>",
    },
    {
        "text": "<p>A photograph is enlarged so that its area is 9 times greater. By "
                "what factor did its width increase?</p>",
        "choices": ["3", "9", "81", "4.5"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> √9.</p>",
    },
    {
        "text": "<p>A map has a scale of 1 to 25,000. Two towns are 8 cm apart on the "
                "map. How far apart are they in kilometres?</p>",
        "choices": ["2 km", "20 km", "0.2 km", "200 km"],
        "correct": "2 km",
        "explanation": "<p><strong>2 km.</strong> 8 × 25,000 = 200,000 sm, "
                       "va 200,000 sm = 2 km.</p>"
                       "<p>Ikki bosqichli: masshtab, keyin birlik "
                       "(SAT-50).</p>",
    },
    {
        "text": "<p>A tin of paint covers a statue 2 metres tall. How many tins are "
                "needed for a similar statue 6 metres tall?</p>",
        "choices": ["9", "3", "27", "6"],
        "correct": "9",
        "explanation": "<p><strong>9 ta.</strong> Boʻyoq sirt yuzasiga "
                       "bogʻliq — masshtab 3, demak yuza 9 barobar.</p>"
                       "<p><strong>27</strong> — hajm koeffitsienti, u "
                       "boʻyoqqa emas, toʻldiruvchiga tegishli.</p>",
    },
    {
        "text": "<p>Two similar water tanks have heights 4 and 6 metres. The smaller "
                "holds 32 litres. How much does the larger hold?</p>",
        "choices": ["108 litres", "48 litres", "72 litres", "216 litres"],
        "correct": "108 litres",
        "explanation": "<p><strong>108 litr.</strong> Masshtab 1.5, hajm "
                       "1.5 kub = 3.375, va 32 × 3.375.</p>"
                       "<p><strong>48</strong> — faqat chiziqli koeffitsient "
                       "qoʻllangan.</p>",
    },
]


# =====================================================================
# SAT-75 — right triangle trigonometry
# =====================================================================

Q_SAT75 = [
    {
        "text": "<p>In a right triangle, the side opposite angle <i>A</i> is 6, the "
                "adjacent side is 8 and the hypotenuse is 10. What is sin <i>A</i>?</p>",
        "choices": ["3/5", "4/5", "3/4", "5/3"],
        "correct": "3/5",
        "explanation": "<p><strong>3/5.</strong> 6 ÷ 10, qisqartirilgan.</p>"
                       "<p><strong>4/5</strong> — bu kosinus.</p>",
    },
    {
        "text": "<p>For that same triangle, what is cos <i>A</i>?</p>",
        "choices": ["4/5", "3/5", "3/4", "5/4"],
        "correct": "4/5",
        "explanation": "<p><strong>4/5.</strong> Yondosh boʻlingan "
                       "gipotenuzaga.</p>",
    },
    {
        "text": "<p>For that same triangle, what is tan <i>A</i>?</p>",
        "choices": ["3/4", "4/3", "3/5", "4/5"],
        "correct": "3/4",
        "explanation": "<p><strong>3/4.</strong> Qarshi boʻlingan yondoshga — "
                       "gipotenuza ishtirok etmaydi.</p>",
    },
    {
        "text": "<p>In a 5-12-13 right triangle, what is sin of the angle opposite the "
                "side of 5?</p>",
        "choices": ["5/13", "12/13", "5/12", "13/5"],
        "correct": "5/13",
        "explanation": "<p><strong>5/13.</strong> Qarshi tomon 5, gipotenuza "
                       "13.</p>",
    },
    {
        "text": "<p>In that 5-12-13 triangle, what is tan of the angle opposite the side "
                "of 12?</p>",
        "choices": ["12/5", "5/12", "12/13", "5/13"],
        "correct": "12/5",
        "explanation": "<p><strong>12/5.</strong> Bu burchak uchun qarshi tomon "
                       "12 va yondosh 5.</p>"
                       "<p>Tangens 1 dan katta boʻlishi mumkin.</p>",
    },
    {
        "text": "<p>Which ratio does <u>not</u> involve the hypotenuse?</p>",
        "choices": ["Tangent", "Sine", "Cosine", "All three do"],
        "correct": "Tangent",
        "explanation": "<p><strong>Tangens.</strong> U qarshi boʻlingan "
                       "yondoshga.</p>",
    },
    {
        "text": "<p>Can the sine of an angle be 1.2?</p>",
        "choices": ["No — the opposite side cannot exceed the hypotenuse",
                    "Yes, for large angles", "Yes, for obtuse angles",
                    "Only in a 30-60-90 triangle"],
        "correct": "No — the opposite side cannot exceed the hypotenuse",
        "explanation": "<p><strong>Yoʻq.</strong> Sinus 1 dan katta "
                       "boʻlmaydi.</p>"
                       "<p>Bu javobni tekshirishning tez usuli.</p>",
    },
    {
        "text": "<p>Can the tangent of an angle be 3?</p>",
        "choices": ["Yes — tangent has no upper limit",
                    "No, ratios are at most 1",
                    "Only for right angles",
                    "Only in special triangles"],
        "correct": "Yes — tangent has no upper limit",
        "explanation": "<p><strong>Ha.</strong> Qarshi tomon yondoshdan ancha "
                       "uzun boʻlishi mumkin.</p>"
                       "<p>Chegara faqat sinus va kosinusda bor.</p>",
    },
    {
        "text": "<p>What is sin 30°?</p>",
        "choices": ["1/2", "√3/2", "√2/2", "1"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 30-60-90 uchburchagida qisqa "
                       "katet gipotenuzaning yarmi (SAT-72).</p>",
    },
    {
        "text": "<p>What is cos 60°?</p>",
        "choices": ["1/2", "√3/2", "√2/2", "2"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 60° uchun yondosh tomon qisqa "
                       "katet.</p>"
                       "<p>Diqqat: sin 30° va cos 60° teng — chunki "
                       "burchaklar 90 ga toʻldiradi.</p>",
    },
    {
        "text": "<p>What is tan 45°?</p>",
        "choices": ["1", "√2", "1/2", "√2/2"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> 45-45-90 da katetlar teng, "
                       "demak nisbat 1 (SAT-71).</p>",
    },
    {
        "text": "<p>A ramp is 20 metres long and rises at 30°. How high is its top?</p>",
        "choices": ["10 metres", "10√3 metres", "20 metres", "40 metres"],
        "correct": "10 metres",
        "explanation": "<p><strong>10 metr.</strong> 20 × sin 30°.</p>"
                       "<p><strong>10√3</strong> — bu gorizontal masofa.</p>",
    },
    {
        "text": "<p>A ladder 10 metres long leans at 60° to the ground. How far is its "
                "foot from the wall?</p>",
        "choices": ["5 metres", "5√3 metres", "10 metres", "8.7 metres"],
        "correct": "5 metres",
        "explanation": "<p><strong>5 metr.</strong> Gorizontal masofa yondosh "
                       "tomon: 10 × cos 60°.</p>"
                       "<p><strong>5√3</strong> — bu balandlik.</p>",
    },
    {
        "text": "<p>In a right triangle the two acute angles are <i>A</i> and <i>B</i>. "
                "What is true?</p>",
        "choices": ["sin A equals cos B", "sin A equals sin B",
                    "tan A equals tan B", "They are unrelated"],
        "correct": "sin A equals cos B",
        "explanation": "<p><strong>sin A = cos B.</strong> Ikki oʻtkir burchak "
                       "90 ga toʻldiradi, va tomonlarning roli "
                       "almashadi.</p>",
    },
    {
        "text": "<p>A student writes cos A = opposite ÷ hypotenuse. What is the correct "
                "definition?</p>",
        "choices": ["Adjacent ÷ hypotenuse", "Opposite ÷ adjacent",
                    "Hypotenuse ÷ adjacent", "Opposite ÷ hypotenuse"],
        "correct": "Adjacent ÷ hypotenuse",
        "explanation": "<p><strong>Yondosh ÷ gipotenuza.</strong> "
                       "CAH: Cosine, Adjacent, Hypotenuse.</p>",
    },
    {
        "text": "<p>A student computes tan of an angle as 13/5 in a 5-12-13 triangle, "
                "using the hypotenuse. What is correct for the angle opposite 5?</p>",
        "choices": ["5/12", "13/5", "5/13", "12/5"],
        "correct": "5/12",
        "explanation": "<p><strong>5/12.</strong> Tangensda gipotenuza umuman "
                       "ishlatilmaydi.</p>",
    },
    {
        "text": "<p>Two similar right triangles have a scale factor of 4. What is true "
                "of the sine of their corresponding angles?</p>",
        "choices": ["It is the same in both", "It is 4 times greater",
                    "It is 16 times greater", "It is 4 times smaller"],
        "correct": "It is the same in both",
        "explanation": "<p><strong>Bir xil.</strong> Sinus — nisbat, va nisbat "
                       "masshtabga bogʻliq emas (SAT-74).</p>",
    },
    {
        "text": "<p>A right triangle has legs 7 and 24. What is the sine of the angle "
                "opposite the side of 7?</p>",
        "choices": ["7/25", "24/25", "7/24", "25/7"],
        "correct": "7/25",
        "explanation": "<p><strong>7/25.</strong> Gipotenuza 25 — bu 7-24-25 "
                       "uchligi (SAT-70).</p>",
    },
    {
        "text": "<p>From a point 40 metres from the base of a tower, the angle of "
                "elevation to the top is 45°. How tall is the tower?</p>",
        "choices": ["40 metres", "40√2 metres", "20 metres", "80 metres"],
        "correct": "40 metres",
        "explanation": "<p><strong>40 metr.</strong> tan 45° = 1, demak "
                       "balandlik masofaga teng.</p>"
                       "<p>Bu 45-45-90 uchburchagi.</p>",
    },
    {
        "text": "<p>A kite string is 50 metres long and makes an angle of 60° with the "
                "ground. How high is the kite, assuming the string is straight?</p>",
        "choices": ["25√3 metres", "25 metres", "50 metres", "50√3 metres"],
        "correct": "25√3 metres",
        "explanation": "<p><strong>25√3 metr.</strong> 50 × sin 60°, taxminan "
                       "43.3.</p>"
                       "<p><strong>25</strong> — bu yerdagi gorizontal masofa, "
                       "balandlik emas.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-71 Practice: Special Right Triangles — 45-45-90",
        "description": "20 ta SAT uslubidagi savol — 1 : 1 : √2 nisbati, kvadrat "
                       "diagonali va koʻpaytirish/boʻlish yoʻnalishi.",
        "tutorial":    "SAT-71:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT71,
    },
    {
        "title":       "SAT-72 Practice: Special Right Triangles — 30-60-90",
        "description": "20 ta SAT uslubidagi savol — 1 : √3 : 2 nisbati, qaysi tomon "
                       "qaysi burchakka qarshi, va teng tomonli uchburchak balandligi.",
        "tutorial":    "SAT-72:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT72,
    },
    {
        "title":       "SAT-73 Practice: Triangle Inequality and Similarity (AA, SAS)",
        "description": "20 ta SAT uslubidagi savol — uchburchak mavjudmi, uchinchi "
                       "tomon oraligʻi va oʻxshashlikda proporsiya.",
        "tutorial":    "SAT-73:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT73,
    },
    {
        "title":       "SAT-74 Practice: Congruent Triangles and Area/Perimeter Scaling",
        "description": "20 ta SAT uslubidagi savol — uzunlik k, yuza k², hajm k³; "
                       "teskari yoʻnalishda ildiz.",
        "tutorial":    "SAT-74:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT74,
    },
    {
        "title":       "SAT-75 Practice: Right Triangle Trigonometry — Sine, Cosine, Tangent",
        "description": "20 ta SAT uslubidagi savol — SOH-CAH-TOA, tomon nomi burchakka "
                       "bogʻliqligi va nisbatning chegaralari.",
        "tutorial":    "SAT-75:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT75,
    },
]
