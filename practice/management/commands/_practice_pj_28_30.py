# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-28 … PJ-30.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

⚠️ Har bir feʼl shakli TOʻLIQ konstanta sifatida yozilgan (YOMU / YOMIMASU /
YONDE), oʻzak + qoʻshimcha sifatida emas. PJ-25…27 da aynan shu birikma
xato kalitlar bergan edi: "{YAS}くないです" → 安いくないです.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_28_30.py --master=prime \\
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

# ── I guruh: lugʻat · ます · て ────────────────────────────────────────
YOMU,  YOMIMASU,  YONDE  = r("読","よ")+"む",   r("読","よ")+"みます",   r("読","よ")+"んで"
KAKU,  KAKIMASU,  KAITE  = r("書","か")+"く",   r("書","か")+"きます",   r("書","か")+"いて"
HANASU,HANASHIMASU,HANASHITE = r("話","はな")+"す", r("話","はな")+"します", r("話","はな")+"して"
MATSU, MACHIMASU, MATTE  = r("待","ま")+"つ",   r("待","ま")+"ちます",   r("待","ま")+"って"
KAU,   KAIMASU,   KATTE  = r("買","か")+"う",   r("買","か")+"います",   r("買","か")+"って"
NOMU,  NOMIMASU,  NONDE  = r("飲","の")+"む",   r("飲","の")+"みます",   r("飲","の")+"んで"
KIKU,  KIKIMASU,  KIITE  = r("聞","き")+"く",   r("聞","き")+"きます",   r("聞","き")+"いて"
OYOGU, OYOGIMASU, OYOIDE = r("泳","およ")+"ぐ", r("泳","およ")+"ぎます", r("泳","およ")+"いで"
ASOBU, ASOBIMASU, ASONDE = r("遊","あそ")+"ぶ", r("遊","あそ")+"びます", r("遊","あそ")+"んで"
SHINU, SHINIMASU, SHINDE = r("死","し")+"ぬ",   r("死","し")+"にます",   r("死","し")+"んで"
TSUKURU,TSUKURIMASU,TSUKUTTE = r("作","つく")+"る", r("作","つく")+"ります", r("作","つく")+"って"
NORU,  NORIMASU,  NOTTE  = r("乗","の")+"る",   r("乗","の")+"ります",   r("乗","の")+"って"
KAERU, KAERIMASU, KAETTE = r("帰","かえ")+"る", r("帰","かえ")+"ります", r("帰","かえ")+"って"
HAIRU, HAIRIMASU, HAITTE = r("入","はい")+"る", r("入","はい")+"ります", r("入","はい")+"って"
IKU,   IKIMASU,   ITTE   = r("行","い")+"く",   r("行","い")+"きます",   r("行","い")+"って"
KAESU, KAESHIMASU, KAESHITE = r("返","かえ")+"す", r("返","かえ")+"します", r("返","かえ")+"して"

# ── II guruh ──────────────────────────────────────────────────────────
TABERU, TABEMASU, TABETE = r("食","た")+"べる", r("食","た")+"べます", r("食","た")+"べて"
MIRU,   MIMASU,   MITE   = r("見","み")+"る",   r("見","み")+"ます",   r("見","み")+"て"
OKIRU,  OKIMASU,  OKITE  = r("起","お")+"きる", r("起","お")+"きます", r("起","お")+"きて"
NERU,   NEMASU,   NETE   = r("寝","ね")+"る",   r("寝","ね")+"ます",   r("寝","ね")+"て"
OSHIERU,OSHIEMASU,OSHIETE = r("教","おし")+"える", r("教","おし")+"えます", r("教","おし")+"えて"

# ── III guruh ─────────────────────────────────────────────────────────
KURU, KIMASU, KITE = r("来","く")+"る", r("来","き")+"ます", r("来","き")+"て"
BENKYOU = r("勉強","べんきょう")

