# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-49 … PJ-51.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Ikkita narsa bu yerda eng oson sinadi va ikkalasi ham jim:
  * PJ-49 — とき ichidagi ZAMON (行くとき / 行ったとき). Har bir savol
    «asosiy ish boʻlayotganda, とき dagi ish tugaganmi?» degan yagona
    savolga qaytadi.
  * PJ-51 — ば shaklining yasalishi. Har bir kalit `verify_pj_49_51.py`
    da qoidalardan qayta hisoblanadi (う-qator → え-qator, II guruh
    れば, い → ければ, ない → なければ).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_49_51.py --master=prime \\
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


# ── feʼllar ──────────────────────────────────────────────────────────
IKU,   ITTA   = r("行","い")+"く",   r("行","い")+"った"
IKANAI          = r("行","い")+"かない"
IKANAKATTA      = r("行","い")+"かなかった"
KURU,  KITA   = r("来","く")+"る",   r("来","き")+"た"
TABERU, TABETA = r("食","た")+"べる", r("食","た")+"べた"
YOMU,  YONDA  = r("読","よ")+"む",   r("読","よ")+"んだ"
MIRU,  MITA   = r("見","み")+"る",   r("見","み")+"た"
KAERU, KAETTA = r("帰","かえ")+"る", r("帰","かえ")+"った"
HAIRU, HAITTA = r("入","はい")+"る", r("入","はい")+"った"
DERU,  DETA   = r("出","で")+"る",   r("出","で")+"た"
TSUKU, TSUITA = r("着","つ")+"く",   r("着","つ")+"いた"
KAU,   KATTA  = r("買","か")+"う",   r("買","か")+"った"
MATSU          = r("待","ま")+"つ"
ISOGU          = r("急","いそ")+"ぐ"
HANASU         = r("話","はな")+"す"
OSU            = r("押","お")+"す"
OWARU, OWATTA  = r("終","お")+"わる", r("終","お")+"わった"
AKERU, AKETA   = r("開","あ")+"ける", r("開","あ")+"けた"
AKU            = r("開","あ")+"く"
KESU           = r("消","け")+"す"
ARAU           = r("洗","あら")+"う"
HATARAKU       = r("働","はたら")+"く"
FURU,  FUTTA   = r("降","ふ")+"る",  r("降","ふ")+"った"
MANIAU         = r("間","ま")+"に"+r("合","あ")+"う"
SURU           = "する"
RENSHU         = r("練習","れんしゅう")

# ── ば shakllari ─────────────────────────────────────────────────────
IKEBA   = r("行","い")+"けば"
YOMEBA  = r("読","よ")+"めば"
MIREBA  = r("見","み")+"れば"
TABEREBA = r("食","た")+"べれば"
KAEREBA = r("帰","かえ")+"れば"
KAEBA   = r("買","か")+"えば"
MATEBA  = r("待","ま")+"てば"
ISOGEBA = r("急","いそ")+"げば"
HANASEBA = r("話","はな")+"せば"
SUREBA  = "すれば"
KUREBA  = r("来","く")+"れば"
YASUKEREBA = r("安","やす")+"ければ"
TAKAKEREBA = r("高","たか")+"ければ"
IKANAKEREBA = r("行","い")+"かなければ"
YOKEREBA = "よければ"

# ── sifat va otlar ───────────────────────────────────────────────────
TAKAI, YASUI = r("高","たか")+"い", r("安","やす")+"い"
CHIISAI      = r("小","ちい")+"さい"
ISOGASHII    = r("忙","いそが")+"しい"
SHIZUKA      = r("静","しず")+"か"
HIMA         = r("暇","ひま")
GAKUSEI      = r("学生","がくせい")
KODOMO       = r("子","こ")+"ども"
SENSEI       = r("先生","せんせい")
IE           = r("家","いえ")
EKI          = r("駅","えき")
MADO         = r("窓","まど")
YUKI         = r("雪","ゆき")
AME          = r("雨","あめ")
TEGAMI       = r("手紙","てがみ")
DENWA        = r("電話","でんわ")
DENKI        = r("電気","でんき")
KYOSHITSU    = r("教室","きょうしつ")
JIKAN        = r("時間","じかん")
MIZU         = r("水","みず")
MIGI         = r("右","みぎ")
SHIAI        = r("試合","しあい")
NIHON        = r("日本","にほん")
MISE         = r("店","みせ")
TE           = r("手","て")
SHIGOTO      = r("仕事","しごと")
HON          = r("本","ほん")


