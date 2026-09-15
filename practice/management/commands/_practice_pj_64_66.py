# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-64 … PJ-66.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batch kursdagi eng xavflisi: uchala dars ham BITTA あ-oʻzakdan
yasaladi va notoʻgʻri kalit soʻz emas, MAVJUD BOʻLMAGAN soʻz beradi.
Har bir shakl `verify_pj_64_66_forms.py` da kana jadvalidan qayta
hisoblanadi. Toʻrtta tuzoq:
    言う  → 言わ…   (あ emas, わ)
    来る  → こ…     (き emas)
    食べる → 食べさせる (せる emas, させる)
    話す  → qisqa kauzativ-passiv YOʻQ (話さされる — soʻz emas)

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_64_66.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "日本語",
    "description": "Yapon tili — grammatika va yozuv mashqlari",
    "icon":        "bi-brilliance",
    "color":       "#be123c",
}

DEFAULTS = {
    "level":                "medium",
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


# ── lugʻat shakllari ─────────────────────────────────────────────────
IKU     = r("行","い")+"く"
YOMU    = r("読","よ")+"む"
IU      = r("言","い")+"う"
MATSU   = r("待","ま")+"つ"
TSUKAU  = r("使","つか")+"う"
NOMU    = r("飲","の")+"む"
HANASU  = r("話","はな")+"す"
TABERU  = r("食","た")+"べる"
KURU    = r("来","く")+"る"
SURU    = "する"
FURU    = r("降","ふ")+"る"
NAKU    = r("泣","な")+"く"
FUMU    = r("踏","ふ")+"む"
NUSUMU  = r("盗","ぬす")+"む"
SHIKARU = r("叱","しか")+"る"
HOMERU  = r("褒","ほ")+"める"
RENSHUU_SURU = r("練習","れんしゅう")+"する"
YARU    = "やる"
KANGAERU = r("考","かんが")+"える"

# ── passiv ───────────────────────────────────────────────────────────
FURARETA   = r("降","ふ")+"られました"
KORARETA   = r("来","こ")+"られました"
NAKARETA   = r("泣","な")+"かれました"
FUMARETA   = r("踏","ふ")+"まれました"
NUSUMARETA = r("盗","ぬす")+"まれました"
TABERARETA = r("食","た")+"べられました"
SHIKARARETA = r("叱","しか")+"られました"
IWARERU    = r("言","い")+"われる"

# ── kauzativ ─────────────────────────────────────────────────────────
IKASERU     = r("行","い")+"かせる"
YOMASERU    = r("読","よ")+"ませる"
IWASERU     = r("言","い")+"わせる"
MATASERU    = r("待","ま")+"たせる"
TABESASERU  = r("食","た")+"べさせる"
KOSASERU    = r("来","こ")+"させる"
SASERU      = "させる"
IKASEMASHITA = r("行","い")+"かせました"
YOMASEMASHITA = r("読","よ")+"ませました"
IKASETEKURETA = r("行","い")+"かせてくれました"
YARASETE    = "やらせて"
KANGAESASETE = r("考","かんが")+"えさせて"

# ── kauzativ-passiv ──────────────────────────────────────────────────
IKASERARERU   = r("行","い")+"かせられる"
IKASARERU     = r("行","い")+"かされる"
YOMASERARERU  = r("読","よ")+"ませられる"
YOMASARERU    = r("読","よ")+"まされる"
HANASASERARERU = r("話","はな")+"させられる"
TABESASERARERU = r("食","た")+"べさせられる"
MATASARETA    = r("待","ま")+"たされました"
MATASERARETA  = r("待","ま")+"たせられました"
RENSHUU_SASERARETA = r("練習","れんしゅう")+"させられました"

# ── otlar ────────────────────────────────────────────────────────────
WATASHI = r("私","わたし")
AME     = r("雨","あめ")
HAHA    = r("母","はは")
OTOUTO  = r("弟","おとうと")
SENSEI  = r("先生","せんせい")
KODOMO  = r("子","こ")+"ども"
TOMODACHI = r("友","とも")+"だち"
GAKUSEI = r("学生","がくせい")
HON     = r("本","ほん")
KEEKI   = "ケーキ"
PIANO   = "ピアノ"
ASHI    = r("足","あし")
SAIFU   = r("財布","さいふ")
DENSHA  = r("電車","でんしゃ")
ICHIJIKAN = r("一時間","いちじかん")
MAINICHI = r("毎日","まいにち")
UKEMI   = r("受身","うけみ")
MEIWAKU = r("迷惑","めいわく")


# ══════════════════════════════════════════════════════════════════════
# PJ-64 — aziyat passivi
# ══════════════════════════════════════════════════════════════════════
Q_PJ64 = [
    # 1–5 tanish
    q(f"<p>«{AME}に{FURARETA}» ni tarjima qiling.</p>",
      ["Yomgʻirda qolib ketdim", "Yomgʻir yogʻdi",
       "Yomgʻirni yoqtiraman", "Yomgʻir toʻxtadi"],
      "Yomgʻirda qolib ketdim",
      f"<p>Soʻzma-soʻz «yomgʻir tomonidan yogʻildim». Bu "
      f"<strong>{MEIWAKU}の{UKEMI}</strong> — yomgʻir yogʻdi va "
      f"men shundan zarar koʻrdim.</p>"),

    q(f"<p>Aziyat passivida sababchi qaysi qoʻshimchani oladi?</p>",
      ["に", "が", "を", "で"],
      "に",
      f"<p>{AME}<strong>に</strong>{FURARETA}. Bu PJ-63 dagi "
      f"qoidaning oʻzi — passiv gapda qiluvchi doim に.</p>"),

    q(f"<p>Yaponchada oʻtimsiz feʼl passivga oʻta oladimi?</p>",
      ["Ha — va bu aynan aziyat passivi",
       "Yoʻq, hech qachon",
       "Faqat yozma tilda",
       "Faqat II guruh feʼllarida"],
      "Ha — va bu aynan aziyat passivi",
      f"<p>{FURU}, {NAKU}, {KURU} — hammasi oʻtimsiz, va hammasi "
      f"passivga oʻtadi. Oʻzbekchada bunday narsa yoʻq.</p>"),

    q(f"<p>«{KODOMO}に{NAKARETA}» ni tarjima qiling.</p>",
      ["Bola yigʻladi va menga xalaqit berdi",
       "Bolani yigʻlatdim", "Bola uchun yigʻladim",
       "Bola yigʻlamadi"],
      "Bola yigʻladi va menga xalaqit berdi",
      f"<p>Gapning egasi — <strong>men</strong>, garchi men hech "
      f"nima qilmagan boʻlsam ham. Mavzu ish emas, uning menga "
      f"tegishi.</p>"),

    q(f"<p>Bu shakl qanday ohang bildiradi?</p>",
      ["Doim norozilik", "Doim minnatdorchilik",
       "Betaraf", "Hurmat"],
      "Doim norozilik",
      f"<p>Shuning uchun uning nomi <strong>{MEIWAKU}の{UKEMI}</strong> "
      f"— «tashvish passivi».</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{WATASHI}は{OTOUTO}に{KEEKI}を{TABERARETA}» — nega を "
      f"qolgan?</p>",
      ["Chunki gapning egasi tort emas, men",
       f"Chunki ケーキ katakana bilan yozilgan",
       f"Chunki {TABERU} II guruh feʼli",
       "Chunki gap oʻtgan zamonda"],
      "Chunki gapning egasi tort emas, men",
      f"<p>Egasi <strong>odam</strong> boʻlsa, gap shikoyatga "
      f"aylanadi. «ケーキは…{TABERARETA}» boʻlsa shunchaki fakt "
      f"boʻlardi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{DENSHA}で{ASHI}を"
      f"___。</strong></p>",
      [FUMARETA, f"{r('踏','ふ')}みました", f"{r('踏','ふ')}まられました",
       f"{r('踏','ふ')}めました"],
      FUMARETA,
      f"<p>«Oyogʻimni bosib ketishdi». Kim bosgani aytilmagan — "
      f"muhimi, <strong>menga</strong> tegdi.</p>"),

    q(f"<p>«{TOMODACHI}に___» — «doʻstim keldi va ishim buzildi» "
      f"degan maʼnoni bering.</p>",
      [KORARETA, f"{r('来','き')}られました", f"{r('来','き')}ました",
       f"{r('来','こ')}させました"],
      KORARETA,
      f"<p>{KURU} ning ない-oʻzagi <strong>こ</strong> (PJ-63). "
      f"«{r('来','き')}られました» degan shakl yoʻq.</p>"),

    q(f"<p>Gap aziyat passivi ekanini qanday bilasiz?</p>",
      ["Tarjimada «-ib qoʻydi» yoki «-ib ketdi» qoʻshgingiz kelsa",
       "Feʼl II guruhga tegishli boʻlsa",
       "Gap oʻtgan zamonda boʻlsa",
       "Ega jonsiz narsa boʻlsa"],
      "Tarjimada «-ib qoʻydi» yoki «-ib ketdi» qoʻshgingiz kelsa",
      f"<p>Yana uchta belgi: ega odam, を qolgan, feʼl oʻtimsiz "
      f"boʻlishi mumkin.</p>"),

    q(f"<p>Oʻzbekchada shikoyat qayerda turadi?</p>",
      ["Yordamchi feʼlda — «-ib qoʻydi»",
       "Passivda", "Qoʻshimchada", "Gap boshida"],
      "Yordamchi feʼlda — «-ib qoʻydi»",
      f"<p>«Ukam tortimni yeb <strong>qoʻydi</strong>» — bu PJ-58 "
      f"dagi 〜てしまう ga toʻgʻri keladi. Yaponcha esa shikoyatni "
      f"<strong>passivga</strong> yashiradi.</p>"),

    q(f"<p>«{SAIFU}を{NUSUMARETA}» ni tarjima qiling.</p>",
      ["Hamyonimni oʻgʻirlab ketishdi", "Hamyonni oʻgʻirladim",
       "Hamyonim topildi", "Hamyonni berdim"],
      "Hamyonimni oʻgʻirlab ketishdi",
      f"<p>Yana を qolgan, chunki zarar koʻrgan — men.</p>"),

    q(f"<p>Nega yaponchada bu shakl kerak?</p>",
      ["Chunki yapon tili gapning mavzusini oʻzgartirmaslikni yaxshi koʻradi",
       "Chunki passiv muloyimroq",
       "Chunki oʻtimsiz feʼllar kam",
       "Chunki oddiy gap qiyin"],
      "Chunki yapon tili gapning mavzusini oʻzgartirmaslikni yaxshi koʻradi",
      f"<p>Hikoya siz haqingizda ketayotgan boʻlsa, hatto yomgʻir "
      f"haqidagi gap ham sizdan boshlanishi kerak.</p>"),

    # 13–16 farqlash
    q(f"<p>Oddiy passiv va aziyat passivi — asosiy farqi nima?</p>",
      ["Aziyat passivida ega deyarli doim odam va ohang salbiy",
       "Aziyat passivi faqat oʻtgan zamonda",
       "Oddiy passiv faqat yozma tilda",
       "Farqi yoʻq"],
      "Aziyat passivida ega deyarli doim odam va ohang salbiy",
      f"<p>Yana ikkita belgi: oʻtimsiz feʼl ham boʻlishi mumkin, "
      f"va を koʻpincha qoladi.</p>"),

    q(f"<p>«{AME}が{r('降','ふ')}りました» va «{AME}に{FURARETA}» — "
      f"farqi nima?</p>",
      ["Birinchisi betaraf fakt, ikkinchisida norozilik bor",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Birinchisi kelasi zamon",
       "Farqi yoʻq"],
      "Birinchisi betaraf fakt, ikkinchisida norozilik bor",
      f"<p>Yaxshi yomgʻir haqida gapirsangiz oddiy "
      f"{r('降','ふ')}りました ishlating.</p>"),

    q(f"<p>«ケーキは{OTOUTO}に{TABERARETA}» — bu shikoyatmi?</p>",
      ["Yoʻq — ega tort, demak bu shunchaki fakt",
       "Ha, doim shikoyat",
       f"Ha, chunki {OTOUTO} に bilan turibdi",
       "Bu notoʻgʻri gap"],
      "Yoʻq — ega tort, demak bu shunchaki fakt",
      f"<p>Shikoyat uchun ega <strong>odam</strong> boʻlishi "
      f"kerak: {WATASHI}は{OTOUTO}に{KEEKI}を{TABERARETA}.</p>"),

    q(f"<p>Qaysi feʼl aziyat passiviga eng koʻp uchraydi?</p>",
      [NAKU, HOMERU, TABERU, r("建","た")+"てる"],
      NAKU,
      f"<p>{NAKU}, {FURU}, {KURU}, {r('死','し')}ぬ — oʻtimsiz va "
      f"yoqimsiz. {HOMERU} esa oddiy passivning feʼli.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{AME}が{FURARETA}", f"{AME}に{FURARETA}",
       f"{KODOMO}に{NAKARETA}", f"{TOMODACHI}に{KORARETA}"],
      f"{AME}が{FURARETA}",
      f"<p>Sababchi doim <strong>に</strong> oladi, が emas.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WATASHI}は{OTOUTO}に{KEEKI}を{TABERARETA}",
       f"{WATASHI}は{OTOUTO}が{KEEKI}を{TABERARETA}",
       f"{WATASHI}を{OTOUTO}に{KEEKI}が{TABERARETA}",
       f"{WATASHI}は{OTOUTO}に{KEEKI}が{TABERARETA}"],
      f"{WATASHI}は{OTOUTO}に{KEEKI}を{TABERARETA}",
      f"<p>Zarar koʻrgan は, sababchi に, buyum esa "
      f"<strong>を</strong> — u oʻz joyida qoladi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{FURARETA} · {AME}に · {r('昨日','きのう')}</strong></p>",
      [f"{r('昨日','きのう')}{AME}に{FURARETA}",
       f"{AME}に{r('昨日','きのう')}{FURARETA}",
       f"{FURARETA}{r('昨日','きのう')}{AME}に",
       f"{r('昨日','きのう')}{FURARETA}{AME}に"],
      f"{r('昨日','きのう')}{AME}に{FURARETA}",
      f"<p>Vaqt — sababchi に — passiv feʼl. Yapon gapi doim feʼl "
      f"bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> どうして{r('濡','ぬ')}れていますか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{AME}に{FURARETA}。", f"{AME}が{FURARETA}。",
       f"{AME}を{FURARETA}。", f"{AME}に{r('降','ふ')}りました。"],
      f"{AME}に{FURARETA}。",
      f"<p>«Yomgʻirda qolib ketdim» — sababchi <strong>に</strong>, "
      f"va feʼl passivda.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-65 — kauzativ
