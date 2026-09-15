# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-70 … PJ-72. Keigo bloki yopiladi.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Asosiy tuzoq — ikki mahsuldor qolipning bir-biriga oʻxshashligi:
    お + ます-oʻzak + に なる   ← boshqani koʻtaradi (PJ-69)
    お + ます-oʻzak + する      ← oʻzini pasaytiradi (PJ-70)
Ikkalasi `verify_pj_70_72_forms.py` da bitta oʻzak jadvalidan qayta
hisoblanadi va ustma-ust tushmasligi tekshiriladi.

Ikkinchi tuzoq: beshta istisno ます shakli faqat 尊敬語 da
(いらっしゃいます), 謙譲語 da esa hammasi oddiy (参ります).

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_70_72.py --master=prime \\
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


# ── keigo atamalari ──────────────────────────────────────────────────
SONKEIGO = r("尊敬語","そんけいご")
KENJOUGO = r("謙譲語","けんじょうご")
TEINEIGO = r("丁寧語","ていねいご")
UCHI = r("内","うち")
SOTO = r("外","そと")

# ── lugʻat feʼllari ──────────────────────────────────────────────────
MATSU   = r("待","ま")+"つ"
MOTSU   = r("持","も")+"つ"
OKURU   = r("送","おく")+"る"
TSUTAERU = r("伝","つた")+"える"
YOMU    = r("読","よ")+"む"
IKU     = r("行","い")+"く"
KURU    = r("来","く")+"る"
IU      = r("言","い")+"う"
MIRU    = r("見","み")+"る"
IRU     = "いる"
SURU    = "する"
AU      = r("会","あ")+"う"
KIKU    = r("聞","き")+"く"
ANNAI   = r("案内","あんない")+"する"
SETSUMEI = r("説明","せつめい")+"する"
RENRAKU = r("連絡","れんらく")+"する"

# ── 尊敬語 (PJ-69, taqqoslash uchun) ─────────────────────────────────
IRASSHARU = "いらっしゃる"
IRASSHAIMASU = "いらっしゃいます"
MESHIAGARU = r("召","め")+"し"+r("上","あ")+"がる"
OSSHARU = "おっしゃる"
NASARU = "なさる"
GORAN = "ご"+r("覧","らん")+"になる"
OMACHI_NINARU = "お"+r("待","ま")+"ちになる"
OMACHI_NINARIMASU = "お"+r("待","ま")+"ちになります"

# ── 謙譲語 (PJ-70) ───────────────────────────────────────────────────
OMACHI_SURU = "お"+r("待","ま")+"ちします"
OMACHI_ITASU = "お"+r("待","ま")+"ちいたします"
OMOCHI_SURU = "お"+r("持","も")+"ちします"
OOKURI_SURU = "お"+r("送","おく")+"りします"
OTSUTAE_SURU = "お"+r("伝","つた")+"えします"
GOANNAI = "ご"+r("案内","あんない")+"します"
GOSETSUMEI = "ご"+r("説明","せつめい")+"します"
GORENRAKU = "ご"+r("連絡","れんらく")+"します"
MAIRU = r("参","まい")+"る"
MAIRIMASU = r("参","まい")+"ります"
ORU = "おる"
ORIMASU = "おります"
MOUSU = r("申","もう")+"す"
MOUSHIMASU = r("申","もう")+"します"
ITASU = "いたす"
ITASHIMASU = "いたします"
HAIKEN = r("拝見","はいけん")+"する"
HAIKENSHIMASU = r("拝見","はいけん")+"します"
UKAGAU = r("伺","うかが")+"う"
UKAGAIMASU = r("伺","うかが")+"います"
ITADAKU = "いただく"
OMENIKAKARU = "お"+r("目","め")+"にかかる"

# ── 丁寧語 (PJ-71) ───────────────────────────────────────────────────
GOZAIMASU = "ございます"
DEGOZAIMASU = "でございます"
IRASSHAIMASE = "いらっしゃいませ"
SHOUSHOU = r("少々","しょうしょう")+"お"+r("待","ま")+"ちください"
KASHIKOMARI = "かしこまりました"
MOUSHIWAKE = r("申","もう")+"し"+r("訳","わけ")+"ございません"
OKOSHI = "またお"+r("越","こ")+"しくださいませ"

