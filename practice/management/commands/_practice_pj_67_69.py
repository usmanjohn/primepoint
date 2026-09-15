# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-67 … PJ-69.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Uch tuzoq, uchalasi ham `verify_pj_67_69_forms.py` da qoidadan qayta
hisoblanadi:
    来る → 来い  (きろ EMAS)
    食べる → 食べろ  (食べれ EMAS — え-qator faqat I guruhda)
    いらっしゃる → いらっしゃいます  (いらっしゃります EMAS)
Oxirgisi butun keigo blokidagi eng koʻp qilinadigan xato.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_67_69.py --master=prime \\
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
MATSU   = r("待","ま")+"つ"
KAKU    = r("書","か")+"く"
TSUKAU  = r("使","つか")+"う"
HASHIRU = r("走","はし")+"る"
GANBARU = r("頑張","がんば")+"る"
TOMARU  = r("止","と")+"まる"
HAIRU   = r("入","はい")+"る"
NIGERU  = r("逃","に")+"げる"
TABERU  = r("食","た")+"べる"
MIRU    = r("見","み")+"る"
OKIRU   = r("起","お")+"きる"
KURU    = r("来","く")+"る"
SURU    = "する"
DEKAKERU = r("出","で")+"かける"
KAERU   = r("帰","かえ")+"る"

# ── buyruq / taqiq ───────────────────────────────────────────────────
IKE     = r("行","い")+"け"
YOME    = r("読","よ")+"め"
MATE    = r("待","ま")+"て"
GANBARE = r("頑張","がんば")+"れ"
TOMARE  = r("止","と")+"まれ"
NIGERO  = r("逃","に")+"げろ"
TABERO  = r("食","た")+"べろ"
MIRO    = r("見","み")+"ろ"
SHIRO   = "しろ"
KOI     = r("来","こ")+"い"
IKUNA   = r("行","い")+"くな"
HAIRUNA = r("入","はい")+"るな"
TABERUNA = r("食","た")+"べるな"
MIRUNA  = r("見","み")+"るな"
KURUNA  = r("来","く")+"るな"
TABENASAI = r("食","た")+"べなさい"
IKINASAI  = r("行","い")+"きなさい"

# ── keigo ────────────────────────────────────────────────────────────
IRASSHARU   = "いらっしゃる"
IRASSHAIMASU = "いらっしゃいます"
MESHIAGARU  = r("召","め")+"し"+r("上","あ")+"がる"
MESHIAGARIMASU = r("召","め")+"し"+r("上","あ")+"がります"
OSSHARU     = "おっしゃる"
OSSHAIMASU  = "おっしゃいます"
NASARU      = "なさる"
NASAIMASU   = "なさいます"
KUDASARU    = "くださる"
KUDASAIMASU = "くださいます"
GORAN       = "ご"+r("覧","らん")+"になる"
GOZONJI     = "ご"+r("存","ぞん")+"じだ"
ITADAKU     = "いただく"
OYOMI       = "お"+r("読","よ")+"みになる"
OKAKI       = "お"+r("書","か")+"きになる"
OMACHI      = "お"+r("待","ま")+"ちになる"
OTSUKAI     = "お"+r("使","つか")+"いになる"
ODEKAKE     = "お"+r("出","で")+"かけになる"
KAERARERU   = r("帰","かえ")+"られました"

MEIREI   = r("命令形","めいれいけい")
SONKEIGO = r("尊敬語","そんけいご")
KENJOUGO = r("謙譲語","けんじょうご")
TEINEIGO = r("丁寧語","ていねいご")
KEIGO    = r("敬語","けいご")
UCHI     = r("内","うち")
SOTO     = r("外","そと")

# ── otlar ────────────────────────────────────────────────────────────
WATASHI  = r("私","わたし")
OKYAKU   = "お"+r("客","きゃく")+"さま"
SENSEI   = r("先生","せんせい")
SHACHOU  = r("社長","しゃちょう")
BUCHOU   = r("部長","ぶちょう")
NAMAE    = r("名前","なまえ")
KAZOKU   = r("家族","かぞく")
JUUSHO   = r("住所","じゅうしょ")
IKEN     = r("意見","いけん")
HON      = r("本","ほん")


