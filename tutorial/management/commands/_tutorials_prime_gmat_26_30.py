# -*- coding: utf-8 -*-
"""Prime GMAT — Data Insights, part one: GMAT-26 … GMAT-30, all Data Sufficiency.

Written with STYLE_GUIDE_PRIME_GMAT.md §7 · lesson list in toc_prime_gmat.txt.
Exam English in the stems, Uzbek for the teaching.

Facts (mba.com / gmac.com, checked 2026-10-02): Data Insights has 20 questions in 45 minutes,
an on-screen calculator, five question types (Data Sufficiency, Multi-Source Reasoning, Table
Analysis, Graphics Interpretation, Two-Part Analysis), and multi-part questions score only
when every part is correct.

The five Data Sufficiency verdicts are always the same and always in the same order (A–E);
they live in DS below and are copied, never retyped.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_gmat_26_30.py --author=prime
"""

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


def ds_stem(time, question, s1, s2, key, solution):
    """A Data Sufficiency exam card: question, two statements, the fixed five verdicts."""
    i = LET.index(key)
    items = "\n".join(f"    <li>{c}</li>" for c in DS)
    return f"""<div class="ps-stem">
  <p class="ps-stem__tag">GMAT-style question · Data Sufficiency <span class="ps-time">{time}</span></p>
  <div class="ps-stem__q">
    <p>{question}</p>
    <p>(1) {s1}</p>
    <p>(2) {s2}</p>
  </div>
  <ol class="ps-ch">
{items}
  </ol>
  <details class="ps-sol">
    <summary>Yechimni koʻrish</summary>
    <div class="ps-sol__body">
      <p class="ps-sol__ans">Javob: {key}) {DS[i]}</p>
      {solution}
    </div>
  </details>
</div>"""


def ds_trap(key, why):
    return f"""<div class="ps-trap">
  <span class="ps-trap__t">Tuzoq javob</span>
  <span class="ps-trap__val">{DS[LET.index(key)]}</span>
  <span class="ps-trap__why">{why}</span>
</div>"""


def ds_quiz(n, question, s1, s2, key, why):
    return f"""<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">{n}</span> {question} (1) {s1} (2) {s2}</p>
  <details class="pe-reveal"><summary>Javobni koʻrish</summary>
  <p class="pe-reveal__a">{key} — {DS[LET.index(key)]} {why}</p></details>
</div>"""


VERDICTS = """<ol>
  <li><b>A</b> — faqat (1) yetarli;</li>
  <li><b>B</b> — faqat (2) yetarli;</li>
  <li><b>C</b> — ikkalasi birga yetarli, alohida hech biri;</li>
  <li><b>D</b> — har biri alohida yetarli;</li>
  <li><b>E</b> — ikkalasi birga ham yetarli emas.</li>
</ol>"""

