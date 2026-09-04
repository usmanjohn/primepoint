# -*- coding: utf-8 -*-
"""Prime SAT mashqlar — SAT-51 … SAT-55.

20 savoldan iborat test, har biri oʻz darsiga bogʻlangan.
Written with STYLE_GUIDE_PS_PRACTICE.md · lesson list in toc_ps_practices.txt

⚠️ Blok C: hisoblash yengil, jumla ogʻir. Interpretatsiya savollari koʻp.
⚠️ Savollar INGLIZCHA, tushuntirishlar OʻZBEKCHA.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_ps_51_55.py --master=prime \\
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
# SAT-51 — percentages
# =====================================================================

Q_SAT51 = [
    {
        "text": "<p>What is 20% of 150?</p>",
        "choices": ["30", "75", "3", "300"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> 0.20 × 150.</p>"
                       "<p>Tez yoʻl: 10 foizi 15, demak 20 foizi 30.</p>",
    },
    {
        "text": "<p>What is 35% of 240?</p>",
        "choices": ["84", "72", "96", "68"],
        "correct": "84",
        "explanation": "<p><strong>84.</strong> 0.35 × 240, yoki 120 − 36.</p>"
                       "<p>50 foizi 120, 15 foizi 36 — ayirsangiz 84.</p>",
    },
    {
        "text": "<p>12 is what percent of 48?</p>",
        "choices": ["25%", "40%", "4%", "400%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 12 ÷ 48 = 0.25.</p>"
                       "<p>Foizni topish uchun qismni butunga boʻling.</p>",
    },
    {
        "text": "<p>24 is 40% of what number?</p>",
        "choices": ["60", "9.6", "64", "96"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> 24 ÷ 0.40.</p>"
                       "<p><strong>9.6</strong> — koʻpaytirilgan; butun qismdan "
                       "katta boʻlishi kerak.</p>",
    },
    {
        "text": "<p>A jacket costs 80,000 som. The price rises by 15%. What is the new "
                "price?</p>",
        "choices": ["92,000 som", "12,000 som", "95,000 som", "68,000 som"],
        "correct": "92,000 som",
        "explanation": "<p><strong>92,000.</strong> 80,000 × 1.15.</p>"
                       "<p><strong>12,000</strong> — bu faqat oʻsish miqdori, "
                       "yangi narx emas.</p>",
    },
    {
        "text": "<p>45 is what percent of 300?</p>",
        "choices": ["15%", "45%", "6.7%", "150%"],
        "correct": "15%",
        "explanation": "<p><strong>15%.</strong> 45 ÷ 300 = 0.15.</p>",
    },
    {
        "text": "<p>What is 7% of 2,400?</p>",
        "choices": ["168", "1,680", "16.8", "340"],
        "correct": "168",
        "explanation": "<p><strong>168.</strong> 1 foizi 24, demak 7 foizi 168.</p>"
                       "<p>1 foizni topib koʻpaytirish eng tez yoʻl.</p>",
    },
    {
        "text": "<p>In a class of 40, 65% passed. How many failed?</p>",
        "choices": ["14", "26", "35", "6"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Oʻtganlar 26, demak "
                       "40 − 26 = 14.</p>"
                       "<p><strong>26</strong> — oʻtganlar soni. Savol "
                       "yiqilganlarni soʻragan.</p>",
    },
    {
        "text": "<p>70% of the students take the bus, and 30% of those students are in "
                "Grade 9. What percent of all students are Grade 9 bus riders?</p>",
        "choices": ["21%", "100%", "40%", "30%"],
        "correct": "21%",
        "explanation": "<p><strong>21%.</strong> 0.30 × 0.70.</p>"
                       "<p>100 oʻquvchi bilan tekshiring: 70 avtobusda, ularning "
                       "30 foizi 21 kishi.</p>",
    },
    {
        "text": "<p>A number is 120% of 45. What is it?</p>",
        "choices": ["54", "37.5", "9", "165"],
        "correct": "54",
        "explanation": "<p><strong>54.</strong> 1.2 × 45.</p>"
                       "<p>100 dan katta foiz — natija asl sondan katta boʻladi.</p>",
    },
    {
        "text": "<p>In a survey, 480 of 600 people said yes. What percent said "
                "no?</p>",
        "choices": ["20%", "80%", "120%", "12%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> Yoʻq deganlar 120, va "
                       "120 ÷ 600 = 0.20.</p>"
                       "<p><strong>80%</strong> — ha deganlar. Savolning oxirgi "
                       "soʻzini oʻqing.</p>",
    },
    {
        "text": "<p>A shop's sales were 250 units in May and 300 in June. June's sales "
                "are what percent of May's?</p>",
        "choices": ["120%", "20%", "83%", "50%"],
        "correct": "120%",
        "explanation": "<p><strong>120%.</strong> 300 ÷ 250 = 1.2.</p>"
                       "<p><strong>20%</strong> — bu oʻsish (SAT-52). Savol "
                       "«what percent of» degan, oʻsishni emas.</p>",
    },
    {
        "text": "<p>A tank is 40% full and holds 240 litres at that level. What is its "
                "full capacity?</p>",
        "choices": ["600 litres", "96 litres", "336 litres", "480 litres"],
        "correct": "600 litres",
        "explanation": "<p><strong>600 litr.</strong> 240 ÷ 0.40.</p>"
                       "<p>Butun izlanmoqda, demak boʻlish kerak.</p>",
    },
    {
        "text": "<p>Of 200 workers, 60% are men and 25% of the men work night shifts. "
                "How many men work night shifts?</p>",
        "choices": ["30", "50", "120", "85"],
        "correct": "30",
        "explanation": "<p><strong>30.</strong> Erkaklar 120, ularning 25 foizi "
                       "30.</p>"
                       "<p><strong>50</strong> — 25 foiz hammadan olingan.</p>",
    },
    {
        "text": "<p>A student computes '18 is 30% of what' as 5.4. What is the correct "
                "answer?</p>",
        "choices": ["60", "5.4", "54", "6"],
        "correct": "60",
        "explanation": "<p><strong>60.</strong> Butunni topish uchun boʻlish "
                       "kerak.</p>"
                       "<p>Javob berilgan qismdan kichik chiqsa, u albatta "
                       "xato.</p>",
    },
    {
        "text": "<p>A student says that 50% of 40% is 90%. What is the correct "
                "answer?</p>",
        "choices": ["20%", "90%", "10%", "45%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> 0.5 × 0.4 = 0.2.</p>"
                       "<p>Foizlar faqat bir xil bazadan olinganda qoʻshiladi.</p>",
    },
    {
        "text": "<p>15% of a number is 9. What is 40% of that number?</p>",
        "choices": ["24", "3.6", "60", "36"],
        "correct": "24",
        "explanation": "<p><strong>24.</strong> Son 60 (9 ÷ 0.15), va 40 foizi "
                       "24.</p>"
                       "<p>Ikki bosqichli: avval butunni toping, keyin yangi "
                       "foizni.</p>",
    },
    {
        "text": "<p>A price of 60,000 som is 75% of the original price. What was the "
                "original?</p>",
        "choices": ["80,000 som", "45,000 som", "105,000 som", "135,000 som"],
        "correct": "80,000 som",
        "explanation": "<p><strong>80,000.</strong> 60,000 ÷ 0.75.</p>"
                       "<p>Tekshiruv: 80,000 ning 75 foizi 60,000 ✓</p>",
    },
    {
        "text": "<p>A farmer plants 35% of a 400-hectare field with wheat and 20% with "
                "barley. How many hectares are left?</p>",
        "choices": ["180", "220", "140", "80"],
        "correct": "180",
        "explanation": "<p><strong>180 gektar.</strong> 55 foizi ekilgan, "
                       "45 foizi qolgan: 0.45 × 400.</p>"
                       "<p>Bu yerda foizlar qoʻshiladi — chunki ikkalasi ham "
                       "bir xil bazadan (400 gektar).</p>",
    },
    {
        "text": "<p>A shop takes 12% commission on sales. If a seller received 44,000 "
                "som after commission, what were the sales?</p>",
        "choices": ["50,000 som", "49,280 som", "38,720 som", "36,667 som"],
        "correct": "50,000 som",
        "explanation": "<p><strong>50,000.</strong> Sotuvchi 88 foizni oladi, "
                       "demak 44,000 ÷ 0.88.</p>"
                       "<p><strong>49,280</strong> — 44,000 ga 12 foiz "
                       "qoʻshilgan; komissiya 50,000 dan olingan edi.</p>",
    },
]


# =====================================================================
# SAT-52 — percent change
# =====================================================================

Q_SAT52 = [
    {
        "text": "<p>A price rises from 60 to 75. What is the percent increase?</p>",
        "choices": ["25%", "20%", "15%", "80%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 15 ÷ 60.</p>"
                       "<p><strong>20%</strong> — 15 ÷ 75, yaʼni yangi qiymatga "
                       "boʻlingan.</p>",
    },
    {
        "text": "<p>A number falls from 120 to 90. What is the percent decrease?</p>",
        "choices": ["25%", "33%", "30%", "75%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> 30 ÷ 120.</p>"
                       "<p><strong>33%</strong> — 30 ÷ 90; maxrajda eski qiymat "
                       "turishi kerak.</p>",
    },
    {
        "text": "<p>A value increases by 25%. By what factor is it multiplied?</p>",
        "choices": ["1.25", "0.25", "0.75", "25"],
        "correct": "1.25",
        "explanation": "<p><strong>1.25.</strong> Eskisi (1) va qoʻshimchasi "
                       "(0.25).</p>",
    },
    {
        "text": "<p>A value decreases by 35%. By what factor is it multiplied?</p>",
        "choices": ["0.65", "1.35", "0.35", "0.35 then 1"],
        "correct": "0.65",
        "explanation": "<p><strong>0.65.</strong> 1 − 0.35 — qolgan qism.</p>",
    },
    {
        "text": "<p>A price is increased by 20% and then decreased by 20%. Compared "
                "with the original, the final price is</p>",
        "choices": ["4% lower", "the same", "4% higher", "40% lower"],
        "correct": "4% lower",
        "explanation": "<p><strong>4% past.</strong> 1.2 × 0.8 = 0.96.</p>"
                       "<p>Ikkinchi foiz kattaroq sondan olinadi, shuning uchun "
                       "ular tenglashmaydi.</p>",
    },
    {
        "text": "<p>A coat costs 500. It is discounted 30%, then a further 20% off the "
                "sale price. What is the final price?</p>",
        "choices": ["280", "250", "300", "240"],
        "correct": "280",
        "explanation": "<p><strong>280.</strong> 500 × 0.7 × 0.8.</p>"
                       "<p><strong>250</strong> — 50 foiz chegirma deb "
                       "hisoblangan; aslida jami 44 foiz.</p>",
    },
    {
        "text": "<p>After a 25% discount, a shirt costs 90,000 som. What was the "
                "original price?</p>",
        "choices": ["120,000 som", "112,500 som", "115,000 som", "67,500 som"],
        "correct": "120,000 som",
        "explanation": "<p><strong>120,000.</strong> 90,000 ÷ 0.75.</p>"
                       "<p><strong>112,500</strong> — 90,000 ga 25 foiz "
                       "qoʻshilgan; chegirma 120,000 dan olingan edi.</p>",
    },
    {
        "text": "<p>A population grows from 4,000 to 4,600. What is the percent "
                "increase?</p>",
        "choices": ["15%", "13%", "600%", "6%"],
        "correct": "15%",
        "explanation": "<p><strong>15%.</strong> 600 ÷ 4,000.</p>",
    },
    {
        "text": "<p>A quantity is increased to 140% of its original value. By what "
                "percent did it increase?</p>",
        "choices": ["40%", "140%", "60%", "14%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> «To 140%» va «by 40%» bir xil "
                       "narsa.</p>"
                       "<p><strong>140%</strong> — bu yangi qiymatning ulushi, "
                       "oʻsish emas.</p>",
    },
    {
        "text": "<p>A value is halved and then doubled. What is the net percent "
                "change?</p>",
        "choices": ["0%", "50% decrease", "100% increase", "25% decrease"],
        "correct": "0%",
        "explanation": "<p><strong>0%.</strong> 0.5 × 2 = 1.</p>"
                       "<p>Bu yerda ular tenglashadi, chunki koeffitsientlar "
                       "bir-birining teskarisi — 0.8 va 1.2 esa emas.</p>",
    },
    {
        "text": "<p>A shop's takings fell 10% one month and rose 10% the next. What "
                "happened over the two months?</p>",
        "choices": ["A 1% fall", "No change", "A 1% rise", "A 20% fall"],
        "correct": "A 1% fall",
        "explanation": "<p><strong>1 foiz pasayish.</strong> 0.9 × 1.1 = 0.99.</p>"
                       "<p>Tartib ahamiyatsiz — natija oʻsha-oʻsha.</p>",
    },
    {
        "text": "<p>A city's budget rose by 5% each year for two years. What was the "
                "total percent increase?</p>",
        "choices": ["10.25%", "10%", "25%", "5%"],
        "correct": "10.25%",
        "explanation": "<p><strong>10.25%.</strong> 1.05 × 1.05 = 1.1025.</p>"
                       "<p>Ketma-ket oʻsishlar qoʻshilmaydi — ikkinchi yil "
                       "kattaroq summadan olinadi.</p>",
    },
    {
        "text": "<p>A shirt is marked up 50% and then put on sale at 20% off. Compared "
                "with the cost price, the sale price is</p>",
        "choices": ["20% higher", "30% higher", "the same", "70% higher"],
        "correct": "20% higher",
        "explanation": "<p><strong>20 foiz baland.</strong> 1.5 × 0.8 = 1.2.</p>"
                       "<p><strong>30% higher</strong> — 50 dan 20 ayirilgan, "
                       "yaʼni foizlar qoʻshilgan.</p>",
    },
    {
        "text": "<p>Which change leaves a value unchanged after a 25% increase?</p>",
        "choices": ["A 20% decrease", "A 25% decrease", "A 75% decrease",
                    "A 30% decrease"],
        "correct": "A 20% decrease",
        "explanation": "<p><strong>20 foiz pasayish.</strong> 1.25 × 0.8 = 1.</p>"
                       "<p>Qaytish uchun kerakli foiz oshirish foizidan har doim "
                       "<b>kichik</b> boʻladi.</p>",
    },
    {
        "text": "<p>A student computes the decrease from 80 to 60 as 33%. What is the "
                "correct answer?</p>",
        "choices": ["25%", "33%", "20%", "75%"],
        "correct": "25%",
        "explanation": "<p><strong>25%.</strong> Oʻquvchi 20 ni 60 ga boʻlgan.</p>"
                       "<p>Foiz oʻzgarishi har doim boshlangʻich qiymatdan "
                       "oʻlchanadi.</p>",
    },
    {
        "text": "<p>A student says a 20% rise followed by a 20% fall returns the price "
                "to its start. What actually happens?</p>",
        "choices": ["It ends 4% lower", "It ends the same", "It ends 4% higher",
                    "It ends 40% lower"],
        "correct": "It ends 4% lower",
        "explanation": "<p><strong>4 foiz past.</strong> 1.2 × 0.8 = 0.96.</p>"
                       "<p>Ikki foiz boshqa-boshqa sondan olingan.</p>",
    },
    {
        "text": "<p>A quantity falls by 40% and then rises by 40%. What is the net "
                "change?</p>",
        "choices": ["A 16% decrease", "No change", "A 16% increase",
                    "An 80% decrease"],
        "correct": "A 16% decrease",
        "explanation": "<p><strong>16 foiz pasayish.</strong> 0.6 × 1.4 = 0.84.</p>"
                       "<p>Foiz qanchalik katta boʻlsa, yoʻqotish ham shunchalik "
                       "katta: 20 foizda 4, 40 foizda 16.</p>",
    },
    {
        "text": "<p>A price after two successive 10% discounts is 81,000 som. What was "
                "the original price?</p>",
        "choices": ["100,000 som", "99,000 som", "90,000 som", "101,250 som"],
        "correct": "100,000 som",
        "explanation": "<p><strong>100,000.</strong> 0.9 × 0.9 = 0.81, va "
                       "81,000 ÷ 0.81.</p>"
                       "<p><strong>90,000</strong> — faqat bitta chegirma "
                       "hisobga olingan.</p>",
    },
    {
        "text": "<p>A phone cost 900,000 som last year and 720,000 som this year. What "
                "is the percent decrease?</p>",
        "choices": ["20%", "25%", "18%", "80%"],
        "correct": "20%",
        "explanation": "<p><strong>20%.</strong> 180,000 ÷ 900,000.</p>"
                       "<p><strong>25%</strong> — yangi narxga boʻlingan.</p>",
    },
    {
        "text": "<p>A farmer's yield rose 20% in one year and fell 25% the next. "
                "Compared with two years ago, the yield is now</p>",
        "choices": ["10% lower", "5% lower", "5% higher", "the same"],
        "correct": "10% lower",
        "explanation": "<p><strong>10 foiz past.</strong> 1.2 × 0.75 = 0.9.</p>"
                       "<p><strong>5% lower</strong> — foizlar ayirilgan "
                       "(25 − 20), bu esa notoʻgʻri amal.</p>",
    },
]


# =====================================================================
# SAT-53 — tables, graphs, bar charts
# =====================================================================
# Ustunli diagramma: Mon 30, Tue 45, Wed 25, Thu 50, Fri 40 (jami 190)
# Ikki tomonlama jadval: 9-sinf 24 piyoda / 16 avtobus; 10-sinf 18 / 22

Q_SAT53 = [
    {
        "text": "<p>A bar chart shows books borrowed: Monday 30, Tuesday 45, Wednesday "
                "25, Thursday 50, Friday 40. On which day were the most books "
                "borrowed?</p>",
        "choices": ["Thursday", "Tuesday", "Friday", "Monday"],
        "correct": "Thursday",
        "explanation": "<p><strong>Payshanba.</strong> 50 — eng katta qiymat.</p>",
    },
    {
        "text": "<p>Using that chart, how many books were borrowed in the whole "
                "week?</p>",
        "choices": ["190", "180", "200", "150"],
        "correct": "190",
        "explanation": "<p><strong>190.</strong> 30 + 45 + 25 + 50 + 40.</p>",
    },
    {
        "text": "<p>Using that chart, how many more books were borrowed on Tuesday "
                "than on Monday?</p>",
        "choices": ["15", "45", "75", "30"],
        "correct": "15",
        "explanation": "<p><strong>15.</strong> 45 − 30.</p>"
                       "<p><strong>45</strong> — seshanbaning qiymati. «How many "
                       "more» farqni soʻraydi.</p>",
    },
    {
        "text": "<p>Using that chart, what fraction of the week's books were borrowed "
                "on Wednesday?</p>",
        "choices": ["25 out of 190", "25 out of 100", "25 out of 50",
                    "190 out of 25"],
        "correct": "25 out of 190",
        "explanation": "<p><strong>190 dan 25 tasi.</strong> Maxrajda haftaning "
                       "jami soni turadi.</p>",
    },
    {
        "text": "<p>A two-way table shows Grade 9: 24 walk, 16 bus; Grade 10: 18 walk, "
                "22 bus. How many students are there in total?</p>",
        "choices": ["80", "42", "40", "60"],
        "correct": "80",
        "explanation": "<p><strong>80.</strong> 24 + 16 + 18 + 22.</p>"
                       "<p>Chekka yigʻindilarni darrov yozib qoʻying.</p>",
    },
    {
        "text": "<p>Using that table, how many students walk?</p>",
        "choices": ["42", "40", "24", "38"],
        "correct": "42",
        "explanation": "<p><strong>42.</strong> 24 + 18 — ikkala sinfdan.</p>"
                       "<p><strong>24</strong> — faqat 9-sinf.</p>",
    },
    {
        "text": "<p>Using that table, what percent of Grade 9 students take the "
                "bus?</p>",
        "choices": ["40%", "42%", "20%", "60%"],
        "correct": "40%",
        "explanation": "<p><strong>40%.</strong> 16 ÷ 40 — maxrajda 9-sinf "
                       "jami.</p>"
                       "<p><strong>42%</strong> — 16 ÷ 38, yaʼni avtobusdagilar "
                       "ichida.</p>",
    },
    {
        "text": "<p>Using that table, what percent of bus riders are in Grade 10?</p>",
        "choices": ["About 58%", "55%", "About 42%", "27.5%"],
        "correct": "About 58%",
        "explanation": "<p><strong>Taxminan 58%.</strong> 22 ÷ 38 ≈ 0.579.</p>"
                       "<p><strong>55%</strong> — 22 ÷ 40, yaʼni 10-sinf jami "
                       "maxrajga olingan.</p>",
    },
    {
        "text": "<p>Using that table, what percent of all students are Grade 9 students "
                "who walk?</p>",
        "choices": ["30%", "60%", "57%", "24%"],
        "correct": "30%",
        "explanation": "<p><strong>30%.</strong> 24 ÷ 80.</p>"
                       "<p>«Of all students» — maxraj butun jadval jami.</p>",
    },
    {
        "text": "<p>A line graph of a company's sales rises from 2020 to 2022, falls in "
                "2023, then rises again in 2024. In which year were sales "
                "lowest?</p>",
        "choices": ["2020", "2023", "2024", "It cannot be determined"],
        "correct": "It cannot be determined",
        "explanation": "<p><strong>Aniqlab boʻlmaydi.</strong> 2023 da tushgan, "
                       "lekin u 2020 dagi qiymatdan past ekani aytilmagan.</p>"
                       "<p>Kamayish va eng kichik qiymat — ikki boshqa narsa.</p>",
    },
    {
        "text": "<p>A graph's vertical axis is labelled 'Sales (thousands)'. A bar "
                "reaches 45. What does this represent?</p>",
        "choices": ["45,000 sales", "45 sales", "4,500 sales", "450 sales"],
        "correct": "45,000 sales",
        "explanation": "<p><strong>45,000.</strong> «Thousands» yozuvi shkalani "
                       "belgilaydi.</p>"
                       "<p>Oʻq nomini oʻqimaslik Blok C dagi eng arzon "
                       "yoʻqotish.</p>",
    },
    {
        "text": "<p>A bar chart's vertical axis starts at 90, not 0. Two bars reach 95 "
                "and 100. What is true?</p>",
        "choices": ["The second value is about 5% larger, though the bar looks twice as tall",
                    "The second value is twice the first",
                    "The chart is wrong",
                    "The difference cannot be found"],
        "correct": "The second value is about 5% larger, though the bar looks twice as tall",
        "explanation": "<p><strong>Taxminan 5 foiz katta.</strong> 95 va 100 — "
                       "farqi 5.</p>"
                       "<p>Noldan boshlanmagan shkala farqni koʻzga kattaroq "
                       "koʻrsatadi. Sonni oʻqing, balandlikni emas.</p>",
    },
    {
        "text": "<p>In a two-way table, the row totals are 40 and 40, and one column "
                "total is 42. What is the other column total?</p>",
        "choices": ["38", "42", "40", "80"],
        "correct": "38",
        "explanation": "<p><strong>38.</strong> Jami 80, va 80 − 42.</p>"
                       "<p>Chekka yigʻindilar ikki tomondan ham bir xil jamiga "
                       "olib kelishi kerak.</p>",
    },
    {
        "text": "<p>A line graph shows a company's profit rising each year but by "
                "smaller amounts. What is happening?</p>",
        "choices": ["Profit is still rising, but more slowly each year",
                    "Profit is falling",
                    "Profit is constant",
                    "Profit became negative"],
        "correct": "Profit is still rising, but more slowly each year",
        "explanation": "<p><strong>Hali ham oʻsmoqda, lekin sekinroq.</strong> "
                       "Chiziq koʻtarilyapti, faqat tikligi kamaymoqda.</p>"
                       "<p>Oʻsishning sekinlashishi kamayish degani emas.</p>",
    },
    {
        "text": "<p>A student answers 'how many more books on Thursday than Wednesday' "
                "with 50. What is the correct answer?</p>",
        "choices": ["25", "50", "75", "2"],
        "correct": "25",
        "explanation": "<p><strong>25.</strong> 50 − 25.</p>"
                       "<p>Oʻquvchi grafikdan bitta sonni koʻchirgan; savol "
                       "farqni soʻragan.</p>",
    },
    {
        "text": "<p>A student answers 'what percent of those who walk are in Grade 9' "
                "with 60%. What is the correct answer?</p>",
        "choices": ["About 57%", "60%", "30%", "About 53%"],
        "correct": "About 57%",
        "explanation": "<p><strong>Taxminan 57%.</strong> 24 ÷ 42.</p>"
                       "<p>Oʻquvchi maxrajga 40 (9-sinf jami) qoʻygan; «of those "
                       "who walk» 42 ni talab qiladi.</p>",
    },
    {
        "text": "<p>Using the bar chart, if each borrowed book earns the library 500 "
                "som in fees, how much did Thursday earn?</p>",
        "choices": ["25,000 som", "50,000 som", "12,500 som", "95,000 som"],
        "correct": "25,000 som",
        "explanation": "<p><strong>25,000.</strong> 50 × 500.</p>"
                       "<p>Ikki bosqichli savol: avval jadvaldan son, keyin "
                       "koʻpaytirish.</p>",
    },
    {
        "text": "<p>Using the two-way table, if each bus holds 30 students, how many "
                "buses are needed for all bus riders?</p>",
        "choices": ["2", "1", "38", "1.27"],
        "correct": "2",
        "explanation": "<p><strong>2 ta.</strong> 38 oʻquvchi, va 38 ÷ 30 ≈ 1.27 — "
                       "yuqoriga yaxlitlanadi.</p>"
                       "<p><strong>1.27</strong> — avtobus butun sonda "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>A table shows monthly rainfall in millimetres: 40, 55, 30, 75, 50. "
                "What is the total rainfall in centimetres?</p>",
        "choices": ["25 cm", "250 cm", "2.5 cm", "2,500 cm"],
        "correct": "25 cm",
        "explanation": "<p><strong>25 sm.</strong> Jami 250 mm, va "
                       "250 ÷ 10 = 25.</p>"
                       "<p>Jadval bir birlikda, savol boshqasida — SAT-50 shu "
                       "yerda qaytadi.</p>",
    },
    {
        "text": "<p>A chart shows a school's income by source: fees 60%, grants 25%, "
                "donations 15%. If total income is 400 million som, how much more "
                "comes from fees than from grants?</p>",
        "choices": ["140 million som", "240 million som", "100 million som",
                    "35 million som"],
        "correct": "140 million som",
        "explanation": "<p><strong>140 million.</strong> Fees 240, grants 100, "
                       "farqi 140.</p>"
                       "<p>Yoki 35 foiz farqi × 400 = 140 — bir xil javob.</p>",
    },
]


# =====================================================================
# SAT-54 — scatterplots
# =====================================================================

Q_SAT54 = [
    {
        "text": "<p>As the number of hours studied increases, test scores also "
                "increase. What type of association is this?</p>",
        "choices": ["Positive", "Negative", "No association", "Causal"],
        "correct": "Positive",
        "explanation": "<p><strong>Musbat.</strong> Ikkalasi birga oshadi.</p>"
                       "<p><strong>Causal</strong> — sochilma diagramma sababni "
                       "koʻrsata olmaydi.</p>",
    },
    {
        "text": "<p>As a car's age increases, its value decreases. What type of "
                "association is this?</p>",
        "choices": ["Negative", "Positive", "No association", "Proportional"],
        "correct": "Negative",
        "explanation": "<p><strong>Manfiy.</strong> Biri oshsa, ikkinchisi "
                       "kamayadi.</p>",
    },
    {
        "text": "<p>A line of best fit is <i>cost</i> = 4(<i>items</i>) + 25. What does "
                "the 4 represent?</p>",
        "choices": ["The cost of each additional item",
                    "The fixed starting cost",
                    "The number of items", "The total cost"],
        "correct": "The cost of each additional item",
        "explanation": "<p><strong>Har bir qoʻshimcha buyumning narxi.</strong> "
                       "Qiyalik — bir birlik kirishga toʻgʻri keladigan "
                       "oʻzgarish.</p>"
                       "<p>25 esa boshlangʻich haq.</p>",
    },
    {
        "text": "<p>For that same line, what does the 25 represent?</p>",
        "choices": ["The cost when no items are bought",
                    "The cost of each item", "The number of items",
                    "The slope"],
        "correct": "The cost when no items are bought",
        "explanation": "<p><strong>Hech narsa olinmaganda ham toʻlanadigan "
                       "haq.</strong> Kesishish — kirish nolga teng "
                       "boʻlgandagi qiymat.</p>",
    },
    {
        "text": "<p>Using <i>score</i> = 5(<i>hours</i>) + 30, what is the predicted "
                "score for 8 hours?</p>",
        "choices": ["70", "40", "35", "240"],
        "correct": "70",
        "explanation": "<p><strong>70.</strong> 5(8) + 30.</p>",
    },
    {
        "text": "<p>A student studied 8 hours and scored 76. Using that line, what is "
                "the residual?</p>",
        "choices": ["6", "−6", "70", "76"],
        "correct": "6",
        "explanation": "<p><strong>6.</strong> Qoldiq = haqiqiy − bashorat = "
                       "76 − 70.</p>"
                       "<p><strong>−6</strong> — ayirish teskari qilingan.</p>",
    },
    {
        "text": "<p>A student studied 4 hours and scored 45. Using <i>score</i> = "
                "5(<i>hours</i>) + 30, what is the residual?</p>",
        "choices": ["−5", "5", "50", "45"],
        "correct": "−5",
        "explanation": "<p><strong>−5.</strong> Bashorat 50, haqiqiy 45.</p>"
                       "<p>Manfiy qoldiq — nuqta chiziqdan pastda.</p>",
    },
    {
        "text": "<p>A point lies above the line of best fit. What does this mean?</p>",
        "choices": ["The actual value is higher than the predicted value",
                    "The actual value is lower than predicted",
                    "The point is an error",
                    "The line is wrong"],
        "correct": "The actual value is higher than the predicted value",
        "explanation": "<p><strong>Haqiqiy qiymat bashoratdan yuqori.</strong> "
                       "Qoldiq musbat.</p>",
    },
    {
        "text": "<p>Ice cream sales and cases of sunburn both rise in summer. What "
                "conclusion is supported?</p>",
        "choices": ["The two are associated, but neither causes the other",
                    "Ice cream causes sunburn",
                    "Sunburn causes people to buy ice cream",
                    "There is no association"],
        "correct": "The two are associated, but neither causes the other",
        "explanation": "<p><strong>Bogʻliq, lekin sabab emas.</strong> "
                       "Ikkalasining sababi — issiq havo.</p>"
                       "<p>Bu SAT'ning eng sevimli interpretatsiya "
                       "savoli.</p>",
    },
    {
        "text": "<p>Which phrase in an answer choice is most likely to make it "
                "wrong?</p>",
        "choices": ["'causes'", "'is associated with'", "'tends to'",
                    "'on average'"],
        "correct": "'causes'",
        "explanation": "<p><strong>«Causes».</strong> Kuzatilgan maʼlumot sababni "
                       "isbotlamaydi.</p>"
                       "<p>Qolgan uchtasi ehtiyotkor iboralar — ular odatda "
                       "toʻgʻri javobda turadi.</p>",
    },
    {
        "text": "<p>A scatterplot's points lie very close to the line of best fit. "
                "What does this mean?</p>",
        "choices": ["The association is strong, so predictions are more reliable",
                    "One variable causes the other",
                    "The slope must be large",
                    "There are no outliers"],
        "correct": "The association is strong, so predictions are more reliable",
        "explanation": "<p><strong>Bogʻliqlik kuchli.</strong> Zichlik "
                       "bashoratning ishonchliligini oshiradi.</p>"
                       "<p>Qiyalikning kattaligi bogʻliqlik kuchi haqida hech "
                       "narsa aytmaydi.</p>",
    },
    {
        "text": "<p>A study's data covers 1 to 12 hours of study. Using the line to "
                "predict a score for 40 hours is</p>",
        "choices": ["unreliable, because it is far outside the data",
                    "reliable, because the line is a formula",
                    "impossible to compute",
                    "guaranteed to be too low"],
        "correct": "unreliable, because it is far outside the data",
        "explanation": "<p><strong>Ishonchsiz.</strong> Chiziq faqat maʼlumot "
                       "toʻplangan oraliqda tekshirilgan.</p>"
                       "<p>Hisoblash mumkin — ishonch esa yoʻq.</p>",
    },
    {
        "text": "<p>A line of best fit for a car's value is <i>value</i> = "
                "−1,500(<i>years</i>) + 20,000. What does −1,500 mean?</p>",
        "choices": ["The value falls by 1,500 each year",
                    "The car is worth −1,500", "The car lasts 1,500 years",
                    "The starting value"],
        "correct": "The value falls by 1,500 each year",
        "explanation": "<p><strong>Har yili 1,500 ga tushadi.</strong> Manfiy "
                       "qiyalik — kamayish.</p>"
                       "<p>20,000 esa yangi mashinaning qiymati.</p>",
    },
    {
        "text": "<p>Using that car model, what is the predicted value after 6 "
                "years?</p>",
        "choices": ["11,000", "9,000", "12,500", "20,000"],
        "correct": "11,000",
        "explanation": "<p><strong>11,000.</strong> 20,000 − 9,000.</p>"
                       "<p><strong>9,000</strong> — faqat yoʻqotilgan qiymat.</p>",
    },
    {
        "text": "<p>A student says a residual of −8 means the prediction was 8 too "
                "low. What is correct?</p>",
        "choices": ["The prediction was 8 too high",
                    "The prediction was 8 too low",
                    "The prediction was exact",
                    "The residual cannot be negative"],
        "correct": "The prediction was 8 too high",
        "explanation": "<p><strong>Bashorat 8 ga baland edi.</strong> Qoldiq "
                       "manfiy — haqiqiy qiymat bashoratdan past.</p>",
    },
    {
        "text": "<p>A student concludes from a scatterplot that owning more books "
                "causes higher exam scores. What is wrong?</p>",
        "choices": ["Association does not establish causation",
                    "The scatterplot must be negative",
                    "Books cannot be counted",
                    "The sample was too large"],
        "correct": "Association does not establish causation",
        "explanation": "<p><strong>Bogʻliqlik sababni isbotlamaydi.</strong> "
                       "Uchinchi omil (masalan, oila sharoiti) ikkalasiga ham "
                       "taʼsir qilishi mumkin.</p>",
    },
    {
        "text": "<p>Two scatterplots have the same slope, but one has points much more "
                "tightly clustered. What differs?</p>",
        "choices": ["The strength of the association",
                    "The direction of the association",
                    "The units", "The intercept"],
        "correct": "The strength of the association",
        "explanation": "<p><strong>Bogʻliqlikning kuchi.</strong> Qiyalik "
                       "yoʻnalish va tezlikni beradi, zichlik esa kuchni.</p>",
    },
    {
        "text": "<p>A line of best fit is <i>y</i> = 2<i>x</i> + 7. Two data points are "
                "(5, 20) and (8, 21). Which has the larger residual in size?</p>",
        "choices": ["(5, 20), with a residual of 3",
                    "(8, 21), with a residual of −2",
                    "They are equal",
                    "Neither has a residual"],
        "correct": "(5, 20), with a residual of 3",
        "explanation": "<p><strong>(5, 20).</strong> Bashorat 17, qoldiq +3; "
                       "(8, 21) uchun bashorat 23, qoldiq −2.</p>"
                       "<p>Kattalik boʻyicha 3 > 2.</p>",
    },
    {
        "text": "<p>A shop finds that as advertising spending rises, sales rise. The "
                "line of best fit has slope 4. What does this predict?</p>",
        "choices": ["Each extra unit spent on advertising is associated with 4 more sales",
                    "Advertising causes exactly 4 sales",
                    "Sales are 4 times advertising",
                    "The shop should spend nothing"],
        "correct": "Each extra unit spent on advertising is associated with 4 more sales",
        "explanation": "<p><strong>Har qoʻshimcha birlik xarajat 4 ta koʻproq "
                       "sotuv bilan bogʻliq.</strong></p>"
                       "<p>«Causes exactly» — sabab ham, aniqlik ham "
                       "asoslanmagan.</p>",
    },
    {
        "text": "<p>A researcher measures plant height against water given, and the "
                "points show no pattern at all. What should be concluded?</p>",
        "choices": ["There is no association in this data",
                    "Water has no effect on any plant",
                    "The measurements are wrong",
                    "The association is negative"],
        "correct": "There is no association in this data",
        "explanation": "<p><strong>Bu maʼlumotda bogʻliqlik yoʻq.</strong> Bu "
                       "xulosa faqat shu tajribaga tegishli.</p>"
                       "<p>«Hech qanday oʻsimlikka taʼsir qilmaydi» — juda "
                       "keng, asossiz xulosa.</p>",
    },
]


# =====================================================================
# SAT-55 — mean and median
# =====================================================================

Q_SAT55 = [
    {
        "text": "<p>What is the mean of 5, 8, 11, 12?</p>",
        "choices": ["9", "9.5", "36", "8"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> 36 ÷ 4.</p>",
    },
    {
        "text": "<p>What is the median of 5, 8, 11, 12?</p>",
        "choices": ["9.5", "9", "8", "11"],
        "correct": "9.5",
        "explanation": "<p><strong>9.5.</strong> Sonlar juft, demak oʻrtadagi "
                       "ikkitasining oʻrtasi: (8 + 11) ÷ 2.</p>"
                       "<p>Mediana roʻyxatda boʻlmasligi mumkin.</p>",
    },
    {
        "text": "<p>What is the median of 14, 3, 9, 21, 7?</p>",
        "choices": ["9", "10.8", "7", "14"],
        "correct": "9",
        "explanation": "<p><strong>9.</strong> Tartiblang: 3, 7, 9, 14, 21.</p>"
                       "<p><strong>10.8</strong> — oʻrta arifmetik.</p>",
    },
    {
        "text": "<p>The mean of 8 numbers is 15. What is their sum?</p>",
        "choices": ["120", "23", "15", "8"],
        "correct": "120",
        "explanation": "<p><strong>120.</strong> Oʻrtacha × soni = yigʻindi.</p>",
    },
    {
        "text": "<p>Five numbers have a mean of 14. Four of them are 10, 12, 16 and 18. "
                "What is the fifth?</p>",
        "choices": ["14", "12", "16", "70"],
        "correct": "14",
        "explanation": "<p><strong>14.</strong> Yigʻindi 70, maʼlumlari 56.</p>"
                       "<p>Beshinchi son oʻrtachaga teng chiqdi — bu tasodif "
                       "emas, chunki qolganlari muvozanatda.</p>",
    },
    {
        "text": "<p>Which changes more when 500 is added to the set 1, 2, 3, 4, 5?</p>",
        "choices": ["The mean", "The median", "They change equally",
                    "Neither changes"],
        "correct": "The mean",
        "explanation": "<p><strong>Oʻrta arifmetik.</strong> 3 dan 85.83 ga; "
                       "mediana esa 3 dan 3.5 ga.</p>"
                       "<p>Chetdagi qiymat oʻrta arifmetikni tortadi.</p>",
    },
    {
        "text": "<p>Nine houses on a street are worth between 300 and 400 million som. "
                "One is worth 5 billion. Which better represents a typical house?</p>",
        "choices": ["The median", "The mean", "Both equally", "Neither"],
        "correct": "The median",
        "explanation": "<p><strong>Mediana.</strong> Bitta juda katta qiymat oʻrta "
                       "arifmetikni koʻtarib yuboradi.</p>"
                       "<p>Shuning uchun uy narxlari haqidagi hisobotlarda "
                       "mediana ishlatiladi.</p>",
    },
    {
        "text": "<p>A data set is 6, 6, 6, 6, 6. What are the mean and median?</p>",
        "choices": ["Both 6", "Mean 6, median 5", "Mean 30, median 6",
                    "Both 30"],
        "correct": "Both 6",
        "explanation": "<p><strong>Ikkalasi ham 6.</strong> Barcha qiymatlar "
                       "teng.</p>",
    },
    {
        "text": "<p>Adding a value equal to the current mean to a data set will</p>",
        "choices": ["leave the mean unchanged", "raise the mean",
                    "lower the mean", "always change the median a lot"],
        "correct": "leave the mean unchanged",
        "explanation": "<p><strong>Oʻrtacha oʻzgarmaydi.</strong> Yigʻindi ham, "
                       "soni ham mos ravishda oshadi.</p>"
                       "<p>Oʻrtachadan katta qiymat uni koʻtaradi, kichigi "
                       "tushiradi.</p>",
    },
    {
        "text": "<p>A frequency table shows: value 1 appears 3 times, value 2 appears 5 "
                "times, value 3 appears 2 times. What is the mean?</p>",
        "choices": ["1.9", "2", "3.33", "10"],
        "correct": "1.9",
        "explanation": "<p><strong>1.9.</strong> Yigʻindi 3 + 10 + 6 = 19, soni "
                       "10.</p>"
                       "<p>Har bir qiymatni chastotasiga koʻpaytiring.</p>",
    },
    {
        "text": "<p>For that same frequency table, what is the median?</p>",
        "choices": ["2", "1.9", "1.5", "3"],
        "correct": "2",
        "explanation": "<p><strong>2.</strong> Oʻn qiymat: 1,1,1,2,2,2,2,2,3,3 — "
                       "5 va 6-oʻrindagilar ikkalasi ham 2.</p>",
    },
    {
        "text": "<p>A class's test scores are mostly between 70 and 80, but three "
                "students scored 20. What is true?</p>",
        "choices": ["The mean is pulled below the median",
                    "The mean is pulled above the median",
                    "The mean and median are equal",
                    "The median is pulled below the mean"],
        "correct": "The mean is pulled below the median",
        "explanation": "<p><strong>Oʻrta arifmetik pastga tortiladi.</strong> "
                       "Past chetdagi qiymatlar uni kamaytiradi.</p>"
                       "<p>Mediana esa oʻz oʻrnida qoladi.</p>",
    },
    {
        "text": "<p>A shop's daily sales for a week are 20, 22, 25, 21, 23, 24, 105. "
                "Which measure better describes a typical day?</p>",
        "choices": ["The median, 23", "The mean, about 34", "The mean, 105",
                    "Neither"],
        "correct": "The median, 23",
        "explanation": "<p><strong>Mediana, 23.</strong> 105 — chetdagi qiymat "
                       "(ehtimol bayram kuni).</p>"
                       "<p>Oʻrtacha taxminan 34 — hech bir odatiy kunga "
                       "oʻxshamaydi.</p>",
    },
    {
        "text": "<p>Six numbers have a mean of 9. If one number, 4, is removed, what is "
                "the mean of the remaining five?</p>",
        "choices": ["10", "9", "8", "11"],
        "correct": "10",
        "explanation": "<p><strong>10.</strong> Yigʻindi 54, olib tashlangach 50, "
                       "va 50 ÷ 5.</p>"
                       "<p>Oʻrtachadan kichik son olib tashlansa, oʻrtacha "
                       "oshadi.</p>",
    },
    {
        "text": "<p>A student finds the median of 9, 3, 7, 15, 5 by taking the middle "
                "number as written, and answers 7. Why is the method wrong even "
                "though the answer is right?</p>",
        "choices": ["The list must be sorted first; here it happened to agree",
                    "The answer is actually 9",
                    "The median needs the mean first",
                    "There is no median for five numbers"],
        "correct": "The list must be sorted first; here it happened to agree",
        "explanation": "<p><strong>Avval tartiblash kerak.</strong> Bu safar "
                       "tasodifan mos keldi.</p>"
                       "<p>Boshqa qatorda bu usul xato javob beradi.</p>",
    },
    {
        "text": "<p>A student says the mean of 8 numbers with sum 96 is 96 ÷ 8 = 12, "
                "then says the median must also be 12. What is wrong?</p>",
        "choices": ["The median cannot be found from the sum alone",
                    "The mean is wrong",
                    "The median is always larger",
                    "Nothing is wrong"],
        "correct": "The median cannot be found from the sum alone",
        "explanation": "<p><strong>Medianani yigʻindidan topib boʻlmaydi.</strong> "
                       "U qiymatlarning tartibiga bogʻliq.</p>"
                       "<p>Oʻrta arifmetik esa toʻgʻri hisoblangan.</p>",
    },
    {
        "text": "<p>The mean of 4 numbers is 25. A fifth number is added and the new "
                "mean is 28. What is the fifth number?</p>",
        "choices": ["40", "28", "3", "140"],
        "correct": "40",
        "explanation": "<p><strong>40.</strong> Eski yigʻindi 100, yangi yigʻindi "
                       "140, farqi 40.</p>"
                       "<p>Yigʻindilar orqali ishlash bu turdagi savolni "
                       "ochadi.</p>",
    },
    {
        "text": "<p>Seven numbers are arranged in order. Which position is the "
                "median?</p>",
        "choices": ["The fourth", "The third", "The middle two averaged",
                    "The seventh"],
        "correct": "The fourth",
        "explanation": "<p><strong>Toʻrtinchi.</strong> Uchtasi undan past, "
                       "uchtasi baland.</p>"
                       "<p>Toq sonda mediana roʻyxatdagi haqiqiy qiymat "
                       "boʻladi.</p>",
    },
    {
        "text": "<p>A cricket team's scores are 12, 15, 18, 20, 95. The captain reports "
                "the mean as the team's typical score. Why is this misleading?</p>",
        "choices": ["The 95 pulls the mean to 32, above four of the five scores",
                    "The mean is too small",
                    "The median cannot be computed",
                    "Five scores are not enough"],
        "correct": "The 95 pulls the mean to 32, above four of the five scores",
        "explanation": "<p><strong>Oʻrtacha 32.</strong> Beshta natijaning "
                       "toʻrttasi undan past.</p>"
                       "<p>Mediana 18 — bu jamoani ancha haqqoniy "
                       "ifodalaydi.</p>",
    },
    {
        "text": "<p>A factory reports a mean wage of 8 million som. Ten workers earn "
                "4 million and the manager earns 48 million. How many workers are "
                "there in total, including the manager?</p>",
        "choices": ["11", "10", "12", "6"],
        "correct": "11",
        "explanation": "<p><strong>11.</strong> Yigʻindi 40 + 48 = 88, va "
                       "88 ÷ 8 = 11.</p>"
                       "<p>Bu oʻrtachaning qanday chalgʻitishini koʻrsatadi: "
                       "hech kim 8 million olmaydi.</p>",
    },
]


# =====================================================================
# Testlar
# =====================================================================

PRACTICES = [
    {
        "title":       "SAT-51 Practice: Percentages — Part, Whole, and Base",
        "description": "20 ta SAT uslubidagi savol — foizning uch shakli, «of» "
                       "koʻpaytirish ekani va bazani aniqlash.",
        "tutorial":    "SAT-51:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT51,
    },
    {
        "title":       "SAT-52 Practice: Percent Change — Increase, Decrease, and Successive Changes",
        "description": "20 ta SAT uslubidagi savol — maxrajda eski qiymat, ketma-ket "
                       "oʻzgarishlar koʻpaytmasi va dastlabki narxni topish.",
        "tutorial":    "SAT-52:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT52,
    },
    {
        "title":       "SAT-53 Practice: Interpreting Tables, Graphs, and Bar Charts",
        "description": "20 ta SAT uslubidagi savol — ustunli diagramma, ikki tomonlama "
                       "jadval, shkala tuzogʻi va maxrajni tanlash.",
        "tutorial":    "SAT-53:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT53,
    },
    {
        "title":       "SAT-54 Practice: Scatterplots — Lines of Best Fit and Trends",
        "description": "20 ta SAT uslubidagi savol — qiyalik va kesishishning maʼnosi, "
                       "qoldiq va sabab-bogʻliqlik farqi.",
        "tutorial":    "SAT-54:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT54,
    },
    {
        "title":       "SAT-55 Practice: Descriptive Statistics — Mean and Median",
        "description": "20 ta SAT uslubidagi savol — tartiblash, chetdagi qiymat, "
                       "yigʻindi orqali teskari savollar va chastota jadvali.",
        "tutorial":    "SAT-55:",
        "subject":     "Math",
        "level":       "easy",
        "questions":   Q_SAT55,
    },
]
