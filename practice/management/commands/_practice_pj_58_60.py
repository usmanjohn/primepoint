# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-58 … PJ-60.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchda uch narsa jim sinadi:
  * て-shakli (yana) — chunki uchala yordamchi feʼl ham unga ulanadi;
  * qisqarish qoidasi — て→ちゃ/と, で→じゃ/ど (jaranglilik);
  * PJ-60 da YOʻNALISH — あげる mendan chiqadi, くれる menga keladi,
    もらう men olaman. Har bir kalit `verify_pj_58_60_forms.py` da
    yoʻnalish jadvalidan qayta hisoblanadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_58_60.py --master=prime \\
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


# ── feʼllar: lugʻat · て-shakli ───────────────────────────────────────
TABERU,  TABETE   = r("食","た")+"べる",   r("食","た")+"べて"
YOMU,    YONDE    = r("読","よ")+"む",     r("読","よ")+"んで"
KAU,     KATTE    = r("買","か")+"う",     r("買","か")+"って"
WASURERU, WASURETE = r("忘","わす")+"れる", r("忘","わす")+"れて"
NOMU,    NONDE    = r("飲","の")+"む",     r("飲","の")+"んで"
KIRU,    KITE     = r("着","き")+"る",     r("着","き")+"て"
KESU,    KESHITE  = r("消","け")+"す",     r("消","け")+"して"
KOWARERU, KOWARETE = r("壊","こわ")+"れる", r("壊","こわ")+"れて"
OKURERU, OKURETE  = r("遅","おく")+"れる", r("遅","おく")+"れて"
AKERU,   AKETE    = r("開","あ")+"ける",   r("開","あ")+"けて"
OKU                = r("置","お")+"く"
JUNBI_SURU         = r("準備","じゅんび")+"する"
JUNBI_SHITE        = r("準備","じゅんび")+"して"
GANBARU            = r("頑張","がんば")+"る"
NAKUSU, NAKUSHITE  = "なくす", "なくして"

# ── yasалган shakllar ────────────────────────────────────────────────
YONDESHIMAIMASHITA = r("読","よ")+"んでしまいました"
WASURETESHIMAIMASHITA = r("忘","わす")+"れてしまいました"
KATTEOKIMASU       = r("買","か")+"っておきます"
TABETEMIMASU       = r("食","た")+"べてみます"
KITEMITEMO         = r("着","き")+"てみても"

# ── berish-olish ─────────────────────────────────────────────────────
AGERU,  AGEMASHITA  = "あげる", "あげました"
KURERU, KUREMASHITA = "くれる", "くれました"
MORAU,  MORAIMASHITA = "もらう", "もらいました"
ITADAKU             = "いただく"
KUDASARU            = "くださる"
SASHIAGERU          = "さしあげる"

# ── otlar ────────────────────────────────────────────────────────────
WATASHI   = r("私","わたし")
HON       = r("本","ほん")
SAIFU     = r("財布","さいふ")
SHUKUDAI  = r("宿題","しゅくだい")
ZENBU     = r("全部","ぜんぶ")
DENSHA    = r("電車","でんしゃ")
SENSEI    = r("先生","せんせい")
OTOUTO    = r("弟","おとうと")
FUKU      = r("服","ふく")
RYOURI    = r("料理","りょうり")
MADO      = r("窓","まど")
ASHITA    = r("明日","あした")
KAIGI     = r("会議","かいぎ")
SHIRYOU   = r("資料","しりょう")
PUREZENTO = "プレゼント"
UCHI      = r("内","うち")
ICHINICHI = r("一日","いちにち")
NEBOU     = r("寝坊","ねぼう")


