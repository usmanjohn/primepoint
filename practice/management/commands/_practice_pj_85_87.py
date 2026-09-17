# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-85 … PJ-87.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi:
    1. BITTA HARF (PJ-85). 〜あいだ va 〜あいだに — に bor-yoʻqligi
       maʼnoni butunlay oʻzgartiradi: に boʻlsa oraliq ichidagi
       bitta nuqta, boʻlmasa butun oraliq. Va うち／あいだ ikkalasi
       ham OT: な-sifat な, ot の oladi.
    2. OʻZGARISHNING IKKI TOMONI (PJ-86). につれて ikkala tomondan
       ham oʻzgarish talab qiladi; bir martalik voqea unga
       tushmaydi, va undan keyin buyruq kelmaydi. にしたがって ning
       esa ikkinchi, butunlay boshqa vazifasi bor — «…ga muvofiq».
    3. TOʻRT VAZIFA, BITTA QOLIP (PJ-87). によって — bajaruvchi,
       sabab, vosita, farqlanish. Passivda に bilan によって ni
       ajratish: aziyat → に, yaratish → によって. Ot oldida
       による.

⚠️ CUMULATIVE: PJ-85 mashqida につれて・にしたがって (86) va によって
(87) yoʻq. PJ-86 da によって hali yoʻq.
`verify_pj_practice_85_87.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_85_87.py --master=prime \\
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


# ── feʼllar ──────────────────────────────────────────────────────────
NERU      = r("寝", "ね") + "る"
NETEIRU   = r("寝", "ね") + "ている"
FURU      = r("降", "ふ") + "る"
FURIDASHITA = r("降", "ふ") + "り" + r("出", "だ") + "した"
FUTTEITA  = r("降", "ふ") + "っていた"
KAERU     = r("帰", "かえ") + "る"
KAERIMASU = r("帰", "かえ") + "ります"
TABERU    = r("食", "た") + "べる"
WASURERU  = r("忘", "わす") + "れる"
WASURENAI = r("忘", "わす") + "れない"
KAKU      = r("書", "か") + "く"
NARAU     = r("習", "なら") + "う"
KIKU      = r("聞", "き") + "く"
KIITEIRU  = r("聞", "き") + "いている"
SOUJI     = r("掃除", "そうじ")
NOBORU    = r("登", "のぼ") + "る"
TORU      = r("年", "とし") + "をとる"
SAGARU    = r("下", "さ") + "がる"
AGARU     = r("上", "あ") + "がる"
FUERU     = r("増", "ふ") + "える"
HERU      = r("減", "へ") + "る"
NARU      = r("鳴", "な") + "る"
TATSU     = r("立", "た") + "つ"
KIRU      = r("着", "き") + "る"
KUMITATERU = r("組", "く") + "み" + r("立", "た") + "てる"
KOUDOU    = r("行動", "こうどう")
SHIKARARETA = r("叱", "しか") + "られた"
KAKARETA  = r("書", "か") + "かれた"
TSUKURARETA = r("作", "つく") + "られた"
TATERARETA = r("建", "た") + "てられた"
KOWARETA  = r("壊", "こわ") + "れた"
KAIKETSU  = r("解決", "かいけつ")
TASHIKAMERU = r("確", "たし") + "かめる"
TOMATTA   = r("止", "と") + "まった"
CHIGAU    = r("違", "ちが") + "う"
KAWARU    = r("変", "か") + "わる"
KANGAERARETEIRU = r("考", "かんが") + "えられている"
OMOU      = r("思", "おも") + "う"

# ── sifatlar ─────────────────────────────────────────────────────────
ATSUI     = r("熱", "あつ") + "い"
KURAI     = r("暗", "くら") + "い"
KURAKU    = r("暗", "くら") + "く"
WAKAI     = r("若", "わか") + "い"
AKARUI    = r("明", "あか") + "るい"
SAMUI     = r("寒", "さむ") + "い"
SAMUKU    = r("寒", "さむ") + "く"
ATATAKAKU = r("暖", "あたた") + "かく"
GENKI     = r("元気", "げんき")
NEMUI     = r("眠", "ねむ") + "い"
NEMUKU    = r("眠", "ねむ") + "く"
WARUKU    = r("悪", "わる") + "く"
OOKIKU    = r("大", "おお") + "きく"

# ── otlar ────────────────────────────────────────────────────────────
GAKUSEI   = r("学生", "がくせい")
NATSUYASUMI = r("夏休", "なつやす") + "み"
UNTEN     = r("運転", "うんてん")
AME       = r("雨", "あめ")
HAHA      = r("母", "はは")
ONGAKU    = r("音楽", "おんがく")
JIKAN     = r("時間", "じかん")
KION      = r("気温", "きおん")
JINKOU    = r("人口", "じんこう")
KURUMA    = r("車", "くるま")
KAZU      = r("数", "かず")
TOSHI     = r("都市", "とし")
KUUKI     = r("空気", "くうき")
SETSUMEISHO = r("説明書", "せつめいしょ")
SHIJI     = r("指示", "しじ")
KISOKU    = r("規則", "きそく")
SENSEI    = r("先生", "せんせい")
NATSUME   = r("夏目漱石", "なつめそうせき")
TAIFUU    = r("台風", "たいふう")
HIGAI     = r("被害", "ひがい")
JISHIN    = r("地震", "じしん")
IE        = r("家", "いえ")
HITO      = r("人", "ひと")
KANGAEKATA = r("考", "かんが") + "え" + r("方", "かた")
MONDAI    = r("問題", "もんだい")
HANASHIAI = r("話", "はな") + "し" + r("合", "あ") + "い"
JIKKEN    = r("実験", "じっけん")
OOAME     = r("大雨", "おおあめ")
DENSHA    = r("電車", "でんしゃ")
TERA      = r("寺", "てら")
HASSEIKI  = r("八世紀", "はっせいき")
YOUBI     = r("曜日", "ようび")
HOUHOU    = r("方法", "ほうほう")
KUNI      = r("国", "くに")
ASAGOHAN  = r("朝", "あさ") + "ごはん"
BERU      = "ベル"
KOOTO     = "コート"
GOHAN     = "ごはん"
MINNA     = "みんな"

# ── tayyor qoliplar ──────────────────────────────────────────────────
GAKUSEI_NO_UCHI = GAKUSEI + "のうちに"
GAKUSEI_UCHI    = GAKUSEI + "うちに"
GENKI_NA_UCHI   = GENKI + "なうちに"
GENKI_UCHI      = GENKI + "うちに"
KURAKU_NARANAI  = KURAKU + "ならないうちに"
KURAKU_NAI      = KURAKU + "ないうちに"
TORU_NI         = TORU + "につれて"
TORIMASU_NI     = r("年", "とし") + "をとりますにつれて"
TOTTA_NI        = r("年", "とし") + "をとったにつれて"
SETSU_SHITAGATTE = SETSUMEISHO + "にしたがって"
SETSU_TSURETE    = SETSUMEISHO + "につれて"
TAIFUU_NIYORU   = TAIFUU + "による" + HIGAI
TAIFUU_NIYOTTE  = TAIFUU + "によって" + HIGAI
SENSEI_NI       = SENSEI + "に" + SHIKARARETA
SENSEI_NIYOTTE  = SENSEI + "によって" + SHIKARARETA


# ══════════════════════════════════════════════════════════════════════
# PJ-85 — 〜うちに va 〜あいだに
# ══════════════════════════════════════════════════════════════════════
Q_PJ85 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>うちに va あいだに orasidagi asosiy farq nimada?</p>",
      ["うちに — holat oʻz-oʻzidan oʻzgaradi; あいだに — chegarasi "
       "aniq muddat",
       "あいだに — holat oʻz-oʻzidan oʻzgaradi; うちに — chegarasi "
       "aniq muddat",
       "Ikkalasi ham bir xil, faqat うちに kitobiy",
       "うちに faqat oʻtgan zamonda ishlatiladi"],
      "うちに — holat oʻz-oʻzidan oʻzgaradi; あいだに — chegarasi "
      "aniq muddat",
      f"<p><strong>うちに ning oynasi oʻz-oʻzidan yopiladi</strong>: "
      f"ovqat sovuydi, kun qorayadi, yoshlik oʻtadi. あいだに ning "
      f"chegarasi esa kalendarda turadi: {NATSUYASUMI}のあいだに, "
      f"{HAHA}がいないあいだに.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NETEIRU}あいだ___、"
      f"{AME}が{FURIDASHITA}。</strong></p>",
      ["に", "で", "は", "hech nima"],
      "に",
      f"<p><strong>{NETEIRU}あいだに</strong>. Yogʻa boshlash — bir "
      f"martalik ish, u oraliqning bitta nuqtasida boʻlib oʻtadi. "
      f"に aynan oʻsha nuqtani belgilaydi.</p>"),

    q(f"<p>{NETEIRU}あいだ、ずっと{AME}が{FUTTEITA} — bu gapda に nega "
      f"yoʻq?</p>",
      ["Ish butun oraliq davomida davom etgani uchun",
       "Gap oʻtgan zamonda boʻlgani uchun",
       "あいだ dan keyin に hech qachon qoʻyilmagani uchun",
       "ずっと bilan に ishlatilmagani uchun"],
      "Ish butun oraliq davomida davom etgani uchun",
      f"<p><strong>Ish butun oraliq davomida davom etgan.</strong> "
      f"に oraliqning ichidagi bitta nuqtani koʻrsatadi; bu yerda "
      f"esa yomgʻir boshidan oxirigacha yoqqan, shuning uchun に "
      f"tushmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GAKUSEI}___うちに、"
      f"たくさん{r('本', 'ほん')}を{r('読', 'よ')}みたい。</strong></p>",
      ["の", "な", "だ", "hech nima"],
      "の",
      f"<p><strong>{GAKUSEI_NO_UCHI}</strong>. うち — ot, shuning "
      f"uchun ot oldidan <strong>の</strong> oladi. Bu aynan PJ-81 "
      f"dagi はず bilan bir xil ulanish.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GENKI}___うちに、"
      f"{r('山', 'やま')}に{r('登', 'のぼ')}りたい。</strong></p>",
      ["な", "の", "だ", "hech nima"],
      "な",
      f"<p><strong>{GENKI_NA_UCHI}</strong>. {GENKI} — な-sifat, va "
      f"u うち dan oldin <strong>な</strong> ni saqlaydi. Ot esa の "
      f"oladi — ikkovini adashtirmang.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ATSUI}___"
      f"{TABERU[:-1]}てください。</strong> («issiqligida yeng»)</p>",
      ["うちに", "あいだに", "あいだ", "うち"],
      "うちに",
      f"<p><strong>{ATSUI}うちに</strong>. Ovqat sovuydi — oyna "
      f"oʻz-oʻzidan yopiladi. Oʻzbekcha «issiq<strong>ligida</strong>» "
      f"ham aynan shu maʼnoni beradi.</p>"),

    q(f"<p>«Unutmasdan yozib qoʻyaman» — qaysi gap toʻgʻri?</p>",
      [f"{WASURENAI}うちに{KAKU[:-1]}いておきます",
       f"{WASURERU}うちに{KAKU[:-1]}いておきます",
       f"{WASURERU[:-1]}なくうちに{KAKU[:-1]}いておきます",
       f"{WASURENAI}あいだ{KAKU[:-1]}いておきます"],
      f"{WASURENAI}うちに{KAKU[:-1]}いておきます",
      f"<p><strong>{WASURENAI}うちに</strong>. «… boʻlmasdan oldin» "
      f"degani uchun ない-shakli kerak (PJ-34). Oʻzbekcha "
      f"«unut<strong>masdan</strong>» ham inkor — tarjima "
      f"soʻzma-soʻz ishlaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KURAKU}___うちに"
      f"{KAERIMASU}。</strong> («qorongʻi tushmasdan qaytaman»)</p>",
      ["ならない", "ない", "なくて", "なく"],
      "ならない",
      f"<p><strong>{KURAKU_NARANAI}</strong>. Sifat avval feʼlga "
      f"aylanadi ({KURAKU}なる), keyin ない-shakliga oʻtadi. "
      f"«{KURAKU_NAI}» degan gap yaponchada yoʻq.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NATSUYASUMI}の___"
      f"{UNTEN}を{NARAU[:-1]}いたい。</strong></p>",
      ["あいだに", "うちに", "あいだ", "うち"],
      "あいだに",
      f"<p><strong>{NATSUYASUMI}のあいだに</strong>. Taʼtilning boshi "
      f"ham, oxiri ham kalendarda aniq — bu oyna soat boʻyicha "
      f"yopiladi. うち esa oʻzgarib ketadigan holat uchun.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ONGAKU}を{KIITEIRU}"
      f"うちに、{NEMUKU}___。</strong></p>",
      ["なってきた", "なっている", "ならない", "なった<ruby>人<rt>ひと</rt></ruby>"],
      "なってきた",
      f"<p><strong>{NEMUKU}なってきた</strong>. 〜ているうちに "
      f"sezilmagan oʻzgarishni bildiradi, shuning uchun keyingi "
      f"gapda koʻpincha なる yoki 〜てくる turadi.</p>"),

    q(f"<p>{WAKAI}うちに、いろいろな{KUNI}へ{r('行', 'い')}く — nega bu "
      f"yerda うち turadi?</p>",
      ["Yoshlik chegarasi kalendarda yoʻq, lekin u albatta tugaydi",
       "Yoshlikning boshi va oxiri aniq belgilangan",
       "うち har doim sifat bilan keladi",
       "あいだ faqat feʼl bilan keladi"],
      "Yoshlik chegarasi kalendarda yoʻq, lekin u albatta tugaydi",
      f"<p><strong>Yoshlik oʻz-oʻzidan tugaydi.</strong> Aynan "
      f"shunday holatlar うちに ni chaqiradi — uning ichida doim "
      f"bir oz shoshilish bor. あいだ esa chegarasi belgilangan "
      f"muddat uchun.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HAHA}がいない___、"
      f"{SOUJI}をしておく。</strong></p>",
      ["あいだに", "あいだ", "うち", "あいだで"],
      "あいだに",
      f"<p><strong>いないあいだに</strong>. Onaning yoʻqligi — boshi "
      f"va oxiri bor oraliq, tozalash esa uning ichidagi bitta "
      f"ish. Butun oraliq davomida davom etsa, に tushardi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>«Men uxlab yotganimda tinimsiz yomgʻir yogʻdi» — qaysi gap "
      f"toʻgʻri?</p>",
      [f"{NETEIRU}あいだ、ずっと{AME}が{FUTTEITA}",
       f"{NETEIRU}あいだに、ずっと{AME}が{FUTTEITA}",
       f"{NETEIRU}うちに、ずっと{AME}が{FUTTEITA}",
       f"{NETEIRU}うち、ずっと{AME}が{FUTTEITA}"],
      f"{NETEIRU}あいだ、ずっと{AME}が{FUTTEITA}",
      f"<p><strong>あいだ</strong> — に siz. «Tinimsiz» degani ish "
      f"butun oraliq davomida davom etganini bildiradi, demak "
      f"bitta nuqtani koʻrsatadigan に bu yerga tushmaydi.</p>"),

    q("<p>Qaysi holatda うちに emas, あいだに ishlatiladi?</p>",
      ["Chegarasi kalendarda aniq muddat haqida gapirganda",
       "Ovqat sovib qolishidan oldin",
       "Yosh ekanida",
       "Qorongʻi tushmasdan oldin"],
      "Chegarasi kalendarda aniq muddat haqida gapirganda",
      f"<p><strong>Chegarasi aniq muddat</strong>: "
      f"{NATSUYASUMI}のあいだに, {r('授業', 'じゅぎょう')}のあいだに. "
      f"Qolgan uchtasida esa holat oʻz-oʻzidan oʻzgaradi — bu "
      f"うちに ning maydoni.</p>"),

    q(f"<p>«Yomgʻir yogʻmasdan qaytaylik» — qaysi gap toʻgʻri?</p>",
      [f"{AME}が{FURU[:-1]}らないうちに{KAERU[:-1]}りましょう",
       f"{AME}が{FURU}うちに{KAERU[:-1]}りましょう",
       f"{AME}が{FURU[:-1]}らないあいだ{KAERU[:-1]}りましょう",
       f"{AME}が{FURU[:-1]}らなくうちに{KAERU[:-1]}りましょう"],
      f"{AME}が{FURU[:-1]}らないうちに{KAERU[:-1]}りましょう",
      f"<p><strong>{FURU[:-1]}らないうちに</strong>. «… boʻlmasdan "
      f"oldin» uchun ない-shakli + うちに kerak. Tasdiq shakli "
      f"({FURU}うちに) «yomgʻir yogʻayotgan paytda» degan boshqa "
      f"maʼnoni berardi.</p>"),

    q("<p>〜ているうちに qanday maʼno qoʻshadi?</p>",
      ["Ish qilib turganda sezilmagan holda boshqa narsa oʻzgardi",
       "Ish ataylab, rejaga koʻra qilindi",
       "Ish hali boshlanmagan",
       "Ish har kuni takrorlanadi"],
      "Ish qilib turganda sezilmagan holda boshqa narsa oʻzgardi",
      f"<p><strong>Sezilmagan oʻzgarish.</strong> {ONGAKU}を{KIITEIRU}"
      f"うちに、{NEMUKU}なってきた — hech kim buni "
      f"rejalashtirmagan. Oʻzbekchada «…b oʻtirib» degan qolip "
      f"shu ishni qiladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [KURAKU_NAI + KAERIMASU,
       KURAKU_NARANAI + KAERIMASU,
       GAKUSEI_NO_UCHI,
       GENKI_NA_UCHI],
      KURAKU_NAI + KAERIMASU,
      f"<p>Xato <strong>{KURAKU_NAI}</strong> da: sifat "
      f"toʻgʻridan-toʻgʻri inkor qilinmaydi. Avval feʼlga "
      f"aylanadi ({KURAKU}なる), keyin ない-shakliga oʻtadi — "
      f"<strong>{KURAKU_NARANAI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [GAKUSEI_NO_UCHI,
       GAKUSEI_UCHI,
       GAKUSEI + "だうちに",
       GAKUSEI + "なうちに"],
      GAKUSEI_NO_UCHI,
      f"<p><strong>{GAKUSEI_NO_UCHI}</strong>. うち ot boʻlgani "
      f"uchun ot oldidan <strong>の</strong> oladi. だ ham, な ham "
      f"bu yerga tushmaydi — な faqat な-sifatlar uchun.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{KURAKU} / "
      f"ならない / うちに / {KAERU[:-1]}りましょう</strong></p>",
      [f"{KURAKU}ならないうちに{KAERU[:-1]}りましょう",
       f"うちに{KURAKU}ならない{KAERU[:-1]}りましょう",
       f"{KURAKU}うちにならない{KAERU[:-1]}りましょう",
       f"{KAERU[:-1]}りましょう{KURAKU}ならないうちに"],
      f"{KURAKU}ならないうちに{KAERU[:-1]}りましょう",
      f"<p><strong>{KURAKU_NARANAI}{KAERU[:-1]}りましょう</strong>. "
      f"Vaqt qolipi birinchi, asosiy gap keyin — yapon gapida "
      f"kesim doim oxirida turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>{HAHA}: {GOHAN}が"
      f"できましたよ。</strong></p><p><strong>ラノ: ___</strong></p>",
      [f"はい、{ATSUI}うちにいただきます。",
       f"はい、{ATSUI}あいだにいただきます。",
       f"はい、{ATSUI}うちいただきます。",
       f"はい、{ATSUI}のうちにいただきます。"],
      f"はい、{ATSUI}うちにいただきます。",
      f"<p><strong>{ATSUI}うちに</strong> — ovqat sovib qolmasdan. "
      f"い-sifat うち ga yalangʻoch ulanadi, の olmaydi; あいだ esa "
      f"chegarasi aniq muddat uchun.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-86 — 〜につれて va 〜にしたがって
# ══════════════════════════════════════════════════════════════════════
Q_PJ86 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜につれて nimani bildiradi?</p>",
      ["Ikki narsa birga, sekin-asta oʻzgaradi",
       "Bir ish tugagandan keyin ikkinchisi boshlanadi",
       "Ikki ish bir vaqtda qilinadi",
       "Ish qoidaga muvofiq bajariladi"],
      "Ikki narsa birga, sekin-asta oʻzgaradi",
      f"<p><strong>Ikki narsa birga oʻzgaradi</strong>: {TORU_NI}、"
      f"{JIKAN}が{r('早', 'はや')}く{r('感', 'かん')}じられる. "
      f"Oʻzbekcha «…gan sari» — aynan shu qolipning oʻzi.</p>"),

    q("<p>〜につれて qaysi shaklga ulanadi?</p>",
      [f"{r('辞書形', 'じしょけい')} yoki ot",
       "ます-shakli",
       "た-shakli",
       "て-shakli"],
      f"{r('辞書形', 'じしょけい')} yoki ot",
      f"<p><strong>{r('辞書形', 'じしょけい')} yoki ot</strong>: "
      f"{TORU_NI}, {JIKAN}の{r('経過', 'けいか')}につれて. "
      f"«{TORIMASU_NI}» ham, «{TOTTA_NI}» ham notoʻgʻri — qolip "
      f"hozir davom etayotgan oʻzgarish haqida.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('年', 'とし')}を___"
      f"につれて、{JIKAN}が{r('早', 'はや')}く{r('感', 'かん')}じられる"
      f"ようになる。</strong></p>",
      ["とる", "とります", "とった", "とって"],
      "とる",
      f"<p><strong>{TORU_NI}</strong>. Lugʻat shakli kerak. "
      f"ます-shakli ham, oʻtgan zamon ham, て-shakli ham bu "
      f"yerga tushmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SETSUMEISHO}___"
      f"{KUMITATERU[:-1]}てください。</strong> («qoʻllanmaga muvofiq "
      f"yigʻing»)</p>",
      ["にしたがって", "につれて", "のうちに", "のあいだに"],
      "にしたがって",
      f"<p><strong>{SETSU_SHITAGATTE}</strong>. Qoʻllanma "
      f"oʻzgarayotgani yoʻq — bu «…ga muvofiq» maʼnosi, va u "
      f"faqat にしたがって da bor. «{SETSU_TSURETE}» notoʻgʻri.</p>"),

    q("<p>Oʻzbekcha «…gan sari» ning yaponcha jufti qaysi biri?</p>",
      ["〜につれて", "〜てから", "〜あいだに", "〜たら"],
      "〜につれて",
      f"<p><strong>〜につれて</strong>. Ikkalasi ham gapning "
      f"oʻrtasida, birinchi oʻzgarishdan keyin turadi. Shuning "
      f"uchun tarjima qilayotganda oʻzbekcha gapni tuzing va "
      f"«…gan sari» qayerda ekanini koʻring.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KISOKU}___"
      f"{KOUDOU}する。</strong> («qoidaga muvofiq ish tutmoq»)</p>",
      ["にしたがって", "につれて", "のあいだに", "のうちに"],
      "にしたがって",
      f"<p><strong>{KISOKU}にしたがって</strong>. Qoida, koʻrsatma, "
      f"qonun, anʼana — bularning hammasi «…ga muvofiq» maʼnosini "
      f"chaqiradi. Qoida oʻzgarayotgani yoʻq, shuning uchun "
      f"につれて mumkin emas.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{TOSHI}が{OOKIKU}"
      f"なる___、{KUUKI}が{WARUKU}なってきた。</strong></p>",
      ["につれて", "のあいだに", "のうちに", "たら"],
      "につれて",
      f"<p><strong>{OOKIKU}なるにつれて</strong>. Ikkala tomon ham "
      f"sifatdan yasalgan feʼl ({OOKIKU}なる, {WARUKU}なる) — "
      f"oʻzgarish qoliplarining eng tabiiy jufti.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{JINKOU}が{FUERU}"
      f"につれて、{KURUMA}の{KAZU}___{FUERU[:-1]}た。</strong></p>",
      ["も", "は", "が", "を"],
      "も",
      f"<p><strong>{KAZU}も{FUERU[:-1]}た</strong>. «U ham» degan "
      f"{r('助詞', 'じょし')} ikki oʻzgarishning birga "
      f"borayotganini kuchaytiradi, shuning uchun bu qolip bilan "
      f"juda tez-tez keladi.</p>"),

    q(f"<p>Nega «{BERU}が{NARU}につれて、{MINNA}が{TATSU[:-1]}った» "
      f"notoʻgʻri?</p>",
      ["Qoʻngʻiroq bir marta jiringlaydi — bu oʻzgarish emas",
       "につれて faqat yozma tilda ishlatiladi",
       "につれて oʻtgan zamon bilan kelmaydi",
       f"{BERU} ot boʻlgani uchun につれて olmaydi"],
      "Qoʻngʻiroq bir marta jiringlaydi — bu oʻzgarish emas",
      f"<p><strong>Bir martalik voqea.</strong> につれて ikkala "
      f"tomondan ham oʻzgarish talab qiladi. Bu yerda PJ-51 "
      f"dagi <strong>と</strong> kerak: {BERU}が{NARU}と、"
      f"{MINNA}が{TATSU[:-1]}った.</p>"),

    q(f"<p>«Sovuq boʻlsa, palto kiying» — qaysi gap toʻgʻri?</p>",
      [f"{SAMUKU}なったら、{KOOTO}を{KIRU[:-1]}てください",
       f"{SAMUKU}なるにつれて、{KOOTO}を{KIRU[:-1]}てください",
       f"{SAMUKU}なるにしたがって、{KOOTO}を{KIRU[:-1]}てください",
       f"{SAMUKU}なるあいだに、{KOOTO}を{KIRU[:-1]}てください"],
      f"{SAMUKU}なったら、{KOOTO}を{KIRU[:-1]}てください",
      f"<p><strong>{SAMUKU}なったら</strong>. につれて li gapdan "
      f"keyin iltimos yoki buyruq kelmaydi — qolip kuzatilgan "
      f"oʻzgarish haqida xabar beradi, kimgadir buyurmaydi. "
      f"Buyruq uchun PJ-50 dagi たら.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('高', 'たか')}く"
      f"{NOBORU}にしたがって、{KION}が___。</strong></p>",
      [f"{SAGARU}", f"{AGARU}", f"{FUERU}", f"{HERU}"],
      f"{SAGARU}",
      f"<p><strong>{KION}が{SAGARU}</strong> — balandlikka "
      f"chiqqan sari harorat tushadi. Bu qolipda ikkala tomon "
      f"ham oʻzgarish boʻlgani uchun にしたがって toʻgʻri "
      f"ishlaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('係', 'かかり')}の"
      f"{HITO}の{SHIJI}___、ゆっくり{r('外', 'そと')}へ{r('出', 'で')}て"
      f"ください。</strong></p>",
      ["にしたがって", "につれて", "のうちに", "のあいだ"],
      "にしたがって",
      f"<p><strong>{SHIJI}にしたがって</strong> — «koʻrsatmaga "
      f"muvofiq». Bu yaponcha eʼlonlarning odatiy tili: "
      f"vokzalda, maktabda, samolyotda shu gapni eshitasiz.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>Qaysi qolipda «…ga muvofiq» degan ikkinchi maʼno bor?</p>",
      ["〜にしたがって", "〜につれて", "〜あいだに", "〜うちに"],
      "〜にしたがって",
      f"<p><strong>〜にしたがって</strong>. U {r('従', 'したが')}う "
      f"(«ergashmoq, boʻysunmoq») feʼlidan kelib chiqqan, shuning "
      f"uchun {KISOKU}にしたがって — «qoidaga muvofiq». につれて da "
      f"bu maʼno umuman yoʻq.</p>"),

    q(f"<p>«Bahor kelsa, har safar issiq boʻladi» — qaysi qolip "
      f"tabiiy?</p>",
      [f"{r('春', 'はる')}になると", f"{r('春', 'はる')}になるにつれて",
       f"{r('春', 'はる')}になるあいだに", f"{r('春', 'はる')}になるうちに"],
      f"{r('春', 'はる')}になると",
      f"<p><strong>{r('春', 'はる')}になると</strong> — PJ-51 dagi "
      f"と «har safar shunday boʻladi» degan takrorlanadigan "
      f"qoidani bildiradi. につれて esa bitta, davom etayotgan "
      f"oʻzgarishni kuzatadi.</p>"),

    q(f"<p>{SETSUMEISHO}につれて{KUMITATERU} — nega notoʻgʻri?</p>",
      ["Qoʻllanma oʻzgarmaydi, につれて esa oʻzgarish talab qiladi",
       "につれて otga umuman ulanmaydi",
       "につれて faqat inkor bilan keladi",
       f"{KUMITATERU} feʼli bu qolipni olmaydi"],
      "Qoʻllanma oʻzgarmaydi, につれて esa oʻzgarish talab qiladi",
      f"<p><strong>Qoʻllanma oʻzgarmaydi.</strong> につれて ikkala "
      f"tomondan ham oʻzgarish talab qiladi. «Muvofiq» maʼnosi "
      f"esa faqat にしたがって da bor: "
      f"<strong>{SETSU_SHITAGATTE}</strong>.</p>"),

    q("<p>Kundalik suhbatda につれて oʻrniga nima ishlatiladi?</p>",
      ["〜と yoki だんだん", "〜あいだに", "〜うちに", "〜にしたがって"],
      "〜と yoki だんだん",
      f"<p><strong>〜と yoki だんだん</strong>: "
      f"{r('春', 'はる')}になると、だんだん{ATATAKAKU}なる. につれて "
      f"va にしたがって — maqola, darslik va yangilik tili. Ularni "
      f"oʻqish uchun oʻrganing, gapirish uchun emas.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [TORIMASU_NI,
       TORU_NI,
       SETSU_SHITAGATTE,
       f"{JINKOU}が{FUERU}につれて"],
      TORIMASU_NI,
      f"<p>Xato <strong>{TORIMASU_NI}</strong> da: qolip "
      f"<strong>{r('辞書形', 'じしょけい')}</strong> ga ulanadi, "
      f"ます-shakliga emas. Toʻgʻrisi — "
      f"<strong>{TORU_NI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [TORU_NI,
       TOTTA_NI,
       TORIMASU_NI,
       r("年", "とし") + "をとってにつれて"],
      TORU_NI,
      f"<p><strong>{TORU_NI}</strong>. Faqat lugʻat shakli. "
      f"Oʻtgan zamon, ます-shakli va て-shakli — uchalasi ham "
      f"notoʻgʻri, chunki qolip hozir davom etayotgan oʻzgarish "
      f"haqida.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{JINKOU} / "
      f"が / {FUERU} / につれて / {KURUMA}の{KAZU}も{FUERU[:-1]}た"
      f"</strong></p>",
      [f"{JINKOU}が{FUERU}につれて、{KURUMA}の{KAZU}も{FUERU[:-1]}た",
       f"{KURUMA}の{KAZU}も{FUERU[:-1]}たにつれて、{JINKOU}が{FUERU}",
       f"{JINKOU}につれて{FUERU}が、{KURUMA}の{KAZU}も{FUERU[:-1]}た",
       f"につれて{JINKOU}が{FUERU}、{KURUMA}の{KAZU}も{FUERU[:-1]}た"],
      f"{JINKOU}が{FUERU}につれて、{KURUMA}の{KAZU}も{FUERU[:-1]}た",
      f"<p><strong>{JINKOU}が{FUERU}につれて、{KURUMA}の{KAZU}も"
      f"{FUERU[:-1]}た</strong>. Birinchi oʻzgarish + につれて, "
      f"keyin ikkinchi oʻzgarish. Tartib hech qachon "
      f"almashmaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム: この{r('山', 'やま')}"
      f"は{r('上', 'うえ')}のほうが{SAMUI}ですか。</strong></p>"
      f"<p><strong>ムニラ: ___</strong></p>",
      [f"はい、{r('高', 'たか')}く{NOBORU}につれて{KION}が{SAGARU}ので、"
       f"{r('上', 'うえ')}は{SAMUI}です。",
       f"はい、{r('高', 'たか')}く{r('登', 'のぼ')}りますにつれて{KION}が"
       f"{SAGARU}ので、{r('上', 'うえ')}は{SAMUI}です。",
       f"はい、{r('高', 'たか')}く{r('登', 'のぼ')}ったにつれて{KION}が"
       f"{SAGARU}ので、{r('上', 'うえ')}は{SAMUI}です。",
       f"はい、{r('高', 'たか')}く{NOBORU}につれて{KION}が{AGARU}ので、"
       f"{r('上', 'うえ')}は{SAMUI}です。"],
      f"はい、{r('高', 'たか')}く{NOBORU}につれて{KION}が{SAGARU}ので、"
      f"{r('上', 'うえ')}は{SAMUI}です。",
      f"<p>Balandlikka chiqqan sari harorat tushadi, shuning uchun "
      f"choʻqqi sovuqroq. Sabab PJ-53 dagi <strong>ので</strong> "
      f"bilan berilgan va ikkala tomon ham oʻzgarish — qolip "
      f"toʻgʻri ishlaydi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-87 — 〜によって va yozma passiv
# ══════════════════════════════════════════════════════════════════════
Q_PJ87 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>によって ning toʻrtta vazifasi qaysilar?</p>",
      ["Bajaruvchi, sabab, vosita, farqlanish",
       "Vaqt, joy, sabab, maqsad",
       "Taxmin, ishonch, xulosa, burch",
       "Buyruq, taqiq, ruxsat, iltimos"],
      "Bajaruvchi, sabab, vosita, farqlanish",
      f"<p><strong>Bajaruvchi</strong> (tomonidan), "
      f"<strong>sabab</strong> (tufayli), <strong>vosita</strong> "
      f"(orqali), <strong>farqlanish</strong> (ga qarab). "
      f"Toʻrtalasi bitta savolga javob beradi: gapdagi ish "
      f"qayerdan kelib chiqdi?</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>『{r('坊', 'ぼっ')}"
      f"ちゃん』は{NATSUME}___{KAKARETA}。</strong></p>",
      ["によって", "に", "で", "から"],
      "によって",
      f"<p><strong>{NATSUME}によって{KAKARETA}</strong>. "
      f"{KAKU} — yaratish feʼli, shuning uchun bajaruvchi "
      f"によって bilan koʻrsatiladi. Hech kim aziyat chekmadi — "
      f"bu shunchaki maʼlumot.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENSEI}___"
      f"{SHIKARARETA}。</strong> («ustoz meni urishdi»)</p>",
      ["に", "によって", "で", "から"],
      "に",
      f"<p><strong>{SENSEI_NI}</strong>. Gap odam haqida va u "
      f"taʼsir koʻrgan — bu PJ-64 dagi aziyat passivi, unda "
      f"oddiy <strong>に</strong> turadi. によって esa yaratish "
      f"va rasmiy xabar uchun.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{TAIFUU}___{HIGAI}"
      f"が{r('新聞', 'しんぶん')}に{r('出', 'で')}ていた。</strong></p>",
      ["による", "によって", "によっての", "によっては"],
      "による",
      f"<p><strong>{TAIFUU_NIYORU}</strong>. Ot oldida qolip "
      f"<strong>による</strong> ga oʻzgaradi — bu PJ-48 dagi "
      f"aniqlovchi ergash gapning oʻzi. «{TAIFUU_NIYOTTE}» "
      f"notoʻgʻri.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HITO}によって"
      f"{KANGAEKATA}が___。</strong></p>",
      [f"{CHIGAU}", f"{TSUKURARETA}", f"{KOWARETA}", f"{KAKARETA}"],
      f"{CHIGAU}",
      f"<p><strong>{HITO}によって{KANGAEKATA}が{CHIGAU}</strong> — "
      f"«odamga qarab fikrlash tarzi har xil». Farqlanish "
      f"maʼnosida gap deyarli har doim {CHIGAU}, {KAWARU} yoki "
      f"{r('決', 'き')}まる bilan tugaydi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>{JISHIN}によって{IE}が{KOWARETA} — bu yerda によって qaysi "
      f"maʼnoda?</p>",
      ["Sabab — «zilzila tufayli»",
       "Bajaruvchi — «zilzila tomonidan»",
       "Vosita — «zilzila orqali»",
       "Farqlanish — «zilzilaga qarab»"],
      "Sabab — «zilzila tufayli»",
      f"<p><strong>Sabab.</strong> によって oldida odam emas, "
      f"tabiiy hodisa turgani uchun maʼno «tufayli» boʻladi. "
      f"PJ-53 dagi ので ham boʻlardi — farqi ohangda: によって "
      f"yozma va rasmiy.</p>"),

    q(f"<p>{MONDAI}は{HANASHIAI}によって{KAIKETSU}した — bu yerda "
      f"によって qaysi maʼnoda?</p>",
      ["Vosita — «suhbat orqali»",
       "Sabab — «suhbat tufayli»",
       "Bajaruvchi — «suhbat tomonidan»",
       "Farqlanish — «suhbatga qarab»"],
      "Vosita — «suhbat orqali»",
      f"<p><strong>Vosita.</strong> によって oldida usul yoki yoʻl "
      f"tursa, maʼnosi «orqali» boʻladi: "
      f"{JIKKEN}によって{TASHIKAMERU} — «tajriba orqali "
      f"tekshirmoq».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('開', 'ひら')}いて"
      f"いる{JIKAN}は{YOUBI}によって___。</strong></p>",
      [f"{CHIGAU}", f"{TSUKURARETA}", f"{TATERARETA}", f"{TOMATTA}"],
      f"{CHIGAU}",
      f"<p><strong>{YOUBI}によって{CHIGAU}</strong> — «kunga qarab "
      f"farq qiladi». Bu によって ning toʻrtinchi maʼnosi, va u "
      f"doim {CHIGAU} yoki {KAWARU} bilan keladi.</p>"),

    q(f"<p>«Bu ibodatxona sakkizinchi asrda qurilgan» — qaysi gap "
      f"tabiiy?</p>",
      [f"この{TERA}は{HASSEIKI}に{TATERARETA}",
       f"この{TERA}は{HASSEIKI}によって{TATERARETA}",
       f"この{TERA}は{HASSEIKI}による{TATERARETA}",
       f"この{TERA}は{HASSEIKI}にによって{TATERARETA}"],
      f"この{TERA}は{HASSEIKI}に{TATERARETA}",
      f"<p><strong>{HASSEIKI}に{TATERARETA}</strong>. Bajaruvchi "
      f"umuman aytilmagan, chunki u muhim emas — yozma matnda "
      f"passivning eng koʻp uchraydigan koʻrinishi shu. "
      f"{HASSEIKI} — vaqt, bajaruvchi emas, shuning uchun によって "
      f"olmaydi.</p>"),

    q(f"<p>Ilmiy maqolada «{r('私', 'わたし')}は、この{HOUHOU}がいいと"
      f"{OMOU}» oʻrniga nima yoziladi?</p>",
      [f"この{HOUHOU}がいいと{KANGAERARETEIRU}",
       f"この{HOUHOU}がいいと{OMOU}ようになる",
       f"この{HOUHOU}がいいと{OMOU}べきだ",
       f"この{HOUHOU}がいいと{OMOU}ばかりだ"],
      f"この{HOUHOU}がいいと{KANGAERARETEIRU}",
      f"<p><strong>{KANGAERARETEIRU}</strong> — «shunday deb "
      f"hisoblanadi». Yozma matn xolis ovozni talab qiladi, "
      f"shuning uchun «men oʻylaymanki» degan gap ilmiy matnda "
      f"oʻrinsiz.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{OOAME}___、{DENSHA}"
      f"が{TOMATTA}。</strong></p>",
      ["によって", "による", "によっての", "によっては"],
      "によって",
      f"<p><strong>{OOAME}によって</strong> — «kuchli yomgʻir "
      f"tufayli». Gapning davomi feʼl bilan keladi, shuning "
      f"uchun による emas, によって. による faqat ot oldida "
      f"turadi.</p>"),

    q(f"<p>«Bu usul butun dunyoda qoʻllanadi» — qaysi gap tabiiy?</p>",
      [f"この{HOUHOU}は{r('世界中', 'せかいじゅう')}で{r('使', 'つか')}われている",
       f"この{HOUHOU}は{r('世界中', 'せかいじゅう')}によって{r('使', 'つか')}われている",
       f"この{HOUHOU}は{r('世界中', 'せかいじゅう')}による{r('使', 'つか')}われている",
       f"この{HOUHOU}は{r('世界中', 'せかいじゅう')}で{r('使', 'つか')}うられている"],
      f"この{HOUHOU}は{r('世界中', 'せかいじゅう')}で{r('使', 'つか')}われている",
      f"<p><strong>{r('世界中', 'せかいじゅう')}で{r('使', 'つか')}"
      f"われている</strong>. Kim qoʻllashi aytilmagan va kerak "
      f"ham emas — bu yozma yapon tilining odatiy ovozi. "
      f"{r('世界中', 'せかいじゅう')} joy, bajaruvchi emas.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>Passivda qachon によって, qachon oddiy に turadi?</p>",
      ["Yaratish feʼllarida によって, odam aziyat chekkanda に",
       "Yaratish feʼllarida に, odam aziyat chekkanda によって",
       "Yozma matnda に, suhbatda によって",
       "Ikkalasi ham har doim oʻrin almashtira oladi"],
      "Yaratish feʼllarida によって, odam aziyat chekkanda に",
      f"<p><strong>Yaratish → によって, aziyat → に.</strong> "
      f"{r('作', 'つく')}る, {KAKU}, {r('建', 'た')}てる, "
      f"{r('発見', 'はっけん')}する — dunyoda yangi narsa paydo "
      f"qilgan feʼllar によって ni oladi. {SENSEI_NI} esa "
      f"oddiy に.</p>"),

    q("<p>Ot oldida によって qanday oʻzgaradi?</p>",
      ["による", "によっての", "によっては", "Oʻzgarmaydi"],
      "による",
      f"<p><strong>による</strong>: {TAIFUU_NIYORU}, "
      f"{JISHIN}による{HIGAI}. Bu {r('因', 'よ')}る feʼlining "
      f"lugʻat shakli — u otni aniqlab turibdi, xuddi PJ-48 "
      f"dagi aniqlovchi ergash gapdek.</p>"),

    q(f"<p>{KUNI}によって{ASAGOHAN}が{CHIGAU} — bu gap nimani "
      f"aytyapti?</p>",
      ["Mamlakatga qarab nonushta har xil boʻladi",
       "Nonushta mamlakatlar tomonidan tayyorlanadi",
       "Mamlakat tufayli nonushta buzildi",
       "Nonushta mamlakat orqali tarqaldi"],
      "Mamlakatga qarab nonushta har xil boʻladi",
      f"<p><strong>Mamlakatga qarab har xil.</strong> Bu yerda "
      f"によって na sabab, na bajaruvchi — u faqat nimaga qarab "
      f"farq borligini koʻrsatadi. {CHIGAU} feʼli buni darrov "
      f"aytib beradi.</p>"),

    q("<p>Yozma yapon tilida passiv nega shunchalik koʻp?</p>",
      ["Bajaruvchi muhim emas, mavzu oʻzgarmaydi va matn xolis boʻladi",
       "Passiv gap qisqaroq boʻlgani uchun",
       "Faol gap yaponchada grammatik jihatdan notoʻgʻri boʻlgani uchun",
       "Passiv faqat oʻtgan zamonda ishlagani uchun"],
      "Bajaruvchi muhim emas, mavzu oʻzgarmaydi va matn xolis boʻladi",
      f"<p>Uchta sabab: kim qilgani koʻpincha ahamiyatsiz; xat "
      f"boshining mavzusi は bilan boshda qoladi; va ilmiy matn "
      f"«{r('私', 'わたし')}は…と{OMOU}» emas, "
      f"{KANGAERARETEIRU} deb yozadi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [SENSEI_NIYOTTE,
       SENSEI_NI,
       f"{NATSUME}によって{KAKARETA}",
       TAIFUU_NIYORU],
      SENSEI_NIYOTTE,
      f"<p>Xato <strong>{SENSEI_NIYOTTE}</strong> da: odam aziyat "
      f"chekkan passivda oddiy <strong>に</strong> turadi. "
      f"Toʻgʻrisi — <strong>{SENSEI_NI}</strong>. によって esa "
      f"yaratish feʼllari uchun.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [TAIFUU_NIYORU,
       TAIFUU_NIYOTTE,
       f"{TAIFUU}によっての{HIGAI}",
       f"{TAIFUU}のによって{HIGAI}"],
      TAIFUU_NIYORU,
      f"<p><strong>{TAIFUU_NIYORU}</strong>. Ot oldida faqat "
      f"<strong>による</strong> turadi. によって otni aniqlay "
      f"olmaydi, va によって otga yalangʻoch ulangani uchun "
      f"oldiga の ham qoʻyilmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>この"
      f"{r('橋', 'はし')} / は / {r('一人', 'ひとり')}の"
      f"{r('技師', 'ぎし')} / によって / {TSUKURARETA}</strong></p>",
      [f"この{r('橋', 'はし')}は{r('一人', 'ひとり')}の{r('技師', 'ぎし')}"
       f"によって{TSUKURARETA}",
       f"{r('一人', 'ひとり')}の{r('技師', 'ぎし')}はこの{r('橋', 'はし')}"
       f"によって{TSUKURARETA}",
       f"この{r('橋', 'はし')}によって{r('一人', 'ひとり')}の"
       f"{r('技師', 'ぎし')}は{TSUKURARETA}",
       f"によってこの{r('橋', 'はし')}は{r('一人', 'ひとり')}の"
       f"{r('技師', 'ぎし')}{TSUKURARETA}"],
      f"この{r('橋', 'はし')}は{r('一人', 'ひとり')}の{r('技師', 'ぎし')}"
      f"によって{TSUKURARETA}",
      f"<p><strong>この{r('橋', 'はし')}は…によって{TSUKURARETA}"
      f"</strong>. Passiv gapda taʼsir koʻrgan narsa は bilan "
      f"boshda, bajaruvchi によって bilan oʻrtada, kesim esa "
      f"oxirida turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ: この{r('図書館', 'としょかん')}"
      f"は{r('毎日', 'まいにち')}{r('同', 'おな')}じ{JIKAN}に"
      f"{r('開', 'ひら')}きますか。</strong></p>"
      f"<p><strong>パリ: ___</strong></p>",
      [f"いいえ、{YOUBI}のによって{CHIGAU}そうです。",
       f"いいえ、{YOUBI}によって{CHIGAU}そうです。",
       f"いいえ、{YOUBI}による{CHIGAU}そうです。",
       f"いいえ、{YOUBI}によって{TSUKURARETA}そうです。"],
      f"いいえ、{YOUBI}によって{CHIGAU}そうです。",
      f"<p><strong>{YOUBI}によって{CHIGAU}</strong> — «kunga qarab "
      f"farq qiladi». Eshitilgan xabar PJ-74 dagi そうです bilan "
      f"berilgan. による bu yerga tushmaydi, chunki keyin ot "
      f"emas, feʼl keladi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-85 Mashq: 〜うちに va 〜あいだに",
        "tutorial":    "PJ-85:",
        "description": "Ikki xil vaqt oynasi — va に bor-yoʻqligi "
                       "maʼnoni qanday oʻzgartirishi.",
        "questions":   Q_PJ85,
        **DEFAULTS,
    },
    {
        "title":       "PJ-86 Mashq: 〜につれて va 〜にしたがって",
        "tutorial":    "PJ-86:",
        "description": "«…gan sari» — birga oʻzgarish, va にしたがって "
                       "ning ikkinchi ishi: «…ga muvofiq».",
        "questions":   Q_PJ86,
        **DEFAULTS,
    },
    {
        "title":       "PJ-87 Mashq: 〜によって va yozma passiv",
        "tutorial":    "PJ-87:",
        "description": "Bitta qolip, toʻrtta vazifa — va passivda "
                       "に bilan によって orasidagi chegara.",
        "questions":   Q_PJ87,
        **DEFAULTS,
    },
]