# ── otlar ─────────────────────────────────────────────────────────────
HON, GK, KY, SE = r("本","ほん"), r("学校","がっこう"), r("教室","きょうしつ"), r("先生","せんせい")
NG, WA, IE      = r("日本語","にほんご"), r("私","わたし"), r("家","いえ")
JISHO, JISHOKEI = r("辞書","じしょ"), r("辞書形","じしょけい")
GODAN, ICHIDAN, FUKISOKU = r("五段","ごだん"), r("一段","いちだん"), r("不規則","ふきそく")
UMI, TEGAMI, ASAGOHAN = r("海","うみ"), r("手紙","てがみ"), r("朝","あさ")+"ごはん"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-28 — lugʻat shakli
# ══════════════════════════════════════════════════════════════════════
Q_PJ28 = [
    q(f"<p>Yapon lugʻati feʼlni qaysi shaklda beradi?</p>",
      ["ます shaklida", f"{JISHOKEI} — lugʻat shaklida",
       "て shaklida", "Oʻtgan zamon shaklida"],
      f"{JISHOKEI} — lugʻat shaklida",
      f"<p>Lugʻat feʼlning bezaksiz shaklini beradi. Shuning uchun "
      f"<strong>{NOMIMASU}</strong> ni qidirsangiz topmaysiz — "
      f"<strong>{NOMU}</strong> ni qidiring.</p>"),

    q("<p>Nega lugʻatda ます yoʻq?</p>",
      ["Chunki ます — muloyimlik qoʻshimchasi, feʼlning qismi emas",
       "Chunki ます juda uzun",
       "Chunki ます faqat soʻzlashuvda ishlatiladi",
       "Chunki ます eski shakl"],
      "Chunki ます — muloyimlik qoʻshimchasi, feʼlning qismi emas",
      f"<p>ます — alohida qoʻshimcha ({r('助動詞','じょどうし')}). Oʻzbekchada "
      f"ham lugʻatda «oʻqiyman» emas, «oʻqi<strong>moq</strong>» turadi: "
      f"lugʻat feʼlning oʻzini beradi, kiyimini emas.</p>"),

    q("<p>Lugʻat shakli qaysi qatordagi tovush bilan tugaydi?</p>",
      ["あ qatori", "い qatori", "う qatori", "え qatori"], "う qatori",
      f"<p><strong>う qatori</strong> — toʻqqizta variant: う, く, ぐ, す, つ, "
      f"ぬ, ぶ, む, る. Boshqa oxir yoʻq.</p>"),

    q(f"<p>Butun yapon tilida ぬ bilan tugaydigan nechta feʼl bor?</p>",
      ["Bittagina", "Beshta", "Yigirmata", "Yuzdan ortiq"], "Bittagina",
      f"<p>Faqat <strong>{SHINU}</strong> («oʻlmoq»). Uni yodlash oson — "
      f"raqobatchisi yoʻq.</p>"),

    q(f"<p>{TABEMASU} ning lugʻat shakli qaysi?</p>",
      [TABERU, f"{r('食','た')}べく", f"{r('食','た')}べう", f"{r('食','た')}べつ"],
      TABERU,
      f"<p><strong>{TABERU}</strong> — II guruh: ます oʻrniga <strong>る</strong> "
      f"qoʻyiladi, oʻzak esa oʻzgarmaydi.</p>"),

    q(f"<p>{YOMIMASU} ning lugʻat shakli qaysi?</p>",
      [YOMU, f"{r('読','よ')}みる", f"{r('読','よ')}みむ", f"{r('読','よ')}みう"],
      YOMU,
      f"<p><strong>{YOMU}</strong> — I guruh: み koʻtarilib <strong>む</strong> "
      f"boʻladi, い qatoridan う qatoriga.</p>"),

    q(f"<p>{HANASHIMASU} ning lugʻat shakli qaysi?</p>",
      [HANASU, f"{r('話','はな')}しる", f"{r('話','はな')}しう", f"{r('話','はな')}しつ"],
      HANASU,
      f"<p><strong>{HANASU}</strong>. し — さ qatorining い pogʻonasi, uning "
      f"う pogʻonasi <strong>す</strong>. «しる» emas.</p>"),

    q(f"<p>{MACHIMASU} ning lugʻat shakli qaysi?</p>",
      [MATSU, f"{r('待','ま')}ちる", f"{r('待','ま')}ちう", f"{r('待','ま')}ちく"],
      MATSU,
      f"<p><strong>{MATSU}</strong>. ち — た qatorining い pogʻonasi, uning "
      f"う pogʻonasi <strong>つ</strong>, «ちう» emas.</p>"),

    q(f"<p>{KAIMASU} («sotib olaman») ning lugʻat shakli qaysi?</p>",
      [KAU, f"{r('買','か')}いる", f"{r('買','か')}いく", f"{r('買','か')}いつ"],
      KAU,
      f"<p><strong>{KAU}</strong> — い koʻtarilib <strong>う</strong> boʻladi. "
      f"Bu bitta tovushli oxir, lekin qoida oʻsha-oʻsha.</p>"),

    q(f"<p>{KIMASU} ning lugʻat shakli — <strong>来る</strong> — qanday "
      f"oʻqiladi?</p>",
      ["くる", "きる", "こる", "きく"], "くる",
      f"<p><strong>くる</strong>. Kanji oʻsha turadi, lekin oʻqilishi "
      f"oʻzgaradi: lugʻat shaklida <strong>く</strong>, ます shaklida "
      f"<strong>き</strong>. Buni faqat furigana koʻrsatadi.</p>"),

    q(f"<p>{OKIMASU} ning lugʻat shakli qaysi?</p>",
      [OKIRU, r("起","お")+"く", r("起","お")+"きう", r("起","お")+"きつ"],
      OKIRU,
      f"<p><strong>{OKIRU}</strong> — II guruh feʼli, shuning uchun "
      f"<strong>る</strong> qoʻshiladi. «{r('起','お')}く» — I guruhning "
      f"qoidasi, bu feʼlga toʻgʻri kelmaydi.</p>"),

    q(f"<p>{KIKIMASU} ning lugʻat shakli qaysi?</p>",
      [KIKU, r("聞","き")+"きる", r("聞","き")+"る", r("聞","き")+"きう"],
      KIKU,
      f"<p><strong>{KIKU}</strong> — bu <strong>I guruh</strong> feʼli, "
      f"garchi oʻzagi {OKIMASU} kabi «き» bilan tugasa ham. Mana shu juftlik "
      f"butun darsning ogohlantirishi.</p>"),

    q(f"<p>{OKIMASU} va {KIKIMASU} — oʻzaklari bir xil «き» bilan tugaydi. "
      f"Bundan nima kelib chiqadi?</p>",
      ["ます shakliga qarab guruhni doim aniqlab boʻlmaydi",
       "Ikkalasi ham II guruhda",
       "Ikkalasi ham I guruhda",
       "Ikkalasining maʼnosi yaqin"],
      "ます shakliga qarab guruhni doim aniqlab boʻlmaydi",
      f"<p>{OKIRU} — II guruh, {KIKU} — I guruh, lekin ます shakli buni "
      f"koʻrsatmaydi. Xulosa amaliy: yangi feʼlni <strong>lugʻat "
      f"shaklida</strong> yodlang.</p>"),

    q("<p>Oʻzagi <strong>え</strong> qatori bilan tugagan feʼl qaysi guruhda?</p>",
      ["Albatta II guruhda", "Albatta I guruhda",
       "Albatta III guruhda", "Aniqlab boʻlmaydi"],
      "Albatta II guruhda",
      f"<p>Bu yagona 100% ishonchli belgi: I guruh oʻzagi hech qachon え "
      f"qatori bilan tugamaydi. {OSHIEMASU} → <strong>{OSHIERU}</strong>, "
      f"{TABEMASU} → <strong>{TABERU}</strong>.</p>"),

    q(f"<p>{KAERIMASU} ning lugʻat shakli qaysi?</p>",
      [KAERU, r("帰","かえ")+"りる", r("帰","かえ")+"りむ", r("帰","かえ")+"りう"],
      KAERU,
      f"<p><strong>{KAERU}</strong> — り koʻtarilib <strong>る</strong> "
      f"boʻladi. Bu oʻsha tuzoq feʼl: koʻrinishi II guruhga oʻxshaydi, "
      f"lekin u I guruhda.</p>"),

    q(f"<p>Qaysi juftlik toʻgʻri?</p>",
      [f"{NEMASU} → {NERU}", f"{NEMASU} → {r('寝','ね')}く",
       f"{NEMASU} → {r('寝','ね')}む", f"{NEMASU} → {r('寝','ね')}う"],
      f"{NEMASU} → {NERU}",
      f"<p>Oʻzak <strong>ね</strong> — え qatori, demak feʼl II guruhda va "
      f"lugʻat shakli <strong>{NERU}</strong>.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{JISHO}に「{r('飲','の')}む」があります",
       f"{JISHO}に「のみます」があります",
       f"{JISHO}に「のみる」があります",
       f"{JISHO}に「のむます」があります"],
      f"{JISHO}に「{r('飲','の')}む」があります",
      f"<p>Lugʻatda faqat lugʻat shakli turadi: <strong>{NOMU}</strong>. "
      f"«のみます» — bu matndagi shakl, lugʻatdagi emas.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{KAKIMASU} → {KAKU}", f"{HANASHIMASU} → {HANASU}",
       f"{KIKIMASU} → {r('聞','き')}きる", f"{MIMASU} → {MIRU}"],
      f"{KIKIMASU} → {r('聞','き')}きる",
      f"<p>{KIKU} — I guruh feʼli, shuning uchun き koʻtarilib "
      f"<strong>く</strong> boʻladi: <strong>{KIKU}</strong>. «きる» — "
      f"II guruhning qoidasi.</p>"),

    q(f"<p>Yangi feʼlni qanday yodlash toʻgʻri?</p>",
      ["Faqat ます shaklida", "Faqat maʼnosi bilan",
       "Lugʻat shakli va ます shakli bilan birga", "Faqat kanjisi bilan"],
      "Lugʻat shakli va ます shakli bilan birga",
      f"<p>Ikkita shakl birga tursa, guruh ham oʻz-oʻzidan koʻrinadi: "
      f"<strong>{KIKU} / {KIKIMASU}</strong> — I guruh, "
      f"<strong>{OKIRU} / {OKIMASU}</strong> — II guruh.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"「{MACHIMASU}」の{JISHOKEI}は{r('何','なん')}ですか。</p>"
      f"<p><strong>やまだ:</strong> ___ です。</p>",
      [MATSU, r("待","ま")+"ちる", r("待","ま")+"ちう", r("待","ま")+"つる"],
      MATSU,
      f"<p><strong>{MATSU}</strong>. ち た qatorining い pogʻonasi; uning "
      f"う pogʻonasi <strong>つ</strong>.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-29 — て-shakli 1 (II va III guruh)
# ══════════════════════════════════════════════════════════════════════
Q_PJ29 = [
    q("<p>て-shakli oʻzi qanday maʼno beradi?</p>",
      ["Hech qanday — u ulagich, zamon ham koʻrsatmaydi",
       "Hozirgi zamon", "Oʻtgan zamon", "Buyruq"],
      "Hech qanday — u ulagich, zamon ham koʻrsatmaydi",
      f"<p>て-shakli ({r('て形','てけい')}) gapni tugatmaydi va zamon "
      f"koʻrsatmaydi. U oʻzidan keyin nima kelishini kutib turadi.</p>"),

    q(f"<p>{TABERU} ning て-shakli qaysi?</p>",
      [TABETE, f"{r('食','た')}べるて", f"{r('食','た')}べって", f"{r('食','た')}べんで"],
      TABETE,
      f"<p><strong>{TABETE}</strong> — II guruh: <strong>る almashadi</strong>, "
      f"て unga qoʻshilmaydi.</p>"),

    q(f"<p>{MIRU} ning て-shakli qaysi?</p>",
      [MITE, f"{r('見','み')}るて", f"{r('見','み')}って", f"{r('見','み')}んで"],
      MITE,
      f"<p><strong>{MITE}</strong>. Oʻzak bitta tovushdan iborat "
      f"({r('見','み')}), lekin qoida oʻsha: る → て.</p>"),

    q(f"<p>{OKIRU} ning て-shakli qaysi?</p>",
      [OKITE, f"{r('起','お')}きって", f"{r('起','お')}きるて", f"{r('起','お')}きいて"],
      OKITE,
      f"<p><strong>{OKITE}</strong>. ます shakli bilan bir xil oʻzakdan: "
      f"{r('起','お')}き + ます, {r('起','お')}き + て.</p>"),

    q("<p>する va " + KURU + " ning て-shakllari qaysi?</p>",
      [f"して · {KITE}", f"しって · {r('来','き')}って",
       f"すて · {r('来','く')}て", f"しんで · {r('来','き')}んで"],
      f"して · {KITE}",
      f"<p><strong>して</strong> va <strong>{KITE}</strong> — III guruhda "
      f"bor-yoʻgʻi shu ikkitasi, ular yodlanadi.</p>"),

    q(f"<p>{NERU} ning て-shakli qaysi?</p>",
      [NETE, f"{r('寝','ね')}るて", f"{r('寝','ね')}って", f"{r('寝','ね')}んで"],
      NETE,
      f"<p><strong>{NETE}</strong> — る oʻrniga て. II guruhda boshqa "
      f"variant yoʻq.</p>"),

    q(f"<p>{BENKYOU}する ning て-shakli qaysi?</p>",
      [f"{BENKYOU}して", f"{BENKYOU}すて", f"{BENKYOU}しって", f"{BENKYOU}するて"],
      f"{BENKYOU}して",
      f"<p><strong>{BENKYOU}して</strong> — する ning har bir qoʻshma feʼli "
      f"して boʻladi: {r('電話','でんわ')}して ham shunday.</p>"),

    q(f"<p>{OSHIERU} ning て-shakli qaysi?</p>",
      [OSHIETE, f"{r('教','おし')}えるて", f"{r('教','おし')}えって", f"{r('教','おし')}えんで"],
      OSHIETE,
      f"<p><strong>{OSHIETE}</strong>. Oʻzak <strong>え</strong> qatori bilan "
      f"tugagani uchun feʼl albatta II guruhda — demak る → て.</p>"),

    q(f"<p>«Turib, nonushta qilaman» ni tanlang.</p>",
      [f"{OKITE}、{ASAGOHAN}を{TABEMASU}",
       f"{OKIMASU}、{ASAGOHAN}を{TABETE}",
       f"{OKITE}、{ASAGOHAN}を{TABETE}",
       f"{OKIMASU}て、{ASAGOHAN}を{TABEMASU}"],
      f"{OKITE}、{ASAGOHAN}を{TABEMASU}",
      f"<p>Birinchi feʼl <strong>て</strong> da qoladi, oxirgisi gapni "
      f"<strong>ます</strong> bilan tugatadi. Ikkalasi ham て boʻlsa, gap "
      f"tugamaydi.</p>"),

    q(f"<p>Bu qolip oʻzbekchadagi qaysi qoʻshimchaga toʻgʻri keladi?</p>",
      ["«-(i)b»: turib, koʻrib, yeb", "«-gan»: turgan, koʻrgan",
       "«-moq»: turmoq, koʻrmoq", "«-di»: turdi, koʻrdi"],
      "«-(i)b»: turib, koʻrib, yeb",
      f"<p>Oʻzbekchada ham birinchi feʼl tugallanmagan holda qoladi va "
      f"zamonni <strong>oxirgi</strong> feʼl tashiydi — «tur<strong>ib</strong>, "
      f"nonushta qildim». Yapon tili aynan shunday ishlaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong>{r('映画','えいが')}を___、{NEMASU}。</strong></p>",
      [MITE, MIMASU, MIRU, f"{r('見','み')}るて"], MITE,
      f"<p><strong>{MITE}</strong> — birinchi ish て-shaklida ulanadi, "
      f"gapni esa {NEMASU} tugatadi.</p>"),

    q(f"<p>Necha marta ます ishlatiladi: «{OKITE}、{TABETE}、{GK}へ"
      f"{r('行','い')}きます»?</p>",
      ["Bir marta — faqat oxirgi feʼlda", "Ikki marta", "Uch marta",
       "Umuman ishlatilmaydi"],
      "Bir marta — faqat oxirgi feʼlda",
      f"<p>Uchta ish, bitta gap, bitta ます. Qolgan feʼllar "
      f"<strong>て</strong> da qoladi.</p>"),

    q(f"<p>«Kecha kino koʻrib, uxladim» — {MIRU} qanday shaklda turadi?</p>",
      [MITE, f"{r('見','み')}ました", f"{r('見','み')}るて", f"{r('見','み')}って"],
      MITE,
      f"<p><strong>{MITE}</strong> — oʻzgarmaydi. て-shakli zamon "
      f"koʻrsatmaydi; oʻtgan zamonni gapning oxirgi feʼli "
      f"({r('寝','ね')}ました) tashiydi.</p>"),

    q(f"<p>Otlarni ulash uchun nima ishlatiladi?</p>",
      ["て", "と", "で", "に"], "と",
      f"<p><strong>と</strong> — «{HON}と{r('鉛筆','えんぴつ')}» (kitob va "
      f"qalam). て esa <strong>feʼllarni</strong> ulaydi. Yaponchada «va» "
      f"degan yagona soʻz yoʻq.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{TABETE}、{NEMASU}", f"{TABEMASU}と{NEMASU}",
       f"{TABERU}と{NEMASU}", f"{TABEMASU}て{NEMASU}"],
      f"{TABETE}、{NEMASU}",
      f"<p><strong>{TABETE}、{NEMASU}</strong> — «yeb, uxlayman». と ikki "
      f"<strong>otni</strong> ulaydi, feʼllarni emas; て esa ます dan emas, "
      f"lugʻat shaklidan yasaladi.</p>"),

    q(f"<p>«{TABETE}、{NEMASU}» va «{NETE}、{TABEMASU}» — farqi bormi?</p>",
      ["Ha: て bilan ulangan ishlar vaqt tartibida yoziladi",
       "Yoʻq, maʼnosi bir xil",
       "Ha, lekin faqat muloyimlikda",
       "Ha, ikkinchisi notoʻgʻri"],
      "Ha: て bilan ulangan ishlar vaqt tartibida yoziladi",
      f"<p>Birinchisi «yeb, uxlayman», ikkinchisi «uxlab, yeyman». Tartib "
      f"maʼnoni oʻzgartiradi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{OKITE}、{GK}へ{IKIMASU}",
       f"{r('昨日','きのう')}{r('映画','えいが')}を{r('見','み')}まして、{r('寝','ね')}ました",
       f"{BENKYOU}して、{r('帰','かえ')}ります",
       f"{KITE}、{NG}を{OSHIEMASU}"],
      f"{r('昨日','きのう')}{r('映画','えいが')}を{r('見','み')}まして、{r('寝','ね')}ました",
      f"<p>て-shakli <strong>ます dan emas, lugʻat shaklidan</strong> "
      f"yasaladi. Toʻgʻrisi — <strong>{MITE}、{r('寝','ね')}ました</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TABERU} → {TABETE}", f"{OKIRU} → {OKITE}",
       "する → すて", f"{OSHIERU} → {OSHIETE}"],
      "する → すて",
      f"<p>する — III guruh feʼli va uning て-shakli yodlanadi: "
      f"<strong>して</strong>. «すて» degan shakl yoʻq. Qolgan uchtasi "
      f"II guruhning る → て qoidasi boʻyicha toʻgʻri yasalgan.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {NEMASU} · "
      f"{r('映画','えいが')} · を · {MITE}</p>",
      [f"{r('映画','えいが')}を{MITE}、{NEMASU}",
       f"{MITE}、{r('映画','えいが')}を{NEMASU}",
       f"{r('映画','えいが')}を{NEMASU}、{MITE}",
       f"を{r('映画','えいが')}{MITE}、{NEMASU}"],
      f"{r('映画','えいが')}を{MITE}、{NEMASU}",
      f"<p>Toʻldiruvchi oʻz feʼlidan oldin turadi, て bilan ulangan ish esa "
      f"birinchi boʻladi. Gapni {NEMASU} tugatadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム:</strong> "
      f"{r('毎朝','まいあさ')}{r('何','なに')}をしますか。</p>"
      f"<p><strong>ムニラ:</strong> ___、{GK}へ{IKIMASU}。</p>",
      [f"{OKITE}、{ASAGOHAN}を{TABETE}",
       f"{OKIMASU}、{ASAGOHAN}を{TABEMASU}",
       f"{OKIRU}、{ASAGOHAN}を{TABERU}",
       f"{OKITE}、{ASAGOHAN}を{TABEMASU}"],
      f"{OKITE}、{ASAGOHAN}を{TABETE}",
      f"<p>Gap allaqachon {IKIMASU} bilan tugagan, shuning uchun undan "
      f"oldingi <strong>ikkala</strong> feʼl ham て-shaklida qolishi kerak: "
      f"<strong>{OKITE}、{ASAGOHAN}を{TABETE}</strong>.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-30 — て-shakli 2 (I guruh, beshta qoida)
