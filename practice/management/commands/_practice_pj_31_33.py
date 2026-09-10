# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-31 … PJ-33.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

⚠️ Feʼl shakllari toʻliq konstanta sifatida yoziladi (YOMU / YONDE), oʻzak +
qoʻshimcha sifatida emas. Lekin て-shakliga qoʻshimcha ulash XAVFSIZ: bu
haqiqiy morfema chegarasi va u yerda hech narsa oʻzgarmaydi — shuning uchun
ています / てください / てはいけません pastdagi yordamchilar bilan yasaladi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_31_33.py --master=prime \\
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

# ── lugʻat · ます · て ────────────────────────────────────────────────
YOMU,  YOMIMASU,  YONDE   = r("読","よ")+"む",   r("読","よ")+"みます",   r("読","よ")+"んで"
KAKU,  KAKIMASU,  KAITE   = r("書","か")+"く",   r("書","か")+"きます",   r("書","か")+"いて"
HANASU,HANASHIMASU,HANASHITE = r("話","はな")+"す", r("話","はな")+"します", r("話","はな")+"して"
MATSU, MACHIMASU, MATTE   = r("待","ま")+"つ",   r("待","ま")+"ちます",   r("待","ま")+"って"
NOMU,  NOMIMASU,  NONDE   = r("飲","の")+"む",   r("飲","の")+"みます",   r("飲","の")+"んで"
OYOGU, OYOGIMASU, OYOIDE  = r("泳","およ")+"ぐ", r("泳","およ")+"ぎます", r("泳","およ")+"いで"
HASHIRU,HASHIRIMASU,HASHITTE = r("走","はし")+"る", r("走","はし")+"ります", r("走","はし")+"って"
TSUKAU,TSUKAIMASU,TSUKATTE = r("使","つか")+"う", r("使","つか")+"います", r("使","つか")+"って"
SUWARU,SUWARIMASU,SUWATTE = r("座","すわ")+"る", r("座","すわ")+"ります", r("座","すわ")+"って"
TATSU, TACHIMASU, TATTE   = r("立","た")+"つ",   r("立","た")+"ちます",   r("立","た")+"って"
SUMU,  SUMIMASU,  SUNDE   = r("住","す")+"む",   r("住","す")+"みます",   r("住","す")+"んで"
MOTSU, MOCHIMASU, MOTTE   = r("持","も")+"つ",   r("持","も")+"ちます",   r("持","も")+"って"
SHIRU, SHIRIMASU, SHITTE  = r("知","し")+"る",   r("知","し")+"ります",   r("知","し")+"って"
# «bilmayman» — bu feʼlning INKORI, va aynan u yagona istisno. Ijobiy shakl
# (知ります) deyarli ishlatilmaydi, shuning uchun ikkalasi alohida turadi.
SHIRIMASEN = r("知","し")+"りません"
IKU,   IKIMASU,   ITTE    = r("行","い")+"く",   r("行","い")+"きます",   r("行","い")+"って"
KAERU, KAERIMASU, KAETTE  = r("帰","かえ")+"る", r("帰","かえ")+"ります", r("帰","かえ")+"って"
KAU,   KAIMASU,   KATTE   = r("買","か")+"う",   r("買","か")+"います",   r("買","か")+"って"
TABERU,TABEMASU,  TABETE  = r("食","た")+"べる", r("食","た")+"べます", r("食","た")+"べて"
MIRU,  MIMASU,    MITE    = r("見","み")+"る",   r("見","み")+"ます",   r("見","み")+"て"
AKERU, AKEMASU,   AKETE   = r("開","あ")+"ける", r("開","あ")+"けます", r("開","あ")+"けて"
MISERU,MISEMASU,  MISETE  = r("見","み")+"せる", r("見","み")+"せます", r("見","み")+"せて"
OSHIERU,OSHIEMASU,OSHIETE = r("教","おし")+"える", r("教","おし")+"えます", r("教","おし")+"えて"
KURU,  KIMASU,    KITE    = r("来","く")+"る",   r("来","き")+"ます",   r("来","き")+"て"

# ── て-shakliga ulanadigan qoliplar ───────────────────────────────────
# Bu chegarada hech narsa oʻzgarmaydi, shuning uchun ulash xavfsiz.
def teiru(te):    return te + "います"
def kudasai(te):  return te + "ください"
def temoii(te):   return te + "もいいです"
def teikenai(te): return te + "はいけません"

