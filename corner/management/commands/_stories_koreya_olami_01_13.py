# -*- coding: utf-8 -*-
"""Koreya olami — 1, 2 va 13-matnlar (birinchi partiya).

Toc: corner/management/commands/toc_koreya_olami.txt
  1.  Bitta boʻgʻin — toʻqqizta soʻz          (til qanday ishlaydi)
  2.  Oʻzbek va koreys: bir xil tartib        (til qanday ishlaydi)
  13. Koreys alifbosi — ogʻzingizning surati  (alifbo va tovush)
⛔ AUDIO YOʻQ (matn oʻzbekcha — toc sarlavhasiga qarang).

Uchalasi ham `storyvideo/` uchun manba: ko01, ko03, ko02.

FAKTLAR (tekshirilgan):
  • 출(出) oilasi — examprep VocabRoot bazasining oʻzidan: 출구·출근·출발·출석·
    제출·수출·외출·출입·지출, jami 9 ta. Bazada TOPIK uchun 51 ta ildiz va
    202 ta soʻz bor.
  • Koreys lugʻatining yarmidan koʻpi 한자어 (xitoycha ildizli). Aniq foiz
    manbaga qarab 57–60% deb keltiriladi, shuning uchun matnda «yarmidan
    koʻpi» deyilgan.
  • Alifbo 1443-yilda tugatilgan, «훈민정음» kitobi esa 1446-yilda chop
    etilgan — bu ikki sana ALOHIDA. Dastlab 28 ta harf boʻlgan, bugun 24 tasi
    ishlatiladi (4 tasi isteʼmoldan chiqqan).
  • Sejong (세종, 1397–1450), taxtda 1418–1450.
  • Harf shakllari haqidagi daʼvo «훈민정음 해례본» (1446) ning oʻzidan:
    ㄱ — til ildizi boʻgʻizni toʻsgan shakl, ㄴ — tilning tanglayga tekkani,
    ㅁ — ogʻiz shakli, ㅅ — tish shakli, ㅇ — boʻgʻiz shakli. Qolgan undoshlar
    shu beshtasiga chiziq qoʻshib yasalgan.
  • «훈민정음 해례본» 1997-yilda YUNESKOning «Jahon xotirasi» roʻyxatiga
    kiritilgan.
  • Talaffuz qavs ichida `storyvideo/korean.py` bergan shaklda yozilgan
    (chulgu, hunminjongum, chonun chegul ilgoyoʻ...), shunda shelf, video va
    ovoz matni bir-biriga zid boʻlmaydi.

    python manage.py import_corner \\
        corner/management/commands/_stories_koreya_olami_01_13.py --author=prime
"""

SUBJECT = {
    "name":    "Korean",
    "summary": "Koreys tili: oʻqish matnlari, lugʻat va til haqidagi hikoyalar.",
    "icon":    "bi-translate",
    "color":   "#6366f1",
    "order":   0,
}

COLLECTION = {
    "title":       "Koreya olami",
    "description": (
        "Koreys tili va Koreya haqida oʻzbekcha matnlar: alifbo qanday "
        "oʻylab topilgan, soʻzlar qanday yasaladi, nega oʻzbek tili koreys "
        "tiliga ingliz tilidan yaqinroq. Darsga bogʻlanmagan — shunchaki "
        "qiziqarli oʻqish uchun."
    ),
    "order": 5,
}