# ── うち / そと (PJ-72) ──────────────────────────────────────────────
CHICHI = r("父","ちち")
OTOUSAN = "お"+r("父","とう")+"さん"
HAHA = r("母","はは")
OKAASAN = "お"+r("母","かあ")+"さん"
ANI = r("兄","あに")
ONIISAN = "お"+r("兄","にい")+"さん"
HEISHA = r("弊社","へいしゃ")
ONSHA = r("御社","おんしゃ")
BUCHOU = r("部長","ぶちょう")
TANAKA = r("田中","たなか")

# ── otlar ────────────────────────────────────────────────────────────
WATASHI = r("私","わたし")
OKYAKU  = "お"+r("客","きゃく")+"さま"
SENSEI  = r("先生","せんせい")
KABAN   = r("荷物","にもつ")
SHASHIN = r("写真","しゃしん")
SENEN   = r("千円","せんえん")


# ══════════════════════════════════════════════════════════════════════
# PJ-70 — 謙譲語
# ══════════════════════════════════════════════════════════════════════
Q_PJ70 = [
    # 1–5 tanish
    q(f"<p>{KENJOUGO} nima qiladi?</p>",
      ["Meni pasaytiradi", "Suhbatdoshni koʻtaradi",
       "Gapga kiyim beradi", "Buyruq beradi"],
      "Meni pasaytiradi",
      f"<p>Va u <strong>faqat mening</strong> ishimga qoʻyiladi. "
      f"Natija {SONKEIGO} bilan bir xil: masofa ochiladi.</p>"),

    q(f"<p>{MATSU} ni お〜する qolipiga qoʻying.</p>",
      [OMACHI_SURU, OMACHI_NINARIMASU, f"お{MATSU}します",
       f"ご{r('待','ま')}ちします"],
      OMACHI_SURU,
      f"<p><strong>ます-oʻzagi</strong> {r('待','ま')}ち, ustiga "
      f"する. お〜になる esa boshqa odam uchun (PJ-69).</p>"),

    q(f"<p>{ANNAI} ni kamtar shaklga qoʻying.</p>",
      [GOANNAI, f"お{r('案内','あんない')}します",
       f"ご{r('案内','あんない')}になります", f"{r('案内','あんない')}いたします"],
      GOANNAI,
      f"<p>Xitoycha oʻzakli feʼl <strong>ご</strong> oladi — "
      f"PJ-69 dagi お / ご qoidasining oʻzi.</p>"),

    q(f"<p>Rasmiy tanishuvda ismingizni qanday aytasiz?</p>",
      [f"ラノと{MOUSHIMASU}", f"ラノと{r('言','い')}います",
       f"ラノと{OSSHARU}います", f"ラノと{IRASSHAIMASU}"],
      f"ラノと{MOUSHIMASU}",
      f"<p>{MOUSU} — «aytmoq» ning kamtar shakli. {OSSHARU} esa "
      f"{SONKEIGO} — u suhbatdosh uchun.</p>"),

    q(f"<p>«Koʻrmoq» ning {KENJOUGO} shakli qaysi?</p>",
      [HAIKEN, GORAN, f"{r('見','み')}られる", f"お{r('見','み')}になる"],
      HAIKEN,
      f"<p>{GORAN} — {SONKEIGO}. Mening koʻrishim — "
      f"<strong>{HAIKEN}</strong>.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Ikki mahsuldor qolip bir-biridan nimasi bilan farq "
      f"qiladi?</p>",
      ["Faqat oxiri bilan: …になる ↔ …する",
       "Boshi bilan: お ↔ ご",
       "Oʻzagi bilan", "Hech qanday farqi yoʻq"],
      "Faqat oxiri bilan: …になる ↔ …する",
      f"<p>{OMACHI_NINARU} va {OMACHI_SURU} — boshi bir xil. "
      f"Shuning uchun ularni <strong>yonma-yon</strong> yodlash "
      f"kerak.</p>"),

    q(f"<p>«{OKYAKU}の{KABAN}を___» — qaysi shakl?</p>",
      [OMOCHI_SURU, f"お{r('持','も')}ちになります",
       f"{r('持','も')}ちます", f"ご{r('持','も')}ちします"],
      OMOCHI_SURU,
      f"<p>Koʻtarish — <strong>mening</strong> ishim, demak "
      f"{KENJOUGO}.</p>"),

    q(f"<p>{MAIRU} ning ます shakli istisnomi?</p>",
      [f"Yoʻq — {MAIRIMASU}, oddiy qoida",
       f"Ha — {r('参','まい')}いります",
       f"Ha — {r('参','まい')}います",
       "Bu feʼlning ます shakli yoʻq"],
      f"Yoʻq — {MAIRIMASU}, oddiy qoida",
      f"<p>Beshta istisno faqat {SONKEIGO} da: "
      f"{IRASSHAIMASU}, なさいます… {KENJOUGO} feʼllari oddiy: "
      f"{MAIRIMASU}, {MOUSHIMASU}, {ITASHIMASU}.</p>"),

    q(f"<p>«Kecha kino koʻrdim» ga {KENJOUGO} kerakmi?</p>",
      ["Yoʻq — bu ish suhbatdoshga tegmaydi",
       "Ha, doim kerak",
       "Ha, agar mijoz bilan gapirsangiz",
       "Faqat yozma tilda"],
      "Yoʻq — bu ish suhbatdoshga tegmaydi",
      f"<p>Keigo — <strong>munosabat</strong>ning tili, tarjimai "
      f"holning emas. Oddiy {r('見','み')}ました yetadi.</p>"),

    q(f"<p>«Uchrashmoq» ning {KENJOUGO} shakli qaysi?</p>",
      [OMENIKAKARU, f"お{r('会','あ')}いになる", f"{r('会','あ')}われる",
       f"{r('会','あ')}わせる"],
      OMENIKAKARU,
      f"<p>Soʻzma-soʻz «koʻzingizga ilashmoq» — kamtarlikning "
      f"tasviri.</p>"),

    q(f"<p>Kamtarroq shakl qaysi?</p>",
      [OMACHI_ITASU, OMACHI_SURU, OMACHI_NINARIMASU,
       f"{r('待','ま')}ちます"],
      OMACHI_ITASU,
      f"<p>する oʻrniga <strong>いたす</strong> qoʻyiladi. Ish "
      f"joyida va mijoz bilan aynan shu eshitiladi.</p>"),

    q(f"<p>Oʻzbekchada {KENJOUGO} ga eng yaqin narsa nima?</p>",
      ["«Kamina», «bandangiz» — lekin ular kitobiy",
       "«Keldilar», «aytdilar»",
       "«Borma» — taqiq",
       "Oʻzbekchada toʻliq muqobili bor"],
      "«Kamina», «bandangiz» — lekin ular kitobiy",
      f"<p>Oʻzbek tili boshqani koʻtaradi, lekin oʻzini deyarli "
      f"pasaytirmaydi. Shuning uchun bu dars kursdagi eng "
      f"«begona» dars.</p>"),

    # 13–16 farqlash
    q(f"<p>«{WATASHI}がお{r('待','ま')}ちになります» — nima xato?</p>",
      [f"{SONKEIGO} oʻzingizga ishlatilmaydi",
       f"{KENJOUGO} suhbatdoshga ishlatilmaydi",
       "Qoʻshimcha notoʻgʻri", "Hech qanday xato yoʻq"],
      f"{SONKEIGO} oʻzingizga ishlatilmaydi",
      f"<p>Toʻgʻrisi — {WATASHI}が{OMACHI_SURU}.</p>"),

    q(f"<p>«{OKYAKU}が{OMACHI_SURU}» — nima xato?</p>",
      [f"{KENJOUGO} suhbatdoshga ishlatilmaydi",
       f"{SONKEIGO} oʻzingizga ishlatilmaydi",
       "お oʻrniga ご boʻlishi kerak", "Hech qanday xato yoʻq"],
      f"{KENJOUGO} suhbatdoshga ishlatilmaydi",
      f"<p>Toʻgʻrisi — {OKYAKU}が{OMACHI_NINARIMASU}.</p>"),

    q(f"<p>Qaysi feʼl ご oladi, お emas?</p>",
      [SETSUMEI, MATSU, MOTSU, OKURU],
      SETSUMEI,
      f"<p>Xitoycha oʻzakli feʼllar <strong>ご</strong> oladi: "
      f"{GOSETSUMEI}, {GOANNAI}, {GORENRAKU}.</p>"),

    q(f"<p>{UKAGAU} qaysi uchta feʼlning oʻrnini bosadi?</p>",
      [f"{KIKU} · {r('訪','たず')}ねる · {IKU}",
       f"{IU} · {MIRU} · {SURU}",
       f"{IRU} · {AU} · {r('食','た')}べる",
       f"{IKU} · {KURU} · {IRU}"],
      f"{KIKU} · {r('訪','たず')}ねる · {IKU}",
      f"<p>«Soʻramoq», «tashrif buyurmoq» — bitta soʻz uchta "
      f"maʼnoni koʻtaradi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"お{r('案内','あんない')}します", GOANNAI, GOSETSUMEI,
       OMACHI_SURU],
      f"お{r('案内','あんない')}します",
      f"<p>{r('案内','あんない')} — xitoycha oʻzak, demak "
      f"<strong>ご</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{MAIRU} → {r('参','まい')}いります", f"{MOUSU} → {MOUSHIMASU}",
       f"{ITASU} → {ITASHIMASU}", f"{ORU} → {ORIMASU}"],
      f"{MAIRU} → {r('参','まい')}いります",
      f"<p>Toʻgʻrisi — <strong>{MAIRIMASU}</strong>. {KENJOUGO} "
      f"feʼllari ます da istisno emas.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{OMOCHI_SURU} · {OKYAKU}の · {KABAN}を</strong></p>",
      [f"{OKYAKU}の{KABAN}を{OMOCHI_SURU}",
       f"{KABAN}を{OKYAKU}の{OMOCHI_SURU}",
       f"{OMOCHI_SURU}{OKYAKU}の{KABAN}を",
       f"{OKYAKU}の{OMOCHI_SURU}{KABAN}を"],
      f"{OKYAKU}の{KABAN}を{OMOCHI_SURU}",
      f"<p>Egalik — toʻldiruvchi — feʼl. Yapon gapi doim feʼl "
      f"bilan tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>おきゃく:</strong> この{SHASHIN}を{r('見','み')}てください。</p>"
      f"<p><strong>てんいん:</strong> ___</p>",
      [f"{HAIKENSHIMASU}。", f"{GORAN}になります。",
       f"お{r('見','み')}になります。", f"{r('見','み')}られます。"],
      f"{HAIKENSHIMASU}。",
      f"<p>Koʻrish — <strong>xodimning</strong> ishi, demak "
      f"{KENJOUGO}. Mijozning koʻrishi esa {GORAN}.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-71 — 丁寧語 va doʻkondagi yaponcha
