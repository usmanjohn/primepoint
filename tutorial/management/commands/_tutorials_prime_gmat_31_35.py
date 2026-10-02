# -*- coding: utf-8 -*-
"""Prime GMAT — Data Insights, part two: GMAT-31 … GMAT-35.
Table Analysis, Graphics Interpretation, Two-Part Analysis, Multi-Source Reasoning, and the
section's strategy lesson.

Written with STYLE_GUIDE_PRIME_GMAT.md §7 · lesson list in toc_prime_gmat.txt.
Facts (mba.com / gmac.com, checked 2026-10-02): 20 questions / 45 minutes, on-screen
calculator, multi-part questions score only when every part is right.

Tables and charts come from _dikit.py (same folder) — never hand-typed; the batch gate
re-measures every bar and dot back to the data.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_31_35.py --author=prime
"""
import importlib.util
import os

_spec = importlib.util.spec_from_file_location(
    '_dikit', os.path.join(os.path.dirname(os.path.abspath(__file__)), '_dikit.py'))
kit = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(kit)

PLAYLIST = {
    "title": "Prime GMAT",
    "category": "math",
    "description": (
        "GMAT Focus Edition'ning Quant boʻlimi — biznes maktabiga yoʻl. Savollar ingliz "
        "tilida, chunki imtihon shunday; tushuntirish oʻzbek tilida. Har bir darsda "
        "haqiqiy GMAT uslubidagi savollar, tuzoq javoblar va 20 savollik mashq."
    ),
}

DS = [
    "Statement (1) ALONE is sufficient, but statement (2) alone is not sufficient.",
    "Statement (2) ALONE is sufficient, but statement (1) alone is not sufficient.",
    "BOTH statements TOGETHER are sufficient, but NEITHER statement ALONE is sufficient.",
    "EACH statement ALONE is sufficient.",
    "Statements (1) and (2) TOGETHER are NOT sufficient.",
]
LET = "ABCDE"


def stem(kind, time, body, choices, key, solution):
    i = LET.index(key)
    items = "\n".join(f"    <li>{c}</li>" for c in choices)
    return f"""<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question · {kind} <span class="ps-time">{time}</span></p>
  <div class="ps-stem__q">
    {body}
  </div>
  <ol class="ps-ch">
{items}
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: {key}) {choices[i]}</p>
      {solution}
    </div>
  </details>
</div>"""


def trap(value, why):
    return f"""<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">{value}</span>
  <span class="ps-trap__why">{why}</span>
</div>"""


def quiz(n, question, answer):
    return f"""<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">{n}</span> {question}</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">{answer}</p></details>
</div>"""


# ── data used in the lessons (different from the practices on purpose) ──
TL_H = ["Store", "Staff", "Sales ($k)", "Rating"]
TL = [["Chilonzor", 12, 360, "4.5"], ["Yunusobod", 15, 420, "4.1"], ["Sergeli", 8, 200, "4.8"],
      ["Mirzo Ulugʻbek", 10, 330, "4.3"], ["Olmazor", 9, 270, "4.6"]]
tl = kit.table(TL_H, TL)
GL1L, GL1 = ["Q1", "Q2", "Q3", "Q4"], [80, 100, 90, 130]
gl1 = kit.bar_chart(GL1L, GL1, 150, 50, "A company's revenue in each quarter, in thousands of dollars.", "Quarterly revenue bar chart", "Revenue ($ thousands)")
GL2L, GL2 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], [20, 24, 30, 27, 33, 36]
gl2 = kit.line_chart(GL2L, GL2, 40, 10, "Monthly visitors to a museum, in thousands.", "Monthly visitors line chart", "Visitors (thousands)")
GL3L, GL3 = ["Q1", "Q2", "Q3", "Q4"], [60, 75, 70, 90]
gl3 = kit.bar_chart(GL3L, GL3, 100, 25, "A firm's profit in each quarter, in thousands of dollars.", "Quarterly profit bar chart", "Profit ($ thousands)")
EV = kit.table(["Event", "Days", "People"], [["Training", 2, 25], ["Launch", 1, 60], ["Workshop", 3, 18]])