STORIES = [
    # ══════════════════════════════════════════════════════════════════
    # 1 — Bitta boʻgʻin — toʻqqizta soʻz
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Bitta boʻgʻin — toʻqqizta soʻz",
        "summary": (
            "Koreys lugʻatini soʻzma-soʻz yodlash — eng sekin yoʻl. Bitta "
            "boʻgʻin, 출, kamida toʻqqizta soʻzni ochib beradi."
        ),
        "order":   1,
        "open_question":
            "出 — chiqmoq. Unda 入 nima degani? 입구 qanday joy boʻladi?",
        "grammar": [
            {
                "pattern":  "한자어 ildiz oilasi",
                "meaning":  "Koreys lugʻatining yarmidan koʻpi xitoycha "
                            "ildizlardan yasalgan. Bitta ildizning maʼnosini "
                            "bilsangiz, uni oʻz ichiga olgan notanish soʻzni "
                            "ham taxmin qila olasiz. Ildiz soʻzning boshida "
                            "ham, oxirida ham turishi mumkin.",
                "examples": [
                    "출(出) = chiqmoq  →  출구 chiqish joyi, 출발 joʻnash",
                    "출(出) soʻz oxirida  →  수출 eksport, 지출 xarajat",
                    "입(入) = kirmoq  →  입구 kirish joyi, 입학 oʻqishga kirish",
                ],
            },
        ],
        "questions": [
            {
                "text": "Nega 출 boʻgʻini ham 출구, ham 수출 soʻzida uchraydi?",
                "choices": [
                    "Bu tasodif — ikki soʻzning maʼnosi bogʻliq emas",
                    "U ildiz, maʼnosi «chiqmoq», va soʻzning istalgan "
                    "joyida tura oladi",
                    "출 — koreyscha koʻplik qoʻshimchasi",
                    "Bir soʻzda xato yozilgan",
                ],
                "answer": 1,
                "explanation": "출(出) — «chiqmoq» maʼnosidagi ildiz. 출구 = "
                               "chiqish + ogʻiz, 수출 = tashib + chiqarish. "
                               "Ildiz boshda ham, oxirida ham turaveradi.",
            },
            {
                "text": "Matnga koʻra, 출석 soʻzi nimani anglatadi?",
                "choices": ["Xarajat", "Davomat", "Eksport", "Joʻnash"],
                "answer": 1,
                "explanation": "출석(出席) = «chiqish + oʻrindiq», yaʼni "
                               "oʻrningga chiqish — davomat.",
            },
            {
                "text": "Agar 학(學) «oʻqish» degani boʻlsa, 입학 nima "
                        "boʻlishi mumkin?",
                "choices": [
                    "Oʻqishni tugatish",
                    "Oʻqishga kirish",
                    "Oʻqituvchi",
                    "Dars xonasi",
                ],
                "answer": 1,
                "explanation": "입(入) = kirmoq, 학(學) = oʻqish. Ikkalasini "
                               "qoʻshsangiz: oʻqishga kirish. Soʻzni koʻrmagan "
                               "boʻlsangiz ham ildizlardan topdingiz — matnning "
                               "asosiy gapi shu.",
            },
        ],
        "body": """
<p>Koreys tilini oʻrganayotgan koʻp odam bir xil ish qiladi: lugʻat ochadi va soʻzlarni
bittalab yodlaydi. Bu eng sekin yoʻl. Sababi oddiy — koreys soʻzlarining katta qismi
yasalgan, yaʼni ular <b>ildizlardan</b> yigʻilgan, xuddi «kitob-xona» yoki «suv-quvur»
kabi.</p>

<p>Koreyadagi har bir binoda bir yozuv bor:
<span class="cn-word" data-tr="chiqish joyi">출구</span> (chulgu). Metroda, bozorda,
aeroportda — hamma joyda. Uning birinchi boʻgʻini <b>출</b> (chul), xitoychadan kirgan
ildiz, maʼnosi: <i>chiqmoq</i>. Ikkinchisi 구 — <i>ogʻiz</i>, yaʼni teshik. Chiqish
ogʻzi. Chiqish joyi.</p>

<p>Endi shu bitta ildizni bilgan odam nechta soʻzni taniydi?</p>

<p><span class="cn-word" data-tr="ishga chiqish">출근</span> — ishga chiqish.
<span class="cn-word" data-tr="joʻnash, yoʻlga chiqish">출발</span> — joʻnash.
<span class="cn-word" data-tr="davomat, qatnashish">출석</span> — davomat, yaʼni
oʻrningga chiqish. <span class="cn-word" data-tr="topshirish">제출</span> — topshirish,
yaʼni koʻtarib chiqarish. <span class="cn-word" data-tr="eksport">수출</span> —
tashib chiqarish, yaʼni eksport.
<span class="cn-word" data-tr="koʻchaga chiqish">외출</span> — tashqariga chiqish.
<span class="cn-word" data-tr="kirish-chiqish, qatnov">출입</span> (churip) —
kirish-chiqish. <span class="cn-word" data-tr="xarajat, sarf">지출</span> — pulning
chiqishi, yaʼni xarajat.</p>

<p>Toʻqqizta soʻz. Hammasi bitta boʻgʻindan. Eʼtibor bering: ildiz soʻzning boshida ham,
oxirida ham turishi mumkin — 출구 da boshida, 수출 da oxirida.</p>

<p>Endi eng muhim joyi. Aytaylik, siz <b>수출</b> soʻzini umuman koʻrmagansiz.
수 — «tashimoq», 출 — «chiqarish». Demak: tashib chiqarish. Eksport. Siz bu soʻzni
yodlamadingiz — <b>oʻqib chiqardingiz</b>.</p>

<p>Powertyning koreys lugʻatida shunday 51 ta ildiz bor va ular ikki yuzdan ortiq
soʻzni ochadi. Koreys lugʻatining yarmidan koʻpi shu tarzda yasalgan. Shuning uchun
qoida bitta: <b>soʻzni yodlama — ildizini top.</b></p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 2 — Oʻzbek va koreys: bir xil tartib
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Oʻzbek va koreys: bir xil tartib",
        "summary": (
            "Koreys gapi oʻzbek gapi bilan bir xil tartibda tuziladi — ingliz "
            "tili esa boshqacha. Oʻzbek oʻquvchisi buni bilmasdan afzallikni "
            "qoʻldan chiqaradi."
        ),
        "order":   2,
        "open_question":
            "Ingliz tilida fe'l oʻrtada turadi. Koreys tilini ingliz tili "
            "orqali oʻrganayotgan odam qanday xatolarga yoʻl qoʻyadi deb "
            "oʻylaysiz?",
        "grammar": [
            {
                "pattern":  "SOV tartibi va 조사 (kelishik koʻrsatkichlari)",
                "meaning":  "Koreys va oʻzbek tilida gap bir xil tartibda "
                            "tuziladi: ega — toʻldiruvchi — fe'l. Ikkala tilda "
                            "ham soʻzdan KEYIN qoʻshimcha qoʻyiladi va fe'l "
                            "gapning oxirida turadi. Ingliz tilida esa fe'l "
                            "oʻrtada.",
                "examples": [
                    "Men kitob-ni oʻqiy-man  =  저는 책을 읽어요",
                    "maktab-ga  =  학교에      ·      Aziz-ga  =  아지즈에게",
                    "kitob-ning  =  책의       ·      suv-ni  =  물을",
                ],
            },
        ],
        "questions": [
            {
                "text": "Koreys gapida fe'l qayerda turadi?",
                "choices": [
                    "Gapning boshida",
                    "Ega bilan toʻldiruvchi orasida",
                    "Gapning oxirida",
                    "Qayerda boʻlsa ham farqi yoʻq",
                ],
                "answer": 2,
                "explanation": "Koreys tilida ham, oʻzbek tilida ham fe'l "
                               "oxirida keladi: 책을 읽어요 — «kitobni "
                               "oʻqiyman». Ingliz tilida esa oʻrtada: "
                               "I read a book.",
            },
            {
                "text": "Oʻzbekcha -ni qoʻshimchasiga koreyschada nima "
                        "toʻgʻri keladi?",
                "choices": ["에", "의", "을/를", "에게"],
                "answer": 2,
                "explanation": "을/를 — tushum kelishigi koʻrsatkichi, "
                               "oʻzbekcha -ni. 물을 마셔요 = «suvni ichaman».",
            },
            {
                "text": "«Maktabga boraman» gapi koreyschada qaysi tartibda "
                        "tuziladi?",
                "choices": [
                    "Boraman — maktabga",
                    "Maktabga — boraman",
                    "Men — boraman — maktabga",
                    "Boraman — men — maktabga",
                ],
                "answer": 1,
                "explanation": "학교에 가요 — soʻzma-soʻz «maktabga boraman». "
                               "Oʻzbekchadagi tartib bilan bir xil.",
            },
        ],
        "body": """
<p>Koreys tilini oʻrganayotgan oʻzbek oʻquvchi koʻpincha inglizcha darsliklardan
foydalanadi. Va bilmagan holda oʻzining eng katta afzalligini qoʻldan chiqaradi.</p>

<p>Mana bitta gap, uch tilda:</p>

<p>Oʻzbekcha: <b>Men kitobni oʻqiyman.</b><br>
Koreyscha: <b><span class="cn-word" data-tr="men (kamtarona)">저</span>는
<span class="cn-word" data-tr="kitob">책</span>을
<span class="cn-word" data-tr="oʻqiyman">읽어요</span></b> (chonun chegul ilgoyoʻ).<br>
Inglizcha: <b>I read a book.</b></p>

<p>Diqqat bilan qarang. Oʻzbekcha va koreyscha gapda soʻzlar <b>bir xil tartibda</b>
turibdi: avval «men», keyin «kitobni», eng oxirida fe'l. Inglizchada esa fe'l
oʻrtaga tushib qolgan.</p>

<p>Bu tasodif emas. Ikkala tilda ham fe'l gapning oxirida turadi. Ikkala tilda ham
qoʻshimcha soʻzning <b>oldiga</b> emas, <b>orqasiga</b> qoʻshiladi. Ingliz tilida esa
«to school» — soʻzdan oldin.</p>

<p>Qoʻshimchalar ham juft-juft mos keladi. Oʻzbekcha <b>-ni</b> — koreyschada
<span class="cn-word" data-tr="tushum kelishigi koʻrsatkichi">을</span>/를:
«suvni ichaman» = <span class="cn-word" data-tr="suv">물</span>을
<span class="cn-word" data-tr="ichaman">마셔요</span>. Oʻzbekcha <b>-ga</b> —
koreyschada <span class="cn-word" data-tr="joʻnalish koʻrsatkichi (joyga)">에</span>:
«maktabga boraman» = <span class="cn-word" data-tr="maktab">학교</span>에
<span class="cn-word" data-tr="boraman">가요</span>. Oʻzbekcha <b>-ning</b> —
koreyschada <span class="cn-word" data-tr="qaratqich kelishigi koʻrsatkichi">의</span>.</p>

<p>Buning amaliy foydasi katta. Koreyscha gapni tuzayotganda uni ingliz tilidan emas,
<b>oʻzbek tilidan</b> tarjima qiling — soʻzlarni oʻrniga qoʻyish kifoya.
«Do'stimga xat yozdim» degan gapni oʻzbekchadan koreyschaga oʻgirish uchun tartibni
oʻzgartirish shart emas.</p>

<p>Ingliz tilida gapiradigan oʻquvchi buni bir yil davomida oʻrganadi. Siz esa buni
allaqachon bilasiz.</p>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    # 13 — Koreys alifbosi — ogʻzingizning surati
    # ══════════════════════════════════════════════════════════════════
    {
        "title":   "Koreys alifbosi — ogʻzingizning surati",
        "summary": (
            "Haqiqiy voqea: dunyodagi kam alifbolardan biri — kim, qachon va "
            "nima uchun yaratgani aniq maʼlum boʻlgan alifbo. Harflar ularni "
            "talaffuz qiladigan aʼzoning shakliga qarab chizilgan."
        ),
        "order":   13,
        "open_question":
            "ㅋ harfi ㄱ ga bitta chiziq qoʻshib yasalgan. Sizningcha, "
            "qoʻshimcha chiziq tovushga nima qoʻshadi?",
        "grammar": [
            {
                "pattern":  "Undoshlarning asosiy beshtasi",
                "meaning":  "«훈민정음 해례본» (1446) kitobiga koʻra, beshta "
                            "asosiy undosh tovushni hosil qiladigan aʼzoning "
                            "shaklidan olingan. Qolganlari shu beshtasiga "
                            "chiziq qoʻshib yasalgan: chiziq qoʻshilsa, tovush "
                            "kuchayadi.",
                "examples": [
                    "ㄱ — til ildizi boʻgʻizni toʻsgan shakl",
                    "ㄴ — til uchi tanglayga tekkan shakl · ㅁ — ogʻiz shakli",
                    "ㅅ — tish shakli · ㅇ — boʻgʻiz shakli",
                    "ㄱ → ㅋ,  ㄴ → ㄷ → ㅌ,  ㅁ → ㅂ → ㅍ,  ㅅ → ㅈ → ㅊ",
                ],
            },
        ],
        "questions": [
            {
                "text": "ㅁ harfi nimaning shaklidan olingan?",
                "choices": ["Tishning", "Ogʻizning", "Boʻgʻizning", "Tilning"],
                "answer": 1,
                "explanation": "«훈민정음 해례본» buni toʻgʻridan-toʻgʻri "
                               "aytadi: ㅁ — ogʻiz shakli. Shuning uchun u "
                               "kvadrat.",
            },
            {
                "text": "Alifbo qachon tugatilgan va kitob qachon chop "
                        "etilgan?",
                "choices": [
                    "Ikkalasi ham 1446-yilda",
                    "Alifbo 1443-yilda, kitob 1446-yilda",
                    "Alifbo 1446-yilda, kitob 1443-yilda",
                    "Ikkalasi ham 1443-yilda",
                ],
                "answer": 1,
                "explanation": "Alifbo 1443-yilda tugatilgan, «훈민정음» "
                               "kitobi esa uch yildan keyin, 1446-yilda "
                               "chiqqan. Bu ikki sanani aralashtirmang.",
            },
            {
                "text": "Nega bu alifbo tarixda alohida oʻrin tutadi?",
                "choices": [
                    "U dunyodagi eng qadimgi alifbo",
                    "Unda eng koʻp harf bor",
                    "Uni kim, qachon va nima uchun yaratgani aniq maʼlum",
                    "Uni faqat olimlar oʻqiy oladi",
                ],
                "answer": 2,
                "explanation": "Dunyodagi alifbolarning deyarli hammasi "
                               "asta-sekin oʻzgarib shakllangan. 한글 esa "
                               "maqsad bilan, maʼlum sanada, maʼlum odam "
                               "tomonidan yaratilgan va sababi yozib "
                               "qoldirilgan.",
            },
        ],
        "body": """
<p>Dunyodagi alifbolarning deyarli hammasi asta-sekin, asrlar davomida shakllangan.
Ularni kim oʻylab topganini hech kim bilmaydi. <span class="cn-word"
data-tr="koreys alifbosi">한글</span> (hangul) — kam sonli istisnolardan biri: uni kim
yaratgani, qachon yaratgani va <b>nima uchun</b> yaratgani aniq maʼlum.</p>

<p>XV asrda Koreyada yozuv xitoycha ierogliflar bilan olib borilardi. Ularni oʻrganish
uchun yillar kerak edi, shuning uchun oddiy odam yoza olmasdi. Shoh
<span class="cn-word" data-tr="Sejong — Koreya shohi (1397–1450)">세종</span> (sejoʻng)
buni oʻzgartirishga qaror qildi. Alifbo <b>1443-yilda</b> tugatildi, uni tushuntiruvchi
<span class="cn-word" data-tr="«Xalqni oʻrgatuvchi toʻgʻri tovushlar» — alifbo haqidagi kitob">훈민정음</span>
(hunminjongum) kitobi esa <b>1446-yilda</b> chop etildi.</p>

<p>Endi eng qizigʻi. Harflar shunchaki chizilmagan — har biri oʻzini talaffuz
qiladigan aʼzoning surati.</p>

<p><b>ㄱ</b> — <span class="cn-word" data-tr="til">혀</span> ildizi
<span class="cn-word" data-tr="boʻgʻiz">목구멍</span>ni toʻsgan paytdagi shakl.
Hozir «k» tovushini ayting va tilingiz orqasi qayerga borishiga eʼtibor bering — ㄱ
aynan shuni chizadi.</p>

<p><b>ㄴ</b> — til uchi tanglayga tekkan shakl. <b>ㅁ</b> —
<span class="cn-word" data-tr="ogʻiz">입</span>ning oʻzi, shuning uchun u kvadrat.
<b>ㅅ</b> — <span class="cn-word" data-tr="tish">이</span> shakli.
<b>ㅇ</b> — boʻgʻizning shakli, dumaloq.</p>

<p>Asosiy <span class="cn-word" data-tr="undosh">자음</span>lar shu beshtasi. Qolganlari
ularga chiziq qoʻshib yasalgan: ㄱ ga bitta chiziq qoʻshsangiz ㅋ, ㄴ dan ㄷ, ㄷ dan ㅌ
hosil boʻladi. <span class="cn-word" data-tr="unli">모음</span>lar esa uchta belgidan
yigʻilgan: nuqta (osmon), yotiq chiziq ㅡ (yer) va tik chiziq ㅣ (odam).</p>

<p>Dastlab 28 ta harf bor edi; bugun 24 tasi ishlatiladi. «훈민정음 해례본» 1997-yilda
YUNESKOning «Jahon xotirasi» roʻyxatiga kiritilgan.</p>

<p>Shuning uchun 한글 ni yodlash shart emas. Uni <b>tushunish</b> mumkin.</p>
""",
    },
]