# ═════════════════════════════════════════════════════════════════════════
GMAT26 = f"""
<h2>GMAT-26: The Data Insights Section and Data Sufficiency</h2>

<p>Quant blokini tugatdingiz — endi GMAT'ning uchinchi boʻlimi, <mark>Data Insights</mark>.
Bu boʻlim biznesdagi eng kundalik savolni tekshiradi: <b>qoʻlimdagi maʼlumot qaror qabul qilish
uchun yetarlimi?</b> Uning yuragi — Data Sufficiency (maʼlumot yetarliligi) savollari. Ularda
javobni topish shart emas; faqat javob <b>topilishi mumkinmi</b>, shuni aniqlaysiz.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>Data Insights boʻlimining tuzilishini va vaqtini bilasiz;</li>
    <li>Data Sufficiency savolining beshta oʻzgarmas javobini yoddan aytasiz;</li>
    <li>«AD / BCE» usuli bilan har bir savolni ikki-uch qadamda hal qilasiz;</li>
    <li>savolni oxirigacha yechmasdan, yetarlilikni aniqlashni oʻrganasiz.</li>
  </ul>
</div>

<h3>Boʻlim qanday tuzilgan</h3>

<p>Data Insights — <b>20 ta savol, 45 daqiqa</b>, yaʼni bir savolga oʻrtacha 2 daqiqa 15 soniya.
Quant'dan farqli, bu boʻlimda <b>ekrandagi kalkulyator</b> bor. Savollar besh turda keladi:</p>

<ul>
  <li><b>Data Sufficiency</b> — maʼlumot yetarlimi;</li>
  <li><b>Table Analysis</b> — saralanadigan jadval;</li>
  <li><b>Graphics Interpretation</b> — grafik va diagramma;</li>
  <li><b>Two-Part Analysis</b> — ikki qismli javob;</li>
  <li><b>Multi-Source Reasoning</b> — bir nechta manbali maʼlumot.</li>
</ul>

<p>Koʻp qismli savollarda <b>barcha qismlar toʻgʻri</b> boʻlsagina ball beriladi — qisman
ball yoʻq. Bu darsdan GMAT-30 gacha faqat Data Sufficiency bilan ishlaymiz; qolgan turlar
GMAT-31 dan boshlanadi.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kalkulyator bor, lekin Data Sufficiency'da u deyarli kerak emas: savol qiymatni emas,
  qiymat <b>topilishi mumkinligini</b> soʻraydi. «3<i>x</i> + 2 = 11 dan <i>x</i> ni topsa
  boʻladi» — shu bilan toʻxtaysiz, <i>x</i> = 3 ekanini hisoblash ham shart emas.
</div>

<h3>Beshta oʻzgarmas javob</h3>

<p>Har bir Data Sufficiency savolida bitta savol va ikkita maʼlumot — (1) va (2) beriladi.
Javob variantlari <b>hamma savolda bir xil va bir xil tartibda</b>:</p>

{VERDICTS}

<p>Imtihonda ularni oʻqishga vaqt sarflamaslik uchun beshtasini yodlab oling — bu bir
martalik mehnat, keyin har bir savolda soniyalar tejaladi.</p>

<h3>AD / BCE usuli</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">1-qadam: (1) yolgʻiz yetarlimi?</span>
    <span class="pm-solve__why">Ha — javob A yoki D; yoʻq — javob B, C yoki E</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">2-qadam: (2) yolgʻiz yetarlimi?</span>
    <span class="pm-solve__why">(1) ni butunlay unutib tekshiring</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">3-qadam (faqat ikkalasi ham yetmasa): birgalikda?</span>
    <span class="pm-solve__why">Ha — C, yoʻq — E</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Qoralama qogʻozga har savol uchun «AD / BCE» deb yozing va keraksiz harflarni chizib boring.
  (1) yetarli boʻlsa, BCE ni chizasiz — endi faqat A yoki D qoldi, va savolning yarmi hal.
</div>

<h3>Birinchi misol</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">What is <i>x</i>? (1) 3<i>x</i> + 2 = 11 (2) <i>x</i><sup>2</sup> = 9</span>
    <span class="pm-solve__why">Bitta son soʻralmoqda</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(1): chiziqli tenglama — bitta yechim → yetarli → A yoki D</span>
    <span class="pm-solve__why">Yechimning oʻzini hisoblash shart emas</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(2): <i>x</i> = 3 yoki −3 → yetarli emas → <b>A</b></span>
    <span class="pm-solve__why">Ikki xil qiymat — javob yagona emas</span>
  </div>
</div>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">What is <i>y</i>? (1) <i>y</i> = 2<i>x</i> (2) <i>x</i> = 5</span>
    <span class="pm-solve__why">(1) — <i>x</i> nomaʼlum; (2) — <i>y</i> haqida hech narsa yoʻq</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Birgalikda: <i>y</i> = 10 → <b>C</b></span>
    <span class="pm-solve__why">Hech biri yolgʻiz yetmaydi, ikkalasi birga yetadi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki qoida hech qachon buzilmaydi: maʼlumotlar <b>har doim toʻgʻri</b> va <b>bir-biriga zid
  kelmaydi</b>. Shuning uchun «(2) notoʻgʻri boʻlsa-chi?» deb oʻylash shart emas. Lekin (2) ni
  yolgʻiz tekshirayotganda (1) dagi maʼlumotni <b>ishlatmang</b> — bu eng koʻp uchraydigan xato.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bizda maktabdan qolgan odat — har bir masalani oxirigacha yechish. Data Sufficiency'da bu
  vaqtni oʻgʻirlaydi: «yechim bitta boʻladimi?» degan savolga javob topilishi bilan toʻxtang.
  Ikki daqiqalik savolni 40 soniyada yopish — shu odatdan voz kechish natijasi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>sufficient</b><span>yetarli — yagona javob beradi</span></li>
  <li><b>alone</b><span>yolgʻiz, boshqasisiz</span></li>
  <li><b>together</b><span>birgalikda</span></li>
  <li><b>determine</b><span>aniqlamoq — yagona javobni topa olmoq</span></li>
  <li><b>what is the value of</b><span>qiymati nechaga teng — bitta son kerak</span></li>
</ul>

<h3>GMAT savollari</h3>

{ds_stem("45 s", "What is the value of <i>x</i>?", "2<i>x</i> + 5 = 13", "<i>x</i><sup>2</sup> = 16", "A",
 "<p>(1): <i>x</i> = 4 — yagona. (2): <i>x</i> = 4 yoki −4 — ikki qiymat, yetarli emas.</p><p><b>D</b> — (2) dan faqat musbat ildizni olgan javob; <i>x</i> manfiy ham boʻlishi mumkin.</p>")}

{ds_trap("D", "<i>x</i><sup>2</sup> = 16 ikki qiymat beradi. (1) dagi «<i>x</i> = 4» ni (2) ni tekshirayotganda xayolga keltirmang.")}

{ds_stem("60 s", "A shop sold 120 shirts, each either red or blue. How many of the shirts were red?", "25% of the shirts were red.", "90 of the shirts were blue.", "D",
 "<p>(1): 0.25 × 120 = 30 — yetarli. (2): 120 − 90 = 30 — yetarli.</p><p><b>C</b> — har birini alohida tekshirmay, «ikkalasini birga ishlatsa boʻladi» deb shoshilgan javob.</p>")}

{ds_trap("C", "Ikkalasi birga yetarli — toʻgʻri, lekin har biri <b>yolgʻiz ham</b> yetarli. Avval alohida tekshiring.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Data Sufficiency'da <b>tartib qatʼiy</b>:</p>
  <ol>
    <li>savol nimani soʻrayotganini yozing (bitta qiymatmi, ha/yoʻqmi);</li>
    <li>(1) ni yolgʻiz, keyin (2) ni yolgʻiz tekshiring;</li>
    <li>faqat ikkalasi ham yetmasa, ularni birlashtiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">(2) ni tekshirishda (1) dagi maʼlumotdan foydalanish</p>
  <p class="pe-good">(2) ni xuddi (1) yoʻqdek tekshirish</p>
  <p class="pe-fix__why">Aks holda B yoki D oʻrniga notoʻgʻri javob chiqadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><i>x</i> = 3 ni topish uchun hisoblashni oxirigacha davom ettirish</p>
  <p class="pe-good">«Chiziqli tenglama — bitta yechim» deb toʻxtash</p>
  <p class="pe-fix__why">Savol qiymatni emas, yetarlilikni soʻraydi.</p>
</div>

<h3>Mashq</h3>

{ds_quiz(1, "What is <i>x</i>?", "<i>x</i> + 4 = 10", "<i>x</i> − 4 = 2", "D", "Ikkalasi ham <i>x</i> = 6 beradi.")}

{ds_quiz(2, "What is <i>x</i>?", "<i>x</i><sup>2</sup> = 1", "<i>x</i> &lt; 0", "C", "(1) — ±1; birgalikda −1.")}

{ds_quiz(3, "What is <i>a</i> + <i>b</i>?", "<i>a</i> + <i>b</i> − 3 = 7", "<i>a</i> = 4", "A", "(1) dan <i>a</i> + <i>b</i> = 10.")}

{ds_quiz(4, "What is <i>y</i>?", "<i>x</i> + <i>y</i> = 6", "2<i>x</i> + 2<i>y</i> = 12", "E", "(2) — (1) ning ikki baravari, yangi maʼlumot yoʻq.")}

{ds_quiz(5, "What is the price of one bottle of water?", "A box of water costs $18.", "12 bottles of water cost $18.", "B", "(1) — qutida nechta shisha borligi nomaʼlum.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Data Insights</b><span>maʼlumot tahlili boʻlimi</span></li>
  <li><b>Data Sufficiency</b><span>maʼlumot yetarliligi</span></li>
  <li><b>statement</b><span>maʼlumot, shart</span></li>
  <li><b>sufficient</b><span>yetarli</span></li>
  <li><b>alone</b><span>yolgʻiz</span></li>
  <li><b>together</b><span>birgalikda</span></li>
  <li><b>determine</b><span>aniqlamoq</span></li>
  <li><b>on-screen calculator</b><span>ekrandagi kalkulyator</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Data Insights: 20 savol, 45 daqiqa, kalkulyator bor, koʻp qismli savolda qisman ball yoʻq.</li>
    <li>DS javoblari doim bir xil: A, B, C, D, E — yodlang.</li>
    <li>AD / BCE: avval (1) yolgʻiz, keyin (2) yolgʻiz, keyin birga.</li>
    <li>Maʼlumotlar har doim toʻgʻri va bir-biriga zid emas.</li>
    <li>Qiymatni emas, uning yagona ekanini aniqlang — va toʻxtang.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT27 = f"""