# ══════════════════════════════════════════════════════════════════════
# PJ-58 — 〜てしまいます
# ══════════════════════════════════════════════════════════════════════
Q_PJ58 = [
    # 1–5 tanish
    q(f"<p>〜てしまう qaysi shaklga qoʻshiladi?</p>",
      ["て-shakliga", "Lugʻat shakliga", "た-shakliga", "ない-shakliga"],
      "て-shakliga",
      f"<p>Yana oʻsha て-shakli. PJ-55 da unga も qoʻshgan edingiz, "
      f"bu safar butun bir feʼl — <strong>しまう</strong> — "
      f"qoʻshiladi.</p>"),

    q(f"<p>{YOMU} ning てしまう shakli qaysi?</p>",
      [f"{YONDE}しまう", f"{YOMU}しまう", f"{r('読','よ')}みてしまう",
       f"{r('読','よ')}んだしまう"],
      f"{YONDE}しまう",
      f"<p>て-shakli <strong>{YONDE}</strong> (I guruh, む → んで), "
      f"ustiga しまう.</p>"),

    q(f"<p>〜てしまう ning ikki maʼnosi qaysilar?</p>",
      ["Butunlay tugatish va afsus", "Xohish va qaror",
       "Shart va sabab", "Buyruq va taqiq"],
      "Butunlay tugatish va afsus",
      f"<p>Oʻzbekcha «-ib boʻlmoq» va «-ib qoʻymoq» — bir xil "
      f"juftlik.</p>"),

    q(f"<p>{TABETE}しまう ning ogʻzaki qisqargan shakli qaysi?</p>",
      [f"{r('食','た')}べちゃう", f"{r('食','た')}べじゃう",
       f"{r('食','た')}べとく", f"{r('食','た')}べどく"],
      f"{r('食','た')}べちゃう",
      f"<p>て jarangsiz, demak <strong>ちゃ</strong>う.</p>"),

    q(f"<p>{YONDE}しまう ning ogʻzaki qisqargan shakli qaysi?</p>",
      [f"{r('読','よ')}んじゃう", f"{r('読','よ')}んちゃう",
       f"{r('読','よ')}んどく", f"{r('読','よ')}んとく"],
      f"{r('読','よ')}んじゃう",
      f"<p>で jarangli, demak <strong>じゃ</strong>う. Bu PJ-6 dagi "
      f"dakuten qoidasining oʻzi: ち ustiga ikki nuqta → じ.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{SAIFU}を{NAKUSHITE}しまいました» — qaysi maʼno?</p>",
      ["Afsus", "Butunlay tugatish", "Buyruq", "Shart"],
      "Afsus",
      f"<p>«Yoʻqotmoq» feʼlining yaxshi tomoni yoʻq — demak "
      f"afsus. Oʻzbekcha «yoʻqotib <strong>qoʻydim</strong>».</p>"),

    q(f"<p>«{SHUKUDAI}を{ZENBU}してしまいました» — qaysi maʼno?</p>",
      ["Butunlay tugatish", "Afsus", "Ruxsat", "Taxmin"],
      "Butunlay tugatish",
      f"<p><strong>{ZENBU}</strong> soʻzi maʼnoni aniqlab turibdi: "
      f"«hammasini qilib boʻldim». Uy vazifasi — vazifa, afsus "
      f"emas.</p>"),

    q(f"<p>«Telefonim sinib qoldi» ni yozing.</p>",
      [f"でんわが{KOWARETE}しまいました", f"でんわを{KOWARETE}しまいました",
       f"でんわが{r('壊','こわ')}すてしまいました", f"でんわが{KOWARERU}しまいました"],
      f"でんわが{KOWARETE}しまいました",
      f"<p>{KOWARERU} — «oʻzi sinmoq» (なる tomoni), shuning uchun "
      f"<strong>が</strong>. {r('壊','こわ')}す esa «men sindirmoq» "
      f"(する tomoni).</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NEBOU}して、"
      f"{DENSHA}に{OKURETE}___。</strong></p>",
      ["しまいました", "おきました", "みました", "いました"],
      "しまいました",
      f"<p>Kechikish — xohlanmagan natija, demak "
      f"<strong>しまいました</strong>. «Kechikib qoldim.»</p>"),

    q(f"<p>{WASURERU} ning てしまいました shakli qaysi?</p>",
      [WASURETESHIMAIMASHITA, f"{r('忘','わす')}れるしまいました",
       f"{r('忘','わす')}れしまいました", f"{r('忘','わす')}れたしまいました"],
      WASURETESHIMAIMASHITA,
      f"<p>II guruh, て-shakli <strong>{WASURETE}</strong>.</p>"),

    q(f"<p>Nega bu qolip koʻpincha oʻtgan zamonda chiqadi?</p>",
      ["Chunki tugagan ish ham, afsus ham allaqachon boʻlgan narsa",
       "Chunki しまう faqat oʻtgan zamonda ishlatiladi",
       "Chunki て-shakli oʻtgan zamon",
       "Chunki bu faqat ogʻzaki nutqda uchraydi"],
      "Chunki tugagan ish ham, afsus ham allaqachon boʻlgan narsa",
      f"<p>Shuning uchun matnlarda eng koʻp "
      f"<strong>〜てしまいました</strong> va oddiy shaklda "
      f"<strong>〜てしまった</strong> koʻrinadi.</p>"),

    q(f"<p>{r('壊','こわ')}す va {KOWARERU} — farqi nima?</p>",
      [f"{r('壊','こわ')}す — men sindirdim; {KOWARERU} — oʻzi sindi",
       f"{r('壊','こわ')}す — oʻtgan zamon; {KOWARERU} — hozirgi",
       f"{r('壊','こわ')}す — rasmiy; {KOWARERU} — oddiy",
       "Farqi yoʻq"],
      f"{r('壊','こわ')}す — men sindirdim; {KOWARERU} — oʻzi sindi",
      f"<p>Bu PJ-57 dagi する / なる chizigʻining oʻzi — "
      f"{r('決','き')}める / {r('決','き')}まる kabi.</p>"),

    # 13–16 farqlash
    q(f"<p>Qaysi feʼl bilan kelganda maʼno deyarli doim "
      f"<strong>afsus</strong> boʻladi?</p>",
      [NAKUSU, f"{r('宿題','しゅくだい')}をする", YOMU, f"{r('書','か')}く"],
      NAKUSU,
      f"<p>«Yoʻqotmoq», «unutmoq», «sinmoq», «kechikmoq» — "
      f"bularning yaxshi tomoni yoʻq. Qolganlari vazifa, demak "
      f"tugatish.</p>"),

    q(f"<p>ちゃう va じゃう orasidagi tanlov nimaga qarab "
      f"qilinadi?</p>",
      ["て yoki で ga — jaranglilikka",
       "Feʼlning guruhiga", "Gapning zamoniga", "Muloyimlik darajasiga"],
      "て yoki で ga — jaranglilikka",
      f"<p>て → <strong>ちゃ</strong>, で → <strong>じゃ</strong>. "
      f"Feʼl guruhi bu yerda bevosita ishtirok etmaydi.</p>"),

    q(f"<p>Inshoda qaysi shaklni yozasiz?</p>",
      [f"{WASURETE}しまいました", f"{r('忘','わす')}れちゃいました",
       f"{r('忘','わす')}れちゃった", f"{r('忘','わす')}れちゃう"],
      f"{WASURETE}しまいました",
      f"<p>ちゃう faqat ogʻzaki nutqniki. Yozma ishda va ustoz "
      f"bilan doim toʻliq shakl.</p>"),

    q(f"<p>«{HON}を{ICHINICHI}で{YONDESHIMAIMASHITA}» — qaysi "
      f"maʼno?</p>",
      ["Butunlay tugatish", "Afsus", "Ikkalasi ham boʻlishi mumkin",
       "Hech qaysi"],
      "Butunlay tugatish",
      f"<p>«{ICHINICHI}で» — bir kunda. Bu gapda tezlik va "
      f"tugallanganlik bor, afsus emas.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{YOMU}しまいました", f"{YONDE}しまいました",
       f"{TABETE}しまいました", f"{KESHITE}しまいました"],
      f"{YOMU}しまいました",
      f"<p>しまう <strong>て-shakliga</strong> qoʻshiladi: "
      f"{YONDE}しまいました.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{YONDE}しまう → {r('読','よ')}んでちゃう",
       f"{TABETE}しまう → {r('食','た')}べちゃう",
       f"{NONDE}しまう → {r('飲','の')}んじゃう",
       f"{KESHITE}しまう → {r('消','け')}しちゃう"],
      f"{YONDE}しまう → {r('読','よ')}んでちゃう",
      f"<p>Toʻgʻrisi — <strong>{r('読','よ')}んじゃう</strong>. で dan "
      f"keyin doim じゃ.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>しまいました · {SAIFU}を · {NAKUSHITE}</strong></p>",
      [f"{SAIFU}を{NAKUSHITE}しまいました",
       f"{NAKUSHITE}しまいました{SAIFU}を",
       f"しまいました{SAIFU}を{NAKUSHITE}",
       f"{SAIFU}をしまいました{NAKUSHITE}"],
      f"{SAIFU}を{NAKUSHITE}しまいました",
      f"<p>Toʻldiruvchi, keyin asosiy feʼlning て-shakli, oxirida "
      f"yordamchi feʼl. Yapon gapi doim feʼl bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> {SHUKUDAI}はどうですか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"もう{ZENBU}してしまいました。", f"もう{ZENBU}しましたしまいました。",
       f"もう{ZENBU}するしまいました。", f"もう{ZENBU}してちゃいました。"],
      f"もう{ZENBU}してしまいました。",
      f"<p>«Allaqachon hammasini qilib boʻldim» — bu "
      f"<strong>tugatish</strong> maʼnosi, va shakl て + "
      f"しまいました.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-59 — 〜ておきます va 〜てみます
