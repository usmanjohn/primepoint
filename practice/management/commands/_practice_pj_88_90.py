# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-88 … PJ-90.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi:
    1. OʻZBEKCHA «UCHUN» (PJ-88). として (rol), にとって (baho
       nuqtasi) va PJ-56 dagi ために (manfaat) — uchalasi ham
       oʻzbekchada «uchun» yoki «sifatida» boʻlib chiqadi.
       Tanlovni gapning OXIRI hal qiladi: baho kelsa にとって,
       harakat kelsa ために.
    2. MAVZU YOKI NISHON (PJ-89). について — nima haqida;
       に対して — kimga qaratilgan. Va ot oldida uchtasi uch xil
       shaklga oʻtadi: についての, に関する, に対する.
    3. BITTA HARF (PJ-90). ながら «bir vaqtda», ながらも «…ga
       qaramay». つつ — ikkalasining kitobiy egizagi, つつある esa
       butunlay boshqa narsa: jarayon.

⚠️ CUMULATIVE: PJ-88 mashqida について oilasi (89) va ながらも・つつ
(90) yoʻq. PJ-89 da ながらも・つつ hali yoʻq.
`verify_pj_practice_88_90.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_88_90.py --master=prime \\
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
WATASHI  = r("私", "わたし")
KAZOKU   = r("家族", "かぞく")
KODOMO   = r("子供", "こども")
OYA      = r("親", "おや")
SEKININ  = r("責任", "せきにん")
TSUUYAKU = r("通訳", "つうやく")
KAIGI    = r("会議", "かいぎ")
SOUKO    = r("倉庫", "そうこ")
HEYA     = r("部屋", "へや")
ISHA     = r("医者", "いしゃ")
AN       = r("案", "あん")
SANSEI   = r("賛成", "さんせい")
SHIAWASE = r("幸", "しあわ") + "せ"
HON      = r("本", "ほん")
SENSEI   = r("先生", "せんせい")
BUNKA    = r("文化", "ぶんか")
NIHON    = r("日本", "にほん")
TAIDO    = r("態度", "たいど")
KANKYOU  = r("環境", "かんきょう")
HOURITSU = r("法律", "ほうりつ")
SHITSUMON = r("質問", "しつもん")
KEN      = r("件", "けん")
CHOUSA   = r("調査", "ちょうさ")
ANI      = r("兄", "あに")
OTOUTO   = r("弟", "おとうと")
SHITSUREI = r("失礼", "しつれい")
ONGAKU   = r("音楽", "おんがく")
WAGAYA   = r("我", "わ") + "が" + r("家", "や")
HONYA    = r("本屋", "ほんや")
YUKI     = r("雪", "ゆき")
SHIAI    = r("試合", "しあい")
MACHI    = r("町", "まち")

# ── sifatlar ─────────────────────────────────────────────────────────
TAISETSU = r("大切", "たいせつ")
MUZUKASHII = r("難", "むずか") + "しい"
SEMAI    = r("狭", "せま") + "い"
TANOSHII = r("楽", "たの") + "しい"
SHIZUKA  = r("静", "しず") + "か"
WARUI    = r("悪", "わる") + "い"
YUUMEI   = r("有名", "ゆうめい")

# ── feʼllar ──────────────────────────────────────────────────────────
HATARAKU  = r("働", "はたら") + "く"
DERU      = r("出", "で") + "る"
DEMASHITA = r("出", "で") + "ました"
KAU       = r("買", "か") + "う"
KAIMASHITA = r("買", "か") + "いました"
TSUKAU    = r("使", "つか") + "う"
TSUKAWARETEIRU = r("使", "つか") + "われている"
HANASU    = r("話", "はな") + "す"
HAPPYOU   = r("発表", "はっぴょう")
KOTAERU   = r("答", "こた") + "える"
KOTAETA   = r("答", "こた") + "えた"
OKONAU    = r("行", "おこな") + "う"
KAWARU    = r("変", "か") + "わる"
SHABERU   = "しゃべる"
ARUKU     = r("歩", "ある") + "く"
ARUKI     = r("歩", "ある") + "き"
KANGAERU  = r("考", "かんが") + "える"
SHITTEIRU = r("知", "し") + "っている"
SHITTEI   = r("知", "し") + "ってい"
SHIRI     = r("知", "し") + "り"
SHIRANAKATTA = r("知", "し") + "らなかった"
OSHIERU   = r("教", "おし") + "える"
KURENAKATTA = "くれなかった"
HERU      = r("減", "へ") + "る"
HERI      = r("減", "へ") + "り"
KIERU     = r("消", "き") + "える"
KIE       = r("消", "き") + "え"
FURU      = r("降", "ふ") + "る"
FURI      = r("降", "ふ") + "り"
TSUZUITA  = r("続", "つづ") + "いた"
BENKYOU   = r("勉強", "べんきょう")
KIKU      = r("聞", "き") + "く"
KIKI      = r("聞", "き") + "き"

# ── tayyor qoliplar ──────────────────────────────────────────────────
OYA_TOSHITE_NO = OYA + "としての" + SEKININ
OYA_TOSHITE    = OYA + "として" + SEKININ
WATASHI_NITOTTE = WATASHI + "にとって"
WATASHI_NO_NITOTTE = WATASHI + "のにとって"
KODOMO_NO_TAMENI = KODOMO + "のために" + HON + "を" + KAIMASHITA
KODOMO_NITOTTE_KAU = KODOMO + "にとって" + HON + "を" + KAIMASHITA
KANKYOU_NI_KANSURU = KANKYOU + "に" + r("関", "かん") + "する" + HOURITSU
KANKYOU_NI_KANSHITE = KANKYOU + "に" + r("関", "かん") + "して" + HOURITSU
KANKYOU_NITSUITE_NO = KANKYOU + "についての" + HON
KANKYOU_NITSUITE = KANKYOU + "について" + HON
SENSEI_NITAISHITE = SENSEI + "に" + r("対", "たい") + "して"
SENSEI_NITSUITE = SENSEI + "について"
ARUKI_TSUTSU = ARUKI + "つつ" + KANGAERU
ARUKU_TSUTSU = ARUKU + "つつ" + KANGAERU
SEMAI_NAGARAMO = SEMAI + "ながらも"
SEMAI_TSUTSUMO = SEMAI + "つつも"
HERI_TSUTSUARU = HERI + "つつある"
HERU_TSUTSUARU = HERU + "つつある"


# ══════════════════════════════════════════════════════════════════════
# PJ-88 — 〜として va 〜にとって
# ══════════════════════════════════════════════════════════════════════
Q_PJ88 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜として nimani koʻrsatadi?</p>",
      ["Rolni, maqomni — «… sifatida»",
       "Baho beriladigan nuqtani — «… nazdida»",
       "Manfaatni — «… foydasiga»",
       "Sababni — «… tufayli»"],
      "Rolni, maqomni — «… sifatida»",
      f"<p><strong>Rol.</strong> {TSUUYAKU}として{HATARAKU} — "
      f"«tarjimon sifatida ishlaydi». Oʻzbekcha «sifatida» "
      f"qayerda tursa, として ham oʻsha yerda.</p>"),

    q("<p>〜にとって nimani koʻrsatadi?</p>",
      ["Baho beriladigan nuqtani — «… nazdida»",
       "Rolni — «… sifatida»",
       "Vositani — «… orqali»",
       "Vaqtni — «… paytida»"],
      "Baho beriladigan nuqtani — «… nazdida»",
      f"<p><strong>Baho nuqtasi</strong>: {WATASHI_NITOTTE}"
      f"{KAZOKU}がいちばん{TAISETSU}です. Kimning koʻzida muhim? "
      f"Meniki. Shuning uchun undan keyin deyarli doim baho "
      f"beruvchi soʻz keladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>ラノさんは{TSUUYAKU}"
      f"___{KAIGI}に{DEMASHITA}。</strong></p>",
      ["として", "にとって", "のために", "のように"],
      "として",
      f"<p><strong>{TSUUYAKU}として</strong> — «tarjimon "
      f"sifatida». Rano yigʻilishga tomoshabin sifatida emas, "
      f"aynan shu vazifada keldi. のように qoʻyilsa, u tarjimon "
      f"emas, faqat tarjimonga oʻxshaydi degan boshqa maʼno "
      f"chiqardi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WATASHI}___"
      f"{KAZOKU}がいちばん{TAISETSU}です。</strong></p>",
      ["にとって", "として", "のために", "によって"],
      "にとって",
      f"<p><strong>{WATASHI_NITOTTE}</strong>. Gapning oxirida "
      f"baho beruvchi soʻz ({TAISETSU}だ) turibdi — demak baho "
      f"nuqtasi kerak. のために qoʻyilsa, keyin harakat kelishi "
      f"kerak boʻlardi.</p>"),

    q("<p>として va にとって otga qanday ulanadi?</p>",
      ["Yalangʻoch — の ham, だ ham olmaydi",
       "Otdan keyin の qoʻshiladi",
       "Otdan keyin だ qoʻshiladi",
       "Otdan keyin な qoʻshiladi"],
      "Yalangʻoch — の ham, だ ham olmaydi",
      f"<p><strong>Yalangʻoch</strong>: {WATASHI_NITOTTE}, "
      f"{TSUUYAKU}として. Bu ularni PJ-56 dagi ために dan "
      f"ajratadi — ために esa otdan keyin <strong>の</strong> "
      f"talab qiladi: {WATASHI}のために.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>«Ota-ona sifatidagi masʼuliyat» — qaysi gap toʻgʻri?</p>",
      [OYA_TOSHITE_NO, OYA_TOSHITE,
       OYA + "にとっての" + SEKININ,
       OYA + "のための" + SEKININ],
      OYA_TOSHITE_NO,
      f"<p><strong>{OYA_TOSHITE_NO}</strong>. Ot oldida として "
      f"ga <strong>の</strong> qoʻshiladi. «Ota-ona nazdidagi» "
      f"yoki «ota-ona uchun» degan gap boshqa maʼno berardi.</p>"),

    q(f"<p>«Bola uchun kitob sotib oldim» — qaysi gap toʻgʻri?</p>",
      [KODOMO_NO_TAMENI, KODOMO_NITOTTE_KAU,
       KODOMO + "として" + HON + "を" + KAIMASHITA,
       KODOMO + "にとっての" + HON + "を" + KAIMASHITA],
      KODOMO_NO_TAMENI,
      f"<p><strong>{KODOMO_NO_TAMENI}</strong>. Keyin harakat "
      f"({KAU}) kelyapti, demak manfaat — ために. にとって esa "
      f"faqat baho beruvchi soʻz bilan yuradi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KODOMO}___"
      f"{MUZUKASHII}{HON}です。</strong></p>",
      ["にとって", "のために", "として", "のように"],
      "にとって",
      f"<p><strong>{KODOMO}にとって</strong> — qiyinlik "
      f"bolaning koʻzida. Bir xil ot, bir xil oʻzbekcha «uchun», "
      f"lekin bu safar gapning oxirida baho ({MUZUKASHII}) "
      f"turibdi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>この{HEYA}は"
      f"{SOUKO}___{TSUKAWARETEIRU}。</strong></p>",
      ["として", "にとって", "のために", "によって"],
      "として",
      f"<p><strong>{SOUKO}として</strong> — «ombor sifatida». "
      f"として odamga ham, narsaga ham ulanadi; muhimi "
      f"<em>vazifa</em> nomlanishi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WATASHI}___は"
      f"この{AN}に{SANSEI}です。</strong> («men esa bu taklifni "
      f"maʼqullayman»)</p>",
      ["として", "にとって", "のため", "のよう"],
      "として",
      f"<p><strong>{WATASHI}としては</strong> — «mening "
      f"nazarimda esa». は qoʻshilishi fikrni boshqalarnikidan "
      f"ajratib koʻrsatadi. Bu として ning qardosh "
      f"shakli.</p>"),

    q(f"<p>«Shifokordek gapiradi» — u shifokor emas. Qaysi gap "
      f"toʻgʻri?</p>",
      [f"{ISHA}のように{HANASU}",
       f"{ISHA}として{HANASU}",
       f"{ISHA}にとって{HANASU}",
       f"{ISHA}のために{HANASU}"],
      f"{ISHA}のように{HANASU}",
      f"<p><strong>{ISHA}のように{HANASU}</strong> — bu "
      f"oʻxshatish (PJ-56). として qoʻyilsa, gap «u rostdan "
      f"ham shifokor va shu maqomda gapiryapti» degan "
      f"teskari maʼnoni berardi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WATASHI}___の"
      f"{SHIAWASE}は、{KAZOKU}といっしょにいることです。</strong></p>",
      ["にとって", "として", "のため", "のよう"],
      "にとって",
      f"<p><strong>{WATASHI}にとっての{SHIAWASE}</strong> — "
      f"«mening nazdimdagi baxt». Ot oldida にとって ham "
      f"<strong>の</strong> oladi, xuddi として dek.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>にとって dan keyin nima keladi?</p>",
      [f"Baho beruvchi soʻz — {TAISETSU}だ, {MUZUKASHII}, "
       f"{r('必要', 'ひつよう')}だ",
       f"Harakat — {KAU}, {HATARAKU}, {r('作', 'つく')}る",
       "Vaqt soʻzi",
       "Faqat inkor"],
      f"Baho beruvchi soʻz — {TAISETSU}だ, {MUZUKASHII}, "
      f"{r('必要', 'ひつよう')}だ",
      f"<p><strong>Baho beruvchi soʻz.</strong> Harakat kelsa, "
      f"qolip ために ga oʻzgaradi: {KODOMO_NO_TAMENI}. Bu "
      f"ikkovini ajratishning eng ishonchli yoʻli — gapning "
      f"oxiriga qarash.</p>"),

    q("<p>Qaysi qolip otdan keyin の talab qiladi?</p>",
      ["〜のために", "〜にとって", "〜として", "Uchalasi ham"],
      "〜のために",
      f"<p><strong>〜のために</strong>: {WATASHI}のために. "
      f"にとって va として esa yalangʻoch ulanadi. の "
      f"bor-yoʻqligi — bu uchtasini ajratishning eng arzon "
      f"belgisi.</p>"),

    q(f"<p>«Shifokor sifatida gapiradi» — u rostdan ham shifokor. "
      f"Qaysi gap toʻgʻri?</p>",
      [f"{ISHA}として{HANASU}",
       f"{ISHA}のように{HANASU}",
       f"{ISHA}にとって{HANASU}",
       f"{ISHA}みたいに{HANASU}"],
      f"{ISHA}として{HANASU}",
      f"<p><strong>{ISHA}として{HANASU}</strong>. Bitta savol "
      f"ikkovini ajratadi: «bu odam rostdan ham shumi?» Ha — "
      f"として; yoʻq — のように yoki みたいに.</p>"),

    q("<p>«Sifatida» deb qoʻysangiz gap turadigan qolip qaysi?</p>",
      ["〜として", "〜にとって", "〜のために", "〜によって"],
      "〜として",
      f"<p><strong>〜として</strong>. «Tarjimon sifatida», "
      f"«ombor sifatida», «ota-ona sifatida» — hammasi "
      f"toʻgʻri. «Bola sifatida qiyin» esa maʼnoni buzadi, "
      f"demak u yerda にとって kerak.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [WATASHI_NO_NITOTTE + TAISETSU + "です",
       WATASHI_NITOTTE + TAISETSU + "です",
       WATASHI + "のために" + KAU,
       OYA_TOSHITE_NO],
      WATASHI_NO_NITOTTE + TAISETSU + "です",
      f"<p>Xato <strong>{WATASHI_NO_NITOTTE}</strong> da: "
      f"にとって otga yalangʻoch ulanadi. の faqat ために ga "
      f"kerak. Toʻgʻrisi — <strong>{WATASHI_NITOTTE}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [OYA_TOSHITE_NO, OYA_TOSHITE,
       OYA + "だとしての" + SEKININ,
       OYA + "のとしての" + SEKININ],
      OYA_TOSHITE_NO,
      f"<p><strong>{OYA_TOSHITE_NO}</strong>. Ot oldida として "
      f"ga <strong>の</strong> qoʻshiladi, lekin として ning "
      f"oʻzi otga yalangʻoch ulanadi — だ ham, の ham "
      f"undan oldin turmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{WATASHI} / "
      f"にとって / {KAZOKU}が / いちばん / {TAISETSU}です</strong></p>",
      [f"{WATASHI}にとって{KAZOKU}がいちばん{TAISETSU}です",
       f"{KAZOKU}が{WATASHI}いちばんにとって{TAISETSU}です",
       f"いちばん{WATASHI}にとって{KAZOKU}が{TAISETSU}です",
       f"{TAISETSU}です{WATASHI}にとって{KAZOKU}がいちばん"],
      f"{WATASHI}にとって{KAZOKU}がいちばん{TAISETSU}です",
      f"<p><strong>{WATASHI}にとって{KAZOKU}がいちばん"
      f"{TAISETSU}です</strong>. Baho nuqtasi boshda, ega "
      f"keyin, baho esa oxirida — yapon gapida kesim doim "
      f"eng oxirgi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム: ラノさんはどうして"
      f"{KAIGI}に{DEMASHITA}か。</strong></p>"
      f"<p><strong>ムニラ: ___</strong></p>",
      [f"{TSUUYAKU}として{DEMASHITA}。",
       f"{TSUUYAKU}にとって{DEMASHITA}。",
       f"{TSUUYAKU}のために{DEMASHITA}。",
       f"{TSUUYAKU}のように{DEMASHITA}。"],
      f"{TSUUYAKU}として{DEMASHITA}。",
      f"<p><strong>{TSUUYAKU}として</strong> — «tarjimon "
      f"sifatida». Savol uning <em>rolini</em> soʻrayapti, "
      f"shuning uchun javob ham rol bilan beriladi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-89 — 〜に関して, 〜について, 〜に対して
# ══════════════════════════════════════════════════════════════════════
KANSHITE  = "に" + r("関", "かん") + "して"
KANSURU   = "に" + r("関", "かん") + "する"
TAISHITE  = "に" + r("対", "たい") + "して"
TAISURU   = "に" + r("対", "たい") + "する"

Q_PJ89 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜について nimani koʻrsatadi?</p>",
      ["Gapning mavzusini — «… haqida»",
       "Munosabat qaratilgan tomonni — «… ga nisbatan»",
       "Rolni — «… sifatida»",
       "Sababni — «… tufayli»"],
      "Gapning mavzusini — «… haqida»",
      f"<p><strong>Mavzu.</strong> {NIHON}の{BUNKA}について"
      f"{HAPPYOU}する — «madaniyat haqida taqdimot qilmoq». "
      f"Oʻzbekcha «haqida» qayerda tursa, について ham oʻsha "
      f"yerda.</p>"),

    q(f"<p>〜{TAISHITE} nimani koʻrsatadi?</p>",
      ["Munosabat yoki harakat qaratilgan tomonni",
       "Gapning mavzusini",
       "Ish bajarilgan vaqtni",
       "Ishning natijasini"],
      "Munosabat yoki harakat qaratilgan tomonni",
      f"<p><strong>Nishon.</strong> {SENSEI_NITAISHITE}"
      f"{SHITSUREI}だ — «ustozga nisbatan qoʻpol». Ustoz bu "
      f"yerda suhbatning mavzusi emas, munosabat yoʻnalgan "
      f"odam.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NIHON}の{BUNKA}___"
      f"{HAPPYOU}しました。</strong></p>",
      ["について", f"{TAISHITE}", "として", "にとって"],
      "について",
      f"<p><strong>{BUNKA}について</strong>. Madaniyat — "
      f"taqdimotning mavzusi. Oʻzbekchada «haqida» chiqdi, "
      f"demak について.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SENSEI}___そんな"
      f"{TAIDO}をとってはいけない。</strong></p>",
      [f"{TAISHITE}", "について", f"{KANSHITE}", "にとって"],
      f"{TAISHITE}",
      f"<p><strong>{SENSEI_NITAISHITE}</strong>. Munosabat "
      f"ustozga <em>qaratilgan</em>. Oʻzbekchada «-ga» paydo "
      f"boʻldi — bu nishon belgisi. について esa faqat mavzuni "
      f"nomlaydi.</p>"),

    q(f"<p>〜{KANSHITE} ning について dan farqi nimada?</p>",
      ["Maʼnosi bir xil, lekin ohangi rasmiyroq",
       "Maʼnosi butunlay boshqa",
       f"{KANSHITE} faqat odam bilan ishlatiladi",
       f"{KANSHITE} faqat suhbatda ishlatiladi"],
      "Maʼnosi bir xil, lekin ohangi rasmiyroq",
      f"<p><strong>Ohang.</strong> {KANSHITE} — rasmiy hujjat, "
      f"ilmiy maqola va yangilik tili: この{KEN}{KANSHITE}"
      f"{CHOUSA}を{OKONAU}. Kundalik suhbatda u gʻalati "
      f"rasmiy eshitiladi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>«Atrof-muhitga oid qonun» — qaysi gap toʻgʻri?</p>",
      [KANKYOU_NI_KANSURU, KANKYOU_NI_KANSHITE,
       KANKYOU + "について" + HOURITSU,
       KANKYOU + TAISHITE + HOURITSU],
      KANKYOU_NI_KANSURU,
      f"<p><strong>{KANKYOU_NI_KANSURU}</strong>. Ot oldida "
      f"{KANSHITE} lugʻat shakliga qaytadi — chunki u "
      f"{r('関', 'かん')}する degan feʼldan kelgan.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KANKYOU}について"
      f"___{HON}</strong></p>",
      ["の", "する", "な", "hech nima"],
      "の",
      f"<p><strong>{KANKYOU_NITSUITE_NO}</strong>. について "
      f"feʼldan kelmagan, shuning uchun otni aniqlashda "
      f"oddiygina <strong>の</strong> qoʻshiladi — する emas.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHITSUMON}___"
      f"{r('丁寧', 'ていねい')}に{KOTAETA}。</strong></p>",
      [f"{TAISHITE}", "について", f"{KANSHITE}", "として"],
      f"{TAISHITE}",
      f"<p><strong>{SHITSUMON}{TAISHITE}</strong> — «savolga "
      f"javoban». Javob savolga <em>qaratilgan</em>, shuning "
      f"uchun nishon qolipi kerak.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ANI}は{SHIZUKA}___"
      f"のに{r('対', 'たい')}して、{OTOUTO}はよく{SHABERU}。</strong></p>",
      ["な", "だ", "の", "hech nima"],
      "な",
      f"<p><strong>{SHIZUKA}なのに{r('対', 'たい')}して</strong>. "
      f"Qarshi qoʻyish maʼnosida な-sifat va ot <strong>な + "
      f"の</strong> oladi. Feʼl va い-sifat esa oddiy shaklga "
      f"の qoʻshadi.</p>"),

    q(f"<p>«Bolaga boʻlgan munosabat» — qaysi gap toʻgʻri?</p>",
      [KODOMO + TAISURU + TAIDO,
       KODOMO + TAISHITE + TAIDO,
       KODOMO + "についての" + TAIDO,
       KODOMO + KANSURU + TAIDO],
      KODOMO + TAISURU + TAIDO,
      f"<p><strong>{KODOMO}{TAISURU}{TAIDO}</strong>. Ot "
      f"oldida {TAISHITE} ham lugʻat shakliga qaytadi, xuddi "
      f"{KANSHITE} dek — ikkalasi ham feʼldan kelgan.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>この{KEN}___"
      f"{CHOUSA}を{OKONAU}。</strong> (rasmiy eʼlon)</p>",
      [f"{KANSHITE}", "にとって", "として", "のために"],
      f"{KANSHITE}",
      f"<p><strong>この{KEN}{KANSHITE}</strong> — «ushbu "
      f"masala yuzasidan». について ham toʻgʻri boʻlardi, "
      f"lekin rasmiy eʼlonda {KANSHITE} tabiiyroq.</p>"),

    q("<p>について otga qanday ulanadi?</p>",
      ["Yalangʻoch", "Otdan keyin の qoʻshiladi",
       "Otdan keyin な qoʻshiladi", "Otdan keyin だ qoʻshiladi"],
      "Yalangʻoch",
      f"<p><strong>Yalangʻoch</strong>: {BUNKA}について. "
      f"«{BUNKA}のについて» notoʻgʻri. の faqat <em>otni "
      f"aniqlaganda</em> va qolipdan <em>keyin</em> "
      f"qoʻshiladi: {KANKYOU_NITSUITE_NO}.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>«Ustoz haqida gapirdik» — qaysi gap toʻgʻri?</p>",
      [SENSEI_NITSUITE + HANASU[:-1] + "しました",
       SENSEI_NITAISHITE + HANASU[:-1] + "しました",
       SENSEI + "として" + HANASU[:-1] + "しました",
       SENSEI + "にとって" + HANASU[:-1] + "しました"],
      SENSEI_NITSUITE + HANASU[:-1] + "しました",
      f"<p><strong>{SENSEI_NITSUITE}</strong>. Ustoz — "
      f"suhbatning mavzusi, va u xonada boʻlmasligi ham "
      f"mumkin. {TAISHITE} qoʻyilsa, gap «ustozga qarab "
      f"gapirdik» degan boshqa maʼnoga oʻtadi.</p>"),

    q("<p>Kundalik suhbatda qaysi biri tabiiyroq?</p>",
      ["〜について", f"〜{KANSHITE}", f"〜{TAISURU}", "〜としての"],
      "〜について",
      f"<p><strong>〜について</strong>. Sinfda ham, xatda ham, "
      f"suhbatda ham tabiiy. {KANSHITE} esa hujjat tili — "
      f"doʻstingizga aytsangiz, ariza yozgandek eshitiladi. "
      f"Shubhalansangiz について ni tanlang.</p>"),

    q(f"<p>«Akam tinch, ukam esa koʻp gapiradi» — qaysi qolip?</p>",
      [f"{ANI}は{SHIZUKA}なのに{r('対', 'たい')}して",
       f"{ANI}は{SHIZUKA}について",
       f"{ANI}は{SHIZUKA}{KANSHITE}",
       f"{ANI}は{SHIZUKA}として"],
      f"{ANI}は{SHIZUKA}なのに{r('対', 'たい')}して",
      f"<p><strong>なのに{r('対', 'たい')}して</strong> — bu "
      f"{TAISHITE} ning ikkinchi ishi: ikki narsani qarshi "
      f"qoʻyish. Yozma matnda juda koʻp uchraydi.</p>"),

    q("<p>Ot oldida uchtasi qanday shaklga oʻtadi?</p>",
      [f"についての · {KANSURU} · {TAISURU}",
       f"についての · {KANSHITE}の · {TAISHITE}の",
       f"についてする · {KANSURU} · {TAISURU}",
       f"についての · {KANSURU}の · {TAISURU}の"],
      f"についての · {KANSURU} · {TAISURU}",
      f"<p>Ikkitasi <strong>する</strong>, bittasi "
      f"<strong>の</strong>. {KANSHITE} va {TAISHITE} feʼldan "
      f"kelgani uchun lugʻat shakliga qaytadi; について esa "
      f"feʼl emas, shuning uchun oddiygina の oladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [KANKYOU_NI_KANSHITE,
       KANKYOU_NI_KANSURU,
       KANKYOU_NITSUITE_NO,
       KODOMO + TAISURU + TAIDO],
      KANKYOU_NI_KANSHITE,
      f"<p>Xato <strong>{KANKYOU_NI_KANSHITE}</strong> da: ot "
      f"oldida {KANSHITE} emas, <strong>{KANSURU}</strong> "
      f"turishi kerak. Toʻgʻrisi — "
      f"<strong>{KANKYOU_NI_KANSURU}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [KANKYOU_NITSUITE_NO,
       KANKYOU_NITSUITE,
       KANKYOU + "についてする" + HON,
       KANKYOU + "のについての" + HON],
      KANKYOU_NITSUITE_NO,
      f"<p><strong>{KANKYOU_NITSUITE_NO}</strong>. について "
      f"otga yalangʻoch ulanadi, lekin otni aniqlaganda "
      f"oxiriga <strong>の</strong> qoʻshiladi. する esa faqat "
      f"{KANSHITE} va {TAISHITE} da.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{SHITSUMON} / "
      f"{TAISHITE} / {r('丁寧', 'ていねい')}に / {KOTAETA}</strong></p>",
      [f"{SHITSUMON}{TAISHITE}{r('丁寧', 'ていねい')}に{KOTAETA}",
       f"{r('丁寧', 'ていねい')}に{SHITSUMON}{KOTAETA}{TAISHITE}",
       f"{TAISHITE}{SHITSUMON}{r('丁寧', 'ていねい')}に{KOTAETA}",
       f"{KOTAETA}{SHITSUMON}{TAISHITE}{r('丁寧', 'ていねい')}に"],
      f"{SHITSUMON}{TAISHITE}{r('丁寧', 'ていねい')}に{KOTAETA}",
      f"<p><strong>{SHITSUMON}{TAISHITE}{r('丁寧', 'ていねい')}に"
      f"{KOTAETA}</strong>. Nishon boshda, hol oʻrtada, kesim "
      f"oxirida. {TAISHITE} otdan <em>keyin</em> turadi, "
      f"hech qachon undan oldin emas.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>パリ: きのうの{KAIGI}では"
      f"{r('何', 'なに')}を{HANASU[:-1]}しましたか。</strong></p>"
      f"<p><strong>イムロン: ___</strong></p>",
      [f"{NIHON}の{BUNKA}について{HANASU[:-1]}しました。",
       f"{NIHON}の{BUNKA}{TAISHITE}{HANASU[:-1]}しました。",
       f"{NIHON}の{BUNKA}として{HANASU[:-1]}しました。",
       f"{NIHON}の{BUNKA}のについて{HANASU[:-1]}しました。"],
      f"{NIHON}の{BUNKA}について{HANASU[:-1]}しました。",
      f"<p><strong>{BUNKA}について</strong> — savol «nima "
      f"haqida gapirdingiz» deb soʻrayapti, demak javob ham "
      f"mavzu qolipi bilan beriladi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-90 — 〜ながらも va 〜つつ
# ══════════════════════════════════════════════════════════════════════
Q_PJ90 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜ながらも nimani bildiradi?</p>",
      ["… ga qaramay, … boʻlsa-da",
       "Ikki ish bir vaqtda",
       "Ish endigina tugadi",
       "Ish qoidaga muvofiq bajarildi"],
      "… ga qaramay, … boʻlsa-da",
      f"<p><strong>Qarama-qarshilik.</strong> {SHITTEI}ながらも、"
      f"{OSHIERU[:-1]}て{KURENAKATTA} — «bilgani holda ham "
      f"aytmadi». PJ-38 dagi ながら ga bitta も qoʻshildi, va "
      f"maʼno burildi.</p>"),

    q("<p>ながら va ながらも orasidagi farq nimada?</p>",
      ["も qarshilik maʼnosini taʼkidlaydi",
       "も gapni oʻtgan zamonga oʻtkazadi",
       "も gapni inkor qiladi",
       "Farq yoʻq, ikkalasi bir xil"],
      "も qarshilik maʼnosini taʼkidlaydi",
      f"<p><strong>も qarshilikni taʼkidlaydi.</strong> も siz "
      f"ham gap qarshilikni bildirishi mumkin, lekin も bilan "
      f"bu <em>albatta</em> qarshilik. «Bir vaqtda» maʼnosiga "
      f"esa も hech qachon qoʻshilmaydi.</p>"),

    q(f"<p>{ARUKU} feʼlini つつ bilan qoʻshing.</p>",
      [ARUKI + "つつ", ARUKU + "つつ",
       r("歩", "ある") + "きますつつ", r("歩", "ある") + "いてつつ"],
      ARUKI + "つつ",
      f"<p><strong>{ARUKI}つつ</strong>. ます-shakli "
      f"{r('歩', 'ある')}きます, oʻzagi {ARUKI} — oʻshanga つつ "
      f"ulanadi. Lugʻat shakli ham, て-shakli ham bu yerga "
      f"tushmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHITTEI}___、"
      f"{OSHIERU[:-1]}て{KURENAKATTA}。</strong></p>",
      ["ながらも", "つつある", "ながらの",
       "ますながら"],
      "ながらも",
      f"<p><strong>{SHITTEI}ながらも</strong>. Bilardi — demak "
      f"aytishi kerak edi, lekin aytmadi. Kutilgan natija "
      f"chiqmadi, va aynan shu ながらも ning ishi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SEMAI}___、"
      f"{TANOSHII}{WAGAYA}。</strong></p>",
      ["ながらも", "つつも", "つつある", "ますながらも"],
      "ながらも",
      f"<p><strong>{SEMAI_NAGARAMO}</strong> — «tor boʻlsa-da, "
      f"quvnoq uyimiz». Mashhur ibora. い-sifat ながらも ga "
      f"yalangʻoch ulanadi; つつ esa faqat feʼl bilan "
      f"keladi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q("<p>つつ qaysi shaklga ulanadi?</p>",
      ["ます-oʻzagiga", "Lugʻat shakliga", "て-shakliga",
       "た-shakliga"],
      "ます-oʻzagiga",
      f"<p><strong>ます-oʻzagiga</strong>: {ARUKI}つつ, "
      f"{SHIRI}つつ, {HERI}つつ. «{ARUKU_TSUTSU}» notoʻgʻri — "
      f"lugʻat shakli bu qolipni olmaydi.</p>"),

    q("<p>〜つつある nimani bildiradi?</p>",
      ["… boʻlib bormoqda — jarayon, tendensiya",
       "… ga qaramay — qarshilik",
       "… ekan — vaqt oynasi",
       "… sifatida — rol"],
      "… boʻlib bormoqda — jarayon, tendensiya",
      f"<p><strong>Jarayon.</strong> {MACHI}の{HONYA}は"
      f"{HERI_TSUTSUARU} — «kitob doʻkonlari kamayib bormoqda». "
      f"Bu つつも emas: つつある va つつも butunlay boshqa ikki "
      f"qolip.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HONYA}が"
      f"{r('減', 'へ')}___つつある。</strong></p>",
      ["り", "る", "って", "ります"],
      "り",
      f"<p><strong>{HERI_TSUTSUARU}</strong>. Bu yerda ham "
      f"ます-oʻzagi kerak: {r('減', 'へ')}ります → {HERI}. "
      f"«{HERU_TSUTSUARU}» notoʻgʻri.</p>"),

    q(f"<p>«{SEMAI}» bilan つつも ishlatsa boʻladimi?</p>",
      ["Yoʻq — つつ faqat feʼlga ulanadi",
       "Ha — つつ har qanday soʻzga ulanadi",
       "Ha, lekin faqat suhbatda",
       "Yoʻq — つつ faqat sifatga ulanadi"],
      "Yoʻq — つつ faqat feʼlga ulanadi",
      f"<p><strong>Yoʻq.</strong> «{SEMAI_TSUTSUMO}» degan gap "
      f"yaponchada yoʻq. Sifat va ot uchun <strong>ながらも</strong> "
      f"kerak: {SEMAI_NAGARAMO}. ながらも ikkalasiga ham "
      f"ulanadi, つつ esa faqat feʼlning oʻzagiga.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WARUI}と{SHIRI}___、"
      f"やってしまった。</strong></p>",
      ["つつも", "つつある", "ますつつ", "るつつ"],
      "つつも",
      f"<p><strong>{SHIRI}つつも</strong> — «bila turib ham». "
      f"つつも — ながらも ning kitobiy shakli. Oxiridagi "
      f"〜てしまった (PJ-58) afsusni qoʻshadi va bu qolip bilan "
      f"juda tez-tez keladi.</p>"),

    q("<p>ながら ikkala tomonda nimani talab qiladi?</p>",
      ["Bitta ega — ikkala ishni bir odam qiladi",
       "Ikki boshqa ega",
       "Faqat oʻtgan zamonni",
       "Faqat inkorni"],
      "Bitta ega — ikkala ishni bir odam qiladi",
      f"<p><strong>Bitta ega.</strong> «{ANI}は{SHITTEIRU}"
      f"ながら、{OTOUTO}は{SHIRANAKATTA}» notoʻgʻri — ikki "
      f"boshqa odam. Bunday paytda PJ-54 dagi <strong>が</strong> "
      f"kerak. Bu cheklov PJ-38 dan beri oʻzgarmagan.</p>"),

    q(f"<p>{YUKI}が{KIE}つつある — bu gap nimani aytyapti?</p>",
      ["Qor erib bormoqda",
       "Qor yogʻayotganiga qaramay",
       "Qor endigina eridi",
       "Qor erishi kerak"],
      "Qor erib bormoqda",
      f"<p><strong>Qor erib bormoqda.</strong> つつある — "
      f"jarayon, tendensiya. Qarshilik uchun つつ<strong>も</strong> "
      f"kerak boʻlardi: {YUKI}が{FURI}つつも、{SHIAI}は"
      f"{TSUZUITA}.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q("<p>Qaysi juftlik toʻgʻri?</p>",
      ["つつある — jarayon; つつも — qarshilik",
       "つつある — qarshilik; つつも — jarayon",
       "Ikkalasi ham qarshilik",
       "Ikkalasi ham jarayon"],
      "つつある — jarayon; つつも — qarshilik",
      f"<p><strong>つつある</strong> «boʻlib bormoqda» "
      f"({HERI_TSUTSUARU}), <strong>つつも</strong> esa «…ga "
      f"qaramay» ({SHIRI}つつも). Bitta soʻzdan yasalgan, "
      f"lekin ikki boshqa ish.</p>"),

    q(f"<p>«Musiqa tinglab oʻqiyman» — も qoʻshsa boʻladimi?</p>",
      ["Yoʻq — «bir vaqtda» maʼnosiga も qoʻshilmaydi",
       "Ha — も har doim qoʻshiladi",
       "Ha, lekin faqat yozma tilda",
       "Yoʻq — bu gapda ながら umuman ishlatilmaydi"],
      "Yoʻq — «bir vaqtda» maʼnosiga も qoʻshilmaydi",
      f"<p><strong>Yoʻq.</strong> {ONGAKU}を{KIKI}ながら"
      f"{BENKYOU}する — ikkala ish bir vaqtda ketyapti, hech "
      f"qanday gʻalatilik yoʻq. も qoʻyilsa, gap qarshilikni "
      f"daʼvo qilib qoladi.</p>"),

    q("<p>Yozma matnda ながら oʻrniga nima ishlatiladi?</p>",
      ["つつ", "ながらも", "つつある", "ばかり"],
      "つつ",
      f"<p><strong>つつ</strong> — ながら ning kitobiy egizagi: "
      f"{ARUKI_TSUTSU}. Maqola, esse va rasmiy nutqda yashaydi; "
      f"suhbatda uni eshitmaysiz.</p>"),

    q(f"<p>Qaysi qolip <strong>sifatga ham</strong> ulanadi?</p>",
      ["ながらも", "つつ", "つつも", "つつある"],
      "ながらも",
      f"<p><strong>ながらも</strong>: {SEMAI_NAGARAMO}, "
      f"{r('残念', 'ざんねん')}ながらも, {KODOMO}ながらも. "
      f"つつ oilasining hammasi esa faqat feʼlning "
      f"ます-oʻzagiga ulanadi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [ARUKU_TSUTSU, ARUKI_TSUTSU, SEMAI_NAGARAMO, HERI_TSUTSUARU],
      ARUKU_TSUTSU,
      f"<p>Xato <strong>{ARUKU_TSUTSU}</strong> da: つつ "
      f"ます-oʻzagiga ulanadi, lugʻat shakliga emas. Toʻgʻrisi "
      f"— <strong>{ARUKI_TSUTSU}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [SEMAI_NAGARAMO, SEMAI_TSUTSUMO,
       SEMAI + "つつある", SEMAI + "ますながらも"],
      SEMAI_NAGARAMO,
      f"<p><strong>{SEMAI_NAGARAMO}</strong>. つつ faqat "
      f"feʼl bilan keladi, shuning uchun sifatga つつも ham, "
      f"つつある ham ulanmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{SHITTEI} / "
      f"ながらも / {OSHIERU[:-1]}て / {KURENAKATTA}</strong></p>",
      [f"{SHITTEI}ながらも{OSHIERU[:-1]}て{KURENAKATTA}",
       f"ながらも{SHITTEI}{OSHIERU[:-1]}て{KURENAKATTA}",
       f"{OSHIERU[:-1]}て{KURENAKATTA}{SHITTEI}ながらも",
       f"{SHITTEI}{OSHIERU[:-1]}てながらも{KURENAKATTA}"],
      f"{SHITTEI}ながらも{OSHIERU[:-1]}て{KURENAKATTA}",
      f"<p><strong>{SHITTEI}ながらも{OSHIERU[:-1]}て"
      f"{KURENAKATTA}</strong>. Qarshilik qolipi birinchi "
      f"qismni yopadi, asosiy gap esa keyin keladi va kesim "
      f"bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: あの{HONYA}はまだ"
      f"ありますか。</strong></p><p><strong>パリ: ___</strong></p>",
      [f"はい。まちの{HONYA}は{HERI}つつありますが、あの{r('店', 'みせ')}は"
       f"まだ{r('開', 'あ')}いています。",
       f"はい。まちの{HONYA}は{HERU}つつありますが、あの{r('店', 'みせ')}は"
       f"まだ{r('開', 'あ')}いています。",
       f"はい。まちの{HONYA}は{HERI}つつもありますが、あの{r('店', 'みせ')}は"
       f"まだ{r('開', 'あ')}いています。",
       f"はい。まちの{HONYA}は{r('減', 'へ')}りますつつありますが、"
       f"あの{r('店', 'みせ')}はまだ{r('開', 'あ')}いています。"],
      f"はい。まちの{HONYA}は{HERI}つつありますが、あの{r('店', 'みせ')}は"
      f"まだ{r('開', 'あ')}いています。",
      f"<p><strong>{HERI_TSUTSUARU}</strong> — «kamayib "
      f"bormoqda», jarayon. Keyin PJ-54 dagi <strong>が</strong> "
      f"bilan qarshi qoʻyilyapti: umumiy yoʻnalish shunday, "
      f"lekin bu doʻkon hali ochiq.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-88 Mashq: 〜として va 〜にとって",
        "tutorial":    "PJ-88:",
        "description": "Rol va baho nuqtasi — va nega oʻzbekcha "
                       "«uchun» uchta yaponcha qolipni koʻtaradi.",
        "questions":   Q_PJ88,
        **DEFAULTS,
    },
    {
        "title":       "PJ-89 Mashq: 〜に関して, 〜について, 〜に対して",
        "tutorial":    "PJ-89:",
        "description": "Mavzu yoki nishon? Va ot oldida uchtasi "
                       "uch xil shaklga oʻtadi.",
        "questions":   Q_PJ89,
        **DEFAULTS,
    },
    {
        "title":       "PJ-90 Mashq: 〜ながらも va 〜つつ",
        "tutorial":    "PJ-90:",
        "description": "Bitta も maʼnoni teskari buradi — va つつある "
                       "qarshilik emas, jarayon.",
        "questions":   Q_PJ90,
        **DEFAULTS,
    },
]