SURU, SHIMASU, SHITE = "する", "します", "して"
BENKYOU = r("勉強","べんきょう")
SHUKUDAI, MADO, SHASHIN = r("宿題","しゅくだい"), r("窓","まど"), r("写真","しゃしん")
HON, GK, KY, SE = r("本","ほん"), r("学校","がっこう"), r("教室","きょうしつ"), r("先生","せんせい")
NG, WA, TSK = r("日本語","にほんご"), r("私","わたし"), r("図書館","としょかん")
IMA, KISOKU, KYOKASHO = r("今","いま"), r("規則","きそく"), r("教科書","きょうかしょ")


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-31 — 〜ています
# ══════════════════════════════════════════════════════════════════════
Q_PJ31 = [
    q("<p>〜ています qanday yasaladi?</p>",
      ["て-shakli + います", "ます oʻzagi + います",
       "Lugʻat shakli + います", "ない-shakli + います"],
      "て-shakli + います",
      f"<p><strong>て-shakli + います</strong>: {YONDE} + います → "
      f"{teiru(YONDE)}. «{r('読','よ')}みています» notoʻgʻri.</p>"),

    q(f"<p>{TABERU} dan «yeyapti» ni tanlang.</p>",
      [teiru(TABETE), f"{r('食','た')}べていります",
       f"{r('食','た')}べっています", f"{r('食','た')}べるています"],
      teiru(TABETE),
      f"<p><strong>{teiru(TABETE)}</strong> — II guruh: る → て, keyin います.</p>"),

    q(f"<p>{YOMU} dan «hozir oʻqiyapti» ni tanlang.</p>",
      [teiru(YONDE), f"{r('読','よ')}みています",
       f"{r('読','よ')}んています", f"{r('読','よ')}むています"],
      teiru(YONDE),
      f"<p><strong>{teiru(YONDE)}</strong> — む → んで, keyin います. "
      f"て-shakli PJ-30 dagi beshta qoidadan chiqadi.</p>"),

    q(f"<p>{OYOGU} dan «suzyapti» ni tanlang.</p>",
      [teiru(OYOIDE), f"{r('泳','およ')}いています",
       f"{r('泳','およ')}ぎています", f"{r('泳','およ')}っています"],
      teiru(OYOIDE),
      f"<p><strong>{teiru(OYOIDE)}</strong> — ぐ jarangli, demak "
      f"<strong>いで</strong>, keyin います.</p>"),

    q(f"<p>{BENKYOU}する dan «oʻqiyapti» ni tanlang.</p>",
      [f"{BENKYOU}しています", f"{BENKYOU}すています",
       f"{BENKYOU}するています", f"{BENKYOU}しっています"],
      f"{BENKYOU}しています",
      f"<p><strong>{BENKYOU}しています</strong> — する ning て-shakli して, "
      f"keyin います.</p>"),

    q(f"<p>{teiru(YONDE)} ning inkorini tanlang.</p>",
      [f"{YONDE}いません", f"{YONDE}ありません",
       f"{r('読','よ')}みません", f"{YONDE}くないです"],
      f"{YONDE}いません",
      f"<p><strong>{YONDE}いません</strong> — «oʻqimayapti». います oddiy "
      f"feʼl, shuning uchun odatdagidek いません boʻladi. て-shakli esa hech "
      f"qachon oʻzgarmaydi.</p>"),

    q(f"<p>{teiru(KAITE)} ning oʻtgan zamonini tanlang.</p>",
      [f"{KAITE}いました", f"{KAITE}いますでした",
       f"{r('書','か')}きました", f"{KAITE}かったです"],
      f"{KAITE}いました",
      f"<p><strong>{KAITE}いました</strong> — «yozayotgan edi». Zamonni "
      f"います tashiydi, て-shakli qimirlamaydi.</p>"),

    q(f"<p>«Hozir nima qilyapsiz?» ni tanlang.</p>",
      [f"{IMA}{r('何','なに')}をしていますか", f"{IMA}{r('何','なに')}をしますか",
       f"{IMA}{r('何','なに')}をしましたか", f"{IMA}{r('何','なに')}をしてください"],
      f"{IMA}{r('何','なに')}をしていますか",
      f"<p><strong>していますか</strong> — ayni damda. «しますか» esa «qilasizmi» "
      f"degan savol: odat yoki kelasi zamon.</p>"),

    q(f"<p>«Toshkentda yashayman» ni tanlang.</p>",
      [f"タシケントに{teiru(SUNDE)}", f"タシケントに{SUMIMASU}",
       f"タシケントに{SUMU}", f"タシケントで{SUMIMASU}"],
      f"タシケントに{teiru(SUNDE)}",
      f"<p><strong>{teiru(SUNDE)}</strong> — {SUMU} doim ています shaklida "
      f"turadi. Bu davom etayotgan ish emas, <strong>holat</strong>: bir marta "
      f"koʻchib kelgan, natijasi hozir davom etyapti.</p>"),

    q("<p>«Bilmayman» yaponchada qanday?</p>",
      [f"{SHITTE}いません", SHIRIMASEN,
       f"{r('知','し')}りていません", f"{r('知','し')}りましていません"],
      SHIRIMASEN,
      f"<p><strong>{SHIRIMASEN}</strong>. Bu butun kursdagi yagona "
      f"istisno: «bilish» — holat, u <em>bor</em> yoki <em>yoʻq</em>, shuning "
      f"uchun inkor ています dan emas, oddiy shakldan yasaladi.</p>"),

    q("<p>«Bilaman» yaponchada qanday?</p>",
      [SHIRIMASU, teiru(SHITTE), SHIRU, f"{r('知','し')}っていました"],
      teiru(SHITTE),
      f"<p><strong>{teiru(SHITTE)}</strong> — ijobiy tomonda ています "
      f"ishlatiladi, inkorda esa <strong>{SHIRIMASEN}</strong>. Bu juftlikni "
      f"birga yodlang: shakllari bir-biriga mos kelmaydi.</p>"),

    q(f"<p>{YOMIMASU} va {teiru(YONDE)} — farqi nima?</p>",
      ["Birinchisi odat yoki kelasi, ikkinchisi hozir davom etyapti",
       "Birinchisi hozir, ikkinchisi kelasi zamon",
       "Farqi yoʻq",
       "Birinchisi muloyimroq"],
      "Birinchisi odat yoki kelasi, ikkinchisi hozir davom etyapti",
      f"<p>{YOMIMASU} — «oʻqiyman». {teiru(YONDE)} — «hozir oʻqiyapman». "
      f"Oʻzbekchada ham xuddi shu juftlik bor: «oʻqiyman» va «oʻqi<strong>yapman"
      f"</strong>».</p>"),

    q(f"<p>Nega «{teiru(SUNDE)}» davom etayotgan ish emas?</p>",
      ["Chunki 住む bir zumda tugaydigan ish — ています uning natijasini bildiradi",
       "Chunki 住む — II guruh feʼli",
       "Chunki 住む doim oʻtgan zamonda ishlatiladi",
       "Chunki 住む sifat"],
      "Chunki 住む bir zumda tugaydigan ish — ています uning natijasini bildiradi",
      f"<p>Koʻchib kelish bir zumda tugaydi. Shuning uchun {teiru(SUNDE)} "
      f"«koʻchib boryapti» emas, <strong>«hozir shu yerda yashaydi»</strong> "
      f"degani — qolgan holat.</p>"),

    q(f"<p>«{r('学校','がっこう')}で{NG}を{OSHIETE}います» — bu nima maʼnoni beradi?</p>",
      ["Uning ishi shu — maktabda yapon tili oʻqitadi",
       "Hozir shu daqiqada dars berayotir, boshqa maʼno yoʻq",
       "Kecha oʻqitgan edi",
       "Oʻqitmoqchi"],
      "Uning ishi shu — maktabda yapon tili oʻqitadi",
      f"<p>ています ning uchinchi vazifasi — <strong>muntazam mashgʻulot</strong>. "
      f"Kasb va doimiy ish doim shu shaklda aytiladi.</p>"),

    q(f"<p>Qaysi feʼl <strong>doim</strong> ています shaklida turadi?</p>",
      [SUMU, YOMU, TABERU, OYOGU], SUMU,
      f"<p><strong>{SUMU}</strong> — «yashamoq». U bilan bir qatorda "
      f"{SHIRU}, {MOTSU} va {r('結婚','けっこん')}する ham doim ています "
      f"shaklida ishlatiladi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WA}は{r('名前','なまえ')}を{teiru(SHITTE)}",
       f"{WA}は{r('名前','なまえ')}を{r('知','し')}りています",
       f"{WA}は{r('名前','なまえ')}を{SHIRU}います",
       f"{WA}は{r('名前','なまえ')}を{r('知','し')}っていります"],
      f"{WA}は{r('名前','なまえ')}を{teiru(SHITTE)}",
      f"<p><strong>{teiru(SHITTE)}</strong> — «bilaman». Bu feʼlning oddiy "
      f"shakli faqat <em>inkorda</em> ishlatiladi: {SHIRIMASEN}.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{IMA}{HON}を{teiru(YONDE)}",
       f"タシケントに{SUMIMASU}",
       f"{teiru(TABETE)}",
       f"{BENKYOU}しています"],
      f"タシケントに{SUMIMASU}",
      f"<p>{SUMU} doim ています shaklida turadi: "
      f"<strong>{teiru(SUNDE)}</strong>. «{SUMIMASU}» deb aytilmaydi.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TABERU} → {teiru(TABETE)}", f"{YOMU} → {r('読','よ')}みています",
       f"{OYOGU} → {teiru(OYOIDE)}", f"{MIRU} → {teiru(MITE)}"],
      f"{YOMU} → {r('読','よ')}みています",
      f"<p>ています <strong>ます oʻzagiga emas, て-shakliga</strong> qoʻshiladi: "
      f"{YOMU} → {YONDE} → <strong>{teiru(YONDE)}</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {teiru(SHITE)} · "
      f"を · {SHUKUDAI} · {IMA}</p>",
      [f"{IMA}{SHUKUDAI}を{teiru(SHITE)}", f"{SHUKUDAI}を{IMA}{teiru(SHITE)}",
       f"{teiru(SHITE)}{IMA}{SHUKUDAI}を", f"を{SHUKUDAI}{IMA}{teiru(SHITE)}"],
      f"{IMA}{SHUKUDAI}を{teiru(SHITE)}",
      f"<p><strong>{IMA}{SHUKUDAI}を{teiru(SHITE)}</strong> — «hozir uy "
      f"vazifasi qilyapman». Vaqt soʻzi oldinda, feʼl doim oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>パリ:</strong> "
      f"ムニラさんはどこに{teiru(SUNDE)}か。</p><p><strong>ラノ:</strong> ___</p>",
      [f"サマルカンドに{teiru(SUNDE)}", f"サマルカンドに{SUMIMASU}",
       f"サマルカンドに{SUMU}", f"サマルカンドに{SUNDE}ください"],
      f"サマルカンドに{teiru(SUNDE)}",
      f"<p>Savol qaysi shaklda berilsa, javob ham shu shaklda qaytadi — "
      f"yapon suhbatining odatiy qoidasi. Va {SUMU} baribir doim ています "
      f"shaklida turadi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-32 — 〜てください va 〜てもいいです
