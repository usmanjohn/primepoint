# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-61 … PJ-63.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Uch narsa jim sinadi:
  * PJ-61 — yoʻnalish (yana), lekin endi て-shakli ustida;
  * PJ-62 — はず ot boʻlgani uchun undan oldin な / の;
  * PJ-63 — PASSIV SHAKLI. Bu batchning eng xavfli joyi: 言う → 言われる
    (あ emas, わ), 来る → 来られる (き emas, こ), 食べる → 食べられる
    (べれる emas). Har bir kalit `verify_pj_61_63_forms.py` da ない-oʻzagidan
    qayta hisoblanadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_61_63.py --master=prime \\
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


# ── feʼllar: lugʻat · て-shakli ───────────────────────────────────────
OSHIERU,  OSHIETE  = r("教","おし")+"える",  r("教","おし")+"えて"
TETSUDAU, TETSUDATTE = r("手伝","てつだ")+"う", r("手伝","てつだ")+"って"
YOMU,     YONDE    = r("読","よ")+"む",      r("読","よ")+"んで"
KAKU,     KAITE    = r("書","か")+"く",      r("書","か")+"いて"
IU                 = r("言","い")+"う"
KURU               = r("来","く")+"る"
KIMASU             = r("来","き")+"ます"
TABERU             = r("食","た")+"べる"
HOMERU             = r("褒","ほ")+"める"
SHIKARU            = r("叱","しか")+"る"
YOBU               = r("呼","よ")+"ぶ"
TATERU             = r("建","た")+"てる"
ERABU              = r("選","えら")+"ぶ"
TSUKAU             = r("使","つか")+"う"
TSUKURU            = r("作","つく")+"る"
KASU,     KASHITE  = r("貸","か")+"す",      r("貸","か")+"して"
NAOSU              = r("直","なお")+"す"
FURU               = r("降","ふ")+"る"
HARERU             = r("晴","は")+"れる"
IRU                = "いる"

# ── passiv shakllari ─────────────────────────────────────────────────
YOMARERU   = r("読","よ")+"まれる"
KAKARERU   = r("書","か")+"かれる"
IWARERU    = r("言","い")+"われる"
TSUKURARERU = r("作","つく")+"られる"
TSUKAWARERU = r("使","つか")+"われる"
HOMERARERU = r("褒","ほ")+"められる"
HOMERARETA = r("褒","ほ")+"められました"
SHIKARARETA = r("叱","しか")+"られました"
YOBARETA   = r("呼","よ")+"ばれました"
TATERARETA = r("建","た")+"てられました"
ERABARETA  = r("選","えら")+"ばれました"
KORARERU   = r("来","こ")+"られる"
SARERU     = "される"
TABERARERU = r("食","た")+"べられる"
TABERARETA = r("食","た")+"べられました"

# ── yordamchi qoliplar ───────────────────────────────────────────────
KURETA     = "くれました"
AGETA      = "あげました"
MORATTA    = "もらいました"
MORAEMASUKA = "もらえますか"
ITADAKEMASUKA = "いただけますか"
MASHOUKA   = "ましょうか"

# ── otlar va sifatlar ────────────────────────────────────────────────
WATASHI  = r("私","わたし")
TOMODACHI = r("友","とも")+"だち"
SENSEI   = r("先生","せんせい")
OTOUTO   = r("弟","おとうと")
HAHA     = r("母","はは")
NIHONGO  = r("日本語","にほんご")
HON      = r("本","ほん")
NAMAE    = r("名前","なまえ")
KYOUSHITSU = r("教室","きょうしつ")
AMEK     = r("雨","あめ")
SAMUI    = r("寒","さむ")+"い"
SHIZUKA  = r("静","しず")+"か"
GAKUSEI  = r("学生","がくせい")
ASHITA   = r("明日","あした")
TOSHOKAN = r("図書館","としょかん")
KEEKI    = "ケーキ"
SASHIMI  = "さしみ"


