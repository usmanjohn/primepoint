# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-76 … SAT-80 (Blok D yakuni).

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.
⚠️ Javob har doim "correct" da va choices ning BIRINCHISIDA turadi —
   display_choices() uni savol id boʻyicha aralashtiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_76_80.py --master=prime \\
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
# SAT-76 — trigonometric identities
# =====================================================================

Q_SAT76 = [
    {
        "text": "<p>If sin <i>A</i> = 0.6 and <i>A</i> + <i>B</i> = 90°, what is cos <i>B</i>?</p>",
        "choices": ["0.6", "0.8", "0.4", "1.6"],
        "correct": "0.6",
        "explanation": "<p><strong>0.6.</strong> sin(x) = cos(90 − x) — hech narsa "
                       "hisoblanmaydi.</p>"
                       "<p><strong>0.8</strong> — bu cos A, boshqa burchakniki.</p>",
    },
    {
        "text": "<p>If sin 25° = 0.42, what is cos 65°?</p>",
        "choices": ["0.42", "0.58", "0.91", "0.25"],
        "correct": "0.42",
        "explanation": "<p><strong>0.42.</strong> 25 + 65 = 90, demak ular "
                       "toʻldiruvchi.</p>"
                       "<p><strong>0.58</strong> — 1 − 0.42, bu ayniyat emas.</p>",
    },
    {
        "text": "<p>If cos <i>x</i> = 0.28, what is sin(90° − <i>x</i>)?</p>",
        "choices": ["0.28", "0.72", "0.96", "0.62"],
        "correct": "0.28",
        "explanation": "<p><strong>0.28.</strong> Ayniyat ikkala yoʻnalishda "
                       "ishlaydi: cos(x) = sin(90 − x).</p>",
    },
    {
        "text": "<p>Which expression is equivalent to sin(90° − <i>x</i>)?</p>",
        "choices": ["cos <i>x</i>", "sin <i>x</i>", "−cos <i>x</i>", "1 − cos <i>x</i>"],
        "correct": "cos <i>x</i>",
        "explanation": "<p><strong>cos x.</strong> Toʻldiruvchi burchakda qarshi va "
                       "yondosh tomonlar oʻrin almashadi.</p>",
    },
    {
        "text": "<p>In a right triangle, cos <i>A</i> = 5/13. What is sin <i>A</i>?</p>",
        "choices": ["12/13", "5/13", "13/5", "8/13"],
        "correct": "12/13",
        "explanation": "<p><strong>12/13.</strong> 5-12-13 uchligi; yoki "
                       "sin² = 1 − 25/169 = 144/169.</p>"
                       "<p><strong>8/13</strong> — 13 − 5 deb olingan; uchinchi tomon "
                       "ayirish bilan topilmaydi.</p>",
    },
    {
        "text": "<p>In a right triangle, sin <i>A</i> = 8/17. What is cos <i>A</i>?</p>",
        "choices": ["15/17", "9/17", "8/17", "17/15"],
        "correct": "15/17",
        "explanation": "<p><strong>15/17.</strong> 8-15-17 uchligi: 64 + 225 = 289.</p>"
                       "<p><strong>9/17</strong> — 17 − 8 deb olingan.</p>",
    },
    {
        "text": "<p>For any angle <i>x</i>, what does sin²<i>x</i> + cos²<i>x</i> equal?</p>",
        "choices": ["1", "0", "2", "<i>x</i>"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Bu Pifagor teoremasining "
                       "gipotenuza kvadratiga boʻlingani.</p>",
    },
    {
        "text": "<p>An acute angle <i>x</i> has sin <i>x</i> = 3/5. What is cos <i>x</i>?</p>",
        "choices": ["4/5", "5/4", "2/5", "3/4"],
        "correct": "4/5",
        "explanation": "<p><strong>4/5.</strong> 3-4-5 uchligi.</p>"
                       "<p><strong>3/4</strong> — bu tan x, kosinus emas.</p>",
    },
    {
        "text": "<p>What is the value of tan 45°?</p>",
        "choices": ["1", "0", "√2", "1/2"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> 45-45-90 da ikkala katet teng, "
                       "demak qarshi ÷ yondosh = 1.</p>",
    },
    {
        "text": "<p>If tan <i>A</i> = 3/4 and <i>A</i> + <i>B</i> = 90°, what is tan <i>B</i>?</p>",
        "choices": ["4/3", "3/4", "5/4", "1"],
        "correct": "4/3",
        "explanation": "<p><strong>4/3.</strong> Toʻldiruvchi burchakda tangens "
                       "teskarisiga aylanadi.</p>",
    },
    {
        "text": "<p>Which statement is true?</p>",
        "choices": ["sin 45° = cos 45°", "sin 45° = 2 cos 45°",
                    "sin 45° = 1", "cos 45° = 0"],
        "correct": "sin 45° = cos 45°",
        "explanation": "<p><strong>sin 45° = cos 45°.</strong> 45 oʻzining "
                       "toʻldiruvchisi: 90 − 45 = 45.</p>",
    },
    {
        "text": "<p>Given that sin 30° = 1/2, what is cos 60°?</p>",
        "choices": ["1/2", "√3/2", "1", "2"],
        "correct": "1/2",
        "explanation": "<p><strong>1/2.</strong> 30 va 60 toʻldiruvchi.</p>"
                       "<p><strong>√3/2</strong> — bu cos 30°.</p>",
    },
    {
        "text": "<p>If sin <i>x</i> = cos <i>y</i> and both angles are acute, "
                "what must be true?</p>",
        "choices": ["<i>x</i> + <i>y</i> = 90", "<i>x</i> = <i>y</i>",
                    "<i>x</i> + <i>y</i> = 180", "<i>x</i> − <i>y</i> = 90"],
        "correct": "<i>x</i> + <i>y</i> = 90",
        "explanation": "<p><strong>x + y = 90.</strong> Ayniyatning taʼrifi shu.</p>",
    },
    {
        "text": "<p>What is the value of sin 90°?</p>",
        "choices": ["1", "0", "90", "1/2"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> Va cos 0° ham 1 — ayniyat bu "
                       "chegarada ham ishlaydi.</p>",
    },
    {
        "text": "<p>What is the value of cos 0°?</p>",
        "choices": ["1", "0", "−1", "90"],
        "correct": "1",
        "explanation": "<p><strong>1.</strong> cos 0° = sin 90° = 1.</p>",
    },
    {
        "text": "<p>In a right triangle the acute angles are <i>x</i> and <i>y</i>. "
                "sin <i>x</i> is equal to the cosine of which angle?</p>",
        "choices": ["<i>y</i>", "<i>x</i>", "90° + <i>x</i>", "180° − <i>x</i>"],
        "correct": "<i>y</i>",
        "explanation": "<p><strong>y.</strong> Toʻgʻri burchakli uchburchakda "
                       "x + y = 90, demak y = 90 − x.</p>",
    },
    {
        "text": "<p>cos 40° is equal to the sine of which angle?</p>",
        "choices": ["50°", "40°", "140°", "130°"],
        "correct": "50°",
        "explanation": "<p><strong>50°.</strong> 90 − 40 = 50.</p>"
                       "<p><strong>140°</strong> — 180 dan ayirilgan; ayniyat "
                       "90 bilan ishlaydi.</p>",
    },
    {
        "text": "<p>sin 62° is equal to the cosine of which angle?</p>",
        "choices": ["28°", "62°", "118°", "38°"],
        "correct": "28°",
        "explanation": "<p><strong>28°.</strong> 90 − 62 = 28.</p>",
    },
    {
        "text": "<p>Which expression is equal to cos²<i>x</i>?</p>",
        "choices": ["1 − sin²<i>x</i>", "1 + sin²<i>x</i>",
                    "sin²<i>x</i> − 1", "sin<i>x</i> − 1"],
        "correct": "1 − sin²<i>x</i>",
        "explanation": "<p><strong>1 − sin²x.</strong> sin² + cos² = 1 "
                       "tenglamasidan.</p>",
    },
    {
        "text": "<p>A right triangle has acute angles <i>A</i> and <i>B</i>, and "
                "sin <i>A</i> = 0.6. What is sin <i>B</i>?</p>",
        "choices": ["0.8", "0.6", "0.4", "1.0"],
        "correct": "0.8",
        "explanation": "<p><strong>0.8.</strong> Ikki qadam: sin B = cos A, va "
                       "cos A = √(1 − 0.36) = 0.8.</p>"
                       "<p><strong>0.6</strong> — bu cos B; savol sinusni "
                       "soʻragan.</p>",
    },
]


# =====================================================================
# SAT-77 — radians and arc length
# =====================================================================

Q_SAT77 = [
    {
        "text": "<p>An angle measures 135°. What is its measure in radians?</p>",
        "choices": ["3π/4", "4π/3", "2π/3", "3π/2"],
        "correct": "3π/4",
        "explanation": "<p><strong>3π/4.</strong> 135/180 ni 45 ga qisqartiring: 3/4.</p>"
                       "<p><strong>4π/3</strong> — kasr agʻdarilgan; u 180° dan "
                       "katta burchak.</p>",
    },
    {
        "text": "<p>Convert 45° to radians.</p>",
        "choices": ["π/4", "π/2", "π/3", "π/6"],
        "correct": "π/4",
        "explanation": "<p><strong>π/4.</strong> 45/180 = 1/4.</p>",
    },
    {
        "text": "<p>Convert 60° to radians.</p>",
        "choices": ["π/3", "π/6", "π/4", "2π/3"],
        "correct": "π/3",
        "explanation": "<p><strong>π/3.</strong> 60/180 = 1/3.</p>"
                       "<p><strong>π/6</strong> — bu 30°.</p>",
    },
    {
        "text": "<p>Convert 5π/6 radians to degrees.</p>",
        "choices": ["150", "300", "100", "120"],
        "correct": "150",
        "explanation": "<p><strong>150.</strong> (5/6) × 180 = 150.</p>"
                       "<p><strong>300</strong> — 360 ga koʻpaytirilgan; koʻprik "
                       "180 = π.</p>",
    },
    {
        "text": "<p>Convert π/2 radians to degrees.</p>",
        "choices": ["90", "180", "45", "60"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> π yarim aylana, π/2 esa chorak.</p>",
    },
    {
        "text": "<p>Convert 3π/2 radians to degrees.</p>",
        "choices": ["270", "135", "540", "240"],
        "correct": "270",
        "explanation": "<p><strong>270.</strong> (3/2) × 180 = 270.</p>",
    },
    {
        "text": "<p>In a circle with radius 9, a central angle measures 2π/3 radians. "
                "What is the length of the arc it subtends?</p>",
        "choices": ["6π", "3π", "12π", "18π"],
        "correct": "6π",
        "explanation": "<p><strong>6π.</strong> s = rθ = 9 × 2π/3.</p>"
                       "<p><strong>18π</strong> — butun aylana uzunligi; burchak "
                       "ishlatilmagan.</p>",
    },
    {
        "text": "<p>A circle has radius 12. What is the length of the arc "
                "cut off by a central angle of 60°?</p>",
        "choices": ["4π", "2π", "24π", "12π"],
        "correct": "4π",
        "explanation": "<p><strong>4π.</strong> Ulush 1/6, aylana 24π.</p>"
                       "<p><strong>2π</strong> — 12π ning oltidan biri, yaʼni "
                       "aylana uzunligi yarim olingan.</p>",
    },
    {
        "text": "<p>A circle has radius 10. What is the arc length for a "
                "central angle of 36°?</p>",
        "choices": ["2π", "π", "20π", "4π"],
        "correct": "2π",
        "explanation": "<p><strong>2π.</strong> 36/360 = 1/10; 20π ning oʻndan "
                       "biri.</p>",
    },
    {
        "text": "<p>A circle has radius 4 and a central angle of π/2 radians. "
                "What is the arc length?</p>",
        "choices": ["2π", "8π", "π/2", "4π"],
        "correct": "2π",
        "explanation": "<p><strong>2π.</strong> rθ = 4 × π/2.</p>",
    },
    {
        "text": "<p>An arc of length 5π lies on a circle of radius 15. What is the "
                "central angle, in radians?</p>",
        "choices": ["π/3", "3π", "π/5", "75π"],
        "correct": "π/3",
        "explanation": "<p><strong>π/3.</strong> θ = s ÷ r = 5π ÷ 15.</p>"
                       "<p><strong>75π</strong> — boʻlish oʻrniga "
                       "koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>An arc of length 6π lies on a circle of radius 9. What is the "
                "central angle, in radians?</p>",
        "choices": ["2π/3", "3π/2", "π/3", "54π"],
        "correct": "2π/3",
        "explanation": "<p><strong>2π/3.</strong> 6π ÷ 9 = 2π/3.</p>",
    },
    {
        "text": "<p>What fraction of a full circle is a central angle of 72°?</p>",
        "choices": ["1/5", "1/4", "2/5", "1/6"],
        "correct": "1/5",
        "explanation": "<p><strong>1/5.</strong> 72/360.</p>",
    },
    {
        "text": "<p>180° is equal to how many radians?</p>",
        "choices": ["π", "2π", "π/2", "180π"],
        "correct": "π",
        "explanation": "<p><strong>π.</strong> Bu butun mavzuning koʻprigi.</p>",
    },
    {
        "text": "<p>How many radians are there in a full circle?</p>",
        "choices": ["2π", "π", "360π", "4π"],
        "correct": "2π",
        "explanation": "<p><strong>2π.</strong> Bu fakt formula varagʻida bor.</p>",
    },
    {
        "text": "<p>A circle has radius 5. What is the length of the minor arc "
                "cut off by a central angle of 144°?</p>",
        "choices": ["4π", "6π", "10π", "2π"],
        "correct": "4π",
        "explanation": "<p><strong>4π.</strong> 144/360 = 2/5; aylana 10π.</p>",
    },
    {
        "text": "<p>A circle has radius 5 and a central angle of 144°. What is the "
                "length of the <i>major</i> arc?</p>",
        "choices": ["6π", "4π", "10π", "8π"],
        "correct": "6π",
        "explanation": "<p><strong>6π.</strong> Qolgan burchak 360 − 144 = 216, "
                       "yaʼni 3/5. Nazorat: 4π + 6π = 10π ✓</p>"
                       "<p><strong>4π</strong> — qisqa yoy; savol uzunini "
                       "soʻragan.</p>",
    },
    {
        "text": "<p>Convert 30° to radians.</p>",
        "choices": ["π/6", "π/3", "π/12", "6π"],
        "correct": "π/6",
        "explanation": "<p><strong>π/6.</strong> 30/180 = 1/6.</p>",
    },
    {
        "text": "<p>Convert 2π/9 radians to degrees.</p>",
        "choices": ["40", "20", "80", "90"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> (2/9) × 180 = 40.</p>",
    },
    {
        "text": "<p>A circular running track has a radius of 50 metres. A runner "
                "goes along an arc with a central angle of 72°. How far does the "
                "runner travel, in metres?</p>",
        "choices": ["20π", "10π", "100π", "36π"],
        "correct": "20π",
        "explanation": "<p><strong>20π.</strong> Ulush 72/360 = 1/5; aylana "
                       "uzunligi 100π; beshdan biri 20π.</p>"
                       "<p><strong>100π</strong> — butun aylana boʻylab yugurilgan "
                       "deb hisoblangan.</p>",
    },
]


# =====================================================================
# SAT-78 — area of a sector
# =====================================================================

Q_SAT78 = [
    {
        "text": "<p>In a circle with center <i>O</i> and radius 10, sector <i>AOB</i> "
                "has a central angle of 72°. What is the area of sector <i>AOB</i>?</p>",
        "choices": ["20π", "4π", "25π", "100π"],
        "correct": "20π",
        "explanation": "<p><strong>20π.</strong> Ulush 1/5, butun yuza 100π.</p>"
                       "<p><strong>4π</strong> — bu yoy uzunligi; yuza uchun "
                       "«butun» πr² boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A circle has radius 9. What is the area of a sector with a "
                "central angle of 120°?</p>",
        "choices": ["27π", "6π", "81π", "9π"],
        "correct": "27π",
        "explanation": "<p><strong>27π.</strong> Ulush 1/3, butun yuza 81π.</p>"
                       "<p><strong>6π</strong> — yoy uzunligi.</p>",
    },
    {
        "text": "<p>A circle has radius 6. What is the area of a sector with a "
                "central angle of 60°?</p>",
        "choices": ["6π", "2π", "36π", "12π"],
        "correct": "6π",
        "explanation": "<p><strong>6π.</strong> (1/6) × 36π.</p>",
    },
    {
        "text": "<p>A circle has radius 6. What is the area of a sector with a "
                "central angle of 90°?</p>",
        "choices": ["9π", "3π", "18π", "36π"],
        "correct": "9π",
        "explanation": "<p><strong>9π.</strong> Chorak aylana: (1/4) × 36π.</p>",
    },
    {
        "text": "<p>A circle has radius 4. What is the area of a sector with a "
                "central angle of 45°?</p>",
        "choices": ["2π", "π", "16π", "4π"],
        "correct": "2π",
        "explanation": "<p><strong>2π.</strong> 45/360 = 1/8; 16π ning "
                       "sakkizdan biri.</p>",
    },
    {
        "text": "<p>A circle has radius 12. What is the area of a sector with a "
                "central angle of 30°?</p>",
        "choices": ["12π", "2π", "144π", "24π"],
        "correct": "12π",
        "explanation": "<p><strong>12π.</strong> 30/360 = 1/12; 144π ning "
                       "oʻn ikkidan biri.</p>",
    },
    {
        "text": "<p>A sector of a circle of radius 6 has area 8π. What is the "
                "measure, in degrees, of its central angle?</p>",
        "choices": ["80", "60", "120", "40"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 8π ÷ 36π = 2/9; (2/9) × 360 = 80.</p>"
                       "<p><strong>40</strong> — ulush toʻgʻri, lekin 360 emas, "
                       "180 ga koʻpaytirilgan.</p>",
    },
    {
        "text": "<p>A sector of a circle of radius 4 has area 2π. What is the "
                "measure, in degrees, of its central angle?</p>",
        "choices": ["45", "90", "30", "60"],
        "correct": "45",
        "explanation": "<p><strong>45.</strong> 2π ÷ 16π = 1/8; (1/8) × 360 = 45.</p>",
    },
    {
        "text": "<p>A sector of a circle of radius 6 has area 6π. What is the "
                "measure, in degrees, of its central angle?</p>",
        "choices": ["60", "90", "30", "120"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> 6π ÷ 36π = 1/6.</p>",
    },
    {
        "text": "<p>A circle of radius 10 has a 90° sector removed. What is the "
                "area of the region that remains?</p>",
        "choices": ["75π", "25π", "100π", "50π"],
        "correct": "75π",
        "explanation": "<p><strong>75π.</strong> Qolgan burchak 270°, yaʼni 3/4 "
                       "of 100π.</p>"
                       "<p><strong>25π</strong> — olib tashlangan boʻlak; savol "
                       "qolganini soʻragan.</p>",
    },
    {
        "text": "<p>A circle of radius 8 has a 45° sector removed. What is the "
                "area of the region that remains?</p>",
        "choices": ["56π", "8π", "64π", "48π"],
        "correct": "56π",
        "explanation": "<p><strong>56π.</strong> 315/360 = 7/8; (7/8) × 64π. "
                       "Nazorat: 8π + 56π = 64π ✓</p>",
    },
    {
        "text": "<p>What fraction of a circle is a sector with a central angle of "
                "π/6 radians?</p>",
        "choices": ["1/12", "1/6", "1/3", "1/4"],
        "correct": "1/12",
        "explanation": "<p><strong>1/12.</strong> (π/6) ÷ 2π = 1/12. "
                       "π/6 — bu 30°.</p>"
                       "<p><strong>1/6</strong> — maxrajga qarab javob berilgan.</p>",
    },
    {
        "text": "<p>A circle has radius 6. What is the length of the arc cut off "
                "by a central angle of 60°?</p>",
        "choices": ["2π", "6π", "12π", "3π"],
        "correct": "2π",
        "explanation": "<p><strong>2π.</strong> Oʻsha 1/6 ulush, lekin bu safar "
                       "12π ga koʻpaytiriladi.</p>"
                       "<p><strong>6π</strong> — bu sektor yuzasi.</p>",
    },
    {
        "text": "<p>A sector of a circle has radius 6 and a central angle of 60°. "
                "What is the perimeter of the sector?</p>",
        "choices": ["12 + 2π", "2π", "12 + 6π", "6 + 2π"],
        "correct": "12 + 2π",
        "explanation": "<p><strong>12 + 2π.</strong> Ikkita radius (6 + 6) plyus "
                       "yoy (2π).</p>"
                       "<p><strong>2π</strong> — faqat yoy; radiuslar "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>If the radius of a circle is doubled, the area of a sector with "
                "the same central angle is multiplied by what factor?</p>",
        "choices": ["4", "2", "8", "1"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> Yuzada radius kvadratga koʻtariladi. "
                       "Yoy esa faqat 2 barobar ortadi.</p>",
    },
    {
        "text": "<p>A circle has radius 3. What is the area of a sector with a "
                "central angle of 240°?</p>",
        "choices": ["6π", "3π", "9π", "4π"],
        "correct": "6π",
        "explanation": "<p><strong>6π.</strong> 240/360 = 2/3; (2/3) × 9π.</p>",
    },
    {
        "text": "<p>A circle has radius 5. What is the area of a sector with a "
                "central angle of 36°?</p>",
        "choices": ["5π/2", "π/2", "10π", "25π"],
        "correct": "5π/2",
        "explanation": "<p><strong>5π/2.</strong> 36/360 = 1/10; 25π ning oʻndan "
                       "biri.</p>",
    },
    {
        "text": "<p>What is the area of a semicircle of radius 8?</p>",
        "choices": ["32π", "64π", "16π", "8π"],
        "correct": "32π",
        "explanation": "<p><strong>32π.</strong> Yarim aylana — 180°, yaʼni "
                       "ulush 1/2 of 64π.</p>",
    },
    {
        "text": "<p>A sector of a circle of radius 6 has area 9π. What is the "
                "measure, in degrees, of its central angle?</p>",
        "choices": ["90", "60", "120", "45"],
        "correct": "90",
        "explanation": "<p><strong>90.</strong> 9π ÷ 36π = 1/4.</p>",
    },
    {
        "text": "<p>A pizza with a radius of 12 inches is cut into 8 equal slices. "
                "What is the area, in square inches, of one slice?</p>",
        "choices": ["18π", "24π", "144π", "3π"],
        "correct": "18π",
        "explanation": "<p><strong>18π.</strong> Har bir boʻlak 45°, yaʼni 1/8 "
                       "of 144π.</p>"
                       "<p><strong>3π</strong> — bu bir boʻlakning yoyi "
                       "(qirrasi), yuzasi emas.</p>",
    },
]


# =====================================================================
# SAT-79 — circle equations
# =====================================================================

Q_SAT79 = [
    {
        "text": "<p>In the xy-plane, the equation of a circle is "
                "(<i>x</i> − 3)² + (<i>y</i> + 2)² = 25. What is the center?</p>",
        "choices": ["(3, −2)", "(−3, 2)", "(3, 2)", "(−3, −2)"],
        "correct": "(3, −2)",
        "explanation": "<p><strong>(3, −2).</strong> Qavsdagi ishoralarni "
                       "agʻdaring.</p>"
                       "<p><strong>(−3, 2)</strong> — qavsdagi sonlar "
                       "koʻchirilgan; bu eng koʻp uchraydigan xato.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "(<i>x</i> − 3)² + (<i>y</i> + 2)² = 25?</p>",
        "choices": ["5", "25", "√5", "12.5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Oʻng tomonda r² turadi.</p>"
                       "<p><strong>25</strong> — r² ning oʻzi olingan.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "(<i>x</i> + 1)² + (<i>y</i> − 7)² = 36?</p>",
        "choices": ["(−1, 7)", "(1, −7)", "(1, 7)", "(−1, −7)"],
        "correct": "(−1, 7)",
        "explanation": "<p><strong>(−1, 7).</strong> (x + 1) = (x − (−1)).</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "(<i>x</i> + 1)² + (<i>y</i> − 7)² = 36?</p>",
        "choices": ["6", "36", "18", "√6"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> √36 = 6.</p>",
    },
    {
        "text": "<p>A circle in the xy-plane has center (−4, 6) and radius 3. "
                "Which is an equation of the circle?</p>",
        "choices": ["(<i>x</i> + 4)² + (<i>y</i> − 6)² = 9",
                    "(<i>x</i> − 4)² + (<i>y</i> + 6)² = 9",
                    "(<i>x</i> + 4)² + (<i>y</i> − 6)² = 3",
                    "(<i>x</i> − 4)² + (<i>y</i> + 6)² = 3"],
        "correct": "(<i>x</i> + 4)² + (<i>y</i> − 6)² = 9",
        "explanation": "<p><strong>(x + 4)² + (y − 6)² = 9.</strong> h = −4 → "
                       "x − (−4); oʻng tomon 3² = 9.</p>"
                       "<p>Oxirgi ikkitasida oʻng tomonga radiusning oʻzi "
                       "yozilgan.</p>",
    },
    {
        "text": "<p>A circle has center (0, −5) and radius 2. Which is an equation "
                "of the circle?</p>",
        "choices": ["<i>x</i>² + (<i>y</i> + 5)² = 4",
                    "<i>x</i>² + (<i>y</i> − 5)² = 4",
                    "<i>x</i>² + (<i>y</i> + 5)² = 2",
                    "(<i>x</i> + 5)² + <i>y</i>² = 4"],
        "correct": "<i>x</i>² + (<i>y</i> + 5)² = 4",
        "explanation": "<p><strong>x² + (y + 5)² = 4.</strong> h = 0, k = −5, "
                       "r² = 4.</p>",
    },
    {
        "text": "<p>A circle has center (2, 1) and radius 3. Which is an equation "
                "of the circle?</p>",
        "choices": ["(<i>x</i> − 2)² + (<i>y</i> − 1)² = 9",
                    "(<i>x</i> + 2)² + (<i>y</i> + 1)² = 9",
                    "(<i>x</i> − 2)² + (<i>y</i> − 1)² = 3",
                    "(<i>x</i> − 1)² + (<i>y</i> − 2)² = 9"],
        "correct": "(<i>x</i> − 2)² + (<i>y</i> − 1)² = 9",
        "explanation": "<p><strong>(x − 2)² + (y − 1)² = 9.</strong> Oxirgi "
                       "variantda koordinatalar oʻrni almashib ketgan.</p>",
    },
    {
        "text": "<p>What is the radius of the circle <i>x</i>² + <i>y</i>² = 49?</p>",
        "choices": ["7", "49", "24.5", "√7"],
        "correct": "7",
        "explanation": "<p><strong>7.</strong> √49 = 7.</p>",
    },
    {
        "text": "<p>What is the center of the circle <i>x</i>² + <i>y</i>² = 49?</p>",
        "choices": ["(0, 0)", "(7, 7)", "(49, 49)", "(0, 7)"],
        "correct": "(0, 0)",
        "explanation": "<p><strong>(0, 0).</strong> h va k ikkalasi ham nol.</p>",
    },
    {
        "text": "<p>Where is the point (6, 1) relative to the circle "
                "(<i>x</i> − 2)² + (<i>y</i> − 1)² = 16?</p>",
        "choices": ["On the circle", "Inside the circle",
                    "Outside the circle", "At the center"],
        "correct": "On the circle",
        "explanation": "<p><strong>On the circle.</strong> 16 + 0 = 16, aynan "
                       "r² ga teng.</p>",
    },
    {
        "text": "<p>Where is the origin (0, 0) relative to the circle "
                "(<i>x</i> − 3)² + (<i>y</i> − 4)² = 20?</p>",
        "choices": ["Outside the circle", "Inside the circle",
                    "On the circle", "At the center"],
        "correct": "Outside the circle",
        "explanation": "<p><strong>Outside.</strong> 9 + 16 = 25, va 25 > 20.</p>",
    },
    {
        "text": "<p>Where is the point (2, −1) relative to the circle "
                "(<i>x</i> − 1)² + (<i>y</i> + 2)² = 10?</p>",
        "choices": ["Inside the circle", "On the circle",
                    "Outside the circle", "At the center"],
        "correct": "Inside the circle",
        "explanation": "<p><strong>Inside.</strong> 1 + 1 = 2, va 2 &lt; 10.</p>",
    },
    {
        "text": "<p>A circle has center (2, 2) and passes through (2, 7). "
                "What is its radius?</p>",
        "choices": ["5", "7", "9", "√5"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Nuqtalar bir vertikalda: 7 − 2.</p>",
    },
    {
        "text": "<p>A circle has center (0, 0) and passes through (6, 8). "
                "What is its radius?</p>",
        "choices": ["10", "14", "48", "√14"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> 6-8-10 uchligi (3-4-5 ning "
                       "ikkilangani).</p>"
                       "<p><strong>14</strong> — koordinatalar qoʻshilgan.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "(<i>x</i> − 5)² + (<i>y</i> + 1)² = 12?</p>",
        "choices": ["2√3", "12", "6", "4√3"],
        "correct": "2√3",
        "explanation": "<p><strong>2√3.</strong> √12 = √4 × √3 = 2√3 ≈ 3.46.</p>"
                       "<p><strong>6</strong> — 12 ning yarmi olingan.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + (<i>y</i> − 4)² = 1?</p>",
        "choices": ["(0, 4)", "(4, 0)", "(0, −4)", "(1, 4)"],
        "correct": "(0, 4)",
        "explanation": "<p><strong>(0, 4).</strong> x had qavssiz — h = 0.</p>",
    },
    {
        "text": "<p>The endpoints of a diameter of a circle are (1, 2) and (7, 10). "
                "What is the center?</p>",
        "choices": ["(4, 6)", "(8, 12)", "(3, 4)", "(6, 8)"],
        "correct": "(4, 6)",
        "explanation": "<p><strong>(4, 6).</strong> Markaz — diametrning "
                       "oʻrtasi: ((1+7)/2, (2+10)/2).</p>"
                       "<p><strong>(8, 12)</strong> — koordinatalar qoʻshilgan, "
                       "ikkiga boʻlinmagan.</p>",
    },
    {
        "text": "<p>The endpoints of a diameter of a circle are (1, 2) and (7, 10). "
                "What is the radius?</p>",
        "choices": ["5", "10", "14", "√10"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Diametr √(36 + 64) = 10, "
                       "radius uning yarmi.</p>"
                       "<p><strong>10</strong> — bu diametr, radius emas.</p>",
    },
    {
        "text": "<p>A circle has center (3, −1) and radius 4. Which point lies "
                "on the circle?</p>",
        "choices": ["(7, −1)", "(3, 4)", "(4, −1)", "(7, 4)"],
        "correct": "(7, −1)",
        "explanation": "<p><strong>(7, −1).</strong> Markazdan oʻngga 4 birlik: "
                       "masofa aynan 4.</p>",
    },
    {
        "text": "<p>On a map, a circular park is centred at the point (4, 3) and "
                "has a radius of 6 units. Which equation represents the edge of "
                "the park?</p>",
        "choices": ["(<i>x</i> − 4)² + (<i>y</i> − 3)² = 36",
                    "(<i>x</i> + 4)² + (<i>y</i> + 3)² = 36",
                    "(<i>x</i> − 4)² + (<i>y</i> − 3)² = 6",
                    "(<i>x</i> − 3)² + (<i>y</i> − 4)² = 36"],
        "correct": "(<i>x</i> − 4)² + (<i>y</i> − 3)² = 36",
        "explanation": "<p><strong>(x − 4)² + (y − 3)² = 36.</strong> Markaz "
                       "musbat, demak qavsda minus; oʻng tomon 6² = 36.</p>",
    },
]


# =====================================================================
# SAT-80 — completing the square
# =====================================================================

Q_SAT80 = [
    {
        "text": "<p>The graph of <i>x</i>² + <i>y</i>² − 4<i>x</i> − 10<i>y</i> + 20 = 0 "
                "in the xy-plane is a circle. What is the length of the radius?</p>",
        "choices": ["3", "9", "5", "2"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> (x − 2)² + (y − 5)² = −20 + 4 + 25 "
                       "= 9, demak r = √9.</p>"
                       "<p><strong>9</strong> — bu r²; oxirgi qadam "
                       "unutilgan.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + <i>y</i>² − 4<i>x</i> − 10<i>y</i> + 20 = 0?</p>",
        "choices": ["(2, 5)", "(−2, −5)", "(4, 10)", "(−4, −10)"],
        "correct": "(2, 5)",
        "explanation": "<p><strong>(2, 5).</strong> Koeffitsiyentlarning yarmi, "
                       "ishorasi agʻdarilgan.</p>"
                       "<p><strong>(4, 10)</strong> — yarmi olinmagan.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + <i>y</i>² − 8<i>x</i> + 6<i>y</i> = 0?</p>",
        "choices": ["(4, −3)", "(−4, 3)", "(8, −6)", "(−8, 6)"],
        "correct": "(4, −3)",
        "explanation": "<p><strong>(4, −3).</strong> −8 ning yarmi −4 → h = 4; "
                       "6 ning yarmi 3 → k = −3.</p>"
                       "<p><strong>(8, −6)</strong> — yarmi olinmagan.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² − 8<i>x</i> + 6<i>y</i> = 0?</p>",
        "choices": ["5", "25", "10", "7"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> Oʻng tomon 0 + 16 + 9 = 25.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + <i>y</i>² − 6<i>x</i> + 4<i>y</i> − 12 = 0?</p>",
        "choices": ["(3, −2)", "(−3, 2)", "(6, −4)", "(3, 2)"],
        "correct": "(3, −2)",
        "explanation": "<p><strong>(3, −2).</strong> Yarmi: −3 va 2; ishorani "
                       "agʻdaring.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² − 6<i>x</i> + 4<i>y</i> − 12 = 0?</p>",
        "choices": ["5", "25", "12", "√12"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> 12 + 9 + 4 = 25.</p>"
                       "<p><strong>√12</strong> — ozod haddan toʻgʻridan-toʻgʻri "
                       "ildiz olingan.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + <i>y</i>² + 10<i>x</i> − 2<i>y</i> + 17 = 0?</p>",
        "choices": ["(−5, 1)", "(5, −1)", "(−10, 2)", "(10, −2)"],
        "correct": "(−5, 1)",
        "explanation": "<p><strong>(−5, 1).</strong> 10 ning yarmi 5 → h = −5.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² + 10<i>x</i> − 2<i>y</i> + 17 = 0?</p>",
        "choices": ["3", "9", "17", "√17"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> −17 + 25 + 1 = 9. Oʻng tomon "
                       "manfiydan boshlansa ham musbat chiqishi mumkin.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² − 2<i>x</i> − 8 = 0?</p>",
        "choices": ["3", "9", "8", "2√2"],
        "correct": "3",
        "explanation": "<p><strong>3.</strong> (x − 1)² + y² = 8 + 1 = 9. "
                       "y hadi allaqachon toʻliq.</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + <i>y</i>² + 6<i>y</i> + 5 = 0?</p>",
        "choices": ["(0, −3)", "(0, 3)", "(0, −6)", "(−3, 0)"],
        "correct": "(0, −3)",
        "explanation": "<p><strong>(0, −3).</strong> x hadi yoʻq, demak h = 0.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² + 6<i>y</i> + 5 = 0?</p>",
        "choices": ["2", "4", "5", "√5"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> −5 + 9 = 4, demak r = 2.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² − 12<i>x</i> + 4<i>y</i> + 15 = 0?</p>",
        "choices": ["5", "25", "15", "√15"],
        "correct": "5",
        "explanation": "<p><strong>5.</strong> −15 + 36 + 4 = 25.</p>",
    },
    {
        "text": "<p>What number completes the square for <i>x</i>² − 6<i>x</i>?</p>",
        "choices": ["9", "3", "36", "−3"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Yarmi −3, kvadrati 9.</p>"
                       "<p><strong>3</strong> — bu qavsga tushadigan son, "
                       "qoʻshiladigani emas.</p>",
    },
    {
        "text": "<p>What number completes the square for <i>y</i>² + 10<i>y</i>?</p>",
        "choices": ["25", "5", "100", "−5"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> Yarmi 5, kvadrati 25.</p>",
    },
    {
        "text": "<p>Which expression is equal to <i>x</i>² − 6<i>x</i> + 9?</p>",
        "choices": ["(<i>x</i> − 3)²", "(<i>x</i> − 9)²",
                    "(<i>x</i> + 3)²", "(<i>x</i> − 6)²"],
        "correct": "(<i>x</i> − 3)²",
        "explanation": "<p><strong>(x − 3)².</strong> Qavsga koeffitsiyentning "
                       "yarmi tushadi, kvadrati emas.</p>",
    },
    {
        "text": "<p>What does the graph of "
                "<i>x</i>² + <i>y</i>² − 2<i>x</i> + 2<i>y</i> + 2 = 0 describe?</p>",
        "choices": ["A single point", "A circle of radius 1",
                    "A circle of radius 2", "Nothing at all"],
        "correct": "A single point",
        "explanation": "<p><strong>A single point.</strong> (x − 1)² + (y + 1)² "
                       "= −2 + 1 + 1 = 0, yaʼni radius nol: (1, −1).</p>",
    },
    {
        "text": "<p>What is the center of the circle "
                "<i>x</i>² + <i>y</i>² + 4<i>x</i> − 6<i>y</i> − 3 = 0?</p>",
        "choices": ["(−2, 3)", "(2, −3)", "(−4, 6)", "(4, −6)"],
        "correct": "(−2, 3)",
        "explanation": "<p><strong>(−2, 3).</strong> Yarmi 2 va −3; ishorani "
                       "agʻdaring.</p>",
    },
    {
        "text": "<p>What is the radius of the circle "
                "<i>x</i>² + <i>y</i>² + 4<i>x</i> − 6<i>y</i> − 3 = 0?</p>",
        "choices": ["4", "16", "3", "√3"],
        "correct": "4",
        "explanation": "<p><strong>4.</strong> 3 + 4 + 9 = 16.</p>",
    },
    {
        "text": "<p>When completing the square, why must the number you add also be "
                "added to the other side?</p>",
        "choices": ["To keep the equation balanced",
                    "To make the radius larger",
                    "Because the center must be positive",
                    "To remove the constant term"],
        "correct": "To keep the equation balanced",
        "explanation": "<p><strong>To keep the equation balanced.</strong> Faqat "
                       "bir tomonga qoʻshilsa, tenglama boshqa aylanani "
                       "tasvirlaydi.</p>",
    },
    {
        "text": "<p>A circle is described by "
                "<i>x</i>² + <i>y</i>² − 14<i>x</i> + 2<i>y</i> + 40 = 0. "
                "What is the length of the radius?</p>",
        "choices": ["√10", "10", "40", "5"],
        "correct": "√10",
        "explanation": "<p><strong>√10.</strong> (x − 7)² + (y + 1)² = −40 + 49 "
                       "+ 1 = 10, va radius √10 ≈ 3.16.</p>"
                       "<p><strong>10</strong> — bu r²; javob ildiz ostida "
                       "qolishi ham mumkin.</p>",
    },
]


PRACTICES = [
    {
        "title":       "SAT-76 Practice: Trigonometric Identities — sin(x) = cos(90° − x)",
        "description": "20 ta SAT uslubidagi savol — toʻldiruvchi burchak ayniyati, "
                       "sin² + cos² = 1 va tangensning teskarisi.",
        "tutorial":    "SAT-76:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT76,
    },
    {
        "title":       "SAT-77 Practice: Radians vs. Degrees and Arc Length",
        "description": "20 ta SAT uslubidagi savol — 180° = π koʻprigi, ikki "
                       "yoʻnalishda oʻgirish va yoy uzunligi ulush sifatida.",
        "tutorial":    "SAT-77:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT77,
    },
    {
        "title":       "SAT-78 Practice: Area of a Sector of a Circle",
        "description": "20 ta SAT uslubidagi savol — sektor yuzasi, teskari savol, "
                       "qolgan soha va yoy bilan farqi.",
        "tutorial":    "SAT-78:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT78,
    },
    {
        "title":       "SAT-79 Practice: Circle Equations in the Coordinate Plane",
        "description": "20 ta SAT uslubidagi savol — markaz va radiusni oʻqish, "
                       "ishora tuzogʻi va nuqtaning aylanaga nisbati.",
        "tutorial":    "SAT-79:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT79,
    },
    {
        "title":       "SAT-80 Practice: Completing the Square to Find a Circle's Center and Radius",
        "description": "20 ta SAT uslubidagi savol — yarmi/kvadrati/ikkala tomonga, "
                       "va oxirgi qadam: radius = √r².",
        "tutorial":    "SAT-80:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT80,
    },
]