# ═════════════════════════════════════════════════════════════════════════
GMAT31 = f"""
<h2>GMAT-31: Table Analysis</h2>

<p>Table Analysis savolida ekranda elektron jadvalga oʻxshash jadval beriladi va uning ostida
<mark>uchta bayonot</mark> turadi. Har biri uchun «ha» yoki «yoʻq» (yoki «toʻgʻri / notoʻgʻri»)
tanlaysiz va ball faqat <b>uchalasi ham toʻgʻri</b> boʻlsagina beriladi. Jadvalni ustun boʻyicha
saralash mumkin — bu imtihondagi eng foydali tugma.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>jadval ustunlari va birliklarini bir qarashda oʻqiysiz;</li>
    <li>«bir xodimga», «foiz», «mediana» kabi hisoblarni jadvaldan tez chiqarasiz;</li>
    <li>har bir bayonot uchun faqat kerakli ustunlarni tekshirasiz;</li>
    <li>uchta bayonotli savolni «I, II, III» koʻrinishida ham yecha olasiz.</li>
  </ul>
</div>

<h3>Avval jadvalni oʻqing</h3>

<p>Toshkentdagi besh doʻkon haqida jadval:</p>

{tl}

<p>Har bir ustunga qarang: <b>Staff</b> — xodimlar soni, <b>Sales ($k)</b> — sotuv <b>ming dollarda</b>,
<b>Rating</b> — mijozlar bahosi. «$k» belgisini koʻrmaslik — eng koʻp uchraydigan xato: 360 — bu
360,000 dollar.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bayonotni oʻqishdan oldin jadvalning <b>sarlavhalarini</b> oʻqing — birliklar, «ming», «foiz»
  shu yerda yoziladi. Keyin har bir bayonot uchun oʻzingizga savol bering: «buning uchun qaysi
  ustun kerak?» Koʻpincha bitta yoki ikkita ustun yetadi, qolganlari chalgʻitish uchun.
</div>

<h3>«Bir xodimga» — boʻlish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qaysi doʻkonda bir xodimga sotuv eng yuqori?</span>
    <span class="pm-solve__why">Sales ÷ Staff — har bir qator uchun</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Chilonzor 30, Yunusobod 28, Sergeli 25, Mirzo Ulugʻbek 33, Olmazor 30</span>
    <span class="pm-solve__why">Kalkulyator bor, lekin bu boʻlishlar ogʻzaki</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Mirzo Ulugʻbek — 33 ming dollar</span>
    <span class="pm-solve__why">Eng katta sotuv (Yunusobod) — eng yuqori samaradorlik emas</span>
  </div>
</div>

<h3>Mediana — saralang</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Baholar medianasi?</span>
    <span class="pm-solve__why">Ekranda Rating ustuni boʻyicha saralang</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">4.1, 4.3, 4.5, 4.6, 4.8</span>
    <span class="pm-solve__why">Besh qiymat — oʻrtadagisi uchinchi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">4.5</span>
    <span class="pm-solve__why">Juft sonli boʻlsa — ikki oʻrta qiymatning oʻrtachasi</span>
  </div>
</div>

<h3>Ulush — jamini toping</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Eng yuqori bahoga ega ikki doʻkon sotuvning necha foizini beradi?</span>
    <span class="pm-solve__why">Sergeli 4.8 va Olmazor 4.6</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">200 + 270 = 470; jami 1,580</span>
    <span class="pm-solve__why">Avval butun ustunning jamini</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">470 ÷ 1,580 ≈ 30%</span>
    <span class="pm-solve__why">Bu yerda kalkulyator vaqt tejaydi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Haqiqiy imtihonda jadvalning yuqorisida <b>«Sort by»</b> tugmasi bor. Mediana, eng katta/kichik,
  «nechta … dan yuqori» savollarida birinchi ish — tegishli ustun boʻyicha saralash. Bu yerda
  sahifa saralamaydi, shuning uchun qogʻozda tez tartiblab yozishni mashq qiling.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ball faqat uchala bayonot ham toʻgʻri baholansa beriladi — qisman ball yoʻq. Shuning uchun bitta
  bayonotda ikkilansangiz ham, qolgan ikkitasini aniq qilib olish muhim: ikkilangan bayonotga eng
  ehtimoliy javobni belgilang va vaqtni boshqa savolga saqlang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bayonotlardagi soʻzlar qatʼiy: «more than half» — aynan yarmi emas; «exactly» — taxmin emas;
  «at least» — tenglik ham kiradi. Jadvaldagi son chegaraga aynan teng chiqsa, shu soʻzlar
  javobni hal qiladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>per staff member</b><span>bir xodimga — boʻlish</span></li>
  <li><b>the median of the column</b><span>ustun medianasi — saralang</span></li>
  <li><b>more than half</b><span>yarmidan koʻp — qatʼiy</span></li>
  <li><b>Yes / No for each statement</b><span>har bir bayonotga ha yoki yoʻq</span></li>
  <li><b>($k)</b><span>ming dollar</span></li>
</ul>

<h3>GMAT savollari</h3>

{stem("Table Analysis", "90 s", "<p>Based on the table of the five stores above, which of the following statements are true?</p>" + kit.statements(
    ["Mirzo Ulugʻbek had the highest sales per staff member.",
     "The median rating of the five stores is 4.5.",
     "The store with the most staff also had the highest rating."]),
    ["I only", "I and II only", "I and III only", "II and III only", "I, II and III"], "B",
    "<p>I — 33 ming, eng yuqori. II — 4.1, 4.3, <b>4.5</b>, 4.6, 4.8. III — eng koʻp xodim Yunusobod, bahosi eng past (4.1).</p><p><b>I, II and III</b> — «katta doʻkon — eng yaxshi» degan taxmin.</p>")}

{trap("I, II and III", "Uchinchi bayonot jadvalga qaramasdan «mantiqiy» tuyuladi. Har bir bayonotni jadval bilan tekshiring.")}

{stem("Table Analysis", "60 s", "<p>Using the table above, what percent of the five stores' total sales came from the two stores with the highest ratings?</p>",
    ["25%", "27%", "30%", "33%", "47%"], "C",
    "<p>Sergeli va Olmazor: 470; jami 1,580; 470 ÷ 1,580 ≈ 29.7%.</p><p><b>47%</b> — 470 ni foiz deb oʻqigan javob.</p>")}

{trap("47%", "Ming dollardagi sonni foiz bilan adashtirmang: ulush uchun jamiga boʻlish kerak.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Table Analysis'da <b>uch qadam</b>:</p>
  <ol>
    <li>sarlavhalar va birliklar (ming, foiz) — 10 soniya;</li>
    <li>har bir bayonot uchun kerakli ustun(lar)ni aniqlang va kerak boʻlsa saralang;</li>
    <li>chegaraviy soʻzlarni («more than», «exactly», «at least») son bilan solishtiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Highest sales → highest sales per staff member</p>
  <p class="pe-good">Divide each row: sales ÷ staff</p>
  <p class="pe-fix__why">Jami va «bir birlikka» — har xil savol.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3 of 6 branches → «more than half»</p>
  <p class="pe-good">3 of 6 is exactly half → not more than half</p>
  <p class="pe-fix__why">Qatʼiy chegara — tenglik kirmaydi.</p>
</div>

<h3>Mashq</h3>

{quiz(1, "Using the store table, how many stores have a rating above 4.4?", "3 ta — 4.5, 4.8, 4.6.")}

{quiz(2, "How many staff do the five stores have in total?", "54 — 12 + 15 + 8 + 10 + 9.")}

{quiz(3, "What are the average sales per store, in thousands of dollars?", "316 — 1,580 ÷ 5.")}

{quiz(4, "What are Sergeli's sales per staff member, in thousands of dollars?", "25 — 200 ÷ 8.")}

{quiz(5, "By how many thousand dollars do Chilonzor's sales per staff member exceed Yunusobod's?", "2 — 30 − 28.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Table Analysis</b><span>jadval tahlili</span></li>
  <li><b>column</b><span>ustun</span></li>
  <li><b>row</b><span>qator</span></li>
  <li><b>sort</b><span>saralamoq</span></li>
  <li><b>per</b><span>… ga, har bir … uchun</span></li>
  <li><b>statement</b><span>bayonot</span></li>
  <li><b>rating</b><span>baho, reyting</span></li>
  <li><b>share of the total</b><span>jamidagi ulush</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Uchta bayonot — uchalasi toʻgʻri boʻlsagina ball.</li>
    <li>Avval sarlavhalar va birliklar.</li>
    <li>Har bir bayonot uchun faqat kerakli ustunlar; saralash — mediana va reyting uchun.</li>
    <li>«Bir xodimga» — boʻlish; ulush — jamiga boʻlish.</li>
    <li>«More than», «exactly», «at least» — chegarani hal qiladi.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT32 = f"""