# ══════════════════════════════════════════════════════════════════════
# PJ-61 — 〜てあげる / 〜てくれる / 〜てもらう
# ══════════════════════════════════════════════════════════════════════
Q_PJ61 = [
    # 1–5 tanish
    q(f"<p>Uchala qolip ham qaysi shaklga qoʻshiladi?</p>",
      ["て-shakliga", "Lugʻat shakliga", "た-shakliga", "ない-shakliga"],
      "て-shakliga",
      f"<p>PJ-60 da narsa berilgan edi, bugun <strong>ish</strong> "
      f"beriladi — va ish て-shakli bilan koʻrsatiladi.</p>"),

    q(f"<p>«Doʻstim menga yapon tilini oʻrgatib berdi» — qaysi feʼl?</p>",
      [f"{OSHIETE}{KURETA}", f"{OSHIETE}{AGETA}", f"{OSHIETE}{MORATTA}",
       f"{OSHIERU}{KURETA}"],
      f"{OSHIETE}{KURETA}",
      f"<p>Yaxshilik <strong>menga kelyapti</strong>, demak "
      f"くれる. Ega — doʻstim.</p>"),

    q(f"<p>Oʻsha voqeani «{WATASHI}» ni ega qilib ayting.</p>",
      [f"{WATASHI}は{TOMODACHI}に{NIHONGO}を{OSHIETE}{MORATTA}",
       f"{WATASHI}は{TOMODACHI}に{NIHONGO}を{OSHIETE}{KURETA}",
       f"{WATASHI}は{TOMODACHI}に{NIHONGO}を{OSHIETE}{AGETA}",
       f"{TOMODACHI}は{WATASHI}に{NIHONGO}を{OSHIETE}{MORATTA}"],
      f"{WATASHI}は{TOMODACHI}に{NIHONGO}を{OSHIETE}{MORATTA}",
      f"<p>Bir voqea, boshqa kamera — PJ-60 dagi くれる / もらう "
      f"juftligining oʻzi.</p>"),

    q(f"<p>Ustozga yordam taklif qilyapsiz. Nima deysiz?</p>",
      [f"{r('手伝','てつだ')}い{MASHOUKA}",
       f"{TETSUDATTE}あげます", f"{TETSUDATTE}あげましょうか",
       f"{TETSUDATTE}{MORAEMASUKA}"],
      f"{r('手伝','てつだ')}い{MASHOUKA}",
      f"<p>〜てあげます ustozga nisbatan <strong>marhamat "
      f"qilayotgandek</strong> eshitiladi. Taklif uchun PJ-40 dagi "
      f"〜ましょうか.</p>"),

    q(f"<p>«Kelganingiz uchun rahmat» ni yozing.</p>",
      [f"{r('来','き')}てくれてありがとう", f"{r('来','き')}てあげてありがとう",
       f"{KURU}てくれてありがとう", f"{r('来','き')}てもらってありがとう"],
      f"{r('来','き')}てくれてありがとう",
      f"<p>て-shakli + <strong>くれて</strong> + ありがとう. "
      f"Yaponchada rahmat aytganda nima uchun ekanini feʼl bilan "
      f"koʻrsatish odat.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Nega 〜てあげる ni odamning yuziga aytish notoʻgʻri?</p>",
      ["Chunki u yaxshilikni sovgʻa qilib koʻrsatadi",
       "Chunki u faqat yozma tilda ishlatiladi",
       "Chunki u oʻtgan zamonda turolmaydi",
       "Chunki あげる II guruh feʼli"],
      "Chunki u yaxshilikni sovgʻa qilib koʻrsatadi",
      f"<p>Yapon odobi yaxshilikni <strong>oʻzi aytmaslikni</strong> "
      f"talab qiladi. Shuning uchun bu qolip koʻproq uchinchi odam "
      f"haqida gapirganda ishlatiladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{OTOUTO}___"
      f"{TETSUDATTE}あげました。</strong></p>",
      ["を", "に", "が", "で"],
      "を",
      f"<p>{TETSUDAU} toʻldiruvchisi <strong>odam</strong>, shuning "
      f"uchun u を oladi. Koʻpchilik boshqa feʼllar odamni に bilan "
      f"oladi.</p>"),

    q(f"<p>Ustozdan muloyim iltimos: «oʻrgatib bera olasizmi?»</p>",
      [f"{OSHIETE}{ITADAKEMASUKA}", f"{OSHIETE}あげますか",
       f"{OSHIETE}くれますか", f"{OSHIERU}もらえますか"],
      f"{OSHIETE}{ITADAKEMASUKA}",
      f"<p>Eng muloyim shakl. {OSHIETE}{MORAEMASUKA} ham toʻgʻri, "
      f"lekin いただけますか ustoz va mijoz uchun.</p>"),

    q(f"<p>Muloyimlik boʻyicha tartiblang.</p>",
      ["〜てください → 〜てもらえますか → 〜ていただけますか",
       "〜ていただけますか → 〜てもらえますか → 〜てください",
       "〜てもらえますか → 〜てください → 〜ていただけますか",
       "Uchalasi bir xil"],
      "〜てください → 〜てもらえますか → 〜ていただけますか",
      f"<p>Gap uzaygan sari muloyimlashadi — siz buni PJ-54 dagi "
      f"けど → けれども → が zinapoyasida ham koʻrgansiz.</p>"),

    q(f"<p>«{TOMODACHI}が{HON}を{YONDE}{KURETA}» ni tarjima qiling.</p>",
      ["Doʻstim menga kitob oʻqib berdi", "Men doʻstimga kitob oʻqib berdim",
       "Doʻstim kitob oʻqidi", "Doʻstimdan kitob oʻqib berishlarini oldim"],
      "Doʻstim menga kitob oʻqib berdi",
      f"<p>Ega — doʻstim, feʼl — くれる, demak yaxshilik "
      f"<strong>menga</strong> kelyapti.</p>"),

    q(f"<p>«{WATASHI}は{OTOUTO}に{NIHONGO}を{OSHIETE}___» — qaysi "
      f"feʼl?</p>",
      [AGETA, KURETA, MORATTA, "いただきました"],
      AGETA,
      f"<p>Yaxshilik <strong>mendan chiqyapti</strong>, demak "
      f"あげる. Ukam eshitmayapti, shuning uchun bu yerda "
      f"muammo yoʻq.</p>"),

    q(f"<p>Oʻzbekchada bu darsning qurilmasi qanday ataladi?</p>",
      ["«-ib bermoq»", "«-ib qoʻymoq»", "«-ib koʻrmoq»", "«-ib boʻlmoq»"],
      "«-ib bermoq»",
      f"<p>«Yozib <strong>berdi</strong>», «tushuntirib "
      f"<strong>berdi</strong>» — qurilma allaqachon sizda bor, "
      f"faqat yaponchada «bermoq» ikkiga boʻlingan.</p>"),

    # 13–16 farqlash
    q(f"<p>〜てくれる va 〜てもらう farqi nima?</p>",
      ["Ega boshqa — bir voqeani ikki tomondan aytadi",
       "Birinchisi kelasi, ikkinchisi oʻtgan zamon",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Birinchisi narsa, ikkinchisi ish uchun"],
      "Ega boshqa — bir voqeani ikki tomondan aytadi",
      f"<p>Ega boshqa odam boʻlsa <strong>くれる</strong>, ega men "
      f"boʻlsam <strong>もらう</strong>.</p>"),

    q(f"<p>Qaysi gap odobsiz eshitiladi?</p>",
      [f"{SENSEI}に{OSHIETE}あげます", f"{SENSEI}に{OSHIETE}{ITADAKEMASUKA}",
       f"{SENSEI}が{OSHIETE}{KURETA}", f"{r('手伝','てつだ')}い{MASHOUKA}"],
      f"{SENSEI}に{OSHIETE}あげます",
      f"<p>Ustozga hech qachon 〜てあげます deyilmaydi — u "
      f"«men sizga marhamat qilaman» degan ohang beradi.</p>"),

    q(f"<p>Qaysi feʼl odamni <strong>を</strong> bilan oladi?</p>",
      [TETSUDAU, OSHIERU, KASU, YOMU],
      TETSUDAU,
      f"<p>{TETSUDAU}, {r('誘','さそ')}う, {r('送','おく')}る — "
      f"bularning toʻldiruvchisi odam. Qolganlari odamni に bilan "
      f"oladi.</p>"),

    q(f"<p>«〜てくれてありがとう» quruq «ありがとう» dan nimasi bilan "
      f"farq qiladi?</p>",
      ["Nima uchun rahmat aytilayotganini feʼl bilan koʻrsatadi",
       "Ancha rasmiyroq", "Faqat yozma tilda ishlatiladi",
       "Farqi yoʻq"],
      "Nima uchun rahmat aytilayotganini feʼl bilan koʻrsatadi",
      f"<p>{r('来','き')}てくれてありがとう · {OSHIETE}くれてありがとう "
      f"— bu gapni yodlab qoʻysangiz, suhbatingiz darrov tabiiy "
      f"eshitiladi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{TOMODACHI}が{WATASHI}に{OSHIETE}{AGETA}",
       f"{TOMODACHI}が{WATASHI}に{OSHIETE}{KURETA}",
       f"{WATASHI}は{TOMODACHI}に{OSHIETE}{MORATTA}",
       f"{WATASHI}は{OTOUTO}に{OSHIETE}{AGETA}"],
      f"{TOMODACHI}が{WATASHI}に{OSHIETE}{AGETA}",
      f"<p>Menga kelayotgan yaxshilik doim <strong>くれる</strong>. "
      f"あげる menga qarab yoʻnala olmaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{YONDE}{KURETA}", f"{YOMU}てくれました",
       f"{r('読','よ')}みてくれました", f"{r('読','よ')}んだくれました"],
      f"{YONDE}{KURETA}",
      f"<p>Uchala qolip ham <strong>て-shakliga</strong> "
      f"qoʻshiladi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{KURETA} · {NIHONGO}を · {WATASHI}に · "
      f"{TOMODACHI}が · {OSHIETE}</strong></p>",
      [f"{TOMODACHI}が{WATASHI}に{NIHONGO}を{OSHIETE}{KURETA}",
       f"{WATASHI}に{TOMODACHI}が{NIHONGO}を{OSHIETE}{KURETA}",
       f"{NIHONGO}を{TOMODACHI}が{WATASHI}に{OSHIETE}{KURETA}",
       f"{TOMODACHI}が{NIHONGO}を{OSHIETE}{WATASHI}に{KURETA}"],
      f"{TOMODACHI}が{WATASHI}に{NIHONGO}を{OSHIETE}{KURETA}",
      f"<p>Kim — kimga — nima — ish — yordamchi feʼl. Yapon gapi "
      f"doim feʼl bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ラノ:</strong> この{r('漢字','かんじ')}が"
      f"{r('分','わ')}かりません。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"{OSHIETE}あげましょうか。", f"{OSHIETE}あげます。",
       f"{OSHIETE}{MORATTA}。", f"{OSHIERU}てくれますか。"],
      f"{OSHIETE}あげましょうか。",
      f"<p>Tengdosh doʻstga 〜てあげましょうか deb taklif qilish "
      f"tabiiy — quruq 〜てあげます esa biroz ustunlik qilayotgandek "
      f"eshitiladi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-62 — でしょう / かもしれません / はずです