# ══════════════════════════════════════════════════════════════════════
Q_PJ32 = [
    q("<p>〜てください nima maʼnoni beradi?</p>",
      ["Iltimos, qiling", "Qilsam boʻladimi?", "Qilish mumkin emas", "Qilyapman"],
      "Iltimos, qiling",
      f"<p><strong>{kudasai(MATTE)}</strong> — «kuting». Muloyim, lekin "
      f"baribir koʻrsatma: oʻqituvchi, shifokor, doʻkonchi shunday "
      f"gapiradi.</p>"),

    q(f"<p>{MATSU} dan «kuting» ni tanlang.</p>",
      [kudasai(MATTE), f"{r('待','ま')}ちてください",
       f"{r('待','ま')}つください", f"{MACHIMASU}ください"],
      kudasai(MATTE),
      f"<p><strong>{kudasai(MATTE)}</strong> — ください <strong>て-shaklga</strong> "
      f"qoʻshiladi, ます oʻzagiga emas.</p>"),

    q(f"<p>{SUWARU} dan «oʻtiring» ni tanlang.</p>",
      [kudasai(SUWATTE), f"{r('座','すわ')}りてください",
       f"{r('座','すわ')}るください", f"{r('座','すわ')}んでください"],
      kudasai(SUWATTE),
      f"<p><strong>{kudasai(SUWATTE)}</strong> — {SUWARU} I guruh, "
      f"る → って.</p>"),

    q(f"<p>{YOMU} dan «oʻqing» ni tanlang.</p>",
      [kudasai(YONDE), f"{r('読','よ')}んてください",
       f"{r('読','よ')}みてください", f"{r('読','よ')}ってください"],
      kudasai(YONDE),
      f"<p><strong>{kudasai(YONDE)}</strong> — む → んで (jarangli), keyin "
      f"ください.</p>"),

    q(f"<p>{KURU} dan «keling» — <strong>来てください</strong> — qanday "
      f"oʻqiladi?</p>",
      ["きてください", "くてください", "こてください", "きりてください"],
      "きてください",
      f"<p><strong>きてください</strong>. Kanji oʻsha turadi, lekin oʻqilishi "
      f"て-shaklida <strong>き</strong> ga oʻtadi: {KURU} «くる», "
      f"{KITE} «きて». Buni faqat furigana koʻrsatadi.</p>"),

    q("<p>〜てもいいですか nima maʼnoni beradi?</p>",
      ["Qilsam boʻladimi?", "Iltimos, qiling",
       "Qilish shart", "Qilib boʻlmaydi"],
      "Qilsam boʻladimi?",
      f"<p>Bu <strong>oʻzingizga</strong> ruxsat soʻraydi. Soʻzma-soʻz maʼnosi "
      f"«qilsa <em>ham</em> yaxshi»: も «ham», いい «yaxshi» — ikkalasi ham "
      f"tanish soʻzlar.</p>"),

    q(f"<p>«Derazani ochsam boʻladimi?» ni tanlang.</p>",
      [f"{MADO}を{temoii(AKETE)}か", f"{MADO}を{kudasai(AKETE)}",
       f"{MADO}を{AKETE}はいいですか", f"{MADO}を{AKEMASU}もいいですか"],
      f"{MADO}を{temoii(AKETE)}か",
      f"<p><strong>{temoii(AKETE)}か</strong> — て + もいいです + か. "
      f"«{kudasai(AKETE)}» esa «oching» — yoʻnalish teskari.</p>"),

    q(f"<p>«Rasmga olsam boʻladimi?» ni tanlang.</p>",
      [f"{SHASHIN}を{temoii(r('撮','と')+'って')}か",
       f"{SHASHIN}を{r('撮','と')}りてもいいですか",
       f"{SHASHIN}を{r('撮','と')}るもいいですか",
       f"{SHASHIN}を{r('撮','と')}んでもいいですか"],
      f"{SHASHIN}を{temoii(r('撮','と')+'って')}か",
      f"<p>{r('撮','と')}る I guruh, る → <strong>って</strong>, keyin "
      f"もいいですか.</p>"),

    q(f"<p>«{temoii(SUWATTE)}» ning yasalishida いい nima?</p>",
      ["い-sifat — shuning uchun です oladi, います emas",
       "Feʼl — shuning uchun います oladi",
       "Ot — shuning uchun の oladi",
       "Qoʻshimcha — hech narsa olmaydi"],
      "い-sifat — shuning uchun です oladi, います emas",
      f"<p>いい — PJ-25 dagi «yaxshi» sifati. Sifat kesim boʻlganda "
      f"<strong>です</strong> oladi, shuning uchun «いいますか» notoʻgʻri.</p>"),

    q("<p>«はい、いいですよ。どうぞ。» nima maʼnoni beradi?</p>",
      ["Ruxsat berilyapti", "Rad qilinyapti",
       "Savol berilyapti", "Buyruq berilyapti"],
      "Ruxsat berilyapti",
      f"<p><strong>どうぞ</strong> — «marhamat, bemalol». U eshikni ochib "
      f"turib ham, choy uzatib turib ham aytiladi, gapsiz ham ishlaydi.</p>"),

    q("<p>«すみません、ちょっと…» nima maʼnoni beradi?</p>",
      ["Muloyim rad javobi", "Ruxsat berish",
       "Yana bir marta soʻrash", "Kechikkani uchun uzr"],
      "Muloyim rad javobi",
      f"<p>Gap <strong>ataylab tugatilmaydi</strong> — yaponchada «yoʻq» "
      f"koʻpincha aytilmaydi, lekin suhbatdosh hammasini tushunadi. "
      f"Oʻzbekchada ham «Hozir bir oz…» deb qoʻyamiz.</p>"),

    q(f"<p>{kudasai(MISETE)} va {temoii(MISETE)}か — farqi nima?</p>",
      ["Birinchisi «sen koʻrsat», ikkinchisi «men koʻrsatsam boʻladimi»",
       "Birinchisi muloyimroq",
       "Birinchisi oʻtgan zamonda",
       "Farqi yoʻq"],
      "Birinchisi «sen koʻrsat», ikkinchisi «men koʻrsatsam boʻladimi»",
      f"<p>Yoʻnalish qarama-qarshi: <strong>ください</strong> bilan siz "
      f"suhbatdoshga aytasiz, <strong>もいいですか</strong> bilan esa "
      f"undan oʻzingizga ruxsat soʻraysiz.</p>"),

    q("<p>«Qilmang» degan gapni bugungi qolip bilan aytib boʻladimi?</p>",
      ["Yoʻq — uning oʻz shakli bor, ない-shaklidan yasaladi",
       "Ha — てくださいません deyiladi",
       "Ha — てもいいませんか deyiladi",
       "Ha — てくださいではありません deyiladi"],
      "Yoʻq — uning oʻz shakli bor, ない-shaklidan yasaladi",
      f"<p>て-shakli oʻzi ijobiy; unga ください qoʻshib inkor chiqarib "
      f"boʻlmaydi. «Qilmang» — <strong>〜ないでください</strong>, va u "
      f"boshqa oʻzakdan yasaladi.</p>"),

    q(f"<p>{SE} tez gapirdi va siz tushunmadingiz. Nima deysiz?</p>",
      [f"もう{r('一度','いちど')}{kudasai(r('言','い')+'って')}",
       f"{SHASHIN}を{temoii(r('撮','と')+'って')}か",
       f"{MADO}を{kudasai(AKETE)}", f"{kudasai(SUWATTE)}"],
      f"もう{r('一度','いちど')}{kudasai(r('言','い')+'って')}",
      f"<p><strong>もう{r('一度','いちど')}{kudasai(r('言','い')+'って')}</strong> "
      f"— «yana bir marta ayting». Qolgan uchtasi deraza, rasm va oʻtirish "
      f"haqida: tushunmaganda ular yordam bermaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{KYOKASHO}を{kudasai(AKETE)}", f"{KYOKASHO}を{AKEMASU}ください",
       f"{KYOKASHO}を{AKERU}ください", f"{KYOKASHO}を{r('開','あ')}けりてください"],
      f"{KYOKASHO}を{kudasai(AKETE)}",
      f"<p>{AKERU} II guruh: る → て, keyin ください. Boshqa yoʻl yoʻq.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{HON}を{temoii(YONDE)}か", f"{HON}を{YONDE}もいいますか",
       f"{HON}を{YOMIMASU}もいいですか", f"{HON}を{YOMU}もいいですか"],
      f"{HON}を{temoii(YONDE)}か",
      f"<p>もいいです <strong>て-shaklga</strong> qoʻshiladi, va いい sifat "
      f"boʻlgani uchun <strong>です</strong> oladi — «いいます» emas.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [kudasai(TATTE), kudasai(MITE), f"{r('聞','き')}きてください", kudasai(HANASHITE)],
      f"{r('聞','き')}きてください",
      f"<p>{r('聞','き')}く I guruh, く → <strong>いて</strong>: "
      f"<strong>{kudasai(r('聞','き')+'いて')}</strong>. «きいて» ni ます "
      f"oʻzagi «きき» bilan aralashtirmang.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TABERU} → {kudasai(TABETE)}", f"{IKU} → {kudasai(ITTE)}",
       f"{KAU} → {r('買','か')}いてください", f"{HANASU} → {kudasai(HANASHITE)}"],
      f"{KAU} → {r('買','か')}いてください",
      f"<p>{KAU} う bilan tugaydi, demak <strong>って</strong>: "
      f"<strong>{kudasai(KATTE)}</strong>. «いて» faqat く feʼllariniki.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: ください · を · "
      f"{KYOKASHO} · {AKETE}</p>",
      [f"{KYOKASHO}を{kudasai(AKETE)}", f"{kudasai(AKETE)}{KYOKASHO}を",
       f"を{KYOKASHO}{kudasai(AKETE)}", f"{KYOKASHO}{kudasai(AKETE)}を"],
      f"{KYOKASHO}を{kudasai(AKETE)}",
      f"<p>Toʻldiruvchi va uning を qoʻshimchasi feʼldan oldin turadi, "
      f"ください esa て-shaklga yopishib gap oxirida qoladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イムロン:</strong> "
      f"{SE}、{MADO}を{temoii(AKETE)}か。</p><p><strong>やまだ:</strong> ___</p>",
      ["はい、いいですよ。どうぞ。", "はい、いいますよ。どうぞ。",
       f"いいえ、{AKEMASU}", f"はい、{AKERU}もいいです"],
      "はい、いいですよ。どうぞ。",
      f"<p>いい — <strong>sifat</strong>, shuning uchun です oladi: "
      f"«いいますよ» notoʻgʻri. Va もいいです て-shaklga qoʻshiladi, lugʻat "
      f"shakliga emas.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-33 — taqiq va majburiyat
