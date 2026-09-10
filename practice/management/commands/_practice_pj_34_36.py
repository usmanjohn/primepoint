# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-34 … PJ-36.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

⚠️ Feʼl shakllari toʻliq konstanta sifatida yoziladi. て / ない / た oʻzaklariga
qoʻshimcha ulash xavfsiz — bu haqiqiy morfema chegarasi; oʻzak + qoʻshimcha
birikmasi esa PJ-25…27 da xato kalitlar bergan edi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_34_36.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "日本語",
    "description": "Yapon tili — grammatika va yozuv mashqlari",
    "icon":        "bi-brilliance",
    "color":       "#be123c",
}

DEFAULTS = {
    "level":                "easy",
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

# ── lugʻat · て · ない · た ───────────────────────────────────────────
YOMU,  YONDE,  YOMANAI,  YONDA  = r("読","よ")+"む", r("読","よ")+"んで", r("読","よ")+"まない", r("読","よ")+"んだ"
KAKU,  KAITE,  KAKANAI,  KAITA  = r("書","か")+"く", r("書","か")+"いて", r("書","か")+"かない", r("書","か")+"いた"
HANASU,HANASHITE,HANASANAI,HANASHITA = r("話","はな")+"す", r("話","はな")+"して", r("話","はな")+"さない", r("話","はな")+"した"
MATSU, MATTE,  MATANAI,  MATTA  = r("待","ま")+"つ", r("待","ま")+"って", r("待","ま")+"たない", r("待","ま")+"った"
KAU,   KATTE,  KAWANAI,  KATTA  = r("買","か")+"う", r("買","か")+"って", r("買","か")+"わない", r("買","か")+"った"
OYOGU, OYOIDE, OYOGANAI, OYOIDA = r("泳","およ")+"ぐ", r("泳","およ")+"いで", r("泳","およ")+"がない", r("泳","およ")+"いだ"
IKU,   ITTE,   IKANAI,   ITTA   = r("行","い")+"く", r("行","い")+"って", r("行","い")+"かない", r("行","い")+"った"
HAIRU, HAITTE, HAIRANAI, HAITTA = r("入","はい")+"る", r("入","はい")+"って", r("入","はい")+"らない", r("入","はい")+"った"
HASHIRU,HASHITTE,HASHIRANAI,HASHITTA = r("走","はし")+"る", r("走","はし")+"って", r("走","はし")+"らない", r("走","はし")+"った"
TORU,  TOTTE,  TORANAI,  TOTTA  = r("撮","と")+"る", r("撮","と")+"って", r("撮","と")+"らない", r("撮","と")+"った"
NOBORU,NOBOTTE,NOBORANAI,NOBOTTA = r("登","のぼ")+"る", r("登","のぼ")+"って", r("登","のぼ")+"らない", r("登","のぼ")+"った"
AU,    ATTE,   AWANAI,   ATTA   = r("会","あ")+"う", r("会","あ")+"って", r("会","あ")+"わない", r("会","あ")+"った"
YASUMU,YASUNDE,YASUMANAI,YASUNDA = r("休","やす")+"む", r("休","やす")+"んで", r("休","やす")+"まない", r("休","やす")+"んだ"
KIKU,  KIITE,  KIKANAI,  KIITA  = r("聞","き")+"く", r("聞","き")+"いて", r("聞","き")+"かない", r("聞","き")+"いた"
TABERU,TABETE, TABENAI,  TABETA = r("食","た")+"べる", r("食","た")+"べて", r("食","た")+"べない", r("食","た")+"べた"
MIRU,  MITE,   MINAI,    MITA   = r("見","み")+"る", r("見","み")+"て", r("見","み")+"ない", r("見","み")+"た"
WASURERU,WASURETE,WASURENAI,WASURETA = r("忘","わす")+"れる", r("忘","わす")+"れて", r("忘","わす")+"れない", r("忘","わす")+"れた"
KURU,  KITE,   KONAI,    KITA   = r("来","く")+"る", r("来","き")+"て", r("来","こ")+"ない", r("来","き")+"た"
SURU,  SHITE,  SHINAI,   SHITA  = "する", "して", "しない", "した"

def naide(nai):    return nai + "で"
def naidekuda(nai): return nai + "でください"
def tari(ta):      return ta + "り"
def kotoga(ta):    return ta + "ことがあります"
def kotonai(ta):   return ta + "ことがありません"

BENKYOU, SOUJI = r("勉強","べんきょう"), r("掃除","そうじ")
HON, GK, KY, SE = r("本","ほん"), r("学校","がっこう"), r("教室","きょうしつ"), r("先生","せんせい")
NG, WA, TSK = r("日本語","にほんご"), r("私","わたし"), r("図書館","としょかん")
NIHON, FUJI, ONGAKU = r("日本","にほん"), r("富士山","ふじさん"), r("音楽","おんがく")
SHASHIN, NICHI, JIKAN = r("写真","しゃしん"), r("日曜日","にちようび"), r("時間","じかん")


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-34 — ない-shakli
# ══════════════════════════════════════════════════════════════════════
Q_PJ34 = [
    q("<p>I guruh feʼlining ない-shaklida oxirgi tovush qaysi qatorga tushadi?</p>",
      ["あ qatori", "い qatori", "う qatori", "え qatori"], "あ qatori",
      f"<p><strong>あ qatori</strong>: {YOMU} → {YOMANAI}. Bu ます shaklidagi "
      f"harakatning teskarisi — u yerda い qatoriga tushgan edi.</p>"),

    q(f"<p>{KAKU} ning ない-shaklini tanlang.</p>",
      [KAKANAI, r("書","か")+"きない", r("書","か")+"くない", r("書","か")+"いない"],
      KAKANAI,
      f"<p><strong>{KAKANAI}</strong> — く あ qatoriga tushadi: か. "
      f"«{r('書','か')}きない» — bu ます oʻzagi, ない bilan aralashtirmang.</p>"),

    q(f"<p>{TABERU} ning ない-shaklini tanlang.</p>",
      [TABENAI, r("食","た")+"べらない", r("食","た")+"べるない", r("食","た")+"べあない"],
      TABENAI,
      f"<p><strong>{TABENAI}</strong> — II guruh: る tushadi, ない qoʻshiladi. "
      f"て-shakli bilan bir xil mantiq.</p>"),

    q(f"<p>{KAU} ning ない-shaklini tanlang.</p>",
      [KAWANAI, r("買","か")+"あない", r("買","か")+"いない", r("買","か")+"らない"],
      KAWANAI,
      f"<p><strong>{KAWANAI}</strong> — う bilan tugagan feʼl あ emas, "
      f"<strong>わ</strong> oladi. Bu birinchi tuzoq.</p>"),

    q(f"<p>{KURU} ning ない-shakli — <strong>来ない</strong> — qanday oʻqiladi?</p>",
      ["こない", "くない", "きない", "けない"], "こない",
      f"<p><strong>こない</strong> — ikkinchi tuzoq: oʻqilishi oʻzgaradi. "
      f"Bu kanji toʻrt xil oʻqiladi: {KURU}, {r('来','き')}ます, {KITE}, {KONAI}.</p>"),

    q("<p>ある feʼlining ない-shakli qaysi?</p>",
      ["ない", "あらない", "ありない", "あるない"], "ない",
      f"<p><strong>ない</strong> — uchinchi va eng kutilmagan tuzoq: feʼlning "
      f"oʻzi butunlay yoʻqoladi. Uning muloyim shaklini siz PJ-16 dan beri "
      f"bilasiz: <strong>ありません</strong>.</p>"),

    q(f"<p>{HANASU} ning ない-shaklini tanlang.</p>",
      [HANASANAI, r("話","はな")+"しない", r("話","はな")+"すない", r("話","はな")+"さらない"],
      HANASANAI,
      f"<p><strong>{HANASANAI}</strong> — す あ qatoriga tushadi: さ. "
      f"«{r('話','はな')}しない» esa ます oʻzagi (し) bilan yasalgan — bu qoida yoʻq.</p>"),

    q("<p>〜ないでください nima maʼnoni beradi?</p>",
      ["Iltimos, qilmang", "Iltimos, qiling", "Qilish shart emas", "Qilmadim"],
      "Iltimos, qilmang",
      f"<p>ない-shakliga <strong>でください</strong> qoʻshiladi: "
      f"<strong>{naidekuda(HAIRANAI)}</strong> — «kirmang».</p>"),

    q(f"<p>«Bu yerda rasmga olmang» ni tanlang.</p>",
      [f"ここで{SHASHIN}を{naidekuda(TORANAI)}",
       f"ここで{SHASHIN}を{TORANAI}ください",
       f"ここで{SHASHIN}を{TOTTE}ください",
       f"ここで{SHASHIN}を{r('撮','と')}りないでください"],
      f"ここで{SHASHIN}を{naidekuda(TORANAI)}",
      f"<p>{TORU} → {TORANAI} → <strong>{naidekuda(TORANAI)}</strong>. "
      f"ない bilan ください orasida <strong>で</strong> turadi.</p>"),

    q(f"<p>{WASURERU} dan «unutmang» ni tanlang.</p>",
      [naidekuda(WASURENAI), f"{WASURENAI}ください",
       f"{WASURETE}ください", f"{r('忘','わす')}れりないでください"],
      naidekuda(WASURENAI),
      f"<p><strong>{naidekuda(WASURENAI)}</strong>. «{WASURETE}ください» esa "
      f"«unuting» — teskari maʼno.</p>"),

    q("<p>〜ないでください va 〜てはいけません farqi nima?</p>",
      ["Birinchisi shaxsiy iltimos, ikkinchisi qoida",
       "Birinchisi qoida, ikkinchisi shaxsiy iltimos",
       "Farqi yoʻq",
       "Birinchisi oʻtgan zamonda"],
      "Birinchisi shaxsiy iltimos, ikkinchisi qoida",
      f"<p>Grammatika emas, <strong>kimning gapi</strong> ekani hal qiladi. "
      f"«Iltimos, yopmang» va «Yopish mumkin emas» — oʻzbekchada ham shu "
      f"ikkilik bor.</p>"),

    q(f"<p>«{naide(TABENAI)}» nima maʼnoni beradi?</p>",
      ["yemasdan", "yemang", "yemadim", "yeyish shart emas"], "yemasdan",
      f"<p>ないで oʻzi ham ishlaydi — ください siz. «{r('朝','あさ')}ごはんを"
      f"{naide(TABENAI)}、{GK}へ{r('行','い')}きました» — «nonushta qilmasdan, "
      f"maktabga bordim».</p>"),

    q(f"<p>て va ないで juftligi oʻzbekchada nimaga toʻgʻri keladi?</p>",
      ["-ib va -masdan", "-gan va -magan", "-moq va -mamoq", "-di va -madi"],
      "-ib va -masdan",
      f"<p>«Yeb, bordim» — {TABETE}; «ye<strong>masdan</strong>, bordim» — "
      f"{naide(TABENAI)}. Kursdagi eng toza mosliklardan biri.</p>"),

    q("<p>ない oʻzagidan nechta qolip yasaladi?</p>",
      ["Toʻrtta", "Bitta", "Ikkita", "Oltita"], "Toʻrtta",
      f"<p>〜ないで, 〜ないでください, 〜なければなりません va 〜なくてもいいです. "
      f"Shuning uchun bu oʻzakni yasay bilish — toʻrtta qolipni birdan "
      f"qoʻlga kiritish degani.</p>"),

    q(f"<p>{HASHIRU} dan «yugurish shart» ni tanlang.</p>",
      [f"{HASHIRANAI[:-1]}ければなりません", f"{HASHIRU}なければなりません",
       f"{HASHITTE}なければなりません", f"{r('走','はし')}りなければなりません"],
      f"{HASHIRANAI[:-1]}ければなりません",
      f"<p>ない-shakli {HASHIRANAI}, oxirgi <strong>い</strong> tashlanadi va "
      f"ければなりません qoʻyiladi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{KY}で{naidekuda(HASHIRANAI)}", f"{KY}で{HASHIRANAI}ください",
       f"{KY}で{r('走','はし')}りないでください", f"{KY}で{HASHIRU}ないでください"],
      f"{KY}で{naidekuda(HASHIRANAI)}",
      f"<p>{HASHIRU} → {HASHIRANAI} → <strong>{naidekuda(HASHIRANAI)}</strong>. "
      f"で ni tashlab qoʻymang.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{JIKAN}があらない", f"{JIKAN}がありません",
       f"{KY}に{naidekuda(HAIRANAI)}", f"{HON}を{naidekuda(YOMANAI)}"],
      f"{JIKAN}があらない",
      f"<p>ある ning inkori <strong>ない</strong> — «あらない» degan soʻz yoʻq. "
      f"Muloyim shakli esa <strong>ありません</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{MATSU} → {MATANAI}", f"{OYOGU} → {OYOGANAI}",
       f"{KAU} → {r('買','か')}あない", f"{MIRU} → {MINAI}"],
      f"{KAU} → {r('買','か')}あない",
      f"<p>う → <strong>わ</strong>: <strong>{KAWANAI}</strong>. Jadval "
      f"boʻyicha «あ» chiqishi kerak edi, lekin chiqmaydi.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {naidekuda(YOMANAI)} · "
      f"を · {HON} · ここで</p>",
      [f"ここで{HON}を{naidekuda(YOMANAI)}", f"ここを{HON}で{naidekuda(YOMANAI)}",
       f"{naidekuda(YOMANAI)}ここで{HON}を", f"を{HON}ここで{naidekuda(YOMANAI)}"],
      f"ここで{HON}を{naidekuda(YOMANAI)}",
      f"<p>Joy <strong>で</strong> oladi, toʻldiruvchi esa <strong>を</strong>. "
      f"«ここを{HON}で» da ikkalasi almashib qolgan, qolgan ikkitasida esa "
      f"feʼl notoʻgʻri joyda.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"{TSK}で{r('食','た')}べてもいいですか。</p>"
      f"<p><strong>やまもと:</strong> いいえ、___。</p>",
      [naidekuda(TABENAI), f"{TABETE}ください",
       f"{TABENAI[:-1]}くてもいいです", f"{TABETA}ことがあります"],
      naidekuda(TABENAI),
      f"<p>«いいえ» dan keyin taqiq yoki iltimos kelishi kerak: "
      f"<strong>{naidekuda(TABENAI)}</strong>. «{TABETE}ください» — teskari "
      f"maʼno, «{TABENAI[:-1]}くてもいいです» esa «yemasa ham boʻladi».</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-35 — た-shakli va tajriba
