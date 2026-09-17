# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-82 … PJ-84.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi:
    1. IKKI XIL «KERAK». Oʻzbekchada bitta soʻz, yaponchada ikkita
       qolip. Savol «qoidami yoki vijdonmi?» degan tanlovni har
       safar qayta soʻraydi, chunki oʻquvchi uni oʻzbekchadan
       koʻrmaydi.
    2. ULANISH MAʼNONI HAL QILADI (PJ-83). ばかり uchta boshqa
       narsaga ulanadi va uchta boshqa gap chiqadi:
           ot + ばかり        — faqat shu
           て-shakli + ばかりいる — faqat shu ish
           た-shakli + ばかり   — endigina
       Testning yarmi shu ustunda turadi.
    3. TOR OYNA (PJ-84). たところ soatga, たばかり koʻngilga qaraydi.
       「先月来たところです」 — xato; 「先月来たばかりです」 — toʻgʻri.
       Va ところ **holat** feʼliga umuman tushmaydi.

⚠️ CUMULATIVE: PJ-82 mashqida ばかり (83) va ところ (84) yoʻq.
PJ-83 da ところ hali yoʻq. PJ-84 da hammasi erkin.
`verify_pj_practice_82_84.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_82_84.py --master=prime \\
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
IKU      = r("行", "い") + "く"
IKANAI   = r("行", "い") + "かない"
MAMORU   = r("守", "まも") + "る"
AYAMARU  = r("謝", "あやま") + "る"
KAESU    = r("返", "かえ") + "す"
TODOKERU = r("届", "とど") + "ける"
YOMU     = r("読", "よ") + "む"
TABERU   = r("食", "た") + "べる"
TABETA   = r("食", "た") + "べた"
MISERU   = r("見", "み") + "せる"
DASU     = r("出", "だ") + "す"
DERU     = r("出", "で") + "る"
DETA     = r("出", "で") + "た"
YASUMU   = r("休", "やす") + "む"
CHUUI    = r("注意", "ちゅうい")
ASOBU    = r("遊", "あそ") + "ぶ"
ASONDE   = r("遊", "あそ") + "んで"
KIKU     = r("聞", "き") + "く"
KIITE    = r("聞", "き") + "いて"
IU       = r("言", "い") + "う"
ITTE     = r("言", "い") + "って"
KURU     = r("来", "く") + "る"
KONAI_ST = r("来", "こ")
KITA     = r("来", "き") + "た"
KAU      = r("買", "か") + "う"
KATTA    = r("買", "か") + "った"
NOMU     = r("飲", "の") + "む"
TSUKU    = r("着", "つ") + "く"
TSUITA   = r("着", "つ") + "いた"
TSUKURU  = r("作", "つく") + "る"
TSUKUTTE = r("作", "つく") + "って"
HAIRU    = r("入", "はい") + "る"
NERU     = r("寝", "ね") + "る"
NETEIRU  = r("寝", "ね") + "ている"
SUMU     = r("住", "す") + "む"
SUNDEIRU = r("住", "す") + "んでいる"
SUNDEIMASU = r("住", "す") + "んでいます"
MIRARETA = r("見", "み") + "られた"
DEKAKERU = r("出", "で") + "かける"
UMARETA  = r("生", "う") + "まれた"
KEKKON   = r("結婚", "けっこん")
FURU     = r("降", "ふ") + "る"

# ── sifatlar ─────────────────────────────────────────────────────────
YASUI    = r("安", "やす") + "い"
YASUKU   = r("安", "やす") + "く"
TAKAI    = r("高", "たか") + "い"
GENKI    = r("元気", "げんき")
KOUHEI   = r("公平", "こうへい")
WARUI    = r("悪", "わる") + "い"
HAYAI    = r("速", "はや") + "い"

# ── otlar ────────────────────────────────────────────────────────────
YAKUSOKU = r("約束", "やくそく")
GAKUSEI  = r("学生", "がくせい")
SENSEI   = r("先生", "せんせい")
NIKKI    = r("日記", "にっき")
HITO     = r("人", "ひと")
NEDAN    = r("値段", "ねだん")
PASUPOOTO = "パスポート"
KUUKOU   = r("空港", "くうこう")
ASHITA   = r("明日", "あした")
IMA      = r("今", "いま")
IE       = r("家", "いえ")
EKI      = r("駅", "えき")
NIKU     = r("肉", "にく")
MIZU     = r("水", "みず")
KUTSU    = r("靴", "くつ")
KOUEN    = r("公園", "こうえん")
MONKU    = r("文句", "もんく")
HITORI   = r("一人", "ひとり")
DENWA    = r("電話", "でんわ")
SHUKUDAI = r("宿題", "しゅくだい")
KYOUSHITSU = r("教室", "きょうしつ")
SENGETSU = r("先月", "せんげつ")
NIHON    = r("日本", "にほん")
TOUKYOU  = r("東京", "とうきょう")
GOHAN    = "ごはん"
KYONEN   = r("去年", "きょねん")
OTOUTO   = r("弟", "おとうと")
REPOOTO  = "レポート"
TOKEI    = r("時計", "とけい")

# ── tayyor qoliplar ──────────────────────────────────────────────────
GAKUSEI_DE_ARU  = GAKUSEI + "であるべきだ"
GAKUSEI_BEKI    = GAKUSEI + "べきだ"
YASUI_BEKI      = NEDAN + "は" + YASUI + "べきだ"
YASUKU_NAKEREBA = NEDAN + "は" + YASUKU + "なければならない"
KATTA_BAKARI_NO = KATTA + "ばかりの" + KUTSU
KATTA_BAKARI    = KATTA + "ばかり" + KUTSU
ASONDE_IRU      = ASONDE + "ばかりいる"
ASONDE_ARU      = ASONDE + "ばかりある"
SENGETSU_TOKORO = SENGETSU + NIHON + "に" + KITA + "ところです"
SENGETSU_BAKARI = SENGETSU + NIHON + "に" + KITA + "ばかりです"
DEKAKERU_NI     = DEKAKERU + "ところに" + DENWA + "が" + KITA
DEKAKERU_NASHI  = DEKAKERU + "ところ" + DENWA + "が" + KITA


# ══════════════════════════════════════════════════════════════════════
# PJ-82 — 〜べきです va 〜なければならない
# ══════════════════════════════════════════════════════════════════════
Q_PJ82 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>べき feʼlga qaysi shaklda ulanadi?</p>",
      [f"{r('辞書形', 'じしょけい')} (lugʻat shakli)",
       "ない-shakli",
       "て-shakli",
       "た-shakli"],
      f"{r('辞書形', 'じしょけい')} (lugʻat shakli)",
      f"<p><strong>{r('辞書形', 'じしょけい')}</strong> — {YOMU}べきだ, "
      f"{IKU}べきだ. Feʼl guruhi muhim emas va hech qanday tovush "
      f"oʻzgarishi yoʻq: lugʻat shakli qanday boʻlsa, べき oʻshanga "
      f"yopishadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{YAKUSOKU}を"
      f"{MAMORU}___です。</strong> («vada ustidan chiqish kerak»)</p>",
      ["べき", "わけ", "はず", "こと"],
      "べき",
      f"<p><strong>{YAKUSOKU}を{MAMORU}べきです</strong>. Bu yerda "
      f"hech kim majburlamayapti — gapiruvchi shunday qilish "
      f"toʻgʻri deb baho beryapti. わけ (PJ-80) mantiqiy xulosa "
      f"chiqaradi, はず (PJ-62) esa kutishni bildiradi; ikkalasi "
      f"ham burch haqida emas.</p>"),

    q("<p>〜なければならない nimani bildiradi?</p>",
      ["Qoida yoki vaziyat majbur qiladi, tanlov yoʻq",
       "Gapiruvchi shunday qilish toʻgʻri deb hisoblaydi",
       "Ish qilinmasa ham boʻladi",
       "Ish allaqachon tugagan"],
      "Qoida yoki vaziyat majbur qiladi, tanlov yoʻq",
      f"<p><strong>Qoida yoki vaziyat majbur qiladi</strong> — "
      f"«qilmasam boʻlmaydi». Ikkinchi variant べきだ ning taʼrifi: "
      f"u vijdonning soʻzi, majburiyatning emas. Shu chegara "
      f"butun darsning asosi.</p>"),

    q(f"<p>{IKU} ning «borishim kerak» degan shakli qaysi biri?</p>",
      [f"{IKANAI[:-2]}なければならない",
       f"{r('行', 'い')}きなければならない",
       f"{IKU}なければならない",
       f"{r('行', 'い')}ってなければならない"],
      f"{IKANAI[:-2]}なければならない",
      f"<p><strong>{IKANAI[:-2]}なければならない</strong>. Uch qadam: "
      f"feʼlni ない-shakliga qoʻying ({IKANAI}), oxiridagi ない ni "
      f"なければ ga almashtiring, keyin ならない qoʻshing. ます-shakli "
      f"ham, lugʻat shakli ham bu yerga tushmaydi.</p>"),

    q("<p>〜べきではない nimani bildiradi?</p>",
      ["Qilmaslik toʻgʻri — axloqiy rad",
       "Qilish mumkin emas — qonuniy taqiq",
       "Qilish shart emas",
       "Qilish kerak edi, lekin qilinmadi"],
      "Qilmaslik toʻgʻri — axloqiy rad",
      f"<p><strong>Qilmaslik toʻgʻri</strong>: {HITO}の{NIKKI}を"
      f"{YOMU}べきではない. Bu taqiq emas — qonun ruxsat berishi "
      f"mumkin, lekin gapiruvchi buni notoʻgʻri deb hisoblaydi. "
      f"Qonuniy taqiq — PJ-33 dagi 〜てはいけない.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENSEI}は"
      f"{KOUHEI}___あるべきです。</strong></p>",
      ["で", "な", "の", "だ"],
      "で",
      f"<p><strong>{KOUHEI}であるべきです</strong> — «ustoz odil "
      f"boʻlishi kerak». Ot va な-sifat べき oldida yalangʻoch "
      f"turolmaydi: ular <strong>である</strong> ni oladi. Bu "
      f"な-sifatning ot oldidagi な si emas.</p>"),

    q(f"<p>«Narxi arzon boʻlishi kerak» — qaysi gap toʻgʻri?</p>",
      [YASUKU_NAKEREBA,
       YASUI_BEKI,
       f"{NEDAN}は{YASUKU}べきだ",
       f"{NEDAN}は{YASUI}なければならない"],
      YASUKU_NAKEREBA,
      f"<p><strong>{YASUKU_NAKEREBA}</strong>. い-sifat べき ni "
      f"umuman olmaydi, shuning uchun «kerak» maʼnosi なければならない "
      f"orqali beriladi: {YASUI} → {YASUKU}ない → {YASUKU}なければ "
      f"→ {YASUKU}なければならない.</p>"),

    q(f"<p>«Ehtiyot boʻlish kerak» — qaysi gap toʻgʻri?</p>",
      [f"{CHUUI}すべきだ",
       f"{CHUUI}しべきだ",
       f"{CHUUI}してべきだ",
       f"{CHUUI}したべきだ"],
      f"{CHUUI}すべきだ",
      f"<p><strong>{CHUUI}すべきだ</strong> — «ehtiyot boʻlish "
      f"kerak». する feʼlining ikkita shakli bor: {CHUUI}するべきだ "
      f"(kundalik) va {CHUUI}すべきだ (kitobiy, gazetada shu "
      f"turadi). Ikkalasi ham toʻgʻri; ます-shakli va て-shakli esa "
      f"べき oldiga tushmaydi.</p>"),

    q(f"<p>«Ertaroq uzr soʻrashim kerak edi, lekin soʻramadim» — "
      f"qaysi shakl?</p>",
      [f"{AYAMARU}べきだった",
       f"{AYAMARU}べきだ",
       f"{AYAMARU}べきではない",
       f"{AYAMARU[:-1]}らなければならない"],
      f"{AYAMARU}べきだった",
      f"<p><strong>{AYAMARU}べきだった</strong>. Oʻtgan zamon べき "
      f"ning oʻzidan keyin yasaladi va ichida doim «lekin "
      f"qilmadim» degan davomi bor. Shuning uchun uni alohida "
      f"aytish ham shart emas.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ASHITA}までに"
      f"{REPOOTO}を{DASU[:-1]}___。</strong> («ertagacha topshirishim "
      f"shart»)</p>",
      ["さなければなりません", "すべきです", "してもいいです",
       "さなくてもいいです"],
      "さなければなりません",
      f"<p><strong>{DASU[:-1]}さなければなりません</strong>. Muddat "
      f"belgilangan va uni kim qoʻygani muhim emas — bu tashqi "
      f"majburiyat. べきです bu yerda gʻalati eshitiladi, chunki "
      f"u vijdon haqida gapiradi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HITO}の{NIKKI}を"
      f"{YOMU}___。</strong> («oʻqish kerak emas»)</p>",
      ["べきではない", "べきだった", "べきでした", "べきだ"],
      "べきではない",
      f"<p><strong>{YOMU}べきではない</strong>. Inkor べき ning "
      f"oʻzidan keyin qoʻyiladi. なくてもいい butunlay boshqa narsani "
      f"aytadi — «oʻqimasa ham boʻladi», yaʼni erkinlik, "
      f"taqiq emas.</p>"),

    q(f"<p>«Aeroportda pasportni koʻrsatish kerak» — qaysi gap "
      f"tabiiy?</p>",
      [f"{KUUKOU}で{PASUPOOTO}を{MISERU[:-1]}なければなりません",
       f"{KUUKOU}で{PASUPOOTO}を{MISERU}べきです",
       f"{KUUKOU}で{PASUPOOTO}を{MISERU[:-1]}なくてもいいです",
       f"{KUUKOU}で{PASUPOOTO}を{MISERU}べきでした"],
      f"{KUUKOU}で{PASUPOOTO}を{MISERU[:-1]}なければなりません",
      f"<p><strong>{MISERU[:-1]}なければなりません</strong>. Qoida "
      f"tashqarida turibdi va iloj yoʻq. べきです qoʻyilsa, gap "
      f"«koʻrsatgan maʼqul» degan shaxsiy bahoga aylanadi — "
      f"aeroport qoidasi haqida bunday deyilmaydi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>«Yomon ish qilsangiz, uzr soʻrash kerak» — bu qaysi turdagi "
      f"kerak?</p>",
      [f"{AYAMARU}べきです — vijdon aytadi",
       f"{AYAMARU[:-1]}らなければなりません — qonun majbur qiladi",
       f"{AYAMARU[:-1]}らなくてもいいです — shart emas",
       f"{AYAMARU[:-1]}ってはいけません — taqiqlangan"],
      f"{AYAMARU}べきです — vijdon aytadi",
      f"<p><strong>{AYAMARU}べきです</strong>. Hech qanday qoida "
      f"uzr soʻrashga majburlamaydi — bu ichki burch. Aynan shu "
      f"joyda oʻzbekcha «kerak» ikkiga boʻlinadi va yaponcha "
      f"tanlovni talab qiladi.</p>"),

    q(f"<p>«Ertaga kelmasangiz ham boʻladi» — qaysi qolip?</p>",
      [f"{KONAI_ST}なくてもいいです",
       f"{KONAI_ST}なければなりません",
       f"{KURU}べきです",
       f"{KURU}べきではありません"],
      f"{KONAI_ST}なくてもいいです",
      f"<p><strong>{r('来', 'こ')}なくてもいいです</strong> — "
      f"erkinlik: ish qilinmasa ham hech narsa boʻlmaydi. "
      f"Bu なければなりません ning teskarisi, べきではない ning emas "
      f"— oxirgisi «kelmaslik toʻgʻri» degan bahoni beradi.</p>"),

    q("<p>Qaysi qolip afsusni bildiradi?</p>",
      ["〜べきだった", "〜べきだ", "〜べきではない",
       "〜なければならない"],
      "〜べきだった",
      f"<p><strong>〜べきだった</strong>: {AYAMARU}べきだった — "
      f"«uzr soʻrashim kerak edi». Ish qilinmagan va gapiruvchi "
      f"buni orqaga qarab tan olyapti. Qolgan uchtasi hozirgi "
      f"yoki kelasi ish haqida.</p>"),

    q(f"<p>Ustozga «koʻproq dam oling» deyish uchun qaysi gap "
      f"toʻgʻri?</p>",
      [f"{SENSEI}、もっとお{YASUMU[:-1]}みになってください",
       f"{SENSEI}はもっと{YASUMU}べきです",
       f"{SENSEI}はもっと{YASUMU[:-1]}まなければなりません",
       f"{SENSEI}はもっと{YASUMU}べきでした"],
      f"{SENSEI}、もっとお{YASUMU[:-1]}みになってください",
      f"<p><strong>お{YASUMU[:-1]}みになってください</strong> — "
      f"PJ-69 dagi {r('尊敬語', 'そんけいご')}. べき baho beradigan "
      f"soʻz, baho esa yuqoridagi odamga aytilmaydi: grammatik "
      f"jihatdan toʻgʻri boʻlsa ham, qoʻpol eshitiladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q(f"<p>Qaysi gapda xato bor?</p>",
      [YASUI_BEKI,
       f"{GAKUSEI_DE_ARU}",
       f"{YOMU}べきではない",
       f"{AYAMARU}べきだった"],
      YASUI_BEKI,
      f"<p>Xato <strong>{YASUI_BEKI}</strong> da: い-sifat べき ni "
      f"olmaydi. Toʻgʻrisi — <strong>{YASUKU_NAKEREBA}</strong>. "
      f"Qolgan uchtasi toʻgʻri: ot である oladi, inkor va oʻtgan "
      f"zamon esa べき ning oʻzidan keyin yasaladi.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [GAKUSEI_DE_ARU,
       GAKUSEI_BEKI,
       f"{GAKUSEI}なべきだ",
       f"{GAKUSEI}だべきだ"],
      GAKUSEI_DE_ARU,
      f"<p><strong>{GAKUSEI_DE_ARU}</strong>. Ot べき oldida "
      f"<strong>である</strong> ni oladi. Yalangʻoch ulanish ham, "
      f"な ham, だ ham bu yerga tushmaydi — bu わけ va はず dagi "
      f"ulanishlardan farq qiladi, shuning uchun adashish oson.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>"
      f"{HITO} / の / {NIKKI} / を / {YOMU} / べきではない</strong></p>",
      [f"{HITO}の{NIKKI}を{YOMU}べきではない",
       f"{NIKKI}の{HITO}を{YOMU}べきではない",
       f"{HITO}の{NIKKI}べきではないを{YOMU}",
       f"{YOMU}べきではない{HITO}の{NIKKI}を"],
      f"{HITO}の{NIKKI}を{YOMU}べきではない",
      f"<p><strong>{HITO}の{NIKKI}を{YOMU}べきではない</strong> — "
      f"«birovning kundaligini oʻqish kerak emas». Yapon gapi "
      f"kesim bilan tugaydi, べきではない esa kesimning oʻzi, "
      f"shuning uchun u eng oxirda turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: {SENSEI}は"
      f"とても{r('疲', 'つか')}れていますね。</strong></p>"
      f"<p><strong>パリ: ___</strong></p>",
      [f"はい。{SENSEI}、もっとお{YASUMU[:-1]}みになってください。",
       f"はい。{SENSEI}は{YASUMU}べきです。",
       f"はい。{SENSEI}は{YASUMU[:-1]}まなければなりません。",
       f"はい。{SENSEI}は{YASUMU}べきでした。"],
      f"はい。{SENSEI}、もっとお{YASUMU[:-1]}みになってください。",
      f"<p><strong>お{YASUMU[:-1]}みになってください</strong> — "
      f"ustozga toʻgʻridan-toʻgʻri aytiladigan yagona tabiiy "
      f"javob. Qolgan uchtasi unga baho beradi yoki uni "
      f"majburlaydi; ikkalasi ham hurmat kerak boʻlgan joyda "
      f"ishlamaydi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-83 — 〜ばかり va 〜たばかり
# ══════════════════════════════════════════════════════════════════════
Q_PJ83 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>ばかり ning maʼnosini nima hal qiladi?</p>",
      ["Undan oldin turgan shakl",
       "Undan keyin turgan feʼl",
       "Gapning uzunligi",
       "Gapiruvchining yoshi"],
      "Undan oldin turgan shakl",
      f"<p><strong>Undan oldin turgan shakl</strong>. Ot bilan "
      f"«faqat shu», て-shakli bilan «faqat shu ish», た-shakli "
      f"bilan «endigina» chiqadi. Soʻz bitta, ulanish uchta — "
      f"shuning uchun ばかり ni koʻrganda birinchi qarash oldingi "
      f"soʻzga tushishi kerak.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{OTOUTO}は{NIKU}___"
      f"{TABERU}。</strong> («ukam faqat goʻsht yeydi»)</p>",
      ["ばかり", "をばかり", "ばかりを", "がばかり"],
      "ばかり",
      f"<p><strong>{NIKU}ばかり{TABERU}</strong>. ばかり を va が ni "
      f"siqib chiqaradi, shuning uchun ular yonma-yon turmaydi. "
      f"Boshqa qoʻshimchalar esa qoladi: {KOUEN}でばかり{ASOBU} "
      f"— bu yerda で joyida.</p>"),

    q("<p>〜たばかり nimani bildiradi?</p>",
      ["Ish endigina tugadi",
       "Ish faqat shu odam tomonidan qilinadi",
       "Ish hali boshlanmagan",
       "Ish har doim takrorlanadi"],
      "Ish endigina tugadi",
      f"<p><strong>Ish endigina tugadi</strong>: {NIHON}に{KITA}"
      f"ばかりです — «Yaponiyaga endigina keldim». Takrorlanadigan "
      f"ish esa て-shakli bilan beriladi: 〜てばかりいる.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ASONDE}ばかり___"
      f"。</strong> («faqat oʻynab yuradi»)</p>",
      ["いる", "ある", "する", "なる"],
      "いる",
      f"<p><strong>{ASONDE_IRU}</strong>. Bu PJ-31 dagi 〜ている "
      f"ning ichiga ばかり kirgani, shuning uchun oxirida いる "
      f"turadi. Odam haqida gap ketyapti, demak ある hech qachon "
      f"toʻgʻri kelmaydi.</p>"),

    q("<p>Qaysi soʻz baho beradi, quruq chegara emas?</p>",
      ["ばかり", "だけ", "まで", "から"],
      "ばかり",
      f"<p><strong>ばかり</strong>. {MIZU}だけ{NOMU} — xotirjam "
      f"tanlov, «faqat suv ichaman». {MIZU}ばかり{NOMU} — «suv "
      f"ichaveradi», yaʼni takror va gʻalati. だけ oʻlchaydi, "
      f"ばかり esa munosabat bildiradi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KATTA}ばかり___"
      f"{KUTSU}</strong> («endigina olingan poyabzal»)</p>",
      ["の", "な", "だ", "と"],
      "の",
      f"<p><strong>{KATTA_BAKARI_NO}</strong>. たばかり ot emas, "
      f"shuning uchun otni aniqlaganda oradan <strong>の</strong> "
      f"tushadi. Xuddi shunday: {UMARETA}ばかりの{r('赤', 'あか')}ちゃん "
      f"— «endigina tugʻilgan chaqaloq».</p>"),

    q("<p>«Endigina keldim» — qaysi gap toʻgʻri?</p>",
      [f"{KITA}ばかりです",
       f"{KURU}ばかりです",
       f"{KITA[:-1]}てばかりです",
       f"{r('来', 'き')}ばかりです"],
      f"{KITA}ばかりです",
      f"<p><strong>{KITA}ばかりです</strong>. «Endigina» uchun "
      f"た-shakli kerak. Lugʻat shakli bilan gap «faqat kelish» "
      f"degan boshqa maʼnoga ogʻadi, て-shakli esa takrorni "
      f"bildiradi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KOUEN}___ばかり"
      f"{ASOBU}。</strong> («faqat bogʻda oʻynaydi»)</p>",
      ["で", "を", "が", "hech nima"],
      "で",
      f"<p><strong>{KOUEN}でばかり{ASOBU}</strong>. ばかり faqat "
      f"を va が ni siqib chiqaradi; で, に, と kabi qoʻshimchalar "
      f"joyida qoladi va ばかり ulardan keyin keladi.</p>"),

    q(f"<p>«U faqat noliydi, hech nima qilmaydi» — boʻsh joyga nima "
      f"tushadi?</p><p><strong>{r('彼', 'かれ')}は{MONKU}を___、"
      f"{r('何', 'なに')}もしない。</strong></p>",
      [f"{ITTE}ばかりいて",
       f"{IU}ばかりで",
       f"{ITTE}ばかりあって",
       f"{IU}たばかりで"],
      f"{ITTE}ばかりいて",
      f"<p><strong>{ITTE}ばかりいて</strong>. Takrorlanadigan ish "
      f"uchun て-shakli + ばかりいる kerak, va bu yerda u keyingi "
      f"gapga ulanish uchun yana て-shakliga oʻtgan: いる → いて. "
      f"Odam haqida gap ketgani uchun ある emas.</p>"),

    q(f"<p>{KYONEN}{KEKKON}したばかりです — bir yil oʻtgan boʻlsa ham "
      f"shunday deyish mumkinmi?</p>",
      ["Ha — たばかり gapiruvchining hissiga qaraydi",
       "Yoʻq — たばかり faqat bir necha daqiqaga toʻgʻri keladi",
       "Yoʻq — たばかり faqat bugungi ish haqida",
       "Ha, lekin faqat yozma tilda"],
      "Ha — たばかり gapiruvchining hissiga qaraydi",
      f"<p><strong>Mumkin.</strong> たばかり soatni emas, ishning "
      f"gapiruvchiga qanchalik «yangi» tuyulishini oʻlchaydi. "
      f"Oʻzbekcha «endigina turmush qurganmiz» ham xuddi shunday "
      f"choʻziladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{TABETA}ばかり"
      f"___、おなかがすいていない。</strong></p>",
      ["だから", "ですから", "なのに", "けれども"],
      "だから",
      f"<p><strong>{TABETA}ばかりだから</strong> — «endigina "
      f"ovqatlandim, shuning uchun qornim och emas». たばかり "
      f"koʻpincha sabab boʻlib keladi, shuning uchun undan keyin "
      f"PJ-53 dagi から va ので juda tez-tez turadi. Oddiy shaklda "
      f"から oldiga だ qoʻshiladi.</p>"),

    q(f"<p>«Bu doʻkonda faqat qimmat narsalar bor» — qaysi gap "
      f"tabiiy?</p>",
      [f"この{r('店', 'みせ')}には{TAKAI}{r('物', 'もの')}ばかりある",
       f"この{r('店', 'みせ')}には{TAKAI}{r('物', 'もの')}をばかりある",
       f"この{r('店', 'みせ')}には{TAKAI}{r('物', 'もの')}ばかりのある",
       f"この{r('店', 'みせ')}には{TAKAI}{r('物', 'もの')}たばかりある"],
      f"この{r('店', 'みせ')}には{TAKAI}{r('物', 'もの')}ばかりある",
      f"<p><strong>{TAKAI}{r('物', 'もの')}ばかりある</strong>. ばかり "
      f"sifat bilan aniqlangan otga ham toʻgʻridan-toʻgʻri "
      f"ulanadi. Ohangi yana oʻsha: «arzoni yoʻqmi?» degan "
      f"norozilik eshitiladi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>«Faqat bir kishi keldi» — qaysi gap toʻgʻri?</p>",
      [f"{HITORI}だけ{KITA}",
       f"{HITORI}ばかり{KITA}",
       f"{HITORI}ばかりの{KITA}",
       f"{HITORI}たばかり{KITA}"],
      f"{HITORI}だけ{KITA}",
      f"<p><strong>{HITORI}だけ{KITA}</strong>. Bu quruq chegara: "
      f"bitta, boshqa yoʻq. ばかり esa «koʻp» tomonga ishlaydi, "
      f"shuning uchun bitta odam haqida gʻalati eshitiladi.</p>"),

    q(f"<p>«Faqat suv ichaman» degan xotirjam gapda qaysi soʻz "
      f"turadi?</p>",
      ["だけ", "ばかり", "しか", "まで"],
      "だけ",
      f"<p><strong>だけ</strong>: {MIZU}だけ{NOMU[:-1]}みます. Bu "
      f"tanlov va chegara. ばかり qoʻyilsa, gap «suv ichaveradi» "
      f"degan bahoga aylanadi va gapiruvchi buni gʻalati deb "
      f"hisoblayotgani eshitiladi.</p>"),

    q(f"<p>«Endigina yedim» — qaysi shakl?</p>",
      [f"{TABETA}ばかりです",
       f"{TABERU[:-1]}てばかりです",
       f"{TABERU}ばかりです",
       f"{TABERU[:-1]}ばかりです"],
      f"{TABETA}ばかりです",
      f"<p><strong>{TABETA}ばかりです</strong>. た-shakli «endigina» "
      f"maʼnosini beradi. て-shakli bilan gap «faqat yeb yuradi» "
      f"degan tanqidga aylanadi — bu butunlay boshqa fikr.</p>"),

    q(f"<p>ゲームばかりする va ゲームをするばかり — qaysi biri «faqat "
      f"oʻyin oʻynaydi» degani?</p>",
      ["ゲームばかりする", "ゲームをするばかり",
       "Ikkalasi ham bir xil", "Ikkalasi ham notoʻgʻri"],
      "ゲームばかりする",
      f"<p><strong>ゲームばかりする</strong> — ばかり ot bilan "
      f"ulangan, を esa tushib qolgan. Ikkinchi gap tabiiy "
      f"yaponcha emas: {ASONDE}ばかりいる kabi て-shakli kerak "
      f"boʻlardi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [KATTA_BAKARI,
       KATTA_BAKARI_NO,
       ASONDE_IRU,
       f"{KITA}ばかりです"],
      KATTA_BAKARI,
      f"<p>Xato <strong>{KATTA_BAKARI}</strong> da: たばかり ot "
      f"emas, shuning uchun otdan oldin <strong>の</strong> shart. "
      f"Toʻgʻrisi — <strong>{KATTA_BAKARI_NO}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [ASONDE_IRU,
       ASONDE_ARU,
       f"{ASOBU}ばかりいる",
       f"{ASONDE}ばかりする"],
      ASONDE_IRU,
      f"<p><strong>{ASONDE_IRU}</strong>. Qolip — て-shakli + "
      f"ばかり + <strong>いる</strong>. Odam haqida gap ketgani "
      f"uchun ある ham, lugʻat shakli ham, する ham bu yerga "
      f"tushmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{OTOUTO} / "
      f"は / {NIKU} / ばかり / {TABERU[:-1]}ている</strong></p>",
      [f"{OTOUTO}は{NIKU}ばかり{TABERU[:-1]}ている",
       f"{OTOUTO}ばかりは{NIKU}を{TABERU[:-1]}ている",
       f"{NIKU}は{OTOUTO}ばかり{TABERU[:-1]}ている",
       f"{OTOUTO}は{TABERU[:-1]}ているばかり{NIKU}"],
      f"{OTOUTO}は{NIKU}ばかり{TABERU[:-1]}ている",
      f"<p><strong>{OTOUTO}は{NIKU}ばかり{TABERU[:-1]}ている</strong>. "
      f"ばかり toʻldiruvchidan keyin, feʼldan oldin turadi, va を "
      f"tushib qoladi. Kesim esa yapon gapida doim oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム: もう{r('昼', 'ひる')}"
      f"ごはんを{TABERU[:-1]}ますか。</strong></p>"
      f"<p><strong>イムロン: ___</strong></p>",
      [f"いいえ、{IMA}{TABETA}ばかりです。",
       f"いいえ、{IMA}{TABERU}ばかりです。",
       f"いいえ、{IMA}{TABERU[:-1]}てばかりです。",
       f"いいえ、{IMA}{TABERU[:-1]}ばかりです。"],
      f"いいえ、{IMA}{TABETA}ばかりです。",
      f"<p><strong>{IMA}{TABETA}ばかりです</strong> — «hozirgina "
      f"yedim». た-shakli kerak. て-shakli bilan javob «faqat yeb "
      f"yuraman» degan gʻalati eʼtirofga aylanadi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-84 — 〜ところ (〜るところ, 〜ているところ, 〜たところ)
# ══════════════════════════════════════════════════════════════════════
Q_PJ84 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q(f"<p>{r('所', 'ところ')} aslida qaysi maʼnodagi ot?</p>",
      ["Joy", "Vaqt", "Odam", "Sabab"],
      "Joy",
      f"<p><strong>Joy</strong>: {r('台所', 'だいどころ')} — oshxona, "
      f"{r('場所', 'ばしょ')} — joy. Bu darsda u vaqt oʻqiga "
      f"koʻchadi va ish qaysi bosqichda ekanini koʻrsatadi. "
      f"Vaqt maʼnosida odatda hiragana bilan ところ deb "
      f"yoziladi.</p>"),

    q(f"<p>{r('辞書形', 'じしょけい')} + ところだ — ish qayerda?</p>",
      ["Hali boshlanmagan", "Oʻrtasida", "Hozirgina tugagan",
       "Ancha oldin tugagan"],
      "Hali boshlanmagan",
      f"<p><strong>Hali boshlanmagan</strong>: {IE}を{DERU}ところだ "
      f"— «chiqay deb turibman», bir oyoq ostonada. Shuning uchun "
      f"bu qolip これから va もうすぐ bilan tabiiy juftlashadi.</p>"),

    q("<p>〜ているところだ — ish qayerda?</p>",
      ["Oʻrtasida — aynan hozir davom etyapti",
       "Hali boshlanmagan",
       "Hozirgina tugagan",
       "Har kuni takrorlanadi"],
      "Oʻrtasida — aynan hozir davom etyapti",
      f"<p><strong>Oʻrtasida</strong>: {IMA}、{SHUKUDAI}をしている"
      f"ところだ. Oddiy 〜ている ham toʻgʻri boʻlardi; ところ "
      f"«shu topda bandman» degan urgʻuni qoʻshadi.</p>"),

    q("<p>〜たところだ — ish qayerda?</p>",
      ["Hozirgina tugadi", "Hali boshlanmagan", "Oʻrtasida",
       "Bir oy oldin tugadi"],
      "Hozirgina tugadi",
      f"<p><strong>Hozirgina tugadi</strong>: {IMA}、{EKI}に{TSUITA}"
      f"ところです. Bir-ikki daqiqa oldin, shuning uchun {IMA} va "
      f"ちょうど bu qolip bilan doim yonma-yon yuradi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IMA}、{IE}を{DERU}"
      f"___です。</strong> («hozir chiqaman, hali chiqmadim»)</p>",
      ["ところ", "ばかり", "わけ", "はず"],
      "ところ",
      f"<p><strong>{DERU}ところです</strong>. Lugʻat shakli + ところ "
      f"ishning arafasini koʻrsatadi. ばかり (PJ-83) tugagan ishga, "
      f"わけ (PJ-80) mantiqiy xulosaga, はず (PJ-62) esa kutishga "
      f"tegishli.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IMA}、{GOHAN}を"
      f"{TSUKURU[:-1]}___ところです。</strong> («aynan hozir "
      f"pishiryapman»)</p>",
      ["っている", "る", "った", "り"],
      "っている",
      f"<p><strong>{TSUKUTTE}いるところです</strong>. «Oʻrtasida» "
      f"maʼnosi uchun て-shakli + いる kerak. Lugʻat shakli "
      f"qoʻyilsa, gap «endi pishiraman» degan arafaga aylanadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IMA}、{EKI}に"
      f"{TSUITA}___です。</strong> («hozirgina yetib keldim»)</p>",
      ["ところ", "ばかりの", "わけ", "こと"],
      "ところ",
      f"<p><strong>{TSUITA}ところです</strong>. た-shakli + ところ "
      f"— ish bir-ikki daqiqa oldin tugadi. ばかりの otdan oldin "
      f"turadi, bu yerda esa undan keyin です keladi.</p>"),

    q(f"<p>{TOUKYOU}に{SUNDEIRU}ところです — nega bu gap gʻalati?</p>",
      ["ところ holat feʼliga tushmaydi, gap «yashaydigan joy» "
       "boʻlib oʻqiladi",
       "ところ oldida た-shakli turishi kerak",
       f"{SUMU} feʼli {TOUKYOU} bilan ishlatilmaydi",
       "ところ oldida の kerak"],
      "ところ holat feʼliga tushmaydi, gap «yashaydigan joy» "
      "boʻlib oʻqiladi",
      f"<p><strong>ところ holat feʼliga tushmaydi.</strong> "
      f"{SUMU}, {r('知', 'し')}る, {r('持', 'も')}つ kabi feʼllar "
      f"bilan ところ oʻzining eski, «joy» maʼnosiga qaytadi. "
      f"Toʻgʻrisi — {TOUKYOU}に{SUNDEIMASU}.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{DEKAKERU}ところ"
      f"___{DENWA}が{KITA}。</strong></p>",
      ["に", "を", "が", "hech nima"],
      "に",
      f"<p><strong>{DEKAKERU_NI}</strong> — «chiqayotganimda "
      f"telefon keldi». ところ ot boʻlgani uchun qoʻshimchasiz "
      f"qolmaydi, va ところに «aynan oʻsha paytda uzildi» degan "
      f"maʼnoni beradi. ところへ ham boʻladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NETEIRU}ところ"
      f"___{MIRARETA}。</strong> («uxlayotganimda koʻrib "
      f"qolishdi»)</p>",
      ["を", "に", "で", "と"],
      "を",
      f"<p><strong>{NETEIRU}ところを{MIRARETA}</strong>. ところを "
      f"dan keyin koʻpincha {r('見', 'み')}る ning passiv shakli "
      f"kabi «kimdir ushlab qoldi» maʼnosidagi feʼl keladi.</p>"),

    q("<p>〜たところ bilan qaysi soʻz koʻpincha yonma-yon turadi?</p>",
      ["ちょうど", "これから", "もうすぐ", "そろそろ"],
      "ちょうど",
      f"<p><strong>ちょうど</strong> — «roppa-rosa, aynan»: "
      f"{IMA}ちょうど{TSUITA}ところです. これから va もうすぐ esa "
      f"kelajakka qaraydi, shuning uchun ular lugʻat shakli + "
      f"ところ bilan yuradi.</p>"),

    q(f"<p>{r('辞書形', 'じしょけい')} + ところ bilan qaysi soʻz "
      f"tabiiy?</p>",
      ["これから", "ちょうど", "さっき", "もう"],
      "これから",
      f"<p><strong>これから</strong> — «bundan keyin, endi»: "
      f"これから{r('昼', 'ひる')}ごはんを{TABERU}ところです. Ish hali "
      f"boshlanmagani uchun oldinga qaraydigan soʻz kerak.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENGETSU}{NIHON}に"
      f"{KITA}___です。</strong></p>",
      ["ばかり", "ところ", "ばかりの", "ところの"],
      "ばかり",
      f"<p><strong>{SENGETSU_BAKARI}</strong>. たところ faqat bir "
      f"necha daqiqaga toʻgʻri keladi, bir oyga emas. たばかり esa "
      f"soatga emas, gapiruvchining hissiga qaraydi, shuning "
      f"uchun bir oy ham «endigina» boʻladi.</p>"),

    q("<p>たところ va たばかり orasidagi farq nimada?</p>",
      ["たところ soatga, たばかり koʻngilga qaraydi",
       "たばかり soatga, たところ koʻngilga qaraydi",
       "Ikkalasi ham bir xil",
       "たところ faqat yozma tilda ishlatiladi"],
      "たところ soatga, たばかり koʻngilga qaraydi",
      f"<p><strong>たところ soatga, たばかり koʻngilga qaraydi.</strong> "
      f"Shuning uchun {SENGETSU}{TSUITA}ばかりです toʻgʻri, "
      f"{SENGETSU}{TSUITA}ところです esa notoʻgʻri. Oʻzbekcha "
      f"«hozirgina» va «endigina» aynan shu ikkiga boʻlinadi.</p>"),

    q(f"<p>«Hozir ovqatlanyapman» — qaysi gap toʻgʻri?</p>",
      [f"{IMA}、{TABERU[:-1]}ているところです",
       f"{IMA}、{TABERU}ところです",
       f"{IMA}、{TABETA}ところです",
       f"{IMA}、{TABERU}ところでした"],
      f"{IMA}、{TABERU[:-1]}ているところです",
      f"<p><strong>{TABERU[:-1]}ているところです</strong>. "
      f"«Oʻrtasida» uchun 〜ている kerak. Lugʻat shakli hali "
      f"boshlanmaganini, た-shakli esa tugaganini bildiradi — "
      f"uchtasi uch xil daqiqa.</p>"),

    q(f"<p>«Endigina yeb boʻldim» — qaysi gap toʻgʻri?</p>",
      [f"{IMA}、{TABETA}ところです",
       f"{IMA}、{TABERU}ところです",
       f"{IMA}、{TABERU[:-1]}ているところです",
       f"{IMA}、{TABERU[:-1]}ところです"],
      f"{IMA}、{TABETA}ところです",
      f"<p><strong>{TABETA}ところです</strong>. た-shakli ish "
      f"hozirgina tugaganini koʻrsatadi. Bu qolipda {IMA} va "
      f"ちょうど deyarli har doim yonida turadi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [SENGETSU_TOKORO,
       SENGETSU_BAKARI,
       DEKAKERU_NI,
       f"{IMA}、{TSUITA}ところです"],
      SENGETSU_TOKORO,
      f"<p>Xato <strong>{SENGETSU_TOKORO}</strong> da: たところ "
      f"faqat bir necha daqiqaga toʻgʻri keladi, bir oy oldingi "
      f"ishga emas. Toʻgʻrisi — <strong>{SENGETSU_BAKARI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [DEKAKERU_NI,
       DEKAKERU_NASHI,
       f"{DEKAKERU}ばかりに{DENWA}が{KITA}",
       f"{DEKAKERU}ところのに{DENWA}が{KITA}"],
      DEKAKERU_NI,
      f"<p><strong>{DEKAKERU_NI}</strong>. ところ ot, shuning "
      f"uchun undan keyin qoʻshimcha kerak — bu yerda に. "
      f"Qoʻshimchasiz qoldirish ham, ばかり qoʻyish ham gapni "
      f"buzadi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{IMA} / "
      f"{KYOUSHITSU} / に / {HAIRU} / ところ / です</strong></p>",
      [f"{IMA}{KYOUSHITSU}に{HAIRU}ところです",
       f"{KYOUSHITSU}に{IMA}ところ{HAIRU}です",
       f"{IMA}{HAIRU}ところ{KYOUSHITSU}にです",
       f"{KYOUSHITSU}ところに{IMA}{HAIRU}です"],
      f"{IMA}{KYOUSHITSU}に{HAIRU}ところです",
      f"<p><strong>{IMA}{KYOUSHITSU}に{HAIRU}ところです</strong> — "
      f"«hozir sinfga kiraman». Vaqt soʻzi boshda, joy va "
      f"qoʻshimchasi oʻrtada, kesim esa oxirida: ところです butun "
      f"gapning kesimi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: {IMA}、"
      f"{r('話', 'はな')}せますか。</strong></p>"
      f"<p><strong>ラノ: ___</strong></p>",
      [f"{IMA}{SHUKUDAI}をしているところですから、{r('後', 'あと')}で"
       f"{DENWA}します。",
       f"{IMA}{SHUKUDAI}をするところですから、{r('後', 'あと')}で"
       f"{DENWA}します。",
       f"{IMA}{SHUKUDAI}をしたところですから、{r('後', 'あと')}で"
       f"{DENWA}します。",
       f"{IMA}{SHUKUDAI}をしてばかりですから、{r('後', 'あと')}で"
       f"{DENWA}します。"],
      f"{IMA}{SHUKUDAI}をしているところですから、{r('後', 'あと')}で"
      f"{DENWA}します。",
      f"<p><strong>しているところですから</strong> — hozir bandman, "
      f"shuning uchun keyinroq. «Boshlamoqchiman» yoki «tugatdim» "
      f"desangiz, keyingi gap («keyinroq qoʻngʻiroq qilaman») "
      f"mantiqan ulanmay qoladi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-82 Mashq: 〜べきです va 〜なければならない",
        "tutorial":    "PJ-82:",
        "description": "Oʻzbekchadagi bitta «kerak» ikkiga boʻlinadi: "
                       "qoida majburlaydimi yoki vijdonmi?",
        "questions":   Q_PJ82,
        **DEFAULTS,
    },
    {
        "title":       "PJ-83 Mashq: 〜ばかり va 〜たばかり",
        "tutorial":    "PJ-83:",
        "description": "Bitta soʻz, uchta ulanish, uchta maʼno — "
                       "va ばかり bilan だけ orasidagi ohang farqi.",
        "questions":   Q_PJ83,
        **DEFAULTS,
    },
    {
        "title":       "PJ-84 Mashq: 〜ところ",
        "tutorial":    "PJ-84:",
        "description": "Ish oʻqidagi uchta nuqta — arafa, oʻrta, "
                       "hozirgina — va たところ bilan たばかり farqi.",
        "questions":   Q_PJ84,
        **DEFAULTS,
    },
]
