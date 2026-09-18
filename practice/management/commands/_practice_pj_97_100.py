# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-97 … PJ-100. KURSNING OXIRGI TESTLARI.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning tuzoqlari:
    1. JUFTLIK (PJ-97). 拝啓↔敬具 va 前略↔草々 — aralashtirib
       boʻlmaydi, va elektron xatda 頭語 umuman yozilmaydi.
       先生 va 各位 ga 様 qoʻshilmaydi.
    2. OʻQILISH (PJ-98). 四字熟語 deyarli butunlay on'yomi bilan
       oʻqiladi (一期一会 = いちごいちえ), lekin 三日坊主 —
       kun'yomi. Taxmin qilish bu yerda xato javob beradi.
    3. QATLAM (PJ-99). Soʻzning OʻQILISHI uning qatlamini aytadi:
       kun'yomi→和語, on'yomi→漢語, katakana→外来語. Va katakana
       ingliz tili degani emas — 和製英語 alohida tuzoq.
    4. PJ-100 — kursning yakuniy testi. 1–12 shu darsning oʻz
       faktlari; 13–18 BUTUN KURS boʻyicha takrorlash (は/が,
       て-shakli, 敬語, である体, どころか, たとたん); 19–20
       yoʻl xaritasini qoʻllash.

⚠️ PJ-100 da hech qanday oʻylab topilgan sana, narx yoki markaz
nomi yoʻq — faqat imtihonning tuzilishi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_97_100.py --master=prime \\
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


# ── PJ-97: xat ───────────────────────────────────────────────────────
HAIKEI   = r("拝啓", "はいけい")
KEIGU    = r("敬具", "けいぐ")
ZENRYAKU = r("前略", "ぜんりゃく")
SOUSOU   = r("草々", "そうそう")
KINKEI   = r("謹啓", "きんけい")
TOUGO    = r("頭語", "とうご")
KETSUGO  = r("結語", "けつご")
JIKOU    = r("時候", "じこう") + "の" + r("挨拶", "あいさつ")
OSEWA    = "お" + r("世話", "せわ") + "になっております"
YOROSHIKU = "よろしくお" + r("願", "ねが") + "いいたします"
YOROSHIKU_SHIMASU = "よろしくお" + r("願", "ねが") + "いします"
MOUSHIMASU = "と" + r("申", "もう") + "します"
SAMA     = r("様", "さま")
SENSEI   = r("先生", "せんせい")
KAKUI    = r("各位", "かくい")
TANAKA   = r("田中", "たなか")
YAMADA   = r("山田", "やまだ")
SAKURA   = r("桜", "さくら") + "の" + r("花", "はな") + "が" + r("美", "うつく") + "しい" + r("季節", "きせつ") + "となりました"
OSOREIRI = r("恐", "おそ") + "れ" + r("入", "い") + "りますが"
UKAGAU   = r("伺", "うかが") + "う"
NINENSEI = r("二年生", "にねんせい")
TEGAMI   = r("手紙", "てがみ")

# ── PJ-98: iboralar ──────────────────────────────────────────────────
YOJI     = r("四字熟語", "よじじゅくご")
ISSEKI   = r("一石二鳥", "いっせきにちょう")
JUUNIN   = r("十人十色", "じゅうにんといろ")
JIGOU    = r("自業自得", "じごうじとく")
ICHIGO   = r("一期一会", "いちごいちえ")
ICHIGO_X = r("一期一会", "いっきいっかい")
MIKKA    = r("三日坊主", "みっかぼうず")
MIKKA_X  = r("三日坊主", "さんにちぼうず")
ONKO     = r("温故知新", "おんこちしん")
SHOSHI   = r("初志貫徹", "しょしかんてつ")
IKITOU   = r("意気投合", "いきとうごう")
ISHINOUE = r("石", "いし") + "の" + r("上", "うえ") + "にも" + r("三年", "さんねん")
CHIRIMO  = r("塵", "ちり") + "も" + r("積", "つ") + "もれば" + r("山", "やま") + "となる"
ISOGABA  = r("急", "いそ") + "がば" + r("回", "まわ") + "れ"
SARUMO   = r("猿", "さる") + "も" + r("木", "き") + "から" + r("落", "お") + "ちる"
NANAKORO = r("七転", "ななころ") + "び" + r("八起", "やお") + "き"
HANAYORI = r("花", "はな") + "より" + r("団子", "だんご")

# ── PJ-99: qatlamlar ─────────────────────────────────────────────────
WAGO     = r("和語", "わご")
KANGO    = r("漢語", "かんご")
GAIRAIGO = r("外来語", "がいらいご")
WASEI    = r("和製英語", "わせいえいご")
ATSUMARI = r("集", "あつ") + "まり"
SHUUKAI  = r("集会", "しゅうかい")
HAYASA   = r("速", "はや") + "さ"
SOKUDO   = r("速度", "そくど")
TETSUDAU = r("手伝", "てつだ") + "う"
ENJO     = r("援助", "えんじょ") + "する"
CHUUSHI  = r("中止", "ちゅうし") + "する"
TABEMONO = r("食", "た") + "べ" + r("物", "もの")
SHOKUHIN = r("食品", "しょくひん")
KANGAE   = r("考", "かんが") + "え"
IKEN     = r("意見", "いけん")
JISSHI   = r("実施", "じっし") + "する"
ASHITA   = r("明日", "あした")
MAITSUKI = r("毎月", "まいつき")

# ── PJ-100: yoʻl xaritasi + kurs takrori ─────────────────────────────
KEIZOKU  = r("継続", "けいぞく")
SHUUKAN  = r("習慣", "しゅうかん")
MOKUHYOU = r("目標", "もくひょう")
ONDOKU   = r("音読", "おんどく")
DOKKAI   = r("読解", "どっかい")
CHOUKAI  = r("聴解", "ちょうかい")
GOI      = r("語彙", "ごい")
KIJUNTEN = r("基準点", "きじゅんてん")
WATASHI  = r("私", "わたし")
GAKUSEI  = r("学生", "がくせい")
HON      = r("本", "ほん")
YOMU     = r("読", "よ") + "む"
YONDE    = r("読", "よ") + "んで"
TABERU   = r("食", "た") + "べる"
TABETE   = r("食", "た") + "べて"
IKU      = r("行", "い") + "く"
ITTE     = r("行", "い") + "って"
MESHIAGARU = r("召", "め") + "し" + r("上", "あ") + "がる"
ITADAKU  = r("頂", "いただ") + "く"
KANJI_W  = r("漢字", "かんじ")
YOMENAI  = r("読", "よ") + "めない"
TSUITA   = r("着", "つ") + "いた"
AME      = r("雨", "あめ")
FURIDASHITA = r("降", "ふ") + "り" + r("出", "だ") + "した"
SHIDAI   = r("次第", "しだい")
DENWA    = r("電話", "でんわ")
OOKII    = r("大", "おお") + "きい"
MAINICHI = r("毎日", "まいにち")
TSUZUKERU = r("続", "つづ") + "ける"
KOTOBA   = r("言葉", "ことば")