# ══════════════════════════════════════════════════════════════════════
Q_PJ35 = [
    q("<p>た-shakli qanday yasaladi?</p>",
      ["て-shaklidan: て → た, で → だ", "ます oʻzagiga た qoʻshiladi",
       "Lugʻat shakliga た qoʻshiladi", "ない-shaklidan"],
      "て-shaklidan: て → た, で → だ",
      f"<p>Bitta harf almashadi: {YONDE} → <strong>{YONDA}</strong>. "
      f"Beshta qoida, uch guruh va istisno — hammasi て-shaklidan meros.</p>"),

    q(f"<p>{OYOGU} ning た-shaklini tanlang.</p>",
      [OYOIDA, r("泳","およ")+"いた", r("泳","およ")+"った", r("泳","およ")+"ぎた"],
      OYOIDA,
      f"<p><strong>{OYOIDA}</strong> — て-shakli {OYOIDE} で bilan tugagan, "
      f"demak た-shakli <strong>だ</strong> bilan.</p>"),

    q(f"<p>{YOMU} ning た-shaklini tanlang.</p>",
      [YONDA, r("読","よ")+"んた", r("読","よ")+"った", r("読","よ")+"みた"],
      YONDA,
      f"<p><strong>{YONDA}</strong> — {YONDE} → {YONDA}. む・ぶ・ぬ feʼllari "
      f"jarangli ulanish oladi, shuning uchun だ.</p>"),

    q(f"<p>{IKU} ning た-shaklini tanlang.</p>",
      [ITTA, r("行","い")+"いた", r("行","い")+"きた", r("行","い")+"んだ"],
      ITTA,
      f"<p><strong>{ITTA}</strong> — istisno ham meros boʻlib oʻtadi: "
      f"て-shakli {ITTE} edi, demak た-shakli {ITTA}. Uni ikkinchi marta "
      f"yodlash shart emas.</p>"),

    q(f"<p>{KAKU} ning た-shaklini tanlang.</p>",
      [KAITA, r("書","か")+"いだ", r("書","か")+"った", r("書","か")+"きた"],
      KAITA,
      f"<p><strong>{KAITA}</strong> — く jarangsiz, shuning uchun いて → "
      f"<strong>いた</strong>. Jarangli ぐ boʻlganda いだ chiqar edi.</p>"),

    q("<p>〜たことがあります nima maʼnoni beradi?</p>",
      ["Qilganman — tajriba", "Kecha qildim", "Qilyapman", "Qilish shart"],
      "Qilganman — tajriba",
      f"<p>Hayotda shunday boʻlgan-boʻlmaganini bildiradi. Qachonligi va "
      f"necha marta boʻlgani muhim emas.</p>"),

    q(f"<p>«Yaponiyaga borganman» ni tanlang.</p>",
      [f"{NIHON}へ{kotoga(ITTA)}", f"{NIHON}へ{r('行','い')}きました",
       f"{NIHON}へ{ITTA}ことをあります", f"{NIHON}へ{ITTE}ことがあります"],
      f"{NIHON}へ{kotoga(ITTA)}",
      f"<p><strong>{kotoga(ITTA)}</strong> — た-shakli + ことがあります. "
      f"«{r('行','い')}きました» esa aniq bir voqea: «bordim».</p>"),

    q("<p>«こと» bu qolipda nima?</p>",
      ["«ish, narsa» degan ot — shuning uchun が oladi",
       "Feʼl — shuning uchun ます oladi",
       "Qoʻshimcha — hech narsa olmaydi",
       "Sifat — shuning uchun です oladi"],
      "«ish, narsa» degan ot — shuning uchun が oladi",
      f"<p>Gap soʻzma-soʻz «borgan <em>ish</em> bor» degani. Shuning uchun "
      f"oxirida ある turadi va こと <strong>が</strong> oladi, を emas.</p>"),

    q(f"<p>{FUJI}に{NOBORU} dan «chiqmaganman» ni tanlang.</p>",
      [kotonai(NOBOTTA), f"{NOBOTTE}ことがありません",
       f"{NOBORANAI}ことがあります", f"{r('登','のぼ')}りませんでした"],
      kotonai(NOBOTTA),
      f"<p><strong>{kotonai(NOBOTTA)}</strong> — ある ning muloyim inkori "
      f"ありません. «{r('登','のぼ')}りませんでした» esa «chiqmadim» — aniq "
      f"voqea, tajriba emas.</p>"),

    q(f"<p>Nega «{r('昨日','きのう')}{kotoga(ITTA)}» notoʻgʻri?</p>",
      ["Chunki aniq vaqt bor — u bilan oddiy oʻtgan zamon ishlatiladi",
       "Chunki 行く — I guruh feʼli",
       "Chunki こと が olmaydi",
       "Chunki gap juda uzun"],
      "Chunki aniq vaqt bor — u bilan oddiy oʻtgan zamon ishlatiladi",
      f"<p>Tajriba qolipi qachonligi <strong>aytilmaganda</strong> ishlatiladi. "
      f"Kecha boʻlgan ish tajriba emas: "
      f"<strong>{r('昨日','きのう')}{r('行','い')}きました</strong>.</p>"),

    q("<p>Bu qolipni oʻzbekchaga qaysi qoʻshimcha bilan tarjima qilish oson?</p>",
      ["«-ganman»", "«-dim»", "«-yapman»", "«-moqchiman»"], "«-ganman»",
      f"<p>«Yaponiyaga bor<strong>ganman</strong>» — tajriba; «Kecha "
      f"bor<strong>dim</strong>» — aniq voqea. Shunday tarjima qilsangiz, "
      f"aniq vaqt qoʻshish istagi ham oʻz-oʻzidan yoʻqoladi.</p>"),

    q("<p>«いいえ、まだありません» nima maʼnoni beradi?</p>",
      ["Hali yoʻq — lekin boʻlishi mumkin", "Umuman boʻlmaydi",
       "Bilmayman", "Ha, boʻlgan"],
      "Hali yoʻq — lekin boʻlishi mumkin",
      f"<p><strong>まだ</strong> «hali» degani va eshikni ochiq qoldiradi. "
      f"Yolgʻiz ありません quruq eshitiladi; yaponlar deyarli doim "
      f"まだ qoʻshadi.</p>"),

    q(f"<p>{TABERU} dan «yeb koʻrganmisiz?» ni tanlang.</p>",
      [f"{kotoga(TABETA)}か", f"{TABETA}ことがありましたか",
       f"{TABETE}ことがありますか", f"{r('食','た')}べましたか"],
      f"{kotoga(TABETA)}か",
      f"<p><strong>{kotoga(TABETA)}か</strong>. ある ni oʻtgan zamonga "
      f"oʻtkazish kerak emas — tajriba <em>hozir</em> bor yoki yoʻq.</p>"),

    q(f"<p>{AU} ning た-shaklini tanlang.</p>",
      [ATTA, r("会","あ")+"いた", r("会","あ")+"んだ", r("会","あ")+"うた"],
      ATTA,
      f"<p><strong>{ATTA}</strong> — う・つ・る → って, demak た-shakli "
      f"<strong>った</strong>.</p>"),

    q(f"<p>{SURU} va {KURU} ning た-shakllari — <strong>した</strong> va "
      f"<strong>来た</strong> — qanday oʻqiladi?</p>",
      ["した・きた", "した・くた", "した・こた", "しった・きった"],
      "した・きた",
      f"<p>て-shakllari {SHITE} va {KITE} edi, demak た-shakllari "
      f"<strong>{SHITA}</strong> va <strong>{KITA}</strong>. 来 ning "
      f"oʻqilishi て-shaklidagidek <strong>き</strong> boʻlib qoladi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"すしを{kotoga(TABETA)}", f"すしを{TABETA}ことをあります",
       f"すしを{TABETE}ことがあります", f"すしを{r('食','た')}べたことがいます"],
      f"すしを{kotoga(TABETA)}",
      f"<p>こと — <strong>ega</strong>, shuning uchun が. Va ある feʼli "
      f"jonsiz narsa bilan keladi, いる emas.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{FUJI}に{kotoga(NOBOTTA)}",
       f"{r('三年前','さんねんまえ')}に{kotoga(ITTA)}",
       f"すしを{kotonai(TABETA)}",
       f"{NIHON}の{SE}に{kotoga(ATTA)}"],
      f"{r('三年前','さんねんまえ')}に{kotoga(ITTA)}",
      f"<p>«{r('三年前','さんねんまえ')}» aniq vaqt — u bilan tajriba qolipi "
      f"ishlatilmaydi. Toʻgʻrisi: <strong>{r('三年前','さんねんまえ')}に"
      f"{r('行','い')}きました</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{OYOIDE} → {OYOIDA}", f"{KAITE} → {KAITA}",
       f"{YONDE} → {r('読','よ')}んた", f"{MITE} → {MITA}"],
      f"{YONDE} → {r('読','よ')}んた",
      f"<p>て-shakli <strong>で</strong> bilan tugasa, た-shakli "
      f"<strong>だ</strong> bilan tugaydi: <strong>{YONDA}</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: ことがあります · "
      f"へ · {NIHON} · {ITTA}</p>",
      [f"{NIHON}へ{kotoga(ITTA)}", f"{ITTA}ことがあります{NIHON}へ",
       f"へ{NIHON}{kotoga(ITTA)}", f"{NIHON}{kotoga(ITTA)}へ"],
      f"{NIHON}へ{kotoga(ITTA)}",
      f"<p>Yoʻnalish qoʻshimchasi へ oʻz otidan keyin turadi, feʼl esa "
      f"undan keyin — va butun こと qismi gap oxirida qoladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム:</strong> "
      f"{FUJI}に{kotoga(NOBOTTA)}か。</p><p><strong>ムニラ:</strong> ___</p>",
      ["いいえ、まだありません。", "いいえ、まだいません。",
       "いいえ、まだしません。", f"いいえ、{r('登','のぼ')}りません。"],
      "いいえ、まだありません。",
      f"<p>Savol ある bilan berilgan, demak javob ham ある bilan qaytadi: "
      f"<strong>ありません</strong>. います jonli narsalar uchun.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-36 — 〜たり〜たりします