<h2>GMAT-32: Graphics Interpretation</h2>

<p>Graphics Interpretation savolida grafik — ustunli, chiziqli, nuqtali yoki doiraviy — va uning
ostida <mark>ikkita jumla</mark> beriladi; har bir jumlada bitta boʻsh joy bor va uni ochiladigan
roʻyxatdan tanlaysiz. Savollar uch narsani soʻraydi: grafikdan qiymatni toʻgʻri oʻqish, ikki
qiymatni solishtirish (farq, foiz, nisbat) va tendensiyani koʻrish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>oʻqlar, birliklar va shkalani savolni oʻqishdan oldin tekshirasiz;</li>
    <li>foiz oʻzgarishi va nisbatni grafikdan toʻgʻri hisoblaysiz;</li>
    <li>eng katta oʻzgarishni eng baland ustundan farqlaysiz;</li>
    <li>oʻrtacha va medianani grafik qiymatlaridan topasiz.</li>
  </ul>
</div>

<h3>Avval oʻqlar va birlik</h3>

{gl1}

<p>Ustunlar ustidagi sonlar — <b>ming dollar</b> (chap yuqorida yozilgan). Q4 — 130, yaʼni
130,000 dollar. Shkala noldan boshlanadi; agar boshlanmasa, ustunlar balandligi farqni
boʻrttirib koʻrsatadi — shuning uchun doim <b>sonlarga</b> ishonchingiz koʻproq boʻlsin.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Grafik savolidagi eng arzon xato — birlikni oʻtkazib yuborish. «Thousands», «%», «millions» —
  oʻqning yonida kichik harflarda yoziladi. Javob variantlarida ham, odatda, toʻgʻri son notoʻgʻri
  birlik bilan tuzoq sifatida turadi.
</div>

<h3>Foiz oʻzgarishi — eski qiymatga</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Q4 Q1 dan necha foiz koʻp?</span>
    <span class="pm-solve__why">Oʻzgarish ÷ eski qiymat (GMAT-5)</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(130 − 80) ÷ 80 = 50 ÷ 80</span>
    <span class="pm-solve__why">Baza — Q1, chunki «than Q1»</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">62.5%</span>
    <span class="pm-solve__why">162.5% — Q4 Q1 ning necha foizi; bu boshqa savol</span>
  </div>
</div>

<h3>Chiziqli grafik — tendensiya va oʻzgarish</h3>

{gl2}

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Qaysi oylar orasida tashrif kamaydi?</span>
    <span class="pm-solve__why">Chiziq pastga tushgan joy</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Mart → aprel: 30 dan 27 ga</span>
    <span class="pm-solve__why">Qolgan barcha oʻzgarishlar — oʻsish</span>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Oylik tashriflar medianasi?</span>
    <span class="pm-solve__why">Qiymatlarni tartiblang: 20, 24, 27, 30, 33, 36</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(27 + 30) ÷ 2 = 28.5 → 28,500</span>
    <span class="pm-solve__why">Oʻrtacha esa 170 ÷ 6 ≈ 28,333 — boshqa son</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  «Eng katta oʻzgarish» savolida ustunlarning balandligiga emas, <b>qoʻshni ustunlar orasidagi
  farqqa</b> qarang. Eng baland ustun koʻpincha kichik oʻzgarishdan keyin keladi.
</div>

<h3>Shkala noldan boshlanmasa</h3>

<p>Biznes taqdimotlarida koʻp uchraydigan hiyla: ustunli diagrammaning oʻqi noldan emas, masalan
100 dan boshlanadi. Shunda 110 va 120 ga teng ikki ustunning koʻrinadigan qismi 10 va 20 boʻladi —
ikkinchi ustun ikki baravar baland koʻrinadi, holbuki haqiqiy oʻsish atigi 9 foiz. GMAT bunday
grafikni ham berishi mumkin, va toʻgʻri javob har doim <b>sonlardan</b> hisoblanadi, ustunlarning
koʻrinadigan balandligidan emas. Shuning uchun oʻqning pastki chegarasini birinchi boʻlib tekshiring va har doim ustun ustidagi raqamga tayaning.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Boʻsh joyli jumlani oʻqiganda avval jumlaning <b>oxirini</b> oʻqing: «… percent higher than in
  January» — baza yanvar; «… times the number in week 1» — nisbat. Jumlaning tuzilishi qaysi
  hisob kerakligini aytadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu boʻlimda kalkulyator bor, va grafik savollarida u haqiqatan foydali: 470 ÷ 1,580 kabi
  boʻlishlarni boshda qilish shart emas. Lekin variantlar bir-biridan uzoq boʻlsa, taxmin tezroq.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>percent higher than</b><span>… dan necha foiz koʻp — baza «than» dan keyin</span></li>
  <li><b>times the number</b><span>… marta — nisbat</span></li>
  <li><b>closest to</b><span>eng yaqin — taxmin mumkin</span></li>
  <li><b>trend</b><span>tendensiya, yoʻnalish</span></li>
  <li><b>in thousands</b><span>ming birlikda</span></li>
</ul>

<h3>GMAT savollari</h3>

{stem("Graphics Interpretation", "60 s", gl1 + "<p>Complete the statement: Revenue in Q4 was ____ higher than revenue in Q1.</p>",
    ["50%", "62.5%", "87.5%", "125%", "162.5%"], "B",
    "<p>(130 − 80) ÷ 80 = 0.625.</p><p><b>162.5%</b> — 130 ÷ 80: Q4 Q1 ning necha foizi, oʻsish emas.</p>")}

