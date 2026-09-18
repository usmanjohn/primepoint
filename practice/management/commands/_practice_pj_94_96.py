# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-94 … PJ-96.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi:
    1. YOʻNALISH (PJ-94). どころか RAD ETADI, ばかりか QOʻSHADI.
       Oʻzbek oʻquvchisi どころ ni «oʻrin» degan otdan chiqarib
       «…dan tashqari» deb oʻqiydi va maʼnoni teskari tushunadi.
       Testning uchdan biri shu ustunda.
    2. ZAMON (PJ-95). とたん — た-shakli, oxiri OʻTGAN zamon.
       次第 — ます-oʻzagi, oxiri KELASI zamon. Oʻzbekcha «…ishi
       bilan» ikkalasini ham koʻtaradi, shuning uchun savol har
       safar gapning OXIRIGA qaratiladi.
    3. REGISTR (PJ-96). Bu uslub darsi, shuning uchun savollar
       «toʻgʻrimi?» emas, «qayerda?» deb soʻraydi — bittadan
       tashqari: bitta matn ichida registr aralashmaydi, va
       oʻsha yagona qatʼiy qoida ikki savolda tekshiriladi.

⚠️ CUMULATIVE: PJ-94 mashqida とたん・次第 (95) va である体 (96)
yoʻq. PJ-95 da である体 hali yoʻq. PJ-97…100 dan hech narsa yoʻq
(拝啓・敬具, 四字熟語, ことわざ, 和語・漢語・外来語).
`verify_pj_practice_94_96.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_94_96.py --master=prime \\
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


# ── otlar ────────────────────────────────────────────────────────────
KANJI    = r("漢字", "かんじ")
EIGO     = r("英語", "えいご")
NIHONGO  = r("日本語", "にほんご")
RYOKOU   = r("旅行", "りょこう")
SHIKEN   = r("試験", "しけん")
RAISHUU  = r("来週", "らいしゅう")
MISE     = r("店", "みせ")
HITO     = r("人", "ひと")
KYONEN   = r("去年", "きょねん")
ICHIJIKAN = r("一時間", "いちじかん")
SANJIKAN = r("三時間", "さんじかん")
AME      = r("雨", "あめ")
KAZE     = r("風", "かぜ")
EKI      = r("駅", "えき")
DENWA    = r("電話", "でんわ")
NEKO     = r("猫", "ねこ")
RENRAKU  = r("連絡", "れんらく")
TOUCHAKU = r("到着", "とうちゃく")
KYOUSHITSU = r("教室", "きょうしつ")
GAKUSEI  = r("学生", "がくせい")
MONDAI   = r("問題", "もんだい")
CHOUSA   = r("調査", "ちょうさ")
KEKKA    = r("結果", "けっか")
RIYUU    = r("理由", "りゆう")
SHINEKI  = r("新", "しん") + r("駅", "えき")
RAISHUN  = r("来春", "らいしゅん")
KAIGYOU  = r("開業", "かいぎょう")
TAIFUU   = r("台風", "たいふう")
KYUUSHUU = r("九州", "きゅうしゅう")
JOURIKU  = r("上陸", "じょうりく")
NIKKI    = r("日記", "にっき")
RONBUN   = r("論文", "ろんぶん")
ICHIMON  = r("一問", "いちもん")
TAI      = r("体", "たい")
SHIDAI   = r("次第", "しだい")
TOTAN    = r("途端", "とたん")

# ── feʼllar / sifatlar ───────────────────────────────────────────────
YOMENAI  = r("読", "よ") + "めない"
HANASERU = r("話", "はな") + "せる"
HETTEIRU = r("減", "へ") + "っている"
HERU     = r("減", "へ") + "る"
FUETEIRU = r("増", "ふ") + "えている"
YASUI    = r("安", "やす") + "い"
TAKAKATTA = r("高", "たか") + "かった"
MATTA    = r("待", "ま") + "った"
TSUYOKU  = r("強", "つよ") + "くなった"
FUTTA    = r("降", "ふ") + "った"
FURIDASHITA = r("降", "ふ") + "り" + r("出", "だ") + "した"
AKETA    = r("開", "あ") + "けた"
AKERU    = r("開", "あ") + "ける"
TOBIDASHITA = r("飛", "と") + "び" + r("出", "だ") + "した"
TSUITA   = r("着", "つ") + "いた"
TSUKU    = r("着", "つ") + "く"
TSUKI    = r("着", "つ") + "き"
NARU     = r("鳴", "な") + "る"
NARANAI  = r("鳴", "な") + "らない"
DETA     = r("出", "で") + "た"
TACHIAGATTA = r("立", "た") + "ち" + r("上", "あ") + "がった"
TACHIAGARU  = r("立", "た") + "ち" + r("上", "あ") + "がる"
KURAKU   = r("暗", "くら") + "くなった"
MENOMAE  = r("目", "め") + "の" + r("前", "まえ")
KUWASHII = r("詳", "くわ") + "しい"
OSHIRASE = "お" + r("知", "し") + "らせします"
SHIZUKA  = r("静", "しず") + "か"
OOKII    = r("大", "おお") + "きい"
IKU      = r("行", "い") + "く"
IKIMASU  = r("行", "い") + "きます"
KANTAN   = r("簡単", "かんたん")
OMOU     = r("思", "おも") + "う"
OMOIMASU = r("思", "おも") + "います"
KANGAERU = r("考", "かんが") + "える"
WAKARANAKATTA = r("分", "わ") + "からなかった"
CHIKAI   = r("近", "ちか") + "い"
FURU     = r("降", "ふ") + "る"
SUKOSHI  = r("少", "すこ") + "し"
ONAJI    = r("同", "おな") + "じ"
MITE     = r("見", "み") + "て"
OSHIETE  = r("教", "おし") + "えて"
KURAKU_NARIMASHOU   = r("暗", "くら") + "くなりましょう"
KURAKU_TSUMORI      = r("暗", "くら") + "くなるつもりだ"
OSHIRASE_SHITA      = "お" + r("知", "し") + "らせしました"
OSHIRASE_SHITEIRU   = "お" + r("知", "し") + "らせしています"
OSHIRASE_MASEN      = "お" + r("知", "し") + "らせしませんでした"
TSUITE   = r("着", "つ") + "いて"
TSUKANAI = r("着", "つ") + "かない"
AKETE    = r("開", "あ") + "けて"
AKEMASU  = r("開", "あ") + "けます"
TACHIAGARI = r("立", "た") + "ち" + r("上", "あ") + "がり"
TACHIAGATTE = r("立", "た") + "ち" + r("上", "あ") + "がって"


# ══════════════════════════════════════════════════════════════════════
# PJ-94 — 〜どころか va 〜ばかりか
# ══════════════════════════════════════════════════════════════════════
Q_PJ94 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜どころか nimani bildiradi?</p>",
      ["… u yoqda tursin; aksincha",
       "… dan tashqari, … ham",
       "… ning oʻrniga",
       "… boʻlishi bilan"],
      "… u yoqda tursin; aksincha",
      f"<p><strong>… u yoqda tursin.</strong> {KANJI}どころか、"
      f"ひらがなも{YOMENAI} — «kanji u yoqda tursin, hiraganani "
      f"ham oʻqiy olmaydi». Diqqat: «… dan tashqari» aynan "
      f"<strong>teskarisi</strong> — u qoʻshadi, どころか esa "
      f"rad etadi.</p>"),

    q("<p>〜ばかりか nimani bildiradi?</p>",
      ["Ustiga-ustak, … ham",
       "… u yoqda tursin",
       "Faqat … (atigi)",
       "Endigina … qildi"],
      "Ustiga-ustak, … ham",
      f"<p><strong>Ustiga-ustak.</strong> {AME}が{FUTTA}ばかりか、"
      f"{KAZE}も{TSUYOKU} — «yomgʻir yogʻdi, ustiga-ustak shamol "
      f"ham kuchaydi». Birinchi qism rad etilmaydi; u haqiqat, "
      f"va ustiga yana bittasi qoʻshiladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KANJI}どころか、"
      f"ひらがな___{YOMENAI}。</strong></p>",
      ["も", "は", "が", "を"],
      "も",
      f"<p><strong>も</strong>. どころか ning ikkinchi qismida "
      f"deyarli doim <strong>も</strong> turadi — «hiraganani "
      f"<em>ham</em>». Uni tushirib qoldirish bu qolipning eng "
      f"koʻp uchraydigan xatosi.</p>"),

    q(f"<p>«Keyingi hafta imtihon bor, sayohat qayoqda» — qaysi gap "
      f"toʻgʻri?</p>",
      [f"{RAISHUU}{SHIKEN}があるから、{RYOKOU}どころではない",
       f"{RAISHUU}{SHIKEN}があるから、{RYOKOU}どころか",
       f"{RAISHUU}{SHIKEN}があるから、{RYOKOU}ばかりか",
       f"{RAISHUU}{SHIKEN}があるから、{RYOKOU}ではない"],
      f"{RAISHUU}{SHIKEN}があるから、{RYOKOU}どころではない",
      f"<p><strong>{RYOKOU}どころではない</strong>. Bu alohida "
      f"qolib qotgan qolip: «… qayoqda», «… ning payti emas». "
      f"Oddiy <strong>{RYOKOU}ではない</strong> boʻlsa «bu sayohat "
      f"emas» degan butunlay boshqa gap chiqadi.</p>"),

    q("<p>どころか dan keyingi qism qanday boʻladi?</p>",
      ["Kutilganning aksi, kuchliroq narsa",
       "Birinchisi bilan bir xil darajadagi narsa",
       "Birinchisining sababi",
       "Birinchisining vaqti"],
      "Kutilganning aksi, kuchliroq narsa",
      f"<p><strong>Kutilganning aksi.</strong> {HITO}が{HERU}"
      f"どころか、{KYONEN}より{FUETEIRU} — kutilgani kamayish "
      f"edi, haqiqat esa koʻpayish. Ikkinchi qism birinchisidan "
      f"kuchsizroq boʻlsa, qolip buziladi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHIZUKA}___"
      f"どころか、うるさかった。</strong></p>",
      ["(hech narsa)", "な", "の", "だ"],
      "(hech narsa)",
      f"<p><strong>Hech narsa</strong>: {SHIZUKA}どころか. "
      f"どころか な-sifatning <strong>な</strong> sini tushiradi. "
      f"Bu ばかりか bilan yagona ulanish farqi — u esa aksincha, "
      f"<strong>な</strong> ni saqlaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHIZUKA}___"
      f"ばかりか、{EKI}にも{CHIKAI}。</strong></p>",
      ["な", "(hech narsa)", "の", "で"],
      "な",
      f"<p><strong>な</strong>: {SHIZUKA}なばかりか. ばかりか "
      f"な-sifatdan keyin <strong>な</strong> talab qiladi. "
      f"Bitta qatorni yodlang: {SHIZUKA}<strong>どころか</strong> "
      f"lekin {SHIZUKA}<strong>な</strong>ばかりか.</p>"),

    q(f"<p>«Bir soat u yoqda tursin, uch soat kutdim» — qaysi gap "
      f"toʻgʻri?</p>",
      [f"{ICHIJIKAN}どころか、{SANJIKAN}も{MATTA}",
       f"{ICHIJIKAN}ばかりか、{SANJIKAN}も{MATTA}",
       f"{SANJIKAN}どころか、{ICHIJIKAN}も{MATTA}",
       f"{ICHIJIKAN}どころで、{SANJIKAN}も{MATTA}"],
      f"{ICHIJIKAN}どころか、{SANJIKAN}も{MATTA}",
      f"<p><strong>{ICHIJIKAN}どころか、{SANJIKAN}も{MATTA}</strong>. "
      f"どころか ikkala yoʻnalishga ham ishlaydi — kattadan "
      f"kichikka ham, kichikdan kattaga ham. Muhimi: ikkinchi "
      f"qism <strong>kuchliroq</strong> boʻlsin. Uch soatni "
      f"oldinga qoʻysangiz maʼno teskari boʻlib ketadi.</p>"),

    q(f"<p>Davomi qaysi biri boʻlishi mumkin?</p>"
      f"<p><strong>{HITO}が{HERU}どころか、___。</strong></p>",
      [f"{KYONEN}より{FUETEIRU}",
       f"{KYONEN}より{SUKOSHI}{HETTEIRU}",
       f"{KYONEN}と{ONAJI}だ",
       f"{KYONEN}から{HETTEIRU}"],
      f"{KYONEN}より{FUETEIRU}",
      f"<p><strong>{KYONEN}より{FUETEIRU}</strong>. どころか "
      f"kutilganni rad etadi, shuning uchun davomi "
      f"<strong>teskari</strong> boʻlishi shart. «Ozroq kamaydi» "
      f"yoki «bir xil» degan javoblar rad etish emas — ular "
      f"bilan qolip ishlamaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>その{MISE}は"
      f"{YASUI}どころか、とても___。</strong></p>",
      [TAKAKATTA, YASUI, f"{YASUI}です", f"{YASUI}かった"],
      TAKAKATTA,
      f"<p><strong>{TAKAKATTA}</strong>. «Arzon boʻlish u yoqda "
      f"tursin, juda qimmat edi». い-sifat どころか oldida "
      f"oʻzgarmaydi ({YASUI}どころか), davomi esa kutilganning "
      f"aksi boʻladi.</p>"),

    q(f"<p>{AME}が{FUTTA}ばかりか、{KAZE}も{TSUYOKU}。 — bu gap nima "
      f"deyapti?</p>",
      ["Yomgʻir yogʻdi va ustiga shamol ham kuchaydi",
       "Yomgʻir yogʻmadi, faqat shamol kuchaydi",
       "Yomgʻir yogʻishi bilan shamol tindi",
       "Yomgʻir yogʻdi, lekin shamol tinch edi"],
      "Yomgʻir yogʻdi va ustiga shamol ham kuchaydi",
      f"<p><strong>Ikkalasi ham boʻldi.</strong> ばかりか birinchi "
      f"qismni <strong>rad etmaydi</strong> — u haqiqat, va "
      f"ustiga yana bittasi qoʻshiladi. Agar shu gapda どころか "
      f"tursa, maʼno butunlay oʻzgarardi.</p>"),

    q(f"<p>«Sayohat qayoqda edi» — oʻtgan zamonda qanday "
      f"yoziladi?</p>",
      [f"{RYOKOU}どころではありませんでした",
       f"{RYOKOU}どころじゃありませんでした",
       f"{RYOKOU}でしたどころではない",
       f"{RYOKOU}どころでしたではない"],
      f"{RYOKOU}どころではありませんでした",
      f"<p><strong>{RYOKOU}どころではありませんでした</strong>. "
      f"Qolipning oʻzi <strong>どころではない</strong>, va zamon "
      f"uning <em>oxiriga</em> qoʻyiladi. «どころじゃありません» "
      f"— gapdagi yumshoq shaklning notoʻgʻri aralashmasi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>«Pari ingliz tilidan tashqari yapon tilida ham "
      f"gapiradi» — qaysi qolip?</p>",
      ["ばかりか", "どころか", "どころではない", "しか〜ない"],
      "ばかりか",
      f"<p><strong>ばかりか</strong>: パリさんは{EIGO}ばかりか、"
      f"{NIHONGO}も{HANASERU}。 Bu yerda ingliz tili "
      f"<strong>rad etilmayapti</strong> — u bor, va ustiga yana "
      f"bittasi bor. どころか qoʻysangiz, «ingliz tili u yoqda "
      f"tursin» degan teskari gap chiqadi.</p>"),

    q("<p>だけでなく va ばかりか — farqi nimada?</p>",
      ["Maʼnosi bir xil, ohangi boshqa: ばかりか da hayrat bor",
       "Maʼnosi qarama-qarshi",
       "だけでなく faqat feʼl bilan, ばかりか faqat ot bilan keladi",
       "ばかりか faqat inkor gapda ishlatiladi"],
      "Maʼnosi bir xil, ohangi boshqa: ばかりか da hayrat bor",
      f"<p><strong>Ohang.</strong> {EIGO}だけでなく — quruq "
      f"sanash, hisobotga yaraydi. {EIGO}ばかりか — «buni ham "
      f"deysizmi!», gapiruvchining hayrati eshitiladi va u "
      f"koʻproq yozma tilda uchraydi.</p>"),

    q(f"<p>{RYOKOU}ではない va {RYOKOU}どころではない — farqi "
      f"nimada?</p>",
      ["Birinchisi «bu sayohat emas», ikkinchisi «hozir sayohatning payti emas»",
       "Ikkalasi ham bir xil maʼnoni beradi",
       "Birinchisi yozma, ikkinchisi ogʻzaki shakl",
       "Birinchisi oʻtgan, ikkinchisi kelasi zamon"],
      "Birinchisi «bu sayohat emas», ikkinchisi «hozir sayohatning payti emas»",
      f"<p><strong>Butunlay boshqa gaplar.</strong> Oddiy "
      f"<strong>ではない</strong> narsani inkor qiladi. "
      f"<strong>どころではない</strong> esa narsani emas, "
      f"<em>vaziyatni</em> aytadi: «bu haqda soʻrashning oʻzi "
      f"ortiqcha».</p>"),

    q("<p>どころか ni oʻzbekchaga qaysi ibora aniq tarjima "
      "qiladi?</p>",
      ["… u yoqda tursin", "… dan tashqari", "… ning oʻrniga",
       "… boʻlsa ham"],
      "… u yoqda tursin",
      f"<p><strong>«… u yoqda tursin».</strong> Ikkala tilda ham "
      f"bu ibora otdan <em>keyin</em> turadi, shuning uchun "
      f"tarjimada soʻz tartibini oʻzgartirish ham shart emas. "
      f"«… dan tashqari» esa aynan teskarisi — u ばかりか.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gap toʻgʻri?</p>",
      [f"{SHIZUKA}どころか、うるさかった",
       f"{SHIZUKA}などころか、うるさかった",
       f"{SHIZUKA}だどころか、うるさかった",
       f"{SHIZUKA}のどころか、うるさかった"],
      f"{SHIZUKA}どころか、うるさかった",
      f"<p><strong>{SHIZUKA}どころか</strong>. どころか な-sifatga "
      f"toʻgʻridan-toʻgʻri ulanadi — oraga <strong>な</strong> ham, "
      f"<strong>だ</strong> ham, <strong>の</strong> ham "
      f"qoʻyilmaydi.</p>"),

    q("<p>Qaysi gapda xato bor?</p>",
      [f"{AME}が{FURU}ばかり、{KAZE}も{TSUYOKU}",
       f"{AME}が{FUTTA}ばかりか、{KAZE}も{TSUYOKU}",
       f"{KANJI}どころか、ひらがなも{YOMENAI}",
       f"{HITO}が{HERU}どころか、{FUETEIRU}"],
      f"{AME}が{FURU}ばかり、{KAZE}も{TSUYOKU}",
      f"<p>Xato — <strong>ばかり</strong> da: oxiridagi "
      f"<strong>か</strong> tushib qolgan. か siz bu PJ-83 dagi "
      f"butunlay boshqa qolip boʻlib qoladi («endigina yogʻdi»). "
      f"Toʻgʻrisi: {AME}が{FUTTA}<strong>ばかりか</strong>.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: "
      f"<strong>ひらがなも · {KANJI}どころか · {YOMENAI}</strong></p>",
      [f"{KANJI}どころか、ひらがなも{YOMENAI}",
       f"ひらがなも{KANJI}どころか、{YOMENAI}",
       f"{YOMENAI}、{KANJI}どころか、ひらがなも",
       f"ひらがなも{YOMENAI}、{KANJI}どころか"],
      f"{KANJI}どころか、ひらがなも{YOMENAI}",
      f"<p><strong>{KANJI}どころか、ひらがなも{YOMENAI}</strong>. "
      f"どころか birinchi qismning oxirida turadi, kesim esa "
      f"yapon tilida har doim gapning eng oxirida. Ikkinchi "
      f"qismdagi <strong>も</strong> ham oʻz otidan keyin "
      f"qoladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> {SHIKEN}は{KANTAN}でしたか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{KANTAN}どころか、{ICHIMON}も{WAKARANAKATTA}です",
       f"{KANTAN}ばかりか、{ICHIMON}も{WAKARANAKATTA}です",
       f"{KANTAN}どころではない、{ICHIMON}も{WAKARANAKATTA}です",
       f"{KANTAN}でしたどころか、{ICHIMON}も{WAKARANAKATTA}です"],
      f"{KANTAN}どころか、{ICHIMON}も{WAKARANAKATTA}です",
      f"<p><strong>{KANTAN}どころか、{ICHIMON}も"
      f"{WAKARANAKATTA}です</strong> — «oson u yoqda tursin, "
      f"bitta savolni ham tushunmadim». ばかりか bu yerda "
      f"toʻgʻri kelmaydi: u «oson edi, ustiga …» degan maʼnoni "
      f"berardi, bu esa javobning ohangiga zid.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-95 — 〜たとたん, 〜次第, 〜か〜ないかのうちに
# ══════════════════════════════════════════════════════════════════════
Q_PJ95 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜とたん qaysi shaklga ulanadi?</p>",
      ["た-shakliga", "ます-oʻzagiga", "lugʻat shakliga", "ない-shakliga"],
      "た-shakliga",
      f"<p><strong>た-shakliga</strong>: {AKETA}とたん. Bu qolip "
      f"tugagan voqeani aytadi, shuning uchun ulanishi ham "
      f"oʻtgan zamon shakli. Lugʻat shakli ({AKERU}とたん) "
      f"— xato.</p>"),

    q(f"<p>〜{SHIDAI} qaysi shaklga ulanadi?</p>",
      ["ます-oʻzagiga yoki otga", "た-shakliga", "lugʻat shakliga",
       "て-shakliga"],
      "ます-oʻzagiga yoki otga",
      f"<p><strong>ます-oʻzagiga</strong>: {TSUKI}{SHIDAI} "
      f"({TSUKU} → {TSUKI}ます → {TSUKI}). Otga ham ulanadi: "
      f"{RENRAKU}{SHIDAI}, {TOUCHAKU}{SHIDAI}.</p>"),

    q("<p>〜とたん dan keyingi gap qaysi zamonda boʻladi?</p>",
      ["Oʻtgan zamonda", "Kelasi zamonda", "Lugʻat shaklida",
       "Har qanday zamonda"],
      "Oʻtgan zamonda",
      f"<p><strong>Oʻtgan zamonda.</strong> とたん "
      f"<em>kutilmagan</em> voqeani aytadi, kutilmagan narsa esa "
      f"allaqachon boʻlib oʻtgan boʻladi: {AKETA}とたん、{NEKO}が"
      f"{TOBIDASHITA}。</p>"),

    q(f"<p>〜{SHIDAI} dan keyingi gap qaysi zamonda boʻladi?</p>",
      ["Kelasi zamonda — niyat, iltimos yoki reja",
       "Oʻtgan zamonda", "Faqat inkorda", "Faqat lugʻat shaklida"],
      "Kelasi zamonda — niyat, iltimos yoki reja",
      f"<p><strong>Kelasi zamonda.</strong> {TSUKI}{SHIDAI}、"
      f"{DENWA}します — «yetishim bilan qoʻngʻiroq qilaman». "
      f"{SHIDAI} dan keyin <strong>oʻtgan zamon boʻlmaydi</strong> "
      f"— bu qolipning eng qatʼiy qoidasi.</p>"),

    q("<p>〜か〜ないかのうちに qanday tuziladi?</p>",
      ["lugʻat shakli + か + ない-shakli + かのうちに",
       "た-shakli + か + ない-shakli + うちに",
       "ます-oʻzagi + か + ない-shakli + のうちに",
       "て-shakli + か + ない-shakli + かのうちに"],
      "lugʻat shakli + か + ない-shakli + かのうちに",
      f"<p><strong>lugʻat shakli + か + ない-shakli + かのうちに</strong>: "
      f"{NARU}か{NARANAI}かのうちに. Bitta feʼl ikki marta "
      f"yoziladi — biri tasdiqda, biri inkorda, xuddi oʻzbekcha "
      f"«chalinar-chalinmas» dagidek.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>ドアを___とたん、"
      f"{NEKO}が{TOBIDASHITA}。</strong></p>",
      [AKETA, AKERU, AKETE, AKEMASU],
      AKETA,
      f"<p><strong>{AKETA}</strong>. とたん faqat "
      f"<strong>た-shakliga</strong> ulanadi. Qolgan uch shakl "
      f"— lugʻat, て va ます — bu qolipda ishlamaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{EKI}に___"
      f"{SHIDAI}、{DENWA}します。</strong></p>",
      [TSUKI, TSUKU, TSUITA, TSUITE],
      TSUKI,
      f"<p><strong>{TSUKI}</strong>. {TSUKI}ます dan ます tushadi "
      f"va oʻzak qoladi. Lugʻat shakli ({TSUKU}{SHIDAI}) ham, "
      f"た-shakli ({TSUITA}{SHIDAI}) ham bu yerga tushmaydi.</p>"),

    q(f"<p>{RENRAKU} soʻziga {SHIDAI} ni ulang.</p>",
      [f"{RENRAKU}{SHIDAI}", f"{RENRAKU}の{SHIDAI}",
       f"{RENRAKU}し{SHIDAI}", f"{RENRAKU}した{SHIDAI}"],
      f"{RENRAKU}{SHIDAI}",
      f"<p><strong>{RENRAKU}{SHIDAI}</strong>. する bilan feʼl "
      f"boʻladigan otlarga {SHIDAI} toʻgʻridan-toʻgʻri yopishadi "
      f"— oraga <strong>の</strong> ham, <strong>し</strong> ham "
      f"qoʻyilmaydi. Eʼlonlarda juda koʻp uchraydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>ベルが{NARU}___"
      f"{NARANAI}かのうちに、みんな{KYOUSHITSU}を{DETA}。</strong></p>",
      ["か", "が", "と", "は"],
      "か",
      f"<p><strong>か</strong>: {NARU}<strong>か</strong>{NARANAI}"
      f"かのうちに. Qolipda <strong>か</strong> ikki marta "
      f"keladi — biri feʼlning tasdiq shaklidan keyin, biri "
      f"inkor shaklidan keyin.</p>"),

    q(f"<p>Davomi qaysi biri boʻlishi mumkin?</p>"
      f"<p><strong>{TACHIAGATTA}とたん、___。</strong></p>",
      [f"{MENOMAE}が{KURAKU}",
       f"{MENOMAE}が{KURAKU_NARIMASHOU}",
       f"{MENOMAE}を{MITE}ください",
       f"{MENOMAE}が{KURAKU_TSUMORI}"],
      f"{MENOMAE}が{KURAKU}",
      f"<p><strong>{MENOMAE}が{KURAKU}</strong>. とたん dan keyin "
      f"faqat oʻtgan zamondagi xabar keladi. «…ましょう» (niyat), "
      f"«…ください» (iltimos) va «…つもりだ» (reja) — uchalasi "
      f"ham taqiqlangan, chunki とたん kutilmagan voqeani "
      f"aytadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KUWASHII}ことが"
      f"わかり{SHIDAI}、___。</strong></p>",
      [OSHIRASE, OSHIRASE_SHITA,
       OSHIRASE_SHITEIRU, OSHIRASE_MASEN],
      OSHIRASE,
      f"<p><strong>{OSHIRASE}</strong>. {SHIDAI} dan keyin "
      f"<strong>kelasi zamon</strong> keladi. Oʻtgan zamondagi "
      f"uch variant ham qolipni buzadi, qanchalik hurmatli "
      f"boʻlsa ham.</p>"),

    q(f"<p>«Yetib kelishim bilanoq yomgʻir yogʻa boshladi» — qaysi "
      f"gap toʻgʻri?</p>",
      [f"{TSUITA}とたん、{AME}が{FURIDASHITA}",
       f"{TSUKI}{SHIDAI}、{AME}が{FURIDASHITA}",
       f"{TSUKU}とたん、{AME}が{FURIDASHITA}",
       f"{TSUKI}{SHIDAI}、{AME}が{FURU}"],
      f"{TSUITA}とたん、{AME}が{FURIDASHITA}",
      f"<p><strong>{TSUITA}とたん</strong>. Gap oʻtgan zamonda "
      f"tugayapti va voqea kutilmagan — demak とたん, va u "
      f"<strong>た-shakliga</strong> ulanadi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>«Yetib kelishingiz bilan qoʻngʻiroq qiling» — qaysi gap "
      f"toʻgʻri?</p>",
      [f"{TSUKI}{SHIDAI}、{DENWA}してください",
       f"{TSUITA}とたん、{DENWA}してください",
       f"{TSUKU}か{TSUKANAI}かのうちに、{DENWA}してください",
       f"{TSUITA}{SHIDAI}、{DENWA}してください"],
      f"{TSUKI}{SHIDAI}、{DENWA}してください",
      f"<p><strong>{TSUKI}{SHIDAI}</strong>. «…てください» — "
      f"iltimos, yaʼni kelasi zamon. とたん dan keyin iltimos "
      f"kela olmaydi, chunki u kutilmagan voqeani aytadi.</p>"),

    q(f"<p>とたん va {SHIDAI} ni ajratish uchun gapning qayeriga "
      f"qaraysiz?</p>",
      ["Oxiriga — qaysi zamonda tugaganiga",
       "Boshiga — qaysi ot turganiga",
       "Oʻrtasiga — qaysi qoʻshimcha borligiga",
       "Feʼlning guruhiga"],
      "Oxiriga — qaysi zamonda tugaganiga",
      f"<p><strong>Oxiriga.</strong> Oʻtgan zamonda tugasa — "
      f"とたん. Kelasi zamon, iltimos yoki niyat bilan tugasa — "
      f"{SHIDAI}. Qolipni gapning boshidan topib boʻlmaydi.</p>"),

    q("<p>〜てすぐ va 〜たとたん — farqi nimada?</p>",
      ["とたん da voqea kutilmagan boʻlishi shart, てすぐ da esa shart emas",
       "てすぐ faqat yozma tilda ishlatiladi",
       "とたん kelasi zamon bilan keladi",
       "Ikkalasi ham bir xil, farqi yoʻq"],
      "とたん da voqea kutilmagan boʻlishi shart, てすぐ da esa shart emas",
      f"<p><strong>Kutilmaganlik.</strong> {TSUITE}すぐ"
      f"{DENWA}した — oddiy «darrov», hech qanday shart yoʻq va "
      f"bu gapiruvchining oʻz ishi. {TSUITA}とたん、{AME}が"
      f"{FURIDASHITA} — kutilmagan va gapiruvchining "
      f"ixtiyorida emas.</p>"),

    q(f"<p>Qaysi gapda {SHIDAI} kerak?</p>",
      [f"{TOUCHAKU}___、{RENRAKU}します",
       f"ドアを{AKETA}___、{NEKO}が{TOBIDASHITA}",
       f"{TACHIAGATTA}___、{MENOMAE}が{KURAKU}",
       f"ベルが{NARU}か{NARANAI}___、みんな{DETA}"],
      f"{TOUCHAKU}___、{RENRAKU}します",
      f"<p><strong>{TOUCHAKU}{SHIDAI}、{RENRAKU}します</strong> — "
      f"yagona kelasi zamonda tugaydigan gap. Qolgan uchtasi "
      f"oʻtgan zamonda, demak ularga とたん yoki "
      f"か〜ないかのうちに kerak.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [f"{TSUKU}{SHIDAI}、{DENWA}します",
       f"{TSUKI}{SHIDAI}、{DENWA}します",
       f"{TSUITA}とたん、{AME}が{FURIDASHITA}",
       f"{RENRAKU}{SHIDAI}、{OSHIRASE}"],
      f"{TSUKU}{SHIDAI}、{DENWA}します",
      f"<p>Xato — <strong>{TSUKU}{SHIDAI}</strong> da: "
      f"{SHIDAI} lugʻat shakliga emas, <strong>ます-oʻzagiga</strong> "
      f"ulanadi. Toʻgʻrisi <strong>{TSUKI}{SHIDAI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [f"{TACHIAGATTA}とたん、{MENOMAE}が{KURAKU}",
       f"{TACHIAGARU}とたん、{MENOMAE}が{KURAKU}",
       f"{TACHIAGARI}とたん、{MENOMAE}が{KURAKU}",
       f"{TACHIAGATTE}とたん、{MENOMAE}が{KURAKU}"],
      f"{TACHIAGATTA}とたん、{MENOMAE}が{KURAKU}",
      f"<p><strong>{TACHIAGATTA}とたん</strong>. とたん faqat "
      f"<strong>た-shakliga</strong> ulanadi — lugʻat shakli, "
      f"ます-oʻzagi va て-shakli bu yerda ishlamaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: "
      f"<strong>みんな{KYOUSHITSU}を{DETA} · {NARANAI}かのうちに · "
      f"ベルが{NARU}か</strong></p>",
      [f"ベルが{NARU}か{NARANAI}かのうちに、みんな{KYOUSHITSU}を{DETA}",
       f"みんな{KYOUSHITSU}を{DETA}、ベルが{NARU}か{NARANAI}かのうちに",
       f"ベルが{NARU}か、みんな{KYOUSHITSU}を{DETA}、{NARANAI}かのうちに",
       f"{NARANAI}かのうちに、ベルが{NARU}か、みんな{KYOUSHITSU}を{DETA}"],
      f"ベルが{NARU}か{NARANAI}かのうちに、みんな{KYOUSHITSU}を{DETA}",
      f"<p><strong>ベルが{NARU}か{NARANAI}かのうちに、みんな"
      f"{KYOUSHITSU}を{DETA}</strong>. Qolip bir butun — "
      f"{NARU}か va {NARANAI}か ni ajratib boʻlmaydi. Natija "
      f"gapi esa har doim oxirida turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ラノ:</strong> {EKI}に{TSUITA}ら{OSHIETE}。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"はい、{TSUKI}{SHIDAI}{RENRAKU}します",
       f"はい、{TSUITA}とたん{RENRAKU}します",
       f"はい、{TSUKU}{SHIDAI}{RENRAKU}しました",
       f"はい、{TSUKI}{SHIDAI}{RENRAKU}しました"],
      f"はい、{TSUKI}{SHIDAI}{RENRAKU}します",
      f"<p><strong>{TSUKI}{SHIDAI}{RENRAKU}します</strong> — "
      f"vaʼda, demak kelasi zamon, demak {SHIDAI}, va u "
      f"ます-oʻzagiga ulanadi. とたん bu yerda ishlamaydi "
      f"(kelasi zamon), oʻtgan zamondagi «しました» esa "
      f"vaʼdani xabarga aylantirib qoʻyadi.</p>"),
]


# ── PJ-96 uchun qoʻshimcha soʻzlar ───────────────────────────────────
DOKUSHO  = r("読書", "どくしょ")
JIKAN    = r("時間", "じかん")
HON      = r("本", "ほん")
KAU      = r("買", "か") + "う"
HITSUYOU = r("必要", "ひつよう")
HETTA    = r("減", "へ") + "った"
HETTEITA = r("減", "へ") + "っていた"
HETTEIMASHITA = r("減", "へ") + "っていました"
FUETEIMASU = r("増", "ふ") + "えています"
MACHI     = r("町", "まち")
IPPOU     = r("一方", "いっぽう")

# ══════════════════════════════════════════════════════════════════════
# PJ-96 — だ・である体 va gazeta yaponchasi
# ══════════════════════════════════════════════════════════════════════
Q_PJ96 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q(f"<p>である{TAI} qayerda ishlatiladi?</p>",
      ["Insho, maqola, ilmiy ish va gazetada",
       "Doʻstga yozilgan xabarda",
       "Oʻqituvchiga aytilgan gapda",
       "Sotuvchi bilan suhbatda"],
      "Insho, maqola, ilmiy ish va gazetada",
      f"<p><strong>Yozma matnda.</strong> である{TAI} hurmat "
      f"oʻqidan tashqarida turadi: unda tinglovchi ham, oʻquvchiga "
      f"murojaat ham yoʻq — faqat fikr bor. Shuning uchun u "
      f"{RONBUN} va maqolaning tili.</p>"),

    q(f"<p>{GAKUSEI}です — である{TAI}da qanday boʻladi?</p>",
      [f"{GAKUSEI}である", f"{GAKUSEI}だである",
       f"{GAKUSEI}でいる", f"{GAKUSEI}であります"],
      f"{GAKUSEI}である",
      f"<p><strong>{GAKUSEI}である</strong>. である "
      f"<strong>だ</strong> ning <em>oʻrniga</em> keladi, uning "
      f"ustiga emas — shuning uchun «{GAKUSEI}だである» degan "
      f"shakl yoʻq.</p>"),

    q(f"<p>{OOKII}です — である{TAI}da qanday boʻladi?</p>",
      [OOKII, f"{OOKII}である", f"{OOKII}だ", f"{OOKII}であった"],
      OOKII,
      f"<p><strong>{OOKII}</strong> — bor-yoʻgʻi です tushadi. "
      f"い-sifat bu uslubda <strong>umuman oʻzgarmaydi</strong>, "
      f"ustiga である qoʻyilmaydi. Feʼl ham xuddi shunday.</p>"),

    q(f"<p>{IKIMASU} — である{TAI}da qanday boʻladi?</p>",
      [IKU, f"{IKU}である", f"{IKU}だ", f"{IKU}であります"],
      IKU,
      f"<p><strong>{IKU}</strong>. Feʼl である{TAI}da lugʻat "
      f"shaklida turadi va hech narsa qoʻshilmaydi. Aynan shuning "
      f"uchun bir sahifada である ni bor-yoʻgʻi ikki-uch marta "
      f"uchratasiz — u faqat ot va な-sifat gap oxirida "
      f"turganda koʻrinadi.</p>"),

    q("<p>Maqolada «でも» oʻrniga nima yoziladi?</p>",
      ["しかし", "それから", "ちなみに", "だから"],
      "しかし",
      f"<p><strong>しかし</strong>. Yozma matnda bogʻlovchilar "
      f"ham oʻzgaradi: でも → しかし, だから → したがって, "
      f"それから → また, ちなみに → なお. Xuddi oʻzbekchada "
      f"gapda «lekin», maqolada «biroq» yozilgani kabi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>{GAKUSEI}でした — である{TAI}da qanday boʻladi?</p>",
      [f"{GAKUSEI}であった", f"{GAKUSEI}でありました",
       f"{GAKUSEI}だった{TAI}", f"{GAKUSEI}であるでした"],
      f"{GAKUSEI}であった",
      f"<p><strong>{GAKUSEI}であった</strong>. だった → であった. "
      f"Bu shakl asosan maqola va tarixiy matnlarda "
      f"uchraydi.</p>"),

    q(f"<p>{SHIZUKA}です — である{TAI}da qanday boʻladi?</p>",
      [f"{SHIZUKA}である", f"{SHIZUKA}なである",
       f"{SHIZUKA}だである", f"{SHIZUKA}い"],
      f"{SHIZUKA}である",
      f"<p><strong>{SHIZUKA}である</strong>. な-sifat ham otga "
      f"oʻxshab ishlaydi: だ tushadi, である keladi. Lekin "
      f"otdan oldin turganda oʻzgarmaydi — {SHIZUKA}な{MACHI} "
      f"har uch registrda ham bir xil.</p>"),

    q("<p>Yozma matnda «だから» oʻrniga nima yoziladi?</p>",
      ["したがって", "しかし", "また", "なお"],
      "したがって",
      f"<p><strong>したがって</strong> — «binobarin, shuning "
      f"uchun». Oʻzbekchada ham gapda «shuning uchun», ilmiy "
      f"ishda «binobarin» deymiz; bu bir xil juftlik.</p>"),

    q("<p>Yozma matnda «それから» oʻrniga nima yoziladi?</p>",
      ["また", "しかし", "したがって", "ただし"],
      "また",
      f"<p><strong>また</strong> (yoki さらに) — «shuningdek, "
      f"bundan tashqari». しかし qarama-qarshilikni, "
      f"したがって natijani, ただし esa istisnoni "
      f"bildiradi.</p>"),

    q("<p>Yozma matnda «ちなみに» oʻrniga nima yoziladi?</p>",
      ["なお", "また", IPPOU, "しかし"],
      "なお",
      f"<p><strong>なお</strong> — «qoʻshimcha qilib "
      f"aytganda». Uni {IPPOU} bilan "
      f"adashtirmang: u «ikkinchi tomondan» degani va ikkita "
      f"narsani qiyoslaganda ishlatiladi.</p>"),

    q(f"<p>{GAKUSEI}ではありません — である{TAI}da qanday "
      f"boʻladi?</p>",
      [f"{GAKUSEI}でない", f"{GAKUSEI}であらない",
       f"{GAKUSEI}でないです", f"{GAKUSEI}じゃない"],
      f"{GAKUSEI}でない",
      f"<p><strong>{GAKUSEI}でない</strong>. Bu uslubda "
      f"«ではない» ham uchraydi, lekin «でない» quruqroq va "
      f"maqolaga koʻproq yarashadi. «じゃない» — ogʻzaki "
      f"shakl, yozma matnga tushmaydi.</p>"),

    q(f"<p>である{TAI}dagi insho oxirida «…と{OMOIMASU}» deb "
      f"yozsa boʻladimi?</p>",
      [f"Yoʻq — «…と{OMOU}» yoki «…と{KANGAERU}» boʻlishi kerak",
       f"Ha, xulosada {TAI} oʻzgarishi mumkin",
       "Ha, agar insho qisqa boʻlsa",
       f"Yoʻq — «…と{OMOIMASU}でした» boʻlishi kerak"],
      f"Yoʻq — «…と{OMOU}» yoki «…と{KANGAERU}» boʻlishi kerak",
      f"<p><strong>Boʻlmaydi — «…と{OMOU}» yoki «…と{KANGAERU}» "
      f"boʻlishi kerak.</strong> Yaponcha inshoda oʻqituvchi yoʻq, "
      f"shuning uchun unga murojaat qiladigan ます shakli ham "
      f"yoʻq. Registr matn oxirigacha bir xil qoladi — bu "
      f"darsning yagona qatʼiy qoidasi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>である — eng hurmatli shaklmi?</p>",
      ["Yoʻq — u hurmat oʻqidan tashqarida turadi",
       "Ha, です dan ham hurmatliroq",
       "Ha, u faqat katta yoshdagilarga nisbatan ishlatiladi",
       "Yoʻq — u です dan kamroq hurmatli"],
      "Yoʻq — u hurmat oʻqidan tashqarida turadi",
      f"<p><strong>Hurmat oʻqidan tashqarida.</strong> である"
      f"{TAI}da tinglovchi ham, oʻquvchiga murojaat ham yoʻq — "
      f"faqat fikr bor. Shuning uchun uni «hurmatli» yoki "
      f"«hurmatsiz» deb oʻlchab boʻlmaydi.</p>"),

    q(f"<p>{NIKKI}da qaysi registr tabiiy?</p>",
      [f"だ{TAI} ({r('普通体', 'ふつうたい')})", f"である{TAI}",
       f"{r('丁寧体', 'ていねいたい')}",
       "Uchalasi ham bir xil darajada tabiiy"],
      f"だ{TAI} ({r('普通体', 'ふつうたい')})",
      f"<p><strong>だ{TAI}</strong>. Kundalik, roman va blog — "
      f"{r('普通体', 'ふつうたい')} ning uyi. である esa maqola "
      f"va ilmiy ish uchun; kundalikda u sovuq eshitiladi.</p>"),

    q(f"<p>Sarlavhadagi «へ» nimani bildiradi?</p>"
      f"<p><strong>{SHINEKI}、{RAISHUN}{KAIGYOU}へ</strong></p>",
      ["Kelajak rejani", "Oʻtgan voqeani", "Savolni",
       "Yoʻnalishni — qayerga borishni"],
      "Kelajak rejani",
      f"<p><strong>Kelajak reja.</strong> Toʻliq gapi: "
      f"{SHINEKI}は{RAISHUN}{KAIGYOU}する{r('予定', 'よてい')}"
      f"である。 Sarlavha shu butun iborani bitta belgiga "
      f"siqadi. Yoʻnalish maʼnosidagi «へ» boshqa — u otdan "
      f"keyin, feʼldan oldin turadi.</p>"),

    q(f"<p>Bu sarlavhada nima tushib qolgan?</p>"
      f"<p><strong>{TAIFUU}、{KYUUSHUU}に{JOURIKU}</strong></p>",
      ["Qoʻshimcha ham, gapning oxiri ham",
       "Faqat qoʻshimcha", "Faqat gapning oxiri",
       "Hech narsa tushmagan"],
      "Qoʻshimcha ham, gapning oxiri ham",
      f"<p><strong>Ikkalasi ham.</strong> Toʻliq gapi: "
      f"{TAIFUU}<strong>が</strong>{KYUUSHUU}に{JOURIKU}"
      f"<strong>した</strong>。 Vergul «が» ning oʻrnini "
      f"bosadi, gap esa ot bilan tugaydi. Sarlavhani shunday "
      f"— qoʻshimchalarni oʻzingiz qaytarib — oʻqing.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [f"この{MONDAI}は{KANTAN}だである",
       f"この{MONDAI}は{KANTAN}である",
       f"この{MONDAI}は{KANTAN}でない",
       f"この{MONDAI}は{KANTAN}であった"],
      f"この{MONDAI}は{KANTAN}だである",
      f"<p>Xato — <strong>{KANTAN}だである</strong> da: である "
      f"<strong>だ</strong> ning oʻrniga keladi, uning ustiga "
      f"emas. Toʻgʻrisi <strong>{KANTAN}である</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [f"この{MACHI}は{OOKII}",
       f"この{MACHI}は{OOKII}である",
       f"この{MACHI}は{OOKII}だ",
       f"この{MACHI}は{OOKII}であった"],
      f"この{MACHI}は{OOKII}",
      f"<p><strong>{OOKII}</strong> yolgʻiz turadi. い-sifatga "
      f"ne である, ne だ qoʻshiladi — bu ikkovi faqat ot va "
      f"な-sifat bilan ishlaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Bu gapni である{TAI}ga oʻgiring.</p>"
      f"<p><strong>この{MONDAI}は{KANTAN}ではありません。</strong></p>",
      [f"この{MONDAI}は{KANTAN}でない。",
       f"この{MONDAI}は{KANTAN}でないです。",
       f"この{MONDAI}は{KANTAN}じゃない。",
       f"この{MONDAI}は{KANTAN}ではありませんでした。"],
      f"この{MONDAI}は{KANTAN}でない。",
      f"<p><strong>{KANTAN}でない</strong>. «です» ham, «じゃ» "
      f"ham bu registrda qolmaydi, va zamon ham oʻzgarmasligi "
      f"kerak — asl gap hozirgi zamonda edi.</p>"),

    q("<p>Qaysi matnda registr aralashgan?</p>",
      [f"{CHOUSA}の{KEKKA}、{DOKUSHO}の{JIKAN}は{HETTEITA}。"
       f"しかし、{HON}を{KAU}{HITO}は{FUETEIMASU}。",
       f"{CHOUSA}の{KEKKA}、{DOKUSHO}の{JIKAN}は{HETTEITA}。"
       f"しかし、{HON}を{KAU}{HITO}は{FUETEIRU}。",
       f"{CHOUSA}の{KEKKA}、{DOKUSHO}の{JIKAN}は{HETTEIMASHITA}。"
       f"でも、{HON}を{KAU}{HITO}は{FUETEIMASU}。",
       f"{CHOUSA}の{KEKKA}、{DOKUSHO}の{JIKAN}は{HETTA}。"
       f"したがって、{RIYUU}を{KANGAERU}{HITSUYOU}がある。"],
      f"{CHOUSA}の{KEKKA}、{DOKUSHO}の{JIKAN}は{HETTEITA}。"
      f"しかし、{HON}を{KAU}{HITO}は{FUETEIMASU}。",
      f"<p>Aralashgani — birinchi gapi <strong>{HETTEITA}</strong> "
      f"(oddiy shakl), ikkinchisi esa <strong>{FUETEIMASU}</strong> "
      f"({r('丁寧体', 'ていねいたい')}) boʻlgan matn. Qolgan "
      f"uchtasi ichida har biri boshidan oxirigacha bitta "
      f"registrda qolgan.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-94 Mashq: 〜どころか va 〜ばかりか",
        "tutorial":    "PJ-94:",
        "description": "Biri kutilganni rad etadi, ikkinchisi ustiga "
                       "qoʻshadi — va nega «…dan tashqari» teskari tarjima.",
        "questions":   Q_PJ94,
        **DEFAULTS,
    },
    {
        "title":       "PJ-95 Mashq: 〜たとたん, 〜次第, 〜か〜ないかのうちに",
        "tutorial":    "PJ-95:",
        "description": "Uchta qolip, bitta oʻlchov — gapning oxiri "
                       "oʻtgan zamondami yoki kelasi zamondami.",
        "questions":   Q_PJ95,
        **DEFAULTS,
    },
    {
        "title":       "PJ-96 Mashq: だ・である体 va gazeta yaponchasi",
        "tutorial":    "PJ-96:",
        "description": "Uchta registr, uchta dunyo — va bitta qatʼiy "
                       "qoida: bitta matn ichida registr aralashmaydi.",
        "questions":   Q_PJ96,
        **DEFAULTS,
    },
]
