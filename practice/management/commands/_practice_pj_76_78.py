# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-76 … PJ-78. Blok E yopiladi.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi, uchtasi ham «bilaman» deb oʻtib
ketiladigan turdan:
    1. みたい YALANGʻOCH ulanadi — 学生みたい, 元気みたい.
       ようだ ning な/の si bu yerda XATO.
    2. みたい ≠ 見たい. Ajratuvchi belgi — oldidagi が:
       映画みたい (oʻxshaydi) ↔ 映画が見たい (koʻrgim bor).
    3. Taqlid soʻzi する / だ / feʼl — uchtasidan BIRINI oladi va
       tanlov qoida bilan chiqmaydi: ドキドキする, ぺこぺこだ,
       ザーザー降る. ぺこぺこする esa «xushomad qilmoq».

⚠️ CUMULATIVE: PJ-76 mashqida 擬音語 yoʻq (PJ-77) va 僕/俺/ぞ/ぜ
yoʻq (PJ-78). PJ-77 da PJ-78 ning register materiali yoʻq.
`verify_pj_practice_76_78.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_76_78.py --master=prime \\
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


# ── feʼllar / sifatlar (oxirgi い ALOHIDA — PJ-25 dagi saboq) ─────────
FURU    = r("降", "ふ") + "る"
FURI    = r("降", "ふ") + "り"
FUTTA   = r("降", "ふ") + "った"
MIRU    = r("見", "み") + "る"
MITAI_V = r("見", "み") + "たい"          # koʻrgim bor
NAKU    = r("泣", "な") + "く"
NAITA   = r("泣", "な") + "いた"
NIRU    = r("似", "に") + "ている"
KURABERU = r("比", "くら") + "べる"
NARU    = r("鳴", "な") + "る"
NAKU_A  = r("鳴", "な") + "く"
HIKARU  = r("光", "ひか") + "る"
NERU    = r("寝", "ね") + "る"
ARUKU   = r("歩", "ある") + "く"
ISOGASHII = r("忙", "いそが") + "しい"
TAKAI   = r("高", "たか") + "い"

# ── otlar ────────────────────────────────────────────────────────────
AME     = r("雨", "あめ")
YUKI    = r("雪", "ゆき")
EIGA    = r("映画", "えいが")
GAKUSEI = r("学生", "がくせい")
ISHA    = r("医者", "いしゃ")
GENKI   = r("元気", "げんき")
KODOMO  = r("子供", "こども")
KOE     = r("声", "こえ")
CHICHI  = r("父", "ちち")
OTOUSAN = "お" + r("父", "とう") + "さん"
MUNE    = r("胸", "むね")
ONAKA   = "お" + r("腹", "なか")
INU     = r("犬", "いぬ")
HOSHI   = r("星", "ほし")
SHIKEN  = r("試験", "しけん")
TANAKA  = r("田中", "たなか")
WATASHI = r("私", "わたし")
BOKU    = r("僕", "ぼく")
ORE     = r("俺", "おれ")
KIMI    = r("君", "きみ")
OMAE    = "お" + r("前", "まえ")
OKYAKU  = "お" + r("客", "きゃく") + "さま"
NANSAI  = r("何歳", "なんさい")
TAIHEN  = r("大変", "たいへん")
HONTOU  = r("本当", "ほんとう")
TEINEI  = r("丁寧体", "ていねいたい")
FUTSUU  = r("普通体", "ふつうたい")
GIONGO  = r("擬音語", "ぎおんご")
GITAIGO = r("擬態語", "ぎたいご")

# ── tayyor qoliplar ──────────────────────────────────────────────────
FURUMITAI    = FURU + "みたいです"
FURUYOU      = FURU + "ようです"
FURURASHII   = FURU + "らしいです"
FURISOU      = FURI + "そうです"
FURUSOU      = FURU + "そうです"
GAKUSEIMITAI = GAKUSEI + "みたいです"
GENKIMITAI   = GENKI + "みたいです"
GENKINAYOU   = GENKI + "なようです"
GAKUSEINOYOU = GAKUSEI + "のようです"
KODOMOMITAINA = KODOMO + "みたいな" + KOE
KODOMOMITAINI = KODOMO + "みたいに" + NAITA
KODOMONOYOUNA = KODOMO + "のような" + KOE
EIGAMITAI    = EIGA + "みたいです"
EIGAGAMITAI  = EIGA + "が" + MITAI_V + "です"


# ══════════════════════════════════════════════════════════════════════
# PJ-76 — みたい va kundalik taqqoslash
# ══════════════════════════════════════════════════════════════════════
Q_PJ76 = [
    # 1–5 tanish
    q(f"<p>みたい otga qanday ulanadi?</p>",
      ["Yalangʻoch — hech qanday qoʻshimchasiz",
       "の bilan", "な bilan", "だ bilan"],
      "Yalangʻoch — hech qanday qoʻshimchasiz",
      f"<p><strong>{GAKUSEIMITAI}</strong>. ようだ の talab "
      f"qilardi ({GAKUSEINOYOU}), みたい esa hech nima talab "
      f"qilmaydi.</p>"),

    q(f"<p>{GENKI} ni みたいです bilan bogʻlang.</p>",
      [GENKIMITAI, GENKI + "なみたいです", GENKI + "のみたいです",
       GENKI + "だみたいです"],
      GENKIMITAI,
      f"<p>な-sifat ham <strong>yalangʻoch</strong> ulanadi. "
      f"<strong>な</strong> ようだ uchun: {GENKINAYOU}.</p>"),

    q(f"<p>«Yomgʻir yogʻadiganga oʻxshaydi» — kundalik nutqda "
      f"qaysi qolip?</p>",
      [FURUMITAI, FURISOU, FURI + "みたいです", FURU + "でみたいです"],
      FURUMITAI,
      f"<p>みたい <strong>oddiy shaklga</strong> ulanadi. "
      f"ます-oʻzak faqat koʻrinish そう uchun ({FURISOU}).</p>"),

    q(f"<p>みたい bilan ようだ orasidagi farq nimada?</p>",
      ["Maʼnoda emas, registrda — biri kundalik, biri kitobiy",
       "Maʼnoda — biri koʻrinish, biri xabar",
       "Zamonda — biri hozirgi, biri oʻtgan",
       "Hech qanday farqi yoʻq"],
      "Maʼnoda emas, registrda — biri kundalik, biri kitobiy",
      f"<p>Ikkalasi ham «dalil menda, xulosa meniki» deydi. "
      f"Faqat みたい doʻstlar bilan, ようだ esa yozma tilda "
      f"ishlatiladi.</p>"),

    q(f"<p>Rasmiy hisobotda qaysi qolipni tanlaysiz?</p>",
      [FURUYOU, FURUMITAI, FURU + "みたい", FURU + "みたいだ"],
      FURUYOU,
      f"<p>Qolgan uchtasi — bir xil qolip, uch xil "
      f"muloyimlikda, va uchalasi ham <strong>kundalik</strong>. "
      f"みたい rasmiy matnda notoʻgʻri emas — <strong>joyida "
      f"emas</strong>. Hisobotda, yangilikda va ilmiy matnda "
      f"ようです turadi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KODOMO}みたい"
      f"___{KOE}</strong></p>",
      ["な", "に", "の", "だ"],
      "な",
      f"<p>Otdan oldin <strong>な</strong> — {KODOMOMITAINA}. "
      f"みたい ham な-sifat kabi tuslanadi, xuddi そう va よう "
      f"kabi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KODOMO}みたい"
      f"___{NAITA}</strong></p>",
      ["に", "な", "の", "と"],
      "に",
      f"<p>Feʼldan oldin <strong>に</strong> — {KODOMOMITAINI}, "
      f"«boladek yigʻladi».</p>"),

    q(f"<p>«Oʻtgan zamon» みたい bilan qanday aytiladi?</p>",
      [FUTTA + "みたいです", FURU + "みたいでした",
       FURI + "みたいでした", FURU + "みたいだった"],
      FUTTA + "みたいです",
      f"<p>Zamon <strong>gapning ichida</strong> turadi — "
      f"{FUTTA}, keyin みたい. PJ-74 dagi そうです bilan bir xil "
      f"mantiq.</p>"),

    q(f"<p>«Kinoga oʻxshaydi» va «kinoni koʻrgim bor» — qaysi "
      f"juftlik toʻgʻri?</p>",
      [f"{EIGAMITAI} / {EIGAGAMITAI}",
       f"{EIGAGAMITAI} / {EIGAMITAI}",
       f"{EIGA}をみたいです / {EIGAMITAI}",
       f"{EIGAMITAI} / {EIGA}をみたいです"],
      f"{EIGAMITAI} / {EIGAGAMITAI}",
      f"<p>{MITAI_V} — {MIRU} + たい, shuning uchun oldida "
      f"<strong>が</strong> turadi. みたい esa otga tegib "
      f"turadi, orada hech nima yoʻq.</p>"),

    q(f"<p>みたい ni {MITAI_V} dan nima ajratadi?</p>",
      ["Oldidagi qoʻshimcha — が bor yoki yoʻq",
       "Ohang", "Kanji yozilishi", "Gapdagi oʻrni"],
      "Oldidagi qoʻshimcha — が bor yoki yoʻq",
      f"<p>{EIGA}<strong>が</strong>{MITAI_V} — feʼl, "
      f"toʻldiruvchisi bor. {EIGA}みたい — qoʻshimcha yoʻq. "
      f"Yozuvda ham farq koʻrinadi: biri kanji bilan.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>イノムさんは"
      f"{OTOUSAN}___{NIRU}</strong></p>",
      ["に", "と", "を", "が"],
      "に",
      f"<p>{NIRU} <strong>に</strong> oladi — oʻzbekcha "
      f"«ota<strong>ga</strong> oʻxshaydi» bilan bir xil "
      f"uyacha.</p>"),

    q(f"<p>«Ikki doʻkonni taqqosladim» — qaysi qoʻshimchalar?</p>",
      [f"A と B を{KURABERU}", f"A に B を{KURABERU}",
       f"A を B と{KURABERU}", f"A が B を{KURABERU}"],
      f"A と B を{KURABERU}",
      f"<p>{KURABERU} — <strong>と</strong> bilan bogʻlab, "
      f"<strong>を</strong> bilan toʻldiruvchi qiladi. "
      f"{NIRU} esa に oladi — ikki feʼl, ikki qolip.</p>"),

    # 13–16 farqlash
    q(f"<p>{FURUMITAI} va {FURURASHII} — farqi nima?</p>",
      ["Birinchisida dalil menda, ikkinchisida gap tashqaridan",
       "Birinchisida gap tashqaridan, ikkinchisida dalil menda",
       "Birinchisi rasmiy, ikkinchisi kundalik",
       "Hech qanday farqi yoʻq"],
      "Birinchisida dalil menda, ikkinchisida gap tashqaridan",
      f"<p>みたい — ようだ ning egizagi, demak <strong>oʻz "
      f"xulosam</strong>. らしい esa «odamlar shunday "
      f"deyishdi».</p>"),

    q(f"<p>{FURISOU} va {FURUMITAI} — shakl jihatidan nimasi "
      f"farq qiladi?</p>",
      ["Birinchisi ます-oʻzakka, ikkinchisi oddiy shaklga ulanadi",
       "Birinchisi oddiy shaklga, ikkinchisi ます-oʻzakka ulanadi",
       "Ikkalasi ham ます-oʻzakka ulanadi",
       "Ikkalasi ham oddiy shaklga ulanadi"],
      "Birinchisi ます-oʻzakka, ikkinchisi oddiy shaklga ulanadi",
      f"<p>Beshta taxmin qolipidan <strong>faqat koʻrinish "
      f"そう</strong> ます-oʻzakka ulanadi. Qolgan toʻrttasi — "
      f"oddiy shaklga.</p>"),

    q(f"<p>«Qordek oq» — kundalik va kitobiy shakllari qaysi?</p>",
      [f"{YUKI}みたいに / {YUKI}のように",
       f"{YUKI}のみたいに / {YUKI}ように",
       f"{YUKI}みたいな / {YUKI}のような",
       f"{YUKI}にみたい / {YUKI}によう"],
      f"{YUKI}みたいに / {YUKI}のように",
      f"<p>Sifatdan oldin <strong>に</strong>. Va ようだ otdan "
      f"keyin <strong>の</strong> talab qiladi, みたい "
      f"talab qilmaydi.</p>"),

    q(f"<p>Qaysi qolip <strong>faqat</strong> kundalik nutqda "
      f"ishlatiladi?</p>",
      ["みたいです", "ようです", FURUSOU, "らしいです"],
      "みたいです",
      f"<p>Qolgan uchtasi rasmiy matnda ham uchraydi. みたい esa "
      f"hisobotda va yangilikda deyarli yoʻq.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [GAKUSEIMITAI, GAKUSEI + "のみたいです",
       GAKUSEI + "なみたいです", GAKUSEI + "だみたいです"],
      GAKUSEIMITAI,
      f"<p>みたい <strong>yalangʻoch</strong>. の ようだ uchun, "
      f"だ esa PJ-74 dagi xabar そう uchun.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{CHICHI}と{NIRU}", f"{CHICHI}に{NIRU}",
       f"{GAKUSEIMITAI}", f"{KODOMOMITAINA}"],
      f"{CHICHI}と{NIRU}",
      f"<p>{NIRU} <strong>に</strong> oladi. と ni "
      f"{KURABERU} bilan aralashtirmang.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibga soling.</p>"
      f"<p><strong>みたいです · {ISOGASHII} · {r('先生', 'せんせい')}は · "
      f"{r('今日', 'きょう')}</strong></p>",
      [f"{r('先生', 'せんせい')}は{r('今日', 'きょう')}{ISOGASHII}みたいです",
       f"{r('今日', 'きょう')}{ISOGASHII}は{r('先生', 'せんせい')}みたいです",
       f"{r('先生', 'せんせい')}は{ISOGASHII}{r('今日', 'きょう')}みたいです",
       f"みたいです{r('先生', 'せんせい')}は{r('今日', 'きょう')}{ISOGASHII}"],
      f"{r('先生', 'せんせい')}は{r('今日', 'きょう')}{ISOGASHII}みたいです",
      f"<p>Yapon tili SOV: baho beruvchi qism <strong>oxirida</strong>. "
      f"Vaqt soʻzi mavzudan keyin, sifatdan oldin turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: ラノさん、"
      f"{r('元気', 'げんき')}？</strong></p><p><strong>パリ: ___</strong></p>",
      [f"うん、{GENKIMITAI}よ。",
       f"うん、{GENKI}なみたいですよ。",
       f"うん、{GENKI}のみたいですよ。",
       f"うん、{GENKI}が{MITAI_V}ですよ。"],
      f"うん、{GENKIMITAI}よ。",
      f"<p>な-sifat みたい oldida <strong>yalangʻoch</strong> "
      f"qoladi. Oxirgi variant esa butunlay boshqa gap — "
      f"«tetiklikni koʻrgim bor».</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-77 — 擬音語・擬態語
# ══════════════════════════════════════════════════════════════════════
Q_PJ77 = [
    # 1–5 tanish
    q(f"<p>{GIONGO} nimani bildiradi?</p>",
      ["Quloq eshitadigan tovushni", "Koʻz koʻradigan holatni",
       "Hissiyotni", "Harakat tezligini"],
      "Quloq eshitadigan tovushni",
      f"<p>ザーザー, ドンドン, ワンワン. Holat taqlidi esa "
      f"<strong>{GITAIGO}</strong> — きらきら, ゆっくり.</p>"),

    q(f"<p>{GIONGO} odatda qaysi yozuv bilan yoziladi?</p>",
      ["Katakana", "Hiragana", "Kanji", "Romaji"],
      "Katakana",
      f"<p>Katakana «bu oddiy yapon soʻzi emas» degan belgi — "
      f"tovush soʻz emas, <strong>shovqin</strong>. {GITAIGO} "
      f"esa tuygʻu, demak hiragana.</p>"),

    q(f"<p>ザーザー nimani bildiradi?</p>",
      [f"{AME} quyib yogʻishini", f"{AME} tomchilab yogʻishini",
       "Yulduz yaltirashini", "Qattiq uyquni"],
      f"{AME} quyib yogʻishini",
      f"<p>ザーザー{FURU} — «shovullab yogʻadi». Mayda yomgʻir "
      f"esa <strong>しとしと</strong>, tomchilab boshlagani "
      f"<strong>ぽつぽつ</strong>.</p>"),

    q(f"<p>ドキドキ qaysi soʻz bilan keladi?</p>",
      ["する", "だ", "です", "ある"],
      "する",
      f"<p>{MUNE}がドキドキ<strong>します</strong>. する "
      f"qoʻshilgani uchun bu endi feʼl — tuslanadi, oʻtgan "
      f"zamonga kiradi.</p>"),

    q(f"<p>ぺこぺこ qaysi soʻz bilan keladi?</p>",
      ["だ / です", "する", "ある", "なる"],
      "だ / です",
      f"<p>{ONAKA}がぺこぺこ<strong>です</strong>. ぺこぺこする "
      f"esa «taʼzim qilmoq, xushomad qilmoq» — butunlay "
      f"boshqa maʼno.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{INU}が___と"
      f"{NAKU_A}</strong></p>",
      ["ワンワン", "わんわん", "ニャーニャー", "きらきら"],
      "ワンワン",
      f"<p>It ovozi — tovush, demak <strong>katakana</strong>. "
      f"ニャーニャー mushuk uchun, きらきら esa yaltirash.</p>"),

    q(f"<p>«Yuragim duk-duk urdi» — qaysi shakl?</p>",
      [f"{MUNE}がドキドキしました", f"{MUNE}がドキドキでした",
       f"{MUNE}がドキドキだった", f"{MUNE}がドキドキなりました"],
      f"{MUNE}がドキドキしました",
      f"<p>ドキドキ <strong>する</strong> oladi, keyin u oddiy "
      f"feʼl kabi tuslanadi.</p>"),

    q(f"<p>«Uch soat yurdim, holdan toydim» — qaysi soʻz?</p>",
      ["くたくたです", "わくわくです", "きらきらです", "ぴかぴかします"],
      "くたくたです",
      f"<p><strong>くたくた</strong> — charchoq. わくわく "
      f"quvonchli kutish, きらきら yaltirash, ぴかぴか esa "
      f"yangi va toza narsa.</p>"),

    q(f"<p>«Momaqaldiroq guldiradi» — qaysi juftlik?</p>",
      [f"ゴロゴロ{NARU}", f"ゴロゴロ{NAKU_A}",
       f"パチパチ{NARU}", f"ドンドン{HIKARU}"],
      f"ゴロゴロ{NARU}",
      f"<p>{NARU} — «jaranglamoq», jonsiz narsa uchun. "
      f"{NAKU_A} esa hayvon uchun: {INU}が{NAKU_A}.</p>"),

    q(f"<p>«Qattiq uxladim» — qaysi soʻz?</p>",
      [f"ぐっすり{NERU}", f"ゆっくり{NERU}",
       f"のろのろ{NERU}", f"さっと{NERU}"],
      f"ぐっすり{NERU}",
      f"<p><strong>ぐっすり</strong> faqat uyqu bilan keladi. "
      f"ゆっくり «shoshmasdan», のろのろ «imillab», さっと «bir "
      f"zumda».</p>"),

    q(f"<p>«Yulduzlar yaltiraydi» — qaysi juftlik?</p>",
      [f"{HOSHI}がきらきら{HIKARU}", f"{HOSHI}がきらきらです",
       f"{HOSHI}がぴかぴか{NARU}", f"{HOSHI}がザーザー{HIKARU}"],
      f"{HOSHI}がきらきら{HIKARU}",
      f"<p>きらきら — yulduz va koʻz uchun; ぴかぴか esa yangi "
      f"poyabzal yoki toza deraza uchun. Ikkalasi «yaltiroq», "
      f"lekin bir-birining oʻrnini bosmaydi.</p>"),

    q(f"<p>Takrorlanadigan AB-AB qolipi nimani bildiradi?</p>",
      ["Davomli yoki takroriy ishni", "Bir lahzalik ishni",
       "Tugagan ishni", "Kelajakdagi ishni"],
      "Davomli yoki takroriy ishni",
      f"<p>きらきら, ドキドキ, ワンワン. Bir lahzalik ish esa "
      f"<strong>A-っ-と</strong> qolipida: ぱっと, さっと.</p>"),

    # 13–16 farqlash
    q(f"<p>ゆっくり va のろのろ — ikkalasi «sekin». Farqi?</p>",
      ["ゆっくり yaxshi maʼnoda, のろのろ yomon maʼnoda",
       "ゆっくり yomon maʼnoda, のろのろ yaxshi maʼnoda",
       "ゆっくり odam uchun, のろのろ mashina uchun",
       "Hech qanday farqi yoʻq"],
      "ゆっくり yaxshi maʼnoda, のろのろ yomon maʼnoda",
      f"<p>ゆっくり — «shoshmasdan», iltifot bilan aytiladi "
      f"(ゆっくりどうぞ). のろのろ — «imillab», tanqid. "
      f"Taqlid soʻzlarining koʻpi shunday <strong>baho</strong> "
      f"olib yuradi.</p>"),

    q(f"<p>ぺこぺこ<strong>だ</strong> va ぺこぺこ<strong>する</strong> "
      f"— farqi?</p>",
      ["Birinchisi «qornim ochdi», ikkinchisi «xushomad qilmoq»",
       "Birinchisi «xushomad qilmoq», ikkinchisi «qornim ochdi»",
       "Birinchisi hozirgi, ikkinchisi oʻtgan zamon",
       "Hech qanday farqi yoʻq"],
      "Birinchisi «qornim ochdi», ikkinchisi «xushomad qilmoq»",
      f"<p>Shuning uchun har bir taqlid soʻzi "
      f"<strong>oʻz feʼli bilan</strong> yodlanadi — bu tanlov "
      f"hech qanday qoida bilan chiqmaydi.</p>"),

    q(f"<p>ザーザー va しとしと — ikkalasi yomgʻir. Farqi?</p>",
      ["ザーザー kuchli, しとしと mayda va tinch",
       "ザーザー mayda, しとしと kuchli",
       "ザーザー yozda, しとしと qishda",
       "ザーザー tovush, しとしと rang"],
      "ザーザー kuchli, しとしと mayda va tinch",
      f"<p>Va uchinchisi — <strong>ぽつぽつ</strong>, «tomchilab "
      f"boshladi». Yaponcha ob-havo maʼlumotida uchalasi ham "
      f"eshitiladi.</p>"),

    q(f"<p>きらきら hiragana bilan, ザーザー katakana bilan — "
      f"nega?</p>",
      [f"Birinchisi holat ({GITAIGO}), ikkinchisi tovush ({GIONGO})",
       f"Birinchisi tovush, ikkinchisi holat",
       "Birinchisi qadimiy, ikkinchisi yangi soʻz",
       "Ikkalasini ham ikki xil yozish mumkin, farqi yoʻq"],
      f"Birinchisi holat ({GITAIGO}), ikkinchisi tovush ({GIONGO})",
      f"<p>Qoida qatʼiy emas — mangada ikkalasi ham katakana "
      f"boʻlishi mumkin — lekin roman va gazetada shu tartib "
      f"ishlaydi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{AME}がザーザー{FURU}", f"ザーザーの{AME}が{FURU}",
       f"ザーザーな{AME}が{FURU}", f"{AME}がザーザーです"],
      f"{AME}がザーザー{FURU}",
      f"<p>Bu soʻzlar <strong>hol</strong>, sifat emas — "
      f"otni aniqlamaydi, feʼlni aniqlaydi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{ONAKA}がぺこぺこします", f"{ONAKA}がぺこぺこです",
       f"{MUNE}がドキドキします", f"{HOSHI}がきらきら{HIKARU}"],
      f"{ONAKA}がぺこぺこします",
      f"<p>ぺこぺこする «taʼzim qilmoq» degani — qorin bilan "
      f"birga ishlatilsa, gap gʻalati chiqadi. Toʻgʻrisi — "
      f"ぺこぺこ<strong>です</strong>.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibga soling.</p>"
      f"<p><strong>{FURU}っている · {AME}が · ザーザー · "
      f"{r('朝', 'あさ')}から</strong></p>",
      [f"{r('朝', 'あさ')}から{AME}がザーザー{r('降', 'ふ')}っている",
       f"{AME}がザーザー{r('朝', 'あさ')}から{r('降', 'ふ')}っている",
       f"ザーザー{r('朝', 'あさ')}から{AME}が{r('降', 'ふ')}っている",
       f"{r('朝', 'あさ')}から ザーザーが{AME}{r('降', 'ふ')}っている"],
      f"{r('朝', 'あさ')}から{AME}がザーザー{r('降', 'ふ')}っている",
      f"<p>Vaqt → ega → hol → kesim. Taqlid soʻzi "
      f"<strong>feʼlning oldida</strong> turadi, chunki u "
      f"feʼlni aniqlaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム: "
      f"{SHIKEN}はどうでしたか。</strong></p><p><strong>イムロン: "
      f"___</strong></p>",
      [f"{r('前', 'まえ')}はドキドキしましたが、{r('今', 'いま')}はくたくたです。",
       f"{r('前', 'まえ')}はドキドキでしたが、{r('今', 'いま')}はくたくたします。",
       f"{r('前', 'まえ')}はぺこぺこしましたが、{r('今', 'いま')}はきらきらです。",
       f"{r('前', 'まえ')}はザーザーしましたが、{r('今', 'いま')}はしとしとです。"],
      f"{r('前', 'まえ')}はドキドキしましたが、{r('今', 'いま')}はくたくたです。",
      f"<p>ドキドキ <strong>する</strong> oladi, くたくた "
      f"<strong>です</strong> oladi — bitta gapda ikkala yoʻl. "
      f"Oxirgi ikki variantdagi soʻzlar ob-havo va yaltirash "
      f"uchun, imtihon uchun emas.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-78 — kim qanday gapiradi
# ══════════════════════════════════════════════════════════════════════
Q_PJ78 = [
    # 1–5 tanish
    q(f"<p>Qaysi «men» hamma vaziyatda xavfsiz?</p>",
      [WATASHI, BOKU, ORE, "あたし"],
      WATASHI,
      f"<p>{WATASHI} erkak uchun ham, ayol uchun ham, rasmiy "
      f"joyda ham toʻgʻri. Qolgan uchtasi <strong>joyiga "
      f"qarab</strong> toʻgʻri yoki notoʻgʻri.</p>"),

    q(f"<p>{ORE} ning ohangi qanday?</p>",
      ["Erkakcha, dangal — faqat doʻst va tengdosh bilan",
       "Erkakcha, muloyim — oʻquvchi va talaba uchun",
       "Ayolcha, kundalik", "Neytral, hamma joyda"],
      "Erkakcha, dangal — faqat doʻst va tengdosh bilan",
      f"<p>Muloyim erkak varianti — <strong>{BOKU}</strong>. "
      f"Oʻqituvchi yoki mijoz bilan ikkalasi ham emas, "
      f"{WATASHI}.</p>"),

    q(f"<p>ぞ va ぜ qanday qoʻshimchalar?</p>",
      ["Erkakcha va dangal — yaqin doʻstlar orasida",
       "Ayolcha va yumshoq", "Neytral, hamma ishlatadi",
       "Faqat yozma tilda"],
      "Erkakcha va dangal — yaqin doʻstlar orasida",
      f"<p>Mangada juda koʻp uchraydi. Oʻqituvchiga aytilsa — "
      f"qoʻpollik.</p>"),

    q(f"<p>かしら qanday qoʻshimcha?</p>",
      ["Ayolcha — «qiziq, …mikin»", "Erkakcha — buyruq ohangi",
       "Neytral savol qoʻshimchasi", "Yoshlar tili"],
      "Ayolcha — «qiziq, …mikin»",
      f"<p>わ bilan birga — kattaroq avlod ayollarining tili. "
      f"Bugungi yosh yaponlar orasida kamdan-kam.</p>"),

    q(f"<p>Yangi tanishgan odamga «siz» ni qanday aytasiz?</p>",
      ["Ism + さん", "あなた", KIMI, OMAE],
      "Ism + さん",
      f"<p>{TANAKA}さんは{NANSAI}ですか. あなた sovuq yoki juda "
      f"yaqin eshitiladi; {KIMI} yuqoridan pastga; {OMAE} "
      f"esa dangal yoki qoʻpol.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{GAKUSEI}なの» — nega <strong>な</strong> paydo "
      f"boʻldi?</p>",
      ["だ tushirilgani uchun の dan oldin bogʻlovchi kerak",
       "の savol qoʻshimchasi boʻlgani uchun",
       f"{GAKUSEI} な-sifat boʻlgani uchun",
       "Ayol kishi gapirgani uchun"],
      "だ tushirilgani uchun の dan oldin bogʻlovchi kerak",
      f"<p>PJ-75 dagi ようだ ning <strong>な</strong> si bilan "
      f"bir xil mexanizm: ot va な-sifat oʻzidan keyin biror "
      f"narsa kelsa, bogʻlovchi talab qiladi.</p>"),

    q(f"<p>Kundalik nutqda kim だ ni koʻproq tashlab ketadi?</p>",
      ["Ayol kishi", "Erkak kishi", "Ikkalasi bir xil",
       "Faqat yozma tilda tashlanadi"],
      "Ayol kishi",
      f"<p>«これ、きれいね» ↔ «これ、きれい<strong>だ</strong>な». "
      f"Quloqqa juda aniq tegadigan farq.</p>"),

    q(f"<p>«めっちゃ» ning rasmiy muqobili nima?</p>",
      ["とても", HONTOU + "ですか", "うるさいです", "すごいです"],
      "とても",
      f"<p>めっちゃ — «juda», kuchaytiruvchi. マジ esa "
      f"«rostdan?» → {HONTOU}ですか.</p>"),

    q(f"<p>«やばい» nimani bildiradi?</p>",
      ["«Dahshat!» ham, «zoʻr!» ham — ikki maʼno ham bor",
       "Faqat «dahshat, yomon»", "Faqat «zoʻr, ajoyib»",
       "«Jonga tegadigan»"],
      "«Dahshat!» ham, «zoʻr!» ham — ikki maʼno ham bor",
      f"<p>Ohang va vaziyat hal qiladi. «Jonga tegadigan» esa "
      f"<strong>うざい</strong>.</p>"),

    q(f"<p>«してる» — bu nimaning qisqargani?</p>",
      ["している", "しておく", "しなければならない", "しました"],
      "している",
      f"<p>Bu <strong>haqiqiy kundalik yaponcha</strong>, manga "
      f"tili emas — doʻstlar bilan bemalol ishlatiladi. "
      f"〜なきゃ esa 〜なければならない ning qisqargani.</p>"),

    q(f"<p>«〜とく» — bu nimaning qisqargani?</p>",
      ["〜ておく", "〜ている", "〜てある", "〜てみる"],
      "〜ておく",
      f"<p>PJ-59 dagi 〜ておく. Bu ham kundalik nutqning oddiy "
      f"qisqarishi, badiiy til emas.</p>"),

    q(f"<p>«〜ですわ» va «〜じゃ・〜のう» — kim aytadi?</p>",
      ["Badiiy asar qahramonlari — koʻchada deyarli eshitilmaydi",
       "Hamma, kundalik nutqda",
       "Faqat yoshlar", "Faqat rasmiy joyda"],
      "Badiiy asar qahramonlari — koʻchada deyarli eshitilmaydi",
      f"<p>〜ですわ boy xonim, 〜じゃ・〜のう qariya uchun "
      f"oʻylab topilgan. してる va 〜なきゃ esa haqiqiy "
      f"kundalik yaponcha — ikkisini aralashtirmang.</p>"),

    # 13–16 farqlash
    q(f"<p>{BOKU} va {ORE} — farqi nima?</p>",
      [f"{BOKU} muloyim va kamtar, {ORE} dangal va yaqin",
       f"{BOKU} dangal, {ORE} muloyim",
       f"{BOKU} ayol uchun, {ORE} erkak uchun",
       "Hech qanday farqi yoʻq"],
      f"{BOKU} muloyim va kamtar, {ORE} dangal va yaqin",
      f"<p>Ikkalasi ham erkak nutqi. Ish suhbatida esa "
      f"ikkalasi ham emas — {WATASHI}.</p>"),

    q(f"<p>«あなた» nega ehtiyot bilan ishlatiladi?</p>",
      ["Sovuq yoki juda yaqin eshitiladi — neytral emas",
       "Juda rasmiy eshitiladi",
       "Faqat ayollar ishlatadi",
       "Grammatik jihatdan xato"],
      "Sovuq yoki juda yaqin eshitiladi — neytral emas",
      f"<p>Darsliklarda «siz» deb beriladi, lekin haqiqiy "
      f"nutqda ism ishlatiladi: {TANAKA}さん.</p>"),

    q(f"<p>«してる» va «〜ですわ» — qaysi biri haqiqiy kundalik "
      f"yaponcha?</p>",
      ["してる", "〜ですわ", "Ikkalasi ham", "Ikkalasi ham emas"],
      "してる",
      f"<p>してる, 〜なきゃ, 〜とく — kundalik nutqning oddiy "
      f"qisqarishlari. 〜ですわ, 〜じゃ, やめろ！ esa "
      f"<strong>badiiy til</strong>.</p>"),

    q(f"<p>Nega bu dars «ohanglar xaritasi» deb ataladi?</p>",
      ["Eshitib tanish uchun kerak, oʻzi gapirish uchun emas",
       "Chunki qoidalari juda qatʼiy",
       "Chunki faqat yozma tilga tegishli",
       "Chunki bu soʻzlar eskirgan"],
      "Eshitib tanish uchun kerak, oʻzi gapirish uchun emas",
      f"<p>Va bu chegara zamonaviy yapon tilida "
      f"<strong>yumshayapti</strong>. Chet ellik oʻquvchi "
      f"uchun yoʻl bitta: {WATASHI} va {TEINEI}.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{TANAKA}さんは{NANSAI}ですか",
       f"あなたは{NANSAI}ですか",
       f"{OMAE}は{NANSAI}ですか",
       f"{KIMI}は{NANSAI}ですか"],
      f"{TANAKA}さんは{NANSAI}ですか",
      f"<p>Oʻzbekchada «siz» deyiladigan joyda yaponchada "
      f"<strong>ism</strong> turadi.</p>"),

    q(f"<p>Oʻqituvchingiz «ishlaringiz qalay?» deb soʻradi. "
      f"Qaysi javobda xato bor?</p>",
      ["めっちゃやばいっす",
       f"とても{TAIHEN}です",
       "ちょっと" + r("忙", "いそが") + "しいです",
       "おかげさまで" + GENKI + "です"],
      "めっちゃやばいっす",
      f"<p>Gap notoʻgʻri emas — <strong>odobsiz</strong>. "
      f"Yoshlar tili katta odam bilan ishlatilmaydi va PJ-68…72 "
      f"dagi butun keigo tizimini buzadi.</p>"),

    # 19–20 tuzish
    q(f"<p>Mijoz bilan gaplashyapsiz. Qaysi gap toʻgʻri?</p>",
      [f"{OKYAKU}、{r('何', 'なに')}をお{r('探', 'さが')}しですか",
       f"{OMAE}、{r('何', 'なに')}が{r('欲', 'ほ')}しい",
       f"{KIMI}は{r('何', 'なに')}を{r('探', 'さが')}してるの",
       f"あなたは{r('何', 'なに')}が{r('欲', 'ほ')}しいですか"],
      f"{OKYAKU}、{r('何', 'なに')}をお{r('探', 'さが')}しですか",
      f"<p>Mijoz — «tashqi» va yuqori, demak PJ-69 dagi "
      f"<strong>{r('尊敬語', 'そんけいご')}</strong>. {OMAE} va "
      f"{KIMI} bu yerda umuman mumkin emas.</p>"),

    q(f"<p>Suhbatni toʻldiring. Munira doʻstiga gapiryapti.</p>"
      f"<p><strong>ムニラ: あ、ラノ！ もう{r('帰', 'かえ')}るの？"
      f"</strong></p><p><strong>ラノ: ___</strong></p>",
      [f"うん、{r('今日', 'きょう')}はバイトなの。",
       f"うん、{r('今日', 'きょう')}はバイトなのだぜ。",
       f"はい、{r('今日', 'きょう')}はアルバイトでございます。",
       f"うん、{r('今日', 'きょう')}はバイトでいらっしゃいます。"],
      f"うん、{r('今日', 'きょう')}はバイトなの。",
      f"<p>Doʻst bilan — kundalik nutq va の. Uchinchi va "
      f"toʻrtinchi variant doʻkon tilining keigosi "
      f"(PJ-71), doʻstga aytilsa kulgili chiqadi; "
      f"toʻrtinchisi ustiga oʻzini koʻtaradi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-76 Mashq: 〜みたいです va taqqoslash",
        "tutorial":    "PJ-76:",
        "description": "みたい yalangʻoch ulanadi, ようだ な / の "
                       "talab qiladi — va みたい ≠ 見たい.",
        "questions":   Q_PJ76,
        **DEFAULTS,
    },
    {
        "title":       "PJ-77 Mashq: 擬音語・擬態語",
        "tutorial":    "PJ-77:",
        "description": "Tovush → katakana, holat → hiragana; va har bir "
                       "soʻz する, だ yoki feʼldan bittasini oladi.",
        "questions":   Q_PJ77,
        **DEFAULTS,
    },
    {
        "title":       "PJ-78 Mashq: Kim qanday gapiradi",
        "tutorial":    "PJ-78:",
        "description": "僕 · 俺 · あたし, ぞ · ぜ · わ · かしら, "
                       "yoshlar tili va manga yaponchasi — tanib oling.",
        "questions":   Q_PJ78,
        **DEFAULTS,
    },
]
