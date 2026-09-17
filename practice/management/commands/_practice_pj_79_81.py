# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-79 … PJ-81. Blok F ochiladi.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi — uchalasi ham «tushunarli» deb oʻtib
ketiladigan, keyin yozganda chiqadigan turdan:
    1. RASMIY OTLARNING ULANISHI bir xil emas va aynan shu yerda
       adashiladi:
           こと / の  — feʼlga yalangʻoch
           ということ — oddiy shakl, OT va な-SIFAT だ bilan
           わけ       — な-sifat な, ot という
           はず       — な-sifat な, ot の
           に違いない  — hammasi YALANGʻOCH
       Beshta qolip, toʻrt xil ulanish. Har bir testda kamida uchta
       savol shu ustunda turadi.
    2. INKORNING JOYI (PJ-80): 〜わけではない («degani emas») ≠
       〜ないわけです («shuning uchun qilmas ekan-da»). Bir xil ikki
       boʻlak, boshqa tartib, butunlay boshqa maʼno.
    3. KUCHNING DARAJASI (PJ-81): 来ないはずです («kelmasa kerak»)
       ≠ 来るはずがない («kelishi mumkin emas»). Ikkalasi ham inkor
       tarafda, lekin biri kutish, ikkinchisi rad etish.

⚠️ CUMULATIVE: PJ-79 mashqida わけ (PJ-80) va はずがない / に違いない
(PJ-81) yoʻq. PJ-80 da に違いない va はずがない hali yoʻq — PJ-62 dagi
はずです esa bor, chunki dars uni ataylab solishtiradi.
`verify_pj_practice_79_81.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_79_81.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "日本語",
    "description": "Yapon tili — grammatika va yozuv mashqlari",
    "icon":        "bi-brilliance",
    "color":       "#be123c",
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


def r(kanji, kana):
    return f"<ruby>{kanji}<rt>{kana}</rt></ruby>"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ── feʼllar (oxirgi kana ALOHIDA — PJ-25 dagi saboq) ─────────────────
YOMU    = r("読", "よ") + "む"
HANASU  = r("話", "はな") + "す"
OYOGU   = r("泳", "およ") + "ぐ"
HASHIRU = r("走", "はし") + "る"
NAKU    = r("泣", "な") + "く"
NAITEIRU = r("泣", "な") + "いている"
MIRU    = r("見", "み") + "る"
MIMASHITA = r("見", "み") + "ました"
KIKU    = r("聞", "き") + "く"
KIKIMASHITA = r("聞", "き") + "きました"
KIMERU  = r("決", "き") + "める"
KIMEMASHITA = r("決", "き") + "めました"
YAKUSOKU = r("約束", "やくそく")
HIKKOSU = r("引", "ひ") + "っ" + r("越", "こ") + "す"
SHIRU   = r("知", "し") + "る"
SHIRANAKATTA = r("知", "し") + "らなかった"
WASURERU = r("忘", "わす") + "れる"
KURU    = r("来", "く") + "る"
KONAI   = r("来", "こ") + "ない"
YASUMU  = r("休", "やす") + "む"
IKU     = r("行", "い") + "く"
IKANAI  = r("行", "い") + "かない"
IKEMASEN = r("行", "い") + "けません"
SUMU    = r("住", "す") + "んでいた"
KOMU    = r("混", "こ") + "んでいる"
OKURERU = r("遅", "おく") + "れる"
OKUREMASHITA = r("遅", "おく") + "れました"
TSUKU   = r("着", "つ") + "く"
TORU    = r("撮", "と") + "る"
FURU    = r("降", "ふ") + "る"

# ── sifatlar ─────────────────────────────────────────────────────────
TANOSHII = r("楽", "たの") + "しい"
MUZUKASHII = r("難", "むずか") + "しい"
TAKAI   = r("高", "たか") + "い"
MEZURASHII = r("珍", "めずら") + "しい"
SUKI    = r("好", "す") + "き"
KIRAI   = r("嫌", "きら") + "い"
JOUZU   = r("上手", "じょうず")
GENKI   = r("元気", "げんき")
BYOUKI  = r("病気", "びょうき")

# ── otlar ────────────────────────────────────────────────────────────
HON     = r("本", "ほん")
NAMAE   = r("名前", "なまえ")
MACHI   = r("町", "まち")
KODOMO  = r("子供", "こども")
GAKUSEI = r("学生", "がくせい")
SENSEI  = r("先生", "せんせい")
SHUMI   = r("趣味", "しゅみ")
SHASHIN = r("写真", "しゃしん")
SHIKEN  = r("試験", "しけん")
DENKI   = r("電気", "でんき")
DENSHA  = r("電車", "でんしゃ")
MICHI   = r("道", "みち")
IMI     = r("意味", "いみ")
JIJITSU = r("事実", "じじつ")
KASA    = r("傘", "かさ")
TSUKUE  = r("机", "つくえ")
HANNIN  = r("犯人", "はんにん")
MACHIGAI = r("間違", "まちが") + "い"
KANAZAWA = r("金沢", "かなざわ")
TOUKYOU = r("東京", "とうきょう")
KYOUTO  = r("京都", "きょうと")
OOSAKA  = r("大阪", "おおさか")
TANAKA  = r("田中", "たなか")
SANNEN  = r("三年", "さんねん")
SANJI   = r("三時", "さんじ")
MAINICHI = r("毎日", "まいにち")
KYOU    = r("今日", "きょう")
ASHITA  = r("明日", "あした")
AME     = r("雨", "あめ")
AKAI    = r("赤", "あか") + "い"
ZETTAI  = r("絶対", "ぜったい")
CHIGAINAI = "に" + r("違", "ちが") + "いない"
CHIGAIARIMASEN = "に" + r("違", "ちが") + "いありません"

# ── tayyor qoliplar ──────────────────────────────────────────────────
KOTOGADEKIMASU = HANASU + "ことができます"
NOGADEKIMASU   = HANASU + "のができます"
SHUMIKOTO      = SHUMI + "は" + SHASHIN + "を" + TORU + "ことです"
SHUMINO        = SHUMI + "は" + SHASHIN + "を" + TORU + "のです"
NAITEIRUNO     = KODOMO + "が" + NAITEIRU + "のを" + MIMASHITA
NAITEIRUKOTO   = KODOMO + "が" + NAITEIRU + "ことを" + MIMASHITA
MUNIRA_TOIU    = "「ムニラ」という" + NAMAE
MUNIRA_TO      = "「ムニラ」と" + NAMAE
GAKUSEI_DA_KOTO = GAKUSEI + "だということ"
GAKUSEI_KOTO    = GAKUSEI + "ということ"


# ══════════════════════════════════════════════════════════════════════
# PJ-79 — ということ va gapni otga aylantirish
# ══════════════════════════════════════════════════════════════════════
Q_PJ79 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>こと va の gapda nima qiladi?</p>",
      ["Feʼlni otga aylantiradi",
       "Feʼlni inkor qiladi",
       "Feʼlni oʻtgan zamonga oʻtkazadi",
       "Gapni savolga aylantiradi"],
      "Feʼlni otga aylantiradi",
      f"<p><strong>Feʼlni otga aylantiradi</strong>. Oʻzbekcha "
      f"«oʻqi<strong>moq</strong>» → «oʻqi<strong>sh</strong>» bilan "
      f"bir xil ish: {YOMU} → {YOMU}こと. Shundan keyin u は yoki を "
      f"dan oldin tura oladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HANASU}___が"
      f"できます</strong></p>",
      ["こと", "の", "ということ", "という"],
      "こと",
      f"<p><strong>{KOTOGADEKIMASU}</strong>. PJ-41 dagi "
      f"〜ことができます qatʼiy qolip — bu yerga の hech qachon "
      f"tushmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHUMI}は"
      f"{SHASHIN}を{TORU}___です</strong></p>",
      ["こと", "の", "という", "ということ"],
      "こと",
      f"<p><strong>{SHUMIKOTO}</strong> — «mening ovunchogʻim surat "
      f"olish». «Ovunchoq» bir martalik harakat emas, umumiy odat, "
      f"shuning uchun bu qolipda ham faqat こと turadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>「ムニラ」___"
      f"{NAMAE}は{MEZURASHII}です</strong></p>",
      ["という", "と", "の", "ということ"],
      "という",
      f"<p><strong>{MUNIRA_TOIU}</strong> — «Munira degan ism». "
      f"Oʻzbekcha «degan» qayerda tursa, という ham oʻsha yerda. "
      f"と yolgʻiz otga ulanmaydi.</p>"),

    q("<p>Gap boshida yolgʻiz turgan «ということは» nima maʼnoni "
      "beradi?</p>",
      ["Demak", "Chunki", "Lekin", "Masalan"],
      "Demak",
      f"<p><strong>Demak</strong>. Undan keyin xulosa keladi: "
      f"{DENKI}が"+r('消','き')+f"えている。ということは、もう"
      f"{r('寝','ね')}た。 — «Chiroq oʻchgan. Demak, allaqachon "
      f"uxlagan».</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KODOMO}が"
      f"{NAITEIRU}___を{MIMASHITA}</strong></p>",
      ["の", "こと", "という", "ということ"],
      "の",
      f"<p><strong>{NAITEIRUNO}</strong> — koʻz bilan koʻrilgan aniq "
      f"sahna har doim <strong>の</strong> oladi. {MIRU}, {KIKU}, "
      f"{r('待','ま')}つ kabi sezgi feʼllari shu guruhda.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{MAINICHI}"
      f"{HASHIRU}___を{KIMEMASHITA}</strong></p>",
      ["こと", "の", "という", "ということ"],
      "こと",
      f"<p><strong>{HASHIRU}ことを{KIMEMASHITA}</strong>. Qaror "
      f"boshda turadi — bu mavhum harakat, koʻz bilan koʻriladigan "
      f"sahna emas. {KIMERU}, {YAKUSOKU}する, {r('伝','つた')}える "
      f"— hammasi こと oladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENSEI}が"
      f"{GAKUSEI}___ということを{SHIRANAKATTA}</strong></p>",
      ["だ", "の", "な", "hech nima"],
      "だ",
      f"<p><strong>{GAKUSEI_DA_KOTO}</strong>. ということ oldida "
      f"oddiy shakl turadi, va otning oddiy shakli <strong>だ</strong> "
      f"bilan tugaydi. «{GAKUSEI_KOTO}» — eng koʻp uchraydigan "
      f"xato.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENSEI}が"
      f"{BYOUKI}___ということを{KIKIMASHITA}</strong></p>",
      ["だ", "な", "の", "hech nima"],
      "だ",
      f"<p><strong>{BYOUKI}だということ</strong>. {BYOUKI} — "
      f"な-sifat, uning oddiy shakli ham <strong>だ</strong> bilan "
      f"tugaydi. な faqat otni aniqlaganda chiqadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{OYOGU}___が"
      f"{SUKI}です</strong></p>",
      ["の", "という", "ということ", "だ"],
      "の",
      f"<p><strong>{OYOGU}のが{SUKI}です</strong>. 〜が{SUKI} bilan "
      f"こと ham toʻgʻri, lekin kundalik nutqda <strong>の</strong> "
      f"tabiiyroq eshitiladi.</p>"),

    q(f"<p>«Parining koʻchib ketishini kecha eshitdim» — boʻsh "
      f"joyga nima tushadi?</p><p><strong>パリさんが{HIKKOSU}___を"
      f"{r('昨日','きのう')}{KIKIMASHITA}</strong></p>",
      ["ということ", "という", "の", "だ"],
      "ということ",
      f"<p><strong>{HIKKOSU}ということ</strong>. Birovdan eshitilgan "
      f"butun gap otga aylanadi va を ni oladi — oʻzbekcha "
      f"«koʻchib ketish<strong>-i-ni</strong>» bilan bir xil.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('去年','きょねん')}"
      f"{KANAZAWA}___{MACHI}へ{r('行','い')}きました</strong></p>",
      ["という", "の", "と", "ということ"],
      "という",
      f"<p><strong>{KANAZAWA}という{MACHI}</strong> — «Kanazava degan "
      f"shahar». Tinglovchi bu shaharni bilmasligi mumkin, shuning "
      f"uchun という qoʻyiladi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>の bilan こと orasidagi asosiy farq nimada?</p>",
      ["の — koʻz bilan koʻriladigan aniq harakat, こと — mavhum harakat",
       "の — oʻtgan zamon, こと — hozirgi zamon",
       "の — muloyim, こと — oddiy",
       "の — feʼl uchun, こと — sifat uchun"],
      "の — koʻz bilan koʻriladigan aniq harakat, こと — mavhum harakat",
      f"<p>Tanlash uchun bitta savol yetadi: bu harakatni koʻz bilan "
      f"koʻrasizmi? Koʻrsangiz — <strong>の</strong> "
      f"({NAITEIRUNO}); koʻrmasangiz, u faqat boshda tursa — "
      f"<strong>こと</strong>.</p>"),

    q(f"<p>{TOUKYOU}へ{r('行','い')}きました — nega bu yerda という "
      f"yoʻq?</p>",
      ["Nom tinglovchiga tanish boʻlsa, という tushib qoladi",
       "Shahar nomlariga という qoʻshilmaydi",
       "へ dan oldin という turmaydi",
       "Oʻtgan zamonda という ishlatilmaydi"],
      "Nom tinglovchiga tanish boʻlsa, という tushib qoladi",
      f"<p>という tinglovchi <strong>bilmasligi mumkin</strong> "
      f"boʻlgan nomni tanishtiradi. {TOUKYOU} ni hamma biladi, "
      f"{KANAZAWA} ni esa bilmasligi mumkin — shuning uchun "
      f"{KANAZAWA}という{MACHI}.</p>"),

    q("<p>「"+r("遠慮","えんりょ")+"」とはどういうことですか。 — bu "
      "savol nimani soʻrayapti?</p>",
      ["Soʻzning maʼnosini", "Soʻzning oʻqilishini",
       "Soʻzning yozilishini", "Soʻzni kim aytganini"],
      "Soʻzning maʼnosini",
      f"<p><strong>Soʻzning maʼnosini</strong> — «… nima degani?». "
      f"Bu ということ ning ikkinchi vazifasi; javobda {IMI} degan soʻz "
      f"tez-tez chiqadi.</p>"),

    q(f"<p>«Imtihonning qiyinligi» — yaponchada qanday boʻladi?</p>",
      [f"{SHIKEN}が{MUZUKASHII}ということ",
       f"{SHIKEN}が{MUZUKASHII}だということ",
       f"{SHIKEN}が{MUZUKASHII}なということ",
       f"{SHIKEN}の{MUZUKASHII}ということ"],
      f"{SHIKEN}が{MUZUKASHII}ということ",
      f"<p>{MUZUKASHII} — い-sifat, uning oddiy shakli oʻzi. "
      f"<strong>だ</strong> faqat ot va な-sifatga qoʻshiladi, "
      f"い-sifatga emas.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gap toʻgʻri?</p>",
      [KOTOGADEKIMASU, NOGADEKIMASU,
       HANASU + "ということができます", HANASU + "というができます"],
      KOTOGADEKIMASU,
      f"<p><strong>{KOTOGADEKIMASU}</strong>. 〜ことができます "
      f"tayyor qolip boʻlib, undagi こと hech narsaga "
      f"almashtirilmaydi.</p>"),

    q("<p>Qaysi gapda xato bor?</p>",
      [NAITEIRUKOTO, NAITEIRUNO,
       HASHIRU + "ことを" + KIMEMASHITA,
       SHUMIKOTO],
      NAITEIRUKOTO,
      f"<p><strong>{NAITEIRUKOTO}</strong> xato — koʻz bilan "
      f"koʻrilgan sahna こと emas, <strong>の</strong> oladi: "
      f"{NAITEIRUNO}. Qolgan uchtasi toʻgʻri.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q("<p>Soʻzlarni toʻgʻri tartibga qoʻying.</p>"
      f"<p><strong>を · {HIKKOSU}ということ · パリさんが · "
      f"{KIKIMASHITA}</strong></p>",
      [f"パリさんが{HIKKOSU}ということを{KIKIMASHITA}",
       f"パリさんが{KIKIMASHITA}を{HIKKOSU}ということ",
       f"{HIKKOSU}ということをパリさんが{KIKIMASHITA}",
       f"を{HIKKOSU}ということパリさんが{KIKIMASHITA}"],
      f"パリさんが{HIKKOSU}ということを{KIKIMASHITA}",
      f"<p><strong>パリさんが{HIKKOSU}ということを{KIKIMASHITA}</strong>. "
      f"Otga aylangan gap を ni oladi va feʼl eng oxirida turadi — "
      f"yapon tili oʻzbekcha kabi kesimni oxiriga qoʻyadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム: "
      f"{DENKI}が{r('消','き')}えていますね。</strong></p>"
      f"<p><strong>ラノ: ___</strong></p>",
      [f"ということは、もう{r('寝','ね')}たようですね。",
       f"ということが、もう{r('寝','ね')}たようですね。",
       f"というのは、もう{r('寝','ね')}たようですね。",
       f"ということを、もう{r('寝','ね')}たようですね。"],
      f"ということは、もう{r('寝','ね')}たようですね。",
      f"<p><strong>ということは</strong> — «demak». Undan keyin "
      f"xulosa keladi. が, の va を bu oʻrinda mantiqiy bogʻlanish "
      f"yasamaydi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-80 — わけ va uning toʻrtta aʼzosi
# ══════════════════════════════════════════════════════════════════════
WAKEDESU      = JOUZU + "なわけです"
WAKEDEWANAI   = KIRAI + "なわけではありません"
NAIWAKEDESU   = SUKI + "ではないわけです"
SUKINAWAKE    = SUKI + "なわけではありません"
WAKEGANAI     = WASURERU + "わけがありません"
WAKENIWA      = YASUMU + "わけにはいきません"
IKANAIWAKENIWA = IKANAI + "わけにはいきません"

Q_PJ80 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q(f"<p>{r('訳','わけ')} degan ot qanday maʼno beradi?</p>",
      ["Sabab, mantiq — «ish shunday boʻlgani»",
       "Vaqt — «shu paytda»",
       "Joy — «shu yerda»",
       "Miqdor — «shuncha»"],
      "Sabab, mantiq — «ish shunday boʻlgani»",
      f"<p><strong>Sabab, mantiq</strong>. こと gapni shunchaki otga "
      f"aylantiradi; わけ esa unga «bu yerda mantiq bor» degan maʼno "
      f"qoʻshadi. Shuning uchun u har doim xulosa bilan ishlaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{JOUZU}___"
      f"わけです</strong></p>",
      ["な", "hech nima", "の", "だ"],
      "な",
      f"<p><strong>{WAKEDESU}</strong>. な-sifat わけ oldida "
      f"<strong>な</strong> ni saqlaydi — PJ-75 dagi ようだ bilan "
      f"bir xil ulanish.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GAKUSEI}___"
      f"わけではありません</strong></p>",
      ["という", "な", "の", "hech nima"],
      "という",
      f"<p><strong>{GAKUSEI}というわけではありません</strong>. Ot わけ "
      f"oldida <strong>という</strong> ni oladi — PJ-79 dagi oʻsha "
      f"«degan».</p>"),

    q("<p>〜わけです bilan yangi xabar berish mumkinmi?</p>",
      ["Yoʻq — u faqat tanish narsadan chiqadigan xulosani aytadi",
       "Ha, har qanday yangilik uchun ishlatiladi",
       "Faqat ob-havo haqidagi yangilik uchun",
       "Faqat oʻtgan zamondagi yangilik uchun"],
      "Yoʻq — u faqat tanish narsadan chiqadigan xulosani aytadi",
      f"<p><strong>Yoʻq.</strong> わけ tinglovchi oʻzi ham chiqara "
      f"oladigan xulosani ovoz chiqarib aytadi. Yangi xabar uchun "
      f"PJ-74 dagi {FURU}そうです yoki PJ-62 dagi "
      f"{FURU}でしょう kerak.</p>"),

    q("<p>〜わけではありません qolipining oʻzbekchasi qaysi biri?</p>",
      ["… degani emas", "… boʻlishi kerak", "… boʻlsa kerak",
       "… ning iloji yoʻq"],
      "… degani emas",
      f"<p><strong>«… degani emas»</strong> — soʻzma-soʻz mos "
      f"tushadi: わけ «degani», ではない «emas». Toʻgʻridan-toʻgʻri "
      f"«yoʻq» deyish qoʻpol boʻlgan joyda ishlatiladi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>«Yomon koʻraman degani emas» — boʻsh joyga nima "
      f"tushadi?</p><p><strong>{KIRAI}___わけではありません</strong></p>",
      ["な", "hech nima", "という", "の"],
      "な",
      f"<p><strong>{WAKEDEWANAI}</strong>. {KIRAI} — な-sifat "
      f"(oxiri い boʻlsa ham!), shuning uchun わけ oldida な "
      f"turadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{DENSHA}が"
      f"{r('止','と')}まっている。それで{MICHI}が{KOMU}___。</strong></p>",
      ["わけです", "わけではありません", "わけがありません",
       "わけにはいきません"],
      "わけです",
      f"<p><strong>わけです</strong>. Tiqilinchni gapiruvchi "
      f"allaqachon koʻrgan; yangilik — uning sababga bogʻlanishi. "
      f"それで bilan birga bu qolip juda tez-tez keladi.</p>"),

    q(f"<p>{WAKENIWA} — maʼnosi nima?</p>",
      ["Dam olishning iloji yoʻq",
       "Dam ololmayman, kuchim yetmaydi",
       "Dam olmasligim mumkin",
       "Dam olmadim"],
      "Dam olishning iloji yoʻq",
      f"<p><strong>Dam olishning iloji yoʻq.</strong> Bu qobiliyat "
      f"haqida emas — jismonan dam ola oladi, lekin burch yoʻl "
      f"bermaydi. Qobiliyat uchun PJ-42 dagi {r('休','やす')}めません "
      f"kerak boʻladi.</p>"),

    q(f"<p>«Vada berganman, shuning uchun bormasdan boʻlmaydi» — "
      f"boʻsh joyga nima tushadi?</p><p><strong>{YAKUSOKU}した"
      f"から、{IKANAI}___いきません</strong></p>",
      ["わけには", "わけでは", "わけが", "わけです"],
      "わけには",
      f"<p><strong>{IKANAIWAKENIWA}</strong>. Ikki inkor bir-birini "
      f"yeydi: «bormaslikning iloji yoʻq» = <strong>borishim "
      f"shart</strong>. PJ-33 dagi 〜なければなりません bilan bir "
      f"maʼno, ohangi ogʻirroq.</p>"),

    q(f"<p>«Pari vadasini unutishi mumkin emas» — boʻsh joyga nima "
      f"tushadi?</p><p><strong>パリさんが{YAKUSOKU}を{WASURERU}___"
      f"ありません</strong></p>",
      ["わけが", "わけでは", "わけには", "わけです"],
      "わけが",
      f"<p><strong>{WAKEGANAI}</strong> — «unutishi mumkin emas». "
      f"わけがない ehtimolni butunlay rad etadi; わけではない esa "
      f"faqat xulosani yumshatadi.</p>"),

    q(f"<p>{SANNEN}{OOSAKA}に{SUMU}。ああ、それで___。 — boʻsh joyni "
      f"toʻldiring.</p>",
      [f"{JOUZU}なわけですね",
       f"{JOUZU}わけですね",
       f"{JOUZU}というわけがありませんね",
       f"{JOUZU}なわけにはいきませんね"],
      f"{JOUZU}なわけですね",
      f"<p><strong>{JOUZU}なわけですね</strong> — «shuning uchun "
      f"yaxshi bilar ekan-da». な-sifat な ni saqlaydi, va bu yerda "
      f"kerak boʻlgan aʼzo わけです.</p>"),

    q("<p>〜ないわけにはいかない nimani bildiradi?</p>",
      ["Qilishim shart", "Qilmasligim mumkin", "Qila olmayman",
       "Qilishni xohlamayman"],
      "Qilishim shart",
      f"<p><strong>Qilishim shart.</strong> «Qilmaslikning iloji "
      f"yoʻq» degani — ikki inkor bir-birini yeydi. Bu shakl "
      f"sababni ham sezdiradi: xohlamayman, lekin holat majbur "
      f"qilyapti.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>から bilan わけです orasidagi farq nimada?</p>",
      ["から sababni beradi, わけです undan chiqadigan xulosani aytadi",
       "から yozma tilda, わけです kundalik nutqda ishlatiladi",
       "から oʻtgan zamon uchun, わけです hozirgi zamon uchun",
       "Hech qanday farqi yoʻq"],
      "から sababni beradi, わけです undan chiqadigan xulosani aytadi",
      f"<p>PJ-53 dagi から yangi maʼlumot — <em>sababni</em> beradi. "
      f"わけです esa sababni allaqachon bilgan holda "
      f"<em>natijani</em> tushuntiradi: «shuning uchun ekan-da».</p>"),

    q(f"<p>{SUKINAWAKE} va {NAIWAKEDESU} — farqi nimada?</p>",
      ["Birinchisi «yoqtiraman degani emas», ikkinchisi «demak, "
       "yoqtirmas ekan-da»",
       "Birinchisi muloyim, ikkinchisi oddiy nutq",
       "Birinchisi oʻtgan zamon, ikkinchisi hozirgi zamon",
       "Ikkalasi ham bir xil maʼno beradi"],
      "Birinchisi «yoqtiraman degani emas», ikkinchisi «demak, "
      "yoqtirmas ekan-da»",
      f"<p>Inkorning <strong>joyi</strong> hal qiladi. ない "
      f"わけdan <em>keyin</em> boʻlsa — xulosa inkor qilinadi "
      f"(qisman inkor). ない わけdan <em>oldin</em> boʻlsa — gap "
      f"inkor qilinadi va わけ uni xulosa qiladi.</p>"),

    q("<p>はずです va わけです — qaysi biri hodisani koʻrgandan "
      "<em>keyin</em> aytiladi?</p>",
      ["わけです", "はずです", "Ikkalasi ham oldin aytiladi",
       "Ikkalasi ham keyin aytiladi"],
      "わけです",
      f"<p><strong>わけです</strong> — koʻrdim va tushundim. "
      f"PJ-62 dagi <strong>はずです</strong> esa aksincha: hali "
      f"koʻrmadim, lekin asosim bor va shunday boʻlishini "
      f"kutyapman.</p>"),

    q("<p>わけがない bilan わけではない — qaysi biri kuchliroq?</p>",
      ["わけがない — ehtimolni butunlay rad etadi",
       "わけではない — butun gapni inkor qiladi",
       "Ikkalasi bir xil kuchda",
       "わけではない — chunki u uzunroq"],
      "わけがない — ehtimolni butunlay rad etadi",
      f"<p><strong>わけがない</strong> «boʻlishi mumkin emas» "
      f"deydi va eshikni yopadi. <strong>わけではない</strong> esa "
      f"faqat bitta xulosani rad etadi: «… degani emas» — "
      f"qolgani ochiq qoladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gap toʻgʻri?</p>",
      [WAKEDESU, JOUZU + "わけです", JOUZU + "のわけです",
       JOUZU + "だわけです"],
      WAKEDESU,
      f"<p><strong>{WAKEDESU}</strong>. な-sifat わけ oldida "
      f"<strong>な</strong> ni saqlaydi. の — はず uchun, だ esa "
      f"PJ-79 dagi ということ uchun.</p>"),

    q("<p>Qaysi gapda xato bor?</p>",
      [f"{ASHITA}{AME}が{FURU}わけです",
       f"{MICHI}が{KOMU}わけです",
       WAKEDEWANAI,
       WAKENIWA],
      f"{ASHITA}{AME}が{FURU}わけです",
      f"<p>Birinchi gap xato: ertangi yomgʻir — <strong>yangi "
      f"xabar</strong>, わけ esa yangi xabar bermaydi. Toʻgʻrisi "
      f"{FURU}そうです yoki {FURU}でしょう. Qolgan uchtasi "
      f"toʻgʻri.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q("<p>Soʻzlarni toʻgʻri tartibga qoʻying.</p>"
      f"<p><strong>いきません · {YAKUSOKU}したから · わけには · "
      f"{IKANAI}</strong></p>",
      [f"{YAKUSOKU}したから、{IKANAI}わけにはいきません",
       f"{IKANAI}わけにはいきませんから、{YAKUSOKU}した",
       f"わけには{YAKUSOKU}したから、{IKANAI}いきません",
       f"{YAKUSOKU}したから、いきませんわけには{IKANAI}"],
      f"{YAKUSOKU}したから、{IKANAI}わけにはいきません",
      f"<p><strong>{YAKUSOKU}したから、{IKANAIWAKENIWA}</strong>. "
      f"Sabab oldinda (から), xulosa keyin, kesim esa eng oxirida — "
      f"yapon tilida gap har doim shu tartibda yigʻiladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: "
      f"{r('納豆','なっとう')}、{KIRAI}ですか。</strong></p>"
      f"<p><strong>イノム: ___</strong></p>",
      [f"いいえ、{KIRAI}なわけではありません。ただ、"
       f"{r('匂','にお')}いが{r('苦手','にがて')}なだけです。",
       f"いいえ、{KIRAI}わけではありません。ただ、"
       f"{r('匂','にお')}いが{r('苦手','にがて')}なだけです。",
       f"いいえ、{KIRAI}なわけにはいきません。ただ、"
       f"{r('匂','にお')}いが{r('苦手','にがて')}なだけです。",
       f"いいえ、{KIRAI}なわけがありません。ただ、"
       f"{r('匂','にお')}いが{r('苦手','にがて')}なだけです。"],
      f"いいえ、{KIRAI}なわけではありません。ただ、"
      f"{r('匂','にお')}いが{r('苦手','にがて')}なだけです。",
      f"<p><strong>{KIRAI}なわけではありません</strong> — «yomon "
      f"koʻraman degani emas». Toʻgʻridan-toʻgʻri «yoʻq» demasdan "
      f"yumshoq javob beradi. わけにはいきません burch haqida, "
      f"わけがありません esa juda qatʼiy chiqadi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-81 — はずがない va に違いない: ishonch darajalari
# ══════════════════════════════════════════════════════════════════════
KURUHAZU      = KURU + "はずです"
KONAIHAZU     = KONAI + "はずです"
KURUHAZUGANAI = KURU + "はずがありません"
KURUCHIGAI    = KURU + CHIGAINAI
GAKUSEINOHAZU = GAKUSEI + "のはずです"
GAKUSEINOHAZUGANAI = GAKUSEI + "のはずがありません"
GAKUSEICHIGAI = GAKUSEI + CHIGAINAI
GENKICHIGAI   = GENKI + CHIGAINAI
HAZUDATTA     = TSUKU + "はずだったのに"
KAMOSHIRENAI  = KURU + "かもしれません"
DESHOU        = KURU + "でしょう"

Q_PJ81 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜はずがない qanday maʼno beradi?</p>",
      ["… boʻlishi mumkin emas", "… boʻlsa kerak",
       "… boʻlishi mumkin", "… boʻlishi kerak edi"],
      "… boʻlishi mumkin emas",
      f"<p><strong>«… boʻlishi mumkin emas»</strong>. Soʻzma-soʻz "
      f"«bunday boʻlishining asosi yoʻq» — yaʼni mantiqan imkonsiz. "
      f"Bu his emas, dalilga suyangan xulosa.</p>"),

    q(f"<p>{CHIGAINAI} otga qanday ulanadi?</p>",
      ["Yalangʻoch — hech qanday qoʻshimchasiz",
       "の bilan", "な bilan", "という bilan"],
      "Yalangʻoch — hech qanday qoʻshimchasiz",
      f"<p><strong>{GAKUSEICHIGAI}</strong>. Bu ulanish PJ-76 dagi "
      f"みたい bilan bir xil: feʼl, い-sifat, な-sifat va ot — "
      f"toʻrtalasi ham yalangʻoch ulanadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GAKUSEI}___"
      f"はずがありません</strong></p>",
      ["の", "hech nima", "な", "だ"],
      "の",
      f"<p><strong>{GAKUSEINOHAZUGANAI}</strong>. はず — haqiqiy ot, "
      f"shuning uchun ot undan oldin <strong>の</strong> ni oladi. "
      f"Bu yerda {CHIGAINAI} bilan farq qiladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GENKI}___"
      f"{r('違','ちが')}いありません</strong></p>",
      ["に", "なに", "のに", "だに"],
      "に",
      f"<p><strong>{GENKICHIGAI}</strong>. な-sifat ham yalangʻoch "
      f"ulanadi — はず ning な si bu yerga koʻchmaydi.</p>"),

    q(f"<p>{HAZUDATTA} — bu gap nima haqida?</p>",
      ["Amalga oshmagan reja", "Kelajakdagi reja",
       "Har kuni takrorlanadigan ish", "Birovdan eshitilgan xabar"],
      "Amalga oshmagan reja",
      f"<p><strong>Amalga oshmagan reja.</strong> «Uchda yetib "
      f"borishim kerak edi» — lekin boʻlmadi. のに afsusni "
      f"qoʻshadi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>ラノさんは{KYOU}{KYOUTO}にいます。ここにいる___。 — boʻsh "
      f"joyni toʻldiring.</p>",
      ["はずがありません", "はずです", "かもしれません", "でしょう"],
      "はずがありません",
      f"<p><strong>はずがありません</strong>. Birinchi gap dalil "
      f"beryapti — Rano Kiotoda. Demak bu yerda boʻlishi "
      f"<strong>imkonsiz</strong>, shunchaki «boʻlmasa kerak» "
      f"emas.</p>"),

    q(f"<p>{TSUKUE}の{r('上','うえ')}に{AKAI}{KASA}があります。"
      f"ムニラさんの{KASA}___。 — boʻsh joyni toʻldiring.</p>",
      [CHIGAIARIMASEN, "の" + CHIGAIARIMASEN,
       "な" + CHIGAIARIMASEN, "だ" + CHIGAIARIMASEN],
      CHIGAIARIMASEN,
      f"<p>Otdan keyin <strong>hech qanday qoʻshimcha yoʻq</strong>. "
      f"Soyabonni koʻrib turibmiz — dalil bor, shuning uchun "
      f"«shubhasiz» deyish oʻrinli.</p>"),

    q("<p>«Kelmasa kerak» — qaysi qolip?</p>",
      [KONAIHAZU, KURUHAZUGANAI, KURUCHIGAI, KAMOSHIRENAI],
      KONAIHAZU,
      f"<p><strong>{KONAIHAZU}</strong> — bu oddiy <em>kutish</em>: "
      f"asosim bor, lekin eshik ochiq. {KURUHAZUGANAI} esa "
      f"ehtimolni butunlay yopadi — «kelishi mumkin emas».</p>"),

    q(f"<p>{SANJI}に{TSUKU}はずでした___、{DENSHA}が{OKUREMASHITA}。 "
      f"— boʻsh joyga nima tushadi?</p>",
      ["が", "から", "ので", "と"],
      "が",
      f"<p><strong>が</strong> — PJ-54 dagi «lekin». Reja bor edi, "
      f"lekin amalga oshmadi. から va ので sabab beradi, bu yerda "
      f"esa qarama-qarshilik kerak.</p>"),

    q(f"<p>Doʻstingiz bilan gaplashganda «albatta keladi» ni qanday "
      f"aytasiz?</p>",
      [f"きっと{KURU}よ", f"{KURU}{CHIGAINAI}よ",
       f"{KURU}はずがないよ", f"{KURU}かもしれないよ"],
      f"きっと{KURU}よ",
      f"<p><strong>きっと{KURU}よ</strong>. {CHIGAINAI} kitobiy va "
      f"biroz dramatik — uni maqolada, kitobda, insholarda "
      f"ishlating. Suhbatda きっと tabiiyroq.</p>"),

    q(f"<p>{HANNIN}は{TANAKA}さん___。 — detektiv qahramoni qatʼiy "
      f"ishonch bilan gapiryapti. Boʻsh joyga nima tushadi?</p>",
      [CHIGAINAI, "の" + CHIGAINAI, "な" + CHIGAINAI,
       "という" + CHIGAINAI],
      CHIGAINAI,
      f"<p><strong>{TANAKA}さん{CHIGAINAI}</strong> — «shubhasiz "
      f"Tanaka». Ot yalangʻoch ulanadi. の qoʻshilsa, maʼno "
      f"«shubhasiz Tanakaniki» ga oʻzgaradi.</p>"),

    q(f"<p>«Qimmat boʻlishi mumkin emas» — qaysi biri toʻgʻri?</p>",
      [f"{TAKAI}はずがありません", f"{TAKAI}なはずがありません",
       f"{TAKAI}のはずがありません", f"{TAKAI}だはずがありません"],
      f"{TAKAI}はずがありません",
      f"<p>{TAKAI} — い-sifat, oddiy shakli oʻzi. な va の faqat "
      f"な-sifat bilan otga tegishli, だ esa PJ-79 dagi ということ "
      f"uchun.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>{KONAIHAZU} va {KURUHAZUGANAI} — farqi nimada?</p>",
      ["Birinchisi kutish, ikkinchisi ehtimolni butunlay rad etish",
       "Birinchisi oʻtgan zamon, ikkinchisi hozirgi zamon",
       "Birinchisi kitobiy, ikkinchisi kundalik",
       "Ikkalasi ham bir xil maʼno beradi"],
      "Birinchisi kutish, ikkinchisi ehtimolni butunlay rad etish",
      f"<p>Ikkalasi ham inkor tarafda, lekin kuchi boshqa. "
      f"<strong>{KONAIHAZU}</strong> — «kelmasa kerak», eshik "
      f"ochiq. <strong>{KURUHAZUGANAI}</strong> — «kelishi mumkin "
      f"emas», eshik yopiq.</p>"),

    q("<p>はずがない bilan わけがない orasidagi farq nimada?</p>",
      ["Maʼnosi deyarli bir xil; はずがない sovuqroq mantiq, "
       "わけがない kuchliroq va soʻzlashuvga yaqin",
       "はずがない inkor, わけがない tasdiq",
       "はずがない kelajak uchun, わけがない oʻtgan zamon uchun",
       "わけがない faqat otlar bilan ishlatiladi"],
      "Maʼnosi deyarli bir xil; はずがない sovuqroq mantiq, "
      "わけがない kuchliroq va soʻzlashuvga yaqin",
      f"<p>Koʻp joyda ikkalasi ham toʻgʻri. Farq ohangda: "
      f"はずがない dalilni koʻrsatib beradi, わけがない esa "
      f"«qanaqasiga!» degan hissiyotni olib yuradi.</p>"),

    q(f"<p>Quyidagilarni ishonch darajasi boʻyicha eng kuchsizdan "
      f"eng kuchligacha tartiblang.</p>",
      [f"{KAMOSHIRENAI} → {DESHOU} → {KURUHAZU} → {KURUCHIGAI}",
       f"{KURUHAZU} → {KAMOSHIRENAI} → {DESHOU} → {KURUCHIGAI}",
       f"{KURUCHIGAI} → {KURUHAZU} → {DESHOU} → {KAMOSHIRENAI}",
       f"{DESHOU} → {KAMOSHIRENAI} → {KURUCHIGAI} → {KURUHAZU}"],
      f"{KAMOSHIRENAI} → {DESHOU} → {KURUHAZU} → {KURUCHIGAI}",
      f"<p>かもしれません dalil kam boʻlganda, でしょう umumiy "
      f"taxmin, はずです asosim bor, {CHIGAINAI} esa eng kuchli. "
      f"Yapon tilida taxminni darajalab aytish odob hisoblanadi.</p>"),

    q(f"<p>Dalilingiz umuman boʻlmasa, qaysi qolipni tanlaysiz?</p>",
      [KAMOSHIRENAI, KURUCHIGAI, KURUHAZUGANAI, KURUHAZU],
      KAMOSHIRENAI,
      f"<p><strong>{KAMOSHIRENAI}</strong> — «kelishi mumkin». "
      f"Qolgan uchtasi dalil talab qiladi: はず asos, {CHIGAINAI} "
      f"kuchli dalil, はずがない esa ehtimolni rad etadigan "
      f"dalil.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gap toʻgʻri?</p>",
      [GAKUSEICHIGAI, GAKUSEI + "の" + CHIGAINAI,
       GAKUSEI + "な" + CHIGAINAI, GAKUSEI + "だ" + CHIGAINAI],
      GAKUSEICHIGAI,
      f"<p><strong>{GAKUSEICHIGAI}</strong>. {CHIGAINAI} otga "
      f"yalangʻoch ulanadi. の qoʻshilsa maʼno oʻzgaradi, な va だ "
      f"esa bu yerda umuman turmaydi.</p>"),

    q("<p>Qaysi gapda xato bor?</p>",
      [GAKUSEI + "はずがありません", GAKUSEINOHAZUGANAI,
       GENKI + "なはずがありません", GAKUSEICHIGAI],
      GAKUSEI + "はずがありません",
      f"<p>Birinchisi xato: はず oldida ot <strong>の</strong> ni "
      f"olishi shart — {GAKUSEINOHAZUGANAI}. Qolgan uchtasi "
      f"toʻgʻri.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q("<p>Soʻzlarni toʻgʻri tartibga qoʻying.</p>"
      f"<p><strong>{DENSHA}が{OKUREMASHITA} · {SANJI}に · "
      f"{TSUKU}はずだったのに · </strong></p>",
      [f"{SANJI}に{TSUKU}はずだったのに、{DENSHA}が{OKUREMASHITA}",
       f"{DENSHA}が{OKUREMASHITA}のに、{SANJI}に{TSUKU}はずだった",
       f"{TSUKU}はずだったのに{SANJI}に、{DENSHA}が{OKUREMASHITA}",
       f"{SANJI}に{DENSHA}が{OKUREMASHITA}、{TSUKU}はずだったのに"],
      f"{SANJI}に{TSUKU}はずだったのに、{DENSHA}が{OKUREMASHITA}",
      f"<p><strong>{SANJI}に{HAZUDATTA}、{DENSHA}が{OKUREMASHITA}</strong>. "
      f"Reja oldinda, uni buzgan voqea keyin. のに ikki qismni "
      f"bogʻlaydi va afsusni qoʻshadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>パリ: この{KASA}、"
      f"ムニラさんのでしょうか。</strong></p>"
      f"<p><strong>イノム: ___</strong></p>",
      [f"ムニラさんは{KYOU}{r('休','やす')}みですから、"
       f"ムニラさんのはずがありませんよ。",
       f"ムニラさんは{KYOU}{r('休','やす')}みですから、"
       f"ムニラさんはずがありませんよ。",
       f"ムニラさんは{KYOU}{r('休','やす')}みですから、"
       f"ムニラさんののはずがありませんよ。",
       f"ムニラさんは{KYOU}{r('休','やす')}みですから、"
       f"ムニラさんなはずがありませんよ。"],
      f"ムニラさんは{KYOU}{r('休','やす')}みですから、"
      f"ムニラさんのはずがありませんよ。",
      f"<p>Dalil から bilan berilgan — Munira bugun yoʻq. Shundan "
      f"keyin <strong>のはずがありません</strong> tabiiy chiqadi: "
      f"ot はず oldida bitta <strong>の</strong> oladi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-79 Mashq: 〜ということ va gapni otga aylantirish",
        "tutorial":    "PJ-79:",
        "description": "こと, の, という va ということ — toʻrtta asbob, "
                       "toʻrt xil ish. Ot va な-sifat だ bilan ulanadi.",
        "questions":   Q_PJ79,
        **DEFAULTS,
    },
    {
        "title":       "PJ-80 Mashq: 〜わけです va 〜わけではない",
        "tutorial":    "PJ-80:",
        "description": "わけ oilasining toʻrtta aʼzosi — va inkorning "
                       "joyi maʼnoni qanday oʻzgartirishi.",
        "questions":   Q_PJ80,
        **DEFAULTS,
    },
    {
        "title":       "PJ-81 Mashq: 〜はずがない va 〜に違いない",
        "tutorial":    "PJ-81:",
        "description": "Ishonch shkalasi: かもしれません dan "
                       "に違いない gacha, va はずがない bilan yopilgan eshik.",
        "questions":   Q_PJ81,
        **DEFAULTS,
    },
]