# ══════════════════════════════════════════════════════════════════════
Q_PJ62 = [
    # 1–5 tanish
    q(f"<p>Uchtasini ishonch darajasi boʻyicha tartiblang "
      f"(pastdan yuqoriga).</p>",
      ["かもしれません → でしょう → はずです",
       "はずです → でしょう → かもしれません",
       "でしょう → かもしれません → はずです",
       "かもしれません → はずです → でしょう"],
      "かもしれません → でしょう → はずです",
      f"<p>~50% → ~80% → ~90%. Oʻzbekcha «boʻlishi mumkin» → "
      f"«boʻlsa kerak» → «boʻlishi kerak».</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{GAKUSEI}でしょう", f"{GAKUSEI}だでしょう",
       f"{GAKUSEI}なでしょう", f"{GAKUSEI}のでしょう"],
      f"{GAKUSEI}でしょう",
      f"<p>でしょう oldida ot <strong>quruq</strong> turadi — xuddi "
      f"PJ-52 dagi なら kabi. だ, な va の — uchalasi ham "
      f"ortiqcha.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GAKUSEI}___"
      f"はずです。</strong></p>",
      ["の", "だ", "な", "で"],
      "の",
      f"<p>はず — <strong>ot</strong>, demak undan oldin PJ-48 ning "
      f"qoidasi ishlaydi: ot の, な-sifat な.</p>"),

    q(f"<p>«{SHIZUKA}» ni はずです bilan ulang.</p>",
      [f"{SHIZUKA}なはずです", f"{SHIZUKA}のはずです",
       f"{SHIZUKA}だはずです", f"{SHIZUKA}はずです"],
      f"{SHIZUKA}なはずです",
      f"<p>な-sifat otdan oldin <strong>な</strong> kiyadi.</p>"),

    q(f"<p>«{AMEK}が{FURU}かもしれません» ni tarjima qiling.</p>",
      ["Yomgʻir yogʻishi mumkin", "Yomgʻir yogʻsa kerak",
       "Yomgʻir yogʻishi kerak", "Yomgʻir yogʻdi"],
      "Yomgʻir yogʻishi mumkin",
      f"<p>かもしれません — eng past daraja. Gapiruvchi bilmaydi "
      f"va shuni ochiq aytadi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Ob-havo maʼlumoti qaysi qolipni ishlatadi?</p>",
      ["でしょう", "かもしれません", "はずです", "なければなりません"],
      "でしょう",
      f"<p>{ASHITA}は{HARERU}でしょう — yaponcha ob-havo maʼlumoti "
      f"deyarli har gapni でしょう bilan tugatadi.</p>"),

    q(f"<p>Rano vaʼda bergan edi. U keladi deb qanday aytasiz?</p>",
      [f"{KURU}はずです", f"{KURU}かもしれません", f"{KURU}でしょう",
       f"{KIMASU}はずです"],
      f"{KURU}はずです",
      f"<p>Aniq dalil bor (vaʼda), demak <strong>はず</strong>. "
      f"Va はず oldida oddiy shakl turadi — ます emas.</p>"),

    q(f"<p>«{SAMUI}でしょう？» — bu taxminmi?</p>",
      ["Yoʻq — bu tasdiq soʻrash: «Sovuq-a?»",
       "Ha, gapiruvchi bilmaydi",
       "Ha, bu ob-havo maʼlumoti",
       "Yoʻq, bu buyruq"],
      "Yoʻq — bu tasdiq soʻrash: «Sovuq-a?»",
      f"<p>Ohang koʻtarilganda でしょう «shundaymi?» degan maʼnoni "
      f"beradi. Gapiruvchi javobni biladi.</p>"),

    q(f"<p>«{r('来','く')}るはずでした» nimani anglatadi?</p>",
      ["Kelishi kerak edi — lekin kelmadi",
       "Kelishi kerak", "Keldi", "Kelishi mumkin edi"],
      "Kelishi kerak edi — lekin kelmadi",
      f"<p>〜はずでした — kutish puchga chiqqanda. Oʻzbekchada "
      f"ham «kelishi kerak edi-ku».</p>"),

    q(f"<p>«{r('行','い')}くはずです» majburiyat bildiradimi?</p>",
      ["Yoʻq — bu taxmin. Majburiyat 〜なければなりません",
       "Ha, bu majburiyat",
       "Ha, lekin faqat yozma tilda",
       "Faqat ot bilan kelganda"],
      "Yoʻq — bu taxmin. Majburiyat 〜なければなりません",
      f"<p>Oʻzbekcha «boʻlishi kerak» ikki xil ishlaydi; yaponchada "
      f"bular butunlay boshqa qoliplar (PJ-33).</p>"),

    q(f"<p>«ラノさんは{r('今','いま')}{KYOUSHITSU}に{IRU}はずです» — "
      f"nega はず?</p>",
      ["Chunki dalil bor — dars boshlandi",
       "Chunki gapiruvchi hech nima bilmaydi",
       "Chunki bu ob-havo haqida",
       "Chunki いる I guruh feʼli"],
      "Chunki dalil bor — dars boshlandi",
      f"<p>はず — <strong>mantiqiy kutish</strong>: dalil bor va "
      f"shundan xulosa chiqarilyapti.</p>"),

    q(f"<p>かもしれません ning ogʻzaki qisqargan shakli qaysi?</p>",
      ["かも", "かもね", "かもしれ", "しれません"],
      "かも",
      f"<p>Doʻstlar suhbatida «{AMEK}かも» deyiladi. Yozma ishda "
      f"toʻliq shakl.</p>"),

    # 13–16 farqlash
    q(f"<p>«Nega shunday deb oʻylaysiz?» degan savolga aniq dalil "
      f"aytib bera olsangiz, qaysi qolip?</p>",
      ["はずです", "かもしれません", "でしょう", "でした"],
      "はずです",
      f"<p>Javobingiz yoʻq boʻlsa — かもしれません. «Odatda "
      f"shunday» boʻlsa — でしょう. Aniq dalil boʻlsa — "
      f"<strong>はずです</strong>.</p>"),

    q(f"<p>Qaysi ikkitasi oldida ot <strong>quruq</strong> "
      f"turadi?</p>",
      ["でしょう va かもしれません", "でしょう va はずです",
       "かもしれません va はずです", "Uchalasi ham"],
      "でしょう va かもしれません",
      f"<p>はず esa ot boʻlgani uchun <strong>の</strong> talab "
      f"qiladi: {GAKUSEI}のはずです.</p>"),

    q(f"<p>Kursda undan oldin な / の talab qiladigan qaysi "
      f"soʻzlarni koʻrgansiz?</p>",
      ["とき · ので · こと · はず", "たら · ば · と · なら",
       "から · ので · けど · が", "ても · ために · ように · そう"],
      "とき · ので · こと · はず",
      f"<p>Toʻrttasi ham <strong>ot</strong>. Yaʼni bu yangi qoida "
      f"emas, bir qoidaning toʻrtinchi koʻrinishi.</p>"),

    q(f"<p>«{KURU}でしょう» va «{KURU}はずです» — farqi nima?</p>",
      ["Birinchisi tajribaga, ikkinchisi aniq dalilga asoslangan",
       "Birinchisi kelasi, ikkinchisi oʻtgan zamon",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Farqi yoʻq"],
      "Birinchisi tajribaga, ikkinchisi aniq dalilga asoslangan",
      f"<p>でしょou — «odatda shunday». はず — «vaʼda bergan, "
      f"chipta olgan».</p>".replace("でしょou", "でしょう")),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{GAKUSEI}はずです", f"{GAKUSEI}のはずです",
       f"{GAKUSEI}でしょう", f"{GAKUSEI}かもしれません"],
      f"{GAKUSEI}はずです",
      f"<p>はず ot, demak ot oldida <strong>の</strong>: "
      f"{GAKUSEI}のはずです.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{SHIZUKA}なはずです", f"{SHIZUKA}だはずです",
       f"{SHIZUKA}のはずです", f"{SHIZUKA}はずです"],
      f"{SHIZUKA}なはずです",
      f"<p>な-sifat otdan oldin な kiyadi — PJ-48 dan beri "
      f"davom etayotgan qoida.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>でしょう · {ASHITA}は · {HARERU}</strong></p>",
      [f"{ASHITA}は{HARERU}でしょう", f"{HARERU}でしょう{ASHITA}は",
       f"でしょう{ASHITA}は{HARERU}", f"{ASHITA}はでしょう{HARERU}"],
      f"{ASHITA}は{HARERU}でしょう",
      f"<p>Vaqt — kesim — でしょう. Taxmin qoliplari doim gap "
      f"oxirida turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>イノム:</strong> ラノさんはどこですか。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"{KYOUSHITSU}に{IRU}はずです。{r('授業','じゅぎょう')}が{r('始','はじ')}まりました。",
       f"{KYOUSHITSU}にいるはずでした。{r('授業','じゅぎょう')}が{r('始','はじ')}まりました。",
       f"{KYOUSHITSU}にいるだはずです。{r('授業','じゅぎょう')}が{r('始','はじ')}まりました。",
       f"{KYOUSHITSU}にいますはずです。{r('授業','じゅぎょう')}が{r('始','はじ')}まりました。"],
      f"{KYOUSHITSU}に{IRU}はずです。{r('授業','じゅぎょう')}が{r('始','はじ')}まりました。",
      f"<p>Dalil aytilgan (dars boshlandi), demak "
      f"<strong>はずです</strong>. Va はず oldida oddiy shakl.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-63 — Passiv