<h2>GMAT-27: Data Sufficiency — Value Questions</h2>

<p>«What is the value of …?» — Data Sufficiency savollarining eng koʻp turi. Bunday savolda
maʼlumot <mark>aynan bitta qiymat</mark> bersagina yetarli. Ikki qiymat — yetarli emas, hatto
ikkalasi «yaqin» boʻlsa ham. Bu darsda qachon bitta qiymat chiqishini tez koʻrishni
oʻrganamiz: tenglamalar soni, soʻralgan ifoda va yashirin cheklovlar.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>«nomaʼlumlar soni = mustaqil tenglamalar soni» qoidasini va uning istisnolarini bilasiz;</li>
    <li>soʻralgan ifodani (<i>x</i> + <i>y</i>) har bir oʻzgaruvchisiz topish mumkinligini koʻrasiz;</li>
    <li>kvadrat tenglama va modul ikki qiymat berishini unutmaysiz;</li>
    <li>savoldagi cheklovlardan («<i>x</i> is positive») foydalanasiz.</li>
  </ul>
</div>

<h3>Tenglamalar soni — asosiy qoida</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">What is <i>x</i>? (1) <i>x</i> + <i>y</i> = 10 (2) <i>x</i> − <i>y</i> = 4</span>
    <span class="pm-solve__why">Ikki nomaʼlum</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Har biri yolgʻiz — bitta tenglama, ikki nomaʼlum → yetarli emas</span>
    <span class="pm-solve__why">BCE qoladi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Birga — ikki mustaqil tenglama → <b>C</b></span>
    <span class="pm-solve__why">Qoʻshsak 2<i>x</i> = 14; hisoblash shart emas</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoida — «<i>n</i> ta nomaʼlum uchun <i>n</i> ta <b>mustaqil chiziqli</b> tenglama». Ikki istisnoga
  eʼtibor bering: bir tenglama ikkinchisining nusxasi boʻlsa (<i>x</i> + <i>y</i> = 10 va
  2<i>x</i> + 2<i>y</i> = 20), u yangi maʼlumot bermaydi; tenglama kvadrat yoki modulli boʻlsa,
  bitta tenglama ham ikki qiymat berishi mumkin.
</div>

<h3>Soʻralgan ifodaga qarang</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">What is <i>x</i> + <i>y</i>? (1) 2<i>x</i> + 2<i>y</i> = 18</span>
    <span class="pm-solve__why">Ikki nomaʼlum, bitta tenglama — lekin…</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">2(<i>x</i> + <i>y</i>) = 18 → <i>x</i> + <i>y</i> = 9 → yetarli</span>
    <span class="pm-solve__why"><i>x</i> va <i>y</i> alohida nomaʼlum, lekin savol ularni soʻramagan</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savol ifodani soʻrasa, maʼlumotni <b>shu ifoda shakliga</b> keltirishga urining:
  «What is 2<i>a</i> + 6<i>b</i>?» va «<i>a</i> + 3<i>b</i> = 7» — ikkiga koʻpaytirsangiz, javob 14.
  <i>a</i> va <i>b</i> ni hech qachon alohida topmaysiz.
</div>

<h3>Kvadrat va cheklov</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">What is <i>x</i>? (1) <i>x</i><sup>2</sup> − 5<i>x</i> + 6 = 0 (2) <i>x</i> is odd</span>
    <span class="pm-solve__why">(1): <i>x</i> = 2 yoki 3 → yetarli emas</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(2): cheksiz koʻp toq son → yetarli emas</span>
    <span class="pm-solve__why">BCE dan C yoki E qoldi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Birga: 2 yoki 3 dan faqat 3 toq → <b>C</b></span>
    <span class="pm-solve__why">Cheklov ikki qiymatdan birini kesib tashladi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Yetarli» — <b>yagona</b> degani. <i>x</i> = 2 yoki 3 — ikkalasi ham kichik, yaqin sonlar,
  lekin baribir ikki xil qiymat, demak yetarli emas. Biznes tilida: hisobot «foyda 2 yoki
  3 million» desa, rahbar aniq qaror qabul qila olmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Savol matnidagi cheklovlar — maʼlumotning bir qismi: «<i>x</i> is positive», «<i>n</i> is an integer»,
  «the number of employees». Ular har ikkala maʼlumotga ham qoʻshiladi. Masalan, savolda
  «<i>x</i> &gt; 0» boʻlsa, <i>x</i><sup>2</sup> = 9 yolgʻiz ham yetarli.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>what is the value of</b><span>yagona qiymat kerak</span></li>
  <li><b>can be determined</b><span>aniqlash mumkin</span></li>
  <li><b>is a positive integer</b><span>musbat butun son — yashirin cheklov</span></li>
  <li><b>in terms of</b><span>… orqali — savol ifodani soʻrashi mumkin</span></li>
  <li><b>the ratio of</b><span>nisbat — ifoda, qiymatlar emas</span></li>
</ul>

<h3>GMAT savollari</h3>

{ds_stem("45 s", "What is the value of <i>x</i> + <i>y</i>?", "2<i>x</i> + 2<i>y</i> = 18", "<i>x</i> − <i>y</i> = 3", "A",
 "<p>(1): <i>x</i> + <i>y</i> = 9 — yetarli. (2): faqat ayirma — yigʻindini bermaydi.</p><p><b>C</b> — «ikki nomaʼlumga ikki tenglama kerak» deb (1) ni yolgʻiz rad etgan javob.</p>")}

{ds_trap("C", "Savol <i>x</i> va <i>y</i> ni emas, ularning yigʻindisini soʻraydi — (1) uni bevosita beradi.")}

{ds_stem("60 s", "What is the value of <i>x</i>?", "<i>x</i><sup>2</sup> − 5<i>x</i> + 6 = 0", "<i>x</i> is an odd integer.", "C",
 "<p>(1): 2 yoki 3. (2): istalgan toq son. Birga: faqat 3.</p><p><b>A</b> — kvadrat tenglama ikki ildiz berishini unutgan javob.</p>")}

