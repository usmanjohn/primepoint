# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-46 … PJ-48.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Batchning oʻqitish oʻqi bitta: と dan oldin OT va な-sifat **だ** ni
saqlaydi (PJ-46, PJ-47), OT dan oldin esa u **な / の** ga aylanadi
(PJ-48). Uchala test ham shu qarama-qarshilikni qaytadan bosadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_46_48.py --master=prime \\
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


# ── umumiy soʻzlar ───────────────────────────────────────────────────
OMOU   = r("思", "おも") + "う"
OMOIMASU = r("思", "おも") + "います"
OMOTTE = r("思", "おも") + "っています"
IU     = r("言", "い") + "う"
IIMASHITA = r("言", "い") + "いました"
ITTEIMASHITA = r("言", "い") + "っていました"
HANASU = r("話", "はな") + "す"
KIKU   = r("聞", "き") + "く"

IKU    = r("行", "い") + "く"
IKIMASU = r("行", "い") + "きます"
IKANAI = r("行", "い") + "かない"
ITTA   = r("行", "い") + "った"
KURU   = r("来", "く") + "る"
KONAI  = r("来", "こ") + "ない"
KITA   = r("来", "き") + "た"
KONAKATTA = r("来", "こ") + "なかった"
YOMU   = r("読", "よ") + "む"
YONDA  = r("読", "よ") + "んだ"
TSUKURU = r("作", "つく") + "る"
TSUKUTTA = r("作", "つく") + "った"
KATTA  = r("買", "か") + "った"
KARITA = r("借", "か") + "りた"
SAGASU = r("探", "さが") + "す"
KAERU  = r("帰", "かえ") + "る"
KAETTA = r("帰", "かえ") + "った"
YASUMU = r("休", "やす") + "む"
OWATTA = r("終", "お") + "わった"
FURU   = r("降", "ふ") + "る"
FUTTA  = r("降", "ふ") + "った"

TAKAI  = r("高", "たか") + "い"
YASUI  = r("安", "やす") + "い"
OMOSHIROI = r("面白", "おもしろ") + "い"
MUZUKASHII = r("難", "むずか") + "しい"
ISOGASHII = r("忙", "いそが") + "しい"
ATSUI  = r("暑", "あつ") + "い"

SHIZUKA = r("静", "しず") + "か"
GENKI   = r("元気", "げんき")
DAIJOBU = r("大丈夫", "だいじょうぶ")
BENRI   = r("便利", "べんり")

GAKUSEI = r("学生", "がくせい")
SENSEI  = r("先生", "せんせい")
HON     = r("本", "ほん")
HEYA    = r("部屋", "へや")
HITO    = r("人", "ひと")
RYOURI  = r("料理", "りょうり")
ASHITA  = r("明日", "あした")
KINOU   = r("昨日", "きのう")
KYOU    = r("今日", "きょう")
AME     = r("雨", "あめ")
SHIKEN  = r("試験", "しけん")
EIGA    = r("映画", "えいが")
HAHA    = r("母", "はは")
WATASHI = r("私", "わたし")
NIHONGO = r("日本語", "にほんご")
TOSHOKAN = r("図書館", "としょかん")
JITENSHA = r("自転車", "じてんしゃ")
DARE    = r("誰", "だれ")
KOTOBA  = r("言葉", "ことば")
JIKAN   = r("時間", "じかん")
HANASERU = r("話", "はな") + "せる"
SAGASHITE = r("探", "さが") + "しています"
FUTSUTAI = r("普通体", "ふつうたい")


