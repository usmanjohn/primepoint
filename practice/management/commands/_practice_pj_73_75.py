# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-73 … PJ-75. Taxminning toʻrt ovozi.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Asosiy tuzoq — bitta qoʻshimcha, ikki maʼno, va ularni faqat
ULANISH ajratadi:
    降りそうです   ← ます-oʻzak, koʻrinish (PJ-73)
    降るそうです   ← oddiy shakl, eshitilgan xabar (PJ-74)
    降るようです   ← oddiy shakl + な/の, oʻz xulosam (PJ-75)
    降るらしいです ← oddiy shakl, yalangʻoch, tashqi gap (PJ-75)

⚠️ CUMULATIVE: PJ-73 mashqida 伝聞 そう (降るそうです) YOʻQ — u
keyingi dars. PJ-73 va PJ-74 da ようです / らしい ham yoʻq.
Buni `verify_pj_practice_73_75.py` mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_73_75.py --master=prime \\
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


# ── grammatika atamalari ─────────────────────────────────────────────
YOUTAI = r("様態", "ようたい")
DENBUN = r("伝聞", "でんぶん")
FUTSUU = r("普通体", "ふつうたい")

# ── feʼllar ──────────────────────────────────────────────────────────
FURU   = r("降", "ふ") + "る"
FURI   = r("降", "ふ") + "り"
FUTTA  = r("降", "ふ") + "った"
FURANAI = r("降", "ふ") + "らない"
OCHIRU = r("落", "お") + "ちる"
OCHI   = r("落", "お") + "ち"
NAKU   = r("泣", "な") + "く"
NAKI   = r("泣", "な") + "き"
TABERU = r("食", "た") + "べる"
HIKU   = r("風邪", "かぜ") + "を" + r("引", "ひ") + "く"
HIITA  = r("風邪", "かぜ") + "を" + r("引", "ひ") + "いた"
HIKKOSU = r("引", "ひ") + "っ" + r("越", "こ") + "す"

# ── sifatlar ─────────────────────────────────────────────────────────
OISHII = "おいしい"
OISHI  = "おいし"
NEMUI  = r("眠", "ねむ") + "い"
NEMU   = r("眠", "ねむ")
TAKAI  = r("高", "たか") + "い"
YASUI  = r("安", "やす") + "い"
SHIROI = r("白", "しろ") + "い"
KIREI  = "きれい"
GENKI  = r("元気", "げんき")
TAIHEN = r("大変", "たいへん")
SHIAWASE = r("幸", "しあわ") + "せ"
SHIZUKA  = r("静", "しず") + "か"
HEYA     = r("部屋", "へや")
HANASU   = r("話", "はな") + "す"

# ── otlar ────────────────────────────────────────────────────────────
GAKUSEI = r("学生", "がくせい")
ISHA    = r("医者", "いしゃ")
AME     = r("雨", "あめ")
YUKI    = r("雪", "ゆき")
SORA    = r("空", "そら")
KUMO    = r("雲", "くも")
HANA    = r("花", "はな")
KEIKI   = "ケーキ"
SHINBUN = r("新聞", "しんぶん")
YOHOU   = r("天気予報", "てんきよほう")
TSUGOU  = r("都合", "つごう")
DENKI   = r("電気", "でんき")
SEKI    = r("咳", "せき")
MISE    = r("店", "みせ")
KAO     = r("顔", "かお")
KOE     = r("声", "こえ")
KODOMO  = r("子供", "こども")
HARU    = r("春", "はる")
TENKI   = r("天気", "てんき")
TANAKA  = r("田中", "たなか")
DARE    = r("誰", "だれ")
KIERU   = r("消", "き") + "えています"
KURAI   = r("暗", "くら") + "い"

# ── qoliplar (tayyor shakllar) ───────────────────────────────────────
FURISOU      = FURI + "そうです"
FURUSOU      = FURU + "そうです"
FUTTASOU     = FUTTA + "そうです"
FURANAISOU   = FURANAI + "そうです"
FURISOUNAI   = FURI + "そうにありません"
FURUYOU      = FURU + "ようです"
FURURASHII   = FURU + "らしいです"
OISHISOU     = OISHI + "そうです"
OISHIISOU    = OISHII + "そうです"
OISHIKUNASA  = "おいしくなさそうです"
NEMUSOU      = NEMU + "そうです"
GENKISOU     = GENKI + "そうです"
GENKIDASOU   = GENKI + "だそうです"
GENKINAYOU   = GENKI + "なようです"
GENKIRASHII  = GENKI + "らしいです"
GAKUSEIDASOU = GAKUSEI + "だそうです"
GAKUSEINOYOU = GAKUSEI + "のようです"
GAKUSEIRASHII = GAKUSEI + "らしいです"
ISHADASOU    = ISHA + "だそうです"
YOSASOU      = "よさそうです"
NASASOU      = "なさそうです"
OCHISOU      = OCHI + "そうです"
NAKISOU      = NAKI + "そうです"
NIYORUTO     = "〜によると"
YUKINOYOUNI  = YUKI + "のように" + SHIROI
KODOMONOYOUNA = KODOMO + "のような" + KOE