# ══════════════════════════════════════════════════════════════════════
# PJ-97 — xat, elektron xat va rasmiy murojaat
# ══════════════════════════════════════════════════════════════════════
Q_PJ97 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q(f"<p>{HAIKEI} bilan boshlangan xat nima bilan tugaydi?</p>",
      [KEIGU, SOUSOU, YOROSHIKU, OSEWA],
      KEIGU,
      f"<p><strong>{KEIGU}</strong>. {TOUGO} va {KETSUGO} — "
      f"juftlik: {HAIKEI} ↔ {KEIGU}. {SOUSOU} boshqa juftlikka, "
      f"{ZENRYAKU} ga tegishli.</p>"),

    q(f"<p>{ZENRYAKU} ning jufti qaysi?</p>",
      [SOUSOU, KEIGU, YOROSHIKU, OSEWA],
      SOUSOU,
      f"<p><strong>{SOUSOU}</strong>. {ZENRYAKU} soʻzma-soʻz "
      f"«oldingisini qisqartirdim» degani — mavsum salomi "
      f"yozilmaydi, va xat {SOUSOU} bilan yopiladi.</p>"),

    q("<p>Elektron xat qanday boshlanadi?</p>",
      [f"いつも{OSEWA}。", f"{HAIKEI}", f"{KINKEI}", f"{KEIGU}"],
      f"いつも{OSEWA}。",
      f"<p><strong>いつも{OSEWA}</strong>. {HAIKEI} va "
      f"{KINKEI} — qogʻoz xatning {TOUGO}si; elektron xatda "
      f"ular yozilmaydi.</p>"),

    q(f"<p>{JIKOU} nima?</p>",
      ["Mavsum salomi — xat boshidagi fasl haqidagi jumla",
       "Xat oxiridagi imzo",
       "Konvertdagi manzil",
       "Xat yozilgan sana"],
      "Mavsum salomi — xat boshidagi fasl haqidagi jumla",
      f"<p><strong>Mavsum salomi.</strong> {HAIKEI} dan keyin "
      f"darrov keladi: {SAKURA}。 Bu — yapon xatining eng "
      f"qadimiy qismi va uni tashlab ketish qoʻpollik.</p>"),

    q("<p>Xat oxiridagi qolip soʻz nima deyiladi?</p>",
      [KETSUGO, TOUGO, JIKOU, SAMA],
      KETSUGO,
      f"<p><strong>{KETSUGO}</strong> — xat oxiridagi soʻz "
      f"({KEIGU}, {SOUSOU}). Boshidagisi esa "
      f"<strong>{TOUGO}</strong> ({HAIKEI}, {ZENRYAKU}).</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>___　{SAKURA}。"
      f"</strong></p>",
      [HAIKEI, OSEWA, KEIGU, SOUSOU],
      HAIKEI,
      f"<p><strong>{HAIKEI}</strong>. Mavsum salomi {TOUGO} dan "
      f"keyin turadi, va bu salom bor ekan, {ZENRYAKU} boʻlishi "
      f"mumkin emas — u «salomni qoldirdim» degani.</p>"),

    q("<p>Elektron xat nima bilan yopiladi?</p>",
      [f"{YOROSHIKU}。", f"{KEIGU}", f"{SOUSOU}", f"{JIKOU}"],
      f"{YOROSHIKU}。",
      f"<p><strong>{YOROSHIKU}</strong>. {KEIGU} — qogʻoz "
      f"xatning {KETSUGO}si; elektron xatga u qoʻyilmaydi.</p>"),

    q(f"<p>«Men ikkinchi kurs talabasi Inomman» — rasmiy xatda?</p>",
      [f"{NINENSEI}のイノム{MOUSHIMASU}",
       f"{NINENSEI}のイノムです",
       f"{NINENSEI}のイノムでございましょう",
       f"{NINENSEI}のイノムと{UKAGAU}"],
      f"{NINENSEI}のイノム{MOUSHIMASU}",
      f"<p><strong>{NINENSEI}のイノム{MOUSHIMASU}</strong>. "
      f"Xatda oʻzini tanishtirish uchun <strong>〜{MOUSHIMASU}"
      f"</strong> ishlatiladi — です emas. Bu "
      f"{r('謙譲語', 'けんじょうご')} (PJ-70).</p>"),

    q(f"<p>{ZENRYAKU} dan keyin nima YOZILMAYDI?</p>",
      [JIKOU, "さっそくですが", "asosiy gap", SOUSOU],
      JIKOU,
      f"<p><strong>{JIKOU}</strong> yozilmaydi. {ZENRYAKU} ning "
      f"oʻzi «salomni qoldirdim» degani, shuning uchun undan "
      f"keyin salom yozilsa, xat oʻz-oʻziga qarshi chiqadi.</p>"),

    q("<p>Oʻqituvchingizga xat yozyapsiz. Ismidan keyin nima?</p>",
      [f"{TANAKA}{SENSEI}", f"{TANAKA}{SENSEI}{SAMA}",
       f"{TANAKA}{SAMA}{SENSEI}", f"{TANAKA}{SENSEI}{KAKUI}"],
      f"{TANAKA}{SENSEI}",
      f"<p><strong>{TANAKA}{SENSEI}</strong>. {SENSEI} ning "
      f"oʻzi hurmat belgisi, shuning uchun ustiga {SAMA} "
      f"qoʻyilmaydi — bu ikki marta hurmat boʻladi va "
      f"savodsiz koʻrinadi.</p>"),

    q("<p>Bir guruh odamga birdan murojaat qilyapsiz. Qaysi soʻz?</p>",
      [KAKUI, SAMA, SENSEI, TOUGO],
      KAKUI,
      f"<p><strong>{KAKUI}</strong> — «hurmatli hammangiz». "
      f"U ham yolgʻiz turadi: {KAKUI}{SAMA} deb "
      f"yozilmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>お"
      f"{r('忙', 'いそが')}しいところ___、{YOROSHIKU}。</strong></p>",
      [OSOREIRI, JIKOU, KEIGU, ZENRYAKU],
      OSOREIRI,
      f"<p><strong>{OSOREIRI}</strong> — «bezovta qilganim "
      f"uchun uzr». Iltimosdan oldin qoʻyiladigan tayyor "
      f"jumla; rasmiy xatda deyarli har doim uchraydi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>{HAIKEI} va {OSEWA} — qaysi biri qayerda?</p>",
      [f"{HAIKEI} — qogʻoz xat, {OSEWA} — elektron xat",
       f"{HAIKEI} — elektron xat, {OSEWA} — qogʻoz xat",
       "Ikkalasi ham faqat qogʻoz xatda",
       "Ikkalasi ham faqat elektron xatda"],
      f"{HAIKEI} — qogʻoz xat, {OSEWA} — elektron xat",
      f"<p><strong>{HAIKEI} qogʻozda, {OSEWA} elektron "
      f"xatda.</strong> Elektron xatni {HAIKEI} bilan "
      f"boshlash — bu darsning eng koʻp uchraydigan xatosi.</p>"),

    q(f"<p>{SAMA} va {SENSEI} — farqi nimada?</p>",
      [f"{SAMA} umumiy hurmat, {SENSEI} kasbga bogʻliq",
       f"{SAMA} faqat ayollarga, {SENSEI} erkaklarga",
       f"{SAMA} yozma, {SENSEI} ogʻzaki",
       "Farqi yoʻq, ikkalasi ham bir xil"],
      f"{SAMA} umumiy hurmat, {SENSEI} kasbga bogʻliq",
      f"<p><strong>{SAMA}</strong> — har kimga yaraydigan eng "
      f"xavfsiz tanlov ({YAMADA}{SAMA}). <strong>{SENSEI}</strong> "
      f"— oʻqituvchi, shifokor, yurist. Ikkalasi birga "
      f"qoʻyilmaydi.</p>"),

    q(f"<p>{YOROSHIKU_SHIMASU} va {YOROSHIKU} — farqi?</p>",
      ["いたします — kamtarona shakl, rasmiy xat uchun",
       "します — kamtarona shakl, rasmiy xat uchun",
       "Farqi yoʻq",
       "いたします faqat ogʻzaki nutqda"],
      "いたします — kamtarona shakl, rasmiy xat uchun",
      f"<p><strong>いたします</strong> — する ning "
      f"{r('謙譲語', 'けんじょうご')} shakli (PJ-70), shuning "
      f"uchun u rasmiyroq. Ustozga yoki tashkilotga yozganda "
      f"{YOROSHIKU} toʻgʻri keladi.</p>"),

    q(f"<p>{ZENRYAKU} bilan {HAIKEI} ning asosiy farqi nima?</p>",
      [f"{ZENRYAKU} da {JIKOU} yozilmaydi",
       f"{ZENRYAKU} faqat ayollar yozadigan xatda",
       f"{ZENRYAKU} elektron xat uchun",
       f"{ZENRYAKU} xat oxirida turadi"],
      f"{ZENRYAKU} da {JIKOU} yozilmaydi",
      f"<p><strong>Mavsum salomi.</strong> {HAIKEI} bilan "
      f"toʻliq xat yoziladi — salom bilan. {ZENRYAKU} esa "
      f"«salomni qoldirdim» degani: darrov ishga oʻtiladi va "
      f"xat {SOUSOU} bilan yopiladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [f"{HAIKEI} … {SOUSOU}", f"{HAIKEI} … {KEIGU}",
       f"{ZENRYAKU} … {SOUSOU}", f"{KINKEI} … {r('謹言', 'きんげん')}"],
      f"{HAIKEI} … {SOUSOU}",
      f"<p>Xato — <strong>{HAIKEI} … {SOUSOU}</strong>: "
      f"juftlik buzilgan. {HAIKEI} ning jufti {KEIGU}, "
      f"{SOUSOU} ning jufti esa {ZENRYAKU}.</p>"),

    q("<p>Qaysi murojaat toʻgʻri?</p>",
      [f"{TANAKA}{SENSEI}", f"{TANAKA}{SENSEI}{SAMA}",
       f"{KAKUI}{SAMA}", f"{TANAKA}{SAMA}{SAMA}"],
      f"{TANAKA}{SENSEI}",
      f"<p><strong>{TANAKA}{SENSEI}</strong>. {SENSEI} ham, "
      f"{KAKUI} ham oʻzida hurmat olib yuradi — ularga {SAMA} "
      f"qoʻshilmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q("<p>Elektron xatning toʻgʻri tartibi qaysi?</p>",
      ["Kimga → salom → oʻzini tanishtirish → asosiy gap → yopish → imzo",
       "Salom → kimga → asosiy gap → imzo → yopish",
       "Kimga → asosiy gap → salom → oʻzini tanishtirish → imzo",
       "Oʻzini tanishtirish → kimga → yopish → asosiy gap → salom"],
      "Kimga → salom → oʻzini tanishtirish → asosiy gap → yopish → imzo",
      f"<p><strong>Kimga → salom → tanishtirish → gap → yopish "
      f"→ imzo.</strong> Amalda: {TANAKA}{SENSEI} → いつも"
      f"{OSEWA} → {NINENSEI}のイノム{MOUSHIMASU} → asosiy gap "
      f"→ {YOROSHIKU} → imzo.</p>"),

    q(f"<p>Qisqa xat yozyapsiz, mavsum salomisiz. Qaysi juftlikni "
      f"tanlaysiz?</p>",
      [f"{ZENRYAKU} … {SOUSOU}", f"{HAIKEI} … {KEIGU}",
       f"{KINKEI} … {r('謹言', 'きんげん')}", f"{OSEWA} … {YOROSHIKU}"],
      f"{ZENRYAKU} … {SOUSOU}",
      f"<p><strong>{ZENRYAKU} … {SOUSOU}</strong> — aynan shu "
      f"holat uchun bor juftlik. {HAIKEI} tanlansa, mavsum "
      f"salomi majburiy boʻlib qoladi; {OSEWA} esa elektron "
      f"xatniki, qogʻozniki emas.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-98 — 四字熟語 va ことわざ
# ══════════════════════════════════════════════════════════════════════
Q_PJ98 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q(f"<p>{ISSEKI} nimani anglatadi?</p>",
      ["Bitta ish bilan ikki foyda", "Har kim boshqacha",
       "Qilmishiga yarasha", "Tez tashlab qoʻyadigan odam"],
      "Bitta ish bilan ikki foyda",
      f"<p><strong>Bitta ish bilan ikki foyda.</strong> "
      f"Soʻzma-soʻz «bir tosh, ikki qush»; oʻzbekcha jufti — "
      f"«bir oʻq bilan ikki quyon».</p>"),

    q(f"<p>{JUUNIN} nimani anglatadi?</p>",
      ["Har kimning didi har xil", "Oʻn kishi bir joyda",
       "Oʻn yil sabr", "Oʻn xil rang"],
      "Har kimning didi har xil",
      f"<p><strong>Har kimning didi har xil.</strong> Soʻzma-soʻz "
      f"«oʻn odam, oʻn rang» — har kim boshqacha degani. "
      f"Ranglar haqidagi gap emas.</p>"),

    q(f"<p>{JIGOU} nimani anglatadi?</p>",
      ["Nima eksang, shuni oʻrasan", "Oʻz ishini oʻzi qiladi",
       "Mustaqil odam", "Oʻzini oʻzi boqadi"],
      "Nima eksang, shuni oʻrasan",
      f"<p><strong>Nima eksang, shuni oʻrasan.</strong> "
      f"«Oʻz ishi, oʻz olgani» — qilmishining natijasini "
      f"oʻzi koʻradi. Odatda salbiy holatda ishlatiladi.</p>"),

    q(f"<p>{YOJI} va ことわざ farqi nimada?</p>",
      [f"{YOJI} — toʻrt kanjidan iborat soʻz, ことわざ — toʻliq gap",
       f"{YOJI} — gap, ことわざ — soʻz",
       f"{YOJI} yaponcha, ことわざ xitoycha",
       "Farqi yoʻq, ikkalasi bir xil"],
      f"{YOJI} — toʻrt kanjidan iborat soʻz, ことわざ — toʻliq gap",
      f"<p><strong>Shakl.</strong> {ISSEKI} — bitta <strong>soʻz</strong>, "
      f"on'yomi bilan oʻqiladi. {ISHINOUE} — toʻliq <strong>gap</strong>, "
      f"yaponcha oʻqilishda.</p>"),

    q(f"<p>{ICHIGO} qanday oʻqiladi?</p>",
      ["いちごいちえ", "いっきいっかい", "いちきいちかい",
       "いっこいちえ"],
      "いちごいちえ",
      f"<p><strong>いちごいちえ</strong>. «いっきいっかい» juda "
      f"tabiiy taxmin — va xato. Bu iboralarning oʻqilishi "
      f"qoidadan emas, tarixdan keladi; har birini alohida "
      f"yodlash kerak.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>{MIKKA} qanday oʻqiladi?</p>",
      ["みっかぼうず", "さんにちぼうず", "さんじつぼうず",
       "みかぼうず"],
      "みっかぼうず",
      f"<p><strong>みっかぼうず</strong>. Deyarli barcha {YOJI} "
      f"butunlay on'yomi bilan oʻqiladi, bu esa istisno: "
      f"{r('三日', 'みっか')} — kun'yomi. Istisnolar kam, "
      f"lekin bor.</p>"),

    q(f"<p>{ISHINOUE} nimani aytadi?</p>",
      ["Sabr — qiyin ishni tashlab qoʻymaslik kerak",
       "Toshda oʻtirish foydali",
       "Uch yildan keyin koʻchib ketish kerak",
       "Sovuq joyda yashash qiyin"],
      "Sabr — qiyin ishni tashlab qoʻymaslik kerak",
      f"<p><strong>Sabr — qiyin ishni tashlab qoʻymaslik "
      f"kerak.</strong> Sovuq toshda ham uch "
      f"yil oʻtirsang, u isiydi. Oʻzbekcha jufti — <strong>«sabr "
      f"tagi sariq oltin»</strong>.</p>"),

    q("<p>«Yetti oʻlchab, bir kes» — qaysi yaponcha maqol?</p>",
      [f"{ISOGABA}", f"{CHIRIMO}", f"{SARUMO}", f"{HANAYORI}"],
      f"{ISOGABA}",
      f"<p><strong>{ISOGABA}</strong> — «shoshsang, aylanib "
      f"oʻt». Ikkala maqol ham bitta narsani aytadi: shoshilinch "
      f"yoʻl koʻpincha uzunroq chiqadi.</p>"),

    q("<p>«Tomchi tomchi koʻl boʻlar» — qaysi yaponcha maqol?</p>",
      [f"{CHIRIMO}", f"{ISHINOUE}", f"{NANAKORO}", f"{ISOGABA}"],
      f"{CHIRIMO}",
      f"<p><strong>{CHIRIMO}</strong> — «chang ham yigʻilsa togʻ "
      f"boʻladi». {ISHINOUE} ham sabr haqida, lekin u "
      f"<em>chidash</em> haqida; bu esa <em>toʻplanish</em> "
      f"haqida.</p>"),

    q(f"<p>{SARUMO} nimani aytadi?</p>",
      ["Har qanday usta ham xato qilishi mumkin",
       "Maymunlar daraxtga chiqa olmaydi",
       "Balandga chiqmaslik kerak",
       "Hayvonlardan oʻrganish kerak"],
      "Har qanday usta ham xato qilishi mumkin",
      f"<p><strong>Ustalar ham xato qiladi.</strong> Oʻzbekcha "
      f"jufti — «otning ham oyogʻi qoqiladi». Daraxtga eng "
      f"yaxshi chiqadigan jonivor ham yiqiladi.</p>"),

    q(f"<p>{ONKO} nimani anglatadi?</p>",
      ["Eskini oʻrganib, yangisini tushunish",
       "Eski narsalarni yigʻish",
       "Issiq joyda yashash",
       "Yangi narsani rad etish"],
      "Eskini oʻrganib, yangisini tushunish",
      f"<p><strong>Eskini oʻrganib, yangisini tushunish.</strong> "
      f"Soʻzma-soʻz «eskini isit, yangini bil» — oʻtmishni "
      f"bilgan odam bugunni yaxshiroq tushunadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>"
      f"{r('歩', 'ある')}いて{r('通', 'かよ')}えば、お"
      f"{r('金', 'かね')}も{r('節約', 'せつやく')}できるし"
      f"{r('健康', 'けんこう')}にもいい。まさに___だ。</strong></p>",
      [ISSEKI, JUUNIN, JIGOU, MIKKA],
      ISSEKI,
      f"<p><strong>{ISSEKI}</strong> — bitta ish (piyoda "
      f"yurish), ikkita foyda (pul va sogʻliq). Odatdagi "
      f"qolip: avval vaziyat, keyin <strong>まさに〜だ</strong> "
      f"bilan xulosa.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>{ISHINOUE} va {CHIRIMO} — farqi nimada?</p>",
      ["Birinchisi chidash, ikkinchisi toʻplanish haqida",
       "Birinchisi toʻplanish, ikkinchisi chidash haqida",
       "Ikkalasi ham bir xil narsani aytadi",
       "Birinchisi sabr, ikkinchisi shoshqaloqlik haqida"],
      "Birinchisi chidash, ikkinchisi toʻplanish haqida",
      f"<p><strong>{ISHINOUE}</strong> — qiyin narsaga "
      f"<em>chidash</em>. <strong>{CHIRIMO}</strong> — kichik "
      f"narsalarning <em>toʻplanishi</em>. Ikkalasi ham sabr "
      f"haqida, lekin bir xil emas.</p>"),

    q(f"<p>Ustozingizga {SARUMO} maqolini aytsangiz nima "
      f"boʻladi?</p>",
      ["Uni maymunga qiyoslagan boʻlasiz — bu qoʻpollik",
       "Hech narsa, bu oddiy maqol",
       "Uni maqtagan boʻlasiz",
       "Grammatik xato boʻladi"],
      "Uni maymunga qiyoslagan boʻlasiz — bu qoʻpollik",
      f"<p><strong>Qoʻpollik.</strong> Maqol toʻgʻri, lekin "
      f"ohangi yuqoridagi odamga qaratilmaydi. Oʻzbekchada ham "
      f"«otning ham oyogʻi qoqiladi» — oʻrtoqqa aytiladi, "
      f"otangizga emas.</p>"),

    q(f"<p>{YOJI} qanday oʻqiladi — umumiy qoida?</p>",
      ["Deyarli butunlay on'yomi bilan",
       "Deyarli butunlay kun'yomi bilan",
       "Birinchi ikkitasi on'yomi, oxirgisi kun'yomi",
       "Har doim katakana bilan"],
      "Deyarli butunlay on'yomi bilan",
      f"<p><strong>On'yomi.</strong> Bu iboralarning koʻpi "
      f"Xitoydan kelgan, shuning uchun xitoycha oʻqilish "
      f"ishlaydi: {ISSEKI}, {JUUNIN}. Istisnolar bor "
      f"({MIKKA}), lekin ular kam.</p>"),

    q(f"<p>Inshoda nechta ことわざ yoki {YOJI} ishlatasiz?</p>",
      ["Bittasi, va uni xulosaga qoʻyaman",
       "Har xatboshida bittadan",
       "Kamida uchtasi",
       "Umuman ishlatmayman"],
      "Bittasi, va uni xulosaga qoʻyaman",
      f"<p><strong>Bittasi, xulosaga.</strong> Bitta oʻz "
      f"joyidagi ibora kuchli va oʻqigan odamni koʻrsatadi; "
      f"uchtasi ketma-ket esa bilim emas, koʻz-koʻz qilish "
      f"boʻlib eshitiladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi oʻqilish notoʻgʻri?</p>",
      [ICHIGO_X, ICHIGO, MIKKA, ISSEKI],
      ICHIGO_X,
      f"<p>Xato — <strong>いっきいっかい</strong>. Toʻgʻrisi "
      f"<strong>{ICHIGO}</strong>. Har bir ibora bitta soʻz "
      f"kabi, oʻz oʻqilishi bilan yodlanadi.</p>"),

    q("<p>Qaysi gapda xato bor?</p>",
      [f"{ISSEKI}を{r('使', 'つか')}った",
       f"まさに{ISSEKI}だ",
       f"{MAINICHI}{r('十分', 'じゅっぷん')}でもいい。{CHIRIMO}。",
       f"{r('先生', 'せんせい')}でも{r('間違', 'まちが')}える。{SARUMO}のだから。"],
      f"{ISSEKI}を{r('使', 'つか')}った",
      f"<p>Xato — <strong>{ISSEKI}を{r('使', 'つか')}った</strong>. "
      f"Bu ibora <strong>ot</strong>, va u «ishlatildi» deb emas, "
      f"<strong>まさに〜だ</strong> bilan xulosa qilib "
      f"qoʻyiladi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Doʻstingiz har oy yangi mashgʻulot boshlaydi va uch "
      f"kundan keyin tashlab qoʻyadi. U qanday odam?</p>",
      [MIKKA, SHOSHI, IKITOU, ONKO],
      MIKKA,
      f"<p><strong>{MIKKA}</strong> — «uch kunlik rohib», "
      f"tez tashlab qoʻyadigan odam. Uning teskarisi — "
      f"<strong>{SHOSHI}</strong>, boshlagan ishni oxiriga "
      f"yetkazish.</p>"),

    q(f"<p>Ikki kishi birinchi marta uchrashdi va darrov til "
      f"topishdi. Qaysi ibora?</p>",
      [IKITOU, JIGOU, JUUNIN, ONKO],
      IKITOU,
      f"<p><strong>{IKITOU}</strong> — «ruh mos tushdi», "
      f"darrov til topishmoq. {JUUNIN} aksincha, har kim "
      f"boshqacha degan maʼnoni beradi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-99 — 和語・漢語・外来語
# ══════════════════════════════════════════════════════════════════════
Q_PJ99 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q(f"<p>{WAGO} nima?</p>",
      ["Asl yaponcha soʻz — kun'yomi bilan oʻqiladi",
       "Xitoy ildizli soʻz — on'yomi bilan oʻqiladi",
       "Chetdan kirgan soʻz — katakanada yoziladi",
       "Yaponiyada yasalgan «chet» soʻz"],
      "Asl yaponcha soʻz — kun'yomi bilan oʻqiladi",
      f"<p><strong>Asl yaponcha soʻz.</strong> {ATSUMARI}, "
      f"{HAYASA}, {TABEMONO} — kanji hiragana bilan tugagan, "
      f"demak kun'yomi, demak {WAGO}.</p>"),

    q(f"<p>{KANGO} qanday oʻqiladi?</p>",
      ["On'yomi bilan", "Kun'yomi bilan", "Katakana bilan",
       "Furigana bilan"],
      "On'yomi bilan",
      f"<p><strong>On'yomi.</strong> {SHUUKAI}, {SOKUDO}, "
      f"{SHOKUHIN} — ikki kanji yopishgan, demak xitoycha "
      f"oʻqilish ishlaydi. Bu PJ-11 dagi qoidaning aynan "
      f"oʻzi.</p>"),

    q(f"<p>{GAIRAIGO} qaysi yozuvda yoziladi?</p>",
      ["Katakana", "Hiragana", "Faqat kanji", "Romaji"],
      "Katakana",
      f"<p><strong>Katakana.</strong> Aynan shu ish uchun "
      f"katakana bor (PJ-7): ミーティング, スピード, フード. "
      f"Shuning uchun uchinchi qatlamni ajratish umuman mehnat "
      f"talab qilmaydi.</p>"),

    q(f"<p>{WASEI} nima?</p>",
      ["Yaponiyada yasalgan, chet tilida boshqa maʼno beradigan soʻz",
       "Xitoydan kelgan qadimiy soʻz",
       "Faqat sheʼrda ishlatiladigan soʻz",
       "Yozma tilda ishlatilmaydigan soʻz"],
      "Yaponiyada yasalgan, chet tilida boshqa maʼno beradigan soʻz",
      f"<p><strong>Yaponiyada yasalgan soʻz.</strong> コンセント "
      f"— rozetka, マンション — kvartira, サラリーマン — idora "
      f"xodimi. Ularni ingliz tilidan taxmin qilish xato javob "
      f"beradi.</p>"),

    q(f"<p>{ATSUMARI} qaysi qatlamga tegishli?</p>",
      [WAGO, KANGO, GAIRAIGO, WASEI],
      WAGO,
      f"<p><strong>{WAGO}</strong>. Kanji hiragana bilan "
      f"tugayapti ({ATSUMARI}) — bu kun'yomi, demak asl "
      f"yaponcha soʻz. {SHUUKAI} boʻlsa {KANGO} boʻlardi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Rasmiy eʼlon yozyapsiz. «Yigʻilish» qaysi soʻz bilan?</p>",
      [SHUUKAI, ATSUMARI, "ミーティング", "パーティー"],
      SHUUKAI,
      f"<p><strong>{SHUUKAI}</strong>. Rasmiy matn {KANGO}ni "
      f"chaqiradi, va u である{r('体', 'たい')} bilan bir "
      f"uslubda turadi (PJ-96).</p>"),

    q(f"<p>Doʻstingizga xabar yozyapsiz. «Ertagi yigʻilish» — "
      f"qaysi soʻz?</p>",
      [f"{ASHITA}の{ATSUMARI}", f"{ASHITA}の{SHUUKAI}",
       f"{ASHITA}の{JISSHI}", f"{ASHITA}の{IKEN}"],
      f"{ASHITA}の{ATSUMARI}",
      f"<p><strong>{ATSUMARI}</strong>. Oddiy gapda {WAGO} "
      f"tabiiy; {SHUUKAI} bu yerda birdan sovuq va rasmiy "
      f"boʻlib qoladi.</p>"),

    q("<p>コンセント nimani anglatadi?</p>",
      ["Rozetka", "Rozilik", "Kontsert", "Shartnoma"],
      "Rozetka",
      f"<p><strong>Rozetka.</strong> Bu {WASEI} — Yaponiyada "
      f"yasalgan soʻz. Katakana koʻrganda ingliz tilidan "
      f"taxmin qilmang; lugʻatdan qarang.</p>"),

    q("<p>マンション nimani anglatadi?</p>",
      ["Koʻp qavatli uydagi kvartira", "Qasr", "Saroy",
       "Yakka tartibdagi uy"],
      "Koʻp qavatli uydagi kvartira",
      f"<p><strong>Kvartira.</strong> Yana bir {WASEI}: "
      f"yaponchada マンション — oddiy koʻp qavatli uydagi "
      f"kvartira, hech qanday qasr emas.</p>"),

    q(f"<p>{HAYASA} · {SOKUDO} · スピード — bu uchtalikning "
      f"oʻzbekcha jufti qaysi?</p>",
      ["tezlik · surʼat · skorost", "kuch · quvvat · energiya",
       "oʻy · fikr · ideya", "boshliq · rahbar · direktor"],
      "tezlik · surʼat · skorost",
      f"<p><strong>tezlik · surʼat · skorost.</strong> Har "
      f"ikkala tilda ham bir xil uch qatlam, bir xil tartibda: "
      f"oʻz qatlam → klassik oʻzlashma → zamonaviy "
      f"oʻzlashma.</p>"),

    q(f"<p>{KANGAE} · {IKEN} · アイデア — oʻzbekcha jufti?</p>",
      ["oʻy · fikr · ideya", "tezlik · surʼat · skorost",
       "yigʻilish · majlis · miting", "kuch · quvvat · energiya"],
      "oʻy · fikr · ideya",
      f"<p><strong>oʻy · fikr · ideya.</strong> {KANGAE} — "
      f"{WAGO}, {IKEN} — {KANGO}, アイデア — {GAIRAIGO}. "
      f"Oʻzbekchada esa turkiy, arabcha va yevropacha "
      f"qatlamlar.</p>"),

    q(f"<p>{TETSUDAU} ning {KANGO} jufti qaysi?</p>",
      [ENJO, "サポートする", CHUUSHI, JISSHI],
      ENJO,
      f"<p><strong>{ENJO}</strong> — ikki kanji yopishgan, "
      f"on'yomi bilan oʻqiladi. サポートする — uchinchi "
      f"qatlam, {GAIRAIGO}.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>Nega gazeta sarlavhasi deyarli butunlay {KANGO}dan "
      f"iborat?</p>",
      ["Zichroq — bir xil maʼnoni kamroq belgida aytadi",
       "Chunki gazeta xitoy tilida chiqadi",
       "Chunki katakana bosishga qimmat",
       "Chunki kun'yomi oʻqish qiyin"],
      "Zichroq — bir xil maʼnoni kamroq belgida aytadi",
      f"<p><strong>Zichroq — bir xil maʼnoni kamroq belgida "
      f"aytadi.</strong> Sarlavhada joy tor "
      f"(PJ-96), {KANGO} esa {WAGO}dan qisqaroq: {JISSHI} bir "
      f"soʻzda «amalga oshirmoq» deydi.</p>"),

    q(f"<p>Hikoya yoki sheʼr yozyapsiz. Qaysi qatlam asosiy?</p>",
      [WAGO, KANGO, GAIRAIGO, WASEI],
      WAGO,
      f"<p><strong>{WAGO}</strong> — yumshoq ohang. Adabiyot "
      f"shu qatlamda yashaydi; {KANGO} esa maqola va ilmiy "
      f"ishning tili.</p>"),

    q(f"<p>Soʻzning qaysi qatlamga tegishli ekanini qayerdan "
      f"bilasiz?</p>",
      ["Oʻqilishidan — kun'yomi, on'yomi yoki katakana",
       "Uzunligidan", "Maʼnosidan", "Kanjilar sonidan"],
      "Oʻqilishidan — kun'yomi, on'yomi yoki katakana",
      f"<p><strong>Oʻqilishidan.</strong> Kun'yomi → {WAGO}, "
      f"on'yomi → {KANGO}, katakana → {GAIRAIGO}. Bu asbob "
      f"sizda PJ-11 dan beri bor edi.</p>"),

    q(f"<p>«yigʻilish · majlis · miting» — bu uchtalik nimani "
      f"koʻrsatadi?</p>",
      ["Oʻzbek tilida ham aynan uchta lugʻat qatlami borligini",
       "Uch xil yigʻilish turini",
       "Soʻzlarning uzunligi farqini",
       "Uchta boshqa tilni"],
      "Oʻzbek tilida ham aynan uchta lugʻat qatlami borligini",
      f"<p><strong>Uch qatlam.</strong> Turkiy, arab-fors va "
      f"rus-yevropa qatlamlari — aynan {ATSUMARI} · {SHUUKAI} · "
      f"ミーティング kabi. Tanlovni siz allaqachon quloq bilan "
      f"bilasiz.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda uslub xatosi bor?</p>",
      [f"(doʻstga) {ASHITA}の{SHUUKAI}、{r('行', 'い')}く？",
       f"(doʻstga) {ASHITA}の{ATSUMARI}、{r('行', 'い')}く？",
       f"({r('掲示', 'けいじ')}) {MAITSUKI}{SHUUKAI}を{JISSHI}している。",
       f"({r('会社', 'かいしゃ')}) {r('十時', 'じゅうじ')}からミーティングです。"],
      f"(doʻstga) {ASHITA}の{SHUUKAI}、{r('行', 'い')}く？",
      f"<p>Xato — doʻstga aytilgan gapda <strong>{SHUUKAI}"
      f"</strong>: bu {KANGO}, va oddiy suhbatda u sovuq "
      f"chiqadi. Toʻgʻrisi <strong>{ATSUMARI}</strong>.</p>"),

    q("<p>Qaysi soʻz notoʻgʻri yasalgan?</p>",
      [f"{SHUUKAI}まり", ATSUMARI, SHUUKAI, "ミーティング"],
      f"{SHUUKAI}まり",
      f"<p>Xato — <strong>{SHUUKAI}まり</strong>: ikki qatlam "
      f"bitta soʻzga yopishtirilgan. Yo {ATSUMARI} ({WAGO}), "
      f"yo {SHUUKAI} ({KANGO}) — ikkovi birga emas.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>である{r('体', 'たい')}da insho yozyapsiz. Qaysi "
      f"qatlam asosiy boʻladi?</p>",
      [KANGO, WAGO, GAIRAIGO, WASEI],
      KANGO,
      f"<p><strong>{KANGO}</strong>. である{r('体', 'たい')} "
      f"(PJ-96) va {KANGO} bir-birini chaqiradi: ikkalasi ham "
      f"rasmiy yozma matnning asbobi. {GAIRAIGO} esa faqat "
      f"jufti yoʻq tushunchalar uchun.</p>"),

    q(f"<p>Katakanada yozilgan notanish soʻzni koʻrdingiz. Nima "
      f"qilasiz?</p>",
      ["Lugʻatdan qarayman", "Ingliz tilidan taxmin qilaman",
       "Kun'yomi bilan oʻqiyman", "Kanjisini qidiraman"],
      "Lugʻatdan qarayman",
      f"<p><strong>Lugʻatdan qarayman.</strong> Taxmin koʻp "
      f"hollarda ishlaydi, lekin {WASEI} aynan eng muhim "
      f"joylarda adashtiradi: shartnomada, koʻrsatmada, "
      f"imtihon matnida.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-100 — yoʻl xaritasi + BUTUN KURS boʻyicha takrorlash (13–18)
# ══════════════════════════════════════════════════════════════════════
Q_PJ100 = [
    # ── 1–5 tanish: darsning oʻz faktlari ────────────────────────────
    q("<p>Bu kursni tugatgan oʻquvchi qaysi darajada?</p>",
      ["Mustahkam N4, N3 ga kirib", "N5", "N2", "N1"],
      "Mustahkam N4, N3 ga kirib",
      f"<p><strong>Mustahkam N4, N3 ga kirib.</strong> Uchta "
      f"yozuv, taxminan 600 kanji va N4 grammatikasining "
      f"hammasi — bu kursning nishoni shu edi.</p>"),

    q(f"<p>{KIJUNTEN} qoidasi nima deydi?</p>",
      ["Har bir boʻlimdan alohida eng kam ball olinishi shart",
       "Faqat umumiy ball hisobga olinadi",
       "Tinglash boʻlimi ixtiyoriy",
       "Har bir boʻlimdan 60 ball kerak"],
      "Har bir boʻlimdan alohida eng kam ball olinishi shart",
      f"<p><strong>Har bir boʻlimdan alohida.</strong> Umumiy "
      f"ball yetishi kifoya emas — shuning uchun {CHOUKAI}ni "
      f"tashlab boʻlmaydi, {DOKKAI}dan aʼlo olsangiz ham.</p>"),

    q(f"<p>{ONDOKU} nima?</p>",
      ["Ovoz chiqarib oʻqish", "Jimgina oʻqish",
       "Yodlab aytish", "Koʻchirib yozish"],
      "Ovoz chiqarib oʻqish",
      f"<p><strong>Ovoz chiqarib oʻqish.</strong> U bir vaqtning "
      f"oʻzida talaffuzni, oʻqish tezligini va eshitishni mashq "
      f"qiladi — uchta ish, oʻn daqiqa.</p>"),

    q("<p>N3 uchun taxminan qancha kanji kerak?</p>",
      ["650", "300", "1 000", "2 000"],
      "650",
      f"<p><strong>Taxminan 650.</strong> N4 da 300, N2 da "
      f"1 000, N1 da 2 000. Bu sonlar aniq roʻyxat emas, "
      f"moʻljal: imtihon tashkiloti 2010-yildan beri aniq "
      f"roʻyxat eʼlon qilmaydi.</p>"),

    q(f"<p>{KEIZOKU} nimani anglatadi?</p>",
      ["Davomiylik, uzilmaslik", "Tezlik", "Qiyinchilik",
       "Maqsad"],
      "Davomiylik, uzilmaslik",
      f"<p><strong>Davomiylik.</strong> {MOKUHYOU} — maqsad, "
      f"{SHUUKAN} — odat. Bu uchtasi bu darsning asosiy "
      f"soʻzlari.</p>"),

    # ── 6–12 qoʻllash: strategiya ────────────────────────────────────
    q("<p>N4 dan N3 gacha nima eng koʻp oshadi?</p>",
      ["Soʻz boyligi — taxminan ikki yarim baravar",
       "Grammatika qoidalari soni",
       "Imtihon vaqti",
       "Boʻlimlar soni"],
      "Soʻz boyligi — taxminan ikki yarim baravar",
      f"<p><strong>Soʻz boyligi — {GOI} — taxminan ikki yarim "
      f"baravar.</strong> 1 500 dan 3 750 gacha. "
      f"Odamlar buni «grammatika qiyinlashdi» deb "
      f"tushuntiradi, aslida esa matn tezlashadi.</p>"),

    q("<p>Kanjini qanday yodlash toʻgʻri?</p>",
      [f"Soʻz ichida: {r('学校', 'がっこう')} va {r('学生', 'がくせい')}",
       f"Yolgʻiz, roʻyxat boʻyicha: {r('学', 'がく')}",
       "Faqat oʻqilishini",
       "Faqat chiziqlar tartibini"],
      f"Soʻz ichida: {r('学校', 'がっこう')} va {r('学生', 'がくせい')}",
      f"<p><strong>Soʻz ichida.</strong> Kanjining oʻqilishi "
      f"kontekstdan keladi — yolgʻiz belgi qaysi oʻqilishda "
      f"kelishini aytmaydi. Bu PJ-11 dagi on'yomi va "
      f"kun'yomi qoidasining amaliy natijasi.</p>"),

    q("<p>Kuniga 30 daqiqa bilan N3 gacha qancha vaqt ketadi?</p>",
      ["Taxminan 10–12 oy", "Taxminan 2 oy", "Taxminan 5 yil",
       "Taxminan 3 hafta"],
      "Taxminan 10–12 oy",
      f"<p><strong>10–12 oy.</strong> Kuniga ikki soat bilan "
      f"4–6 oy. Lekin muhimi tezlik emas, "
      f"<strong>{KEIZOKU}</strong> — uzilishsizlik.</p>"),

    q("<p>Notanish soʻz uchradi. Nima qilasiz?</p>",
      ["Belgilab qoʻyaman va oxirigacha oʻqiyman",
       "Darrov toʻxtab lugʻatdan qidiraman",
       "Matnni tashlab, osonrogʻini olaman",
       "Soʻzni tashlab ketaman va qaytmayman"],
      "Belgilab qoʻyaman va oxirigacha oʻqiyman",
      f"<p><strong>Oxirigacha oʻqiyman.</strong> Har soʻzda "
      f"toʻxtagan odam hech qachon tezlashmaydi. "
      f"{r('分', 'わ')}からない{KOTOBA}があっても、"
      f"{r('最後', 'さいご')}まで{r('読', 'よ')}んでみてください。</p>"),

    q("<p>Yangi soʻzni qanday yozib qoʻygan maʼqul?</p>",
      ["Gap ichida", "Yolgʻiz, tarjimasi bilan",
       "Faqat kanjisini", "Faqat katakanada"],
      "Gap ichida",
      f"<p><strong>Gap ichida.</strong> Yolgʻiz soʻz "
      f"unutiladi, gap qoladi — chunki gap soʻzga "
      f"qoʻshimcha, qoʻshni soʻz va ohang beradi.</p>"),

    q("<p>Imtihon sanasini qayerdan bilasiz?</p>",
      ["JLPT ning rasmiy manbasidan",
       "Bu darsdan", "Darslikdan", "Doʻstlardan"],
      "JLPT ning rasmiy manbasidan",
      f"<p><strong>Rasmiy manbadan.</strong> Sana, ariza "
      f"muddati va topshirish joyi har yili va har mamlakatda "
      f"oʻzgaradi — boshqa joydagi son eskirgan boʻlishi "
      f"mumkin.</p>"),

    q(f"<p>Kuniga ikki soat bir hafta, keyin bir oy tanaffus. "
      f"Bu qanday odam?</p>",
      [MIKKA, KEIZOKU, SHUUKAN, MOKUHYOU],
      MIKKA,
      f"<p><strong>{MIKKA}</strong> — PJ-98 dagi «uch kunlik "
      f"rohib». Uning davosi ham oʻsha darsda edi: "
      f"{CHIRIMO}.</p>"),

    # ── 13–18 BUTUN KURS boʻyicha takrorlash ─────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WATASHI}___"
      f"{GAKUSEI}です。</strong> (oʻzim haqimda xabar "
      f"beryapman)</p>",
      ["は", "が", "を", "に"],
      "は",
      f"<p><strong>は</strong> — mavzu (PJ-14). {WATASHI}が"
      f"{GAKUSEI}です boʻlsa, «talaba aynan men» degan "
      f"javob boʻlardi — savolga javob, oddiy xabar "
      f"emas.</p>"),

    q(f"<p>{YOMU} ning て-shakli qaysi?</p>",
      [YONDE, f"{r('読', 'よ')}みて", f"{r('読', 'よ')}んて",
       f"{r('読', 'よ')}って"],
      YONDE,
      f"<p><strong>{YONDE}</strong>. む bilan tugagan "
      f"{r('五段', 'ごだん')} feʼllar んで oladi (PJ-30) — "
      f"んて emas, って ham emas.</p>"),

    q(f"<p>Ustozingiz haqida: «ustoz ovqatlandi» — "
      f"{r('尊敬語', 'そんけいご')}da?</p>",
      [f"{MESHIAGARU}", f"{ITADAKU}", f"{TABERU}", f"{TABETE}"],
      f"{MESHIAGARU}",
      f"<p><strong>{MESHIAGARU}</strong> — {TABERU} ning "
      f"{r('尊敬語', 'そんけいご')} shakli (PJ-69). {ITADAKU} "
      f"esa {r('謙譲語', 'けんじょうご')} — u <em>oʻzingiz</em> "
      f"haqingizda ishlatiladi.</p>"),

    q(f"<p>{GAKUSEI}です — である{r('体', 'たい')}da?</p>",
      [f"{GAKUSEI}である", f"{GAKUSEI}だである",
       f"{GAKUSEI}であります", f"{GAKUSEI}でいる"],
      f"{GAKUSEI}である",
      f"<p><strong>{GAKUSEI}である</strong> (PJ-96). である "
      f"<strong>だ</strong> ning oʻrniga keladi, uning ustiga "
      f"emas. Feʼl va い-sifat esa umuman oʻzgarmaydi: "
      f"{OOKII} — {OOKII}.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KANJI_W}___、"
      f"ひらがなも{YOMENAI}。</strong> («kanji u yoqda tursin, "
      f"hiraganani ham oʻqiy olmaydi»)</p>",
      ["どころか", "ばかりか", "だけでなく", "どころで"],
      "どころか",
      f"<p><strong>どころか</strong> (PJ-94) — «u yoqda "
      f"tursin», kutilganni rad etadi. ばかりか va だけでなく "
      f"aksincha, qoʻshadi — ular bilan gap «ikkalasini ham "
      f"biladi» degan maʼno berardi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{TSUITA}とたん、{AME}が{FURIDASHITA}",
       f"{r('着', 'つ')}き{SHIDAI}、{AME}が{FURIDASHITA}",
       f"{TSUITA}とたん、{DENWA}してください",
       f"{r('着', 'つ')}く{SHIDAI}、{DENWA}します"],
      f"{TSUITA}とたん、{AME}が{FURIDASHITA}",
      f"<p><strong>{TSUITA}とたん</strong> (PJ-95): た-shakli, "
      f"oxiri oʻtgan zamon, voqea kutilmagan. {SHIDAI} esa "
      f"ます-oʻzagiga ulanadi va oʻtgan zamon bilan "
      f"kelmaydi.</p>"),

    # ── 19–20 qoʻllash ───────────────────────────────────────────────
    q("<p>Ertadan boshlab kundalik rejangiz qanday boʻladi?</p>",
      ["Har kuni: bir sahifa, oʻn daqiqa tinglash, oʻn soʻz, uchta gap",
       "Haftada bir kun, olti soat",
       "Faqat grammatika, oʻqishni keyinga qoldirib",
       "Faqat kanji roʻyxatini yodlash"],
      "Har kuni: bir sahifa, oʻn daqiqa tinglash, oʻn soʻz, uchta gap",
      f"<p><strong>Har kuni, toʻrtta ish.</strong> Kuniga bir "
      f"sahifa — yilda bir necha kitob. {MAINICHI}"
      f"{r('十分', 'じゅっぷん')}でも、{TSUZUKERU}ことが"
      f"{r('大切', 'たいせつ')}である。</p>"),

    q(f"<p>Tinglash sizga qiyin. Nima qilasiz?</p>",
      [f"Matnni audio bilan birga ovoz chiqarib oʻqiyman ({ONDOKU})",
       "Tinglashni keyinga qoldiraman",
       "Faqat oʻqishga eʼtibor beraman",
       "Audiosiz matnlarni tanlayman"],
      f"Matnni audio bilan birga ovoz chiqarib oʻqiyman ({ONDOKU})",
      f"<p><strong>{ONDOKU}</strong>. Va tinglashni keyinga "
      f"qoldirib boʻlmaydi: {KIJUNTEN} qoidasi har bir "
      f"boʻlimdan alohida eng kam ballni talab qiladi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-97 Mashq: Xat va rasmiy murojaat qoliplari",
        "tutorial":    "PJ-97:",
        "description": "拝啓↔敬具 juftligi, mavsum salomi va elektron "
                       "xatning oʻz qolipi — hamda 様 qayerga qoʻyilmasligi.",
        "questions":   Q_PJ97,
        **DEFAULTS,
    },
    {
        "title":       "PJ-98 Mashq: 四字熟語 va ことわざ",
        "tutorial":    "PJ-98:",
        "description": "Toʻrt belgili iboralar va maqollar — oʻzbekcha "
                       "juftlari, oʻqilishlari va qayerda ishlatilmasligi.",
        "questions":   Q_PJ98,
        **DEFAULTS,
    },
    {
        "title":       "PJ-99 Mashq: 和語・漢語・外来語",
        "tutorial":    "PJ-99:",
        "description": "Lugʻatning uch qatlami, oʻqilishdan qatlamni "
                       "aniqlash va 和製英語 tuzogʻi.",
        "questions":   Q_PJ99,
        **DEFAULTS,
    },
    {
        "title":       "PJ-100 Mashq: Yakuniy test va yoʻl xaritasi",
        "tutorial":    "PJ-100:",
        "description": "Kursning soʻnggi testi: yoʻl xaritasi faktlari "
                       "va butun 100 dars boʻyicha takrorlash.",
        "questions":   Q_PJ100,
        **DEFAULTS,
    },
]