# ══════════════════════════════════════════════════════════════════════
# PJ-67 — buyruq va taqiq
# ══════════════════════════════════════════════════════════════════════
Q_PJ67 = [
    # 1–5 tanish
    q(f"<p>{IKU} ning buyruq shakli qaysi?</p>",
      [IKE, f"{r('行','い')}きろ", f"{r('行','い')}かれ", f"{IKU}ろ"],
      IKE,
      f"<p>I guruh: oxirgi bogʻin <strong>え-qatorga</strong> tushadi "
      f"va hech nima qoʻshilmaydi.</p>"),

    q(f"<p>{TABERU} ning buyruq shakli qaysi?</p>",
      [TABERO, f"{r('食','た')}べれ", f"{r('食','た')}べい",
       f"{r('食','た')}べよう"],
      TABERO,
      f"<p>II guruh: る tushadi, <strong>ろ</strong> qoʻyiladi. "
      f"え-qator faqat I guruhda.</p>"),

    q(f"<p>{KURU} ning buyruq shakli qaysi?</p>",
      [KOI, f"{r('来','き')}ろ", f"{r('来','く')}れ", f"{r('来','こ')}ろ"],
      KOI,
      f"<p><strong>{KOI}</strong> — istisno. «{r('来','き')}ろ» degan "
      f"shakl yoʻq, uni yodlab qoʻying.</p>"),

    q(f"<p>Taqiq shakli qanday yasaladi?</p>",
      ["Lugʻat shakli + な", "Buyruq shakli + な",
       "ない-shakli + な", "ます-oʻzagi + な"],
      "Lugʻat shakli + な",
      f"<p>Uch guruh uchun ham bir xil, <strong>istisno "
      f"yoʻq</strong>: {IKUNA}, {TABERUNA}, {KURUNA}.</p>"),

    q(f"<p>{MIRU} ning taqiq shakli qaysi?</p>",
      [MIRUNA, f"{r('見','み')}ろな", f"{r('見','み')}ない",
       f"{r('見','み')}なな"],
      MIRUNA,
      f"<p>な <strong>lugʻat shakliga</strong> qoʻshiladi, buyruq "
      f"shakliga emas.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{GANBARE}» qoʻpolmi?</p>",
      ["Yoʻq — sport maydonida bu quvvatlash",
       "Ha, doim qoʻpol",
       "Ha, faqat ustozga aytilsa",
       "Bu buyruq shakli emas"],
      "Yoʻq — sport maydonida bu quvvatlash",
      f"<p>Va u eng koʻp eshitiladigan buyruq shakli. Shakl bir xil, "
      f"lekin vazifasi boshqa.</p>"),

    q(f"<p>Yoʻl belgisida qaysi shakl turadi?</p>",
      [TOMARE, f"{r('止','と')}まってください",
       f"{r('止','と')}まりなさい", f"{r('止','と')}まりましょう"],
      TOMARE,
      f"<p>Belgi muloyim boʻlmaydi — u <strong>qisqa</strong> "
      f"boʻlishi kerak. Shuning uchun buyruq shakli.</p>"),

    q(f"<p>Ustozga «kuting» deysiz. Qaysi shakl?</p>",
      [f"{r('待','ま')}ってください", MATE,
       f"{r('待','ま')}ちなさい", f"{r('待','ま')}つな"],
      f"{r('待','ま')}ってください",
      f"<p>Buyruq shakli odamga aytilmaydi. Muloyimroq: "
      f"{r('待','ま')}っていただけますか (PJ-61).</p>"),

    q(f"<p>〜なさい kimga aytiladi?</p>",
      ["Ota-onadan bolaga, ustozdan oʻquvchiga",
       "Oʻquvchidan ustozga", "Mijozga", "Kattaroq odamga"],
      "Ota-onadan bolaga, ustozdan oʻquvchiga",
      f"<p>Qatʼiy, lekin qoʻpol emas. Imtihon savollarida ham "
      f"chiqadi: {r('答','こた')}えなさい.</p>"),

    q(f"<p>{TABERU} ni なさい qolipiga qoʻying.</p>",
      [TABENASAI, f"{r('食','た')}べるなさい", f"{TABERO}なさい",
       f"{r('食','た')}べらなさい"],
      TABENASAI,
      f"<p><strong>ます-oʻzagi</strong> + なさい. {TABERU} ning "
      f"ます-oʻzagi — {r('食','た')}べ.</p>"),

    q(f"<p>«{HAIRUNA}» qayerda uchraydi?</p>",
      ["Ogohlantirish belgisida — xavf bor",
       "Doʻkonda mijozga", "Ustoz oʻquvchiga",
       "Rasmiy xatda"],
      "Ogohlantirish belgisida — xavf bor",
      f"<p>{r('立入禁止','たちいりきんし')} — «kirish taqiqlangan». "
      f"Xavf bor, vaqt yoʻq, shuning uchun eng qisqa shakl.</p>"),

    q(f"<p>Oʻzbekcha «borma» ning yaponcha qarindoshi nimasi bilan "
      f"oʻxshaydi?</p>",
      ["Ikkalasi ham feʼlga bitta boʻgʻin qoʻshadi — -ma va な",
       "Ikkalasi ham gap boshida turadi",
       "Ikkalasi ham ikki soʻzdan iborat",
       "Hech qanday oʻxshashlik yoʻq"],
      "Ikkalasi ham feʼlga bitta boʻgʻin qoʻshadi — -ma va な",
      f"<p>Farqi: oʻzbekcha «borma» doʻstga aytilsa oddiy gap; "
      f"yaponcha {IKUNA} esa deyarli baqiriq.</p>"),

    # 13–16 farqlash
    q(f"<p>Buyruq shaklining え-qatori qaysi boshqa shakl bilan bir "
      f"xil oʻzakka ega?</p>",
      [f"ば-shakli (PJ-51) — {IKE}ば", "た-shakli", "て-shakli",
       "ない-shakli"],
      f"ば-shakli (PJ-51) — {IKE}ば",
      f"<p>{IKE} — oʻsha {IKE}ば ning oʻzi, faqat ば siz. Yangi "
      f"oʻzak yodlash kerak emas.</p>"),

    q(f"<p>Zinapoyani tartiblang (qoʻpoldan muloyimga).</p>",
      [f"{MEIREI} → 〜なさい → 〜てください",
       f"〜てください → 〜なさい → {MEIREI}",
       f"〜なさい → {MEIREI} → 〜てください",
       "Uchalasi bir xil darajada"],
      f"{MEIREI} → 〜なさい → 〜てください",
      f"<p>Va zinapoya yuqoriga davom etadi: 〜てもらえますか, "
      f"〜ていただけますか (PJ-61).</p>"),

    q(f"<p>{SURU} ning buyruq shakli qaysi?</p>",
      [SHIRO, "すろ", "され", "しれ"],
      SHIRO,
      f"<p>III guruh istisno: する → <strong>{SHIRO}</strong>, "
      f"{KURU} → {KOI}.</p>"),

    q(f"<p>Qaysi joyda buyruq shakli toʻgʻri EMAS?</p>",
      ["Doʻkonda mijozga", "Yoʻl belgisida",
       "Sport maydonida", "Favqulodda holatda"],
      "Doʻkonda mijozga",
      f"<p>Mijoz, ustoz, notanish odam — bu shakllar "
      f"<strong>hech qachon</strong> ularga aytilmaydi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{KURU} → {r('来','き')}ろ", f"{IKU} → {IKE}",
       f"{TABERU} → {TABERO}", f"{SURU} → {SHIRO}"],
      f"{KURU} → {r('来','き')}ろ",
      f"<p>Toʻgʻrisi — <strong>{KOI}</strong>. Bu istisno.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [TABERUNA, f"{TABERO}な", f"{r('食','た')}べな",
       f"{r('食','た')}べるなさいな"],
      TABERUNA,
      f"<p>な lugʻat shakliga qoʻshiladi: {TABERU} + な.</p>"),

    # 19–20 tuzish
    q(f"<p>Sport maydonida jamoangizni quvvatlaysiz. Nima "
      f"baqirasiz?</p>",
      [GANBARE, f"{r('頑張','がんば')}ってください",
       f"{r('頑張','がんば')}りなさい", f"{r('頑張','がんば')}るな"],
      GANBARE,
      f"<p>Bu buyruq emas, <strong>quvvatlash</strong>. Maydonda "
      f"muloyim shakl gʻalati eshitiladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>せんせい:</strong> まだ{r('食','た')}べていませんか。</p>"
      f"<p><strong>おかあさん:</strong> ___ <em>(bolasiga)</em></p>",
      [f"{r('早','はや')}く{TABENASAI}。", f"{r('早','はや')}く{TABERO}。",
       f"{r('早','はや')}く{r('食','た')}べてください。",
       f"{r('早','はや')}く{TABERUNA}。"],
      f"{r('早','はや')}く{TABENASAI}。",
      f"<p>Ota-onadan bolaga — <strong>〜なさい</strong>. {TABERO} "
      f"qoʻpol, 〜てください esa oʻz farzandiga gʻalati "
      f"rasmiy.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-68 — keigo umumiy koʻrinishi
# ══════════════════════════════════════════════════════════════════════
Q_PJ68 = [
    # 1–5 tanish
    q(f"<p>Keigo nima?</p>",
      ["Mavqeni koʻrsatadigan tizim", "Juda muloyim yaponcha",
       "Yozma yaponcha", "Qadimgi yaponcha"],
      "Mavqeni koʻrsatadigan tizim",
      f"<p>Keigo <strong>kim yuqorida, kim pastda</strong> ekanini "
      f"har bir feʼlda koʻrsatadi. です・ます esa muloyimlik.</p>"),

    q(f"<p>{SONKEIGO} nima qiladi?</p>",
      ["Suhbatdoshni koʻtaradi", "Meni pasaytiradi",
       "Gapga kiyim beradi", "Gapni qisqartiradi"],
      "Suhbatdoshni koʻtaradi",
      f"<p>Va u <strong>faqat boshqa odamning</strong> ishiga "
      f"qoʻyiladi.</p>"),

    q(f"<p>{KENJOUGO} nima qiladi?</p>",
      ["Meni pasaytiradi", "Suhbatdoshni koʻtaradi",
       "Gapga kiyim beradi", "Buyruq beradi"],
      "Meni pasaytiradi",
      f"<p>Va u <strong>faqat mening</strong> ishimga qoʻyiladi.</p>"),

    q(f"<p>{TEINEIGO} — bu nima?</p>",
      ["です・ます — butun gapga kiyim", "Maxsus feʼllar",
       "Buyruq shakli", "Oddiy shakl"],
      "です・ます — butun gapga kiyim",
      f"<p>Siz uni PJ-13 dan beri ishlatasiz. Kimning ishi boʻlsa "
      f"ham qoʻyilaveradi.</p>"),

    q(f"<p>Mijoz yeyayapti. Qaysi feʼl?</p>",
      [MESHIAGARU, ITADAKU, f"{r('食','た')}べる", f"{r('食','た')}べます"],
      MESHIAGARU,
      f"<p>{SONKEIGO} — bu <em>uning</em> ishi. {ITADAKU} esa "
      f"mening ishim uchun.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{WATASHI}が{MESHIAGARIMASU}» — nima xato?</p>",
      [f"{SONKEIGO} oʻzingizga ishlatilmaydi",
       "Feʼl notoʻgʻri yasalgan",
       "が oʻrniga は boʻlishi kerak",
       "Hech qanday xato yoʻq"],
      f"{SONKEIGO} oʻzingizga ishlatilmaydi",
      f"<p>«Men marhamat qilib yeyman» — kulgili eshitiladi. "
      f"Toʻgʻrisi — {WATASHI}が{ITADAKU}.</p>"),

    q(f"<p>«{OKYAKU}が{ITADAKU}» — nima xato?</p>",
      [f"{KENJOUGO} suhbatdoshga ishlatilmaydi",
       f"お{r('客','きゃく')}さま notoʻgʻri yozilgan",
       "が oʻrniga を boʻlishi kerak",
       "Hech qanday xato yoʻq"],
      f"{KENJOUGO} suhbatdoshga ishlatilmaydi",
      f"<p>«Mijoz kamtarlik bilan oladi» — bu haqorat. Toʻgʻrisi "
      f"— {OKYAKU}が{MESHIAGARIMASU}.</p>"),

    q(f"<p>Yapon tili odamlarni qanday ikki guruhga boʻladi?</p>",
      [f"{UCHI} va {SOTO}", "Katta va kichik",
       "Erkak va ayol", "Yosh va keksa"],
      f"{UCHI} va {SOTO}",
      f"<p>{UCHI} — men, oilam, ishxonam. {SOTO} — mijoz, begona, "
      f"boshqa kompaniya. PJ-72 butunlay shu haqida.</p>"),

    q(f"<p>Nega oʻz boshligʻingizni mijozga gapirganda "
      f"pasaytirasiz?</p>",
      [f"Chunki u sizning {UCHI} ingizda, mijoz esa {SOTO}",
       "Chunki boshliqni yoqtirmaysiz",
       "Chunki mijoz kattaroq",
       "Chunki bu faqat telefonda shunday"],
      f"Chunki u sizning {UCHI} ingizda, mijoz esa {SOTO}",
      f"<p>Ishxonada {BUCHOU}はいらっしゃいます, telefonda esa "
      f"{BUCHOU}はおりません. Bitta odam, ikki shakl — chegara "
      f"siljigan.</p>"),

    q(f"<p>Talaba sifatida ustoz bilan qaysi daraja yetadi?</p>",
      [TEINEIGO, SONKEIGO, KENJOUGO, "Oddiy shakl"],
      TEINEIGO,
      f"<p>です・ます toʻliq toʻgʻri va hech kim sizdan koʻproq "
      f"kutmaydi. Keigo ish joyida va doʻkonda kerak.</p>"),

    q(f"<p>Keigoning eng oson darajasi qaysi?</p>",
      ["PJ-63 dagi passiv shakl", "Maxsus feʼllar",
       "お〜になる qolipi", "ございます"],
      "PJ-63 dagi passiv shakl",
      f"<p>{KAERARERU} — «ketdilar». Siz buni allaqachon yasay "
      f"olasiz.</p>"),

    q(f"<p>Oʻzbekchada keigoga eng yaqin narsa nima?</p>",
      ["«Keldilar», «aytdilar» — koʻplik bilan hurmat",
       "«Borma» — taqiq",
       "«Oʻqitdim» — kauzativ",
       "Oʻzbekchada hech qanday hurmat shakli yoʻq"],
      "«Keldilar», «aytdilar» — koʻplik bilan hurmat",
      f"<p>Bu {SONKEIGO} tarmogʻiga toʻgʻri keladi. Farqi: "
      f"oʻzbekchada oʻzini pasaytiradigan tarmoq deyarli yoʻq.</p>"),

    # 13–16 farqlash
    q(f"<p>Oʻzbekcha va yaponcha hurmat tizimi nimasi bilan tubdan "
      f"farq qiladi?</p>",
      ["Oʻzbekchada bir daraja butun suhbatga, yaponchada har feʼlga",
       "Oʻzbekchada hurmat yoʻq",
       "Yaponchada faqat bitta daraja bor",
       "Farqi yoʻq"],
      "Oʻzbekchada bir daraja butun suhbatga, yaponchada har feʼlga",
      f"<p>Yaponchada daraja <strong>kimning ishi</strong> "
      f"ekaniga bogʻliq — shuning uchun u har feʼlda qaytadan "
      f"tanlanadi.</p>"),

    q(f"<p>{MESHIAGARU} va {ITADAKU} — maʼnosi farq qiladimi?</p>",
      ["Yoʻq — ikkalasi ham «yemoq», farq kim yuqorida turishida",
       "Ha — biri yemoq, biri ichmoq",
       "Ha — biri hozirgi, biri oʻtgan zamon",
       "Ha — biri rasmiy, biri oddiy"],
      "Yoʻq — ikkalasi ham «yemoq», farq kim yuqorida turishida",
      f"<p>Ular almashsa, gap <strong>grammatik emas, ijtimoiy</strong> "
      f"xato boʻladi.</p>"),

    q(f"<p>Keigo bloki nechta darsdan iborat?</p>",
      ["Toʻrtta: PJ-68, 69, 70, 71", "Ikkita", "Uchta", "Beshta"],
      "Toʻrtta: PJ-68, 69, 70, 71",
      f"<p>PJ-68 xarita, PJ-69 {SONKEIGO}, PJ-70 {KENJOUGO}, "
      f"PJ-71 {TEINEIGO} va doʻkondagi yapon tili.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{OKYAKU}が{MESHIAGARIMASU}", f"{OKYAKU}が{ITADAKU}",
       f"{WATASHI}が{MESHIAGARIMASU}", f"{OKYAKU}が{ITADAKU}ます"],
      f"{OKYAKU}が{MESHIAGARIMASU}",
      f"<p>Mijozning ishi — {SONKEIGO}. Mening ishim — "
      f"{KENJOUGO}.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda ijtimoiy xato bor?</p>",
      [f"{WATASHI}が{MESHIAGARIMASU}", f"{WATASHI}が{ITADAKU}",
       f"{OKYAKU}が{MESHIAGARIMASU}", f"{WATASHI}が{r('食','た')}べます"],
      f"{WATASHI}が{MESHIAGARIMASU}",
      f"<p>{SONKEIGO} ni oʻzingizga qoʻyish — eng katta xato.</p>"),

    q(f"<p>Qaysi jumla keigo haqida notoʻgʻri?</p>",
      [f"Keigo — bu juda muloyim yaponcha",
       "Keigo mavqeni koʻrsatadi",
       f"{SONKEIGO} oʻzingizga ishlatilmaydi",
       "Talaba uchun です・ます yetadi"],
      "Keigo — bu juda muloyim yaponcha",
      f"<p>Keigo — <strong>mavqe</strong>. Muloyimlik esa "
      f"{TEINEIGO} ning ishi.</p>"),

    # 19–20 tuzish
    q(f"<p>Doʻkonda ishlaysiz. Mijoz kirdi. Qaysi feʼl?</p>",
      [f"{OKYAKU}が{IRASSHAIMASU}", f"{OKYAKU}が{ITADAKU}",
       f"{OKYAKU}が{r('参','まい')}ります", f"{WATASHI}が{IRASSHAIMASU}"],
      f"{OKYAKU}が{IRASSHAIMASU}",
      f"<p>Mijozning ishi — {SONKEIGO}. {IRASSHARU} — «boʻlmoq, "
      f"kelmoq» ning hurmat shakli.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>おきゃく:</strong> {BUCHOU}はいますか。</p>"
      f"<p><strong>あなた:</strong> ___</p>",
      [f"{BUCHOU}はおりません。", f"{BUCHOU}はいらっしゃいません。",
       f"{BUCHOU}は{MESHIAGARU}ません。", f"{BUCHOU}はおっしゃいません。"],
      f"{BUCHOU}はおりません。",
      f"<p>Mijoz — {SOTO}, boshliq — {UCHI}. Shuning uchun oʻz "
      f"boshligʻingizni <strong>pasaytirasiz</strong>. Ishxona "
      f"ichida esa いらっしゃいます deyilardi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-69 — 尊敬語
# ══════════════════════════════════════════════════════════════════════
Q_PJ69 = [
    # 1–5 tanish
    q(f"<p>{IRASSHARU} ning ます shakli qaysi?</p>",
      [IRASSHAIMASU, "いらっしゃります", "いらっしゃりました",
       "いらっしゃれます"],
      IRASSHAIMASU,
      f"<p>Beshta istisno feʼlda <strong>り → い</strong>. "
      f"«いらっしゃります» degan shakl <strong>yoʻq</strong> — bu "
      f"butun blokdagi eng koʻp qilinadigan xato.</p>"),

    q(f"<p>«Yemoq» ning {SONKEIGO} shakli qaysi?</p>",
      [MESHIAGARU, ITADAKU, f"{r('食','た')}べられる", OSSHARU],
      MESHIAGARU,
      f"<p>{ITADAKU} — {KENJOUGO} (mening ishim uchun).</p>"),

    q(f"<p>«Aytmoq» ning {SONKEIGO} shakli qaysi?</p>",
      [OSSHARU, f"{r('申','もう')}す", NASARU, GORAN],
      OSSHARU,
      f"<p>ます shakli — <strong>{OSSHAIMASU}</strong>, yana "
      f"り → い.</p>"),

    q(f"<p>{YOMU} ni お〜になる qolipiga qoʻying.</p>",
      [OYOMI, f"お{YOMU}になる", f"お{r('読','よ')}んでになる",
       f"お{r('読','よ')}まになる"],
      OYOMI,
      f"<p><strong>ます-oʻzagi</strong> ishlatiladi: "
      f"{r('読','よ')}み.</p>"),

    q(f"<p>Keigoning eng oson darajasi qaysi?</p>",
      [f"Passiv shakl — {r('読','よ')}まれる, {r('帰','かえ')}られる", "Maxsus feʼllar",
       "お〜になる", "ございます"],
      f"Passiv shakl — {r('読','よ')}まれる, {r('帰','かえ')}られる",
      f"<p>Siz uni PJ-63 dan beri yasay olasiz. Kontekst uni "
      f"passivdan ajratadi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Beshta istisno feʼl qaysilar?</p>",
      [f"{IRASSHARU}, {NASARU}, {OSSHARU}, {KUDASARU}, ござる",
       f"{MESHIAGARU}, {GORAN}, {GOZONJI}, {ITADAKU}, {OSSHARU}",
       f"{IRASSHARU}, {MESHIAGARU}, {GORAN}, {GOZONJI}, ござる",
       f"{NASARU}, {ITADAKU}, {r('申','もう')}す, おる, ござる"],
      f"{IRASSHARU}, {NASARU}, {OSSHARU}, {KUDASARU}, ござる",
      f"<p>Bularning ます shaklida り → い: {IRASSHAIMASU}, "
      f"{NASAIMASU}, {OSSHAIMASU}, {KUDASAIMASU}, ございます.</p>"),

    q(f"<p>PJ-32 dagi «ください» aslida nima?</p>",
      [f"{KUDASARU} ning buyruq shakli",
       f"{KUDASARU} ning ます shakli",
       "Alohida soʻz", f"{ITADAKU} ning shakli"],
      f"{KUDASARU} ning buyruq shakli",
      f"<p>Shuning uchun u «くださり» emas, <strong>ください</strong>. "
      f"PJ-32, PJ-67 va PJ-69 bir joyda uchrashdi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHACHOU}はもう"
      f"{r('帰','かえ')}___。</strong> — «direktor ketdilar»</p>",
      ["られました", "らせました", "りました", "れました"],
      "られました",
      f"<p>Passiv shakl = yengil hurmat. Kontekst ajratadi: "
      f"direktor «qaytarilmaydi».</p>"),

    q(f"<p>«お{r('行','い')}きになる» toʻgʻrimi?</p>",
      [f"Yoʻq — {IKU} uchun {IRASSHARU} bor",
       "Ha, toʻliq toʻgʻri",
       "Ha, lekin faqat yozma tilda",
       f"Yoʻq — お{r('行','い')}きなさる boʻlishi kerak"],
      f"Yoʻq — {IKU} uchun {IRASSHARU} bor",
      f"<p>Maxsus feʼli bor feʼllarga お-qolipi qoʻyilmaydi. "
      f"する va {KURU} ham お-qolipini olmaydi.</p>"),

    q(f"<p>お{NAMAE} nega お oladi, ご emas?</p>",
      [f"Chunki {NAMAE} — kun-oʻqilish",
       f"Chunki {NAMAE} qisqa",
       f"Chunki {NAMAE} — on-oʻqilish",
       "Chunki bu istisno"],
      f"Chunki {NAMAE} — kun-oʻqilish",
      f"<p>Kun-oʻqilishga <strong>お</strong>, on-oʻqilishga "
      f"<strong>ご</strong>: ご{KAZOKU}, ご{JUUSHO}, ご{IKEN}. "
      f"PJ-11 dagi ikki oʻqilish shu yerda ishga tushdi.</p>"),

    q(f"<p>«Koʻrmoq» ning {SONKEIGO} shakli qaysi?</p>",
      [GORAN, f"{r('見','み')}られる", f"{r('拝見','はいけん')}する",
       GOZONJI],
      GORAN,
      f"<p>{r('拝見','はいけん')}する — {KENJOUGO} (PJ-70 da).</p>"),

    q(f"<p>{DEKAKERU} ni お〜になる qolipiga qoʻying.</p>",
      [ODEKAKE, f"お{DEKAKERU}になる", f"お{r('出','で')}かけましになる",
       f"ご{r('出','で')}かけになる"],
      ODEKAKE,
      f"<p>II guruh feʼlining ます-oʻzagi — る siz shakl: "
      f"{r('出','で')}かけ.</p>"),

    # 13–16 farqlash
    q(f"<p>Uch yoʻlni kuchi boʻyicha tartiblang (yengildan "
      f"kuchliga).</p>",
      ["passiv shakl → お〜になる → maxsus feʼl",
       "maxsus feʼl → お〜になる → passiv shakl",
       "お〜になる → passiv shakl → maxsus feʼl",
       "Uchalasi bir xil"],
      "passiv shakl → お〜になる → maxsus feʼl",
      f"<p>Oʻzbekchada ham shunday: «keldi» → «keldilar» → "
      f"«tashrif buyurdilar».</p>"),

    q(f"<p>{SONKEIGO} ni oʻzingizga ishlatish mumkinmi?</p>",
      ["Yoʻq, hech qachon", "Ha, agar muloyim boʻlsangiz",
       "Ha, rasmiy xatda", "Faqat telefonda"],
      "Yoʻq, hech qachon",
      f"<p>Bu butun blokning asosiy qoidasi. Oʻzingiz uchun "
      f"{KENJOUGO} (PJ-70).</p>"),

    q(f"<p>{NASARU} ning ます shakli qaysi?</p>",
      [NASAIMASU, "なさります", "なされます", "なしります"],
      NASAIMASU,
      f"<p>Yana り → い. Beshta feʼl, bitta istisno.</p>"),

    q(f"<p>ます-oʻzagi kursda necha marta ishlatilgan?</p>",
      ["ます, 〜たい, 〜なさい va お〜になる — toʻrt joyda",
       "Faqat ます da", "Ikki joyda", "Beshdan ortiq joyda"],
      "ます, 〜たい, 〜なさい va お〜になる — toʻrt joyda",
      f"<p>PJ-20, PJ-39, PJ-67 va bugun. Yaʼni bu ham yangi "
      f"oʻzak emas.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi shakl mavjud EMAS?</p>",
      ["いらっしゃります", IRASSHAIMASU, OSSHAIMASU, KUDASAIMASU],
      "いらっしゃります",
      f"<p>Beshta istisno feʼlda り → い. Oddiy qoida bu shaklni "
      f"berardi, lekin u yoʻq.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{WATASHI}は{OYOMI}ます", f"{SENSEI}は{OYOMI}ます",
       f"{SENSEI}は{r('読','よ')}まれます", f"{WATASHI}は{r('読','よ')}みます"],
      f"{WATASHI}は{OYOMI}ます",
      f"<p>{SONKEIGO} oʻzingizga ishlatilmaydi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{IRASSHAIMASU} · {OKYAKU}が · もうすぐ</strong></p>",
      [f"もうすぐ{OKYAKU}が{IRASSHAIMASU}",
       f"{OKYAKU}が{IRASSHAIMASU}もうすぐ",
       f"{IRASSHAIMASU}もうすぐ{OKYAKU}が",
       f"もうすぐ{IRASSHAIMASU}{OKYAKU}が"],
      f"もうすぐ{OKYAKU}が{IRASSHAIMASU}",
      f"<p>Vaqt — ega — feʼl. Yapon gapi doim feʼl bilan "
      f"tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>てんいん:</strong> こちらの{HON}を ___ か。</p>"
      f"<p><em>(mijozga: «bu kitobni koʻrdingizmi?»)</em></p>",
      [f"ご{r('覧','らん')}になりました", f"{r('見','み')}ました",
       f"{r('拝見','はいけん')}しました", f"お{r('見','み')}になりました"],
      f"ご{r('覧','らん')}になりました",
      f"<p>Mijozning ishi — {SONKEIGO}. {r('拝見','はいけん')}する "
      f"esa {KENJOUGO}, u xodimning oʻz ishi uchun.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-67 Mashq: Buyruq va taqiq shakllari",
        "tutorial":    "PJ-67:",
        "description": "え-qator (I), ろ (II), 来い (istisno). Taqiq — "
                       "lugʻat shakli + な. Va ikkalasini ham odamga "
                       "aytmang.",
        "questions":   Q_PJ67,
        **DEFAULTS,
    },
    {
        "title":       "PJ-68 Mashq: Keigo 1 — uch tarmoq",
        "tutorial":    "PJ-68:",
        "description": "Keigo muloyimlik emas, mavqe. 尊敬語 oʻzingizga, "
                       "謙譲語 suhbatdoshga hech qachon.",
        "questions":   Q_PJ68,
        **DEFAULTS,
    },
    {
        "title":       "PJ-69 Mashq: Keigo 2 — 尊敬語",
        "tutorial":    "PJ-69:",
        "description": "Maxsus feʼl > お〜になる > passiv shakl. Va "
                       "beshta istisno feʼlda り → い.",
        "questions":   Q_PJ69,
        **DEFAULTS,
    },
]