# ══════════════════════════════════════════════════════════════════════
Q_PJ59 = [
    # 1–5 tanish
    q(f"<p>〜ておく nimani bildiradi?</p>",
      ["Oldindan qilib qoʻymoq", "Qilib koʻrmoq",
       "Qilib boʻlmoq", "Qilishga harakat qilmoq"],
      "Oldindan qilib qoʻymoq",
      f"<p>Ish hozir qilinadi, foydasi keyin koʻrinadi. "
      f"Oʻzbekcha «olib <strong>qoʻyaman</strong>».</p>"),

    q(f"<p>〜てみる nimani bildiradi?</p>",
      ["Qilib koʻrmoq", "Oldindan qilib qoʻymoq",
       "Qattiq harakat qilmoq", "Qilishni xohlamoq"],
      "Qilib koʻrmoq",
      f"<p>みる — «koʻrmoq». Ikkala tilda ham yordamchi feʼl "
      f"aynan «koʻrmoq»: yaponcha {r('見','み')}る, oʻzbekcha "
      f"«koʻrmoq».</p>"),

    q(f"<p>{KAU} ning ておく shakli qaysi?</p>",
      [KATTEOKIMASU, f"{KAU}ておきます", f"{r('買','か')}いておきます",
       f"{KATTE}おくます"],
      KATTEOKIMASU,
      f"<p>て-shakli <strong>{KATTE}</strong> (I guruh, う → って), "
      f"ustiga おきます.</p>"),

    q(f"<p>{TABERU} ning てみる shakli qaysi?</p>",
      [TABETEMIMASU, f"{TABETE}{r('見','み')}ます",
       f"{TABERU}てみます", f"{r('食','た')}べみます"],
      TABETEMIMASU,
      f"<p>Yordamchi feʼl <strong>kana bilan</strong> yoziladi: "
      f"みます. {r('見','み')}る kanjisi faqat asl «koʻrmoq» "
      f"maʼnosida.</p>"),

    q(f"<p>{KATTE}おく ning ogʻzaki qisqargan shakli qaysi?</p>",
      [f"{r('買','か')}っとく", f"{r('買','か')}っどく",
       f"{r('買','か')}っちゃう", f"{r('買','か')}っじゃう"],
      f"{r('買','か')}っとく",
      f"<p>ておく → <strong>とく</strong>. で bilan tugasa — "
      f"どく.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ASHITA}のチケットを"
      f"{KATTE}___。</strong></p>",
      ["おきます", "みます", "しまいます", "います"],
      "おきます",
      f"<p>Bilet <em>kelajak uchun</em> olinadi — bu "
      f"<strong>ておく</strong> ning oʻz ishi.</p>"),

    q(f"<p>«Bu kiyimni kiyib koʻrsam boʻladimi?» qaysi?</p>",
      [f"この{FUKU}を{KITEMITEMO}いいですか",
       f"この{FUKU}を{KITE}おいてもいいですか",
       f"この{FUKU}を{KIRU}てみてもいいですか",
       f"この{FUKU}を{KITE}しまってもいいですか"],
      f"この{FUKU}を{KITEMITEMO}いいですか",
      f"<p>てみる + てもいいですか (PJ-55) — doʻkonda eng koʻp "
      f"ishlatiladigan gap.</p>"),

    q(f"<p>«{MADO}を{AKETE}おいてください» ni tarjima qiling.</p>",
      ["Derazani ochiq qoldiring", "Derazani ochib koʻring",
       "Derazani yopib qoʻying", "Derazani ochib boʻling"],
      "Derazani ochiq qoldiring",
      f"<p>ておく ning ikkinchi maʼnosi: <strong>shundayligicha "
      f"qoldirmoq</strong>. Mantiq bir xil — ish keyingi paytga "
      f"qaratilgan.</p>"),

    q(f"<p>{r('食','た')}べたい va {TABETE}みる — farqi nima?</p>",
      ["Birinchisi xohish, ikkinchisi qaror",
       "Birinchisi qaror, ikkinchisi xohish",
       "Ikkalasi ham xohish", "Farqi yoʻq"],
      "Birinchisi xohish, ikkinchisi qaror",
      f"<p>«Yegim kelyapti» va «yeb koʻraman». Ikkalasini birga "
      f"ham ishlatsa boʻladi: {TABETE}みたいです.</p>"),

    q(f"<p>«{KAIGI}の{r('前','まえ')}に{SHIRYOU}を{YONDE}おいて"
      f"ください» ni tarjima qiling.</p>",
      ["Yigʻilishdan oldin hujjatlarni oʻqib qoʻying",
       "Yigʻilishdan oldin hujjatlarni oʻqib koʻring",
       "Yigʻilishda hujjatlarni oʻqing",
       "Yigʻilishdan keyin hujjatlarni oʻqing"],
      "Yigʻilishdan oldin hujjatlarni oʻqib qoʻying",
      f"<p>ておく — tayyorgarlik. «Oʻqib koʻring» boʻlsa "
      f"{YONDE}みてください boʻlardi.</p>"),

    q(f"<p>Nega yordamchi feʼl kana bilan yoziladi?</p>",
      ["Chunki yordamchi boʻlib qolgan feʼl kanjisini yoʻqotadi",
       "Chunki kanji juda qiyin",
       "Chunki bu faqat ogʻzaki nutqda uchraydi",
       "Chunki みる II guruh feʼli"],
      "Chunki yordamchi boʻlib qolgan feʼl kanjisini yoʻqotadi",
      f"<p>Bu yapon tilining umumiy odati: {TABETE}みます ✓, "
      f"{KATTE}おきます ✓ — {r('見','み')}ます va "
      f"{r('置','お')}きます emas.</p>"),

    q(f"<p>てみる «harakat qilmoq» degani emas. Unda «harakat "
      f"qilmoq» qaysi soʻz?</p>",
      [GANBARU, f"{r('見','み')}る", OKU, f"{r('準備','じゅんび')}する"],
      GANBARU,
      f"<p>てみる — «bir marta qilib, nima boʻlishini koʻrmoq». "
      f"Qattiq harakat uchun <strong>{GANBARU}</strong> yoki "
      f"PJ-55 dagi いくら〜ても.</p>"),

    # 13–16 farqlash
    q(f"<p>Uchta yordamchi feʼldan qaysi biri ishni "
      f"<strong>kelajakka</strong> qaratadi?</p>",
      ["〜ておく", "〜てしまう", "〜てみる", "Uchalasi ham"],
      "〜ておく",
      f"<p>〜てしまう — oʻtmishga (ish tugagan); 〜てみる — "
      f"hozirga (natijani bilmayman); <strong>〜ておく</strong> — "
      f"kelajakka (foydasi keyin).</p>"),

    q(f"<p>«{RYOURI}を{TABETE}おきます» va «{RYOURI}を{TABETE}みます» "
      f"— farqi nima?</p>",
      ["Birinchisi «oldindan yeb qoʻyaman», ikkinchisi «yeb koʻraman»",
       "Birinchisi «yeb koʻraman», ikkinchisi «yeb boʻlaman»",
       "Ikkalasi bir xil",
       "Birinchisi rasmiy, ikkinchisi oddiy"],
      "Birinchisi «oldindan yeb qoʻyaman», ikkinchisi «yeb koʻraman»",
      f"<p>おく — tayyorgarlik (keyin och qolmaslik uchun); "
      f"みる — sinash (mazasini bilish uchun).</p>"),

    q(f"<p>{YONDE}おく ning qisqargan shakli qaysi?</p>",
      [f"{r('読','よ')}んどく", f"{r('読','よ')}んとく",
       f"{r('読','よ')}んじゃう", f"{r('読','よ')}んちゃう"],
      f"{r('読','よ')}んどく",
      f"<p>で dan keyin <strong>ど</strong>く — xuddi じゃう "
      f"kabi jaranglilik qoidasi.</p>"),

    q(f"<p>«{TABETE}みたいです» ni tarjima qiling.</p>",
      ["Yeb koʻrgim kelyapti", "Yeb koʻraman",
       "Yeb boʻldim", "Yeb qoʻyaman"],
      "Yeb koʻrgim kelyapti",
      f"<p>てみる + たい — ikkalasi birga. Oʻzbekchada ham "
      f"xuddi shunday tuziladi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{KAU}ておきます", KATTEOKIMASU, TABETEMIMASU,
       f"{JUNBI_SHITE}おきます"],
      f"{KAU}ておきます",
      f"<p>おく <strong>て-shakliga</strong> qoʻshiladi: "
      f"{KATTEOKIMASU}.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [TABETEMIMASU, f"{TABETE}{r('見','み')}ます",
       f"{TABERU}みます", f"{r('食','た')}べてみるます"],
      TABETEMIMASU,
      f"<p>Yordamchi feʼl kana bilan, va て-shakliga "
      f"qoʻshiladi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>おきます · {ASHITA}のチケットを · {KATTE}</strong></p>",
      [f"{ASHITA}のチケットを{KATTE}おきます",
       f"{KATTE}おきます{ASHITA}のチケットを",
       f"おきます{ASHITA}のチケットを{KATTE}",
       f"{ASHITA}のチケットをおきます{KATTE}"],
      f"{ASHITA}のチケットを{KATTE}おきます",
      f"<p>Toʻldiruvchi, asosiy feʼlning て-shakli, keyin "
      f"yordamchi feʼl.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>てんいん:</strong> この{FUKU}はいかがですか。</p>"
      f"<p><strong>ラノ:</strong> ___</p>",
      [f"{KITEMITEMO}いいですか。", f"{KITE}おいてもいいですか。",
       f"{KITE}しまってもいいですか。", f"{KIRU}てみてもいいですか。"],
      f"{KITEMITEMO}いいですか。",
      f"<p>Doʻkonda kiyimni sinab koʻrish — "
      f"<strong>てみる</strong>, va ruxsat soʻrash — "
      f"てもいいですか.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-60 — あげる, くれる, もらう