{ds_trap("A", "Kvadrat tenglama — odatda ikki ildiz. Ildizlarni tez toping va ikkalasi qolishini tekshiring.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Qiymat savolida <b>ikki savol bering</b>:</p>
  <ol>
    <li>maʼlumot soʻralgan ifodani bevosita beradimi (koʻpaytirish, qoʻshish bilan)?</li>
    <li>ikki xil qiymat chiqishi mumkinmi — kvadrat, modul, juft daraja?</li>
    <li>savoldagi cheklov ulardan birini kesib tashlaydimi?</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad"><i>x</i> + <i>y</i> = 10 va 2<i>x</i> + 2<i>y</i> = 20 → ikki tenglama → C</p>
  <p class="pe-good">Bitta maʼlumotning ikki koʻrinishi → E</p>
  <p class="pe-fix__why">Mustaqil boʻlmagan tenglama yangi maʼlumot bermaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><i>x</i><sup>2</sup> = 25 → <i>x</i> = 5 → yetarli</p>
  <p class="pe-good"><i>x</i> = 5 yoki −5 → yetarli emas (agar cheklov boʻlmasa)</p>
  <p class="pe-fix__why">Juft daraja ishorani yoʻqotadi.</p>
</div>

<h3>Mashq</h3>

{ds_quiz(1, "What is <i>x</i>?", "4<i>x</i> = 20", "<i>x</i><sup>2</sup> = 25", "A", "(2) — ±5.")}

{ds_quiz(2, "What is <i>x</i>?", "<i>x</i> + <i>y</i> = 8", "3<i>x</i> + 3<i>y</i> = 24", "E", "Ikkalasi bitta tenglama.")}

{ds_quiz(3, "What is 3<i>a</i> + 3<i>b</i>?", "<i>a</i> = 2", "<i>a</i> + <i>b</i> = 5", "B", "(2) ni uchga koʻpaytiring: 15.")}

{ds_quiz(4, "What is <i>x</i>?", "<i>x</i><sup>2</sup> = 49", "<i>x</i> &gt; 0", "C", "(1) — ±7; birga 7.")}

{ds_quiz(5, "A phone plan charges a fixed monthly fee plus a charge per gigabyte. What is the monthly fee?",
 "3 GB cost $25 and 6 GB cost $40.", "Each gigabyte costs $5.", "A", "(1) — ikki nuqta, farq 3 GB uchun $15, demak fee $10.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>value question</b><span>qiymat savoli</span></li>
  <li><b>unique value</b><span>yagona qiymat</span></li>
  <li><b>independent equations</b><span>mustaqil tenglamalar</span></li>
  <li><b>unknown</b><span>nomaʼlum</span></li>
  <li><b>constraint</b><span>cheklov</span></li>
  <li><b>expression</b><span>ifoda</span></li>
  <li><b>root</b><span>ildiz</span></li>
  <li><b>fixed fee</b><span>doimiy toʻlov</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Qiymat savolida yetarli = aynan bitta qiymat.</li>
    <li>n nomaʼlum — n mustaqil chiziqli tenglama; nusxa tenglama yangi maʼlumot emas.</li>
    <li>Soʻralgan ifodani bevosita qidiring — oʻzgaruvchilar kerak boʻlmasligi mumkin.</li>
    <li>Kvadrat va modul odatda ikki qiymat beradi.</li>
    <li>Savoldagi cheklovlar ikkala maʼlumotga ham tegishli.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT28 = f"""
<h2>GMAT-28: Data Sufficiency — Yes/No Questions</h2>

<p>«Is <i>x</i> &gt; 0?», «Is <i>n</i> even?» — bunday savollarda javob son emas, <b>ha</b> yoki
<b>yoʻq</b>. Maʼlumot yetarli, agar u <mark>har doim «ha»</mark> yoki <mark>har doim «yoʻq»</mark>
desa. Eng muhim nuqta: aniq «yoʻq» ham yetarli javob. Koʻp nomzod «yoʻq» chiqqanda «yetarli
emas» deb belgilab, ochkoni yoʻqotadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>ha/yoʻq savolida yetarlilik taʼrifini toʻgʻri qoʻllaysiz;</li>
    <li>aniq «yoʻq»ni «yetarli» deb tanib olasiz;</li>
    <li>maʼlumotni buzish uchun son tanlaysiz — bir «ha» va bir «yoʻq» qidirib;</li>
    <li>juft/toq va ishora qoidalarini (GMAT-4) DS ichida ishlatasiz.</li>
  </ul>
</div>

<h3>Har doim «ha» — yetarli</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Is <i>x</i> &gt; 0? (1) <i>x</i><sup>3</sup> &gt; 0</span>
    <span class="pm-solve__why">Toq daraja ishorani saqlaydi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Har doim <i>x</i> &gt; 0 → «ha» → yetarli</span>
    <span class="pm-solve__why">(2) <i>x</i><sup>2</sup> &gt; 0 esa: <i>x</i> = 2 → ha, <i>x</i> = −2 → yoʻq → yetarli emas</span>
  </div>
</div>

<h3>Har doim «yoʻq» — ham yetarli</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Is <i>p</i> prime? (2) 20 &lt; <i>p</i> &lt; 23, <i>p</i> butun son</span>
    <span class="pm-solve__why"><i>p</i> = 21 yoki 22</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">21 = 3 × 7, 22 = 2 × 11 — ikkalasi ham tub emas</span>
    <span class="pm-solve__why">Javob har doim «yoʻq»</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Aniq «yoʻq» → <b>yetarli</b></span>
    <span class="pm-solve__why">Savolga aniq javob berdik — yoʻnalishi muhim emas</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Sufficient» — «javob <b>ha</b>» degani emas, «javob <b>aniq</b>» degani. Rahbar «loyiha
  byudjetdan oshadimi?» deb soʻrasa va siz aniq «yoʻq, oshmaydi» desangiz — bu toʻliq javob.
  Faqat «balki ha, balki yoʻq» — yetarli emas.
</div>

<h3>Son tanlab buzish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Is <i>xy</i> &gt; 0? (1) <i>x</i> &gt; 0</span>
    <span class="pm-solve__why">Bir «ha» va bir «yoʻq» qidiramiz</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step"><i>x</i> = 1, <i>y</i> = 1 → ha; <i>x</i> = 1, <i>y</i> = −1 → yoʻq</span>
    <span class="pm-solve__why">Ikki xil javob topildi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">→ yetarli emas</span>
    <span class="pm-solve__why">Bitta qarshi juft — maʼlumotni yiqitish uchun yetadi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Son tanlaganda roʻyxatni eslang (GMAT-4): <b>manfiy, 0, 1, kasr, katta son</b>. Ha/yoʻq
  savolining tuzogʻi koʻpincha shulardan birida yashiringan — ayniqsa 0 va manfiy sonlarda.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ha/yoʻq savolida maqsad — maʼlumotni <b>buzish</b>. «Ha» beradigan bitta misolni topib,
  «yetarli» deb shoshilmang: endi «yoʻq» beradigan misol qidiring. Topa olmasangiz va qoida
  bilan isbotlasangiz (masalan, toq daraja), shundagina yetarli.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki maʼlumot birga aniq «yoʻq» bersa, javob — <b>C</b>, E emas. «Is <i>xy</i> &gt; 0?
  (1) <i>x</i> &gt; 0 (2) <i>y</i> &lt; 0» — birga <i>xy</i> doim manfiy, demak aniq «yoʻq», yaʼni yetarli.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>is x greater than y</b><span>x y dan kattami — ha/yoʻq</span></li>
  <li><b>is n divisible by 6</b><span>n 6 ga boʻlinadimi</span></li>
  <li><b>definite answer</b><span>aniq javob — ha yoki yoʻq</span></li>
  <li><b>always / never</b><span>har doim / hech qachon — ikkalasi ham yetarli</span></li>
  <li><b>sometimes</b><span>baʼzan — yetarli emas</span></li>
</ul>

<h3>GMAT savollari</h3>

{ds_stem("45 s", "If <i>n</i> is an integer, is <i>n</i> even?", "<i>n</i> is a multiple of 4.", "<i>n</i><sup>2</sup> is a multiple of 4.", "D",
 "<p>(1): 4 ning karralisi — har doim juft. (2): <i>n</i> toq boʻlsa, <i>n</i><sup>2</sup> ham toq — 4 ga boʻlinmaydi; demak <i>n</i> juft.</p><p><b>A</b> — (2) ni «<i>n</i><sup>2</sup> juft, lekin <i>n</i> toq boʻlishi mumkin» deb oʻylagan javob.</p>")}

{ds_trap("A", "Toq sonning kvadrati har doim toq. Kvadrat juft (va 4 ga boʻlinadigan) boʻlsa, son ham juft.")}

{ds_stem("60 s", "Is <i>xy</i> &gt; 0?", "<i>x</i> &gt; 0", "<i>y</i> &lt; 0", "C",
 "<p>Har biri yolgʻiz — ikkinchi oʻzgaruvchining ishorasi nomaʼlum. Birga: musbat × manfiy = manfiy — aniq «yoʻq».</p><p><b>E</b> — «javob yoʻq chiqdi» deb yetarli emas deb belgilagan javob.</p>")}

{ds_trap("E", "Aniq «yoʻq» — ham yetarli javob. Birga ishorasi har doim manfiy, demak C.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Ha/yoʻq savolida <b>ikkita misol</b> qidiring:</p>
  <ol>
    <li>maʼlumotni qanoatlantiradigan va «ha» beradigan son;</li>
    <li>maʼlumotni qanoatlantiradigan va «yoʻq» beradigan son;</li>
    <li>ikkalasi topilsa — yetarli emas; faqat bittasi mumkin boʻlsa — yetarli.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Javob har doim «yoʻq» → yetarli emas</p>
  <p class="pe-good">Javob har doim «yoʻq» → yetarli</p>
  <p class="pe-fix__why">Yetarlilik — javobning aniqligi, yoʻnalishi emas.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">Bitta «ha» misol topildi → yetarli</p>
  <p class="pe-good">«Yoʻq» misol ham qidirildi va topilmadi → yetarli</p>
  <p class="pe-fix__why">Bitta misol hech narsani isbotlamaydi, bitta qarshi misol esa rad etadi.</p>
</div>

<h3>Mashq</h3>

{ds_quiz(1, "Is <i>x</i> &gt; 3?", "<i>x</i> &gt; 5", "<i>x</i> &gt; 1", "A", "(2) — <i>x</i> = 2 yoki 4.")}

{ds_quiz(2, "If <i>n</i> is an integer, is <i>n</i> odd?", "2<i>n</i> is even.", "<i>n</i><sup>2</sup> is odd.", "B", "(1) har qanday butun son uchun toʻgʻri — maʼlumot yoʻq.")}

{ds_quiz(3, "Is <i>x</i> positive?", "<i>x</i> &gt; −1", "<i>x</i> &lt; 1", "E", "Birga −1 &lt; <i>x</i> &lt; 1: 0.5 — ha, 0 — yoʻq.")}

{ds_quiz(4, "Is <i>a</i> &gt; <i>b</i>?", "<i>a</i> − <i>b</i> = 2", "<i>b</i> − <i>a</i> = −2", "D", "Ikkalasi bitta maʼlumot va har biri «ha».")}

{ds_quiz(5, "Did a company's revenue from a product exceed $1 million last year?", "It sold 50,000 units.", "It sold every unit for $25.", "C", "Birga $1.25 million — aniq «ha».")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>yes/no question</b><span>ha/yoʻq savoli</span></li>
  <li><b>definite</b><span>aniq</span></li>
  <li><b>always</b><span>har doim</span></li>
  <li><b>counterexample</b><span>qarshi misol</span></li>
  <li><b>even / odd</b><span>juft / toq</span></li>
  <li><b>prime</b><span>tub son</span></li>
  <li><b>divisible</b><span>boʻlinadigan</span></li>
  <li><b>positive / negative</b><span>musbat / manfiy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Ha/yoʻq savolida yetarli = har doim «ha» yoki har doim «yoʻq».</li>
    <li>Aniq «yoʻq» ham yetarli.</li>
    <li>Bir «ha» va bir «yoʻq» misol qidiring — ikkalasi topilsa, yetarli emas.</li>
    <li>Son roʻyxati: manfiy, 0, 1, kasr, katta son.</li>
    <li>Birga aniq «yoʻq» chiqsa — C, E emas.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT29 = f"""
<h2>GMAT-29: Data Sufficiency — Traps and Hidden Constraints</h2>

<p>Data Sufficiency'da xatolarning koʻpi matematikadan emas, <mark>tuzoqlardan</mark> keladi.
GMAT ularni ongli ravishda qoʻyadi: ikkala maʼlumot birga «aniq ishlaydi» degan C tuzogʻi,
bir xil maʼlumotni ikki xil koʻrinishda berish, va savol matnida yashiringan cheklovlar. Bu
dars uchala tuzoqni tanib olishni oʻrgatadi.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>C tuzogʻini — bitta maʼlumot oʻzi yetarli boʻlgan holatni tanib olasiz;</li>
    <li>ikki xil koʻrinishdagi bir xil maʼlumotni koʻrasiz;</li>
    <li>«soni», «butun», «musbat» kabi yashirin cheklovlardan foydalanasiz;</li>
    <li>savolning oʻzi javobni berishi mumkinligini tekshirasiz.</li>
  </ul>
</div>

<h3>1-tuzoq: «Birga aniq ishlaydi» (C tuzogʻi)</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">What is <i>x</i>? (1) 2<i>x</i> + 3<i>y</i> = 12 and <i>y</i> = 2 (2) <i>y</i> = 2</span>
    <span class="pm-solve__why">Birga — albatta yetarli, lekin…</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">(1) ning oʻzida <i>y</i> = 2 bor → 2<i>x</i> = 6</span>
    <span class="pm-solve__why">(1) yolgʻiz yetarli</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(2) yolgʻiz — <i>x</i> haqida hech narsa → <b>A</b></span>
    <span class="pm-solve__why">C — eng koʻp tanlanadigan notoʻgʻri javob</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki maʼlumot birga ishlashi <b>juda oson</b> koʻrinsa, toʻxtang. GMAT bunday savollarni
  koʻpincha shunday tuzadi: maʼlumotlardan biri oʻzi yetarli, ikkinchisi esa uni «takrorlaydi».
  C ni belgilashdan oldin har birini yana bir marta alohida tekshiring.
</div>

<h3>2-tuzoq: bir maʼlumot, ikki koʻrinish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Narx? (1) 3 daftar + 2 ruchka = $13 (2) 6 daftar + 4 ruchka = $26</span>
    <span class="pm-solve__why">Ikki tenglama koʻrinadi</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(2) = (1) × 2 → yangi maʼlumot yoʻq → <b>E</b></span>
    <span class="pm-solve__why">Ikki tenglama — lekin mustaqil emas</span>
  </div>
</div>

<h3>3-tuzoq: yashirin cheklov</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Ruchka $3, daftar $5, jami $19, har biridan kamida bitta. Ruchkalar soni?</span>
    <span class="pm-solve__why">Sonlar — musbat butun son</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">3<i>p</i> + 5<i>n</i> = 19: <i>n</i> = 1 → 14/3; <i>n</i> = 2 → <i>p</i> = 3; <i>n</i> = 3 → 4/3</span>
    <span class="pm-solve__why">Butun yechim faqat bitta</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Savolning oʻzi <i>p</i> = 3 ni beradi → har qanday (toʻgʻri) maʼlumot yetarli → <b>D</b></span>
    <span class="pm-solve__why">Bitta tenglama, ikki nomaʼlum — lekin butunlik cheklovi hal qildi</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Savolda <b>sanaladigan narsa</b> (odamlar, chiptalar, qutilar) boʻlsa, ular musbat butun son.
  «Bitta tenglama, ikki nomaʼlum — yetarli emas» qoidasi bu yerda ishlamasligi mumkin: butun
  yechimlarni tekshirib chiqing, ular koʻpincha bitta-ikkita boʻladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Savolni oʻqiganingizda avval <b>maʼlumotlarsiz</b> soʻrang: «savolning oʻzidan nima bilaman?»
  Baʼzan savolning oʻzi javobni deyarli beradi, va maʼlumotlar faqat tasdiqlaydi. Bu D yoki
  kutilmagan A/B javoblarining manbai.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Haqiqiy imtihonda ikki maʼlumot <b>hech qachon bir-biriga zid kelmaydi</b>. Agar (1) va (2)
  ni birga qoʻyganda hech qanday son mos kelmasa, xato sizning hisobingizda — qayta tekshiring.
  Bu qoidadan foydalanish ham mumkin: ikkala maʼlumotga mos keladigan bitta misol topsangiz,
  u ikkala yetarlilik tekshiruvida ham ishlaydi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>at least one of each</b><span>har biridan kamida bitta</span></li>
  <li><b>the number of</b><span>soni — musbat butun son</span></li>
  <li><b>exactly</b><span>aynan</span></li>
  <li><b>different from</b><span>… dan farqli</span></li>
  <li><b>each</b><span>har biri — narx yoki miqdor bir xil</span></li>
</ul>

<h3>GMAT savollari</h3>

{ds_stem("45 s", "What is the price of one notebook?", "3 notebooks and 2 pens cost a total of $13.", "6 notebooks and 4 pens cost a total of $26.", "E",
 "<p>(2) — (1) ning aynan ikki baravari; birga ham bitta tenglama, ikki nomaʼlum.</p><p><b>C</b> — «ikki tenglama, ikki nomaʼlum» deb shoshilgan javob.</p>")}

{ds_trap("C", "Ikki tenglama mustaqil boʻlishi kerak. (2) ni ikkiga boʻlsangiz, (1) chiqadi — yangi maʼlumot yoʻq.")}

{ds_stem("75 s", "A customer spent exactly $19 on pens that cost $3 each and notebooks that cost $5 each, buying at least one of each. How many pens did the customer buy?", "The customer bought at least 2 notebooks.", "The customer bought at least 2 pens.", "D",
 "<p>Savolning oʻzi: 3<i>p</i> + 5<i>n</i> = 19 ning musbat butun yechimi faqat <i>p</i> = 3, <i>n</i> = 2. Har bir maʼlumot shu yechimga mos — har biri yolgʻiz yetarli.</p><p><b>E</b> — «bitta tenglama, ikki nomaʼlum» deb butunlik cheklovini eʼtiborsiz qoldirgan javob.</p>")}

{ds_trap("E", "Chiptalar, ruchkalar, odamlar — butun son. Butun yechimlarni sanab chiqing: ular koʻpincha yagona.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>C yoki E ni belgilashdan oldin <b>uchta tekshiruv</b>:</p>
  <ol>
    <li>maʼlumotlardan biri boshqasini oʻz ichiga olmaydimi (C tuzogʻi)?</li>
    <li>ikki tenglama mustaqilmi yoki biri ikkinchisining nusxasimi?</li>
    <li>savolda butunlik yoki musbatlik cheklovi yashiringanmi?</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Birga albatta ishlaydi → C</p>
  <p class="pe-good">Avval har birini alohida, keyin birga</p>
  <p class="pe-fix__why">C faqat ikkalasi ham yolgʻiz yetmagandagina.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">3<i>p</i> + 5<i>n</i> = 19 — ikki nomaʼlum → yetarli emas</p>
  <p class="pe-good">Butun yechimlarni sanash → yagona</p>
  <p class="pe-fix__why">Sanaladigan miqdorlar butun son — bu kuchli cheklov.</p>
</div>

<h3>Mashq</h3>

{ds_quiz(1, "What is <i>x</i>?", "<i>x</i> + <i>y</i> = 5 and <i>y</i> = 1", "<i>y</i> = 1", "A", "(1) oʻzi <i>y</i> ni beradi.")}

{ds_quiz(2, "If <i>n</i> is a positive integer, what is <i>n</i>?", "<i>n</i><sup>2</sup> &lt; 10", "<i>n</i> &gt; 2", "C", "(1) — 1, 2, 3; birga 3.")}

{ds_quiz(3, "Is <i>x</i><sup>2</sup> &gt; <i>x</i>?", "<i>x</i> &gt; 1", "|<i>x</i>| &gt; 2", "D", "(2): <i>x</i> &gt; 2 yoki <i>x</i> &lt; −2 — ikkalasida ham «ha».")}

{ds_quiz(4, "What is the price of one pen?", "2 pens and a notebook cost $8.", "4 pens and 2 notebooks cost $16.", "E", "(2) — (1) ning ikki baravari.")}

{ds_quiz(5, "A shop sold eggs in boxes of 6 and boxes of 10, 46 eggs in all. How many boxes of 10 did it sell?",
 "It sold at least one box of each size.", "It sold 5 boxes in all.", "B", "Butun yechimlar: (6 ta, 1 ta) va (1 ta, 4 ta); (2) faqat ikkinchisiga mos.")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>trap</b><span>tuzoq</span></li>
  <li><b>hidden constraint</b><span>yashirin cheklov</span></li>
  <li><b>integer</b><span>butun son</span></li>
  <li><b>redundant</b><span>ortiqcha, takroriy</span></li>
  <li><b>independent</b><span>mustaqil</span></li>
  <li><b>at least</b><span>kamida</span></li>
  <li><b>exactly</b><span>aynan</span></li>
  <li><b>combination of</b><span>… ning birikmasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Birga «oson ishlasa» — har birini yana alohida tekshiring (C tuzogʻi).</li>
    <li>Nusxa tenglama yangi maʼlumot emas — E boʻlishi mumkin.</li>
    <li>Sanaladigan narsalar — musbat butun son; butun yechimlarni sanang.</li>
    <li>Savolning oʻzi javobni berishi mumkin — u holda har bir maʼlumot yetarli.</li>
    <li>C yoki E dan oldin uchta tekshiruv.</li>
  </ul>
</div>
"""

# ═════════════════════════════════════════════════════════════════════════
GMAT30 = f"""
<h2>GMAT-30: Data Sufficiency — Word Problems</h2>

<p>Data Sufficiency'ning eng biznesga yaqin turi — matnli masalalar: foiz oʻzgarishi, aralashma,
tezlik, toʻplamlar, foiz daromadi. Quant'dagi barcha bilim shu yerda qayta ishlaydi, bitta
farq bilan: masalani yechmaysiz, <mark>yechish uchun nima kerakligini</mark> aniqlaysiz. Shuning
uchun eng kuchli qurol — maʼlumotlarni oʻqishdan <b>oldin</b> «menga nima kerak?» deb soʻrash.</p>

<div class="pe-goal">
  <p class="pe-goal__title">Bu darsdan keyin siz</p>
  <ul>
    <li>maʼlumotlarni oʻqishdan oldin kerakli nomaʼlumlar roʻyxatini tuzasiz;</li>
    <li>foiz oʻzgarishida baza kerak emasligini koʻrasiz;</li>
    <li>toʻplam, tezlik va aralashma formulalarini DS ichida ishlatasiz;</li>
    <li>«foiz» va «son» farqini maʼlumotlarda tanib olasiz.</li>
  </ul>
</div>

<h3>Avval «menga nima kerak?»</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">Of 50 employees, how many speak both English and Korean?</span>
    <span class="pm-solve__why">Formula: jami = A + B − ikkalasi + hech biri</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">Kerak: A, B va «hech biri» (jami maʼlum)</span>
    <span class="pm-solve__why">Uchta nomaʼlum — oldindan bildik</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(1) 30 English, 25 Korean (2) 5 neither → birga <b>C</b></span>
    <span class="pm-solve__why">Har biri yolgʻiz roʻyxatning bir qismini beradi</span>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kerakli roʻyxatni yozib olsangiz, har bir maʼlumot uchun savol oddiylashadi: «bu roʻyxatni
  toʻldiradimi?». Bu usul ayniqsa uzun, koʻp sonli biznes matnlarida vaqt tejaydi — matndagi
  ortiqcha sonlar sizni chalgʻitmaydi.
</div>

<h3>Foiz oʻzgarishi — baza kerak emas</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">By what percent did revenue change? (1) price +10%, units sold −10%</span>
    <span class="pm-solve__why">Tushum = narx × soni</span>
  </div>
  <div class="pm-solve__row">
    <span class="pm-solve__step">1.1 × 0.9 = 0.99 → 1% kamaygan</span>
    <span class="pm-solve__why">Haqiqiy narx va son kerak emas</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">(1) yetarli; (2) «oʻtgan yil tushumi $50,000» — yetarli emas → <b>A</b></span>
    <span class="pm-solve__why">Bitta yil tushumi oʻzgarishni bermaydi</span>
  </div>
</div>

<h3>Tezlik va ish</h3>

<div class="pm-solve">
  <div class="pm-solve__row">
    <span class="pm-solve__step">How long do A and B take together? (1) A alone 6 h (2) B alone 3 h</span>
    <span class="pm-solve__why">Kerak: ikkala unum</span>
  </div>
  <div class="pm-solve__row pm-solve__row--ans">
    <span class="pm-solve__step">Har biri yolgʻiz — bitta unum; birga 1/6 + 1/3 → <b>C</b></span>
    <span class="pm-solve__why">Javobni (2 soat) hisoblash shart emas</span>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Oʻqituvchi maslahati</span>
  Foiz va nisbat savollarida bitta oʻzgarmas qoida: <b>«qancha foiz?»</b> soʻralsa, haqiqiy sonlar
  koʻpincha kerak emas; <b>«qancha dollar / nechta?»</b> soʻralsa, kamida bitta haqiqiy son
  (jami, baza yoki farq) kerak.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Biznes matnlarida «20 ga oshdi» va «20% ga oshdi» — butunlay boshqa maʼlumot. Birinchisi
  haqiqiy son beradi, ikkinchisi faqat nisbat. Maʼlumotlarni oʻqiganda har bir sonning
  yonidagi soʻzga qarang: «units», «percent», «times».
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  «Oʻrtacha» (<i>mean</i>) va «mediana» DS'da ayniqsa koʻp adashtiriladi. Oʻrtacha yigʻindini
  beradi, lekin qiymatlarning oʻrnini bermaydi — shuning uchun oʻrtachadan medianani topib
  boʻlmaydi. Aksincha, eng kichik uchta qiymat maʼlum boʻlsa, besh sonli toʻplamning medianasi
  darrov maʼlum: bu uchinchisi.
</div>

<h3>Exam English — savol qanday soʻraydi</h3>

<ul class="ps-phrase">
  <li><b>by what percent did … change</b><span>necha foizga oʻzgardi — baza kerak emas</span></li>
  <li><b>how many … in all</b><span>jami nechta — haqiqiy son kerak</span></li>
  <li><b>working together</b><span>birgalikda — unumlar qoʻshiladi</span></li>
  <li><b>compounded annually</b><span>har yili kapitallashtiriladi</span></li>
  <li><b>marked up / discounted</b><span>ustama / chegirma</span></li>
</ul>

<h3>GMAT savollari</h3>

{ds_stem("60 s", "By what percent did a store's revenue from a certain product change from 2024 to 2025?", "From 2024 to 2025 the product's price rose by 10% and the number of units sold fell by 10%.", "The store's revenue from the product in 2024 was $50,000.", "A",
 "<p>(1): 1.1 × 0.9 = 0.99 — 1% kamaydi, yetarli. (2): bitta yilning tushumi — oʻzgarishni bermaydi.</p><p><b>C</b> — foiz oʻzgarishini topish uchun haqiqiy summa kerak deb oʻylagan javob.</p>")}

{ds_trap("C", "Foiz oʻzgarishi nisbat — u bazaga bogʻliq emas. (1) oʻzi koʻpaytuvchini beradi.")}

{ds_stem("60 s", "Of the 50 employees at a firm, how many speak both English and Korean?", "30 of the employees speak English and 25 speak Korean.", "5 of the employees speak neither English nor Korean.", "C",
 "<p>(1): «hech biri» nomaʼlum — kesishma 5 dan 25 gacha boʻlishi mumkin. (2): A va B nomaʼlum. Birga: 30 + 25 + 5 − 50 = 10.</p><p><b>E</b> — formulani eslay olmagan yoki «hech biri» ni hisobga olmagan javob.</p>")}

{ds_trap("E", "Toʻplam formulasi: jami = A + B − ikkalasi + hech biri. Toʻrttasidan uchtasi maʼlum boʻlsa — toʻrtinchisi topiladi.")}

<div class="ps-tactic">
  <span class="ps-tactic__t">Test-day taktikasi</span>
  <p>Matnli DS savolida <b>uch qadam</b>:</p>
  <ol>
    <li>savoldan formulani tanlang (toʻplam, tezlik, foiz, aralashma);</li>
    <li>formulada nima nomaʼlum — roʻyxat qiling;</li>
    <li>har bir maʼlumot roʻyxatni toʻldiradimi — shuni tekshiring.</li>
  </ol>
</div>

<div class="pe-fix">
  <p class="pe-bad">Percent change asked → need the actual revenue</p>
  <p class="pe-good">Percent change asked → the multipliers are enough</p>
  <p class="pe-fix__why">Foiz oʻzgarishi — nisbat; baza qisqarib ketadi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad">«Ikkala unum ham bor» → hisoblashni boshlash</p>
  <p class="pe-good">«Ikkala unum ham bor» → yetarli, keyingi savolga</p>
  <p class="pe-fix__why">Javobni topish — vaqt isrofi; yetarlilik soʻralgan.</p>
</div>

<h3>Mashq</h3>

{ds_quiz(1, "What was the price of a jacket before a discount?", "The discount was 20%.", "The discount was $16.", "C", "Birga: 0.2 × narx = 16 → $80.")}

{ds_quiz(2, "How many units must a company sell to break even?", "Its fixed costs are $9,000, and each unit sells for $18 more than it costs to make.", "Each unit sells for $30.", "A", "(1): 9,000 ÷ 18 = 500.")}

{ds_quiz(3, "What was a van's average speed for a whole trip?", "It drove 120 km in 2 hours and then 180 km in 3 hours.", "The trip covered 300 km in 5 hours in total.", "D", "Ikkalasi ham 300 ÷ 5 beradi.")}

{ds_quiz(4, "How much interest does a deposit earn in 2 years at 10% compounded annually?", "The deposit is $10,000.", "After 1 year the balance is $11,000.", "D", "(2) dan deposit 11,000 ÷ 1.1 = 10,000.")}

{ds_quiz(5, "Did a store make a profit on a lamp?", "The lamp's price was marked up 50% above its cost.", "The lamp was sold at 40% off its marked price.", "C", "Birga: 1.5 × 0.6 = 0.9 — aniq «yoʻq».")}

<h3>Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>word problem</b><span>matnli masala</span></li>
  <li><b>percent change</b><span>foiz oʻzgarishi</span></li>
  <li><b>base</b><span>baza</span></li>
  <li><b>rate</b><span>tezlik, unum</span></li>
  <li><b>overlapping sets</b><span>kesishuvchi toʻplamlar</span></li>
  <li><b>break even</b><span>zararsiz ishlamoq</span></li>
  <li><b>deposit</b><span>omonat</span></li>
  <li><b>what you need</b><span>nima kerak</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">Esda qoldiring</p>
  <ul>
    <li>Maʼlumotlarni oʻqishdan oldin formulani tanlang va nomaʼlumlarni yozing.</li>
    <li>Foiz soʻralsa — koʻpaytuvchilar yetarli; son soʻralsa — haqiqiy son kerak.</li>
    <li>Toʻplam: jami = A + B − ikkalasi + hech biri.</li>
    <li>Ish: ikkala unum kerak; tezlik: umumiy masofa va umumiy vaqt.</li>
    <li>Yetarli ekanini bilsangiz — hisoblamang, keyingi savolga oʻting.</li>
  </ul>
</div>
"""

TUTORIALS = [
    {
        "title": "GMAT-26: The Data Insights Section and Data Sufficiency",
        "category": "math", "order": 26,
        "summary": "Data Insights boʻlimi (20 savol, 45 daqiqa, kalkulyator), Data Sufficiency'ning beshta oʻzgarmas javobi va AD / BCE usuli.",
        "stories": ["Enough to Decide"],
        "content": GMAT26,
    },
    {
        "title": "GMAT-27: Data Sufficiency — Value Questions",
        "category": "math", "order": 27,
        "summary": "Qiymat savolida yetarlilik — yagona qiymat: mustaqil tenglamalar, soʻralgan ifoda, kvadrat va modul, savoldagi cheklovlar.",
        "stories": ["One Number or Two?"],
        "content": GMAT27,
    },
    {
        "title": "GMAT-28: Data Sufficiency — Yes/No Questions",
        "category": "math", "order": 28,
        "summary": "Ha/yoʻq savolida yetarlilik: har doim «ha» yoki har doim «yoʻq», aniq «yoʻq» ham yetarli, son tanlab maʼlumotni buzish.",
        "stories": ["A Definite No"],
        "content": GMAT28,
    },
    {
        "title": "GMAT-29: Data Sufficiency — Traps and Hidden Constraints",
        "category": "math", "order": 29,
        "summary": "C tuzogʻi, bir maʼlumotning ikki koʻrinishi, butunlik va musbatlik kabi yashirin cheklovlar.",
        "stories": ["The Second Report Said Nothing New"],
        "content": GMAT29,
    },
    {
        "title": "GMAT-30: Data Sufficiency — Word Problems",
        "category": "math", "order": 30,
        "summary": "Matnli DS masalalari: avval kerakli nomaʼlumlar roʻyxati, foiz oʻzgarishida baza kerak emas, toʻplam, tezlik va foiz daromadi.",
        "stories": ["What the Board Needed to Know"],
        "content": GMAT30,
    },
]