# ══════════════════════════════════════════════════════════════════════
Q_PJ63 = [
    # 1–5 tanish
    q(f"<p>Passiv qaysi oʻzakdan yasaladi?</p>",
      ["ない-shaklining oʻzagidan", "て-shaklidan",
       "た-shaklidan", "Lugʻat shaklidan"],
      "ない-shaklining oʻzagidan",
      f"<p>ない ni olib tashlaysiz va <strong>れる</strong> "
      f"qoʻyasiz: {r('読','よ')}まない → {YOMARERU}.</p>"),

    q(f"<p>{YOMU} ning passiv shakli qaysi?</p>",
      [YOMARERU, f"{r('読','よ')}まられる", f"{r('読','よ')}める",
       f"{r('読','よ')}みれる"],
      YOMARERU,
      f"<p>I guruh: oxirgi bogʻin <strong>あ-qatorga</strong> "
      f"tushadi va れる qoʻshiladi. ({r('読','よ')}める — potensial, "
      f"passiv emas.)</p>"),

    q(f"<p>{TABERU} ning passiv shakli qaysi?</p>",
      [TABERARERU, f"{r('食','た')}べれる", f"{r('食','た')}べらる",
       f"{r('食','た')}べされる"],
      TABERARERU,
      f"<p>II guruh: る tushadi, <strong>られる</strong> "
      f"qoʻyiladi.</p>"),

    q(f"<p>{IU} ning passiv shakli qaysi?</p>",
      [IWARERU, f"{r('言','い')}あれる", f"{r('言','い')}うれる",
       f"{r('言','い')}いれる"],
      IWARERU,
      f"<p>う bilan tugagan feʼlda <strong>わ</strong> chiqadi — "
      f"xuddi ない-shaklida bolgani kabi ({r('言','い')}わない).</p>"
      .replace("bolgani", "boʻlgani")),

    q(f"<p>{KURU} ning passiv shakli qaysi?</p>",
      [KORARERU, f"{r('来','き')}られる", f"{r('来','く')}られる",
       f"{r('来','こ')}れる"],
      KORARERU,
      f"<p>ない-shakli {r('来','こ')}ない, demak oʻzak "
      f"<strong>こ</strong>.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Passiv gapda qiluvchi qaysi qoʻshimchani oladi?</p>",
      ["に", "が", "を", "で"],
      "に",
      f"<p>{WATASHI}は{SENSEI}<strong>に</strong>{HOMERARETA} — "
      f"«oʻqituvchi tomonidan maqtaldim».</p>"),

    q(f"<p>«{SENSEI}が{WATASHI}を{HOMERU}ました» ni passivga "
      f"oʻtkazing.</p>",
      [f"{WATASHI}は{SENSEI}に{HOMERARETA}",
       f"{WATASHI}は{SENSEI}が{HOMERARETA}",
       f"{SENSEI}は{WATASHI}に{HOMERARETA}",
       f"{WATASHI}を{SENSEI}に{HOMERARETA}"],
      f"{WATASHI}は{SENSEI}に{HOMERARETA}",
      f"<p>Eski toʻldiruvchi ega boʻladi (は), eski ega esa "
      f"<strong>に</strong> oladi.</p>"),

    q(f"<p>«{KEEKI}は{OTOUTO}に{TABERARETA}» — passivmi yoki "
      f"potensialmi?</p>",
      ["Passiv — に bilan odam bor va ega jonsiz narsa",
       "Potensial — ega tort yeya oladi",
       "Ikkalasi ham boʻlishi mumkin",
       "Hech qaysi"],
      "Passiv — に bilan odam bor va ega jonsiz narsa",
      f"<p>Uchta belgi: (1) に bilan odam — passiv; (2) toʻldiruvchi "
      f"が — potensial; (3) ega jonsiz narsa — passiv. Tort oʻzi "
      f"yeya olmaydi.</p>"),

    q(f"<p>«{WATASHI}は{SASHIMI}が{TABERARERU}» — passivmi yoki "
      f"potensialmi?</p>",
      ["Potensial — toʻldiruvchi が bilan turibdi",
       "Passiv — sashimi yeb qoʻyilgan",
       "Ikkalasi ham", "Bu notoʻgʻri gap"],
      "Potensial — toʻldiruvchi が bilan turibdi",
      f"<p>Potensial shaklda toʻldiruvchi <strong>が</strong> oladi "
      f"(PJ-42). Passivda esa qiluvchi に bilan chiqadi.</p>"),

    q(f"<p>Nega yaponchada passiv koʻp ishlatiladi?</p>",
      ["Chunki yapon tili gapning mavzusini oʻzgartirmaslikni yaxshi koʻradi",
       "Chunki passiv muloyimroq",
       "Chunki oddiy gap qiyin",
       "Chunki passiv qisqaroq"],
      "Chunki yapon tili gapning mavzusini oʻzgartirmaslikni yaxshi koʻradi",
      f"<p>Hikoya siz haqingizda ketayotgan boʻlsa, har bir gap "
      f"sizdan boshlanadi — hatto ishni boshqa odam qilgan "
      f"boʻlsa ham.</p>"),

    q(f"<p>«この{HON}は{r('百年前','ひゃくねんまえ')}に{KAKARERU}ました» "
      f"ni tarjima qiling.</p>",
      ["Bu kitob yuz yil oldin yozilgan",
       "Bu kitobni yuz yil oldin yozdim",
       "Bu kitob yuz yil oldin oʻqilgan",
       "Bu kitobni yuz yil oldin topdilar"],
      "Bu kitob yuz yil oldin yozilgan",
      f"<p>Kim yozgani muhim emas — yangiliklar va ilmiy matnlar "
      f"shunday yoziladi, xuddi oʻzbekchadagi kabi.</p>"),

    q(f"<p>Passiv feʼl qaysi guruhga aylanadi?</p>",
      ["II guruhga", "I guruhga", "III guruhga",
       "Guruhi oʻzgarmaydi"],
      "II guruhga",
      f"<p>{YOMARERU} endi {TABERU} kabi tuslanadi: "
      f"{r('読','よ')}まれます, {r('読','よ')}まれた, "
      f"{r('読','よ')}まれない.</p>"),

    # 13–16 farqlash
    q(f"<p>Qaysi guruhda passiv va potensial shakl ustma-ust "
      f"tushadi?</p>",
      [f"II guruh va {KURU}", "I guruh", "III guruhdagi する",
       "Hech qaysi"],
      f"II guruh va {KURU}",
      f"<p>I guruhda muammo yoʻq: {r('読','よ')}める — potensial, "
      f"{YOMARERU} — passiv, ikki boshqa shakl.</p>"),

    q(f"<p>Oʻzbekcha va yaponcha passiv nimasi bilan farq "
      f"qiladi?</p>",
      ["Yaponchada qiluvchini に bilan aytish tabiiy, oʻzbekchada esa sunʼiy",
       "Oʻzbekchada passiv yoʻq",
       "Yaponchada passiv faqat yozma tilda",
       "Farqi yoʻq"],
      "Yaponchada qiluvchini に bilan aytish tabiiy, oʻzbekchada esa sunʼiy",
      f"<p>«Alisher tomonidan oʻqildi» kitobiy eshitiladi. Shuning "
      f"uchun yaponcha passivni koʻpincha <strong>oddiy gap</strong> "
      f"bilan tarjima qilish toʻgʻriroq.</p>"),

    q(f"<p>{TSUKAU} ning passiv shakli qaysi?</p>",
      [TSUKAWARERU, f"{r('使','つか')}あれる", f"{r('使','つか')}える",
       f"{r('使','つか')}いれる"],
      TSUKAWARERU,
      f"<p>Yana <strong>わ</strong>: う bilan tugagan feʼllarning "
      f"hammasi shunday. ({r('使','つか')}える — potensial.)</p>"),

    q(f"<p>{SHIKARU} ning passiv oʻtgan zamoni qaysi?</p>",
      [SHIKARARETA, f"{r('叱','しか')}れました",
       f"{r('叱','しか')}らられました", f"{r('叱','しか')}られる"],
      SHIKARARETA,
      f"<p>I guruh, る → ら + れる → られます → "
      f"<strong>{SHIKARARETA}</strong>.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{r('食','た')}べる → {r('食','た')}べれる",
       f"{r('読','よ')}む → {YOMARERU}",
       f"{r('書','か')}く → {KAKARERU}",
       f"{r('言','い')}う → {IWARERU}"],
      f"{r('食','た')}べる → {r('食','た')}べれる",
      f"<p>Toʻgʻrisi — <strong>{TABERARERU}</strong>. II guruh "
      f"passivi doim られる.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WATASHI}は{SENSEI}に{YOBARETA}",
       f"{WATASHI}は{SENSEI}が{YOBARETA}",
       f"{WATASHI}を{SENSEI}に{YOBARETA}",
       f"{WATASHI}は{SENSEI}で{YOBARETA}"],
      f"{WATASHI}は{SENSEI}に{YOBARETA}",
      f"<p>Qiluvchi <strong>に</strong>, ega esa は bilan gap "
      f"boshida.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{TATERARETA} · {r('去年','きょねん')} · "
      f"{TOSHOKAN}は</strong></p>",
      [f"{TOSHOKAN}は{r('去年','きょねん')}{TATERARETA}",
       f"{r('去年','きょねん')}{TATERARETA}{TOSHOKAN}は",
       f"{TATERARETA}{TOSHOKAN}は{r('去年','きょねん')}",
       f"{TOSHOKAN}は{TATERARETA}{r('去年','きょねん')}"],
      f"{TOSHOKAN}は{r('去年','きょねん')}{TATERARETA}",
      f"<p>Ega — vaqt — passiv feʼl. «Kutubxona oʻtgan yili "
      f"qurilgan.»</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> どうして{r('嬉','うれ')}しそうですか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{SENSEI}に{HOMERARETA}。", f"{SENSEI}が{HOMERARETA}。",
       f"{SENSEI}に{r('褒','ほ')}めれました。", f"{SENSEI}に{HOMERU}ました。"],
      f"{SENSEI}に{HOMERARETA}。",
      f"<p>Qiluvchi <strong>に</strong>, va II guruh passivi "
      f"られる — «{r('褒','ほ')}めれました» degan shakl yoʻq.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-61 Mashq: 〜てあげる, 〜てくれる, 〜てもらう",
        "tutorial":    "PJ-61:",
        "description": "Oʻzbekcha «-ib bermoq», yaponcha uch yoʻnalish. "
                       "Va 〜てあげる ni odamning yuziga aytmang.",
        "questions":   Q_PJ61,
        **DEFAULTS,
    },
    {
        "title":       "PJ-62 Mashq: Taxmin — でしょう, かもしれません, はずです",
        "tutorial":    "PJ-62:",
        "description": "Uch ishonch darajasi, va はず ot boʻlgani uchun "
                       "undan oldin な / の.",
        "questions":   Q_PJ62,
        **DEFAULTS,
    },
    {
        "title":       "PJ-63 Mashq: Passiv (受身)",
        "tutorial":    "PJ-63:",
        "description": "ない-oʻzagi + れる / られる. Qiluvchi に oladi, "
                       "va II guruhda られる passiv ham, potensial ham.",
        "questions":   Q_PJ63,
        **DEFAULTS,
    },
]