# ══════════════════════════════════════════════════════════════════════
Q_PJ60 = [
    # 1–5 tanish
    q(f"<p>Sovgʻa MENDAN chiqsa, qaysi feʼl?</p>",
      [AGERU, KURERU, MORAU, ITADAKU],
      AGERU,
      f"<p><strong>あげる</strong> — mendan tashqariga. Yoʻnalish "
      f"yaponchada feʼlning ichida turadi.</p>"),

    q(f"<p>Sovgʻa MENGA kelsa, qaysi feʼl?</p>",
      [KURERU, AGERU, MORAU, SASHIAGERU],
      KURERU,
      f"<p><strong>くれる</strong> — tashqaridan menga. "
      f"«{WATASHI}にあげました» notoʻgʻri boʻlardi.</p>"),

    q(f"<p>MEN olsam, qaysi feʼl?</p>",
      [MORAU, AGERU, KURERU, KUDASARU],
      MORAU,
      f"<p><strong>もらう</strong> — men olaman. くれる bilan bir "
      f"voqeani ikki tomondan aytadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WATASHI}はパリさん"
      f"___{HON}をあげました。</strong></p>",
      ["に", "が", "を", "で"],
      "に",
      f"<p>あげる bilan <strong>に</strong> — «kimga».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{WATASHI}はパリさん"
      f"___{HON}をもらいました。</strong></p>",
      ["に", "を", "が", "へ"],
      "に",
      f"<p>もらう bilan <strong>に</strong> — bu safar «kimdan». "
      f"Chalkash boʻlsa <strong>から</strong> ham toʻgʻri: "
      f"パリさんからもらいました.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"パリさんは{WATASHI}に{HON}を{KUREMASHITA}",
       f"パリさんは{WATASHI}に{HON}を{AGEMASHITA}",
       f"パリさんは{WATASHI}に{HON}を{MORAIMASHITA}",
       f"パリさんが{WATASHI}を{HON}に{KUREMASHITA}"],
      f"パリさんは{WATASHI}に{HON}を{KUREMASHITA}",
      f"<p>Menga kelayotgan sovgʻa doim <strong>くれる</strong>. "
      f"Bu darsdagi eng koʻp qilinadigan xato.</p>"),

    q(f"<p>«ムニラさんが{WATASHI}に{PUREZENTO}を{KUREMASHITA}» ni "
      f"«{WATASHI}» ni ega qilib qayta yozing.</p>",
      [f"{WATASHI}はムニラさんに{PUREZENTO}を{MORAIMASHITA}",
       f"{WATASHI}はムニラさんに{PUREZENTO}を{AGEMASHITA}",
       f"{WATASHI}はムニラさんに{PUREZENTO}を{KUREMASHITA}",
       f"{WATASHI}がムニラさんを{PUREZENTO}に{MORAIMASHITA}"],
      f"{WATASHI}はムニラさんに{PUREZENTO}を{MORAIMASHITA}",
      f"<p>Bir voqea, boshqa kamera. Ega Munira boʻlsa — "
      f"くれる; ega men boʻlsam — <strong>もらう</strong>.</p>"),

    q(f"<p>«{SENSEI}が{OTOUTO}に{HON}を___» — qaysi feʼl?</p>",
      [KUREMASHITA, AGEMASHITA, MORAIMASHITA, "いただきました"],
      KUREMASHITA,
      f"<p>Ukam ham <strong>«oʻz odamim»</strong> — sovgʻa "
      f"ichkariga kelyapti, demak くれる. Yapon tili sizni "
      f"yolgʻiz emas, bir guruh deb koʻradi.</p>"),

    q(f"<p>Yapon tilida «oʻz guruhim» qanday ataladi?</p>",
      [f"{UCHI}", f"{r('外','そと')}", f"{r('内','ない')}", f"{r('家','いえ')}"],
      f"{UCHI}",
      f"<p><strong>{UCHI}</strong> — «ichkari», qolganlari esa "
      f"{r('外','そと')} — «tashqari». PJ-72 butunlay shu "
      f"haqida.</p>"),

    q(f"<p>いただきます aslida nima degani?</p>",
      ["«Olaman» — いただく feʼlining muloyim shakli",
       "«Yoqimli ishtaha»", "«Rahmat»", "«Boshladik»"],
      "«Olaman» — いただく feʼlining muloyim shakli",
      f"<p>Siz taomni kimdandir — pishirgan odamdan, dehqondan, "
      f"tabiatdan — olayotganingizni tan olasiz. Shuning uchun "
      f"uni «yoqimli ishtaha» deb tarjima qilish notoʻgʻri.</p>"),

    q(f"<p>{MORAU} ning muloyim shakli qaysi?</p>",
      [ITADAKU, KUDASARU, SASHIAGERU, AGERU],
      ITADAKU,
      f"<p>あげる → {SASHIAGERU} · くれる → {KUDASARU} · "
      f"もらう → <strong>{ITADAKU}</strong>.</p>"),

    q(f"<p>«{WATASHI}はムニラさんに{PUREZENTO}を{AGEMASHITA}» ni "
      f"tarjima qiling.</p>",
      ["Men Muniraga sovgʻa berdim", "Munira menga sovgʻa berdi",
       "Men Muniradan sovgʻa oldim", "Munira sovgʻa oldi"],
      "Men Muniraga sovgʻa berdim",
      f"<p>Ega — men, feʼl — あげる, demak sovgʻa mendan "
      f"chiqyapti.</p>"),

    # 13–16 farqlash
    q(f"<p>くれる va もらう orasidagi farq nima?</p>",
      ["Bir voqeani ikki tomondan aytadi — ega boshqa",
       "くれる kelasi zamon, もらう oʻtgan",
       "くれる rasmiy, もらう oddiy",
       "くれる narsa uchun, もらう odam uchun"],
      "Bir voqeani ikki tomondan aytadi — ega boshqa",
      f"<p>Tanaka menga kitob berdi: ega Tanaka boʻlsa "
      f"<strong>くれました</strong>, ega men boʻlsam "
      f"<strong>もらいました</strong>.</p>"),

    q(f"<p>Nega «パリさんは{WATASHI}に{AGEMASHITA}» notoʻgʻri?</p>",
      ["Chunki あげる menga qarab yoʻnala olmaydi",
       f"Chunki {WATASHI} は olishi kerak",
       "Chunki あげる faqat narsalar uchun",
       "Chunki gap oʻtgan zamonda"],
      "Chunki あげる menga qarab yoʻnala olmaydi",
      f"<p>Yoʻnalish feʼlning ichida. «{WATASHI}に» soʻzi "
      f"oʻrnida tursa ham, feʼl notoʻgʻri boʻlsa gap "
      f"buziladi.</p>"),

    q(f"<p>Oʻzbekcha va yaponcha yoʻnalishni qayerda "
      f"koʻrsatadi?</p>",
      ["Oʻzbekcha qoʻshimchada, yaponcha feʼlda",
       "Ikkalasi ham feʼlda", "Ikkalasi ham qoʻshimchada",
       "Oʻzbekcha feʼlda, yaponcha qoʻshimchada"],
      "Oʻzbekcha qoʻshimchada, yaponcha feʼlda",
      f"<p>«U <em>menga</em> berdi» va «men <em>unga</em> berdim» "
      f"— oʻzbekchada feʼl bitta. Yaponchada esa feʼl "
      f"oʻzgaradi.</p>"),

    q(f"<p>もらう da に nimani bildiradi?</p>",
      ["Kimdan", "Kimga", "Qayerda", "Nima bilan"],
      "Kimdan",
      f"<p>Bu chalkash joy: あげる va くれる bilan に — «kimga», "
      f"もらう bilan esa «kimdan». Shubha boʻlsa "
      f"<strong>から</strong> ishlating.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{WATASHI}はパリさんに{HON}を{KUREMASHITA}",
       f"{WATASHI}はパリさんに{HON}を{AGEMASHITA}",
       f"パリさんは{WATASHI}に{HON}を{KUREMASHITA}",
       f"{WATASHI}はパリさんに{HON}を{MORAIMASHITA}"],
      f"{WATASHI}はパリさんに{HON}を{KUREMASHITA}",
      f"<p>Mendan chiqayotgan sovgʻa <strong>あげる</strong> "
      f"oladi. くれる faqat menga kelganda.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"パリさんから{HON}を{MORAIMASHITA}",
       f"パリさんを{HON}を{MORAIMASHITA}",
       f"パリさんが{HON}を{MORAIMASHITA}",
       f"パリさんへ{HON}を{MORAIMASHITA}"],
      f"パリさんから{HON}を{MORAIMASHITA}",
      f"<p>«Kimdan» — <strong>に</strong> yoki "
      f"<strong>から</strong>. を va が bu yerda "
      f"ishlatilmaydi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{KUREMASHITA} · {HON}を · {WATASHI}に · "
      f"パリさんは</strong></p>",
      [f"パリさんは{WATASHI}に{HON}を{KUREMASHITA}",
       f"{WATASHI}にパリさんは{HON}を{KUREMASHITA}",
       f"{HON}をパリさんは{WATASHI}に{KUREMASHITA}",
       f"パリさんは{HON}を{WATASHI}に{AGEMASHITA}"],
      f"パリさんは{WATASHI}に{HON}を{KUREMASHITA}",
      f"<p>Ega — kimga — nima — feʼl. Va feʼl "
      f"<strong>くれました</strong>, chunki sovgʻa menga "
      f"kelyapti.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> その{HON}はどこで{r('買','か')}いましたか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{r('買','か')}いませんでした。{SENSEI}が{KUREMASHITA}。",
       f"{r('買','か')}いませんでした。{SENSEI}が{AGEMASHITA}。",
       f"{r('買','か')}いませんでした。{SENSEI}が{MORAIMASHITA}。",
       f"{r('買','か')}いませんでした。{SENSEI}に{AGEMASHITA}。"],
      f"{r('買','か')}いませんでした。{SENSEI}が{KUREMASHITA}。",
      f"<p>Oʻqituvchi Inomga bergan — sovgʻa gapiruvchiga "
      f"kelyapti, demak <strong>くれました</strong>.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-58 Mashq: 〜てしまいます",
        "tutorial":    "PJ-58:",
        "description": "Bitta qolip, ikki maʼno: «-ib boʻldim» va "
                       "«-ib qoʻydim». Va qisqarish: て→ちゃ, で→じゃ.",
        "questions":   Q_PJ58,
        **DEFAULTS,
    },
    {
        "title":       "PJ-59 Mashq: 〜ておきます va 〜てみます",
        "tutorial":    "PJ-59:",
        "description": "Oldindan qilib qoʻymoq va qilib koʻrmoq. "
                       "Yordamchi feʼl doim kana bilan yoziladi.",
        "questions":   Q_PJ59,
        **DEFAULTS,
    },
    {
        "title":       "PJ-60 Mashq: あげる, くれる, もらう",
        "tutorial":    "PJ-60:",
        "description": "Yoʻnalish feʼlning ichida: mendan chiqsa あげる, "
                       "menga kelsa くれる, men olsam もらう.",
        "questions":   Q_PJ60,
        **DEFAULTS,
    },
]