# ══════════════════════════════════════════════════════════════════════
Q_PJ36 = [
    q("<p>〜たり qanday yasaladi?</p>",
      ["た-shakliga り qoʻshiladi", "て-shakliga り qoʻshiladi",
       "ない-shakliga り qoʻshiladi", "Lugʻat shakliga り qoʻshiladi"],
      "た-shakliga り qoʻshiladi",
      f"<p>{YONDA} → <strong>{tari(YONDA)}</strong>. «{YONDE}り» notoʻgʻri: "
      f"り <strong>た</strong>-shaklga qoʻshiladi.</p>"),

    q(f"<p>{MIRU} dan たり yasang.</p>",
      [tari(MITA), r("見","み")+"てり", r("見","み")+"るり", r("見","み")+"だり"],
      tari(MITA),
      f"<p><strong>{tari(MITA)}</strong> — た-shakli {MITA}, keyin り.</p>"),

    q(f"<p>{OYOGU} dan たり yasang.</p>",
      [tari(OYOIDA), r("泳","およ")+"いたり", r("泳","およ")+"ぎたり", r("泳","およ")+"ったり"],
      tari(OYOIDA),
      f"<p><strong>{tari(OYOIDA)}</strong> — で → だ, keyin り. Jaranglilik "
      f"て-shaklidan meros.</p>"),

    q("<p>Gapning zamonini nima hal qiladi?</p>",
      ["Oxirdagi する", "Birinchi たり", "Oxirgi たり", "Gapdagi vaqt soʻzi"],
      "Oxirdagi する",
      f"<p>たり qismlari <strong>hech qachon oʻzgarmaydi</strong>. "
      f"します — hozirgi, しました — oʻtgan zamon.</p>"),

    q(f"<p>«Kitob oʻqiyman, musiqa tinglayman — shunaqa ishlar» ni tanlang.</p>",
      [f"{HON}を{tari(YONDA)}、{ONGAKU}を{tari(KIITA)}します",
       f"{HON}を{tari(YONDA)}、{ONGAKU}を{r('聞','き')}きます",
       f"{HON}を{YONDE}、{ONGAKU}を{KIITE}します",
       f"{HON}を{tari(YONDA)}、{ONGAKU}を{tari(KIITA)}です"],
      f"{HON}を{tari(YONDA)}、{ONGAKU}を{tari(KIITA)}します",
      f"<p>Ikkalasi ham たり boʻladi, gapni esa <strong>します</strong> "
      f"yopadi. Sifat emas — です qoʻyilmaydi.</p>"),

    q("<p>〜て va 〜たり farqi nima?</p>",
      ["〜て tartibni koʻrsatadi, 〜たり misol keltiradi",
       "〜て misol keltiradi, 〜たり tartibni koʻrsatadi",
       "Farqi yoʻq",
       "〜たり faqat oʻtgan zamonda ishlatiladi"],
      "〜て tartibni koʻrsatadi, 〜たり misol keltiradi",
      f"<p>{YONDE}、{r('寝','ね')}ました — avval oʻqidim, <em>keyin</em> "
      f"uxladim. {tari(YONDA)}、{tari(r('寝','ね')+'た')}しました — shunaqa "
      f"ishlar qildim, tartib muhim emas.</p>"),

    q("<p>〜たり ishlatilgan roʻyxat qanday roʻyxat?</p>",
      ["Ochiq — «shunaqa ishlar», hammasi emas",
       "Yopiq — aynan shu ishlar, boshqasi yoʻq",
       "Vaqt tartibida joylashgan",
       "Muhimlik tartibida joylashgan"],
      "Ochiq — «shunaqa ishlar», hammasi emas",
      f"<p>Ikkita ish aytiladi, lekin maʼnosi «faqat shu ikkitasi» emas. "
      f"Bu — <strong>misol</strong>.</p>"),

    q("<p>Odatda nechta たり ishlatiladi?</p>",
      ["Ikkita", "Bitta", "Toʻrtta", "Beshta"], "Ikkita",
      f"<p>Odatda ikkita, koʻpi bilan uchta. Bittasi ham mumkin — unda "
      f"maʼno «masalan, shu» boʻlib qoladi.</p>"),

    q(f"<p>«{tari(ITTA)}{tari(KITA)}します» nima maʼnoni beradi?</p>",
      ["Borib-kelib turadi — takror-takror", "Bordi va qaytmadi",
       "Borish yoki kelish", "Bormoqchi"],
      "Borib-kelib turadi — takror-takror",
      f"<p>Qarama-qarshi juftlikda maʼno «misol» emas, "
      f"<strong>takrorlanish</strong> boʻladi.</p>"),

    q(f"<p>Nega gap oxirida する turadi?</p>",
      ["Chunki たり qismlari gap tugatmaydi — bitta kesim kerak",
       "Chunki する — III guruh feʼli",
       "Chunki bu odat maʼnosini beradi",
       "Chunki ikkita ish sanalgan"],
      "Chunki たり qismlari gap tugatmaydi — bitta kesim kerak",
      f"<p>たり qismlari «shunaqa ish» degan atamaning boʻlagiga aylanadi, "
      f"va butun roʻyxatni bitta feʼl — <strong>する</strong> — yopadi. "
      f"Shuning uchun zamon ham faqat oʻshanda.</p>"),

    q(f"<p>{SOUJI}する dan たり yasang.</p>",
      [f"{SOUJI}したり", f"{SOUJI}するり", f"{SOUJI}してり", f"{SOUJI}しるたり"],
      f"{SOUJI}したり",
      f"<p>する ning た-shakli {SHITA}, demak <strong>{SOUJI}したり</strong>. "
      f"Barcha する-feʼllari shu yoʻldan boradi.</p>"),

    q(f"<p>«Shanba kuni suzdim, rasmga oldim» ni tanlang.</p>",
      [f"{tari(OYOIDA)}、{SHASHIN}を{tari(TOTTA)}しました",
       f"{tari(OYOIDA)}、{SHASHIN}を{tari(TOTTA)}します",
       f"{tari(OYOIDA)}、{SHASHIN}を{r('撮','と')}りました",
       f"{tari(OYOIDA)}、{SHASHIN}を{tari(TOTTA)}しましたり"],
      f"{tari(OYOIDA)}、{SHASHIN}を{tari(TOTTA)}しました",
      f"<p>Oʻtgan zamon — <strong>しました</strong>. Oxirgi する たり "
      f"olmaydi: u gapni tugatadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NICHI}に"
      f"{r('公園','こうえん')}で{tari(YASUNDA)}、{r('友','とも')}だちに"
      f"{tari(ATTA)}___。</strong></p>",
      ["します", "あります", "です", "いきます"], "します",
      f"<p><strong>します</strong> — たり roʻyxatini doim する yopadi. "
      f"あります mavjudlik feʼli, bu yerga toʻgʻri kelmaydi.</p>"),

    q(f"<p>«{tari(YONDA)}» va «{YONDE}» — qaysi biri roʻyxatni ochiq "
      f"qoldiradi?</p>",
      [f"{tari(YONDA)}", f"{YONDE}", "Ikkalasi ham", "Hech qaysi"],
      f"{tari(YONDA)}",
      f"<p>〜たり «masalan, shular» degan maʼno beradi. 〜て esa aniq "
      f"tartibni koʻrsatadi va roʻyxat toʻliq hisoblanadi.</p>"),

    q(f"<p>Sanalgan ishlar qanday boʻlgani maʼqul?</p>",
      ["Maʼnoda bir-biriga yaqin", "Bir xil guruhdagi feʼllar",
       "Bir xil uzunlikdagi soʻzlar", "Har xil zamonda"],
      "Maʼnoda bir-biriga yaqin",
      f"<p>Dam olish kuni qiladigan ishlar, uyda qiladigan ishlar — bir "
      f"toifadan. Butunlay bogʻlanmagan ikki ish gapni gʻalati qiladi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{tari(YASUNDA)}、{BENKYOU}したりします",
       f"{tari(YASUNDA)}、{BENKYOU}します",
       f"{YASUNDE}、{BENKYOU}したりします",
       f"{tari(YASUNDA)}、{BENKYOU}したりです"],
      f"{tari(YASUNDA)}、{BENKYOU}したりします",
      f"<p>Ikkala ish ham たり shaklida, oxirida esa <strong>します</strong>. "
      f"Aralashtirib boʻlmaydi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{tari(MITA)}、{tari(KIITA)}します",
       f"{tari(YONDA)}、{r('寝','ね')}ました",
       f"{tari(OYOIDA)}、{tari(r('遊','あそ')+'んだ')}しました",
       f"{SOUJI}したり、{r('買','か')}い{r('物','もの')}したりします"],
      f"{tari(YONDA)}、{r('寝','ね')}ました",
      f"<p>Ikkinchisi ham たり boʻlishi kerak edi, gapni esa します yopishi: "
      f"<strong>{tari(YONDA)}、{tari(r('寝','ね')+'た')}しました</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{MITA} → {tari(MITA)}", f"{OYOIDA} → {tari(OYOIDA)}",
       f"{YONDE} → {r('読','よ')}んでり", f"{SHITA} → {tari(SHITA)}"],
      f"{YONDE} → {r('読','よ')}んでり",
      f"<p>り <strong>た</strong>-shaklga qoʻshiladi, て-shaklga emas: "
      f"<strong>{tari(YONDA)}</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: します · {tari(KIITA)} · "
      f"を · {ONGAKU}</p>",
      [f"{ONGAKU}を{tari(KIITA)}します", f"{tari(KIITA)}{ONGAKU}をします",
       f"を{ONGAKU}{tari(KIITA)}します", f"{ONGAKU}{tari(KIITA)}をします"],
      f"{ONGAKU}を{tari(KIITA)}します",
      f"<p>Toʻldiruvchi va uning を qoʻshimchasi たり dan oldin turadi, "
      f"します esa gapni yopadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"{NICHI}に{r('何','なに')}をしたりしますか。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"{HON}を{tari(YONDA)}、{ONGAKU}を{tari(KIITA)}します",
       f"{HON}を{r('読','よ')}みます",
       f"{HON}を{YONDE}、{ONGAKU}を{KIITE}します",
       f"{HON}を{tari(YONDA)}、{ONGAKU}を{tari(KIITA)}です"],
      f"{HON}を{tari(YONDA)}、{ONGAKU}を{tari(KIITA)}します",
      f"<p>Ikkala ish ham たり shaklida va gapni <strong>します</strong> "
      f"yopadi. です qoʻyilmaydi — たり roʻyxati feʼl bilan tugaydi, "
      f"sifat bilan emas.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-34 Mashq: ない-shakli va 〜ないでください",
        "tutorial":    "PJ-34:",
        "description": "Inkor oʻzagi uchala guruhda, uchta tuzoq (買わない, "
                       "来ない, ある → ない) va «qilmang» degan gap.",
        "questions":   Q_PJ34,
        **DEFAULTS,
    },
    {
        "title":       "PJ-35 Mashq: た-shakli va 〜たことがあります",
        "tutorial":    "PJ-35:",
        "description": "て → た, で → だ. Tajriba qolipi va uni oddiy oʻtgan "
                       "zamondan ajratish.",
        "questions":   Q_PJ35,
        **DEFAULTS,
    },
    {
        "title":       "PJ-36 Mashq: 〜たり〜たりします",
        "tutorial":    "PJ-36:",
        "description": "Ishlarni misol tariqasida sanash. Roʻyxat ochiq "
                       "qoladi, zamonni esa faqat oxirdagi する tashiydi.",
        "questions":   Q_PJ36,
        **DEFAULTS,
    },
]
