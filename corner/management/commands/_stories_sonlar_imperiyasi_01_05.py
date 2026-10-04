# -*- coding: utf-8 -*-
"""Sonlar imperiyasi — 1-5-qismlar (1-mavsum).

Bible: flowstudio/series/sonlar_imperiyasi.md   Toc: toc_sonlar_imperiyasi.txt
Based on the user's own tale `Zero gravity.docx`. Fairy tale + comedy, every scene
mathematically true; each episode ends on a hook and a «Haqiqatda» box.
⛔ AUDIO YOʻQ (maths shelf).

FAKTLAR (tekshirilgan):
  • Brahmagupta, «Brahmasphutasiddhanta», 628-yil: nol bilan amallar qoidalari;
    musbatni «mulk», manfiyni «qarz» deb atagan; 0 ÷ 0 = 0 deb yozgan (xato).
  • Xitoy, «Toʻqqiz bob»: hisob choʻplari — qizil musbat, qora manfiy.
  • Al-Xorazmiy, taxminan 820-yil, Bagʻdod; hind raqamlari va nol haqidagi kitobi
    (manba: _stories_matematika_olami_01_03.py).
  • + va − belgilari birinchi marta 1489-yilda bosilgan kitobda (Yohannes Vidman).
    × — 1631-yil (Uilyam Otred), ÷ — 1659-yil (Yohann Ran).
  • Bxaskara II (XII asr): sonni nolga boʻlish «cheksiz» deb yozgan — bugun:
    aniqlanmagan.
  • Son oʻqi chizmasi: Jon Uollis, 1685-yil.
  • 0 juft son: 0 = 2 × 0, qoldiqsiz boʻlinadi.

    python manage.py import_corner \\
        corner/management/commands/_stories_sonlar_imperiyasi_01_05.py --author=prime
"""

SUBJECT = {
    "name":    "Matematika",
    "summary": "Matematika: hayotdagi matnlar, atamalar va matematik hikoyalar.",
    "icon":    "bi-calculator",
    "color":   "#f59e0b",
    "order":   7,
}

COLLECTION = {
    "title":       "Sonlar imperiyasi",
    "description": (
        "Qirol Noʻl, egizak Birlar va butun sonlar saltanati haqida kulgili ertak-serial. "
        "Har qismda yangi turdagi son tugʻiladi — chunki eskilari nimanidir uddalay "
        "olmaydi. Ertak — lekin har bir sahna matematik jihatdan toʻgʻri."
    ),
    "order": 2,
}


# ── tiny inline-SVG helpers (pm-* classes, like the tutorials) ─────────────
def _fig(svg, caption):
    return f'<figure class="pm-fig">{svg}<figcaption>{caption}</figcaption></figure>'


def _line(lo, hi, marks, width=340, hl=None, extra=''):
    """A number line from lo to hi; `marks` = [(value, label)]; `hl` = highlighted values."""
    pad = 24
    span = hi - lo

    def x(v):
        return pad + (v - lo) * (width - 2 * pad) / span

    parts = [f'<path d="M{pad - 10} 40 L{width - pad + 10} 40" class="pm-ln"/>']
    for v, lab in marks:
        cls = 'pm-ln pm-ln--hl' if hl and v in hl else 'pm-ln'
        parts.append(f'<path d="M{x(v):.1f} 32 L{x(v):.1f} 48" class="{cls}"/>')
        parts.append(f'<text x="{x(v):.1f}" y="68" text-anchor="middle" class="pm-lbl">{lab}</text>')
    return (f'<svg viewBox="0 0 {width} 84" role="img" xmlns="http://www.w3.org/2000/svg">'
            + ''.join(parts) + extra + '</svg>')


def _haqiqatda(*paras):
    body = ''.join(f'<p>{p}</p>' for p in paras)
    return f'<div class="pe-call pe-tip"><span class="pe-call__t">Haqiqatda</span>{body}</div>'


def _keyingi(text):
    return f'<p><em>Keyingi qismda: {text}</em></p>'


STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # 1 — Noʻl va egizak Birlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "1-qism. Noʻl va egizak Birlar",
        "summary": (
            "Zerikkan Qirol Noʻl ikkita egizak Bir yasaydi — biri musbat, biri manfiy. "
            "Ular birinchi marta quchoqlashganda, saroyda vahima boshlanadi."
        ),
        "order":   1,
        "grammar": [
            {
                "pattern":  "Qarama-qarshi sonlar",
                "meaning":  "Noldan bir xil uzoqlikda, lekin teskari tomonda turgan sonlar. "
                            "Ularning yigʻindisi doim 0 ga teng.",
                "examples": ["1 + (−1) = 0", "7 + (−7) = 0", "−1 — bu 1 ning qarama-qarshisi"],
            },
        ],
        "questions": [
            {
                "text": "Birjon (+1) va Minusjon (−1) quchoqlashganda nima qoladi?",
                "choices": ["Ikki", "Noʻl", "Bir", "Minus ikki"],
                "answer": 1,
                "explanation": "Qarama-qarshi sonlar qoʻshilsa, bir-birini yoʻq qiladi: "
                               "1 + (−1) = 0. Shuning uchun tekislikda faqat Qirol Noʻl "
                               "qoladi.",
            },
            {
                "text": "Qirol nima uchun Minusjonga «sen salbiy emas, manfiysan» deydi?",
                "choices": [
                    "Chunki Minusjon yomon son",
                    "Chunki Minusjon Birjondan kichikroq yasalgan",
                    "Chunki u Birjonning teskarisi: noldan xuddi shuncha uzoqda, lekin "
                    "boshqa tomonda",
                    "Chunki u Oyda yashaydi",
                ],
                "answer": 2,
                "explanation": "Manfiy — «yomon» degani emas. −1 noldan 1 qadam uzoqda, "
                               "xuddi +1 kabi; faqat yoʻnalishi teskari.",
            },
            {
                "text": "Saroyga uchta Birjon va bitta Minusjon kirdi. Hammasi quchoqlashsa, "
                        "kim qoladi?",
                "choices": ["Ikkita Birjon", "Hech kim", "Bitta Birjon", "Ikkita Minusjon"],
                "answer": 0,
                "explanation": "1 + 1 + 1 + (−1) = 2. Bitta juftlik yoʻqoladi, ikkita Birjon "
                               "qoladi.",
            },
        ],
        "open_question": (
            "Hayotda qayerda «uchrashsa, bir-birini yoʻq qiladigan» juftlarni koʻrgansiz? "
            "Masalan, qarz va uni toʻlagan pul. Yana nimalar?"
        ),
        "body": """
<p>Bu hikoyani bilgan odam hech qachon <strong>noʻlga oʻtirib qolmas</strong> ekan.</p>

<p>Qadim-qadim zamonda, hali birorta ham son yoʻq paytda, cheksiz oltin tekislikning qoq
oʻrtasida <b>Qirol Noʻl</b> yashagan ekan. Yumaloq, oltindek yaltiroq, boshida chapga
biroz qiyshaygan kichkina toj. U adolatli va bosiq edi: doim oʻrtada turib, hamma narsani
kuzatardi. Bitta muammosi bor edi — kuzatadigan hech narsa yoʻq edi.</p>

<p>— Men hech narsa emasman, — derdi u har tong koʻzguga qarab. — Lekin mensiz hech
narsa boʻlmaydi!</p>

<p>Koʻzguda esa yana oʻsha hech narsa.</p>

<p>Zerikkan qirol osmonga nom beribdi. Oʻng tomondagi Quyoshni
<span class="cn-word" data-tr="noldan katta, oʻng tomondagi">musbat</span>, chap tomondagi
Oyni <span class="cn-word" data-tr="noldan kichik, chap tomondagi">manfiy</span> deb
atabdi. Keyin bir kuni ermak uchun bitta son yasabdi: ingichka, tik, quyoshdek oltin.
Nima deyishni bilmay, «Bir» debdi. Quyosh suyunib ketibdi: «Meniki!» Qirol Birning
koʻkragiga kichkina «+» nishon taqibdi. Uni hamma <b>Birjon</b> deb chaqira
boshlabdi.</p>

<p>Oy hasad qilibdi: «Menga ham!» Qirol ikkinchi Birni yasabdi — xuddi oʻshanday,
faqat kumushrang. Endi ikkovini hech kim ajrata olmas edi. Shunda qirol ikkinchisining
beliga yotiq kamar bogʻlabdi — «−» <span class="cn-word" data-tr="sonning yoʻnalishini koʻrsatuvchi belgi: + yoki −">ishora</span>si:</p>

<p>— Buni umrbod taqib yurasan.</p>

<p>— Nega menga minus? — qovogʻini solibdi ukasi. — Men salbiymanmi?</p>

<p>— Yoʻq, oʻgʻlim. Sen salbiy emassan. Sen <em>manfiysan</em> — yaʼni akangning
teskarisi.</p>

<p>— Salbiy emas, manfiy, — deb takrorlabdi <b>Minusjon</b>. Bu gap keyinchalik butun
saltanatga mashhur boʻldi.</p>

<p>Qirol ularni ikki yoniga qoʻyibdi: Birjonni oʻngga, bir qadam narida; Minusjonni
chapga, xuddi shuncha masofada.</p>

""" + _fig(_line(-2, 2, [(-1, '−1'), (0, '0'), (1, '+1')], hl=[0]),
           'Birjon oʻngda, Minusjon chapda — ikkalasi Qirol Noʻldan bir qadam uzoqda.') + """

<p>— Ikkalangiz menga bir xil yaqinsiz, — debdi u. — Faqat yoʻnalishlaringiz teskari.</p>

<p>Egizaklar bir-birini birinchi marta koʻrib, xursand boʻlib quchoqlashibdi —
<strong>puf!</strong> — ikkalasi ham gʻoyib boʻlibdi. Tekislikda yana yolgʻiz Qirol Noʻl.
Oy hushidan ketibdi. Qirol saroy boʻylab yugurib: «Qayerdasizlar?!» Egizaklar quchogʻini
boʻshatgan zahoti — yana paydo boʻlishibdi, qiqir-qiqir kulishib.</p>

<p>Qirol peshonasidagi terni artib, tushunibdi: Bir bilan minus Bir qoʻshilsa, yana uning
oʻzi — noʻl qolar ekan. <strong>1 + (−1) = 0.</strong> Ular
<span class="cn-word" data-tr="noldan bir xil uzoq, lekin teskari tomondagi sonlar">qarama-qarshi sonlar</span>
edi.</p>

<p>— Quchoqlashmanglar! — deb baqiribdi Oy. — Har safar yoʻq boʻlib qolasizlar!</p>

<p>Bu gap saroyda eng koʻp takrorlanadigan gapga aylanibdi.</p>

<p>Kunlar oʻtibdi. Bir kuni egizaklar qirol xazinasidan eski sandiq topishibdi. Ichida
gʻalati oʻyinchoqlar bor edi: ikki tayoqchadan yasalgan «+», bitta tayoqchali «−»… va
sandiq tagida yana nimadir yaltirab turardi.</p>

""" + _haqiqatda(
            "Odamlar uzoq vaqt nolni son deb hisoblamagan. Hind matematigi "
            "<b>Brahmagupta</b> 628-yilda nol bilan hisoblash qoidalarini yozib qoldirgan: songa "
            "nol qoʻshilsa, son oʻzgarmaydi; sondan oʻzini ayirsa, nol chiqadi. U musbat sonlarni "
            "«mulk», manfiylarni «qarz» deb atagan.",
            "Qadimgi Xitoyda hisob choʻplari bilan ishlashgan: <b>qizil</b> choʻp — musbat, "
            "<b>qora</b> choʻp — manfiy son.",
            "Hind raqamlari va nolni Gʻarbga yetkazganlardan biri — vatandoshimiz "
            "<b>al-Xorazmiy</b> (taxminan 820-yil, Bagʻdod).",
        ) + _keyingi("egizaklar oʻyinchoqlar bilan oʻynab, sonlarni koʻpaytirishni kashf "
                     "qiladi — va Qirol Noʻl oʻzining qoʻrqinchli kuchini bilib oladi."),
    },

    # ══════════════════════════════════════════════════════════════════
    # 2 — Ishoralar oʻyini
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "2-qism. Ishoralar oʻyini",
        "summary": (
            "Egizaklar sandiqdagi oʻyinchoqlardan koʻpaytirishni kashf qiladi. Qirol Noʻl "
            "esa oʻzining qoʻrqinchli kuchini bilib oladi: kimni koʻpaytirsa, oʻsha yoʻqoladi."
        ),
        "order":   2,
        "grammar": [
            {
                "pattern":  "Nolning ikki qoidasi",
                "meaning":  "Songa nol qoʻshilsa, son oʻzgarmaydi. Son nolga koʻpaytirilsa, "
                            "natija doim nol.",
                "examples": ["5 + 0 = 5", "5 × 0 = 0", "1 000 000 × 0 = 0"],
            },
        ],
        "questions": [
            {
                "text": "Qirol Noʻl nima uchun «qoʻshilaman — hech kim sezmaydi» deydi?",
                "choices": [
                    "Chunki u juda kichkina",
                    "Chunki songa nol qoʻshilsa, son oʻzgarmaydi",
                    "Chunki u koʻrinmas",
                    "Chunki qoʻshish taqiqlangan",
                ],
                "answer": 1,
                "explanation": "a + 0 = a. Masalan, 5 + 0 = 5 — besh beshligicha qoladi.",
            },
            {
                "text": "Saroyda 3 ta Birjon bor. Ular bitta qatorga turdi, keyin yana xuddi "
                        "shunday 4 ta qator tuzildi. Jami nechta Birjon? Qirol bu safar "
                        "4 qatorni emas, 0 qatorni buyursa-chi?",
                "choices": ["12 va 0", "7 va 3", "12 va 3", "7 va 0"],
                "answer": 0,
                "explanation": "Koʻpaytirish — bir xil sonni qayta-qayta qoʻshish: 3 × 4 = "
                               "3 + 3 + 3 + 3 = 12. Nol qator esa — hech kim yoʻq: 3 × 0 = 0.",
            },
        ],
        "open_question": (
            "Nol qoʻshish hech narsani oʻzgartirmaydi, nolga koʻpaytirish esa hammasini "
            "yoʻq qiladi. Bir ham shunday ikki xil «xarakter»ga egami? 5 + 1 va 5 × 1 ni "
            "solishtirib koʻring."
        ),
        "body": """
<p>Sandiqni ochgan egizaklar birinchi boʻlib «+» oʻyinchoqni olishibdi. Birjon uni
oʻzining yoniga qoʻygan edi — yonida yana bitta Birjon paydo boʻlibdi! <strong>1 + 1 = 2.</strong></p>

<p>— Zoʻr-ku! — qichqiribdi Birjon. — Yana bitta qoʻshamiz!</p>

<p>Shu tariqa ular <span class="cn-word" data-tr="sonlarni birlashtirish amali">qoʻshish</span>ni
kashf qilishibdi. «−» oʻyinchoq esa aksincha ishlar ekan: kimni bossang, oʻsha bitta
kamayadi. Bu <span class="cn-word" data-tr="bir sondan boshqasini olib tashlash amali">ayirish</span> edi.
Minusjon «−»ni juda yoqtirib qolibdi, lekin hech kimga bermas, belidan ham yechmas
edi.</p>

<p>Bir kuni Birjon «+»ni yonboshiga yotqizib, qiyshaytirib koʻribdi. Oʻyinchoq «×»ga
aylanibdi. Uni kimga tekkizsa — oʻsha birdaniga bir necha marta koʻpayib ketar ekan:
uchta Birjonga «× 4» tekkizsa, saroy oʻn ikkita Birjonga toʻlib ketibdi. Bu
<span class="cn-word" data-tr="bir xil sonni bir necha marta qoʻshishning qisqa yoʻli">koʻpaytirish</span>
edi: <strong>3 × 4 = 3 + 3 + 3 + 3 = 12</strong>.</p>

<p>Egizaklarning shovqinini eshitib, Qirol Noʻl ham oʻyinga qoʻshilibdi. Avval «+»ni
oʻzi bilan sinab koʻribdi: beshlikka qoʻshilibdi. Besh — besh boʻlib qolaveribdi.
Yettiga qoʻshilibdi — yetti hatto sezmabdi ham.</p>

<p>— Qoʻshilaman — hech kim sezmaydi, — xoʻrsinibdi qirol. <strong>5 + 0 = 5.</strong></p>

<p>Keyin «×»ni olibdi. Beshlikni koʻpaytiribdi — <strong>puf!</strong> — besh gʻoyib
boʻlibdi, oʻrnida faqat Noʻl. Yettini koʻpaytiribdi — puf! Mingni — puf!</p>

<p>— Voy, kechirasiz… — debdi qirol har safar. — Yana koʻpaytirib qoʻydim-a.</p>

<p>Saroydagilar qirol «×» oʻyinchoqni qoʻliga olganini koʻrishi bilan har tomonga
qochishar ekan. Chunki <strong>har qanday son × 0 = 0</strong>. Nolni beshta qator qilib
tursang ham — hech kim yoʻq. Besh kishini nol marta saflasang ham — hech kim yoʻq.</p>

<p>— Qoʻshilaman — hech kim sezmaydi. Koʻpaytiraman — hamma yoʻqoladi, — debdi qirol
kechqurun Oyga. — Bu qanaqa hayot?!</p>

<p>Oy uni yupatibdi: «Sen hech kimni yomonlik bilan yoʻq qilmaysan. Senda shunday
<span class="cn-word" data-tr="amalning doim bajariladigan xossasi">qoida</span> bor, xolos.»</p>

<p>Oʻsha kechasi qirol charchab, tekislikning qoq oʻrtasida uxlab qolibdi. Egizaklar esa
hali uxlamagan edi. Ular «−» oʻyinchoq ustida sakrab oʻynashardi — sakrashdi, sakrashdi,
toki undan ikkita nuqta otilib chiqib, biri tepasiga, biri pastiga yopishib qolguncha.
Oʻyinchoq «÷»ga aylandi.</p>

<p>Egizaklar bir-biriga qarashdi. Keyin uxlab yotgan qirolga qarashdi.</p>

""" + _haqiqatda(
            "Ertakda belgilar egizaklarning oʻyinidan tugʻiladi — bu <b>rivoyat</b>. Aslida "
            "belgilar ancha yosh: «+» va «−» birinchi marta 1489-yilda Germaniyada bosilgan "
            "kitobda uchraydi (Yohannes Vidman), «×» — 1631-yilda (Uilyam Otred), «÷» esa "
            "1659-yilda (Yohann Ran). Undan oldin hisoblar soʻz bilan yozilgan.",
            "Nolning ikki qoidasi esa qadimiy va oʻzgarmas: <b>a + 0 = a</b> va "
            "<b>a × 0 = 0</b>.",
        ) + _keyingi("egizaklar «÷» oʻyinchoqni uxlab yotgan qirolning ustiga qoʻyadi. "
                     "Shu kechadan keyin saltanatda birinchi qonun paydo boʻladi."),
    },

    # ══════════════════════════════════════════════════════════════════
    # 3 — Nolga boʻlish
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "3-qism. Nolga boʻlish",
        "summary": (
            "Egizaklar uxlab yotgan qirolni «÷» ostiga qoʻyadi. Qirol Noʻl javob izlab "
            "ufq tomon yuguradi — va saltanatning birinchi qonuni tugʻiladi."
        ),
        "order":   3,
        "grammar": [
            {
                "pattern":  "Nolga boʻlib boʻlmaydi",
                "meaning":  "Boʻluvchi nolga yaqinlashgan sari natija cheksiz katta boʻlib "
                            "ketadi: musbat tomondan juda katta musbat, manfiy tomondan juda "
                            "katta manfiy. Bitta javob yoʻq — shuning uchun 1 ÷ 0 aniqlanmagan.",
                "examples": ["1 ÷ 0,1 = 10", "1 ÷ 0,001 = 1000", "1 ÷ (−0,001) = −1000"],
            },
        ],
        "questions": [
            {
                "text": "1 ÷ 0,01 nechaga teng?",
                "choices": ["0,01", "1", "100", "10"],
                "answer": 2,
                "explanation": "0,01 — yuzdan bir. Bitta butunda yuzta yuzdan bir bor: "
                               "1 ÷ 0,01 = 100.",
            },
            {
                "text": "Nima uchun qirol nolga boʻlishni taqiqladi?",
                "choices": [
                    "Chunki javob doim 0 chiqadi",
                    "Chunki javob doim 1 chiqadi",
                    "Chunki javob — cheksizlik degan son",
                    "Chunki boʻluvchi nolga yaqinlashgan sari natija bir tomondan katta "
                    "musbat, boshqa tomondan katta manfiy boʻlib ketadi — bitta javob yoʻq",
                ],
                "answer": 3,
                "explanation": "Cheksizlik son emas, yoʻnalish. 1 ÷ 0 ning javobi yoʻq — "
                               "u aniqlanmagan.",
            },
            {
                "text": "Qirol 1 ÷ (−0,1) ni hisoblaganda qaysi tomonga yugurdi va qayerga "
                        "yetdi?",
                "choices": ["Oʻngga, 10 ga", "Chapga, −10 ga", "Chapga, −0,1 ga",
                            "Hech qayerga, 0 da qoldi"],
                "answer": 1,
                "explanation": "Musbatni manfiyga boʻlsak, natija manfiy: 1 ÷ (−0,1) = −10. "
                               "Manfiy sonlar chap tomonda.",
            },
        ],
        "open_question": (
            "0 ÷ 5 = 0 — bunda hech qanday muammo yoʻq. 5 ÷ 0 esa taqiqlangan. Nima uchun "
            "nol boʻlinuvchi boʻlsa mumkin, boʻluvchi boʻlsa mumkin emas? Pechenye va "
            "bolalar misolida oʻylab koʻring."
        ),
        "body": """
<p>Egizaklar sekin, oyoq uchida yurib kelishdi va «÷» oʻyinchoqni uxlab yotgan qirolning
<em>ustiga</em> qoʻyishdi. Tepada Birjon, pastda — Qirol Noʻl. <strong>1 ÷ 0.</strong></p>

<p>— Hazratim, — pichirladi Birjon, — meni teng boʻlish uchun nechta siz kerak?</p>

<p>Qirol uygʻonib ketdi. Savol uning qulogʻiga kirdi va <span class="cn-word" data-tr="boʻlish amali">boʻlish</span>
oʻz ishini boshladi. Qirol javob topishga urindi. Avval oʻzini <strong>oʻndan birgacha</strong>
kichraytirdi — bitta Birjonni toʻldirish uchun shunday oʻnta qirol kerak boʻldi:
<strong>1 ÷ 0,1 = 10</strong>. Qirol oʻngga qarab oʻn qadam yugurdi.</p>

<p>«Hali Noʻl emasman-ku», deb yanada kichraydi — <strong>yuzdan birgacha</strong>. Endi
yuzta kerak: <strong>1 ÷ 0,01 = 100</strong>. Yuz qadam! Keyin <strong>mingdan bir</strong>
— ming qadam! Toji uchib ketdi, mantiyasi hilpiradi:</p>

<p>— O-o-on! Yu-u-uz! Mi-i-ing! Million!</p>

<p>U nolga qancha yaqinlashsa, shuncha uzoqqa, shuncha tez yugurar edi. Shu payt
Minusjon ham sakrab, oʻzini qirolning ustiga tashladi: <strong>1 ÷ (−0,001) = −1000</strong>.
Qirol endi teskari tomonga — <strong>chapga</strong> uchib ketdi! Bir oʻngga, bir chapga,
har safar yanada uzoqroqqa.</p>

""" + _fig(
            '<svg viewBox="0 0 340 120" role="img" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M10 60 L330 60" class="pm-ln"/>'
            '<path d="M170 52 L170 68" class="pm-ln pm-ln--hl"/>'
            '<text x="170" y="84" text-anchor="middle" class="pm-lbl">0</text>'
            '<path d="M182 50 Q230 44 250 30 Q275 14 318 8" class="pm-ln pm-ln--hl"/>'
            '<path d="M158 70 Q110 76 90 90 Q65 106 22 112" class="pm-ln pm-ln--hl"/>'
            '<text x="300" y="34" text-anchor="end" class="pm-lbl">10 · 100 · 1000 →</text>'
            '<text x="40" y="44" class="pm-lbl">← −1000 · −100 · −10</text>'
            '</svg>',
            'Boʻluvchi nolga yaqinlashgan sari: oʻng tomondan natija ufqqa qochadi, chap '
            'tomondan — teskari ufqqa. Ular hech qachon uchrashmaydi.') + """

<p>Qirolning boshidan uchqunlar sachrab, uzoq-uzoqlarga, ufqning oʻziga qadar sochilib
ketdi. U yerda — hech kim yetib borolmaydigan joyda — nimadir tugʻildi. Uning ovozi
uzoqdan aks-sado berdi:</p>

<p>— Yetib keldim!</p>

<p>Hamma oʻsha tomonga qaradi. U hali ham ufqda edi.</p>

<p>— …Yoʻq, hali yoʻldaman.</p>

<p>Uni <b><span class="cn-word" data-tr="hech qachon tugamaydigan, cheki yoʻq">Cheksizlik</span></b>
deb atashdi. U son emas edi — u <strong>yoʻnalish</strong> edi: «tobora kattaroq»
degani. Unga yugurish mumkin, yetib borish — hech qachon.</p>

<p>Tong otganda qirol tekislikning oʻrtasiga holsiz qaytib keldi. Toji yoʻq, nafasi
boʻgʻzida. U hamma sonlarni yigʻib, saltanatning <b>birinchi qonunini</b> eʼlon qildi:</p>

<p><strong>— Noʻlga boʻlib boʻlmaydi!</strong> Hech kim, hech qachon meni «÷» ostiga
qoʻymasin. Chunki bu savolning javobi yoʻq: oʻngdan yugursam — cheksiz katta, chapdan
yugursam — cheksiz katta manfiy. Bitta javob yoʻq.</p>

<p>Egizaklar boshlarini egib turishdi. Keyin quchoqlashib, kechirim soʻrashdi — puf! —
yana gʻoyib boʻlishdi.</p>

<p>Qoʻrqib qolgan qirol esa oʻzi bilan ufq oʻrtasiga devor qurishga qaror qildi. Birlar
yordamida u yangi sonlar yasay boshladi: avval <b>Ikki</b>ni, keyin <b>Uch</b>ni… toʻrt,
besh… yuz… ikki yuz. Saltanat gavjum boʻla boshladi. Lekin yangi sonlar Birlardek
itoatkor emas edi.</p>

""" + _haqiqatda(
            "Bu savol buyuk olimlarni ham chalgʻitgan. <b>Brahmagupta</b> (628-yil) 0 ÷ 0 = 0 "
            "deb yozgan — bu xato. XII asrda <b>Bxaskara II</b> sonni nolga boʻlish «cheksiz» "
            "beradi, degan. Bugungi matematikada javob aniq: <b>nolga boʻlish aniqlanmagan</b>. "
            "Sabab — ertakdagi bilan bir xil: boʻluvchi nolga oʻngdan yaqinlashsa, natija "
            "cheksiz katta musbat boʻladi, chapdan yaqinlashsa — cheksiz katta manfiy.",
            "Cheksizlik (∞) — son emas. U «hech qanday son bilan toʻxtamaydi» degan "
            "yoʻnalish.",
        ) + _keyingi("yangi sonlar oʻzaro urishib, kim qayerda turishini talashadi. Qirol "
                     "tayogʻini oladi…"),
    },

    # ══════════════════════════════════════════════════════════════════
    # 4 — Tayoq va saf
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "4-qism. Tayoq va saf",
        "summary": (
            "Yangi sonlar kim qayerda turishini talashadi. Qirol Noʻl tayogʻini yerga "
            "qoʻyadi — va sonlar oʻqi tugʻiladi. Paradda juft va toq askarlar janjallashadi."
        ),
        "order":   4,
        "grammar": [
            {
                "pattern":  "Sonlar oʻqi",
                "meaning":  "Har bir songa bitta joy: kattaroq son oʻngroqda turadi. Noldan "
                            "oʻngda musbatlar, chapda manfiylar. 2 ga qoldiqsiz boʻlinadigan son "
                            "juft, boʻlinmaydigani toq. 0 juft: 0 = 2 × 0.",
                "examples": ["−3 < −1 < 0 < 2 < 5", "juft: …, −2, 0, 2, 4, …",
                             "toq: …, −3, −1, 1, 3, …"],
            },
        ],
        "questions": [
            {
                "text": "Sonlar oʻqida qaysi son chaproqda turadi: −5 mi yoki −2 mi?",
                "choices": ["−2", "Ikkalasi bir joyda", "−5", "Ular oʻqda turmaydi"],
                "answer": 2,
                "explanation": "Sonlar oʻqida kichikroq son chaproqda turadi. −5 noldan "
                               "5 qadam chapda, −2 esa atigi 2 qadam: −5 &lt; −2.",
            },
            {
                "text": "Nol juftmi yoki toq?",
                "choices": [
                    "Juft — 2 ga qoldiqsiz boʻlinadi: 0 ÷ 2 = 0",
                    "Toq — chunki u hech narsa",
                    "Na juft, na toq",
                    "Faqat qirol xohlaganda juft",
                ],
                "answer": 0,
                "explanation": "Juft son — 2 ga qoldiqsiz boʻlinadigan son. 0 = 2 × 0, "
                               "qoldiq yoʻq. Shuning uchun nol juft — bu qirolning "
                               "injiqligi emas, haqiqat.",
            },
        ],
        "open_question": (
            "Paradda juft askarlar «biz koʻpmiz» deb maqtanishdi. 1 dan 100 gacha juft "
            "sonlar koʻpmi yoki toq sonlar? −100 dan 100 gacha-chi (nolni ham hisoblab)?"
        ),
        "body": """
<p>Yangi sonlar koʻpaygan sari saltanatda shovqin ham koʻpaydi. Yetti oltining oldiga
turib olardi, sakkiz esa uchning ustiga chiqib ketardi. Baʼzi musbatlar chap tomonga
oʻtib, manfiylar bilan aralashib ketardi.</p>

<p>— Kim qayerda turishini bilmay qoldim! — dedi qirol va jahl bilan uzun
<span class="cn-word" data-tr="uzun yogʻoch hassa">tayoq</span>ini koʻtardi. Sonlar
qoʻrqib, bir joyga toʻplanishdi.</p>

<p>Ammo qirolning rahmi keldi. U tayoqni urish oʻrniga… yerga yotqizdi. Keyin tayoqqa
teng oraliqlarda chiziqchalar chizdi va farmon chiqardi:</p>

<p><strong>— Har bir chiziqcha — bitta va faqat bitta sonning joyi. Kim katta boʻlsa,
oʻngroqda turadi.</strong></p>

""" + _fig(_line(-4, 4, [(v, ('−' + str(-v)) if v < 0 else str(v)) for v in range(-4, 5)],
                 hl=[0]),
           'Qirolning tayogʻi — sonlar oʻqi. Oʻrtada Noʻl, oʻngda musbatlar, chapda '
           'manfiylar.') + """

<p>Sonlar darhol oʻz joylariga yugurdi. Oʻrtada — Qirol Noʻl. Oʻngda: 1, 2, 3, 4…
Chapda: −1, −2, −3, −4… Shu kundan boshlab tayoq
<span class="cn-word" data-tr="har bir songa bitta nuqta mos keladigan toʻgʻri chiziq">sonlar oʻqi</span>
deb ataldi. Endi kim kattaligini bahslashish shart emas edi: oʻngroqdagi doim katta.
Minusjon hatto kashf qildi: «−5 mendan kichik ekan — u chaproqda!»</p>

<p>Keyin parad boʻldi. Qirol hammani yaxshiroq koʻrish uchun sonlarni ikki safga
ajratdi. Ikkiga qoldiqsiz boʻlinadiganlar —
<span class="cn-word" data-tr="2 ga qoldiqsiz boʻlinadigan son">juft</span> askarlar,
koʻk qalpoqda. Boʻlinmaydiganlar —
<span class="cn-word" data-tr="2 ga boʻlganda 1 qoldiq qoladigan son">toq</span> askarlar,
qizil qalpoqda. Serjant Ikki baqirdi:</p>

<p>— Juft-juft safga turinglar!</p>

<p>Toq askarlar bir-biriga qarashdi:</p>

<p>— Bizda juft yoʻq — biz toqmiz!</p>

<p>Parad tartibsizlikka aylandi. Shunda juft askarlar shikoyat qilishdi: «Qirolning ikki
qanotida — Birjon bilan Minusjon — ikkalasi ham toq. Bu adolatdanmi?»</p>

<p>Qirol oʻylab turdi-da, eʼlon qildi:</p>

<p>— Men ham juftman!</p>

<p>— Kim bilan? — soʻradi kimdir.</p>

<p>— Oʻzim bilan: <strong>0 + 0</strong>! Ikkiga boʻlsam ham — <strong>0 ÷ 2 = 0</strong>,
qoldiq yoʻq.</p>

<p>Juftlar xursand boʻlishdi, toqlar ham koʻndi: qirol baribir oʻrtada, hammaga bir xil
yaqin edi. Ammo bu hali holva edi. Sonlar oʻz joylariga qarab, birin-ketin
norozilanishni boshlashdi:</p>

<p>— Joyimiz tor! Har birimizga atigi bitta chiziqcha. Chiziqchalar orasidagi boʻsh yerlar
kimniki?</p>

""" + _haqiqatda(
            "Sonlarni toʻgʻri chiziqda tasvirlash gʻoyasini birinchilardan boʻlib ingliz "
            "matematigi <b>Jon Uollis</b> 1685-yilda yozgan — atigi 340 yil oldin.",
            "<b>Nol — juft son.</b> Juft son 2 ga qoldiqsiz boʻlinadi, 0 esa 2 × 0 ga teng. "
            "Sonlar oʻqida juft va toq sonlar navbatma-navbat keladi: …, −2, −1, 0, 1, 2, …",
        ) + _keyingi("sonlar chiziqchalar orasidagi boʻsh yerlarni talab qiladi — va bu bozor "
                     "hech qachon yopilmaydi."),
    },

    # ══════════════════════════════════════════════════════════════════
    # 5 — Oraliqdagi yerlar
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "5-qism. Oraliqdagi yerlar",
        "summary": (
            "Sonlar chiziqchalar orasidagi yerni talab qiladi. Qirol Noʻl oraliqni ikkiga, "
            "yana ikkiga boʻladi — va yer hech qachon tugamasligini bilib oladi."
        ),
        "order":   5,
        "grammar": [
            {
                "pattern":  "Oraliq hech qachon tugamaydi",
                "meaning":  "Har qanday ikki son orasida yana bir son bor — masalan, ularning "
                            "oʻrtasi (oʻrta arifmetigi). Uni yana va yana topish mumkin.",
                "examples": ["2 bilan 3 orasida: 2½", "2 bilan 2½ orasida: 2¼",
                             "a va b ning oʻrtasi: (a + b) ÷ 2"],
            },
        ],
        "questions": [
            {
                "text": "2 bilan 2½ ning qoq oʻrtasida qaysi son turadi?",
                "choices": ["2⅓", "2¾", "2¼", "3"],
                "answer": 2,
                "explanation": "(2 + 2½) ÷ 2 = 4½ ÷ 2 = 2¼. Har safar oʻrtasini olsak, yangi "
                               "son topiladi.",
            },
            {
                "text": "Dalloll «yer tugamaydi, aka!» deydi. U nimani nazarda tutyapti?",
                "choices": [
                    "Bozor juda katta",
                    "Har qanday ikki son orasida doim yana bir son topiladi",
                    "Sonlar oʻqi cheksiz uzun",
                    "Sotuvchilar kam",
                ],
                "answer": 1,
                "explanation": "Oraliqni qancha boʻlmang, yana boʻlish mumkin: 2 va 3 orasida "
                               "2½, 2 va 2½ orasida 2¼, va hokazo — cheksiz.",
            },
        ],
        "open_question": (
            "0 va 1 orasida nechta son bor? Qancha son yozsangiz ham, yana bittasini qoʻshish "
            "mumkinmi? Qanday qilib?"
        ),
        "body": """
<p>Ertasi kuni ertalab saroy oldida navbat turardi. Har bir son qoʻlida ariza:</p>

<p>— Hazratim, ikki bilan uch orasidan <strong>bir yarim sotix</strong> bering!</p>

<p>— Menga yetti bilan sakkiz orasidan, daryo boʻyidan!</p>

<p>Qirol Noʻl hayron qoldi: «Chiziqchalar orasida yer bor ekanmi?» U tayoqqa qaradi.
Haqiqatan ham, har ikki chiziqcha orasida boʻsh joy yotardi. U ikki bilan uchning qoq
oʻrtasiga yangi chiziqcha tortdi:</p>

<p>— Bu — <b>ikki butun ikkidan bir</b>. Uning joyi ikkiga ham, uchga ham bir xil yaqin.</p>

""" + _fig(_line(2, 3, [(2, '2'), (2.25, '2¼'), (2.5, '2½'), (2.75, '2¾'), (3, '3')],
                 hl=[2.5]),
           'Ikki bilan uch orasida — 2½. Uning oʻrtalarida — 2¼ va 2¾. Va bu hech qachon '
           'tugamaydi.') + """

<p>Shunday qilib <span class="cn-word" data-tr="butunning teng qismi: ½, ¼, …">kasr</span>
yerlar paydo boʻldi. Lekin navbat tugamas edi. 2½ ning oʻzi ham shikoyat qildi: «Meni
ikki bilan siqib qoʻydingiz!» Qirol ikki bilan 2½ ning oʻrtasini ham topdi — 2¼. Keyin
2¼ bilan 2½ oʻrtasini — 2⅜…</p>

<p>Bozor qizib ketdi. Bir <span class="cn-word" data-tr="bozorda oldi-sotdiga vositachilik qiluvchi">dallol</span>
sonlar orasida yugurib, baqirardi:</p>

<p>— Yer tugamaydi, aka, tugamaydi! Qancha boʻlsangiz ham, oʻrtasi bor!</p>

<p>U haq edi. Qirol tushundi: har qanday ikki son orasida doim yana bir son bor — ularning
<span class="cn-word" data-tr="ikki sonning yigʻindisini 2 ga boʻlish">oʻrtasi</span>.
Uni yana va yana topish mumkin. Oraliqdagi yerlar
<strong>hech qachon tugamaydi</strong>.</p>

<p>Sonlar yerli boʻlib, xursand boʻlishdi. Lekin oradan koʻp oʻtmay, bir guruh son saroy
oldida norozilik bildirdi. Ularning boshida — Ikki va Uch.</p>

<p>— Biz bir narsani payqadik, — dedi Uch. — Egizaklar qachon quchoqlashsa, ular yoʻqoladi,
oʻrnida esa doim <em>siz</em> paydo boʻlasiz. Siz bizdan oʻzingizni abadiy qilish uchun
foydalanyapsiz!</p>

<p>Birjon bilan Minusjon bir-biriga qarashdi. Qirol esa ranjib ketdi:</p>

<p>— Men buni atayin qilmayman. Bu — <strong>1 + (−1) = 0</strong>, bu qoida, mening
hiyla-nayrangim emas. Lekin… agar sizga shunday tuyulgan boʻlsa, kechirasiz.</p>

<p>Va yarashish belgisi sifatida u katta saxiylik qildi: sandiqdagi barcha oʻyinchoqlarni
— «+», «−», «×» va hatto «÷»ni — hamma sonlarga oʻynash uchun berdi. Faqat bitta shart
bilan: hech kim «÷» ostiga nolni qoʻymasin.</p>

<p>Sonlar suyunishdi. Ular hali bilmas edi: «÷» bilan oʻynash ularning dunyoqarashini
butunlay oʻzgartirib yuboradi.</p>

""" + _haqiqatda(
            "Har qanday ikki kasr orasida yana bir kasr bor — masalan, ularning oʻrta "
            "arifmetigi: <b>(a + b) ÷ 2</b>. Shuning uchun 0 bilan 1 orasidagi kasrlar soni "
            "cheksiz. Matematiklar bu xossani <b>zichlik</b> deb atashadi.",
            "Diqqat: bu «sonlar oʻqi kasrlar bilan toʻla» degani emas. Keyingi qismlarda "
            "oʻqda hali ham… teshiklar borligini koʻramiz.",
        ) + _keyingi("sonlar bir-birini «÷» bilan boʻlib koʻradi. Natijalar hech kimga "
                     "oʻxshamaydi — va bitta Uch hech gapirishdan toʻxtamaydi."),
    },
]