# ══════════════════════════════════════════════════════════════════════
# PJ-49 — 〜とき
# ══════════════════════════════════════════════════════════════════════
Q_PJ49 = [
    # 1–5 tanish
    q(f"<p>とき aslida qaysi soʻz turkumiga kiradi?</p>",
      ["Ot", "Feʼl", "Sifat", "Qoʻshimcha"],
      "Ot",
      f"<p><strong>とき</strong> — ot ({r('時','とき')}, «payt»). Shuning "
      f"uchun 〜とき yangi grammatika emas: bu PJ-48 dagi aniqlovchi "
      f"ergash gap, faqat aniqlanayotgan ot doim bitta.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GAKUSEI}___とき、"
      f"この{MISE}で{HATARAKU}いていました。</strong></p>",
      ["の", "だ", "な", "が"],
      "の",
      f"<p>とき — ot, demak undan oldin ot <strong>の</strong> oladi "
      f"(PJ-48). «{GAKUSEI}だとき» notoʻgʻri.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HIMA}___とき、"
      f"{HON}を{YOMU}。</strong></p>",
      ["な", "の", "だ", "い"],
      "な",
      f"<p>{HIMA} — な-sifat, va otdan oldin u <strong>な</strong> "
      f"kiyadi. Bu ham PJ-48 ning qoidasi.</p>"),

    q(f"<p>«Kichkinaligimda» qaysi?</p>",
      [f"{CHIISAI}とき", f"{CHIISAI}なとき", f"{CHIISAI}のとき",
       f"{CHIISAI}だとき"],
      f"{CHIISAI}とき",
      f"<p>{CHIISAI} — い-sifat, u otdan oldin <strong>oʻzi</strong> "
      f"turadi. Na な, na の, na だ qoʻshiladi.</p>"),

    q(f"<p>«Bolaligimda» qaysi?</p>",
      [f"{KODOMO}のとき", f"{KODOMO}なとき", f"{KODOMO}だとき",
       f"{KODOMO}とき"],
      f"{KODOMO}のとき",
      f"<p>{KODOMO} — ot, demak <strong>の</strong>.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Yaponiyaga <em>yetib borganimda</em> kamera oldim» qaysi?</p>",
      [f"{NIHON}へ{ITTA}とき、カメラを{KATTA}",
       f"{NIHON}へ{IKU}とき、カメラを{KATTA}",
       f"{NIHON}へ{IKU}のとき、カメラを{KATTA}",
       f"{NIHON}へ{r('行','い')}きましたとき、カメラを{KATTA}"],
      f"{NIHON}へ{ITTA}とき、カメラを{KATTA}",
      f"<p>Borish <strong>tugagan</strong> — demak た-shakli. "
      f"«{IKU}とき» boʻlsa kamera hali Oʻzbekistonda olingan boʻlardi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IE}を{r('出','で')}___とき、"
      f"{DENKI}を{KESU}してください。</strong></p>",
      ["る", "た", "るの", "ました"],
      "る",
      f"<p>Chiroq uydan <em>chiqishdan oldin</em> oʻchiriladi, demak "
      f"chiqish hali tugamagan: <strong>{DERU}とき</strong> — lugʻat "
      f"shakli.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KYOSHITSU}に"
      f"{r('入','はい')}___とき、{SENSEI}はもういました。</strong></p>",
      ["った", "る", "るの", "りました"],
      "った",
      f"<p>Oʻqituvchini koʻrish uchun avval <em>kirib boʻlish</em> kerak "
      f"— demak <strong>{HAITTA}とき</strong>.</p>"),

    q(f"<p>«{IE}に{KAERU}___とき、{TE}を{ARAU}います» — boʻsh joyga nima?</p>",
      ["った", "る", "りました", "るの"],
      "った",
      f"<p>Qoʻl uyga <em>kirgandan keyin</em> yuviladi, demak "
      f"<strong>{KAETTA}とき</strong>.</p>"),

    q(f"<p>«{NIHON}へ{IKU}とき、カメラを{KATTA}» — kamera qayerda "
      f"olingan?</p>",
      ["Yaponiyaga yetib bormasdan oldin", "Yaponiyada",
       "Yaponiyadan qaytgandan keyin", "Buni gapdan bilib boʻlmaydi"],
      "Yaponiyaga yetib bormasdan oldin",
      f"<p>Lugʻat shakli — ish <strong>tugamagan</strong>. Demak kamera "
      f"yoʻlga chiqishdan oldin yoki yoʻlda olingan.</p>"),

    q(f"<p>«{ISOGASHII}とき<strong>は</strong>{DENWA}しません» — は nima "
      f"qoʻshadi?</p>",
      ["«…ganda esa» — boshqa paytga qarshi qoʻyadi",
       "Savolga aylantiradi", "Gapni muloyimroq qiladi",
       "Hech narsa, faqat bezak"],
      "«…ganda esa» — boshqa paytga qarshi qoʻyadi",
      f"<p>とき — ot, demak boshqa otlardek qoʻshimcha ola oladi. "
      f"<strong>は</strong> uni boshqa paytlarga qarshi qoʻyadi: "
      f"band paytda emas, boshqa paytda — ha.</p>"),

    q(f"<p>«Talabalik paytimda» qaysi?</p>",
      [f"{GAKUSEI}のとき", f"{GAKUSEI}だとき", f"{GAKUSEI}なとき",
       f"{GAKUSEI}でとき"],
      f"{GAKUSEI}のとき",
      f"<p>Ot + <strong>の</strong> + とき. Yaponchada oʻtmish haqida "
      f"gapirishning eng tabiiy yoʻli shu.</p>"),

    # 13–16 farqlash
    q(f"<p>とき ichidagi zamon nimaga qarab tanlanadi?</p>",
      ["Asosiy ish boʻlayotganda とき dagi ish tugaganmi — shunga",
       "Hozir soat nechaligiga",
       "Gap oxiridagi feʼlning zamoniga",
       "Gapiruvchining yoshiga"],
      "Asosiy ish boʻlayotganda とき dagi ish tugaganmi — shunga",
      f"<p>Bu darsning yagona savoli. Tugagan boʻlsa — <strong>た</strong>, "
      f"tugamagan boʻlsa — <strong>lugʻat shakli</strong>. Gap oxiridagi "
      f"zamon bunga umuman qaramaydi.</p>"),

    q(f"<p>«{NIHON}へ{IKU}とき、カメラを{KATTA}» — gap oxiri oʻtgan "
      f"zamonda, ichkarisi hozirgi. Bu xatomi?</p>",
      ["Yoʻq — ichkaridagi zamon mustaqil oʻlchanadi",
       "Ha, ikkalasi bir xil boʻlishi kerak",
       "Ha, ichkarisi ham oʻtgan zamonda boʻlishi kerak",
       "Faqat yozma tilda toʻgʻri"],
      "Yoʻq — ichkaridagi zamon mustaqil oʻlchanadi",
      f"<p>PJ-47 va PJ-48 dagi qoida bu yerda ham ishlaydi: gapning "
      f"ichi <strong>asosiy ishga nisbatan</strong> oʻlchanadi, "
      f"«hozir» ga emas.</p>"),

    q(f"<p>とき dan oldin qaysi soʻz turi <strong>hech narsa</strong> "
      f"qoʻshmaydi?</p>",
      ["い-sifat", "な-sifat", "Ot", "Hammasi な qoʻshadi"],
      "い-sifat",
      f"<p>{CHIISAI}とき ✓ · {SHIZUKA}<strong>な</strong>とき ✓ · "
      f"{KODOMO}<strong>の</strong>とき ✓. Faqat い-sifat quruq "
      f"turadi.</p>"),

    q(f"<p>«{r('三時','さんじ')}に{TSUKU}いたとき<strong>に</strong>"
      f"{DENWA}しました» — に nima qoʻshadi?</p>",
      ["Aniq bir paytga ishora qiladi",
       "Gapni inkorga aylantiradi", "Shart maʼnosini beradi",
       "とき ni otdan feʼlga aylantiradi"],
      "Aniq bir paytga ishora qiladi",
      f"<p>に qoʻshish deyarli hech qachon xato emas, lekin majburiy "
      f"ham emas. Shubha boʻlsa quruq <strong>とき</strong>.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{HIMA}だとき", f"{HIMA}なとき", f"{KODOMO}のとき",
       f"{CHIISAI}とき"],
      f"{HIMA}だとき",
      f"<p>{HIMA} な-sifat, demak otdan oldin <strong>な</strong>: "
      f"{HIMA}なとき. だ faqat と oldida chiqadi (PJ-46).</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{IE}を{DERU}とき、{DENKI}を{KESU}してください",
       f"{IE}を{DETA}とき、{DENKI}を{KESU}してください",
       f"{IE}を{r('出','で')}ますとき、{DENKI}を{KESU}してください",
       f"{IE}を{DERU}のとき、{DENKI}を{KESU}してください"],
      f"{IE}を{DERU}とき、{DENKI}を{KESU}してください",
      f"<p>Chiroq chiqishdan oldin oʻchiriladi — demak lugʻat shakli. "
      f"«{r('出','で')}ますとき» ham notoʻgʻri: otdan oldin faqat "
      f"oddiy shakl.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>とき · {r('毎年','まいとし')}{r('夏','なつ')}に · "
      f"{KODOMO}の · {r('村','むら')}へ{r('行','い')}きました</strong></p>",
      [f"{KODOMO}のとき、{r('毎年','まいとし')}{r('夏','なつ')}に{r('村','むら')}へ{r('行','い')}きました",
       f"{r('毎年','まいとし')}{r('夏','なつ')}に{KODOMO}のとき、{r('村','むら')}へ{r('行','い')}きました",
       f"とき{KODOMO}の、{r('毎年','まいとし')}{r('夏','なつ')}に{r('村','むら')}へ{r('行','い')}きました",
       f"{r('村','むら')}へ{r('行','い')}きました{KODOMO}のとき"],
      f"{KODOMO}のとき、{r('毎年','まいとし')}{r('夏','なつ')}に{r('村','むら')}へ{r('行','い')}きました",
      f"<p>Vaqt boʻlagi gap boshida turadi, feʼl esa oxirida. «Bolaligimda "
      f"har yili yozda qishloqqa borardim.»</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ラノ:</strong> いつ{DENWA}しますか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{EKI}に{TSUITA}ときに{DENWA}します。",
       f"{EKI}に{TSUKU}のときに{DENWA}します。",
       f"{EKI}に{r('着','つ')}きましたときに{DENWA}します。",
       f"{EKI}に{TSUITA}だときに{DENWA}します。"],
      f"{EKI}に{TSUITA}ときに{DENWA}します。",
      f"<p>Telefon bekatga <em>yetib borgandan keyin</em> qilinadi — "
      f"demak <strong>{TSUITA}とき</strong>. Otdan oldin ました "
      f"turolmaydi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-50 — 〜たら