# ══════════════════════════════════════════════════════════════════════
# PJ-73 — koʻrinish そう (様態)
# ══════════════════════════════════════════════════════════════════════
Q_PJ73 = [
    # 1–5 tanish
    q(f"<p>Koʻrinish {YOUTAI} そう nimani bildiradi?</p>",
      ["Koʻrganimdan chiqargan xulosani",
       "Birovdan eshitgan xabarni",
       "Buyruqni",
       "Majburiyatni"],
      "Koʻrganimdan chiqargan xulosani",
      f"<p>Bulutni koʻrdim — <strong>{FURISOU}</strong>. Dalil "
      f"koʻzimda. Eshitilgan xabar boshqa qolip bilan chiqadi va "
      f"uni keyingi darsda koʻrasiz.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SORA}が"
      f"{KURAI}です。{AME}が___</strong></p>",
      [FURISOU, FURU + "です", FURU, FURI],
      FURISOU,
      f"<p>Koʻrinish そう <strong>ます-oʻzakka</strong> ulanadi: "
      f"{FURU} → {FURI} → <strong>{FURISOU}</strong>. "
      f"«Yogʻay deb turibdi».</p>"),

    q(f"<p>{OISHII} ni koʻrinish そう qolipiga qoʻying.</p>",
      [OISHISOU, OISHIISOU, "おいしいそうな", "おいしくそうです"],
      OISHISOU,
      f"<p>い-sifatdan <strong>い tushadi</strong>: {OISHII} → "
      f"{OISHI} → {OISHISOU}. «Mazali koʻrinadi».</p>"),

    q(f"<p>{GENKI}だ ni koʻrinish そう qolipiga qoʻying.</p>",
      [GENKISOU, GENKIDASOU, GENKI + "なそうです", GENKI + "にそうです"],
      GENKISOU,
      f"<p>な-sifatdan <strong>だ tushadi</strong>. Uchala soʻz "
      f"turida ham bir xil narsa boʻladi — oxiri kesiladi.</p>"),

    q(f"<p>いい ni koʻrinish そう qolipiga qoʻying.</p>",
      [YOSASOU, "いそうです", "いいそうです", "よそうです"],
      YOSASOU,
      f"<p>いい — <strong>istisno</strong>: さ qoʻshiladi. Bu さ "
      f"tanish boʻlishi kerak — よく va よかった da ham いい «い» "
      f"bilan boshlanmaydi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Stakan yiqilay dedi» — qaysi shakl?</p>",
      [f"コップが{OCHISOU}", f"コップが{OCHIRU}そうです",
       f"コップが{OCHIRU}", f"コップが{OCHI}ました"],
      f"コップが{OCHISOU}",
      f"<p>{OCHIRU} ning ます-oʻzagi {OCHI}. Bir lahzalik feʼl "
      f"bilan bu qolip «<strong>hozir boʻladi</strong>» degan "
      f"ohangni oladi.</p>"),

    q(f"<p>ない ni koʻrinish そう qolipiga qoʻying.</p>",
      [NASASOU, "なそうです", "ないそうです", "なくそうです"],
      NASASOU,
      f"<p>いい bilan bir xil istisno: <strong>さ</strong> "
      f"qoʻshiladi. {GENKI}じゃ{NASASOU} — juda koʻp "
      f"uchraydigan shakl.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>おいしそう___"
      f"{KEIKI}</strong></p>",
      ["な", "に", "の", "だ"],
      "な",
      f"<p>〜そう <strong>な-sifat kabi</strong> tuslanadi, demak "
      f"otdan oldin <strong>な</strong>: おいしそうな{KEIKI}.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>おいしそう___"
      f"{TABERU}ました</strong></p>",
      ["に", "な", "の", "と"],
      "に",
      f"<p>Feʼldan oldin <strong>に</strong> — «mazza qilib yedi». "
      f"Otdan oldin esa な. Xuddi {SHIZUKA}な{HEYA} / {SHIZUKA}に"
      f"{HANASU} kabi — な-sifatning ikki uyasi.</p>"),

    q(f"<p>«Yomgʻir yogʻadiganga oʻxshamaydi» — qaysi shakl?</p>",
      [FURISOUNAI, FURI + "そうじゃありません",
       r("降", "ふ") + "らそうです", FURI + "そうなくないです"],
      FURISOUNAI,
      f"<p>Feʼlda inkor <strong>そう dan keyin</strong> keladi: "
      f"{FURISOUNAI} yoki {FURI}そうもありません. "
      f"«{FURI}そうじゃありません» yaponcha eshitilmaydi.</p>"),

    q(f"<p>«Mazali koʻrinmaydi» — qaysi shakl?</p>",
      [OISHIKUNASA, OISHI + "そうじゃないです",
       OISHII + "なさそうです", OISHI + "そうにありません"],
      OISHIKUNASA,
      f"<p>Sifatda inkor <strong>そう dan oldin</strong> keladi: "
      f"おいし<strong>くなさ</strong>そうです. Feʼlda esa "
      f"aksincha — {FURISOUNAI}.</p>"),

    q(f"<p>{NAKU} ni koʻrinish そう qolipiga qoʻying.</p>",
      [NAKISOU, NAKU + "そうです", NAKI + "ました", NAKI + "そうな"],
      NAKISOU,
      f"<p>ます-oʻzagi {NAKI}. {NAKISOU}な{KAO} — «yigʻlay degan "
      f"yuz», hikoyalarda juda koʻp uchraydigan ibora.</p>"),

    # 13–16 farqlash
    q(f"<p>«この{HANA}は{KIREI}そうです» — nima xato?</p>",
      [f"Gulning chiroyliligini koʻrib turibsiz — bu xulosa emas",
       f"{KIREI} い-sifat, demak い tushishi kerak",
       "Otga そう ulanmaydi",
       "Hech qanday xato yoʻq"],
      "Gulning chiroyliligini koʻrib turibsiz — bu xulosa emas",
      f"<p>〜そう doim <strong>koʻrinmaydigan</strong> narsa "
      f"haqida: taʼm, kayfiyat, kelajak. Toʻgʻrisi — "
      f"{KIREI}です.</p>"),

    q(f"<p>«{GAKUSEI}そうです» — toʻgʻrimi?</p>",
      ["Yoʻq — koʻrinish そう otga ulanmaydi",
       "Ha, bu normal gap",
       "Ha, lekin faqat yozma tilda",
       f"Yoʻq — {GAKUSEI} い-sifat"],
      "Yoʻq — koʻrinish そう otga ulanmaydi",
      f"<p>U faqat feʼl, い-sifat va な-sifatga ulanadi. "
      f"«Talabaga oʻxshaydi» degan maʼno boshqa qolip bilan "
      f"chiqadi — PJ-75.</p>"),

    q(f"<p>«{TSUGOU}がいそうです» — nima xato?</p>",
      [f"いい istisno: <strong>{YOSASOU}</strong> boʻlishi kerak",
       f"{TSUGOU} ga そう ulanmaydi",
       "が oʻrniga は kerak",
       "Hech qanday xato yoʻq"],
      f"いい istisno: <strong>{YOSASOU}</strong> boʻlishi kerak",
      f"<p>いい dan yasalgan hech qanday shakl «い» bilan "
      f"boshlanmaydi. {TSUGOU}が{YOSASOU} — «qulay "
      f"koʻrinadi».</p>"),

    q(f"<p>«コップが{OCHISOU}» — stakan yiqildimi?</p>",
      ["Yoʻq — hali yiqilmadi, lekin hozir yiqiladi",
       "Ha, yiqildi",
       "Ha, lekin men koʻrmadim",
       "Yiqilgani haqida eshitdim"],
      "Yoʻq — hali yiqilmadi, lekin hozir yiqiladi",
      f"<p>Koʻp oʻquvchi buni «yiqildi shekilli» deb tarjima "
      f"qiladi. Toʻgʻri tarjima — «<strong>yiqilay dedi</strong>», "
      f"yaʼni hali sodir boʻlmagan.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"おいしそうな{KEIKI}を{TABERU}ました",
       f"おいしそう{KEIKI}を{TABERU}ました",
       f"おいしいそうな{KEIKI}を{TABERU}ました",
       f"おいしそうに{KEIKI}を{TABERU}ました"],
      f"おいしそうな{KEIKI}を{TABERU}ました",
      f"<p>Otdan oldin <strong>な</strong>. «おいしそうに» ham "
      f"grammatik, lekin u holda «tortni mazza qilib yedi» "
      f"boʻladi — tort emas, yeyish tasvirlanadi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{AME}が{FURI}そうじゃありません",
       f"{AME}が{FURISOUNAI}",
       f"{AME}が{FURISOU}",
       f"{KEIKI}は{OISHIKUNASA}"],
      f"{AME}が{FURI}そうじゃありません",
      f"<p>Feʼlda inkor <strong>そうにない</strong> yoki "
      f"<strong>そうもない</strong> bilan yasaladi. «そうじゃ"
      f"ありません» tushunarli, lekin yaponlar bunday "
      f"demaydi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibga soling.</p>"
      f"<p><strong>{NEMU}そうな · {KAO} · を · していました · "
      f"ムニラさんは</strong></p>",
      [f"ムニラさんは{NEMUSOU}な{KAO}をしていました",
       f"ムニラさんは{KAO}を{NEMUSOU}なしていました",
       f"{NEMUSOU}なムニラさんは{KAO}をしていました",
       f"ムニラさんは{KAO}をしていました{NEMUSOU}な"],
      f"ムニラさんは{NEMUSOU}な{KAO}をしていました",
      f"<p>Yapon tili SOV: kesim <strong>oxirida</strong>. "
      f"{NEMUSOU}な — {KAO} ni aniqlaydi, shuning uchun uning "
      f"oldida turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム: "
      f"{KUMO}が{KURAI}ですね。</strong></p><p><strong>パリ: "
      f"___</strong></p>",
      [f"ええ、{AME}が{FURISOU}ですね。",
       f"ええ、{AME}が{FURU}ですね。",
       f"ええ、{AME}が{FURI}ますね。",
       f"ええ、{AME}が{FURI}そうにありませんね。"],
      f"ええ、{AME}が{FURISOU}ですね。",
      f"<p>Qora bulutni <strong>ikkalasi ham koʻrib turibdi</strong> "
      f"— aynan koʻrinish そう uchun tugʻilgan vaziyat. Oxirgi "
      f"variant teskari maʼno beradi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-74 — eshitilgan xabar そう (伝聞)