# ══════════════════════════════════════════════════════════════════════
# PJ-46 — 〜と思います
# ══════════════════════════════════════════════════════════════════════
Q_PJ46 = [
    # 1–5 tanish
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ASHITA}{AME}が{FURU}___{OMOIMASU}。</strong></p>",
      ["と", "を", "が", "で"],
      "と",
      f"<p><strong>と</strong> — «deb». U oʻzidan oldingi butun gapni "
      f"olib, uni {OMOU} feʼlining toʻldiruvchisiga aylantiradi. "
      f"Oʻzbekchada ham «yomgʻir yogʻadi <em>deb</em> oʻylayman».</p>"),

    q(f"<p>«{IKIMASU}» ni 〜と{OMOIMASU} qolipiga qoʻying.</p>",
      [f"{IKU}と{OMOIMASU}", f"{IKIMASU}と{OMOIMASU}",
       f"{IKU}だと{OMOIMASU}", f"{IKIMASU}だと{OMOIMASU}"],
      f"{IKU}と{OMOIMASU}",
      f"<p>と dan oldin <strong>doim oddiy shakl</strong> turadi. "
      f"です・ます gapning eng oxirida — {OMOIMASU} da — koʻrinadi, "
      f"ichkarida emas.</p>"),

    q(f"<p>Toʻgʻri javobni tanlang.</p><p><strong>この{HON}は{OMOSHIROI}___{OMOIMASU}。</strong></p>",
      ["と", "だと", "なと", "のと"],
      "と",
      f"<p>{OMOSHIROI} — <strong>い-sifat</strong>, unga だ qoʻshilmaydi. "
      f"い-sifat oʻzi kesim boʻla oladi, boglama kerak emas.</p>"),

    q(f"<p>Toʻgʻri javobni tanlang.</p><p><strong>この{HEYA}は{SHIZUKA}___{OMOIMASU}。</strong></p>",
      ["だと", "と", "なと", "いと"],
      "だと",
      f"<p>{SHIZUKA} — <strong>な-sifat</strong>, demak と oldida "
      f"<strong>だ</strong> saqlanadi. «な» faqat otdan oldin "
      f"chiqadi.</p>"),

    q(f"<p>Toʻgʻri javobni tanlang.</p><p><strong>イノムさんは{GAKUSEI}___{OMOIMASU}。</strong></p>",
      ["だと", "と", "のと", "でと"],
      "だと",
      f"<p>Ot ham な-sifat kabi <strong>だ</strong> oladi. と dan oldin "
      f"だ hech qachon tushmaydi — u yerda u muloyimlik emas, "
      f"<em>yopishtiruvchi</em>.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Kecha yomgʻir yoqqan deb oʻylayman» qaysi?</p>",
      [f"{KINOU}{AME}が{FUTTA}と{OMOIMASU}",
       f"{KINOU}{AME}が{FURU}と{OMOIMASU}",
       f"{KINOU}{AME}が{FUTTA}と{OMOU}ました",
       f"{KINOU}{AME}が{FURU}と{OMOIMASU}でした"],
      f"{KINOU}{AME}が{FUTTA}と{OMOIMASU}",
      f"<p>Ichkaridagi zamon <strong>mustaqil</strong>: voqea oʻtgan "
      f"zamonda ({FUTTA}), oʻylash esa hozir ({OMOIMASU}).</p>"),

    q(f"<p>«{SHIKEN}は{MUZUKASHII}くなかったです» ni fikrga aylantiring.</p>",
      [f"{SHIKEN}は{MUZUKASHII}くなかったと{OMOIMASU}",
       f"{SHIKEN}は{MUZUKASHII}くなかったですと{OMOIMASU}",
       f"{SHIKEN}は{MUZUKASHII}くないだったと{OMOIMASU}",
       f"{SHIKEN}は{MUZUKASHII}くなかっただと{OMOIMASU}"],
      f"{SHIKEN}は{MUZUKASHII}くなかったと{OMOIMASU}",
      f"<p>い-sifatning oʻtgan zamon inkori — <strong>くなかった</strong> "
      f"(PJ-45). です tushadi va だ qoʻshilmaydi.</p>"),

    q(f"<p>«Menimcha u kelmaydi» — eng tabiiy shakl qaysi?</p>",
      [f"{KONAI}と{OMOIMASU}", f"{KURU}と{OMOU}ません",
       f"{KONAI}と{OMOU}ません", f"{KURU}と{OMOIMASU}"],
      f"{KONAI}と{OMOIMASU}",
      f"<p>Inkor <strong>ichkarida</strong> turadi. "
      f"«{KURU}と{OMOU}ません» ham grammatik jihatdan toʻgʻri, lekin u "
      f"«keladi deb oʻylamayman» — birovning gapiga eʼtirozdek "
      f"eshitiladi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>この{EIGA}について___{OMOIMASU}か。</strong></p>",
      ["どう", "なに", "どこ", "だれ"],
      "どう",
      f"<p>Fikr «nima» emas, <strong>«qanday»</strong> boʻladi: "
      f"どう{OMOIMASU}か. «{r('何','なに')}を{OMOIMASU}か» deyilmaydi.</p>"),

    q(f"<p>«パリさんは{r('日本','にほん')}へ{r('行','い')}きたい» — buni toʻgʻri xabar qiling.</p>",
      [f"パリさんは{r('日本','にほん')}へ{r('行','い')}きたいと{OMOTTE}",
       f"パリさんは{r('日本','にほん')}へ{r('行','い')}きたいと{OMOIMASU}",
       f"パリさんは{r('日本','にほん')}へ{r('行','い')}きたいですと{OMOIMASU}",
       f"パリさんは{r('日本','にほん')}へ{r('行','い')}きたいだと{OMOIMASU}"],
      f"パリさんは{r('日本','にほん')}へ{r('行','い')}きたいと{OMOTTE}",
      f"<p>Bu <strong>boshqa odamning</strong> fikri, shuning uchun "
      f"{OMOTTE} kerak. Siz birovning miyasiga kira olmaysiz — faqat "
      f"uning turgan holatini aytasiz.</p>"),

    q(f"<p>«{BENRI}です» ni fikrga aylantiring.</p>",
      [f"{BENRI}だと{OMOIMASU}", f"{BENRI}と{OMOIMASU}",
       f"{BENRI}なと{OMOIMASU}", f"{BENRI}いと{OMOIMASU}"],
      f"{BENRI}だと{OMOIMASU}",
      f"<p>{BENRI} — な-sifat («qulay»), demak <strong>だ</strong>. "
      f"Tekshirishning oson yoʻli: soʻz い bilan tugamasa, koʻpincha "
      f"な-sifat.</p>"),

    q(f"<p>{OMOU} va {r('考','かんが')}える — qaysi biri «hisoblab, "
      f"rejalashtirib oʻylash»?</p>",
      [f"{r('考','かんが')}える", OMOU, "Ikkalasi bir xil",
       "Ikkalasi ham faqat fikr bildiradi"],
      f"{r('考','かんが')}える",
      f"<p><strong>{r('考','かんが')}える</strong> — boshda qilingan ish: "
      f"hisoblash, rejalashtirish. {OMOU} esa yurakdan chiqqan fikr yoki "
      f"taxmin. «Ikki kun oʻylab koʻraman» — {r('考','かんが')}える.</p>"),

    # 13–16 farqlash
    q(f"<p>Qaysi qatorda だ KERAK?</p>",
      [f"{GENKI} + と{OMOIMASU}", f"{TAKAI} + と{OMOIMASU}",
       f"{YASUI} + と{OMOIMASU}", f"{ISOGASHII} + と{OMOIMASU}"],
      f"{GENKI} + と{OMOIMASU}",
      f"<p>{GENKI} — <strong>な-sifat</strong>, qolgan uchtasi い-sifat. "
      f"い bilan tugagan sifatga だ hech qachon qoʻshilmaydi.</p>"),

    q(f"<p>«{IKANAI}と{OMOIMASU}» va «{IKU}と{OMOU}ません» — farqi nima?</p>",
      ["Birinchisi yumshoq taxmin, ikkinchisi eʼtirozdek qatʼiy",
       "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
       "Birinchisi muloyim, ikkinchisi oddiy shakl",
       "Farqi yoʻq, ikkalasi bir xil"],
      "Birinchisi yumshoq taxmin, ikkinchisi eʼtirozdek qatʼiy",
      f"<p>Inkorning joyi maʼnoni oʻzgartiradi. Oʻzbekchada ham "
      f"«bormaydi deb oʻylayman» va «boradi deb oʻylamayman» bir xil "
      f"emas — ikkinchisi birovning gapiga qarshi turadi.</p>"),

    q(f"<p>Qachon {OMOTTE} ishlatiladi?</p>",
      ["Boshqa odamning fikrini aytganda",
       "Oʻz fikrini aytganda", "Oʻtgan zamonda", "Savol berganda"],
      "Boshqa odamning fikrini aytganda",
      f"<p>{OMOTTE} — «u shunday fikrda turibdi», yaʼni siz koʻrgan "
      f"<strong>holat</strong>. Oʻz fikringiz uchun oddiy "
      f"{OMOIMASU}.</p>"),

    q(f"<p>Qaysi soʻz turi と oldida <strong>hech qachon</strong> だ "
      f"olmaydi?</p>",
      ["い-sifat", "な-sifat", "Ot", "Feʼl oddiy shakli"],
      "い-sifat",
      f"<p>«{TAKAI}だと» notoʻgʻri. Feʼl ham だ olmaydi, lekin u allaqachon "
      f"kesim — savol sifat va otlar haqida: uchtadan faqat "
      f"<strong>い-sifat</strong> quruq qoladi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{GAKUSEI}と{OMOIMASU}", f"{GAKUSEI}だと{OMOIMASU}",
       f"{TAKAI}と{OMOIMASU}", f"{SHIZUKA}だと{OMOIMASU}"],
      f"{GAKUSEI}と{OMOIMASU}",
      f"<p>Otga <strong>だ</strong> kerak: {GAKUSEI}だと{OMOIMASU}. "
      f"Qolgan uchtasi toʻgʻri.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{KONAKATTA}と{OMOIMASU}", f"{KURU}ませんでしたと{OMOIMASU}",
       f"{KONAI}でしたと{OMOIMASU}", f"{KONAI}だったと{OMOIMASU}"],
      f"{KONAKATTA}と{OMOIMASU}",
      f"<p>Oddiy shaklning oʻtgan zamon inkori — "
      f"<strong>{KONAKATTA}</strong>. ない い-sifat boʻlgani uchun "
      f"い → かった (PJ-45); だった esa otlarniki.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{OMOIMASU} · と · {ATSUI} · {ASHITA}は</strong></p>",
      [f"{ASHITA}は{ATSUI}と{OMOIMASU}", f"{ASHITA}は{OMOIMASU}と{ATSUI}",
       f"{OMOIMASU}{ASHITA}は{ATSUI}と", f"{ATSUI}{ASHITA}はと{OMOIMASU}"],
      f"{ASHITA}は{ATSUI}と{OMOIMASU}",
      f"<p>Fikr avval, «deb oʻylayman» keyin — oʻzbekchadagi tartibning "
      f"aynan oʻzi. {ATSUI} い-sifat boʻlgani uchun だ yoʻq.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> この{HON}はどうですか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"とても{OMOSHIROI}と{OMOIMASU}。", f"とても{OMOSHIROI}だと{OMOIMASU}。",
       f"とても{OMOSHIROI}ですと{OMOIMASU}。", f"とても{OMOSHIROI}と{OMOTTE}。"],
      f"とても{OMOSHIROI}と{OMOIMASU}。",
      f"<p>{OMOSHIROI} — い-sifat, demak だ ham です ham qoʻshilmaydi. "
      f"Va bu <em>oʻz</em> fikri, shuning uchun {OMOTTE} emas, "
      f"oddiy {OMOIMASU}.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-47 — 〜と言いました