# ══════════════════════════════════════════════════════════════════════
NAI_IKU, NAI_TABERU, NAI_SURU, NAI_KURU = (
    r("行","い")+"かない", r("食","た")+"べない", "しない", r("来","こ")+"ない")
NAI_KAU, NAI_TSUKAU, NAI_YOMU = (
    r("買","か")+"わない", r("使","つか")+"わない", r("読","よ")+"まない")

def nakereba(nai):  return nai[:-1] + "ければなりません"
def nakutemo(nai):  return nai[:-1] + "くてもいいです"

Q_PJ33 = [
    q("<p>〜てはいけません nima maʼnoni beradi?</p>",
      ["Qilish mumkin emas", "Qilish shart", "Qilsa boʻladi", "Qilyapti"],
      "Qilish mumkin emas",
      f"<p>Qatʼiy taqiq: qoida, belgi, ustozning gapi. "
      f"<strong>{teikenai(HASHITTE)}</strong> — «yugurish mumkin emas».</p>"),

    q(f"<p>«{teikenai(HANASHITE)}» dagi は qanday oʻqiladi?</p>",
      ["[wa]", "[ha]", "[a]", "[ba]"], "[wa]",
      f"<p><strong>[wa]</strong> — bu oʻsha tanish mavzu qoʻshimchasi. "
      f"Gapning soʻzma-soʻz maʼnosi «gapirish <em>degani</em> — yaramaydi». "
      f"PJ-14 dagi qoida bu yerda ham ishlaydi.</p>"),

    q(f"<p>«Kutubxonada gaplashish mumkin emas» ni tanlang.</p>",
      [f"{TSK}で{teikenai(HANASHITE)}", f"{TSK}で{kudasai(HANASHITE)}",
       f"{TSK}で{temoii(HANASHITE)}", f"{TSK}で{HANASHIMASU}"],
      f"{TSK}で{teikenai(HANASHITE)}",
      f"<p><strong>{teikenai(HANASHITE)}</strong> — て-shakli + はいけません. "
      f"Qolgan uchtasi mos ravishda iltimos, ruxsat va oddiy gap.</p>"),

    q(f"<p>{TSUKAU} ning ない-shaklini tanlang.</p>",
      [NAI_TSUKAU, f"{r('使','つか')}あない", f"{r('使','つか')}いない",
       f"{r('使','つか')}うない"],
      NAI_TSUKAU,
      f"<p><strong>{NAI_TSUKAU}</strong> — う bilan tugagan feʼl あ emas, "
      f"<strong>わ</strong> oladi. Bu doim uchraydigan istisno.</p>"),

    q(f"<p>{TABERU} ning ない-shaklini tanlang.</p>",
      [NAI_TABERU, f"{r('食','た')}べらない", f"{r('食','た')}べあない",
       f"{r('食','た')}べるない"],
      NAI_TABERU,
      f"<p><strong>{NAI_TABERU}</strong> — II guruh: る tushadi, ない "
      f"qoʻshiladi. て-shakli bilan bir xil mantiq.</p>"),

    q(f"<p>{KURU} ning ない-shakli — <strong>来ない</strong> — qanday "
      f"oʻqiladi?</p>",
      ["こない", "くない", "きない", "けない"], "こない",
      f"<p><strong>こない</strong>. Bu kanji endi toʻrt xil oʻqiladi: "
      f"{KURU} «くる», {KIMASU} «きます», {KITE} «きて» va "
      f"{NAI_KURU} «こない».</p>"),

    q(f"<p>{YOMU} ning ない-shaklini tanlang.</p>",
      [NAI_YOMU, f"{r('読','よ')}みない", f"{r('読','よ')}むない",
       f"{r('読','よ')}んない"],
      NAI_YOMU,
      f"<p><strong>{NAI_YOMU}</strong> — I guruhda oxirgi tovush "
      f"<strong>あ</strong> qatoriga tushadi: む → ま.</p>"),

    q("<p>〜なければなりません nima maʼnoni beradi?</p>",
      ["Qilish shart", "Qilish mumkin emas", "Qilsa boʻladi", "Qilish shart emas"],
      "Qilish shart",
      f"<p>Majburiyat. Soʻzma-soʻz maʼnosi <strong>«…masa boʻlmaydi»</strong> "
      f"— ikki inkor, xuddi oʻzbekchadagi «bormasam boʻlmaydi» kabi.</p>"),

    q(f"<p>{NAI_IKU} dan «borish shart» ni tanlang.</p>",
      [nakereba(NAI_IKU), f"{r('行','い')}かないければなりません",
       f"{r('行','い')}くなければなりません", f"{r('行','い')}きなければなりません"],
      nakereba(NAI_IKU),
      f"<p><strong>{nakereba(NAI_IKU)}</strong> — ない-shaklining oxirgi "
      f"<strong>い</strong> tashlanadi va ければなりません qoʻyiladi.</p>"),

    q(f"<p>«Dushdan foydalanish shart» ni tanlang.</p>",
      [f"シャワーを{nakereba(NAI_TSUKAU)}",
       f"シャワーを{r('使','つか')}うなければなりません",
       f"シャワーを{teikenai(TSUKATTE)}",
       f"シャワーを{temoii(TSUKATTE)}"],
      f"シャワーを{nakereba(NAI_TSUKAU)}",
      f"<p>{TSUKAU} → <strong>{NAI_TSUKAU}</strong> → "
      f"<strong>{nakereba(NAI_TSUKAU)}</strong>. Lugʻat shaklidan emas, "
      f"<strong>ない-shaklidan</strong>.</p>"),

    q("<p>〜なくてもいいです nima maʼnoni beradi?</p>",
      ["Qilish shart emas", "Qilish shart", "Qilish mumkin emas", "Qilyapti"],
      "Qilish shart emas",
      f"<p>Ruxsat oʻqining toʻrtinchi burchagi. "
      f"<strong>{nakutemo(NAI_IKU)}</strong> — «borish shart emas».</p>"),

    q(f"<p>ない ning oxirgi い nega く ga aylanadi ({nakutemo(NAI_TSUKAU)})?</p>",
      ["Chunki ない — い-sifat, va い-sifatlar shunday tuslanadi",
       "Chunki bu tartibsiz shakl, yodlanadi",
       "Chunki ない — feʼl",
       "Chunki keyin もいい keladi"],
      "Chunki ない — い-sifat, va い-sifatlar shunday tuslanadi",
      f"<p>PJ-25 da {r('安','やす')}い → {r('安','やす')}く boʻlganini "
      f"koʻrgansiz. ない ham い-sifat, shuning uchun u ham xuddi shunday "
      f"tutadi — yangi qoida emas, eskisining yangi joyda ishlashi.</p>"),

    q(f"<p>{teikenai(TSUKATTE)} va {nakereba(NAI_TSUKAU)} — farqi nima?</p>",
      ["Birinchisi taqiq, ikkinchisi majburiyat",
       "Birinchisi majburiyat, ikkinchisi taqiq",
       "Ikkalasi ham taqiq",
       "Ikkalasi ham ruxsat"],
      "Birinchisi taqiq, ikkinchisi majburiyat",
      f"<p>Qarama-qarshi tomonlar: «ishlatish mumkin emas» va «ishlatish "
      f"shart». Birinchisi <strong>て-shaklidan</strong>, ikkinchisi "
      f"<strong>ない-shaklidan</strong> yasaladi.</p>"),

    q("<p>Qaysi qolip ない-shaklidan yasaladi?</p>",
      ["〜なければなりません", "〜てはいけません", "〜てもいいです", "〜ています"],
      "〜なければなりません",
      f"<p>Faqat shu bittasi. Qolgan uchtasi — {teikenai(TSUKATTE)}, "
      f"{temoii(TSUKATTE)}, {teiru(TSUKATTE)} — hammasi "
      f"<strong>て-shaklidan</strong>.</p>"),

    q(f"<p>{KAU} ning ない-shakli qaysi?</p>",
      [NAI_KAU, f"{r('買','か')}あない", f"{r('買','か')}いない",
       f"{r('買','か')}らない"],
      NAI_KAU,
      f"<p><strong>{NAI_KAU}</strong> — yana oʻsha う → <strong>わ</strong> "
      f"qoidasi. «かあない» eng koʻp uchraydigan xato.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{KY}で{teikenai(HASHITTE)}", f"{KY}で{r('走','はし')}るてはいけません",
       f"{KY}で{HASHIRIMASU}てはいけません", f"{KY}で{r('走','はし')}りてはいけません"],
      f"{KY}で{teikenai(HASHITTE)}",
      f"<p>{HASHIRU} I guruh, る → <strong>って</strong>, keyin はいけません. "
      f"Qolgan uchtasida て-shakli notoʻgʻri yasalgan.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{TSK}で{teikenai(TABETE)}",
       f"{r('明日','あした')}{nakereba(NAI_KURU)}",
       f"{SHASHIN}を{r('撮','と')}るなければなりません",
       f"{HON}を{temoii(YONDE)}"],
      f"{SHASHIN}を{r('撮','と')}るなければなりません",
      f"<p>なければなりません <strong>lugʻat shaklidan emas</strong>, "
      f"ない-shaklidan yasaladi: {r('撮','と')}る → {r('撮','と')}らない → "
      f"<strong>{r('撮','と')}らなければなりません</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{IKU} → {NAI_IKU}", f"{TABERU} → {NAI_TABERU}",
       f"{TSUKAU} → {r('使','つか')}あない", f"{SURU} → {NAI_SURU}"],
      f"{TSUKAU} → {r('使','つか')}あない",
      f"<p>う bilan tugagan feʼl <strong>わ</strong> oladi: "
      f"<strong>{NAI_TSUKAU}</strong>. Jadval boʻyicha «あ» chiqishi kerak "
      f"edi, lekin chiqmaydi.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {teikenai(HASHITTE)} · "
      f"で · プール</p>",
      [f"プールで{teikenai(HASHITTE)}", f"でプール{teikenai(HASHITTE)}",
       f"{teikenai(HASHITTE)}プールで", f"プール{teikenai(HASHITTE)}で"],
      f"プールで{teikenai(HASHITTE)}",
      f"<p>Ish bajarilayotgan joy で oladi va feʼldan oldin turadi — "
      f"PJ-22 dagi qoida. Taqiq esa gap oxirida qoladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム:</strong> "
      f"{SHASHIN}を{temoii(r('撮','と')+'って')}か。</p>"
      f"<p><strong>イムロン:</strong> いいえ、___。</p>",
      [f"{r('撮','と')}ってはいけません", f"{r('撮','と')}ってください",
       f"{r('撮','と')}らなければなりません", f"{r('撮','と')}っています"],
      f"{r('撮','と')}ってはいけません",
      f"<p>«いいえ» dan keyin <strong>taqiq</strong> kelishi kerak. "
      f"«{r('撮','と')}ってください» — buyruq, «{r('撮','と')}らなければ"
      f"なりません» — majburiyat: ikkalasi ham «yoʻq» ga toʻgʻri kelmaydi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-31 Mashq: 〜ています — davom etayotgan ish va holat",
        "tutorial":    "PJ-31:",
        "description": "て-shakli + います. Ikki maʼno — «hozir qilyapti» va "
                       "«shunday holatda» — hamda 知りません istisnosi.",
        "questions":   Q_PJ31,
        **DEFAULTS,
    },
    {
        "title":       "PJ-32 Mashq: 〜てください va 〜てもいいです",
        "tutorial":    "PJ-32:",
        "description": "Iltimos va ruxsat. Ikkalasi ham て-shaklidan, lekin "
                       "yoʻnalishlari qarama-qarshi.",
        "questions":   Q_PJ32,
        **DEFAULTS,
    },
    {
        "title":       "PJ-33 Mashq: Taqiq va majburiyat",
        "tutorial":    "PJ-33:",
        "description": "〜てはいけません · 〜なければなりません · 〜なくてもいいです — "
                       "va ular uchun kerak boʻlgan ない-oʻzagi.",
        "questions":   Q_PJ33,
        **DEFAULTS,
    },
]