# ══════════════════════════════════════════════════════════════════════
Q_PJ65 = [
    # 1–5 tanish
    q(f"<p>Kauzativ qaysi oʻzakdan yasaladi?</p>",
      ["ない-oʻzagidan — passiv bilan bir xil", "て-shaklidan",
       "た-shaklidan", "Lugʻat shaklidan"],
      "ない-oʻzagidan — passiv bilan bir xil",
      f"<p>Faqat れる oʻrniga <strong>せる</strong> qoʻyiladi: "
      f"{r('読','よ')}まれる → {YOMASERU}.</p>"),

    q(f"<p>{IKU} ning kauzativ shakli qaysi?</p>",
      [IKASERU, f"{r('行','い')}きせる", f"{IKU}せる",
       f"{r('行','い')}かさせる"],
      IKASERU,
      f"<p>あ-qatorga tushadi, keyin <strong>せる</strong>.</p>"),

    q(f"<p>{TABERU} ning kauzativ shakli qaysi?</p>",
      [TABESASERU, f"{r('食','た')}べせる", f"{TABERU}させる",
       f"{r('食','た')}べらせる"],
      TABESASERU,
      f"<p>II guruh <strong>させる</strong> oladi, せる emas.</p>"),

    q(f"<p>{IU} ning kauzativ shakli qaysi?</p>",
      [IWASERU, f"{r('言','い')}あせる", f"{r('言','い')}いせる",
       f"{IU}させる"],
      IWASERU,
      f"<p>Yana <strong>わ</strong> — uchinchi marta: ない-shaklida, "
      f"passivda va bugun kauzativda. Oʻzak bitta boʻlgani uchun "
      f"istisno ham bitta.</p>"),

    q(f"<p>{KURU} ning kauzativ shakli qaysi?</p>",
      [KOSASERU, f"{r('来','き')}させる", f"{KURU}させる",
       f"{r('来','こ')}せる"],
      KOSASERU,
      f"<p>ない-oʻzagi <strong>こ</strong>, xuddi passivdagi "
      f"kabi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Kauzativning ikki maʼnosi qaysilar?</p>",
      ["Majbur qilish va ruxsat berish", "Majbur qilish va taqiqlash",
       "Ruxsat berish va soʻrash", "Qilmoq va qilmaslik"],
      "Majbur qilish va ruxsat berish",
      f"<p>Bitta shakl ikki maʼnoni koʻtaradi. Kontekst va "
      f"qoʻshimchalar ajratadi.</p>"),

    q(f"<p>«{HAHA}は{WATASHI}を{IKASETEKURETA}» — bu majburmi yoki "
      f"ruxsatmi?</p>",
      ["Ruxsat — くれる yaxshilikni bildiradi",
       "Majbur", "Ikkalasi ham boʻlishi mumkin",
       "Bu notoʻgʻri gap"],
      "Ruxsat — くれる yaxshilikni bildiradi",
      f"<p>Majburlash yaxshilik boʻlmaydi, shuning uchun "
      f"<strong>〜させてくれました</strong> deyarli doim "
      f"«ruxsat berdi».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENSEI}は{GAKUSEI}"
      f"___{HON}を{YOMASEMASHITA}。</strong></p>",
      ["に", "を", "が", "で"],
      "に",
      f"<p>Oʻtimli feʼlda を band ({HON}を), shuning uchun odam "
      f"faqat <strong>に</strong> qola oladi. Bitta gapda ikkita "
      f"を boʻlmaydi.</p>"),

    q(f"<p>«{KODOMO}を{IKASERU}» va «{KODOMO}に{IKASERU}» — farqi "
      f"nima?</p>",
      ["を majburlash ohangini, に ruxsat ohangini beradi",
       "を rasmiy, に oddiy",
       "を oʻtgan zamon, に hozirgi",
       "Farqi yoʻq"],
      "を majburlash ohangini, に ruxsat ohangini beradi",
      f"<p>Bu faqat oʻtimsiz feʼllarda ishlaydi — oʻtimli feʼlda "
      f"odam doim に oladi.</p>"),

    q(f"<p>«Menga qilishga ruxsat bering» ni yozing.</p>",
      [f"{WATASHI}に{YARASETE}ください", f"{WATASHI}に{YARU}ください",
       f"{WATASHI}を{YARASETE}ください", f"{WATASHI}にやられてください"],
      f"{WATASHI}に{YARASETE}ください",
      f"<p>Kauzativning て-shakli + ください. Yaponchada ruxsat "
      f"soʻrashning asosiy yoʻli shu.</p>"),

    q(f"<p>«{r('少','すこ')}し{KANGAESASETE}ください» ni tarjima "
      f"qiling.</p>",
      ["Biroz oʻylab koʻray", "Biroz oʻylab koʻring",
       "Menga aytib bering", "Oʻylamang"],
      "Biroz oʻylab koʻray",
      f"<p>Yaponchada «oʻylayman» deyish oʻrniga koʻpincha "
      f"«oʻylashimga ruxsat bering» deyiladi — bu ancha "
      f"muloyim.</p>"),

    q(f"<p>Oʻzbekchada bu qoʻshimcha qanday koʻrinadi?</p>",
      ["«-tir- / -dir-» — oʻqi-t-dim, kul-dir-dim",
       "«-ib bermoq»", "«-ib qoʻymoq»", "«-sa ham»"],
      "«-tir- / -dir-» — oʻqi-t-dim, kul-dir-dim",
      f"<p>Yaʼni bu dars yangi <strong>fikr</strong> emas — faqat "
      f"yangi qoʻshimcha.</p>"),

    # 13–16 farqlash
    q(f"<p>«{r('読','よ')}まれる» va «{YOMASERU}» — farqi nima?</p>",
      ["Birinchisi passiv, ikkinchisi kauzativ",
       "Birinchisi kauzativ, ikkinchisi passiv",
       "Ikkalasi ham passiv", "Ikkalasi ham kauzativ"],
      "Birinchisi passiv, ikkinchisi kauzativ",
      f"<p>Bitta oʻzak ({r('読','よ')}ま), ikki qoʻshimcha: "
      f"<strong>れる</strong> — passiv, <strong>せる</strong> — "
      f"kauzativ.</p>"),

    q(f"<p>Muloyimroq ruxsat soʻrash shakli qaysi?</p>",
      ["〜させていただけますか", "〜させてください",
       "〜させます", "〜させました"],
      "〜させていただけますか",
      f"<p>PJ-61 dagi zinapoyaning oʻzi: gap uzaygan sari "
      f"muloyimlashadi.</p>"),

    q(f"<p>Nega oʻtimli feʼlda odam doim に oladi?</p>",
      ["Chunki を allaqachon band — bitta gapda ikkita を boʻlmaydi",
       "Chunki odam har doim に oladi",
       "Chunki oʻtimli feʼllar を olmaydi",
       "Chunki bu muloyimroq"],
      "Chunki を allaqachon band — bitta gapda ikkita を boʻlmaydi",
      f"<p>Bu yapon tilining qatʼiy qoidasi.</p>"),

    q(f"<p>{HANASU} ning kauzativ shakli qaysi?</p>",
      [f"{r('話','はな')}させる", f"{r('話','はな')}さされる",
       f"{r('話','はな')}しせる", f"{HANASU}せる"],
      f"{r('話','はな')}させる",
      f"<p>す ning あ-qatordagi bogʻini <strong>さ</strong>, "
      f"demak {r('話','はな')}さ + せる.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TABERU} → {r('食','た')}べせる", f"{IKU} → {IKASERU}",
       f"{YOMU} → {YOMASERU}", f"{IU} → {IWASERU}"],
      f"{TABERU} → {r('食','た')}べせる",
      f"<p>Toʻgʻrisi — <strong>{TABESASERU}</strong>. II guruh "
      f"させる oladi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{KODOMO}に{HON}を{YOMASEMASHITA}",
       f"{KODOMO}を{HON}を{YOMASEMASHITA}",
       f"{KODOMO}が{HON}を{YOMASEMASHITA}",
       f"{KODOMO}に{HON}に{YOMASEMASHITA}"],
      f"{KODOMO}に{HON}を{YOMASEMASHITA}",
      f"<p>Oʻtimli feʼl: buyum を, odam <strong>に</strong>.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{YOMASEMASHITA} · {HON}を · {GAKUSEI}に · "
      f"{SENSEI}は</strong></p>",
      [f"{SENSEI}は{GAKUSEI}に{HON}を{YOMASEMASHITA}",
       f"{GAKUSEI}に{SENSEI}は{HON}を{YOMASEMASHITA}",
       f"{HON}を{SENSEI}は{GAKUSEI}に{YOMASEMASHITA}",
       f"{SENSEI}は{HON}を{YOMASEMASHITA}{GAKUSEI}に"],
      f"{SENSEI}は{GAKUSEI}に{HON}を{YOMASEMASHITA}",
      f"<p>Kim — kimga — nima — feʼl.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>せんせい:</strong> だれがやりますか。</p>"
      f"<p><strong>ラノ:</strong> ___</p>",
      [f"{WATASHI}に{YARASETE}ください。", f"{WATASHI}が{YARU}ください。",
       f"{WATASHI}に{YARU}せてください。", f"{WATASHI}を{YARASETE}います。"],
      f"{WATASHI}に{YARASETE}ください。",
      f"<p>«Buni men qilay» — yaponchada «qilaman» deyish qoʻpol, "
      f"«qilishimga ruxsat bering» esa tabiiy.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-66 — kauzativ-passiv