# ══════════════════════════════════════════════════════════════════════
Q_PJ50 = [
    # 1–5 tanish
    q(f"<p>〜たら qaysi shaklga qoʻshiladi?</p>",
      ["た-shakliga", "Lugʻat shakliga", "ます-shakliga", "て-shakliga"],
      "た-shakliga",
      f"<p>た-shakli (PJ-35) + <strong>ら</strong>. Boshqa hech qanday "
      f"qoida yoʻq — shuning uchun bu toʻrtta shartning ichida yodlash "
      f"eng osoni.</p>"),

    q(f"<p>{IKU} ning たら shakli qaysi?</p>",
      [f"{ITTA}ら", f"{IKU}たら", f"{r('行','い')}きたら", f"{IKANAI}ら"],
      f"{ITTA}ら",
      f"<p>た-shakli <strong>{ITTA}</strong>, unga ら. Lugʻat shakliga "
      f"qoʻshilmaydi.</p>"),

    q(f"<p>{YASUI} ning たら shakli qaysi?</p>",
      [f"{r('安','やす')}かったら", f"{YASUI}たら", f"{YASUI}だったら",
       f"{r('安','やす')}くたら"],
      f"{r('安','やす')}かったら",
      f"<p>い-sifatning た-shakli <strong>かった</strong>, unga ら. "
      f"«{YASUI}だったら» — otlarning yoʻli.</p>"),

    q(f"<p>{GAKUSEI} ning たら shakli qaysi?</p>",
      [f"{GAKUSEI}だったら", f"{GAKUSEI}かったら", f"{GAKUSEI}たら",
       f"{GAKUSEI}でったら"],
      f"{GAKUSEI}だったら",
      f"<p>Ot <strong>だった</strong> oladi (PJ-45), unga ら. "
      f"な-sifat ham shu yoʻldan boradi: {SHIZUKA}だったら.</p>"),

    q(f"<p>{IKANAI} ning たら shakli qaysi?</p>",
      [f"{IKANAKATTA}ら", f"{IKANAI}たら", f"{r('行','い')}かないだったら",
       f"{r('行','い')}かなくたら"],
      f"{IKANAKATTA}ら",
      f"<p>Inkorning た-shakli <strong>なかった</strong> — ない "
      f"い-sifatdek yuradi (PJ-45). Unga ら.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{IE}に{KAETTA}ら{DENWA}します» — bu «agar» maʼnosidami?</p>",
      ["Yoʻq — uyga qaytish aniq, demak «…gach»",
       "Ha, uyga qaytish noaniq",
       "Ha, bu sof shart gap",
       "Bu kutilmagan kashfiyot maʼnosida"],
      "Yoʻq — uyga qaytish aniq, demak «…gach»",
      f"<p>Shartdagi ish <strong>albatta boʻladigan</strong> boʻlsa, "
      f"たら «…gandan keyin» degani. Oʻzbekchada ham «uyga borsam "
      f"telefon qilaman» — bu shubha emas, vaqt.</p>"),

    q(f"<p>«{MADO}を{AKETA}ら、{YUKI}が{FURU}っていました» — bu qaysi "
      f"maʼno?</p>",
      ["Kutilmagan kashfiyot", "Agar — sof shart",
       "«…gach» — aniq kelajak", "Buyruq"],
      "Kutilmagan kashfiyot",
      f"<p>Ikkala qism ham <strong>oʻtgan zamonda</strong> — demak ish "
      f"allaqachon boʻlgan va natija gapiruvchi uchun kutilmagan edi. "
      f"«Derazani ochsam, qor yogʻayotgan ekan.»</p>"),

    q(f"<p>«Yomgʻir yogʻmasa boramiz» qaysi?</p>",
      [f"{AME}が{r('降','ふ')}らなかったら{r('行','い')}きます",
       f"{AME}が{FURU}なかったら{r('行','い')}きます",
       f"{AME}が{r('降','ふ')}らないたら{r('行','い')}きます",
       f"{AME}が{FUTTA}ら{r('行','い')}きません"],
      f"{AME}が{r('降','ふ')}らなかったら{r('行','い')}きます",
      f"<p>Inkorning た-shakli <strong>{r('降','ふ')}らなかった</strong>, "
      f"unga ら. Oxirgi variant boshqa maʼno beradi: «yogʻsa, "
      f"bormaymiz».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{EKI}に{TSUITA}ら"
      f"{DENWA}して___。</strong></p>",
      ["ください", "います", "あります", "です"],
      "ください",
      f"<p>たら dan keyin <strong>iltimos kelaveradi</strong> — unda "
      f"hech qanday cheklov yoʻq. Aynan shuning uchun たら eng xavfsiz "
      f"shart.</p>"),

    q(f"<p>もし qachon qoʻshiladi?</p>",
      ["Ish haqiqatan ham noaniq boʻlganda",
       "Har doim, たら bilan majburiy",
       "Faqat «…gach» maʼnosida",
       "Faqat oʻtgan zamon bilan"],
      "Ish haqiqatan ham noaniq boʻlganda",
      f"<p>もし — ixtiyoriy kuchaytirgich. «もし{IE}に{KAETTA}ら» "
      f"gʻalati eshitiladi, chunki uyga qaytishingizga shubha yoʻq.</p>"),

    q(f"<p>«{IE}に{KAETTA}ら、ごはんを{r('食','た')}べました» — nega bu "
      f"gap notabiiy?</p>",
      ["Chunki ovqat yeyish kutilmagan emas — uni gapiruvchi oʻzi qilgan",
       "Chunki たら oʻtgan zamon bilan ishlatilmaydi",
       f"Chunki {KAERU} I guruh feʼli",
       "Chunki もし yetishmayapti"],
      "Chunki ovqat yeyish kutilmagan emas — uni gapiruvchi oʻzi qilgan",
      f"<p>Kashfiyot maʼnosidagi たら da ikkinchi qism sizga "
      f"<strong>bogʻliq boʻlmasligi</strong> kerak. Bu yerda PJ-37 dagi "
      f"<strong>〜てから</strong> toʻgʻri keladi.</p>"),

    q(f"<p>«{JIKAN}がなかったら、{r('明日','あした')}でもいいです» ni "
      f"tarjima qiling.</p>",
      ["Vaqtingiz boʻlmasa, ertaga ham boʻladi",
       "Vaqtingiz boʻlgach, ertaga aytasiz",
       "Vaqtingiz boʻlmadi, ertaga boʻladi",
       "Ertaga vaqtingiz boʻlmaydi"],
      "Vaqtingiz boʻlmasa, ertaga ham boʻladi",
      f"<p>Inkor + たら = «boʻlmasa». Bu sof shart — ish noaniq.</p>"),

    # 13–16 farqlash
    q(f"<p>たら ning uchta maʼnosi qaysilar?</p>",
      ["Agar · …gach · kutilmagan kashfiyot",
       "Agar · buyruq · taklif",
       "Sabab · natija · maqsad",
       "Oʻtgan · hozirgi · kelasi"],
      "Agar · …gach · kutilmagan kashfiyot",
      f"<p>Va uchalasini <strong>mazmun</strong> ajratadi, shakl emas: "
      f"ish aniqmi, ikkala qism ham oʻtgan zamondami.</p>"),

    q(f"<p>Nega たら toʻrtta shartdan eng xavfsizi deyiladi?</p>",
      ["Chunki undan keyin buyruq, taklif, xohish va oʻtgan zamon — hammasi kela oladi",
       "Chunki u eng qisqa",
       "Chunki u faqat ogʻzaki nutqda ishlatiladi",
       "Chunki u faqat feʼllar bilan keladi"],
      "Chunki undan keyin buyruq, taklif, xohish va oʻtgan zamon — hammasi kela oladi",
      f"<p>〜ば va 〜と da qattiq cheklovlar bor (PJ-51). たら da esa "
      f"yoʻq — shuning uchun «shubha boʻlsa たら».</p>"),

    q(f"<p>«{r('安','やす')}かったら{KAU}います» va «{r('安','やす')}かったら"
      f"{KAU}いたいです» — ikkalasi ham toʻgʻrimi?</p>",
      ["Ha — たら dan keyin xohish ham kela oladi",
       "Yoʻq, ikkinchisi notoʻgʻri",
       "Yoʻq, birinchisi notoʻgʻri",
       "Ikkalasi ham notoʻgʻri"],
      "Ha — たら dan keyin xohish ham kela oladi",
      f"<p>たら hech narsani taqiqlamaydi. Aynan shu uni boshqa uchta "
      f"shartdan ajratib turadi.</p>"),

    q(f"<p>{SHIZUKA} ning たら shakli qaysi?</p>",
      [f"{SHIZUKA}だったら", f"{SHIZUKA}かったら", f"{SHIZUKA}なったら",
       f"{SHIZUKA}たら"],
      f"{SHIZUKA}だったら",
      f"<p>な-sifat PJ-26 dan beri <strong>ot kabi</strong> tuslanadi, "
      f"demak た-shakli だった.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{IKU}たら", f"{ITTA}ら", f"{r('安','やす')}かったら",
       f"{GAKUSEI}だったら"],
      f"{IKU}たら",
      f"<p>ら <strong>た-shaklga</strong> qoʻshiladi, lugʻat shakliga "
      f"emas. Toʻgʻrisi — {ITTA}ら.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{r('雨','あめ')}が{FUTTA}ら{SHIAI}はありません",
       f"{r('雨','あめ')}が{FURU}たら{SHIAI}はありません",
       f"{r('雨','あめ')}だったたら{SHIAI}はありません",
       f"{r('雨','あめ')}が{r('降','ふ')}りましたら{SHIAI}はありません"],
      f"{r('雨','あめ')}が{FUTTA}ら{SHIAI}はありません",
      f"<p>{FURU} ning た-shakli <strong>{FUTTA}</strong> (I guruh, "
      f"る → った), unga ら.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{r('映画','えいが')}を{MIRU}に{r('行','い')}きます · "
      f"テストが · {OWATTA}ら</strong></p>",
      [f"テストが{OWATTA}ら、{r('映画','えいが')}を{MIRU}に{r('行','い')}きます",
       f"{r('映画','えいが')}を{MIRU}に{r('行','い')}きます、テストが{OWATTA}ら",
       f"テストが{r('映画','えいが')}を{MIRU}に{r('行','い')}きます{OWATTA}ら",
       f"{OWATTA}らテストが、{r('映画','えいが')}を{MIRU}に{r('行','い')}きます"],
      f"テストが{OWATTA}ら、{r('映画','えいが')}を{MIRU}に{r('行','い')}きます",
      f"<p>Shart gap <strong>oldinda</strong>, natija keyin — "
      f"oʻzbekchadagi kabi. «Imtihon tugagach kinoga boramiz.»</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> この{r('本','ほん')}、{TAKAI}ですか。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"{r('安','やす')}かったら{KAU}います。",
       f"{YASUI}たら{KAU}います。",
       f"{YASUI}だったら{KAU}います。",
       f"{r('安','やす')}くたら{KAU}います。"],
      f"{r('安','やす')}かったら{KAU}います。",
      f"<p>い-sifatning た-shakli <strong>かった</strong>, unga ら. "
      f"«Arzon boʻlsa sotib olaman.»</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-51 — 〜ば va 〜と