# ══════════════════════════════════════════════════════════════════════
Q_PJ47 = [
    # 1–5 tanish
    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>ラノさんは「{ASHITA}{IKIMASU}」___{IIMASHITA}。</strong></p>",
      ["と", "を", "が", "で"],
      "と",
      f"<p><strong>と</strong> — oʻsha «deb». U 「」 dan keyin ham, oddiy "
      f"shakldan keyin ham bir xil ishlaydi.</p>"),

    q(f"<p>Qaysi tinish belgisi yaponcha qoʻshtirnoq?</p>",
      ["「」", "«»", "\"\"", "''"],
      "「」",
      f"<p><strong>「」</strong> — {r('鉤括弧','かぎかっこ')}. Yapon matnida "
      f"boshqa qoʻshtirnoq ishlatilmaydi.</p>"),

    q(f"<p>«「{ASHITA}{IKIMASU}」と{IIMASHITA}» ni oʻzlashtirilgan gapga "
      f"aylantiring.</p>",
      [f"{ASHITA}{IKU}と{IIMASHITA}", f"{ASHITA}{IKIMASU}と{IIMASHITA}",
       f"{ASHITA}{ITTA}と{IIMASHITA}", f"{ASHITA}{IKU}だと{IIMASHITA}"],
      f"{ASHITA}{IKU}と{IIMASHITA}",
      f"<p>「」 tushadi va ichkarisi <strong>oddiy shaklga</strong> "
      f"oʻtadi. Zamon esa oʻzgarmaydi — {ASHITA} bilan {ITTA} "
      f"turolmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>イノムさんは{HAHA}___「ありがとう」と{IIMASHITA}。</strong></p>",
      ["に", "を", "で", "へ"],
      "に",
      f"<p>Eshituvchi <strong>に</strong> oladi — oʻzbekcha «-ga» "
      f"(PJ-21). «{HAHA}を{IIMASHITA}» notoʻgʻri.</p>"),

    q(f"<p>Toʻgʻri javobni tanlang.</p>"
      f"<p><strong>{SENSEI}は{DAIJOBU}___{IIMASHITA}。</strong></p>",
      ["だと", "と", "なと", "のと"],
      "だと",
      f"<p>{DAIJOBU} — <strong>な-sifat</strong>, demak と oldida "
      f"だ saqlanadi. Qoida PJ-46 dagining aynan oʻzi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Pari ertaga kelaman dedi» qaysi?</p>",
      [f"パリさんは{ASHITA}{KURU}と{IIMASHITA}",
       f"パリさんは{ASHITA}{KITA}と{IIMASHITA}",
       f"パリさんは{ASHITA}{KURU}ますと{IIMASHITA}",
       f"パリさんは{ASHITA}{KITA}と{IU}ました"],
      f"パリさんは{ASHITA}{KURU}と{IIMASHITA}",
      f"<p>Zamon <strong>siljimaydi</strong>: u gapirganda «kelish» hali "
      f"oldinda edi, shuning uchun ichkarida {KURU}. Oʻzbekchada ham "
      f"«kelaman dedi».</p>"),

    q(f"<p>Nima xato?</p><p><strong>{SENSEI}は{SHIKEN}が{OWATTA}と"
      f"{IU}ましたです。</strong></p>",
      [f"Gap oxiri notoʻgʻri — {IIMASHITA} boʻlishi kerak",
       f"{OWATTA} oʻrniga {r('終','お')}わりました boʻlishi kerak",
       "と oʻrniga を boʻlishi kerak",
       f"{SHIKEN}が oʻrniga {SHIKEN}は boʻlishi kerak"],
      f"Gap oxiri notoʻgʻri — {IIMASHITA} boʻlishi kerak",
      f"<p>«ましたです» degan shakl yoʻq. Ichkarisi ({OWATTA}) esa "
      f"toʻgʻri — u oddiy shaklda turishi kerak.</p>"),

    q(f"<p>«Rano bugun kelmayman degan edi» — eng tabiiy shakl qaysi?</p>",
      [f"ラノさんは{KYOU}{KONAI}と{ITTEIMASHITA}",
       f"ラノさんは{KYOU}{KONAI}と{IIMASHITA}",
       f"ラノさんは{KYOU}{r('来','き')}ませんと{IIMASHITA}",
       f"ラノさんは{KYOU}{KONAKATTA}と{ITTEIMASHITA}"],
      f"ラノさんは{KYOU}{KONAI}と{ITTEIMASHITA}",
      f"<p><strong>{ITTEIMASHITA}</strong> — eshitganingizni boshqaga "
      f"yetkazyapsiz. {IIMASHITA} ham xato emas, lekin xabar "
      f"yetkazishda ています tabiiyroq.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>ムニラさんは「すみません、{JIKAN}がありません」___"
      f"{IIMASHITA}。</strong></p>",
      ["と", "だと", "って", "を"],
      "と",
      f"<p>「」 ichi tegilmaydi va undan keyin <strong>と</strong> "
      f"keladi. って ham shu maʼnoni beradi, lekin u ogʻzaki nutqniki — "
      f"yozma matnda と.</p>"),

    q(f"<p>Qaysi feʼl と bilan ishlay olMAYDI?</p>",
      [f"{r('食','た')}べる", IU, KIKU, OMOU],
      f"{r('食','た')}べる",
      f"<p>と <strong>soʻz yoki fikr</strong> bilan ishlaydigan feʼllar "
      f"oldida turadi: {IU}, {KIKU}, {OMOU}, {r('書','か')}く. "
      f"«Yemoq» ularning biri emas.</p>"),

    q(f"<p>«{ISOGASHII}» ni oʻzlashtirilgan gapga qoʻying.</p>",
      [f"{ISOGASHII}と{IIMASHITA}", f"{ISOGASHII}だと{IIMASHITA}",
       f"{ISOGASHII}ですと{IIMASHITA}", f"{ISOGASHII}なと{IIMASHITA}"],
      f"{ISOGASHII}と{IIMASHITA}",
      f"<p>{ISOGASHII} — い-sifat, demak だ yoʻq. Uch soʻz turidan "
      f"faqat い-sifat quruq turadi.</p>"),

    q(f"<p>{IU} va {HANASU} — farqi nima?</p>",
      [f"{IU} ning toʻldiruvchisi soʻz, {HANASU} niki mavzu",
       f"{IU} muloyimroq", f"{HANASU} faqat oʻtgan zamonda ishlatiladi",
       "Farqi yoʻq"],
      f"{IU} ning toʻldiruvchisi soʻz, {HANASU} niki mavzu",
      f"<p>«Shunday dedi» — {IU}. «Yapon tilida gapiradi», «voqeani "
      f"gapirib berdi» — {HANASU}. Oʻzbekchada ham «gap aytdi» va "
      f"«gaplashdi» bir narsa emas.</p>"),

    # 13–16 farqlash
    q(f"<p>«ラノさんは「{ASHITA}{IKIMASU}」と{IIMASHITA}» — nega ichkarisi "
      f"{IKIMASU}?</p>",
      ["Chunki 「」 ichida odamning oʻz uslubi saqlanadi",
       "Chunki ラノさん muloyim odam", "Chunki bu kelasi zamon",
       "Chunki と dan oldin doim ます turadi"],
      "Chunki 「」 ichida odamning oʻz uslubi saqlanadi",
      f"<p>Koʻchirma gapda siz hech narsani tuzatmaysiz — muloyimligi, "
      f"か si, hammasi qanday aytilgan boʻlsa shundayligicha qoladi. "
      f"「」 siz yozsangiz esa oddiy shakl kerak boʻladi.</p>"),

    q(f"<p>Qaysi qolip «u <em>aynan shu soʻzlarni</em> aytdi» degan "
      f"maʼnoni beradi?</p>",
      [f"「」 + と + {IIMASHITA}", f"Oddiy shakl + と + {IIMASHITA}",
       "Oddiy shakl + って", "「」 + って"],
      f"「」 + と + {IIMASHITA}",
      f"<p><strong>{r('直接話法','ちょくせつわほう')}</strong> — koʻchirma "
      f"gap. 「」 siz shakl esa mazmunni qaytaradi, soʻzlarni emas.</p>"),

    q(f"<p>って nima?</p>",
      ["Ogʻzaki nutqdagi と", "と ning oʻtgan zamoni",
       "Savol qoʻshimchasi", "Koʻplik qoʻshimchasi"],
      "Ogʻzaki nutqdagi と",
      f"<p>Maʼnosi と bilan bir xil, faqat uslubi oddiy. Animeda va "
      f"suhbatda koʻp uchraydi; yozma ishda va ustoz bilan esa doim "
      f"<strong>と</strong>.</p>"),

    q(f"<p>Qaysi gapda zamon xato qoʻyilgan?</p>",
      [f"{ASHITA}{KITA}と{IIMASHITA}", f"{ASHITA}{KURU}と{IIMASHITA}",
       f"{KINOU}{KITA}と{IIMASHITA}", f"{KYOU}{YASUMU}と{IIMASHITA}"],
      f"{ASHITA}{KITA}と{IIMASHITA}",
      f"<p>{ASHITA} («ertaga») bilan oʻtgan zamon turolmaydi. "
      f"Toʻgʻrisi — <strong>{ASHITA}{KURU}と{IIMASHITA}</strong>.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{GENKI}と{IIMASHITA}", f"{GENKI}だと{IIMASHITA}",
       f"{TAKAI}と{IIMASHITA}", f"{GAKUSEI}だと{IIMASHITA}"],
      f"{GENKI}と{IIMASHITA}",
      f"<p>{GENKI} — な-sifat, demak <strong>だ</strong> kerak. "
      f"{TAKAI} い-sifat boʻlgani uchun u だ siz toʻgʻri.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WATASHI}に「ありがとう」と{IIMASHITA}",
       f"{WATASHI}を「ありがとう」と{IIMASHITA}",
       f"{WATASHI}で「ありがとう」と{IIMASHITA}",
       f"{WATASHI}が「ありがとう」を{IIMASHITA}"],
      f"{WATASHI}に「ありがとう」と{IIMASHITA}",
      f"<p>Eshituvchi <strong>に</strong>, gap esa <strong>と</strong> "
      f"oladi. Bu ikki qoʻshimcha oʻrin almashmaydi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{IIMASHITA} · と · {YASUMU} · {ASHITA} · パリさんは</strong></p>",
      [f"パリさんは{ASHITA}{YASUMU}と{IIMASHITA}",
       f"パリさんは{IIMASHITA}と{ASHITA}{YASUMU}",
       f"{ASHITA}パリさんは{IIMASHITA}{YASUMU}と",
       f"パリさんは{YASUMU}{ASHITA}と{IIMASHITA}"],
      f"パリさんは{ASHITA}{YASUMU}と{IIMASHITA}",
      f"<p>Kim aytgani — boshda, aytgan gapi — oʻrtada, "
      f"{IIMASHITA} — oxirida. Yapon gapi doim feʼl bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> ラノさんは{KYOU}{r('来','き')}ますか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{KONAI}と{ITTEIMASHITA}よ。", f"{KONAI}ですと{ITTEIMASHITA}よ。",
       f"{KONAI}だと{ITTEIMASHITA}よ。", f"{KURU}ませんと{IIMASHITA}よ。"],
      f"{KONAI}と{ITTEIMASHITA}よ。",
      f"<p>Inom eshitganini yetkazyapti — <strong>{ITTEIMASHITA}</strong>. "
      f"Ichkarisi oddiy shaklda ({KONAI}), feʼl boʻlgani uchun "
      f"だ olmaydi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-48 — Aniqlovchi ergash gap