{trap("162.5%", "«Higher than» — oʻzgarish soʻralmoqda. Nisbatdan 100% ni ayiring.")}

{stem("Graphics Interpretation", "60 s", gl2 + "<p>Complete the statement: The median monthly number of visitors from January to June was ____.</p>",
    ["27,000", "28,333", "28,500", "30,000", "33,000"], "C",
    "<p>20, 24, 27, 30, 33, 36 → (27 + 30) ÷ 2 = 28.5 ming.</p><p><b>28,333</b> — oʻrtacha, mediana emas.</p>")}

{trap("28,333", "Oʻrtacha va mediana — har xil statistik. Mediana uchun tartiblang va oʻrtadagisini oling.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Grafik savolida <b>toʻrt narsani</b> belgilang:</p>
  <ol>
    <li>oʻqlar va birlik;</li>
    <li>shkala noldan boshlanadimi;</li>
    <li>jumla qaysi hisobni soʻraydi (farq, foiz, nisbat, oʻrtacha);</li>
    <li>baza — «than» dan keyingi qiymat.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">The tallest bar shows the biggest increase</p>
  <p class="pe-good">The biggest difference between neighbouring bars shows it</p>
  <p class="pe-fix__why">Oʻzgarish — farq, daraja emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">130 on a «$ thousands» axis → $130</p>
  <p class="pe-good">$130,000</p>
  <p class="pe-fix__why">Birlik oʻqning yonida yozilgan.</p>
</div>

<h3>Mashq</h3>

{quiz(1, "Using the revenue chart, what was the year's total revenue, in thousands of dollars?", "400 — 80 + 100 + 90 + 130.")}

{quiz(2, "By how many thousand dollars did revenue rise from Q1 to Q2?", "20 — 100 − 80.")}

{quiz(3, "Using the visitors chart, June's visitors were how many times January's?", "1.8 — 36 ÷ 20.")}

{quiz(4, "By what percent did visitors grow from January to June?", "80% — 16 ÷ 20.")}

{quiz(5, "What was the average quarterly revenue, in thousands of dollars?", "100 — 400 ÷ 4.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Graphics Interpretation</b><span>grafik talqini</span></li>
  <li><b>bar chart</b><span>ustunli diagramma</span></li>
  <li><b>line graph</b><span>chiziqli grafik</span></li>
  <li><b>axis</b><span>oʻq</span></li>
  <li><b>scale</b><span>shkala, masshtab</span></li>
  <li><b>drop-down menu</b><span>ochiladigan roʻyxat</span></li>
  <li><b>trend</b><span>tendensiya</span></li>
  <li><b>quarter</b><span>chorak</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Avval oʻqlar, birlik va shkala.</li>
    <li>Foiz oʻzgarishi = farq ÷ eski qiymat; nisbat — boshqa savol.</li>
    <li>Eng katta oʻzgarish — qoʻshni qiymatlar farqi.</li>
    <li>Mediana uchun tartiblang; oʻrtacha bilan adashtirmang.</li>
    <li>Jumlaning oxiri qaysi hisob kerakligini aytadi.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT33 = f"""
<h2>GMAT-33: Two-Part Analysis</h2>

<p>Two-Part Analysis savolida ekranda bitta jadval: ikki ustun (Part 1 va Part 2) va ularning
yonida bir xil variantlar roʻyxati. Har bir ustundan <mark>bittadan</mark> tanlaysiz, va ball
faqat <b>ikkalasi ham toʻgʻri</b> boʻlsa beriladi. Savollar matematik ham, mantiqiy ham boʻlishi
mumkin: ikki nomaʼlumli tenglama, ikki shartli tanlov, bir-biriga bogʻliq ikki qiymat.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ikki qismning bir-biriga bogʻliqligini koʻrasiz;</li>
    <li>avval bitta qismni topib, ikkinchisini undan chiqarasiz;</li>
    <li>bir xil variant ikkala ustun uchun ham toʻgʻri boʻlishi mumkinligini unutmaysiz;</li>
    <li>javobni ikkala shartga qoʻyib tekshirasiz.</li>
  </ul>
</div>

<h3>Ikki nomaʼlum — ikki shart</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">10 ta chipta: kattalar $12, bolalar $7, jami $95</span>
    <span class="pm-solve__why">Part 1 — kattalar, Part 2 — bolalar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Hammasi bolalar boʻlsa: 70; ortiqcha 25, har bir katta +5</span>
    <span class="pm-solve__why">GMAT-17 dagi «hammasi arzon» usuli</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Kattalar 5, bolalar 5</span>
    <span class="pm-solve__why">Tekshiruv: 60 + 35 = 95 ✓, 5 + 5 = 10 ✓</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki qism koʻpincha <b>bir-biriga bogʻliq</b>: bittasini topsangiz, ikkinchisi oddiy ayirish
  yoki boʻlish bilan chiqadi. Shuning uchun avval hisoblash osonroq boʻlgan qismni toping va
  ikkinchisini undan chiqaring — ikkalasini mustaqil yechmang.
</div>

<h3>Ikki mezonli tanlov</h3>

<p>Toʻrtta yetkazib beruvchi: P — $400, 6 kun; Q — $350, 9 kun; R — $480, 4 kun; S — $420, 5 kun.
Part 1: «6 kun ichida yetkazadiganlarning eng arzoni». Part 2: «$450 dan arzonlarning eng tezi».</p>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Part 1: 6 kungacha — P, R, S → eng arzon P ($400)</span>
    <span class="pm-solve__why">Avval filtr, keyin eng yaxshisi</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Part 2: $450 dan arzon — P, Q, S → eng tez S (5 kun)</span>
    <span class="pm-solve__why">R tez, lekin $480 — filtrdan oʻtmaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">P va S</span>
    <span class="pm-solve__why">Har bir ustun — oʻz sharti bilan</span>
  </div>
</div>

<h3>Bogʻliq ikki qiymat</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Tushum xarajatdan 5 baravar koʻp, foyda $40,000</span>
    <span class="pm-solve__why">Part 1 — xarajat, Part 2 — tushum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">5<i>C</i> − <i>C</i> = 40,000 → <i>C</i> = 10,000</span>
    <span class="pm-solve__why">Avval bitta qismni topamiz</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Tushum = 5 × 10,000 = 50,000</span>
    <span class="pm-solve__why">Ikkinchisi birinchisidan chiqadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Ikki shartli tanlovda <b>avval filtrlang</b> (kim shartga mos?), keyin <b>tanlang</b> (moslar
  ichida kim eng yaxshi?). Tartibni almashtirsangiz — eng tez yoki eng arzon variantni filtrdan
  oldin tanlab qoʻyasiz, va u shartga mos kelmasligi mumkin.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bir xil variant <b>ikkala ustun uchun ham</b> toʻgʻri boʻlishi mumkin — GMAT buni ataylab
  ishlatadi. «Ikkinchi ustunda boshqa variant boʻlishi kerak» degan fikrga tayanmang; har bir
  ustunni alohida, oʻz sharti bilan tekshiring.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Javobni topgach, uni <b>ikkala shartga</b> qoʻying. Ikki qismli savolda bitta qism toʻgʻri,
  ikkinchisi notoʻgʻri boʻlsa — ball nol, shuning uchun 10 soniyalik tekshiruv bu yerda ayniqsa
  qimmat.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>select one answer in each column</b><span>har bir ustundan bittadan tanlang</span></li>
  <li><b>make only two selections</b><span>faqat ikkita tanlov</span></li>
  <li><b>the same option may be correct for both</b><span>bir variant ikkalasi uchun ham toʻgʻri boʻlishi mumkin</span></li>
  <li><b>consistent with</b><span>… ga mos</span></li>
  <li><b>respectively</b><span>mos ravishda</span></li>
</ul>

<h3>GMAT savollari</h3>

{stem("Two-Part Analysis", "75 s", "<p>A museum sold 10 tickets for $95. Adult tickets cost $12 and child tickets cost $7. Select the number of adult tickets and the number of child tickets.</p>",
    [kit.pair("Adults", 4, "Children", 6), kit.pair("Adults", 5, "Children", 5), kit.pair("Adults", 6, "Children", 4), kit.pair("Adults", 5, "Children", 6), kit.pair("Adults", 7, "Children", 3)], "B",
    "<p>Hammasi bolalar uchun: 70; 25 ÷ 5 = 5 ta katta.</p><p><b>Adults: 5 · Children: 6</b> — summa toʻgʻri koʻrinsa ham, jami 11 chipta.</p>")}

{trap(kit.pair("Adults", 5, "Children", 6), "Bitta qism (kattalar) toʻgʻri, ikkinchisi xato — ball nol. Ikkala shartni ham tekshiring.")}

{stem("Two-Part Analysis", "90 s", "<p>Supplier P quotes $400 with delivery in 6 days; Q, $350 in 9 days; R, $480 in 4 days; S, $420 in 5 days. Select the cheapest supplier that delivers within 6 days and the fastest supplier that costs less than $450.</p>",
    [kit.pair("Cheapest within 6 days", "P", "Fastest under $450", "S"), kit.pair("Cheapest within 6 days", "Q", "Fastest under $450", "S"),
     kit.pair("Cheapest within 6 days", "P", "Fastest under $450", "R"), kit.pair("Cheapest within 6 days", "S", "Fastest under $450", "S"),
     kit.pair("Cheapest within 6 days", "P", "Fastest under $450", "P")], "A",
    "<p>6 kungacha: P, R, S → P. $450 dan arzon: P, Q, S → S.</p><p><b>Q</b> — eng arzon, lekin 9 kun; <b>R</b> — eng tez, lekin $480.</p>")}

{trap(kit.pair("Cheapest within 6 days", "Q", "Fastest under $450", "S"), "Filtrsiz «eng arzon»ni tanlash. Avval shart (6 kun), keyin eng arzoni.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Two-Part savolida:</p>
  <ol>
    <li>ikki qism qanday bogʻlanganini aniqlang (tenglama, filtr, ayirma);</li>
    <li>osonroq qismni toping, ikkinchisini undan chiqaring;</li>
    <li>javobni ikkala shartga qoʻyib tekshiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Cheapest supplier, then check the delivery time</p>
  <p class="pe-good">Filter by delivery time, then pick the cheapest</p>
  <p class="pe-fix__why">Shart — filtr; mezon — tanlov.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">The two columns must have different answers</p>
  <p class="pe-good">The same option may answer both columns</p>
  <p class="pe-fix__why">Har bir ustun mustaqil tekshiriladi.</p>
</div>

<h3>Mashq</h3>

{quiz(1, "<i>x</i> + <i>y</i> = 12 and <i>x</i> − <i>y</i> = 2. Find <i>x</i> and <i>y</i>.", "7 va 5 — qoʻshsak 2<i>x</i> = 14.")}

{quiz(2, "$2,000 at 5% a year for 3 years: find the simple interest and the interest compounded annually.", "300 va 315.25 dollar — 2,000 × 1.05<sup>3</sup> = 2,315.25.")}

{quiz(3, "For the data 2, 4, 6, 8, 30, find the mean and the median.", "10 va 6.")}

{quiz(4, "From 5 people, find the number of 2-person teams and the number of ways to choose a chair and a secretary.", "10 va 20.")}

{quiz(5, "Machine A makes 30 parts an hour and B makes 20. Together, find the hours to make 500 parts and the number A makes.", "10 soat va 300 ta.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Two-Part Analysis</b><span>ikki qismli tahlil</span></li>
  <li><b>column</b><span>ustun</span></li>
  <li><b>selection</b><span>tanlov</span></li>
  <li><b>criterion</b><span>mezon</span></li>
  <li><b>filter</b><span>saralab olmoq</span></li>
  <li><b>trade-off</b><span>murosa, nimadandir voz kechish</span></li>
  <li><b>supplier</b><span>yetkazib beruvchi</span></li>
  <li><b>respectively</b><span>mos ravishda</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Ikki ustun — bittadan tanlov; ikkalasi toʻgʻri boʻlsagina ball.</li>
    <li>Qismlar koʻpincha bogʻliq — birini toping, ikkinchisini chiqaring.</li>
    <li>Ikki shartli tanlov: avval filtr, keyin eng yaxshisi.</li>
    <li>Bir variant ikkala ustun uchun ham toʻgʻri boʻlishi mumkin.</li>
    <li>Javobni ikkala shartga qoʻyib tekshiring.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
LAUNCH = ("<p><b>Source 1 — Venue email.</b> Rooms cost $200 per day. A group of more than 30 people must use the "
          "large hall, which costs $350 per day. Catering costs $15 per person per day.</p>"
          "<p><b>Source 2 — Planned events.</b></p>" + EV)

GMAT34 = f"""
<h2>GMAT-34: Multi-Source Reasoning</h2>

<p>Multi-Source Reasoning — Data Insights'ning eng uzun savollari. Ekranda bir nechta
<mark>yorliq (tab)</mark> bor: birida xat, birida jadval, boshqasida grafik yoki eslatma. Ularga
bir nechta savol beriladi, va har bir savol uchun kerakli maʼlumot turli yorliqlarda
boʻlishi mumkin. Bu — rahbarning haqiqiy kuni: xat, jadval va siyosat hujjati, va ularni
birlashtirib qaror qabul qilish.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>savollarni oʻqishdan oldin har bir manbani tez koʻzdan kechirasiz;</li>
    <li>qaysi maʼlumot qaysi manbada ekanini qisqa yozib olasiz;</li>
    <li>qoidani (xatdan) va sonlarni (jadvaldan) birlashtirasiz;</li>
    <li>manbalar bir-birini aniqlashtirganda yoki cheklaganda buni sezasiz.</li>
  </ul>
</div>

<h3>Manbalar</h3>

{LAUNCH}

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Birinchi ish — har bir yorliqni <b>30 soniyada</b> koʻzdan kechirib, qisqa eslatma yozish:
  «1 — narxlar va qoidalar; 2 — tadbirlar jadvali». Keyin savollarga oʻtasiz va har bir
  savol uchun qaysi yorliqqa qaytishni darrov bilasiz.
</div>

<h3>Qoida + son</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Launch: 1 kun, 60 kishi</span>
    <span class="pm-solve__why">Manba 2 — sonlar</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">60 &gt; 30 → katta zal $350</span>
    <span class="pm-solve__why">Manba 1 — qoida</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">350 + 60 × 15 = 1,250</span>
    <span class="pm-solve__why">Ovqatlanish ham manba 1 dan</span>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Training: 2 kun, 25 kishi</span>
    <span class="pm-solve__why">30 dan kam — oddiy xona</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2 × 200 + 25 × 15 × 2 = 400 + 750 = 1,150</span>
    <span class="pm-solve__why">Kunlar soni ikkala qismga ham koʻpaytiriladi</span>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Workshop: 3 kun, 18 kishi</span>
    <span class="pm-solve__why">Oddiy xona</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3 × 200 + 18 × 15 × 3 = 600 + 810 = 1,410</span>
    <span class="pm-solve__why">Kam odam, lekin uzoqroq — qimmatroq</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Xatdagi <b>shartlarga</b> («more than 30», «per person per day», «not discounted») eʼtibor
  bering — ular jadvaldagi sonlarni qanday ishlatishni belgilaydi. Koʻp xato — shartni oʻqimay,
  jadvaldagi sonlarni toʻgʻridan-toʻgʻri koʻpaytirish.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Baʼzan manbalar bir-birini <b>aniqlashtiradi</b> (xat jadvaldagi sonni qanday sanashni aytadi)
  yoki <b>cheklaydi</b> (bir manba boshqasidagi variantni chiqarib tashlaydi). «Qaysi manba
  ustunroq?» savoli tugʻilsa, odatda aniqroq va keyinroq yozilgan qoida amal qiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu savollar uzun — boʻlimda eng koʻp vaqt oladi. Ular bir nechtadan keladi va bir xil
  manbalarga tayanadi, shuning uchun birinchi savolga sarflangan tanishish vaqti keyingilarida
  qaytadi. Birinchi savolda shoshilmang.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>according to the information provided</b><span>berilgan maʼlumotga koʻra</span></li>
  <li><b>can be inferred</b><span>xulosa qilish mumkin</span></li>
  <li><b>is consistent with</b><span>… ga mos keladi</span></li>
  <li><b>per person per day</b><span>har bir kishiga har kuni</span></li>
  <li><b>tab</b><span>yorliq — manba sahifasi</span></li>
</ul>

<h3>GMAT savollari</h3>

{stem("Multi-Source Reasoning", "75 s", LAUNCH + "<p>What will the Launch cost, including catering?</p>",
    ["$900", "$1,100", "$1,250", "$1,400", "$1,550"], "C",
    "<p>60 kishi — katta zal $350; ovqat 60 × 15 = 900; jami 1,250.</p><p><b>$1,100</b> — oddiy xona narxi bilan hisoblangan.</p>")}

{trap("$1,100", "Xatdagi «more than 30» sharti jadvaldagi 60 ga qoʻllanadi — katta zal.")}

{stem("Multi-Source Reasoning", "90 s", LAUNCH + "<p>Which of the following statements are true?</p>" + kit.statements(
    ["The Workshop will cost more than the Training.",
     "Only one of the events needs the large hall.",
     "Catering is more than half of the Training's total cost."]),
    ["I only", "I and II only", "II and III only", "I, II and III", "None of the statements"], "D",
    "<p>I — 1,410 &gt; 1,150. II — faqat Launch (60 kishi). III — 750 ÷ 1,150 ≈ 65%.</p><p><b>II and III only</b> — «kam odam — arzon» deb I ni rad etgan javob.</p>")}

{trap("II and III only", "Workshop'da odam kam, lekin 3 kun — kunlar soni ikkala xarajatga ham koʻpaytiriladi.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Multi-Source savollarida:</p>
  <ol>
    <li>har bir yorliqni koʻzdan kechiring va bir qatorda nima borligini yozing;</li>
    <li>savoldagi kalit soʻzni kerakli yorliqqa bogʻlang;</li>
    <li>qoida (xat) + son (jadval) — ikkalasini birlashtiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Launch: 200 + 60 × 15</p>
  <p class="pe-good">Launch: 350 + 60 × 15 (more than 30 → large hall)</p>
  <p class="pe-fix__why">Shart boshqa manbada edi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Workshop catering: 18 × 15</p>
  <p class="pe-good">18 × 15 × 3 days</p>
  <p class="pe-fix__why">«Per person per day» — kunlar soniga ham koʻpaytiriladi.</p>
</div>

<h3>Mashq</h3>

{quiz(1, "Using the two sources, what is the Training's total cost?", "1,150 dollar — 400 + 750.")}

{quiz(2, "What is the Workshop's catering cost?", "810 dollar — 18 × 15 × 3.")}

{quiz(3, "What does the room for the Launch cost?", "350 dollar — katta zal, 1 kun.")}

{quiz(4, "What is the total cost of all three events?", "3,810 dollar — 1,150 + 1,250 + 1,410.")}

{quiz(5, "If the Training grew to 35 people, what would its room cost per day?", "350 dollar — 30 dan koʻp, katta zal.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Multi-Source Reasoning</b><span>koʻp manbali mulohaza</span></li>
  <li><b>source</b><span>manba</span></li>
  <li><b>tab</b><span>yorliq</span></li>
  <li><b>policy</b><span>qoida, siyosat</span></li>
  <li><b>venue</b><span>tadbir oʻtkaziladigan joy</span></li>
  <li><b>catering</b><span>ovqatlanish xizmati</span></li>
  <li><b>infer</b><span>xulosa chiqarmoq</span></li>
  <li><b>discrepancy</b><span>nomuvofiqlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Avval barcha yorliqlarni koʻzdan kechiring va qisqa yozib oling.</li>
    <li>Xat — qoidalar, jadval — sonlar: ikkalasini birlashtiring.</li>
    <li>Shartlar («more than», «per day») sonlarni qanday ishlatishni aytadi.</li>
    <li>Manbalar bir-birini aniqlashtirishi yoki cheklashi mumkin.</li>
    <li>Birinchi savolga sarflangan vaqt keyingilarida qaytadi.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT35 = f"""
<h2>GMAT-35: Data Insights Strategy and Mixed Review</h2>

<p>Beshta savol turini oʻrgandingiz. Endi ular bitta 45 daqiqalik boʻlimda <mark>aralash</mark>
keladi: tez yechiladigan Data Sufficiency yonida uzun Multi-Source toʻplami, oddiy grafik yonida
uchta bayonotli jadval. Bu boʻlimda ball koʻpincha bilim yetmaganidan emas, vaqt notoʻgʻri
taqsimlanganidan yoʻqotiladi. Bu dars — Data Insights uchun reja.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>20 savol va 45 daqiqa uchun vaqt rejasi tuzasiz;</li>
    <li>kalkulyatordan qachon foydalanish va qachon foydalanmaslikni bilasiz;</li>
    <li>qisman ball yoʻqligini hisobga olib, koʻp qismli savollarda qaror qabul qilasiz;</li>
    <li>besh turdagi savolni tanib, har biriga mos usulni darrov tanlaysiz.</li>
  </ul>
</div>

<h3>Vaqt rejasi</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">45 daqiqa ÷ 20 savol = 2 daqiqa 15 soniya</span>
    <span class="pm-solve__why">Quant'dagidan biroz koʻp — savollar uzunroq</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">15-daqiqa — taxminan 7-savol; 30-daqiqa — taxminan 13-savol</span>
    <span class="pm-solve__why">Uchdan bir va uchdan ikki</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">DS va grafik — 1.5 daqiqa; Multi-Source — 3 daqiqagacha</span>
    <span class="pm-solve__why">Tez savollar uzunlarining vaqtini «toʻlaydi»</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu boʻlimda <b>qisman ball yoʻq</b>: uchta bayonotdan ikkitasi toʻgʻri boʻlsa ham — nol. Shuning
  uchun koʻp qismli savolda bir qismga ishonchingiz boʻlmasa, unga 3 daqiqa sarflash odatda
  foydasiz: eng ehtimoliy javobni belgilang va vaqtni yechilishi aniq savolga oʻtkazing.
</div>

<h3>Kalkulyator — qachon?</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">0.37 × 4,820 yoki 470 ÷ 1,580 — kalkulyator</span>
    <span class="pm-solve__why">Noqulay sonlar, variantlar bir-biriga yaqin</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">25% × 360 yoki 120 ÷ 40 — boshda</span>
    <span class="pm-solve__why">Ekrandagi kalkulyatorga sonlarni kiritish bundan sekinroq</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Data Sufficiency — deyarli hech qachon</span>
    <span class="pm-solve__why">Qiymat emas, yetarlilik soʻraladi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Har bir savolni ochganingizda birinchi 5 soniyada <b>turini</b> aniqlang va usulni tanlang:
  DS — AD/BCE; jadval — saralash; grafik — oʻqlar va baza; ikki qism — bogʻliqlik; koʻp manba —
  yorliqlar xaritasi. Tur aniq boʻlsa, qaysi qadamdan boshlash ham aniq.
</div>

<h3>Takrorlash: besh tur, besh usul</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Data Sufficiency → AD / BCE, hisoblamang</span>
    <span class="pm-solve__why">GMAT-26…30</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Table → sarlavhalar, saralash, chegaraviy soʻzlar</span>
    <span class="pm-solve__why">GMAT-31</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Graphics → birlik va baza; Two-Part → bogʻliqlik; Multi-Source → xarita</span>
    <span class="pm-solve__why">GMAT-32…34</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  GMAT'da boʻlimlar tartibini oʻzingiz tanlaysiz. Data Insights Quant va Verbal koʻnikmalarini
  aralashtirgani uchun, koʻpchilik uni ikkinchi oʻringa qoʻyadi — miya «qizigan», lekin hali
  charchamagan paytga. Sinov imtihonlarida ikki xil tartibni solishtirib koʻring.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Question Review &amp; Edit bu boʻlimda ham bor: savollarni belgilab, oxirida vaqt qolsa, koʻpi
  bilan uchta javobni oʻzgartirish mumkin — faqat yangi dalil topgan boʻlsangiz, shubha uchun emas. Uni koʻp qismli savollar uchun saqlang — aynan ularda
  bitta qismdagi xato butun ballni oladi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>each part</b><span>har bir qism — hammasi toʻgʻri boʻlishi kerak</span></li>
  <li><b>approximately</b><span>taxminan — kalkulyatorsiz baholang</span></li>
  <li><b>on-screen calculator</b><span>ekrandagi kalkulyator</span></li>
  <li><b>bookmark</b><span>belgilab qoʻyish</span></li>
  <li><b>time remaining</b><span>qolgan vaqt</span></li>
</ul>

<h3>GMAT savollari</h3>

{stem("Data Sufficiency", "45 s", "<p>What is the price of one child ticket?</p><p>(1) 3 adult tickets and 2 child tickets cost $50.</p><p>(2) An adult ticket costs $10.</p>",
    DS, "C", "<p>(1) — ikki nomaʼlum; (2) — bola chiptasi haqida yoʻq. Birga: 30 + 2<i>c</i> = 50.</p><p><b>A</b> — (1) dan «bitta tenglama yetadi» deb oʻylash.</p>")}

{trap(DS[0], "Bitta tenglamada ikki nomaʼlum — yagona qiymat chiqmaydi.")}

{stem("Graphics Interpretation", "60 s", gl3 + "<p>Complete the statement: Profit in Q4 was ____ higher than profit in Q1.</p>",
    ["20%", "30%", "33.3%", "50%", "150%"], "D",
    "<p>(90 − 60) ÷ 60 = 0.5.</p><p><b>33.3%</b> — farqni yangi qiymatga (90) boʻlgan javob.</p>")}

{trap("33.3%", "Baza — «than Q1», yaʼni eski qiymat 60.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Data Insights boʻlimida <b>uchta nazorat nuqtasi</b>:</p>
  <ol>
    <li>15-daqiqada ~7-savol, 30-daqiqada ~13-savol;</li>
    <li>koʻp qismli savolda bir qismga 3 daqiqadan koʻp sarflamang;</li>
    <li>oxirgi daqiqalarda har bir savolga javob belgilang — boʻsh joy qoldirmang.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Using the calculator for 25% of 360</p>
  <p class="pe-good">360 ÷ 4 = 90 in your head</p>
  <p class="pe-fix__why">Kalkulyatorga kiritish ogʻzaki hisobdan sekinroq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Spending 5 minutes on the third statement of a table question</p>
  <p class="pe-good">Best guess on it, bookmark, move on</p>
  <p class="pe-fix__why">Qisman ball yoʻq — uzoq kurash koʻpincha nol bilan tugaydi.</p>
</div>

<h3>Mashq</h3>

{quiz(1, "How many questions should you have finished by minute 30?", "13 atrofida — boʻlimning uchdan ikkisi.")}

{quiz(2, "How many answers can you change in Question Review &amp; Edit?", "3 tagacha.")}

{quiz(3, "A Two-Part question has one part right and one wrong. How many points does it earn?", "0 — qisman ball yoʻq.")}

{quiz(4, "With five choices, after you eliminate two, what is the chance that a guess is right?", "1/3 — qolgan uchtadan bittasi.")}

{quiz(5, "Using the profit chart, what was the year's total profit, in thousands of dollars?", "295 — 60 + 75 + 70 + 90.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>pacing</b><span>vaqtni taqsimlash</span></li>
  <li><b>partial credit</b><span>qisman ball</span></li>
  <li><b>multi-part question</b><span>koʻp qismli savol</span></li>
  <li><b>on-screen calculator</b><span>ekrandagi kalkulyator</span></li>
  <li><b>section order</b><span>boʻlimlar tartibi</span></li>
  <li><b>bookmark</b><span>belgilab qoʻymoq</span></li>
  <li><b>mixed review</b><span>aralash takrorlash</span></li>
  <li><b>checkpoint</b><span>nazorat nuqtasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>20 savol, 45 daqiqa: ~2 daqiqa 15 soniya; 15-daqiqada ~7, 30-daqiqada ~13.</li>
    <li>Qisman ball yoʻq — bir qismga uzoq kurashmang.</li>
    <li>Kalkulyator — noqulay sonlar uchun, oddiy foizlar uchun emas.</li>
    <li>Birinchi 5 soniyada turni aniqlang va usulni tanlang.</li>
    <li>Review &amp; Edit (3 ta) — koʻp qismli savollar uchun saqlang.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-31: Table Analysis",
        "category": "math", "order": 31,
        "summary": "Jadval tahlili: sarlavhalar va birliklar, saralash, bir xodimga hisob, ulush va mediana, uchta bayonotli savollar.",
        "stories": ["The Spreadsheet Nobody Sorted"],
        "content": GMAT31,
    },
    {
        "title": "GMAT-32: Graphics Interpretation",
        "category": "math", "order": 32,
        "summary": "Grafik talqini: oʻqlar, birlik va shkala, foiz oʻzgarishi va nisbat, eng katta oʻzgarish, oʻrtacha va mediana.",
        "stories": ["The Chart That Started at 100"],
        "content": GMAT32,
    },
    {
        "title": "GMAT-33: Two-Part Analysis",
        "category": "math", "order": 33,
        "summary": "Ikki qismli tahlil: bogʻliq qismlar, ikki shartli tanlov (avval filtr, keyin tanlov), bir variant ikkala ustunga ham.",
        "stories": ["Two Answers, One Decision"],
        "content": GMAT33,
    },
    {
        "title": "GMAT-34: Multi-Source Reasoning",
        "category": "math", "order": 34,
        "summary": "Koʻp manbali mulohaza: yorliqlar xaritasi, qoida va sonni birlashtirish, manbalar bir-birini aniqlashtirishi va cheklashi.",
        "stories": ["Three Emails and a Table"],
        "content": GMAT34,
    },
    {
        "title": "GMAT-35: Data Insights Strategy and Mixed Review",
        "category": "math", "order": 35,
        "summary": "Data Insights uchun vaqt rejasi, qisman ball yoʻqligi, kalkulyatordan qachon foydalanish va besh turdagi savol uchun besh usul.",
        "stories": ["Forty-Five Minutes of Data"],
        "content": GMAT35,
    },
]