# ══════════════════════════════════════════════════════════════════════
Q_PJ66 = [
    # 1–5 tanish
    q(f"<p>Kauzativ-passiv qanday yasaladi?</p>",
      ["Kauzativ yasaladi, keyin unga II guruh passivi qoʻshiladi",
       "Passiv yasaladi, keyin kauzativ qoʻshiladi",
       "ない-oʻzagiga される qoʻshiladi",
       "て-shakliga られる qoʻshiladi"],
      "Kauzativ yasaladi, keyin unga II guruh passivi qoʻshiladi",
      f"<p>{IKU} → {IKASERU} (endi II guruh feʼli) → "
      f"<strong>{IKASERARERU}</strong>. Yangi qoida yoʻq.</p>"),

    q(f"<p>{YOMU} ning kauzativ-passiv shakli qaysi?</p>",
      [YOMASERARERU, f"{r('読','よ')}まれさせる",
       f"{r('読','よ')}ませる", f"{r('読','よ')}まされせる"],
      YOMASERARERU,
      f"<p>Kauzativ {YOMASERU}, unga られる: {YOMASERARERU}. "
      f"Qisqa shakli — <strong>{YOMASARERU}</strong>.</p>"),

    q(f"<p>{IKU} ning qisqa kauzativ-passiv shakli qaysi?</p>",
      [IKASARERU, f"{r('行','い')}かせされる", f"{r('行','い')}かれる",
       f"{r('行','い')}かせる"],
      IKASARERU,
      f"<p>〜せられる → <strong>〜される</strong>. Bu qisqarish "
      f"faqat I guruhda ishlaydi.</p>"),

    q(f"<p>{HANASU} ning qisqa kauzativ-passiv shakli bormi?</p>",
      [f"Yoʻq — «{r('話','はな')}さされる» ikkita さ beradi",
       f"Ha — {r('話','はな')}さされる", f"Ha — {r('話','はな')}される",
       f"Ha — {r('話','はな')}させる"],
      f"Yoʻq — «{r('話','はな')}さされる» ikkita さ beradi",
      f"<p>Yapon tili buni qabul qilmaydi. す bilan tugagan "
      f"feʼllar faqat uzun shaklni ishlatadi: "
      f"<strong>{HANASASERARERU}</strong>.</p>"),

    q(f"<p>Bu shakl qanday ohang bildiradi?</p>",
      ["Doim salbiy — «majburan»", "Doim ijobiy",
       "Betaraf", "Hurmat"],
      "Doim salbiy — «majburan»",
      f"<p>Uni ishlatgan odam ishni yoqtirmaganini aytadi — hatto "
      f"gapda boshqa hech qanday belgi boʻlmasa ham.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{MAINICHI}{PIANO}を{RENSHUU_SASERARETA}» ni tarjima "
      f"qiling.</p>",
      ["Har kuni pianino mashq qildirishardi",
       "Har kuni pianino mashq qilardim",
       "Har kuni pianino mashq qilishga ruxsat berishardi",
       "Har kuni pianino mashq qilmasdim"],
      "Har kuni pianino mashq qildirishardi",
      f"<p>Gapda «yoqmasdi» degan soʻz yoʻq — u "
      f"<strong>feʼlning ichida</strong>.</p>"),

    q(f"<p>«{ICHIJIKAN}{MATASARETA}» va «{ICHIJIKAN}"
      f"{r('待','ま')}ちました» — farqi nima?</p>",
      ["Birinchisida norozilik bor — «kuttirishdi»",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Birinchisi kelasi zamon",
       "Farqi yoʻq"],
      "Birinchisida norozilik bor — «kuttirishdi»",
      f"<p>Ikkinchisi betaraf — «kutdim». Qisqa shakl "
      f"{MATASARETA} I guruh feʼli boʻlgani uchun mumkin.</p>"),

    q(f"<p>Majburlagan odam qaysi qoʻshimchani oladi?</p>",
      ["に", "が", "を", "で"],
      "に",
      f"<p>{WATASHI}は{HAHA}<strong>に</strong>{PIANO}を"
      f"{RENSHUU_SASERARETA}. Bu PJ-63, PJ-64 va bugun — uchinchi "
      f"marta bir xil qoida.</p>"),

    q(f"<p>{TABERU} ning kauzativ-passiv shakli qaysi?</p>",
      [TABESASERARERU, f"{r('食','た')}べさされる",
       f"{r('食','た')}べされる", f"{r('食','た')}べらされる"],
      TABESASERARERU,
      f"<p>II guruhda qisqa shakl <strong>yoʻq</strong>. Kauzativ "
      f"{TABESASERU}, unga られる.</p>"),

    q(f"<p>Qisqa shakl qaysi feʼllarda ishlaydi?</p>",
      ["Faqat I guruhda, va す bilan tugamaydiganlarda",
       "Hamma feʼllarda", "Faqat II guruhda",
       "Faqat III guruhda"],
      "Faqat I guruhda, va す bilan tugamaydiganlarda",
      f"<p>{IKASARERU} ✓ · {YOMASARERU} ✓ · "
      f"«{r('話','はな')}さされる» ✗ · «{r('食','た')}べさされる» ✗.</p>"),

    q(f"<p>«{IKASERARERU}» va «{r('行','い')}かせてくれました» — farqi "
      f"nima?</p>",
      ["Birinchisi majburlash, ikkinchisi ruxsat",
       "Birinchisi ruxsat, ikkinchisi majburlash",
       "Ikkalasi ham majburlash",
       "Ikkalasi ham ruxsat"],
      "Birinchisi majburlash, ikkinchisi ruxsat",
      f"<p>Kauzativ-passiv <strong>doim salbiy</strong>. Ruxsat "
      f"uchun PJ-65 dagi 〜させてくれる.</p>"),

    q(f"<p>Bu uch dars qaysi oʻzakdan boshlanadi?</p>",
      ["ない-oʻzagidan (PJ-34)", "て-shaklidan",
       "た-shaklidan", "ます-oʻzagidan"],
      "ない-oʻzagidan (PJ-34)",
      f"<p>{r('行','い')}か + れる · せる · せられる — uchalasi ham "
      f"oʻsha <strong>{r('行','い')}か</strong> dan.</p>"),

    # 13–16 farqlash
    q(f"<p>«{r('褒','ほ')}められました» va «{RENSHUU_SASERARETA}» — "
      f"ohangi bir xilmi?</p>",
      ["Yoʻq — birinchisi ijobiy boʻlishi mumkin, ikkinchisi doim salbiy",
       "Ha, ikkalasi ham salbiy",
       "Ha, ikkalasi ham betaraf",
       "Yoʻq — birinchisi doim salbiy, ikkinchisi betaraf"],
      "Yoʻq — birinchisi ijobiy boʻlishi mumkin, ikkinchisi doim salbiy",
      f"<p>Oddiy passiv betaraf yoki ijobiy boʻlishi mumkin "
      f"(«maqtaldim»). Kauzativ-passiv esa <strong>hech "
      f"qachon</strong> ijobiy boʻlmaydi.</p>"),

    q(f"<p>Qisqa shakl va uzun shakl — qaysi birini yozasiz?</p>",
      ["Ikkalasi ham toʻgʻri; qisqasi ogʻzaki, uzuni yozma",
       "Faqat qisqa shakl",
       "Faqat uzun shakl",
       "Qisqa shakl har doim xato"],
      "Ikkalasi ham toʻgʻri; qisqasi ogʻzaki, uzuni yozma",
      f"<p>Lekin <strong>す</strong> bilan tugagan feʼlda qisqa "
      f"shakl xato.</p>"),

    q(f"<p>Nega kauzativ natijasi II guruh feʼli boʻlib qoladi?</p>",
      ["Chunki u せる / させる bilan tugaydi — る bilan",
       "Chunki u uzun",
       "Chunki kauzativ doim II guruh",
       "Chunki passiv II guruh"],
      "Chunki u せる / させる bilan tugaydi — る bilan",
      f"<p>Shuning uchun unga II guruh passivi — "
      f"<strong>られる</strong> — qoʻshiladi.</p>"),

    q(f"<p>{MATSU} ning kauzativ-passiv uzun shakli qaysi?</p>",
      [MATASERARETA, f"{r('待','ま')}たれられました",
       f"{r('待','ま')}ちさせられました", f"{r('待','ま')}たせました"],
      MATASERARETA,
      f"<p>Kauzativ {MATASERU}, unga られる → "
      f"{MATASERARETA}. Qisqa shakli — {MATASARETA}.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi shakl mavjud EMAS?</p>",
      [f"{r('話','はな')}さされる", HANASASERARERU,
       IKASARERU, TABESASERARERU],
      f"{r('話','はな')}さされる",
      f"<p>Ikkita さ ketma-ket — yapon tili buni qabul qilmaydi. "
      f"す bilan tugagan feʼlda faqat uzun shakl.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WATASHI}は{HAHA}に{PIANO}を{RENSHUU_SASERARETA}",
       f"{WATASHI}は{HAHA}が{PIANO}を{RENSHUU_SASERARETA}",
       f"{WATASHI}を{HAHA}に{PIANO}が{RENSHUU_SASERARETA}",
       f"{WATASHI}は{HAHA}で{PIANO}を{RENSHUU_SASERARETA}"],
      f"{WATASHI}は{HAHA}に{PIANO}を{RENSHUU_SASERARETA}",
      f"<p>Majburlangan は, majburlagan <strong>に</strong>, "
      f"buyum を.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{RENSHUU_SASERARETA} · {PIANO}を · {HAHA}に · "
      f"{MAINICHI}</strong></p>",
      [f"{MAINICHI}{HAHA}に{PIANO}を{RENSHUU_SASERARETA}",
       f"{HAHA}に{MAINICHI}{PIANO}を{RENSHUU_SASERARETA}",
       f"{PIANO}を{MAINICHI}{HAHA}に{RENSHUU_SASERARETA}",
       f"{MAINICHI}{PIANO}を{RENSHUU_SASERARETA}{HAHA}に"],
      f"{MAINICHI}{HAHA}に{PIANO}を{RENSHUU_SASERARETA}",
      f"<p>Vaqt — majburlagan odam に — buyum を — feʼl.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> {PIANO}が{r('上手','じょうず')}ですね。</p>"
      f"<p><strong>ラノ:</strong> ___</p>",
      [f"{r('子','こ')}どものとき、{MAINICHI}{RENSHUU_SASERARETA}。",
       f"{r('子','こ')}どものとき、{MAINICHI}{r('練習','れんしゅう')}させました。",
       f"{r('子','こ')}どものとき、{MAINICHI}{r('練習','れんしゅう')}されました。",
       f"{r('子','こ')}どものとき、{MAINICHI}{r('練習','れんしゅう')}させてくれました。"],
      f"{r('子','こ')}どものとき、{MAINICHI}{RENSHUU_SASERARETA}。",
      f"<p>«Majbur qilishardi» — kauzativ-passiv. "
      f"<strong>{r('練習','れんしゅう')}させました</strong> «men boshqaga "
      f"qildirdim» degani; <strong>{r('練習','れんしゅう')}させてくれました</strong> "
      f"esa «ruxsat berishdi».</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-64 Mashq: Aziyat passivi (迷惑の受身)",
        "tutorial":    "PJ-64:",
        "description": "Oʻtimsiz feʼl ham passivga oʻtadi. Ega — zarar "
                       "koʻrgan odam, va を koʻpincha qoladi.",
        "questions":   Q_PJ64,
        **DEFAULTS,
    },
    {
        "title":       "PJ-65 Mashq: Kauzativ (使役)",
        "tutorial":    "PJ-65:",
        "description": "ない-oʻzagi + せる / させる. Majbur yoki ruxsat — "
                       "を va に hal qiladi.",
        "questions":   Q_PJ65,
        **DEFAULTS,
    },
    {
        "title":       "PJ-66 Mashq: Kauzativ-passiv (使役受身)",
        "tutorial":    "PJ-66:",
        "description": "Kauzativ + passiv. Qisqa shakl faqat I guruhda, "
                       "す dan tashqari. Maʼnosi doim salbiy.",
        "questions":   Q_PJ66,
        **DEFAULTS,
    },
]