# ══════════════════════════════════════════════════════════════════════
Q_PJ51 = [
    # 1–5 tanish
    q(f"<p>{IKU} ning ば shakli qaysi?</p>",
      [IKEBA, f"{IKU}ば", f"{r('行','い')}きば", f"{r('行','い')}かば"],
      IKEBA,
      f"<p>I guruh: oxirgi bogʻin <strong>え-qatorga</strong> tushadi "
      f"va ば qoʻshiladi. く → け.</p>"),

    q(f"<p>{TABERU} ning ば shakli qaysi?</p>",
      [TABEREBA, f"{r('食','た')}べば", f"{TABERU}ば", f"{r('食','た')}べらば"],
      TABEREBA,
      f"<p>II guruh: る tushadi, <strong>れば</strong> qoʻyiladi. "
      f"Yana eng oson guruh.</p>"),

    q(f"<p>{YASUI} ning ば shakli qaysi?</p>",
      [YASUKEREBA, f"{YASUI}ば", f"{r('安','やす')}くば",
       f"{r('安','やす')}かれば"],
      YASUKEREBA,
      f"<p>い-sifat: い → <strong>ければ</strong>.</p>"),

    q(f"<p>{SURU} va {KURU} ning ば shakllari qaysi?</p>",
      [f"{SUREBA} · {KUREBA}", f"しば · きば", f"するば · くるば",
       f"されば · こば"],
      f"{SUREBA} · {KUREBA}",
      f"<p>III guruh faqat ikkita feʼl, va ikkalasi ham "
      f"<strong>れば</strong> bilan tugaydi.</p>"),

    q(f"<p>{IKANAI} ning ば shakli qaysi?</p>",
      [IKANAKEREBA, f"{IKANAI}ば", f"{r('行','い')}かなくば",
       f"{r('行','い')}かなかれば"],
      IKANAKEREBA,
      f"<p>ない い-sifatdek yuradi: い → <strong>ければ</strong>. "
      f"Aynan shu shakl PJ-33 dagi {IKANAKEREBA}なりません ning "
      f"ichida turibdi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>ある ning ば shakli qaysi?</p>",
      ["あれば", "あるば", "ありば", "あらば"],
      "あれば",
      f"<p>ある — I guruh feʼli, demak る <strong>れ</strong> ga tushadi "
      f"va ば qoʻshiladi. «{JIKAN}があれば» — «vaqt boʻlsa» — bu "
      f"shaklning eng koʻp uchraydigan ishi.</p>"),

    q(f"<p>{MATSU} ning ば shakli qaysi?</p>",
      [MATEBA, f"{r('待','ま')}ちば", f"{MATSU}ば", f"{r('待','ま')}たば"],
      MATEBA,
      f"<p>つ ning え-qatordagi bogʻini — <strong>て</strong>. "
      f"Demak {MATEBA}.</p>"),

    q(f"<p>{KAU} ning ば shakli qaysi?</p>",
      [KAEBA, f"{r('買','か')}いば", f"{r('買','か')}わば", f"{KAU}ば"],
      KAEBA,
      f"<p>う ning え-qatordagi bogʻini — <strong>え</strong>: {KAEBA}. "
      f"(わ faqat ない-shaklida chiqadi.)</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>このボタンを{OSU}___、"
      f"{MIZU}が{DERU}ます。</strong></p>",
      ["と", "たら", "ば", "とき"],
      "と",
      f"<p>Har safar shunday boʻladi — shubha yoʻq. Bu "
      f"<strong>と</strong> ning maydoni: avtomatik natija.</p>"),

    q(f"<p>«{MIGI}へ{IKU}と、{EKI}があります» ni tarjima qiling.</p>",
      ["Oʻngga borsangiz, bekat boʻladi",
       "Oʻngga borsangiz, bekatga yetasiz deb oʻylayman",
       "Oʻngga bordim, bekat bor edi",
       "Oʻngga boring, u yerda bekat bor"],
      "Oʻngga borsangiz, bekat boʻladi",
      f"<p>と — yoʻl koʻrsatishning yaponcha tili: «shunday qilsangiz, "
      f"har doim shu chiqadi».</p>"),

    q(f"<p>«{ISOGU}ば{MANIAU}います» ni tarjima qiling.</p>",
      ["Shoshilsak ulguramiz", "Shoshilyapmiz, ulguramiz",
       "Shoshiling, ulgurasiz", "Shoshilgach ulguramiz"],
      "Shoshilsak ulguramiz",
      f"<p>Sof mantiq: shoshilish → ulgurish. Aynan "
      f"<strong>ば</strong> ning maydoni. (Shakl {ISOGEBA} — ぐ → げ.)</p>"),

    q(f"<p>ば ni qaysi soʻz turi bilan ishlatish deyarli uchramaydi?</p>",
      ["Ot va な-sifat", "I guruh feʼllari", "い-sifatlar",
       "II guruh feʼllari"],
      "Ot va な-sifat",
      f"<p>«ならば» degan shakl bor, lekin u kitobiy. Ular uchun "
      f"keyingi darsdagi <strong>なら</strong> ishlatiladi.</p>"),

    # 13–16 farqlash
    q(f"<p>と dan keyin nima kelolMAYDI?</p>",
      ["Buyruq, iltimos, taklif va xohish", "Oʻtgan zamon",
       "Inkor", "Sifat"],
      "Buyruq, iltimos, taklif va xohish",
      f"<p>Sababi mantiqiy: と «har doim shunday boʻladi» degani, demak "
      f"undan keyin <strong>tabiat</strong> turishi kerak, sizning "
      f"irodangiz emas.</p>"),

    q(f"<p>«{JIKAN}があると、{r('来','き')}てください» — nima xato?</p>",
      ["と dan keyin iltimos turolmaydi — たら kerak",
       "ある feʼli と bilan ishlatilmaydi",
       f"{r('来','き')}てください notoʻgʻri shakl",
       "Hech qanday xato yoʻq"],
      "と dan keyin iltimos turolmaydi — たら kerak",
      f"<p>Toʻgʻrisi — <strong>{JIKAN}があったら、{r('来','き')}て"
      f"ください</strong>. Bu と ning yagona, lekin qattiq taqigʻi.</p>"),

    q(f"<p>«Shubha boʻlsa qaysi shartni tanlaysiz?» degan qoida nima "
      f"deydi?</p>",
      ["〜たら — unda hech qanday cheklov yoʻq", "〜ば — u eng rasmiy",
       "〜と — u eng qisqa", "Farqi yoʻq, uchalasi bir xil"],
      "〜たら — unda hech qanday cheklov yoʻq",
      f"<p>たら dan keyin buyruq ham, taklif ham, xohish ham, oʻtgan "
      f"zamon ham kela oladi. と va ば esa tor maydonlarga ega.</p>"),

    q(f"<p>«いい» ning ば shakli qaysi?</p>",
      [YOKEREBA, "いければ", "いいければ", "よいば"],
      YOKEREBA,
      f"<p>いい istisno soʻz: u tuslanganda <strong>よ</strong> ga "
      f"aylanadi — よかった, よくない, {YOKEREBA}.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{r('食','た')}べる → {r('食','た')}べば",
       f"{r('読','よ')}む → {YOMEBA}",
       f"{r('見','み')}る → {MIREBA}",
       f"{r('話','はな')}す → {HANASEBA}"],
      f"{r('食','た')}べる → {r('食','た')}べば",
      f"<p>Toʻgʻrisi — <strong>{TABEREBA}</strong>. II guruhda る "
      f"れば ga almashadi, shunchaki tushib qolmaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"このボタンを{OSU}と、ドアが{AKU}ます",
       f"このボタンを{OSU}と、ドアを{AKERU}てください",
       f"このボタンを{r('押','お')}せば、ドアを{AKERU}てください",
       f"このボタンを{OSU}と、ドアを{AKERU}たいです"],
      f"このボタンを{OSU}と、ドアが{AKU}ます",
      f"<p>と dan keyin faqat avtomatik natija turadi. Qolgan uchtasida "
      f"iltimos yoki xohish bor — ular <strong>たら</strong> talab "
      f"qiladi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{MIZU}が{DERU}ます · と · このボタンを{OSU}</strong></p>",
      [f"このボタンを{OSU}と、{MIZU}が{DERU}ます",
       f"{MIZU}が{DERU}ますと、このボタンを{OSU}",
       f"と、このボタンを{OSU}{MIZU}が{DERU}ます",
       f"このボタンを{MIZU}が{OSU}と{DERU}ます"],
      f"このボタンを{OSU}と、{MIZU}が{DERU}ます",
      f"<p>Shart oldinda, natija keyin. Ichkarisi <strong>lugʻat "
      f"shaklida</strong> — と hech qachon ます olmaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>イノム:</strong> まだできません。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"{RENSHU}{SUREBA}できますよ。", f"{RENSHU}するばできますよ。",
       f"{RENSHU}しればできますよ。", f"{RENSHU}してばできますよ。"],
      f"{RENSHU}{SUREBA}できますよ。",
      f"<p>する — III guruh, ば shakli <strong>{SUREBA}</strong>. "
      f"«Mashq qilsangiz, uddalaysiz.»</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-49 Mashq: 〜とき",
        "tutorial":    "PJ-49:",
        "description": "とき — ot, demak undan oldin な / の. Va ichkaridagi "
                       "zamon: ish tugaganmi yoki yoʻqmi.",
        "questions":   Q_PJ49,
        **DEFAULTS,
    },
    {
        "title":       "PJ-50 Mashq: Shart 1 — 〜たら",
        "tutorial":    "PJ-50:",
        "description": "た-shakli + ら. Agar · …gach · kutilmagan kashfiyot "
                       "— uchta maʼno, bitta shakl.",
        "questions":   Q_PJ50,
        **DEFAULTS,
    },
    {
        "title":       "PJ-51 Mashq: Shart 2 — 〜ば va 〜と",
        "tutorial":    "PJ-51:",
        "description": "え-qator + ば, い-sifat ければ. Va と ning qattiq "
                       "taqigʻi: keyin buyruq turolmaydi.",
        "questions":   Q_PJ51,
        **DEFAULTS,
    },
]