# ══════════════════════════════════════════════════════════════════════
Q_PJ48 = [
    # 1–5 tanish
    q(f"<p>«Men oʻqigan kitob» qaysi?</p>",
      [f"{WATASHI}が{YONDA}{HON}", f"{HON}が{WATASHI}{YONDA}",
       f"{WATASHI}が{HON}{YONDA}", f"{HON}を{WATASHI}が{YONDA}"],
      f"{WATASHI}が{YONDA}{HON}",
      f"<p>Aniqlovchi <strong>otdan oldin</strong> turadi — "
      f"oʻzbekchadagi «men oʻqi<em>gan</em> kitob» bilan bir xil "
      f"tartib.</p>"),

    q(f"<p>Aniqlovchi ergash gapning feʼli qaysi shaklda turadi?</p>",
      [f"Oddiy shaklda ({FUTSUTAI})", "ます shaklida", "て shaklida",
       "Potensial shaklda"],
      f"Oddiy shaklda ({FUTSUTAI})",
      f"<p>Otdan oldin <strong>faqat oddiy shakl</strong> turadi: "
      f"{YONDA}{HON} ✓, {r('読','よ')}みました{HON} ✗.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>ラノさん___{TSUKUTTA}{RYOURI}はおいしいです。</strong></p>",
      ["が", "は", "を", "で"],
      "が",
      f"<p>Ergash gap ichidagi ega <strong>が</strong> oladi. は — butun "
      f"gapning mavzusini koʻrsatadi (PJ-14), ergash gap esa mavzu "
      f"qoʻyiladigan joy emas.</p>"),

    q(f"<p>«{SHIZUKA}» ni {HEYA} ga ulang.</p>",
      [f"{SHIZUKA}な{HEYA}", f"{SHIZUKA}だ{HEYA}",
       f"{SHIZUKA}の{HEYA}", f"{SHIZUKA}い{HEYA}"],
      f"{SHIZUKA}な{HEYA}",
      f"<p>Otdan oldin な-sifat <strong>な</strong> kiyadi. Aynan "
      f"shuning uchun u «な-sifat» deb ataladi.</p>"),

    q(f"<p>Yaponchada aniqlovchi gapni otga ulaydigan soʻz bormi?</p>",
      ["Yoʻq, ular shunchaki yonma-yon turadi",
       "Ha — の", "Ha — と", "Ha — が"],
      "Yoʻq, ular shunchaki yonma-yon turadi",
      f"<p>Yapon tilida ergash gapni otga ulaydigan bogʻlovchi olmosh "
      f"yoʻq va vergul "
      f"ham qoʻyilmaydi. Gap otga <strong>yopishib</strong> turadi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Inom sotib olgan velosiped» qaysi?</p>",
      [f"イノムさんが{KATTA}{JITENSHA}", f"イノムさんは{KATTA}{JITENSHA}",
       f"イノムさんが{r('買','か')}いました{JITENSHA}",
       f"{JITENSHA}がイノムさん{KATTA}"],
      f"イノムさんが{KATTA}{JITENSHA}",
      f"<p>Ega <strong>が</strong>, feʼl <strong>oddiy shaklda</strong>, "
      f"ot oxirida. Uchala qoida bitta gapda.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>{NIHONGO}が{HANASERU}{HITO}___{SAGASHITE}。</strong></p>",
      ["を", "が", "に", "で"],
      "を",
      f"<p>«Aniqlovchi + ot» butunligicha <strong>bitta ot</strong>, "
      f"demak u odatdagidek を oladi: «gapira oladigan odamni "
      f"qidiryapman».</p>"),

    q(f"<p>«{KINOU}ムニラさんが{TOSHOKAN}で{KARITA}{HON}» ni tarjima "
      f"qiling.</p>",
      ["Kecha Munira kutubxonadan olgan kitob",
       "Munira kecha kutubxonaga bergan kitob",
       "Kitobni kecha kutubxonada Munira oʻqidi",
       "Munira kutubxonadan kitob olmoqchi"],
      "Kecha Munira kutubxonadan olgan kitob",
      f"<p>Oxiridan boshlab oʻqing: {HON} → {KARITA} → {TOSHOKAN}で → "
      f"ムニラさんが → {KINOU}. Uzun aniqlovchini shunday yechish "
      f"kerak.</p>"),

    q(f"<p>«Ertaga keladigan odam» qaysi?</p>",
      [f"{ASHITA}{KURU}{HITO}", f"{ASHITA}{KITA}{HITO}",
       f"{ASHITA}{KURU}ます{HITO}", f"{ASHITA}{KURU}の{HITO}"],
      f"{ASHITA}{KURU}{HITO}",
      f"<p>Ichkaridagi zamon <strong>otga nisbatan</strong> oʻlchanadi: "
      f"ish hali boʻlmagan — demak {KURU}. «Kecha kelgan odam» esa "
      f"{KINOU}{KITA}{HITO}.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>{NIHONGO}___{SENSEI}はやさしいです。</strong></p>",
      ["の", "だ", "な", "が"],
      "の",
      f"<p>Ot otni aniqlaganda <strong>の</strong> ishlatiladi (PJ-17). "
      f"だ faqat と oldida chiqadi, な esa な-sifatlarniki.</p>"),

    q(f"<p>«Men oʻqimaydigan kitob» qaysi?</p>",
      [f"{WATASHI}が{r('読','よ')}まない{HON}",
       f"{WATASHI}が{r('読','よ')}みません{HON}",
       f"{WATASHI}は{r('読','よ')}まない{HON}",
       f"{WATASHI}が{r('読','よ')}まないの{HON}"],
      f"{WATASHI}が{r('読','よ')}まない{HON}",
      f"<p>Inkor ham oddiy shaklda — ない-shakli (PJ-34) toʻgʻridan-toʻgʻri "
      f"otning oldiga turaveradi. Ega esa が oladi.</p>"),

    q(f"<p>«{WATASHI}の{TSUKUTTA}{RYOURI}» — bu toʻgʻrimi?</p>",
      ["Ha — ergash gapda が oʻrniga の ham kela oladi",
       "Yoʻq, の umuman ishlatilmaydi",
       "Ha, lekin maʼnosi «taomning egasi» boʻladi",
       "Yoʻq, faqat は toʻgʻri"],
      "Ha — ergash gapda が oʻrniga の ham kela oladi",
      f"<p>Maʼnosi {WATASHI}が{TSUKUTTA}{RYOURI} bilan bir xil, faqat "
      f"biroz kitobiyroq ohang. Yozganda が ni ishlating, "
      f"の ni esa tanib oling.</p>"),

    # 13–16 farqlash
    q(f"<p>{SHIZUKA} soʻzi と oldida va OT oldida qanday koʻrinadi?</p>",
      [f"と oldida {SHIZUKA}だ, ot oldida {SHIZUKA}な",
       f"Ikkalasida ham {SHIZUKA}だ",
       f"Ikkalasida ham {SHIZUKA}な",
       f"と oldida {SHIZUKA}な, ot oldida {SHIZUKA}だ"],
      f"と oldida {SHIZUKA}だ, ot oldida {SHIZUKA}な",
      f"<p>Bitta boglama, ikki kiyim: <strong>{SHIZUKA}だと"
      f"{OMOIMASU}</strong> va <strong>{SHIZUKA}な{HEYA}</strong>. "
      f"Bu batchning asosiy qarama-qarshiligi.</p>"),

    q(f"<p>Nega ergash gap ichida は ishlatilmaydi?</p>",
      ["Chunki は butun gapning mavzusini koʻrsatadi, ergash gapda esa mavzu boʻlmaydi",
       "Chunki は juda rasmiy", "Chunki は faqat feʼllar bilan keladi",
       "Chunki は oʻtgan zamonda ishlatilmaydi"],
      "Chunki は butun gapning mavzusini koʻrsatadi, ergash gapda esa mavzu boʻlmaydi",
      f"<p>PJ-14 ning qoidasi shu yerda ishlaydi. Ergash gapda faqat "
      f"<strong>ega</strong> bor, ega esa が oladi.</p>"),

    q(f"<p>Uzun aniqlovchini oʻqishni qayerdan boshlash kerak?</p>",
      ["Oxiridagi otdan — keyin chapga qarab",
       "Boshidagi soʻzdan — keyin oʻngga qarab",
       "Gapning eng oxirgi feʼlidan",
       "が qoʻshimchasidan"],
      "Oxiridagi otdan — keyin chapga qarab",
      f"<p>Avval aniqlanayotgan otni toping, keyin undan chapdagi "
      f"birinchi oddiy shakldagi feʼlni — u ergash gapning kesimi. "
      f"Shundan keyin gap oʻzi yechiladi.</p>"),

    q(f"<p>«Aniqlovchi + ot» birikmasi gapda qanday yashaydi?</p>",
      ["Oddiy otdek — を, が, に, は hammasini ola oladi",
       "Faqat ega boʻla oladi", "Faqat を oladi",
       "Hech qanday qoʻshimcha olmaydi"],
      "Oddiy otdek — を, が, に, は hammasini ola oladi",
      f"<p>Ichida nechta soʻz borligi muhim emas: u <strong>bitta "
      f"ot boʻlagi</strong>. Muhimi — qayerda tugashi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{WATASHI}は{YONDA}{HON}", f"{WATASHI}が{YONDA}{HON}",
       f"{SHIZUKA}な{HEYA}", f"{NIHONGO}の{SENSEI}"],
      f"{WATASHI}は{YONDA}{HON}",
      f"<p>Ergash gap ichida <strong>は turolmaydi</strong>. Toʻgʻrisi — "
      f"{WATASHI}が{YONDA}{HON}.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"ムニラさんが{TSUKUTTA}{RYOURI}を{r('食','た')}べました",
       f"ムニラさんが{r('作','つく')}りました{RYOURI}を{r('食','た')}べました",
       f"ムニラさんが{TSUKUTTA}、{RYOURI}を{r('食','た')}べました",
       f"ムニラさんは{TSUKUTTA}{RYOURI}を{r('食','た')}べました"],
      f"ムニラさんが{TSUKUTTA}{RYOURI}を{r('食','た')}べました",
      f"<p>Oddiy shakl, vergulsiz, ega が bilan. Uchala xato — ました, "
      f"vergul va は — qolgan variantlarda bittadan.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{HON} · {KINOU} · {KATTA} · を · {r('読','よ')}みました</strong></p>",
      [f"{KINOU}{KATTA}{HON}を{r('読','よ')}みました",
       f"{KINOU}{HON}を{KATTA}{r('読','よ')}みました",
       f"{HON}を{KINOU}{KATTA}{r('読','よ')}みました",
       f"{KATTA}{HON}{KINOU}を{r('読','よ')}みました"],
      f"{KINOU}{KATTA}{HON}を{r('読','よ')}みました",
      f"<p>«{KINOU}{KATTA}{HON}» butunligicha bitta ot boʻlagi, keyin "
      f"を, keyin feʼl. Yapon gapi doim feʼl bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ラノ:</strong> {DARE}が{TSUKUTTA}{RYOURI}ですか。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"{WATASHI}が{TSUKUTTA}{RYOURI}です。",
       f"{WATASHI}は{TSUKUTTA}{RYOURI}です。",
       f"{WATASHI}が{r('作','つく')}りました{RYOURI}です。",
       f"{WATASHI}の{TSUKUTTA}です{RYOURI}。"],
      f"{WATASHI}が{TSUKUTTA}{RYOURI}です。",
      f"<p>Savolda ham javobda ham ega <strong>が</strong> oladi — bu "
      f"ergash gapning ichi. です esa faqat gapning eng oxirida.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-46 Mashq: 〜と思います",
        "tutorial":    "PJ-46:",
        "description": "Fikr gap oxirida turadi. と dan oldin oddiy shakl, "
                       "va ot bilan な-sifat だ ni saqlaydi.",
        "questions":   Q_PJ46,
        **DEFAULTS,
    },
    {
        "title":       "PJ-47 Mashq: 〜と言いました va koʻchirma gap",
        "tutorial":    "PJ-47:",
        "description": "「」 bilan aynan, 「」 siz mazmunan. Va eng muhimi — "
                       "zamon siljimaydi.",
        "questions":   Q_PJ47,
        **DEFAULTS,
    },
    {
        "title":       "PJ-48 Mashq: Aniqlovchi ergash gap",
        "tutorial":    "PJ-48:",
        "description": "Gap ham sifat kabi otdan oldin turadi. Ichkaridagi "
                       "ega が oladi, だ esa な / の ga aylanadi.",
        "questions":   Q_PJ48,
        **DEFAULTS,
    },
]