# ══════════════════════════════════════════════════════════════════════
Q_PJ71 = [
    # 1–5 tanish
    q(f"<p>です ning eng muloyim shakli qaysi?</p>",
      [DEGOZAIMASU, GOZAIMASU, "でいらっしゃいます", "であります"],
      DEGOZAIMASU,
      f"<p>{TEINEIGO} ning eng qalin kiyimi. Maʼno bir xil — "
      f"masofa boshqa.</p>"),

    q(f"<p>ある ning eng muloyim shakli qaysi?</p>",
      [GOZAIMASU, DEGOZAIMASU, IRASSHAIMASU, "おります"],
      GOZAIMASU,
      f"<p>お{r('手洗','てあら')}いは{r('二階','にかい')}に"
      f"{GOZAIMASU} — «hojatxona ikkinchi qavatda».</p>"),

    q(f"<p>Doʻkonga kirdingiz. Nima eshitasiz?</p>",
      [IRASSHAIMASE, KASHIKOMARI, MOUSHIWAKE, OKOSHI],
      IRASSHAIMASE,
      f"<p>Yaponiyadagi har bir doʻkonda aynan shu.</p>"),

    q(f"<p>«Bir oz kuting» ning doʻkondagi shakli qaysi?</p>",
      [SHOUSHOU, f"{r('待','ま')}ってください", f"{r('待','ま')}て",
       f"{r('待','ま')}ちなさい"],
      SHOUSHOU,
      f"<p>Bu tayyor ibora — yasalmaydi, yodlanadi.</p>"),

    q(f"<p>ませ qayerdan kelgan?</p>",
      ["ます ning buyruq shakli", "ます ning ない-shakli",
       "ませる ning qisqargani", "Alohida soʻz"],
      "ます ning buyruq shakli",
      f"<p>PJ-67 dagi え-qator. Lekin u qoʻpol emas — u faqat "
      f"mijozga qaratilgan tayyor iboralarda qolgan.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Buyurtmani qabul qildingiz. Nima deysiz?</p>",
      [KASHIKOMARI, IRASSHAIMASE, MOUSHIWAKE, OKOSHI],
      KASHIKOMARI,
      f"<p>«Tushundim, boʻladi». {r('分','わ')}かりました dan "
      f"ancha muloyimroq.</p>"),

    q(f"<p>Rasmiy uzr soʻrash iborasi qaysi?</p>",
      [MOUSHIWAKE, "すみません", "ごめんなさい", KASHIKOMARI],
      MOUSHIWAKE,
      f"<p>Soʻzma-soʻz «aytadigan sababim yoʻq». Doʻkon va ish "
      f"joyida すみません oʻrniga shu ishlatiladi.</p>"),

    q(f"<p>ございます qaysi tarmoqqa tegishli?</p>",
      [TEINEIGO, SONKEIGO, KENJOUGO, "Hech qaysiga"],
      TEINEIGO,
      f"<p>U hech kimni koʻtarmaydi va pasaytirmaydi — u butun "
      f"gapga kiyim beradi. Shuning uchun narsalar haqida ham "
      f"ishlatiladi.</p>"),

    q(f"<p>«{SENEN}になります» nega tanqid qilinadi?</p>",
      ["Chunki narx «boʻlmaydi» — u shunchaki shu",
       f"Chunki {SENEN} juda arzon",
       "Chunki なる II guruh feʼli",
       "Chunki gap qisqa"],
      "Chunki narx «boʻlmaydi» — u shunchaki shu",
      f"<p>Toʻgʻrisi — {SENEN}{DEGOZAIMASU}. Lekin bu shakl "
      f"doʻkonlarda hamma joyda eshitiladi.</p>"),

    q(f"<p>«Bayt keigo» nima?</p>",
      ["Doʻkonlarda keng tarqalgan, lekin rasmiy jihatdan notoʻgʻri shakllar",
       "Qadimgi keigo",
       "Yozma keigo",
       "Bolalar ishlatadigan keigo"],
      "Doʻkonlarda keng tarqalgan, lekin rasmiy jihatdan notoʻgʻri shakllar",
      f"<p>〜のほう, 〜になります, よろしかったでしょうか. Ularni "
      f"<strong>taniy olish</strong> kerak, gapirish shart "
      f"emas.</p>"),

    q(f"<p>Nega «bayt keigo» paydo boʻlgan?</p>",
      ["Chunki bu shakllar uzunroq, va yaponchada uzunlik muloyimlik bilan bogʻliq",
       "Chunki xodimlar yapon tilini bilmaydi",
       "Chunki ular qisqaroq",
       "Chunki ular qadimgi shakllar"],
      "Chunki bu shakllar uzunroq, va yaponchada uzunlik muloyimlik bilan bogʻliq",
      f"<p>PJ-61 va PJ-67 da koʻrgan zinapoyangizning davomi. "
      f"Xodimlar muloyimroq boʻlishga urinib, gapni "
      f"choʻzishgan.</p>"),

    q(f"<p>Bu darsning amaliy maqsadi nima?</p>",
      ["Eshitganini tushunish", "Xodim kabi gapirish",
       "Imtihondan oʻtish", "Yozma xat yozish"],
      "Eshitganini tushunish",
      f"<p>Sizdan keigo kutilmaydi. Lekin xodimning gapini "
      f"tushunmasangiz, muloqot toʻxtaydi.</p>"),

    # 13–16 farqlash
    q(f"<p>ございます ning lugʻat shakli qaysi?</p>",
      ["ござる", "ございる", "ござう", "Lugʻat shakli yoʻq"],
      "ござる",
      f"<p>Va u beshta istisnodan biri: oddiy qoida «ござります» "
      f"berardi, lekin <strong>り → い</strong>.</p>"),

    q(f"<p>«ありがとうございました» nega oʻtgan zamonda?</p>",
      ["Chunki ish tugagan — xarid boʻldi, xizmat tugadi",
       "Chunki bu xato",
       "Chunki oʻtgan zamon muloyimroq",
       "Chunki mijoz ketmoqda"],
      "Chunki ish tugagan — xarid boʻldi, xizmat tugadi",
      f"<p>Bu butunlay tabiiy. Xarid davom etayotgan boʻlsa "
      f"ありがとうございます deyiladi.</p>"),

    q(f"<p>ませ ni boshqa feʼllarga qoʻshsa boʻladimi?</p>",
      ["Yoʻq — u faqat tayyor iboralarda qolgan",
       "Ha, har qanday feʼlga",
       "Ha, faqat I guruh feʼllariga",
       "Ha, faqat yozma tilda"],
      "Yoʻq — u faqat tayyor iboralarda qolgan",
      f"<p>{IRASSHAIMASE}, くださいませ — va boshqa deyarli "
      f"hech narsa.</p>"),

    q(f"<p>Doʻkondagi yaponcha qanday oʻrganiladi?</p>",
      ["Ibora sifatida — butunligicha yodlab",
       "Grammatika qoidalari orqali",
       "Faqat kanji orqali",
       "Uni oʻrganish shart emas"],
      "Ibora sifatida — butunligicha yodlab",
      f"<p>Oʻzbekchada ham «xush kelibsiz», «marhamat», «yana "
      f"keling» — siz ularni yasamaysiz.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi shakl mavjud EMAS?</p>",
      ["ござります", GOZAIMASU, DEGOZAIMASU, "ございません"],
      "ござります",
      f"<p>Beshta istisno feʼlda り → い.</p>"),

    q(f"<p>Qaysi gap yozma ishda toʻgʻri?</p>",
      [f"{SENEN}{DEGOZAIMASU}", f"{SENEN}になります",
       f"{SENEN}のほうになります", f"{SENEN}でよろしかったでしょうか"],
      f"{SENEN}{DEGOZAIMASU}",
      f"<p>Qolgan uchtasi «bayt keigo» — eshitiladi, lekin "
      f"yozilmaydi.</p>"),

    # 19–20 tuzish
    q(f"<p>Mijoz chiqib ketmoqda. Nima deysiz?</p>",
      [OKOSHI, IRASSHAIMASE, KASHIKOMARI, SHOUSHOU],
      OKOSHI,
      f"<p>«Yana keling». お{r('越','こ')}しください — «kelmoq» "
      f"ning eng muloyim shakli.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>おきゃく:</strong> これをください。</p>"
      f"<p><strong>てんいん:</strong> ___</p>",
      [f"{KASHIKOMARI}。{SHOUSHOU}。",
       f"{IRASSHAIMASE}。{SHOUSHOU}。",
       f"{MOUSHIWAKE}。{SHOUSHOU}。",
       f"{OKOSHI}。{SHOUSHOU}。"],
      f"{KASHIKOMARI}。{SHOUSHOU}。",
      f"<p>Buyurtma qabul qilindi — {KASHIKOMARI}, keyin kutish "
      f"soʻraladi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-72 — うち va そと
# ══════════════════════════════════════════════════════════════════════
Q_PJ72 = [
    # 1–5 tanish
    q(f"<p>{UCHI} kimlarni oʻz ichiga oladi?</p>",
      ["Men, oilam, sinfim, ishxonam",
       "Mijoz va begonalar",
       "Faqat oila", "Faqat ishxona"],
      "Men, oilam, sinfim, ishxonam",
      f"<p>Va ularni <strong>pasaytiraman</strong>. {SOTO} "
      f"dagilarni esa koʻtaraman.</p>"),

    q(f"<p>Begonaga oʻz otangiz haqida gapiryapsiz. Qaysi soʻz?</p>",
      [CHICHI, OTOUSAN, f"お{r('父','ちち')}", f"{r('父','ちち')}さん"],
      CHICHI,
      f"<p>Oʻz oilangiz — {UCHI}, demak hurmat <strong>olib "
      f"tashlanadi</strong>.</p>"),

    q(f"<p>Uyda otangizga murojaat qilyapsiz. Qaysi soʻz?</p>",
      [OTOUSAN, CHICHI, f"{r('父','ちち')}さん", f"ご{r('父','ちち')}"],
      OTOUSAN,
      f"<p>Uyda chegara yoʻq — u sizning ustingizda.</p>"),

    q(f"<p>Suhbatdoshning onasi haqida gapiryapsiz. Qaysi soʻz?</p>",
      [OKAASAN, HAHA, f"ご{r('母','はは')}", f"{r('母','はは')}さん"],
      OKAASAN,
      f"<p>U {SOTO}, demak koʻtariladi.</p>"),

    q(f"<p>Oʻz kompaniyangizni qanday ataysiz?</p>",
      [HEISHA, ONSHA, f"{r('貴社','きしゃ')}", f"{r('会社','かいしゃ')}さん"],
      HEISHA,
      f"<p>{r('弊','へい')} — «kamtarin». {ONSHA} esa "
      f"suhbatdoshning kompaniyasi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Mijoz telefonda boshligʻingizni soʻradi. Qaysi feʼl?</p>",
      [ORIMASU, IRASSHAIMASU, f"います", f"{MESHIAGARU}"],
      ORIMASU,
      f"<p>Chegara <strong>siljidi</strong>: mijoz {SOTO}, "
      f"boshliq endi sizning {UCHI} ingizda.</p>"),

    q(f"<p>Ishxona ichida hamkasbingizga boshliq haqida "
      f"gapiryapsiz. Qaysi feʼl?</p>",
      [IRASSHAIMASU, ORIMASU, f"{r('参','まい')}ります", "います"],
      IRASSHAIMASU,
      f"<p>Bu yerda boshliq sizdan yuqori — {SOTO} tomonida. "
      f"Bitta odam, ikki shakl.</p>"),

    q(f"<p>Mijozga hamkasbingiz {TANAKA} haqida gapiryapsiz. "
      f"Qanday ataysiz?</p>",
      [f"{TANAKA}", f"{TANAKA}さん", f"{TANAKA}さま",
       f"{TANAKA}{BUCHOU}"],
      f"{TANAKA}",
      f"<p>Oʻz guruhingiz aʼzosiga tashqi odam oldida "
      f"<strong>さん qoʻshilmaydi</strong>. Chet elliklar eng "
      f"koʻp adashadigan joy.</p>"),

    q(f"<p>Nega yaponchada hurmat odamga emas, chegaraga "
      f"beriladi?</p>",
      ["Chunki tizim munosabatni koʻrsatadi, shaxsni emas",
       "Chunki yaponlar odamlarni hurmat qilmaydi",
       "Chunki bu qadimgi qoida",
       "Chunki chegara oʻzgarmaydi"],
      "Chunki tizim munosabatni koʻrsatadi, shaxsni emas",
      f"<p>Shuning uchun bir xil odam chegaraning ikki tomonida "
      f"boʻlishi mumkin.</p>"),

    q(f"<p>Suhbatdoshning akasi haqida gapiryapsiz. Qaysi soʻz?</p>",
      [ONIISAN, ANI, f"ご{r('兄','あに')}", f"{r('兄','あに')}さま"],
      ONIISAN,
      f"<p>{ANI} — mening akam; {ONIISAN} — sizning "
      f"akangiz.</p>"),

    q(f"<p>Yaqin doʻstlar orasida qaysi shakl ishlatiladi?</p>",
      ["Oddiy shakl — keigo kerak emas", f"{SONKEIGO}",
       f"{KENJOUGO}", "ございます"],
      "Oddiy shakl — keigo kerak emas",
      f"<p>Chegara yoʻqolganda tizim ham yoʻqoladi (PJ-45).</p>"),

    q(f"<p>Oʻzbekcha va yaponcha chegara nimasi bilan farq "
      f"qiladi?</p>",
      ["Oʻzbekchada chegara qoʻzgʻalmaydi, yaponchada har suhbatda qayta chiziladi",
       "Oʻzbekchada chegara yoʻq",
       "Yaponchada chegara doim bir joyda",
       "Farqi yoʻq"],
      "Oʻzbekchada chegara qoʻzgʻalmaydi, yaponchada har suhbatda qayta chiziladi",
      f"<p>«Sen» va «siz» orasida bir marta tanlaysiz. Yaponchada "
      f"esa bir xil odam ertalab {UCHI} da, tushdan keyin "
      f"{SOTO} da boʻlishi mumkin.</p>"),

    # 13–16 farqlash
    q(f"<p>Uchta keigo tarmogʻini chegara qanday bogʻlaydi?</p>",
      [f"{SOTO} ning ishi → {SONKEIGO}; {UCHI} ning ishi → {KENJOUGO}",
       f"{UCHI} ning ishi → {SONKEIGO}; {SOTO} ning ishi → {KENJOUGO}",
       "Chegara tarmoqlarga taʼsir qilmaydi",
       f"Uchala tarmoq ham faqat {SOTO} uchun"],
      f"{SOTO} ning ishi → {SONKEIGO}; {UCHI} ning ishi → {KENJOUGO}",
      f"<p>Ikkisiga ham tegmasa — oddiy {TEINEIGO}. Yaʼni keigo "
      f"uchta alohida tizim emas, <strong>bitta tizimning uch "
      f"tomoni</strong>.</p>"),

    q(f"<p>«{CHICHI}» va «{OTOUSAN}» — ikkalasi ham toʻgʻrimi?</p>",
      ["Ha — kimga gapirayotganingizga bogʻliq",
       f"Yoʻq, faqat {CHICHI} toʻgʻri",
       f"Yoʻq, faqat {OTOUSAN} toʻgʻri",
       "Ikkalasi ham notoʻgʻri"],
      "Ha — kimga gapirayotganingizga bogʻliq",
      f"<p>Bitta odam, ikki nom. Tinglovchi oʻzgarsa, nom ham "
      f"oʻzgaradi.</p>"),

    q(f"<p>{HEISHA} dagi {r('弊','へい')} nima degani?</p>",
      ["«Yomon», «kamtarin»", "«Katta»", "«Yangi»", "«Bizning»"],
      "«Yomon», «kamtarin»",
      f"<p>Yaʼni «bizning arzimas kompaniyamiz» — bu soʻzning "
      f"oʻzi {KENJOUGO} ning fikrini koʻrsatadi.</p>"),

    q(f"<p>Chegara qachon yoʻqoladi?</p>",
      ["Oila, yaqin doʻstlar va tengdoshlar orasida",
       "Hech qachon", "Doʻkonda", "Telefonda"],
      "Oila, yaqin doʻstlar va tengdoshlar orasida",
      f"<p>U yerda oddiy shakl ishlatiladi va keigo kerak "
      f"emas.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"Begonaga: {OTOUSAN}は{SENSEI}です",
       f"Begonaga: {CHICHI}は{SENSEI}です",
       f"Uyda: {OTOUSAN}、ごはんですよ",
       f"Suhbatdoshga: {OKAASAN}はお{r('元気','げんき')}ですか"],
      f"Begonaga: {OTOUSAN}は{SENSEI}です",
      f"<p>Oʻz otangiz tashqi odamga <strong>pasaytiriladi</strong>: "
      f"{CHICHI}.</p>"),

    q(f"<p>Qaysi gap mijozga toʻgʻri?</p>",
      [f"{TANAKA}は{ORIMASU}", f"{TANAKA}さんは{ORIMASU}",
       f"{TANAKA}さんは{IRASSHAIMASU}", f"{TANAKA}は{IRASSHAIMASU}"],
      f"{TANAKA}は{ORIMASU}",
      f"<p>さん ham tushadi, feʼl ham pasayadi — ikkalasi ham "
      f"chegara siljigani uchun.</p>"),

    # 19–20 tuzish
    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>A:</strong> {OTOUSAN}は{IRASSHAIMASU}か。</p>"
      f"<p><strong>B:</strong> いいえ、___</p>",
      [f"{CHICHI}は{ORIMASU}ません。", f"{OTOUSAN}は{ORIMASU}ません。",
       f"{CHICHI}は{IRASSHAIMASU}ません。", f"{OTOUSAN}は{IRASSHAIMASU}ません。"],
      f"{CHICHI}は{ORIMASU}ません。",
      f"<p>A tashqaridan soʻrayapti ({OTOUSAN}), B ichkaridan "
      f"javob beryapti ({CHICHI}). Ikkala gap ham toʻgʻri.</p>"),

    q(f"<p>Ish suhbatida oʻz kompaniyangiz va ularnikini "
      f"ataysiz. Qaysi juftlik?</p>",
      [f"{HEISHA} / {ONSHA}", f"{ONSHA} / {HEISHA}",
       f"{HEISHA} / {HEISHA}", f"{ONSHA} / {ONSHA}"],
      f"{HEISHA} / {ONSHA}",
      f"<p>Oʻzimniki pasayadi, ularniki koʻtariladi — butun "
      f"tizimning bir qatordagi koʻrinishi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-70 Mashq: Keigo 3 — 謙譲語",
        "tutorial":    "PJ-70:",
        "description": "お〜する oʻzini pasaytiradi, お〜になる boshqani "
                       "koʻtaradi — faqat oxiri farq qiladi.",
        "questions":   Q_PJ70,
        **DEFAULTS,
    },
    {
        "title":       "PJ-71 Mashq: Keigo 4 — ございます va doʻkon tili",
        "tutorial":    "PJ-71:",
        "description": "Doʻkondagi yaponcha yasalmaydi — yodlanadi. "
                       "Maqsad: eshitganini tushunish.",
        "questions":   Q_PJ71,
        **DEFAULTS,
    },
    {
        "title":       "PJ-72 Mashq: うちとそと",
        "tutorial":    "PJ-72:",
        "description": "内 pasayadi, 外 koʻtariladi — va chegara "
                       "suhbatdoshga qarab siljiydi.",
        "questions":   Q_PJ72,
        **DEFAULTS,
    },
]
