# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-66 … SAT-70 (Blok D boshlanadi).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Blok D: hisob qaytadi, jumla osonlashadi.
⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_66_70.py --master=prime \\
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
# SAT-66 — lines and angles
# =====================================================================

Q_SAT66 = [
    {
        "text": "<p>Two angles are complementary. One measures 28°. What is the "
                "other?</p>",
        "choices": ["62°", "152°", "72°", "28°"],
        "correct": "62°",
        "explanation": "<p><strong>62°.</strong> 90 − 28.</p>"
                       "<p><strong>152°</strong> — 180 dan ayirilgan, yaʼni "
                       "«supplementary» qoidasi.</p>",
    },
    {
        "text": "<p>Two angles are supplementary. One measures 47°. What is the "
                "other?</p>",
        "choices": ["133°", "43°", "313°", "47°"],
        "correct": "133°",
        "explanation": "<p><strong>133°.</strong> 180 − 47.</p>",
    },
    {
        "text": "<p>Two lines intersect and one angle measures 68°. What is the measure "
                "of the vertical angle?</p>",
        "choices": ["68°", "112°", "22°", "292°"],
        "correct": "68°",
        "explanation": "<p><strong>68°.</strong> Vertikal burchaklar teng.</p>"
                       "<p><strong>112°</strong> — bu qoʻshni burchak.</p>",
    },
    {
        "text": "<p>Two lines intersect and one angle measures 68°. What is the measure "
                "of an adjacent angle?</p>",
        "choices": ["112°", "68°", "22°", "32°"],
        "correct": "112°",
        "explanation": "<p><strong>112°.</strong> 180 − 68 — ular toʻgʻri chiziq "
                       "hosil qiladi.</p>",
    },
    {
        "text": "<p>Three angles lie on a straight line and measure 55°, <i>x</i>° and "
                "70°. What is <i>x</i>?</p>",
        "choices": ["55", "125", "35", "235"],
        "correct": "55",
        "explanation": "<p><strong>55.</strong> 180 − 125.</p>"
                       "<p>Toʻgʻri chiziqdagi barcha burchaklar 180 beradi.</p>",
    },
    {
        "text": "<p>Four angles meet at a point and measure 90°, 100°, 80° and "
                "<i>x</i>°. What is <i>x</i>?</p>",
        "choices": ["90", "270", "10", "180"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> Nuqta atrofida toʻliq burilish — "
                       "360 − 270.</p>"
                       "<p>Bu yerda 180 emas, 360 ishlaydi.</p>",
    },
    {
        "text": "<p>Angles measuring (4<i>x</i>)° and (5<i>x</i>)° are complementary. "
                "What is <i>x</i>?</p>",
        "choices": ["10", "20", "9", "18"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 9x = 90.</p>"
                       "<p><strong>20</strong> — 180 ishlatilgan, yaʼni "
                       "«supplementary».</p>",
    },
    {
        "text": "<p>Angles measuring (2<i>x</i> + 15)° and (3<i>x</i> − 5)° are "
                "supplementary. What is <i>x</i>?</p>",
        "choices": ["34", "16", "37", "26"],
        "correct": "34",
        "explanation": "<p><strong>34.</strong> 5x + 10 = 180 → 5x = 170.</p>"
                       "<p>Tekshiruv: 83° va 97°, yigʻindisi 180 ✓</p>",
    },
    {
        "text": "<p>An angle measures 118°. Does it have a complement?</p>",
        "choices": ["No, because it is greater than 90°",
                    "Yes, it is 62°", "Yes, it is −28°", "Yes, it is 242°"],
        "correct": "No, because it is greater than 90°",
        "explanation": "<p><strong>Yoʻq.</strong> Toʻldiruvchi burchak manfiy "
                       "chiqadi, va bunday burchak mavjud emas.</p>",
    },
    {
        "text": "<p>Two lines intersect. If one angle is a right angle, what are the "
                "other three?</p>",
        "choices": ["All 90°", "90°, 45°, 45°", "180°, 90°, 90°", "It cannot be determined"],
        "correct": "All 90°",
        "explanation": "<p><strong>Hammasi 90°.</strong> Vertikali 90, qoʻshnilari "
                       "180 − 90 = 90.</p>"
                       "<p>Bu perpendikulyar chiziqlar.</p>",
    },
    {
        "text": "<p>In a figure marked 'not drawn to scale', an angle looks like a "
                "right angle but is not labelled. What can you assume?</p>",
        "choices": ["Nothing — only labelled measures can be used",
                    "That it is 90°", "That it is close to 90°",
                    "That the figure is wrong"],
        "correct": "Nothing — only labelled measures can be used",
        "explanation": "<p><strong>Hech narsa.</strong> Faqat yozilgan sonlar va "
                       "belgilar ishonchli.</p>",
    },
    {
        "text": "<p>Angle A and angle B are supplementary, and angle A is three times "
                "angle B. What is angle A?</p>",
        "choices": ["135°", "45°", "120°", "60°"],
        "correct": "135°",
        "explanation": "<p><strong>135°.</strong> B + 3B = 180 → B = 45, "
                       "A = 135.</p>"
                       "<p><strong>45°</strong> — bu B burchagi.</p>",
    },
    {
        "text": "<p>Two angles are complementary and equal. What is each?</p>",
        "choices": ["45°", "90°", "30°", "60°"],
        "correct": "45°",
        "explanation": "<p><strong>45°.</strong> 2x = 90.</p>",
    },
    {
        "text": "<p>Rays from one point divide a full turn into angles of 120°, 150° "
                "and <i>x</i>°. What is <i>x</i>?</p>",
        "choices": ["90", "270", "60", "30"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 360 − 270.</p>"
                       "<p>Toʻliq burilish 360 daraja.</p>",
    },
    {
        "text": "<p>A student says an adjacent angle to a 130° angle at an intersection "
                "is 40°. What is correct?</p>",
        "choices": ["50°", "40°", "130°", "230°"],
        "correct": "50°",
        "explanation": "<p><strong>50°.</strong> Oʻquvchi 90 dan ayirgan; toʻgʻri "
                       "chiziqda 180 ishlaydi.</p>",
    },
    {
        "text": "<p>A student says two angles that look equal in a figure must be "
                "equal. What is the flaw?</p>",
        "choices": ["Figures may not be drawn to scale",
                    "Angles are never equal",
                    "The figure must be redrawn",
                    "There is no flaw"],
        "correct": "Figures may not be drawn to scale",
        "explanation": "<p><strong>Chizma masshtabsiz boʻlishi mumkin.</strong></p>"
                       "<p>Tenglik belgilangan yoki hisoblangan boʻlishi "
                       "kerak.</p>",
    },
    {
        "text": "<p>At an intersection, one angle is (3<i>x</i>)° and its vertical "
                "angle is (<i>x</i> + 40)°. What is <i>x</i>?</p>",
        "choices": ["20", "35", "10", "45"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Vertikal burchaklar teng: "
                       "3x = x + 40.</p>"
                       "<p>Tekshiruv: ikkalasi ham 60° ✓</p>",
    },
    {
        "text": "<p>At an intersection, one angle is (2<i>x</i>)° and an adjacent angle "
                "is (<i>x</i> + 30)°. What is <i>x</i>?</p>",
        "choices": ["50", "30", "60", "10"],
        "correct": "50",
        "explanation": "<p><strong>50.</strong> Qoʻshni burchaklar 180 ga "
                       "toʻldiradi: 3x + 30 = 180.</p>"
                       "<p>Tekshiruv: 100° va 80° ✓</p>",
    },
    {
        "text": "<p>A ladder leans against a wall making a 68° angle with the ground. "
                "What angle does it make with the wall?</p>",
        "choices": ["22°", "112°", "68°", "32°"],
        "correct": "22°",
        "explanation": "<p><strong>22°.</strong> Devor va yer perpendikulyar, "
                       "demak ikki burchak 90 ga toʻldiradi.</p>"
                       "<p>Bu yerda 90 ishlaydi, 180 emas — chunki uchburchak "
                       "toʻgʻri burchakli.</p>",
    },
    {
        "text": "<p>A road sign is a straight bar. Two supports meet it making angles of "
                "(5<i>x</i> − 10)° and (3<i>x</i> + 30)° on the same side, together "
                "forming a straight line. What is <i>x</i>?</p>",
        "choices": ["20", "25", "17.5", "22.5"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 8x + 20 = 180 → 8x = 160.</p>"
                       "<p>Tekshiruv: 90° va 90° ✓ — ikkala tayanch ham "
                       "perpendikulyar.</p>",
    },
]


# =====================================================================
# SAT-67 — parallel lines
# =====================================================================

Q_SAT67 = [
    {
        "text": "<p>Two parallel lines are cut by a transversal. One angle is 65°. What "
                "are the only two angle measures in the figure?</p>",
        "choices": ["65° and 115°", "65° and 25°", "65° and 90°", "65° only"],
        "correct": "65° and 115°",
        "explanation": "<p><strong>65° va 115°.</strong> Sakkiz burchak, ikki "
                       "qiymat.</p>"
                       "<p>Ular 180 ga toʻldiradi.</p>",
    },
    {
        "text": "<p>Corresponding angles measure 74° and (<i>x</i> + 20)°. Find "
                "<i>x</i>.</p>",
        "choices": ["54", "86", "106", "94"],
        "correct": "54",
        "explanation": "<p><strong>54.</strong> Mos burchaklar teng: "
                       "x + 20 = 74.</p>",
    },
    {
        "text": "<p>Alternate interior angles measure (3<i>x</i>)° and (<i>x</i> + 40)°. "
                "Find <i>x</i>.</p>",
        "choices": ["20", "35", "10", "45"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Ichki almashinuvchi burchaklar "
                       "teng: 3x = x + 40.</p>"
                       "<p>Tekshiruv: ikkalasi 60° ✓</p>",
    },
    {
        "text": "<p>Co-interior (same-side interior) angles measure 78° and <i>y</i>°. "
                "Find <i>y</i>.</p>",
        "choices": ["102", "78", "12", "282"],
        "correct": "102",
        "explanation": "<p><strong>102.</strong> Ular 180 ga toʻldiradi.</p>"
                       "<p><strong>78</strong> — teng deb olingan; bir tomonli "
                       "ichki burchaklar teng emas.</p>",
    },
    {
        "text": "<p>Co-interior angles measure (2<i>x</i>)° and (3<i>x</i> + 30)°. Find "
                "<i>x</i>.</p>",
        "choices": ["30", "6", "42", "36"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 5x + 30 = 180.</p>"
                       "<p>Tekshiruv: 60° va 120° ✓</p>",
    },
    {
        "text": "<p>A transversal crosses two parallel lines. Which measure is "
                "<u>impossible</u> in the figure if one angle is 40°?</p>",
        "choices": ["100°", "40°", "140°", "All three are possible"],
        "correct": "100°",
        "explanation": "<p><strong>100°.</strong> Faqat 40 va 140 hosil "
                       "boʻladi.</p>"
                       "<p>Sakkiz burchak, ikki qiymat.</p>",
    },
    {
        "text": "<p>A transversal makes corresponding angles of 71° and 71°. What "
                "follows?</p>",
        "choices": ["The lines are parallel", "The lines are perpendicular",
                    "The lines meet at 71°", "Nothing follows"],
        "correct": "The lines are parallel",
        "explanation": "<p><strong>Chiziqlar parallel.</strong> Qoida teskari "
                       "yoʻnalishda ham ishlaydi.</p>",
    },
    {
        "text": "<p>A transversal makes corresponding angles of 71° and 75°. What "
                "follows?</p>",
        "choices": ["The lines are not parallel", "The lines are parallel",
                    "The lines are perpendicular", "Nothing follows"],
        "correct": "The lines are not parallel",
        "explanation": "<p><strong>Parallel emas.</strong> Mos burchaklar teng "
                       "boʻlishi shart edi.</p>",
    },
    {
        "text": "<p>A transversal is perpendicular to two parallel lines. How many "
                "different angle measures appear?</p>",
        "choices": ["One", "Two", "Four", "Eight"],
        "correct": "One",
        "explanation": "<p><strong>Bittasi.</strong> Hammasi 90° — ikki guruh "
                       "bitta qiymatga qoʻshilib ketadi.</p>",
    },
    {
        "text": "<p>Three parallel lines are cut by one transversal. How many different "
                "angle measures appear?</p>",
        "choices": ["Two", "Three", "Six", "Twelve"],
        "correct": "Two",
        "explanation": "<p><strong>Ikkitasi.</strong> Chiziqlar soni qiymatlar "
                       "sonini oshirmaydi.</p>"
                       "<p>Har bir kesishmada oʻsha ikki qiymat "
                       "takrorlanadi.</p>",
    },
    {
        "text": "<p>In a figure, no parallel marks are shown and nothing is stated. Can "
                "you use the parallel line rules?</p>",
        "choices": ["No — parallelism must be given",
                    "Yes, if the lines look parallel",
                    "Yes, always",
                    "Only for corresponding angles"],
        "correct": "No — parallelism must be given",
        "explanation": "<p><strong>Yoʻq.</strong> Parallellik aytilgan yoki "
                       "belgilangan boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A transversal crosses parallel lines <i>m</i> and <i>n</i>. An "
                "angle above <i>m</i> on the left is 118°. What is the angle below "
                "<i>n</i> on the left?</p>",
        "choices": ["118°", "62°", "90°", "42°"],
        "correct": "118°",
        "explanation": "<p><strong>118°.</strong> Ikkalasi ham keng burchak, "
                       "demak teng.</p>"
                       "<p>Atamani bilmasangiz ham: hamma keng burchak "
                       "teng.</p>",
    },
    {
        "text": "<p>Parallel lines are cut by a transversal, and one acute angle is "
                "<i>a</i>°. What is the sum of one acute and one obtuse angle?</p>",
        "choices": ["180°", "90°", "360°", "It depends on a"],
        "correct": "180°",
        "explanation": "<p><strong>180°.</strong> Tor va keng burchak har doim "
                       "toʻldiruvchi.</p>",
    },
    {
        "text": "<p>Two parallel lines are cut by a transversal, and one angle measures "
                "90°. What is the measure of every other angle?</p>",
        "choices": ["90°", "90° and 180°", "45° and 135°", "It cannot be determined"],
        "correct": "90°",
        "explanation": "<p><strong>Hammasi 90°.</strong> Kesuvchi "
                       "perpendikulyar.</p>",
    },
    {
        "text": "<p>A student says co-interior angles are equal. Two such angles measure "
                "(4<i>x</i>)° and (2<i>x</i> + 60)°. What is the correct value of "
                "<i>x</i>?</p>",
        "choices": ["20", "30", "40", "15"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> Ular 180 ga toʻldiradi: "
                       "6x + 60 = 180.</p>"
                       "<p>Oʻquvchining usuli (teng deb olish) 30 berardi — "
                       "u tuzoq javob.</p>",
    },
    {
        "text": "<p>A student assumes two lines are parallel because the figure looks "
                "that way, and finds x = 25. What is the problem?</p>",
        "choices": ["Parallelism was never given, so no rule applies",
                    "The arithmetic is wrong",
                    "25 is too small",
                    "There is no problem"],
        "correct": "Parallelism was never given, so no rule applies",
        "explanation": "<p><strong>Parallellik berilmagan.</strong> Chizma "
                       "masshtabsiz boʻlishi mumkin (SAT-66).</p>",
    },
    {
        "text": "<p>Parallel lines <i>m</i> and <i>n</i> are cut by a transversal. An "
                "angle at <i>m</i> is (5<i>x</i> − 20)° and the corresponding angle at "
                "<i>n</i> is (3<i>x</i> + 40)°. What is <i>x</i>?</p>",
        "choices": ["30", "20", "7.5", "15"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> Mos burchaklar teng: "
                       "5x − 20 = 3x + 40 → 2x = 60.</p>"
                       "<p>Tekshiruv: ikkalasi 130° ✓</p>",
    },
    {
        "text": "<p>A transversal crosses parallel lines. One alternate interior angle "
                "is (7<i>x</i>)° and the other is (4<i>x</i> + 33)°. What is the angle "
                "measure?</p>",
        "choices": ["77°", "11°", "103°", "33°"],
        "correct": "77°",
        "explanation": "<p><strong>77°.</strong> 7x = 4x + 33 → x = 11, va "
                       "7(11) = 77.</p>"
                       "<p><strong>11</strong> — bu x, burchak emas. Savol "
                       "burchakni soʻragan.</p>",
    },
    {
        "text": "<p>A road crosses two parallel railway lines. The angle between the "
                "road and the first line is 55°. What is the angle between the road and "
                "the second line, on the same side?</p>",
        "choices": ["55°", "125°", "35°", "90°"],
        "correct": "55°",
        "explanation": "<p><strong>55°.</strong> Mos burchaklar teng.</p>"
                       "<p>Parallellik saqlangani uchun burchak "
                       "oʻzgarmaydi.</p>",
    },
    {
        "text": "<p>A carpenter checks whether two shelf brackets are parallel by "
                "measuring the angles a straight edge makes with each: 88° and 92° on "
                "the same side. Are they parallel?</p>",
        "choices": ["Yes — same-side angles summing to 180 means parallel",
                    "No — the angles are not equal",
                    "It cannot be determined",
                    "Only if both were 90°"],
        "correct": "Yes — same-side angles summing to 180 means parallel",
        "explanation": "<p><strong>Ha.</strong> 88 + 92 = 180 — bir tomonli "
                       "burchaklar uchun bu aynan parallellik sharti.</p>"
                       "<p>Ular teng boʻlishi shart emas — bu "
                       "co-interior juftlik.</p>",
    },
]


# =====================================================================
# SAT-68 — triangle angles
# =====================================================================

Q_SAT68 = [
    {
        "text": "<p>Two angles of a triangle are 38° and 72°. What is the third?</p>",
        "choices": ["70°", "110°", "80°", "60°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> 180 − 110.</p>",
    },
    {
        "text": "<p>Two angles of a triangle are 38° and 72°. What is the exterior "
                "angle at the third vertex?</p>",
        "choices": ["110°", "70°", "34°", "142°"],
        "correct": "110°",
        "explanation": "<p><strong>110°.</strong> Uzoqdagi ikki burchak "
                       "yigʻindisi: 38 + 72.</p>"
                       "<p><strong>70°</strong> — bu uchinchi <b>ichki</b> "
                       "burchak.</p>",
    },
    {
        "text": "<p>A triangle's angles are <i>x</i>, <i>x</i> and 4<i>x</i>. What is "
                "the largest angle?</p>",
        "choices": ["120°", "30°", "60°", "90°"],
        "correct": "120°",
        "explanation": "<p><strong>120°.</strong> 6x = 180 → x = 30, va "
                       "4x = 120.</p>"
                       "<p><strong>30°</strong> — bu x, eng kattasi emas.</p>",
    },
    {
        "text": "<p>A triangle's angles are 2<i>x</i>, 3<i>x</i> and 4<i>x</i>. What is "
                "<i>x</i>?</p>",
        "choices": ["20", "18", "30", "45"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 9x = 180.</p>"
                       "<p>Burchaklar 40°, 60°, 80° ✓</p>",
    },
    {
        "text": "<p>An exterior angle of a triangle is 125°. What is the interior angle "
                "beside it?</p>",
        "choices": ["55°", "125°", "35°", "65°"],
        "correct": "55°",
        "explanation": "<p><strong>55°.</strong> Ular toʻgʻri chiziqda: "
                       "180 − 125.</p>",
    },
    {
        "text": "<p>An exterior angle is 125° and one remote interior angle is 60°. What "
                "is the other remote interior angle?</p>",
        "choices": ["65°", "55°", "120°", "185°"],
        "correct": "65°",
        "explanation": "<p><strong>65°.</strong> Tashqi burchak ikkisining "
                       "yigʻindisi: 125 − 60.</p>",
    },
    {
        "text": "<p>Can a triangle have angles of 100° and 95°?</p>",
        "choices": ["No — the two already exceed 180°",
                    "Yes, the third would be −15°",
                    "Yes, if it is obtuse",
                    "Only if it is isosceles"],
        "correct": "No — the two already exceed 180°",
        "explanation": "<p><strong>Yoʻq.</strong> 195 > 180.</p>"
                       "<p>Uchburchakda koʻpi bilan bitta oʻtmas burchak "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>A triangle has angles 30°, 60° and 90°. What type is it?</p>",
        "choices": ["Right", "Acute", "Obtuse", "Equilateral"],
        "correct": "Right",
        "explanation": "<p><strong>Toʻgʻri burchakli.</strong> Bittasi aynan "
                       "90°.</p>",
    },
    {
        "text": "<p>A triangle has angles 50°, 60° and 70°. What type is it?</p>",
        "choices": ["Acute", "Right", "Obtuse", "It cannot be determined"],
        "correct": "Acute",
        "explanation": "<p><strong>Oʻtkir burchakli.</strong> Hammasi 90 dan "
                       "kichik.</p>",
    },
    {
        "text": "<p>What is the sum of the interior angles of a quadrilateral?</p>",
        "choices": ["360°", "180°", "540°", "720°"],
        "correct": "360°",
        "explanation": "<p><strong>360°.</strong> Toʻrtburchakni ikki "
                       "uchburchakka boʻlish mumkin.</p>"
                       "<p>180 qoidasi faqat uchburchakka tegishli.</p>",
    },
    {
        "text": "<p>Two angles of a triangle are equal and the third is 80°. What is "
                "each equal angle?</p>",
        "choices": ["50°", "40°", "100°", "80°"],
        "correct": "50°",
        "explanation": "<p><strong>50°.</strong> (180 − 80) ÷ 2.</p>",
    },
    {
        "text": "<p>In a triangle, angle A is twice angle B, and angle C is 90°. What is "
                "angle B?</p>",
        "choices": ["30°", "45°", "60°", "20°"],
        "correct": "30°",
        "explanation": "<p><strong>30°.</strong> A + B = 90, va A = 2B, demak "
                       "3B = 90.</p>"
                       "<p>Tekshiruv: 60°, 30°, 90° ✓</p>",
    },
    {
        "text": "<p>Two triangles share a common angle of 40°. In one, another angle is "
                "70°; in the other, another angle is 55°. What are their third "
                "angles?</p>",
        "choices": ["70° and 85°", "70° and 70°", "85° and 85°", "55° and 70°"],
        "correct": "70° and 85°",
        "explanation": "<p><strong>70° va 85°.</strong> 180 − 110 va "
                       "180 − 95.</p>"
                       "<p>Umumiy burchak ikkalasida ham 40 — bu zanjirning "
                       "bogʻlovchisi.</p>",
    },
    {
        "text": "<p>Why is an exterior angle always larger than either remote interior "
                "angle?</p>",
        "choices": ["Because it equals their sum, and both are positive",
                    "Because it is outside the triangle",
                    "Because it is always obtuse",
                    "It is not always larger"],
        "correct": "Because it equals their sum, and both are positive",
        "explanation": "<p><strong>U ikkisining yigʻindisi.</strong> Ikkalasi "
                       "musbat boʻlgani uchun yigʻindi har biridan katta.</p>",
    },
    {
        "text": "<p>A student says the exterior angle equals the third interior angle. "
                "Two angles are 45° and 65°. What is the exterior angle at the third "
                "vertex?</p>",
        "choices": ["110°", "70°", "45°", "65°"],
        "correct": "110°",
        "explanation": "<p><strong>110°.</strong> Uchinchi ichki burchak 70°, va "
                       "tashqi burchak 180 − 70.</p>"
                       "<p>Oʻquvchi ikkisini teng deb olgan; aslida ular 180 "
                       "ga toʻldiradi.</p>",
    },
    {
        "text": "<p>A student solves <i>x</i> + 2<i>x</i> + (3<i>x</i> − 60) = 180 as "
                "6<i>x</i> = 120. What is the correct value of <i>x</i>?</p>",
        "choices": ["40", "20", "30", "60"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> 6x − 60 = 180 → 6x = 240.</p>"
                       "<p>−60 oʻng tomonga oʻtganda qoʻshiladi.</p>",
    },
    {
        "text": "<p>In a triangle, the exterior angle at one vertex is (5<i>x</i>)° and "
                "the two remote interior angles are (2<i>x</i>)° and (2<i>x</i> + 20)°. "
                "What is <i>x</i>?</p>",
        "choices": ["20", "10", "25", "4"],
        "correct": "20",
        "explanation": "<p><strong>20.</strong> 5x = 4x + 20.</p>"
                       "<p>Tekshiruv: tashqi 100°, ichkilari 40° va 60° ✓</p>",
    },
    {
        "text": "<p>A triangle has an exterior angle of 90° at one vertex. What must be "
                "true?</p>",
        "choices": ["The interior angle there is also 90°",
                    "The triangle is equilateral",
                    "The triangle is obtuse",
                    "The other two angles are equal"],
        "correct": "The interior angle there is also 90°",
        "explanation": "<p><strong>Ichki burchak ham 90°.</strong> "
                       "180 − 90 = 90.</p>"
                       "<p>Demak bu toʻgʻri burchakli uchburchak.</p>",
    },
    {
        "text": "<p>A roof truss forms a triangle. Two of its angles measure 35° and "
                "35°. What is the angle at the apex?</p>",
        "choices": ["110°", "70°", "145°", "35°"],
        "correct": "110°",
        "explanation": "<p><strong>110°.</strong> 180 − 70.</p>"
                       "<p><strong>70°</strong> — bu ikki burchakning "
                       "yigʻindisi, uchidagi burchak emas.</p>",
    },
    {
        "text": "<p>A triangular plot has angles in the ratio 1 : 2 : 3. What is the "
                "largest angle?</p>",
        "choices": ["90°", "60°", "120°", "30°"],
        "correct": "90°",
        "explanation": "<p><strong>90°.</strong> 6 qism, har biri 30° — demak "
                       "30°, 60°, 90°.</p>"
                       "<p>Nisbat 1 : 2 : 3 boʻlgan uchburchak har doim "
                       "toʻgʻri burchakli.</p>",
    },
]


# =====================================================================
# SAT-69 — isosceles and equilateral
# =====================================================================

Q_SAT69 = [
    {
        "text": "<p>An isosceles triangle has an apex angle of 50°. What is each base "
                "angle?</p>",
        "choices": ["65°", "130°", "50°", "80°"],
        "correct": "65°",
        "explanation": "<p><strong>65°.</strong> (180 − 50) ÷ 2.</p>"
                       "<p><strong>130°</strong> — ikkiga boʻlish "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>An isosceles triangle has base angles of 72°. What is the apex "
                "angle?</p>",
        "choices": ["36°", "72°", "108°", "54°"],
        "correct": "36°",
        "explanation": "<p><strong>36°.</strong> 180 − 144.</p>",
    },
    {
        "text": "<p>What is each angle of an equilateral triangle?</p>",
        "choices": ["60°", "45°", "90°", "30°"],
        "correct": "60°",
        "explanation": "<p><strong>60°.</strong> 180 ÷ 3.</p>",
    },
    {
        "text": "<p>In triangle ABC, AB = AC and the angle at B is 55°. What is the "
                "angle at A?</p>",
        "choices": ["70°", "55°", "125°", "62.5°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> B va C teng, demak "
                       "180 − 110.</p>"
                       "<p><strong>62.5°</strong> — 55 uchidagi burchak deb "
                       "olingan.</p>",
    },
    {
        "text": "<p>In triangle PQR, angles at P and R are both 40°. Which sides are "
                "equal?</p>",
        "choices": ["PQ and QR", "PR and QR", "PQ and PR", "No sides are equal"],
        "correct": "PQ and QR",
        "explanation": "<p><strong>PQ va QR.</strong> Teng burchaklarga qarshi "
                       "turgan tomonlar teng: P ga QR, R ga PQ.</p>"
                       "<p>Qoida teskari yoʻnalishda ham ishlaydi.</p>",
    },
    {
        "text": "<p>An isosceles triangle has a right angle at its apex. What are the "
                "base angles?</p>",
        "choices": ["45°", "60°", "90°", "30°"],
        "correct": "45°",
        "explanation": "<p><strong>45°.</strong> (180 − 90) ÷ 2.</p>"
                       "<p>Bu SAT-71 dagi 45-45-90 uchburchagi.</p>",
    },
    {
        "text": "<p>Can an equilateral triangle contain an obtuse angle?</p>",
        "choices": ["No — every angle is 60°", "Yes, if it is large",
                    "Yes, one angle can be 120°", "It cannot be determined"],
        "correct": "No — every angle is 60°",
        "explanation": "<p><strong>Yoʻq.</strong> Uchala burchak ham 60°.</p>",
    },
    {
        "text": "<p>Is every equilateral triangle also isosceles?</p>",
        "choices": ["Yes — it has at least two equal sides",
                    "No, they are different types",
                    "Only if the angles are 60°",
                    "It cannot be determined"],
        "correct": "Yes — it has at least two equal sides",
        "explanation": "<p><strong>Ha.</strong> Uchtasi teng boʻlsa, ikkitasi "
                       "ham teng.</p>"
                       "<p>Aksi notoʻgʻri: har bir teng yonli uchburchak teng "
                       "tomonli emas.</p>",
    },
    {
        "text": "<p>An isosceles triangle has one angle of 100°. What are the other "
                "two?</p>",
        "choices": ["40° each", "80° each", "100° and −20°", "50° each"],
        "correct": "40° each",
        "explanation": "<p><strong>40° dan.</strong> 100° uchidagi burchak "
                       "boʻlishi shart — ikkita 100° 180 dan oshib "
                       "ketardi.</p>",
    },
    {
        "text": "<p>In an isosceles triangle, one of the equal angles is (3<i>x</i>)° "
                "and the apex is (2<i>x</i> + 30)°. What is <i>x</i>?</p>",
        "choices": ["18.75", "30", "25", "37.5"],
        "correct": "18.75",
        "explanation": "<p><strong>18.75.</strong> 3x + 3x + 2x + 30 = 180 → "
                       "8x = 150.</p>"
                       "<p>Teng burchak ikki marta hisobga olinadi.</p>",
    },
    {
        "text": "<p>An isosceles triangle has sides 7, 7 and 10. Which angle is "
                "largest?</p>",
        "choices": ["The one opposite the side of length 10",
                    "The one opposite a side of length 7",
                    "All are equal",
                    "It cannot be determined"],
        "correct": "The one opposite the side of length 10",
        "explanation": "<p><strong>10 ga qarshi turgani.</strong> Eng uzun "
                       "tomonga eng katta burchak qarshi turadi.</p>",
    },
    {
        "text": "<p>The altitude from the apex of an isosceles triangle does what to the "
                "base?</p>",
        "choices": ["Divides it into two equal parts",
                    "Leaves it unchanged",
                    "Divides it in the ratio 1 to 2",
                    "Makes it longer"],
        "correct": "Divides it into two equal parts",
        "explanation": "<p><strong>Teng ikkiga boʻladi.</strong> Shakl "
                       "simmetrik.</p>"
                       "<p>Bu Pifagor bilan birga ishlatiladi (SAT-70).</p>",
    },
    {
        "text": "<p>An equilateral triangle has a perimeter of 27. What is each "
                "side?</p>",
        "choices": ["9", "13.5", "27", "6.75"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 27 ÷ 3 — uchala tomon teng.</p>",
    },
    {
        "text": "<p>Two angles of a triangle are 63° and 54°. Is the triangle "
                "isosceles?</p>",
        "choices": ["Yes — the third angle is 63°", "No", "Only if a side is marked",
                    "It cannot be determined"],
        "correct": "Yes — the third angle is 63°",
        "explanation": "<p><strong>Ha.</strong> 180 − 117 = 63, demak ikki "
                       "burchak teng.</p>"
                       "<p>Ikki teng burchak — ikki teng tomon.</p>",
    },
    {
        "text": "<p>A student finds base angles by computing 180 − 40 = 140 for an apex "
                "of 40°. What is each base angle?</p>",
        "choices": ["70°", "140°", "40°", "100°"],
        "correct": "70°",
        "explanation": "<p><strong>70°.</strong> 140 ikki burchakning "
                       "yigʻindisi — uni ikkiga boʻlish kerak.</p>",
    },
    {
        "text": "<p>A student is told one of the equal angles is 50° and answers 65° for "
                "the third angle. What is correct?</p>",
        "choices": ["80°", "65°", "50°", "130°"],
        "correct": "80°",
        "explanation": "<p><strong>80°.</strong> 180 − 2(50).</p>"
                       "<p>Oʻquvchi 50 ni uchidagi burchak deb olgan.</p>",
    },
    {
        "text": "<p>An isosceles triangle has an apex angle equal to each base angle. "
                "What kind of triangle is it?</p>",
        "choices": ["Equilateral", "Right", "Obtuse", "Impossible"],
        "correct": "Equilateral",
        "explanation": "<p><strong>Teng tomonli.</strong> Uchala burchak teng "
                       "boʻlsa har biri 60°.</p>",
    },
    {
        "text": "<p>In an isosceles triangle, an exterior angle at a base vertex is "
                "110°. What is the apex angle?</p>",
        "choices": ["40°", "70°", "110°", "20°"],
        "correct": "40°",
        "explanation": "<p><strong>40°.</strong> Asos burchagi 180 − 110 = 70, "
                       "ikkalasi 140, va uchidagi 180 − 140.</p>"
                       "<p>Ikki dars birga: SAT-68 va SAT-69.</p>",
    },
    {
        "text": "<p>A triangular sail has two equal edges and an apex angle of 30°. What "
                "is each of the other angles?</p>",
        "choices": ["75°", "150°", "60°", "30°"],
        "correct": "75°",
        "explanation": "<p><strong>75°.</strong> (180 − 30) ÷ 2.</p>",
    },
    {
        "text": "<p>A bridge support is an isosceles triangle whose base angles are each "
                "twice the apex angle. What is the apex angle?</p>",
        "choices": ["36°", "45°", "60°", "72°"],
        "correct": "36°",
        "explanation": "<p><strong>36°.</strong> a + 2a + 2a = 180 → 5a = 180.</p>"
                       "<p>Tekshiruv: 36°, 72°, 72° ✓</p>",
    },
]


# =====================================================================
# SAT-70 — Pythagoras and distance
# =====================================================================

Q_SAT70 = [
    {
        "text": "<p>A right triangle has legs 9 and 12. What is the hypotenuse?</p>",
        "choices": ["15", "21", "225", "√21"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 81 + 144 = 225.</p>"
                       "<p><strong>21</strong> — katetlar qoʻshilgan.</p>",
    },
    {
        "text": "<p>A right triangle has legs 8 and 15. What is the hypotenuse?</p>",
        "choices": ["17", "23", "289", "√23"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> 64 + 225 = 289 — bu 8-15-17 "
                       "uchligi.</p>",
    },
    {
        "text": "<p>A right triangle has hypotenuse 26 and one leg 10. What is the other "
                "leg?</p>",
        "choices": ["24", "28", "36", "16"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> 676 − 100 = 576.</p>"
                       "<p>Bu 5-12-13 ning ikki barobari.</p>",
    },
    {
        "text": "<p>What is the distance between (0, 0) and (8, 15)?</p>",
        "choices": ["17", "23", "√23", "289"],
        "correct": "17",
        "explanation": "<p><strong>17.</strong> Katetlar 8 va 15.</p>",
    },
    {
        "text": "<p>What is the distance between (2, 1) and (5, 5)?</p>",
        "choices": ["5", "7", "25", "√7"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Katetlar 3 va 4.</p>"
                       "<p><strong>25</strong> — ildiz olish unutilgan.</p>",
    },
    {
        "text": "<p>What is the distance between (−2, 1) and (1, 5)?</p>",
        "choices": ["5", "3", "7", "√5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Gorizontal farq 3, vertikal 4 — "
                       "ishoralar muhim emas, ular kvadratga "
                       "koʻtariladi.</p>",
    },
    {
        "text": "<p>What is the distance between (1, 1) and (4, 5)?</p>",
        "choices": ["5", "4", "3", "√5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Yana 3-4-5 uchligi.</p>",
    },
    {
        "text": "<p>What is the distance between (0, 0) and (2, 3)?</p>",
        "choices": ["√13", "5", "13", "√5"],
        "correct": "√13",
        "explanation": "<p><strong>√13.</strong> 4 + 9 = 13, va 13 toʻliq "
                       "kvadrat emas.</p>"
                       "<p>Javob ildiz koʻrinishida qoladi.</p>",
    },
    {
        "text": "<p>Is a triangle with sides 5, 12 and 13 a right triangle?</p>",
        "choices": ["Yes — 25 + 144 = 169", "No", "Only if the angle is marked",
                    "It cannot be determined"],
        "correct": "Yes — 25 + 144 = 169",
        "explanation": "<p><strong>Ha.</strong> Eng uzunini gipotenuza deb "
                       "olib tekshiring.</p>",
    },
    {
        "text": "<p>Is a triangle with sides 4, 5 and 6 a right triangle?</p>",
        "choices": ["No — 16 + 25 is not 36", "Yes", "Only if it is isosceles",
                    "It cannot be determined"],
        "correct": "No — 16 + 25 is not 36",
        "explanation": "<p><strong>Yoʻq.</strong> 41 ≠ 36.</p>",
    },
    {
        "text": "<p>A rectangle is 5 by 12. What is the length of its diagonal?</p>",
        "choices": ["13", "17", "60", "√17"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> Diagonal toʻrtburchakni ikki "
                       "toʻgʻri burchakli uchburchakka boʻladi.</p>"
                       "<p><strong>60</strong> — bu yuza.</p>",
    },
    {
        "text": "<p>A square has side 6. What is the length of its diagonal?</p>",
        "choices": ["6√2", "12", "36", "6"],
        "correct": "6√2",
        "explanation": "<p><strong>6√2.</strong> 36 + 36 = 72, va √72 = 6√2 "
                       "(SAT-25).</p>",
    },
    {
        "text": "<p>A ladder 13 metres long leans against a wall with its foot 5 metres "
                "from the base. How high up the wall does it reach?</p>",
        "choices": ["12 metres", "14 metres", "18 metres", "8 metres"],
        "correct": "12 metres",
        "explanation": "<p><strong>12 metr.</strong> 169 − 25 = 144.</p>"
                       "<p>Narvon gipotenuza — u eng uzun.</p>",
    },
    {
        "text": "<p>In a right triangle, which side is always the longest?</p>",
        "choices": ["The hypotenuse", "The shorter leg", "The longer leg",
                    "It varies"],
        "correct": "The hypotenuse",
        "explanation": "<p><strong>Gipotenuza.</strong> U toʻgʻri burchakka "
                       "qarshi turadi.</p>"
                       "<p>Bu javobni tekshirishning tez usuli.</p>",
    },
    {
        "text": "<p>A student computes the distance from (1, 2) to (4, 6) as 3 + 4 = 7. "
                "What is correct?</p>",
        "choices": ["5", "7", "25", "√7"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Katetlar qoʻshilmaydi — "
                       "kvadratlari qoʻshiladi.</p>",
    },
    {
        "text": "<p>A student is given hypotenuse 13 and leg 5, and computes "
                "169 + 25 = 194. What is the correct other leg?</p>",
        "choices": ["12", "14", "√194", "18"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Gipotenuza berilganda "
                       "<b>ayiriladi</b>: 169 − 25 = 144.</p>",
    },
    {
        "text": "<p>An isosceles triangle has equal sides of 13 and a base of 10. What "
                "is its height from the apex to the base?</p>",
        "choices": ["12", "8", "√69", "6.5"],
        "correct": "12",
        "explanation": "<p><strong>12.</strong> Balandlik asosni teng ikkiga "
                       "boʻladi (SAT-69), demak katet 5 va gipotenuza 13.</p>"
                       "<p>169 − 25 = 144 — yana 5-12-13.</p>",
    },
    {
        "text": "<p>A rectangular box has a base 3 by 4 and height 12. What is the "
                "length of its longest diagonal?</p>",
        "choices": ["13", "19", "12", "√19"],
        "correct": "13",
        "explanation": "<p><strong>13.</strong> Asos diagonali 5 (3-4-5), keyin "
                       "5 va 12 bilan yana Pifagor: 25 + 144 = 169.</p>"
                       "<p>Ikki bosqichli — har biri oddiy uchburchak.</p>",
    },
    {
        "text": "<p>A park is a rectangle 30 metres by 40 metres. How much shorter is "
                "the diagonal path than walking along two sides?</p>",
        "choices": ["20 metres", "10 metres", "50 metres", "30 metres"],
        "correct": "20 metres",
        "explanation": "<p><strong>20 metr.</strong> Diagonal 50, ikki tomon "
                       "70, farqi 20.</p>"
                       "<p>Bu 3-4-5 ning oʻn barobari.</p>",
    },
    {
        "text": "<p>Two ships leave the same port, one sailing 9 km north and the other "
                "12 km east. How far apart are they?</p>",
        "choices": ["15 km", "21 km", "3 km", "√21 km"],
        "correct": "15 km",
        "explanation": "<p><strong>15 km.</strong> Shimol va sharq "
                       "perpendikulyar, demak 81 + 144 = 225.</p>"
                       "<p>Yana 3-4-5, uch barobar.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-66 Practice: Lines and Angles — Vertical, Supplementary, and Complementary",
        "description": "20 ta SAT uslubidagi savol — 180 va 360 qoidalari, vertikal "
                       "burchaklar va masshtabsiz chizmaga ishonmaslik.",
        "tutorial":    "SAT-66:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT66,
    },
    {
        "title":       "SAT-67 Practice: Parallel Lines Cut by a Transversal",
        "description": "20 ta SAT uslubidagi savol — sakkiz burchak va ikki qiymat, "
                       "co-interior tuzogʻi va parallellikni tekshirish.",
        "tutorial":    "SAT-67:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT67,
    },
    {
        "title":       "SAT-68 Practice: Triangles — Interior and Exterior Angle Theorems",
        "description": "20 ta SAT uslubidagi savol — 180 qoidasi, tashqi burchak va "
                       "zanjirli chizmalar.",
        "tutorial":    "SAT-68:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT68,
    },
    {
        "title":       "SAT-69 Practice: Isosceles and Equilateral Triangles",
        "description": "20 ta SAT uslubidagi savol — berilgan burchak uchidagimi yoki "
                       "teng juftlikdanmi, va qoidaning teskari yoʻnalishi.",
        "tutorial":    "SAT-69:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT69,
    },
    {
        "title":       "SAT-70 Practice: Pythagorean Theorem and the Distance Formula",
        "description": "20 ta SAT uslubidagi savol — gipotenuzani aniqlash, uchliklar, "
                       "koordinatadagi masofa va diagonallar.",
        "tutorial":    "SAT-70:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT70,
    },
]