# ══════════════════════════════════════════════════════════════════════
Q_PJ74 = [
    # 1–5 tanish
    q(f"<p>{DENBUN} そう nimaga ulanadi?</p>",
      [f"Oddiy shaklga ({FUTSUU}) — hech nima kesilmaydi",
       "ます-oʻzakka",
       "Otning oʻziga, だ siz",
       "て-shaklga"],
      f"Oddiy shaklga ({FUTSUU}) — hech nima kesilmaydi",
      f"<p>Bu — koʻrinish そу dan yagona farqi. Kechagi darsda "
      f"oxiri kesilardi ({FURISOU}); bugun butun soʻz turadi "
      f"({FURUSOU}).</p>"),

    q(f"<p>«Ertaga yomgʻir yogʻarkan» — qaysi shakl?</p>",
      [FURUSOU, FURISOU, FURU + "でしょう", FURI + "ました"],
      FURUSOU,
      f"<p>Lugʻat shakli {FURU} + そうです. Oʻzbekcha "
      f"«-<strong>arkan</strong>» — bu qolipning eng aniq "
      f"tarjimasi.</p>"),

    q(f"<p>«Talaba ekan» — qaysi shakl?</p>",
      [GAKUSEIDASOU, GAKUSEI + "そうです", GAKUSEI + "のそうです",
       GAKUSEI + "なそうです"],
      GAKUSEIDASOU,
      f"<p>Ot <strong>だ</strong> ni saqlaydi. «{GAKUSEI}そうです» "
      f"degan shakl umuman yoʻq — koʻrinish そう otga "
      f"ulanmaydi.</p>"),

    q(f"<p>«Tetik ekan» — qaysi shakl?</p>",
      [GENKIDASOU, GENKISOU, GENKI + "のそうです", GENKI + "にそうです"],
      GENKIDASOU,
      f"<p>な-sifat ham <strong>だ</strong> ni saqlaydi. "
      f"{GENKISOU} esa «tetik <em>koʻrinadi</em>» — men koʻrdim, "
      f"eshitmadim.</p>"),

    q(f"<p>«Mazali ekan» — qaysi shakl?</p>",
      [OISHIISOU, OISHISOU, OISHI + "だそうです", OISHII + "だそうです"],
      OISHIISOU,
      f"<p>い-sifat oʻz shaklida qoladi: {OISHII} + そうです. "
      f"い-sifatga <strong>だ qoʻshilmaydi</strong>.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Kecha yomgʻir yogʻgan ekan» — qaysi shakl?</p>",
      [FUTTASOU, FURU + "そうでした", FURISOU + "でした",
       FUTTA + "そうでした"],
      FUTTASOU,
      f"<p>Zamon <strong>gapning ichida</strong> turadi: "
      f"{FUTTA} + そうです. «そうでした» degan shakl yoʻq.</p>"),

    q(f"<p>«Yomgʻir yogʻmasakan» — qaysi shakl?</p>",
      [FURANAISOU, FURU + "そうではありません",
       FURI + "そうにありません", FURU + "そうじゃないです"],
      FURANAISOU,
      f"<p>Inkor ham <strong>gapning ichida</strong>: {FURANAI} + "
      f"そうです. {FURISOUNAI} esa boshqa narsa — u koʻrinish "
      f"そう ning inkori.</p>"),

    q(f"<p>{NIYORUTO} nimani bildiradi?</p>",
      ["…ga koʻra — xabarning manbasini", "…dan keyin",
       "…ga qaramay", "…uchun"],
      "…ga koʻra — xabarning manbasini",
      f"<p>{YOHOU}によると, {SHINBUN}によると. Bu qolip deyarli "
      f"doim gap oxiridagi <strong>そうです</strong> bilan "
      f"juftlashadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{YOHOU}に"
      f"よると、{r('明日', 'あした')}{YUKI}が___</strong></p>",
      [FURUSOU, FURISOU, FURU, FURI + "ます"],
      FURUSOU,
      f"<p>«によると» boshlangan gap deyarli doim «そうです» "
      f"bilan tugaydi. Men osmonga qaramadim — "
      f"<strong>eshitdim</strong>.</p>"),

    q(f"<p>«{FURU}そうでした» — nima xato?</p>",
      ["そうです oʻzi oʻtgan zamonga kirmaydi",
       "そうです oʻzi inkor boʻlmaydi",
       f"{FURU} oʻrniga {FURI} kerak",
       "Hech qanday xato yoʻq"],
      "そうです oʻzi oʻtgan zamonga kirmaydi",
      f"<p>そうです — bu gapning oʻzi emas, gapning "
      f"<strong>qayerdan kelgani</strong>. Uni oʻzgartirib "
      f"boʻlmaydi. Toʻgʻrisi — {FUTTASOU}.</p>"),

    q(f"<p>«{FURU}そうではありません» — nima xato?</p>",
      ["そうです oʻzi inkor boʻlmaydi",
       "そうです oʻzi oʻtgan zamonga kirmaydi",
       "ではありません oʻrniga じゃないです kerak",
       "Hech qanday xato yoʻq"],
      "そうです oʻzi inkor boʻlmaydi",
      f"<p>Inkor xabarning <strong>ichida</strong> qoladi: "
      f"{FURANAISOU}. Siz eshitgan xabarni oʻzgartira "
      f"olmaysiz.</p>"),

    q(f"<p>«Parining akasi shifokor ekan» — qaysi shakl?</p>",
      [f"パリさんのお{r('兄', 'にい')}さんは{ISHADASOU}",
       f"パリさんのお{r('兄', 'にい')}さんは{ISHA}そうです",
       f"パリさんのお{r('兄', 'にい')}さんは{ISHA}のそうです",
       f"パリさんのお{r('兄', 'にい')}さんは{ISHA}でそうです"],
      f"パリさんのお{r('兄', 'にい')}さんは{ISHADASOU}",
      f"<p>Ot + <strong>だ</strong> + そうです. Bu — bu qolipning "
      f"eng koʻp yodlanadigan qatori.</p>"),

    # 13–16 farqlash
    q(f"<p>{GENKISOU} va {GENKIDASOU} — farqi nima?</p>",
      ["Birinchisi — koʻrdim, ikkinchisi — eshitdim",
       "Birinchisi — eshitdim, ikkinchisi — koʻrdim",
       "Birinchisi hozirgi, ikkinchisi oʻtgan zamon",
       "Hech qanday farqi yoʻq"],
      "Birinchisi — koʻrdim, ikkinchisi — eshitdim",
      f"<p>Butun farq bitta <strong>だ</strong> da. {GENKISOU} — "
      f"«tetik koʻrinadi»; {GENKIDASOU} — «tetik ekan».</p>"),

    q(f"<p>{FURISOU} va {FURUSOU} — farqi nima?</p>",
      ["Birinchisi bulutni koʻrib, ikkinchisi xabarni eshitib",
       "Birinchisi xabar, ikkinchisi koʻrinish",
       "Birinchisi hozirgi, ikkinchisi kelasi zamon",
       "Birinchisi soʻzlashuv, ikkinchisi yozma til"],
      "Birinchisi bulutni koʻrib, ikkinchisi xabarni eshitib",
      f"<p>Ajratadigan yagona belgi — <strong>bitta bogʻin</strong>: "
      f"{FURI}そう ↔ {FURU}そう. Gapirganda uni yutib "
      f"yubormang.</p>"),

    q(f"<p>{OISHISOU} va {OISHIISOU} — farqi nima?</p>",
      ["Birinchisi — koʻrinishi, ikkinchisi — eshitganim",
       "Birinchisi — eshitganim, ikkinchisi — koʻrinishi",
       "Birinchisi kuchliroq baho beradi",
       "Ikkinchisi notoʻgʻri shakl"],
      "Birinchisi — koʻrinishi, ikkinchisi — eshitganim",
      f"<p>Yana bitta harf: <strong>い</strong> tushganmi yoki "
      f"turibdimi. {OISHISOU} — hali tatib koʻrmadim, lekin "
      f"koʻrinishi yaxshi; {OISHIISOU} — odamlar shunday "
      f"deyishdi.</p>"),

    q(f"<p>Otga qaysi qolip ulanadi?</p>",
      [f"Faqat {DENBUN} そう — {GAKUSEIDASOU}",
       f"Faqat koʻrinish そう — {GAKUSEI}そうです",
       "Ikkalasi ham ulanadi",
       "Ikkalasi ham ulanmaydi"],
      f"Faqat {DENBUN} そう — {GAKUSEIDASOU}",
      f"<p>Koʻrinish そう faqat feʼl va sifatga ulanadi. Shuning "
      f"uchun otdan keyin そう koʻrsangiz, u <strong>albatta "
      f"xabar</strong>.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{SHINBUN}によると、{TANAKA}さんは{ISHADASOU}",
       f"{SHINBUN}によると、{TANAKA}さんは{ISHA}そうです",
       f"{SHINBUN}によると、{TANAKA}さんは{ISHA}だそうでした",
       f"{SHINBUN}によると、{TANAKA}さんは{ISHA}だそうではありません"],
      f"{SHINBUN}によると、{TANAKA}さんは{ISHADASOU}",
      f"<p>Ot だ ni saqlaydi, そうです esa na zamonga kiradi, na "
      f"inkor boʻladi. Uchala xato bitta jadvalda.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{r('去年', 'きょねん')}{FURU}そうでした",
       f"{r('去年', 'きょねん')}{FUTTASOU}",
       f"{r('明日', 'あした')}{FURANAISOU}",
       f"{r('明日', 'あした')}{FURUSOU}"],
      f"{r('去年', 'きょねん')}{FURU}そうでした",
      f"<p>Zamon そうです ga emas, <strong>gapga</strong> "
      f"qoʻyiladi: {FUTTASOU}.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibga soling.</p>"
      f"<p><strong>そうです · {YOHOU}によると · {YUKI}が · "
      f"{r('明日', 'あした')} · {FURU}</strong></p>",
      [f"{YOHOU}によると、{r('明日', 'あした')}{YUKI}が{FURUSOU}",
       f"{r('明日', 'あした')}{YUKI}が{YOHOU}によると{FURUSOU}",
       f"{YOHOU}によると、{YUKI}が{FURU}そうです{r('明日', 'あした')}",
       f"{YUKI}が{FURUSOU}{YOHOU}によると{r('明日', 'あした')}"],
      f"{YOHOU}によると、{r('明日', 'あした')}{YUKI}が{FURUSOU}",
      f"<p>Manba <strong>oldinda</strong>, tamgʻa "
      f"<strong>orqada</strong> — oʻzbekcha «ob-havo "
      f"maʼlumotiga koʻra …-arkan» bilan bir xil tartib.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: イノムさんを"
      f"{r('見', 'み')}ましたか。</strong></p><p><strong>イムロン: "
      f"___</strong></p>",
      [f"いいえ。{r('来月', 'らいげつ')}{r('大阪', 'おおさか')}へ"
       f"{HIKKOSU}そうですよ。",
       f"いいえ。{r('来月', 'らいげつ')}{r('大阪', 'おおさか')}へ"
       f"{HIKKOSU}そうでしたよ。",
       f"いいえ。{r('来月', 'らいげつ')}{r('大阪', 'おおさか')}へ"
       f"{r('引', 'ひ')}っ{r('越', 'こ')}しそうですよ。",
       f"いいえ。{r('来月', 'らいげつ')}{r('大阪', 'おおさか')}へ"
       f"{HIKKOSU}そうではありませんよ。"],
      f"いいえ。{r('来月', 'らいげつ')}{r('大阪', 'おおさか')}へ"
      f"{HIKKOSU}そうですよ。",
      f"<p>Imron Inomni koʻrmagan — u faqat <strong>eshitgan</strong>. "
      f"Demak lugʻat shakli + そうです. よ bilan birga bu gap "
      f"«senga ayta turay» degan ohangni oladi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-75 — ようです va らしいです