# ══════════════════════════════════════════════════════════════════════
Q_PJ30 = [
    q("<p>う・つ・る bilan tugagan I guruh feʼli qanday て oladi?</p>",
      ["って", "んで", "いて", "して"], "って",
      f"<p><strong>って</strong> — uchta har xil oxir bitta natijaga keladi: "
      f"{KAU} → {KATTE}, {MATSU} → {MATTE}, {KAERU} → {KAETTE}.</p>"),

    q("<p>む・ぶ・ぬ bilan tugagan feʼl qanday て oladi?</p>",
      ["って", "んで", "いて", "して"], "んで",
      f"<p><strong>んで</strong> — bu uchta tovush jarangli, shuning uchun "
      f"ulanish ham jarangli chiqadi: て emas, <strong>で</strong>.</p>"),

    q(f"<p>{YOMU} ning て-shakli qaysi?</p>",
      [YONDE, f"{r('読','よ')}んて", f"{r('読','よ')}って", f"{r('読','よ')}みて"],
      YONDE,
      f"<p><strong>{YONDE}</strong> — む → んで. «{r('読','よ')}んて» "
      f"notoʻgʻri: む dan keyin ulanish jarangli boʻladi.</p>"),

    q(f"<p>{KAU} ning て-shakli qaysi?</p>",
      [KATTE, f"{r('買','か')}いて", f"{r('買','か')}んで", f"{r('買','か')}うて"],
      KATTE,
      f"<p><strong>{KATTE}</strong> — う・つ・る → って.</p>"),

    q(f"<p>{KAKU} ning て-shakli qaysi?</p>",
      [KAITE, f"{r('書','か')}いで", f"{r('書','か')}って", f"{r('書','か')}んで"],
      KAITE,
      f"<p><strong>{KAITE}</strong> — く jarangsiz, shuning uchun "
      f"<strong>いて</strong>. Jarangli ぐ boʻlganda いで chiqar edi.</p>"),

    q(f"<p>{OYOGU} ning て-shakli qaysi?</p>",
      [OYOIDE, f"{r('泳','およ')}いて", f"{r('泳','およ')}って", f"{r('泳','およ')}んで"],
      OYOIDE,
      f"<p><strong>{OYOIDE}</strong> — ぐ jarangli, demak <strong>いで</strong>. "
      f"{KAKU} → {KAITE} bilan yonma-yon qoʻying: farq bitta nuqtada.</p>"),

    q(f"<p>{HANASU} ning て-shakli qaysi?</p>",
      [HANASHITE, f"{r('話','はな')}しって", f"{r('話','はな')}って", f"{r('話','はな')}すて"],
      HANASHITE,
      f"<p><strong>{HANASHITE}</strong> — す → して. Bu shakl sizga tanish: "
      f"III guruhning する ham して boʻladi, sababi ham bir xil.</p>"),

    q(f"<p>{ASOBU} ning て-shakli qaysi?</p>",
      [ASONDE, f"{r('遊','あそ')}んて", f"{r('遊','あそ')}って", f"{r('遊','あそ')}びて"],
      ASONDE,
      f"<p><strong>{ASONDE}</strong> — ぶ ham む・ぬ bilan bir uchlikda: "
      f"<strong>んで</strong>.</p>"),

    q(f"<p>{MATSU} ning て-shakli qaysi?</p>",
      [MATTE, f"{r('待','ま')}て", f"{r('待','ま')}ちて", f"{r('待','ま')}んで"],
      MATTE,
      f"<p><strong>{MATTE}</strong>. Kichik <strong>っ</strong> ni tashlab "
      f"qoʻymang — «matte» va «mate» boshqa-boshqa soʻzlar.</p>"),

    q(f"<p>{NORU} ning て-shakli qaysi?</p>",
      [NOTTE, f"{r('乗','の')}んで", f"{r('乗','の')}りて", f"{r('乗','の')}いて"],
      NOTTE,
      f"<p><strong>{NOTTE}</strong> — る ham う・つ bilan bir uchlikda: "
      f"<strong>って</strong>.</p>"),

    q(f"<p>{KAERU} ning て-shakli qaysi?</p>",
      [KAETTE, f"{r('帰','かえ')}て", f"{r('帰','かえ')}んで", f"{r('帰','かえ')}りて"],
      KAETTE,
      f"<p><strong>{KAETTE}</strong>. {KAERU} — koʻrinishi II guruhga "
      f"oʻxshagan, aslida I guruh feʼli, shuning uchun って oladi.</p>"),

    q(f"<p>{IKU} ning て-shakli qaysi?</p>",
      [ITTE, f"{r('行','い')}いて", f"{r('行','い')}きて", f"{r('行','い')}んで"],
      ITTE,
      f"<p><strong>{ITTE}</strong>. く → いて qoidasi «いいて» berishi kerak "
      f"edi — lekin bu <strong>butun kursdagi yagona istisno</strong>.</p>"),

    q(f"<p>{KAKU} va {IKU} — ikkalasi ham く bilan tugaydi. て-shakllari bir "
      f"xilmi?</p>",
      [f"Yoʻq: {KAITE}, lekin {ITTE}",
       f"Ha, ikkalasi ham いて oladi",
       f"Ha, ikkalasi ham って oladi",
       f"Yoʻq: {r('書','か')}って va {r('行','い')}いて"],
      f"Yoʻq: {KAITE}, lekin {ITTE}",
      f"<p>{KAKU} qoidaga boʻysunadi, {IKU} esa yoʻq. Boshqa hech qaysi "
      f"く feʼli bunday qilmaydi — {KIKU} → <strong>{KIITE}</strong>.</p>"),

    q(f"<p>«って» dagi kichik っ nima?</p>",
      ["Sokuon — keyingi undoshni ikkilantiradi",
       "Yōon — tovushni yumshatadi",
       "Dakuten belgisi",
       "Uzun unli belgisi"],
      "Sokuon — keyingi undoshni ikkilantiradi",
      f"<p>PJ-6 dagi <strong>sokuon</strong>. {MATTE} «matte» deb oʻqiladi: "
      f"toʻxtash bir zumga uzayadi.</p>"),

    q(f"<p>Qaysi juftlikda ikkala て-shakl ham toʻgʻri?</p>",
      [f"{NONDE} · {KAITE}", f"{r('飲','の')}んて · {KAITE}",
       f"{NONDE} · {r('書','か')}いで", f"{r('飲','の')}いて · {r('書','か')}って"],
      f"{NONDE} · {KAITE}",
      f"<p>{NOMU} む → <strong>んで</strong>, {KAKU} く → "
      f"<strong>いて</strong>. Jaranglilik har biri oʻz oxiridan keladi.</p>"),

    q(f"<p>{SHINU} ning て-shakli qaysi?</p>",
      [SHINDE, f"{r('死','し')}んて", f"{r('死','し')}って", f"{r('死','し')}にて"],
      SHINDE,
      f"<p><strong>{SHINDE}</strong> — yagona ぬ feʼli, va u む・ぶ bilan "
      f"bir uchlikda: <strong>んで</strong>.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{HON}を{YONDE}、{NEMASU}",
       f"{UMI}へ{r('行','い')}いて、{OYOGIMASU}",
       f"パンを{KATTE}、{TABEMASU}",
       f"{TEGAMI}を{KAITE}、{r('帰','かえ')}りました"],
      f"{UMI}へ{r('行','い')}いて、{OYOGIMASU}",
      f"<p>{IKU} ning て-shakli — <strong>{ITTE}</strong>, «いいて» emas. "
      f"Bu kursdagi yagona istisno.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TSUKURU} → {TSUKUTTE}", f"{KAESU} → {KAESHITE}",
       f"{ASOBU} → {r('遊','あそ')}びて", f"{HAIRU} → {HAITTE}"],
      f"{ASOBU} → {r('遊','あそ')}びて",
      f"<p>ぶ → <strong>んで</strong>, demak <strong>{ASONDE}</strong>. "
      f"«{r('遊','あそ')}びて» — ます oʻzagiga て qoʻshib yuborilgan, bu "
      f"qoida yoʻq.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {OYOIDE} · へ · "
      f"{UMI} · {ITTE} · {r('帰','かえ')}りました</p>",
      [f"{UMI}へ{ITTE}、{OYOIDE}、{r('帰','かえ')}りました",
       f"{ITTE}、{UMI}へ{OYOIDE}、{r('帰','かえ')}りました",
       f"{UMI}へ{OYOIDE}、{ITTE}、{r('帰','かえ')}りました",
       f"へ{UMI}{ITTE}、{OYOIDE}、{r('帰','かえ')}りました"],
      f"{UMI}へ{ITTE}、{OYOIDE}、{r('帰','かえ')}りました",
      f"<p>«Dengizga borib, suzib, qaytdim». Yoʻnalish qoʻshimchasi へ oʻz "
      f"otidan keyin turadi, ishlar esa vaqt tartibida boradi. Zamonni "
      f"faqat oxirgi feʼl tashiydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム:</strong> "
      f"{r('今日','きょう')}は{r('何','なに')}をしますか。</p>"
      f"<p><strong>イムロン:</strong> {UMI}で___、{r('四時','よじ')}に"
      f"{r('帰','かえ')}ります。</p>",
      [OYOIDE, OYOGIMASU, OYOGU, f"{r('泳','およ')}ぎて"], OYOIDE,
      f"<p><strong>{OYOIDE}</strong> — gapni {r('帰','かえ')}ります tugatadi, "
      f"shuning uchun birinchi ish て-shaklida ulanadi. ぐ jarangli, demak "
      f"いで.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-28 Mashq: Lugʻat shakli (辞書形)",
        "tutorial":    "PJ-28:",
        "description": "ます shaklidan lugʻat shakliga qaytish, uchala guruhda. "
                       "Ichida darsning asosiy ogohlantirishi: 起きます va 聞きます.",
        "questions":   Q_PJ28,
        **DEFAULTS,
    },
    {
        "title":       "PJ-29 Mashq: て-shakli 1 — 一段 va 不規則 feʼllar",
        "tutorial":    "PJ-29:",
        "description": "II guruhda る → て, III guruhda して va 来て. "
                       "Va 〜て、〜ます ulanishi — oʻzbekchadagi «-ib» kabi.",
        "questions":   Q_PJ29,
        **DEFAULTS,
    },
    {
        "title":       "PJ-30 Mashq: て-shakli 2 — 五段 feʼllarning beshta qoidasi",
        "tutorial":    "PJ-30:",
        "description": "って · んで · いて · いで · して — va butun kursdagi "
                       "yagona istisno: 行く → 行って.",
        "questions":   Q_PJ30,
        **DEFAULTS,
    },
]