# ══════════════════════════════════════════════════════════════════════
Q_PJ75 = [
    # 1–5 tanish
    q(f"<p>ようです qoʻyilgan gapda dalil kimda?</p>",
      ["Menda — men koʻrdim yoki sezdim, xulosa ham meniki",
       "Menda emas — odamlar shunday deyishdi",
       "Rasmiy manbada",
       "Hech kimda"],
      "Menda — men koʻrdim yoki sezdim, xulosa ham meniki",
      f"<p>Shuning uchun ようです javobgarlikni <strong>oʻzimga "
      f"oladi</strong>: xulosam notoʻgʻri chiqsa, aybdor men.</p>"),

    q(f"<p>らしいです qoʻyilgan gapda dalil kimda?</p>",
      ["Menda emas — gap tashqaridan keldi",
       "Menda — men koʻrdim",
       "Ikkalasida ham",
       "Bu qolip dalil haqida umuman gapirmaydi"],
      "Menda emas — gap tashqaridan keldi",
      f"<p>Shuning uchun らしい javobgarlikni <strong>oʻzimdan "
      f"uzoqlashtiradi</strong>. Oʻzbekcha «-mish», "
      f"«aytishlaricha».</p>"),

    q(f"<p>{GAKUSEI} ni ようです bilan bogʻlang.</p>",
      [GAKUSEINOYOU, GAKUSEI + "ようです", GAKUSEI + "だようです",
       GAKUSEI + "なようです"],
      GAKUSEINOYOU,
      f"<p>ようだ otdan keyin <strong>の</strong> talab qiladi — "
      f"xuddi {GAKUSEI}の{r('兄', 'あに')} kabi. ようだ oʻzi "
      f"otdan kelib chiqqan ({r('様', 'よう')} — «koʻrinish»).</p>"),

    q(f"<p>{GENKI} ni ようです bilan bogʻlang.</p>",
      [GENKINAYOU, GENKI + "のようです", GENKI + "だようです",
       GENKI + "ようです"],
      GENKINAYOU,
      f"<p>な-sifat <strong>な</strong> oladi, の emas. Bu — "
      f"darsning eng koʻp adashiladigan qatori.</p>"),

    q(f"<p>{GAKUSEI} ni らしいです bilan bogʻlang.</p>",
      [GAKUSEIRASHII, GAKUSEI + "のらしいです",
       GAKUSEI + "だらしいです", GAKUSEI + "ならしいです"],
      GAKUSEIRASHII,
      f"<p>らしい <strong>yalangʻoch</strong> ulanadi: na だ, na "
      f"の, na な. U い-sifat kabi tutadi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{DENKI}が"
      f"{KIERU}。{DARE}もいない___</strong></p>",
      ["ようです", "そうです", "ようでした", "らしいでした"],
      "ようです",
      f"<p>Dalil — oʻchgan chiroq, va uni <strong>men "
      f"koʻryapman</strong>. «らしいでした» degan shakl yoʻq: "
      f"らしい い-sifat kabi tuslanadi — らしかったです.</p>"),

    q(f"<p>«Anavi doʻkon arzonmish» — qaysi shakl?</p>",
      [f"あの{MISE}は{YASUI}らしいです",
       f"あの{MISE}は{YASUI}のらしいです",
       f"あの{MISE}は{YASUI}なようです",
       f"あの{MISE}は{YASUI}そうな"],
      f"あの{MISE}は{YASUI}らしいです",
      f"<p>«-mish» → <strong>らしい</strong>. い-sifat oʻz "
      f"shaklida qoladi va らしい yalangʻoch ulanadi.</p>"),

    q(f"<p>«Bolanikiga oʻxshagan ovoz» — qaysi shakl?</p>",
      [KODOMONOYOUNA, KODOMO + "のように" + KOE,
       KODOMO + "なような" + KOE, KODOMO + "らしいような" + KOE],
      KODOMONOYOUNA,
      f"<p>Otdan oldin <strong>ような</strong>. ようだ な-sifat "
      f"kabi tuslanadi, shuning uchun bu ikki uyacha PJ-73 dagi "
      f"そうな / そうに bilan bir xil.</p>"),

    q(f"<p>«Qordek oq» — qaysi shakl?</p>",
      [YUKINOYOUNI, YUKI + "のような" + SHIROI,
       YUKI + "らしい" + SHIROI, YUKI + "そうに" + SHIROI],
      YUKINOYOUNI,
      f"<p>Sifatdan oldin <strong>ように</strong>. Bu yerda "
      f"ようだ taxmin emas, <strong>oʻxshatish</strong> qilyapti "
      f"— ikkala maʼno bir ildizdan.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>ムニラさんは"
      f"{SEKI}をしています。{HIITA}___</strong></p>",
      ["ようです", "ような", "ように", "らしいような"],
      "ようです",
      f"<p>Yoʻtalni men eshityapman, «shamollagan» degan xulosani "
      f"men chiqaryapman — demak <strong>ようです</strong>. "
      f"ような / ように otdan va feʼldan oldin turadi, gap "
      f"oxirida emas.</p>"),

    q(f"<p>«{GENKI}らしいです» toʻgʻrimi?</p>",
      ["Ha — らしい na だ, na な, na の oladi",
       f"Yoʻq — {GENKI}ならしいです boʻlishi kerak",
       f"Yoʻq — {GENKI}だらしいです boʻlishi kerak",
       f"Yoʻq — {GENKI}のらしいです boʻlishi kerak"],
      "Ha — らしい na だ, na な, na の oladi",
      f"<p>Butun farq shu: ようだ bogʻlovchi <strong>talab "
      f"qiladi</strong>, らしい <strong>talab qilmaydi</strong>.</p>"),

    q(f"<p>«{TANAKA}さんは{GAKUSEI}らしい{GAKUSEI}です» — bu "
      f"nima deydi?</p>",
      ["Tanaka — talabaga xos, chinakam talaba",
       "Tanaka talabamish, aniq bilmayman",
       "Tanaka talaba boʻlmoqchi",
       "Tanaka talabaga oʻxshab ketadi, lekin talaba emas"],
      "Tanaka — talabaga xos, chinakam talaba",
      f"<p>らしい ning <strong>ikkinchi ishi</strong>: «…ga xos». "
      f"{HARU}らしい{TENKI} — «bahorga xos ob-havo». Bu maʼnoda "
      f"らしい dan keyin koʻpincha ot keladi.</p>"),

    # 13–16 farqlash
    q(f"<p>{FURISOU} — men buni qayerdan bilaman?</p>",
      ["Qora bulutni koʻrib turibman",
       "Aniq manbadan eshitdim",
       "Dalilga qarab oʻzim xulosa qildim",
       "Odamlar shunday deyishdi"],
      "Qora bulutni koʻrib turibman",
      f"<p>Toʻrtlikda faqat shu qolip <strong>ます-oʻzakka</strong> "
      f"ulanadi. Birinchi savol doim bitta: oxiri kesilganmi?</p>"),

    q(f"<p>{FURUSOU} — men buni qayerdan bilaman?</p>",
      ["Aniq manbadan eshitdim", "Qora bulutni koʻrib turibman",
       "Dalilga qarab oʻzim xulosa qildim",
       "Oʻzim shunday qaror qildim"],
      "Aniq manbadan eshitdim",
      f"<p>Va u odatda {NIYORUTO} bilan yuradi: {YOHOU}によると… "
      f"{FURUSOU}.</p>"),

    q(f"<p>{FURUYOU} — men buni qayerdan bilaman?</p>",
      ["Dalil bor, lekin xulosani men chiqardim",
       "Aniq manbadan eshitdim",
       "Qora bulutni bevosita koʻryapman",
       "Hech qanday asosim yoʻq"],
      "Dalil bor, lekin xulosani men chiqardim",
      f"<p>Masalan hamma soyabon koʻtargan. Bulutni koʻrmadim, "
      f"lekin <strong>belgilarga qarab</strong> xulosa "
      f"chiqardim.</p>"),

    q(f"<p>{FURURASHII} — men buni qayerdan bilaman?</p>",
      ["Odamlar shunday deyishdi, manba aniq emas",
       "Rasmiy manbadan, aniq",
       "Oʻz koʻzim bilan koʻrdim",
       "Oʻzim hisoblab chiqardim"],
      "Odamlar shunday deyishdi, manba aniq emas",
      f"<p>Shuning uchun rasmiy yangilikda そうです, tanaffusdagi "
      f"gapda esa らしい eshitiladi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [GENKINAYOU, GENKI + "のようです", GENKI + "ようです",
       GENKI + "だようです"],
      GENKINAYOU,
      f"<p>な-sifat <strong>な</strong> oladi. Ot esa の oladi: "
      f"{GAKUSEINOYOU}. Ikkalasini almashtirib yuborish — bu "
      f"darsning eng koʻp uchraydigan xatosi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{AME}が{FURI}ようです", f"{AME}が{FURUYOU}",
       f"{AME}が{FURURASHII}", f"{AME}が{FURISOU}"],
      f"{AME}が{FURI}ようです",
      f"<p>ようだ <strong>oddiy shaklga</strong> ulanadi, "
      f"ます-oʻzakka emas. ます-oʻzak faqat koʻrinish そう "
      f"uchun.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibga soling.</p>"
      f"<p><strong>ようです · {DARE}も · {DENKI}が · いない · "
      f"{KIERU}。</strong></p>",
      [f"{DENKI}が{KIERU}。{DARE}もいないようです",
       f"{DARE}もいない{DENKI}が{KIERU}ようです",
       f"{DENKI}が{DARE}もいない{KIERU}ようです",
       f"ようです{DENKI}が{KIERU}。{DARE}もいない"],
      f"{DENKI}が{KIERU}。{DARE}もいないようです",
      f"<p>Avval <strong>dalil</strong>, keyin <strong>xulosa</strong> "
      f"— ようです bilan yozilgan gap deyarli doim shu tartibda "
      f"keladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ: あの{MISE}に"
      f"{r('行', 'い')}ったことがありますか。</strong></p>"
      f"<p><strong>パリ: いいえ。でも ___</strong></p>",
      [f"{YASUI}らしいですよ。", f"{YASUI}ようです。",
       f"{YASUI}そうな{MISE}です。", f"{YASUI}くなさそうです。"],
      f"{YASUI}らしいですよ。",
      f"<p>Pari u yerga <strong>bormagan</strong> — demak oʻz "
      f"dalili yoʻq, gap tashqaridan kelgan. Aynan らしい uchun "
      f"tugʻilgan vaziyat.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-73 Mashq: 〜そうです 1 — koʻrinish",
        "tutorial":    "PJ-73:",
        "description": "ます-oʻzak, い tushadi, だ tushadi — va "
                       "koʻz bilan koʻrinadigan narsaga そう qoʻyilmaydi.",
        "questions":   Q_PJ73,
        **DEFAULTS,
    },
    {
        "title":       "PJ-74 Mashq: 〜そうです 2 — eshitilgan xabar",
        "tutorial":    "PJ-74:",
        "description": "Oddiy shakl, だ saqlanadi, zamon va inkor "
                       "gapning ichida qoladi.",
        "questions":   Q_PJ74,
        **DEFAULTS,
    },
    {
        "title":       "PJ-75 Mashq: 〜ようです va 〜らしいです",
        "tutorial":    "PJ-75:",
        "description": "ようだ な / の talab qiladi, らしい "
                       "yalangʻoch ulanadi — va toʻrtala taxmin bir jadvalda.",
        "questions":   Q_PJ75,
        **DEFAULTS,
    },
]
