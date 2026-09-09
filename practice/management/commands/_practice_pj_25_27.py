# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-25 … PJ-27.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_25_27.py --master=prime \\
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

# ── i-sifatlar ────────────────────────────────────────────────────────
OO  = "<ruby>大<rt>おお</rt></ruby>きい"
CHI = "<ruby>小<rt>ちい</rt></ruby>さい"
ATA = "<ruby>新<rt>あたら</rt></ruby>しい"
TAK = "<ruby>高<rt>たか</rt></ruby>い"
YAS = "<ruby>安<rt>やす</rt></ruby>い"
OMO = "<ruby>面白<rt>おもしろ</rt></ruby>い"
MUZ = "<ruby>難<rt>むずか</rt></ruby>しい"
# い-sifatning OʻZAGI — oxirgi い siz. Tuslangan shakl doim oʻzakdan
# yasaladi; toʻliq shaklga «くない» qoʻshish notoʻgʻri soʻz beradi.
OO_S  = "<ruby>大<rt>おお</rt></ruby>き"
TAK_S = "<ruby>高<rt>たか</rt></ruby>"
YAS_S = "<ruby>安<rt>やす</rt></ruby>"
OMO_S = "<ruby>面白<rt>おもしろ</rt></ruby>"
# ── na-sifatlar ───────────────────────────────────────────────────────
SHI = "<ruby>静<rt>しず</rt></ruby>か"
YUU = "<ruby>有名<rt>ゆうめい</rt></ruby>"
BEN = "<ruby>便利<rt>べんり</rt></ruby>"
GEN = "<ruby>元気<rt>げんき</rt></ruby>"
SUK = "<ruby>好<rt>す</rt></ruby>き"
KIR = "<ruby>嫌<rt>きら</rt></ruby>い"
# ── otlar ─────────────────────────────────────────────────────────────
HO  = "<ruby>本<rt>ほん</rt></ruby>"
KY  = "<ruby>教室<rt>きょうしつ</rt></ruby>"
GK  = "<ruby>学校<rt>がっこう</rt></ruby>"
SE  = "<ruby>先生<rt>せんせい</rt></ruby>"
HIT = "<ruby>人<rt>ひと</rt></ruby>"
NEK = "<ruby>猫<rt>ねこ</rt></ruby>"
EGA = "<ruby>映画<rt>えいが</rt></ruby>"
KN  = "<ruby>昨日<rt>きのう</rt></ruby>"
ONG = "<ruby>音楽<rt>おんがく</rt></ruby>"
NG  = "<ruby>日本語<rt>にほんご</rt></ruby>"
WA  = "<ruby>私<rt>わたし</rt></ruby>"
TSK = "<ruby>図書館<rt>としょかん</rt></ruby>"
# ── feʼllar ───────────────────────────────────────────────────────────
YOMU = "<ruby>読<rt>よ</rt></ruby>む"
KAKU = "<ruby>書<rt>か</rt></ruby>く"
HANA = "<ruby>話<rt>はな</rt></ruby>す"
MATS = "<ruby>待<rt>ま</rt></ruby>つ"
KAU  = "<ruby>買<rt>か</rt></ruby>う"
NOMU = "<ruby>飲<rt>の</rt></ruby>む"
TABE = "<ruby>食<rt>た</rt></ruby>べる"
MIRU = "<ruby>見<rt>み</rt></ruby>る"
OKI  = "<ruby>起<rt>お</rt></ruby>きる"
NERU = "<ruby>寝<rt>ね</rt></ruby>る"
KAER = "<ruby>帰<rt>かえ</rt></ruby>る"
HAIR = "<ruby>入<rt>はい</rt></ruby>る"
HASI = "<ruby>走<rt>はし</rt></ruby>る"
KURU = "<ruby>来<rt>く</rt></ruby>る"
KIMS = "<ruby>来<rt>き</rt></ruby>ます"
GODA = "<ruby>五段<rt>ごだん</rt></ruby>"
ICHI = "<ruby>一段<rt>いちだん</rt></ruby>"
FUKI = "<ruby>不規則<rt>ふきそく</rt></ruby>"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-25 — い-sifatlar
# ══════════════════════════════════════════════════════════════════════
Q_PJ25 = [
    q(f"<p>Qaysi soʻz い-sifat?</p>",
      [ATA, GK, KY, SE], ATA,
      f"<p><strong>{ATA}</strong> — «yangi». Qolgan uchtasi ot: "
      f"maktab, sinf, oʻqituvchi. い-sifat doim <strong>い</strong> bilan "
      f"tugaydi.</p>"),

    q(f"<p>«Bu kitob katta» — toʻgʻri gapni tanlang.</p>",
      [f"この{HO}は{OO}です", f"この{HO}は{OO}なです",
       f"この{HO}は{OO_S}くです", f"この{HO}は{OO}でです"],
      f"この{HO}は{OO}です",
      f"<p><strong>この{HO}は{OO}です</strong> — sifat oʻzi kesim, "
      f"です esa faqat muloyimlik uchun qoʻshiladi. Sifat bilan です "
      f"orasiga hech narsa tushmaydi.</p>"),

    q(f"<p>«Yangi kitob» qanday aytiladi?</p>",
      [f"{ATA}{HO}", f"{ATA}の{HO}", f"{ATA}な{HO}", f"{HO}の{ATA}"],
      f"{ATA}{HO}",
      f"<p><strong>{ATA}{HO}</strong> — sifat otga toʻgʻridan-toʻgʻri "
      f"yopishadi. の <strong>faqat ikki otni</strong> bogʻlaydi: "
      f"{NG}の{HO} («yapon tili kitobi»).</p>"),

    q(f"<p>い-sifat kesim boʻlganda です nima qiladi?</p>",
      ["Faqat muloyimlik qoʻshadi, zamon bermaydi",
       "Sifatga hozirgi zamon beradi",
       "Sifatni otga aylantiradi",
       "Sifatni inkor qiladi"],
      "Faqat muloyimlik qoʻshadi, zamon bermaydi",
      f"<p>Sifatning oʻzi allaqachon kesim: kundalik nutqda "
      f"«{YAS}» deb ham aytiladi. です — <strong>faqat muloyimlik "
      f"belgisi</strong>. Shuning uchun zamonni ham, inkorni ham "
      f"sifatning oʻzi tashiydi.</p>"),

    q(f"<p>{YAS} soʻzining maʼnosi nima?</p>",
      ["arzon", "qimmat", "kichik", "qiyin"], "arzon",
      f"<p><strong>arzon</strong>. Uning qarama-qarshisi — {TAK}, "
      f"u ikki maʼnoda ishlatiladi: «qimmat» va «baland».</p>"),

    q(f"<p>{YAS} ning inkorini tanlang.</p>",
      [f"{YAS_S}くないです", f"{YAS}ではありません",
       f"{YAS_S}くなかったです", f"{YAS}でした"],
      f"{YAS_S}くないです",
      f"<p><strong>{YAS_S}くないです</strong> — oxirgi い oʻrniga "
      f"<strong>くない</strong>. «ではありません» esa otlar va "
      f"な-sifatlarniki.</p>"),

    q(f"<p>{OMO} ning oʻtgan zamonini tanlang.</p>",
      [f"{OMO}でした", f"{OMO}かったです",
       f"{OMO_S}かったです", f"{OMO_S}くでした"],
      f"{OMO_S}かったです",
      f"<p><strong>{OMO_S}かったです</strong> — "
      f"oxirgi い oʻrniga <strong>かった</strong>. «{OMO}でした» — bu darsdagi "
      f"eng koʻp uchraydigan xato: です zamon bermaydi.</p>"),

    q(f"<p>{TAK} ning oʻtgan zamondagi inkorini tanlang.</p>",
      [f"{TAK_S}くなかったです",
       f"{TAK_S}くないでした", f"{TAK}ではありませんでした", f"{TAK}かったです"],
      f"{TAK_S}くなかったです",
      f"<p><strong>{TAK_S}くなかったです</strong>. Buni ikki "
      f"qadamda koʻring: avval inkor — {TAK_S}くない, keyin oʻsha ない ning oʻzi "
      f"い-sifat boʻlgani uchun oʻtgan zamonga oʻtadi: ない → なかった.</p>"),

    q("<p>いい ning inkorini tanlang.</p>",
      ["いくないです", "よくないです", "いいではありません", "いかったです"],
      "よくないです",
      "<p><strong>よくないです</strong> — いい yagona tartibsiz い-sifat. "
      "Uning eski shakli <strong>よい</strong> edi va butun tuslanish oʻsha "
      "eski oʻzakdan yasaladi: い bilan boshlanadi, <strong>よ</strong> bilan "
      "tuslanadi.</p>"),

    q("<p>いい ning oʻtgan zamonini tanlang.</p>",
      ["いかったです", "いいでした", "よかったです", "いくでした"],
      "よかったです",
      "<p><strong>よかったです</strong>. Qisqa shakli <strong>よかった！</strong> "
      "— yaponlar «yaxshi boʻldi!» maʼnosida kuniga koʻp marta aytadigan "
      "ibora.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KN}の{EGA}は___。</strong> "
      f"(«Kechagi kino qiziq edi.»)</p>",
      [f"{OMO}です", f"{OMO_S}かったです",
       f"{OMO}でした", f"{OMO_S}くないです"],
      f"{OMO_S}かったです",
      f"<p>Gap <strong>oʻtgan zamonda</strong> ({KN} — kecha), shuning uchun "
      f"sifat かった shaklida boʻlishi kerak. です oʻzgarmaydi — u hozirgi "
      f"shaklda qoladi.</p>"),

    q(f"<p>«Kichkina mushuk» qanday aytiladi?</p>",
      [f"{CHI}{NEK}", f"{CHI}の{NEK}", f"{NEK}{CHI}", f"{CHI}な{NEK}"],
      f"{CHI}{NEK}",
      f"<p><strong>{CHI}{NEK}</strong>. Yaponchada sifat doim otdan "
      f"<strong>oldin</strong> turadi va hech qanday bogʻlovchi olmaydi.</p>"),

    q(f"<p>Nega «{OMO}でした» notoʻgʻri?</p>",
      ["Chunki zamonni sifat tashiydi, です emas",
       "Chunki bu sifat juda uzun",
       "Chunki でした faqat feʼllar bilan ishlatiladi",
       "Chunki oʻtgan zamon yaponchada yoʻq"],
      "Chunki zamonni sifat tashiydi, です emas",
      f"<p>い-sifat <strong>feʼl kabi</strong> ishlaydi: zamonni oʻzi "
      f"tashiydi. Toʻgʻrisi — <strong><ruby>面白<rt>おもしろ</rt></ruby>かった"
      f"です</strong>: sifat oʻzgardi, です joyida qoldi.</p>"),

    q(f"<p>Qaysi iborada の <strong>kerak</strong>?</p>",
      [f"{OO} + {HO}", f"{NG} + {HO}", f"{ATA} + {NEK}", f"{YAS} + {HO}"],
      f"{NG} + {HO}",
      f"<p><strong>{NG}の{HO}</strong> — bu <strong>ikkita ot</strong>, "
      f"shuning uchun の kerak. Qolgan uchtasi «sifat + ot», u yerda の "
      f"qoʻyilmaydi.</p>"),

    q("<p>«なかった» shakli qayerdan chiqadi?</p>",
      ["ない ning oʻzi い-sifat, shuning uchun い → かった",
       "でした ning qisqargan shakli",
       "Bu alohida yodlanadigan tartibsiz shakl",
       "Feʼllardan olingan"],
      "ない ning oʻzi い-sifat, shuning uchun い → かった",
      "<p><strong>ない</strong> ham い bilan tugaydi va い-sifat qoidasi "
      "boʻyicha tuslanadi. Yaʼni siz bitta qoidani ikki marta qoʻllaysiz — "
      "yapon grammatikasi shunday: kichik qoidalar bir-birining ustiga "
      "qoʻyiladi.</p>"),

    q(f"<p>«{YAS_S}くありません» va «{YAS_S}くないです» orasidagi farq nima?</p>",
      ["Maʼnosi bir xil, birinchisi biroz rasmiyroq",
       "Birinchisi oʻtgan zamon",
       "Birinchisi notoʻgʻri",
       "Ikkinchisi soʻroq gap"],
      "Maʼnosi bir xil, birinchisi biroz rasmiyroq",
      f"<p>Ikkalasi ham «arzon emas». <strong>くないです</strong> kundalik "
      f"nutqda koʻproq eshitiladi, <strong>くありません</strong> esa "
      f"rasmiyroq — masalan eʼlon yoki xatda.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"この{KY}は{OO_S}かったです", f"この{KY}は{OO}でした",
       f"この{KY}は{OO_S}くでした", f"この{KY}は{OO_S}かったでした"],
      f"この{KY}は{OO_S}かったです",
      f"<p><strong>この{KY}は{OO_S}かったです</strong> — «Bu sinf katta edi». "
      f"Qolgan uchtasida zamon notoʻgʻri joyga qoʻyilgan: sifat ham, です ham "
      f"bir vaqtda oʻtgan zamonga oʻtmaydi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{ATA}{HO}です", f"この{HO}は{YAS_S}くないです",
       f"いい{NEK}です", f"{MUZ}の{HO}です"],
      f"{MUZ}の{HO}です",
      f"<p><strong>{MUZ}の{HO}です</strong> notoʻgʻri: {MUZ} — sifat, "
      f"ot emas, shuning uchun の qoʻyilmaydi. Toʻgʻrisi — "
      f"<strong>{MUZ}{HO}です</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: は · この · {HO} · {OMO} · です</p>",
      [f"この{HO}は{OMO}です", f"この{OMO}{HO}はです",
       f"{OMO}この{HO}はです", f"{HO}はこの{OMO}です"],
      f"この{HO}は{OMO}です",
      f"<p><strong>この{HO}は{OMO}です</strong> — «bu kitob qiziqarli». "
      f"Tartib: koʻrsatish olmoshi → ot → は → sifat → です. Yaponchada kesim "
      f"doim gap oxirida turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>アフソナ:</strong> "
      f"{KN}の{EGA}はどうでしたか。</p><p><strong>ジャスル:</strong> ___</p>",
      [f"はい、{OMO}です", f"とても<ruby>面白<rt>おもしろ</rt></ruby>かったです",
       f"はい、{OMO}でした", f"{OMO}ではありませんでした"],
      f"とても<ruby>面白<rt>おもしろ</rt></ruby>かったです",
      f"<p>Savol {KN} («kecha») haqida, demak javob ham oʻtgan zamonda: "
      f"<strong>とても<ruby>面白<rt>おもしろ</rt></ruby>かったです</strong>.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-26 — な-sifatlar
# ══════════════════════════════════════════════════════════════════════
Q_PJ26 = [
    q(f"<p>Qaysi soʻz な-sifat?</p>",
      [SHI, OO, TAK, YAS], SHI,
      f"<p><strong>{SHI}</strong> — «jimjit». Qolgan uchtasi い bilan "
      f"tugaydigan い-sifatlar. な-sifat い bilan tugamaydi — bir nechta "
      f"istisnodan tashqari.</p>"),

    q(f"<p>«Jimjit sinf» qanday aytiladi?</p>",
      [f"{SHI}な{KY}", f"{SHI}{KY}", f"{SHI}の{KY}", f"{SHI}い{KY}"],
      f"{SHI}な{KY}",
      f"<p><strong>{SHI}な{KY}</strong> — otdan oldin turganda な-sifat "
      f"<strong>な</strong> oladi. Turning nomi ham shundan.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>この{KY}は{SHI}___。</strong></p>",
      ["です", "なです", "いです", "だです"], "です",
      f"<p><strong>です</strong>. Kesim boʻlganda <strong>な yoʻqoladi</strong> "
      f"— な faqat otdan oldin turganda paydo boʻladi.</p>"),

    q(f"<p>{SHI} ning inkorini tanlang.</p>",
      [f"{SHI}くないです", f"{SHI}ではありません",
       f"{SHI}なではありません", f"{SHI}かったです"],
      f"{SHI}ではありません",
      f"<p><strong>{SHI}ではありません</strong> — な-sifat <strong>ot "
      f"kabi</strong> tuslanadi. «くない» esa い-sifatlarniki.</p>"),

    q(f"<p>{SHI} ning oʻtgan zamonini tanlang.</p>",
      [f"{SHI}かったです", f"{SHI}でした", f"{SHI}くでした", f"{SHI}なでした"],
      f"{SHI}でした",
      f"<p><strong>{SHI}でした</strong> — otning oʻtgan zamoni bilan "
      f"aynan bir xil: <ruby>学生<rt>がくせい</rt></ruby>でした, {SHI}でした. "
      f"Yangi qoida yodlash kerak emas.</p>"),

    q("<p>Kesim boʻlganda な ga nima boʻladi?</p>",
      ["Yoʻqoladi", "です ga aylanadi", "い ga aylanadi", "Oʻzgarmaydi"],
      "Yoʻqoladi",
      f"<p><strong>Yoʻqoladi.</strong> {SHI}な{KY} — otdan oldin, な bor. "
      f"{KY}は{SHI}です — kesim, な yoʻq. Bitta sifat, ikki holat.</p>"),

    q("<p>きれい qaysi turga tegishli?</p>",
      ["い-sifat", "な-sifat", "Ot", "Feʼl"], "な-sifat",
      "<p><strong>な-sifat</strong>, い bilan tugasa ham. Sababi: bu い "
      "soʻzning bir qismi (<ruby>綺麗<rt>きれい</rt></ruby> — bitta soʻz), "
      "tuslanadigan qoʻshimcha emas. Haqiqiy い-sifatda esa oxirgi い "
      "aynan tuslanadigan qism.</p>"),

    q("<p>きれい ning inkorini tanlang.</p>",
      ["きれいくないです", "きれいではありません",
       "きれかったです", "きれくありません"],
      "きれいではありません",
      "<p><strong>きれいではありません</strong>. «きれいくないです» — "
      "bu darsdagi eng koʻp uchraydigan xato: きれい い bilan tugaydi, "
      "lekin い-sifat emas.</p>"),

    q(f"<p>«Mashhur odam» qanday aytiladi?</p>",
      [f"{YUU}な{HIT}", f"{YUU}だ{HIT}", f"{YUU}の{HIT}", f"{YUU}い{HIT}"],
      f"{YUU}な{HIT}",
      f"<p><strong>{YUU}な{HIT}</strong>. {YUU} ham い bilan tugaydigan "
      f"な-sifat — きれい va {KIR} bilan bir qatorda.</p>"),

    q(f"<p>{SUK} bilan qaysi qoʻshimcha ishlatiladi?</p>",
      ["を", "が", "に", "で"], "が",
      f"<p><strong>が</strong>. {SUK} — feʼl emas, <strong>sifat</strong>, "
      f"shuning uchun を ololmaydi. Yoqadigan narsa gapda ega boʻlib turadi: "
      f"{ONG}が{SUK}です.</p>"),

    q(f"<p>«Menga musiqa yoqadi» ni tanlang.</p>",
      [f"{WA}は{ONG}を{SUK}です", f"{WA}は{ONG}が{SUK}です",
       f"{WA}が{ONG}は{SUK}です", f"{WA}は{ONG}に{SUK}です"],
      f"{WA}は{ONG}が{SUK}です",
      f"<p><strong>{WA}は{ONG}が{SUK}です</strong>. Uni «men musiqani yaxshi "
      f"koʻraman» deb emas, <strong>«menga musiqa yoqadi»</strong> deb tarjima "
      f"qiling — shunda を qoʻyish istagi oʻz-oʻzidan yoʻqoladi.</p>"),

    q(f"<p>{KIR} qaysi turga tegishli va inkori qanday?</p>",
      [f"い-sifat — {KIR}くないです", f"な-sifat — {KIR}ではありません",
       f"い-sifat — {KIR}かったです", f"Ot — {KIR}のです"],
      f"な-sifat — {KIR}ではありません",
      f"<p><strong>な-sifat</strong>, い bilan tugasa ham. {KIR} — «yoqmaydigan», "
      f"{SUK} ning qarama-qarshisi, va u ham が oladi.</p>"),

    q(f"<p>Juftlikni toʻgʻri tanlang: {TAK} va {BEN} ning inkorlari.</p>",
      [f"{TAK_S}くないです · {BEN}ではありません",
       f"{TAK}ではありません · {BEN}くないです",
       f"{TAK_S}くないです · {BEN}くないです",
       f"{TAK}ではありません · {BEN}ではありません"],
      f"{TAK_S}くないです · {BEN}ではありません",
      f"<p>{TAK} — い-sifat, demak <strong>くない</strong>. {BEN} — な-sifat, "
      f"demak <strong>ではありません</strong>. Har bir yangi sifatni "
      f"<strong>turi bilan birga</strong> yodlang.</p>"),

    q(f"<p>Nega «{SHI}かったです» notoʻgʻri?</p>",
      [f"Chunki {SHI} な-sifat, かった esa い-sifatlarniki",
       f"Chunki {SHI} juda uzun soʻz",
       "Chunki かった faqat inkorda ishlatiladi",
       "Chunki oʻtgan zamon yaponchada yoʻq"],
      f"Chunki {SHI} な-sifat, かった esa い-sifatlarniki",
      f"<p>な-sifat <strong>ot kabi</strong> tuslanadi: toʻgʻrisi "
      f"<strong>{SHI}でした</strong>. かった shakli faqat い-sifatlarga "
      f"tegishli.</p>"),

    q("<p>Ikki sifat turini eng qisqa qanday taʼriflasa boʻladi?</p>",
      ["い-sifat feʼl kabi, な-sifat ot kabi",
       "い-sifat ot kabi, な-sifat feʼl kabi",
       "Ikkalasi ham feʼl kabi",
       "Ikkalasi ham ot kabi"],
      "い-sifat feʼl kabi, な-sifat ot kabi",
      "<p><strong>い-sifat feʼl kabi</strong> — zamonni va inkorni oʻzi "
      "tashiydi. <strong>な-sifat ot kabi</strong> — です unga zamon beradi. "
      "Butun dars shu bir jumlaga sigʻadi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WA}は{NG}を{SUK}です", f"{WA}は{NG}が{SUK}です",
       f"{WA}は{NG}が{SUK}いです", f"{WA}は{NG}が{SUK}なです"],
      f"{WA}は{NG}が{SUK}です",
      f"<p><strong>{WA}は{NG}が{SUK}です</strong>. を — feʼlning "
      f"toʻldiruvchisi, {SUK} esa feʼl emas. Va kesim boʻlganda な ham, "
      f"い ham qoʻshilmaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{GEN}な{HIT}です", f"{GEN}{HIT}です",
       f"{GEN}い{HIT}です", f"{GEN}の{HIT}です"],
      f"{GEN}な{HIT}です",
      f"<p><strong>{GEN}な{HIT}です</strong> — «tetik odam». {GEN} な-sifat, "
      f"otdan oldin な oladi. の esa faqat ikki otni bogʻlaydi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{TSK}は{SHI}です", f"きれいな<ruby>花<rt>はな</rt></ruby>です",
       f"{BEN}かったです", f"{YUU}ではありません"],
      f"{BEN}かったです",
      f"<p><strong>{BEN}かったです</strong> notoʻgʻri: {BEN} — な-sifat, "
      f"uning oʻtgan zamoni <strong>{BEN}でした</strong>. かった faqat "
      f"い-sifatlarga qoʻyiladi.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: です · {KY} · {SHI} · な</p>",
      [f"{SHI}な{KY}です", f"{KY}な{SHI}です",
       f"な{SHI}{KY}です", f"{SHI}{KY}なです"],
      f"{SHI}な{KY}です",
      f"<p><strong>{SHI}な{KY}です</strong> — «jimjit sinf». Tartib doim "
      f"bir xil: sifat → な → ot → です.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ベクゾド:</strong> "
      f"{TSK}は{SHI}ですか。</p><p><strong>ジャスル:</strong> ___</p>",
      [f"いいえ、{SHI}くないです", f"いいえ、{SHI}ではありません",
       f"いいえ、{SHI}かったです", f"いいえ、{SHI}なではありません"],
      f"いいえ、{SHI}ではありません",
      f"<p>{SHI} な-sifat boʻlgani uchun inkori <strong>ではありません</strong>. "
      f"«{SHI}くないです» — い-sifatning shakli, bu yerga toʻgʻri kelmaydi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-27 — uchta feʼl guruhi
# ══════════════════════════════════════════════════════════════════════
Q_PJ27 = [
    q("<p>Feʼlning lugʻat shakli qanday koʻrinadi?</p>",
      ["ます siz, う qatoridagi tovush bilan tugaydi",
       "Doim ます bilan tugaydi",
       "Doim る bilan tugaydi",
       "Doim kanji bilan tugaydi"],
      "ます siz, う qatoridagi tovush bilan tugaydi",
      f"<p>Lugʻat shakli (<ruby>辞書形<rt>じしょけい</rt></ruby>) — feʼlning "
      f"bezaksiz shakli: {YOMU}, {TABE}, する. U doim う qatoridagi bir "
      f"tovush bilan tugaydi. <strong>Guruh faqat shu shaklda "
      f"koʻrinadi.</strong></p>"),

    q("<p>Butun yapon tilida nechta tartibsiz feʼl bor?</p>",
      ["Ikkita", "Beshta", "Oʻnta", "Yuzdan ortiq"], "Ikkita",
      f"<p><strong>Ikkita:</strong> する va {KURU}. Shuning uchun III guruhni "
      f"({FUKI}) bir kunda yopib qoʻysa boʻladi.</p>"),

    q(f"<p>{KURU} ning ます shakli — <strong>来ます</strong> — qanday oʻqiladi?</p>",
      ["くます", "きます", "こます", "きります"], "きます",
      f"<p><strong>きます</strong>. Kanji oʻzgarmaydi, lekin "
      f"<strong>oʻqilishi</strong> oʻzgaradi: {KURU} — «くる», {KIMS} — «きます». "
      f"Bu oʻzgarish faqat furigana orqali koʻrinadi, va shuning uchun bu "
      f"kursda har bir kanji furigana bilan yuradi.</p>"),

    q(f"<p>{TABE} qaysi guruhda?</p>",
      [f"I guruh ({GODA})", f"II guruh ({ICHI})",
       f"III guruh ({FUKI})", "Hech qaysi guruhda"],
      f"II guruh ({ICHI})",
      f"<p><strong>II guruh.</strong> る bilan tugaydi va る dan oldin "
      f"<strong>べ</strong> — え qatoridan. Shuning uchun る tushadi: "
      f"<ruby>食<rt>た</rt></ruby>べます.</p>"),

    q(f"<p>{MIRU} ning ます shaklini tanlang.</p>",
      ["<ruby>見<rt>み</rt></ruby>ます", "<ruby>見<rt>み</rt></ruby>ります",
       "<ruby>見<rt>み</rt></ruby>るます", "<ruby>見<rt>み</rt></ruby>います"],
      "<ruby>見<rt>み</rt></ruby>ます",
      f"<p><strong><ruby>見<rt>み</rt></ruby>ます</strong> — II guruh: "
      f"る dan oldin み (い qatori), demak る tushadi va ます qoʻyiladi.</p>"),

    q(f"<p>{YOMU} ning ます shaklini tanlang.</p>",
      ["<ruby>読<rt>よ</rt></ruby>みます", "<ruby>読<rt>よ</rt></ruby>ます",
       "<ruby>読<rt>よ</rt></ruby>むます", "<ruby>読<rt>よ</rt></ruby>ります"],
      "<ruby>読<rt>よ</rt></ruby>みます",
      f"<p><strong><ruby>読<rt>よ</rt></ruby>みます</strong> — I guruh "
      f"({GODA}): oxirgi tovush う qatoridan い qatoriga tushadi, "
      f"む → み.</p>"),

    q(f"<p>{KAKU} ning ます shaklini tanlang.</p>",
      ["<ruby>書<rt>か</rt></ruby>きます", "<ruby>書<rt>か</rt></ruby>ます",
       "<ruby>書<rt>か</rt></ruby>くます", "<ruby>書<rt>か</rt></ruby>ります"],
      "<ruby>書<rt>か</rt></ruby>きます",
      f"<p><strong><ruby>書<rt>か</rt></ruby>きます</strong> — く → き, "
      f"xuddi {YOMU} → <ruby>読<rt>よ</rt></ruby>みます kabi. Bitta qoida, "
      f"butun I guruh.</p>"),

    q(f"<p>{HANA} ning ます shaklini tanlang.</p>",
      ["<ruby>話<rt>はな</rt></ruby>すます", "<ruby>話<rt>はな</rt></ruby>します",
       "<ruby>話<rt>はな</rt></ruby>さます", "<ruby>話<rt>はな</rt></ruby>ります"],
      "<ruby>話<rt>はな</rt></ruby>します",
      f"<p><strong><ruby>話<rt>はな</rt></ruby>します</strong>. Jadval "
      f"boʻyicha «si» chiqishi kerak edi, lekin yapon tilida bunday tovush "
      f"yoʻq — shuning uchun <strong>し</strong>.</p>"),

    q(f"<p>{MATS} ning ます shaklini tanlang.</p>",
      ["<ruby>待<rt>ま</rt></ruby>ちます", "<ruby>待<rt>ま</rt></ruby>つます",
       "<ruby>待<rt>ま</rt></ruby>たます", "<ruby>待<rt>ま</rt></ruby>ります"],
      "<ruby>待<rt>ま</rt></ruby>ちます",
      f"<p><strong><ruby>待<rt>ま</rt></ruby>ちます</strong> — つ → "
      f"<strong>ち</strong>, chunki yapon tilida «ti» tovushi yoʻq. "
      f"{HANA} → します bilan bir xil mantiq.</p>"),

    q(f"<p>{KAU} ning ます shaklini tanlang.</p>",
      ["<ruby>買<rt>か</rt></ruby>います", "<ruby>買<rt>か</rt></ruby>うます",
       "<ruby>買<rt>か</rt></ruby>ります", "<ruby>買<rt>か</rt></ruby>えます"],
      "<ruby>買<rt>か</rt></ruby>います",
      f"<p><strong><ruby>買<rt>か</rt></ruby>います</strong> — う → い. "
      f"Bu ham oddiy I guruh feʼli, hech qanday istisno yoʻq.</p>"),

    q(f"<p>{OKI} ning ます shaklini tanlang.</p>",
      ["<ruby>起<rt>お</rt></ruby>きます", "<ruby>起<rt>お</rt></ruby>きります",
       "<ruby>起<rt>お</rt></ruby>くます", "<ruby>起<rt>お</rt></ruby>きるます"],
      "<ruby>起<rt>お</rt></ruby>きます",
      f"<p><strong><ruby>起<rt>お</rt></ruby>きます</strong> — II guruh: "
      f"る dan oldin き (い qatori), demak る tushadi.</p>"),

    q(f"<p>{NOMU} feʼli qaysi guruhda?</p>",
      [f"I guruh ({GODA})", f"II guruh ({ICHI})",
       f"III guruh ({FUKI})", "Ikkala guruhga ham kiradi"],
      f"I guruh ({GODA})",
      f"<p><strong>I guruh.</strong> る bilan ham tugamaydi, する yoki "
      f"{KURU} ham emas — demak zinapoyaning uchinchi bosqichi: qolgani "
      f"I guruhda. ます shakli: <ruby>飲<rt>の</rt></ruby>みます.</p>"),

    q(f"<p>{KAER} qaysi guruhda?</p>",
      [f"II guruh ({ICHI}) — る dan oldin え bor",
       f"I guruh ({GODA}) — tuzoq feʼllardan biri",
       f"III guruh ({FUKI})", "Guruhsiz feʼl"],
      f"I guruh ({GODA}) — tuzoq feʼllardan biri",
      f"<p><strong>I guruh.</strong> Koʻrinishidan II guruhga oʻxshaydi "
      f"(え + る), lekin ます shakli buni fosh qiladi: "
      f"<strong><ruby>帰<rt>かえ</rt></ruby>ります</strong>, «かえます» emas.</p>"),

    q(f"<p>{HAIR} ning ます shaklini tanlang.</p>",
      ["<ruby>入<rt>はい</rt></ruby>ます", "<ruby>入<rt>はい</rt></ruby>ります",
       "<ruby>入<rt>はい</rt></ruby>いります", "<ruby>入<rt>はい</rt></ruby>るます"],
      "<ruby>入<rt>はい</rt></ruby>ります",
      f"<p><strong><ruby>入<rt>はい</rt></ruby>ります</strong> — beshta tuzoq "
      f"feʼldan biri: る dan oldin い bor, lekin feʼl I guruhda. "
      f"り chiqsa — guruh I.</p>"),

    q("<p>II guruh feʼlining ikkita belgisi qaysi?</p>",
      ["る bilan tugaydi va る dan oldin い yoki え bor",
       "る bilan tugaydi va る dan oldin あ yoki お bor",
       "Kanji bilan boshlanadi va る bilan tugaydi",
       "Ikkita kanjidan iborat"],
      "る bilan tugaydi va る dan oldin い yoki え bor",
      f"<p>Ikkalasi ham bir vaqtda bajarilishi kerak. Agar る dan oldin "
      f"<strong>あ, う</strong> yoki <strong>お</strong> tursa, feʼl albatta "
      f"I guruhda — masalan <ruby>作<rt>つく</rt></ruby>る.</p>"),

    q(f"<p>Quyidagilardan qaysi biri <strong>tuzoq</strong> feʼl emas?</p>",
      [KAER, HAIR, HASI, TABE], TABE,
      f"<p><strong>{TABE}</strong> — bu haqiqiy II guruh feʼli, hech qanday "
      f"tuzoq yoʻq. Qolgan uchtasi II guruhga oʻxshaydi, lekin aslida "
      f"I guruhda: <ruby>帰<rt>かえ</rt></ruby>ります, "
      f"<ruby>入<rt>はい</rt></ruby>ります, <ruby>走<rt>はし</rt></ruby>ります.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ます",
       f"<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ります",
       f"<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>るます",
       f"<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>いります"],
      f"<ruby>六時<rt>ろくじ</rt></ruby>に<ruby>帰<rt>かえ</rt></ruby>ります",
      f"<p><strong><ruby>六時<rt>ろくじ</rt></ruby>に"
      f"<ruby>帰<rt>かえ</rt></ruby>ります</strong> — «soat oltida qaytaman». "
      f"«かえます» — bu darsdagi eng koʻp uchraydigan xato.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{HO}を<ruby>読<rt>よ</rt></ruby>みます",
       f"{NG}を<ruby>話<rt>はな</rt></ruby>すます",
       f"<ruby>七時<rt>しちじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きます",
       f"{KY}に<ruby>入<rt>はい</rt></ruby>ります"],
      f"{NG}を<ruby>話<rt>はな</rt></ruby>すます",
      f"<p><strong>{NG}を<ruby>話<rt>はな</rt></ruby>すます</strong> notoʻgʻri. "
      f"I guruhda ます shunchaki qoʻshilmaydi — oxirgi tovush "
      f"<strong>oʻzgaradi</strong>: す → し, demak "
      f"<ruby>話<rt>はな</rt></ruby>します.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: "
      f"<ruby>寝<rt>ね</rt></ruby>ます · <ruby>十時<rt>じゅうじ</rt></ruby> · "
      f"に · <ruby>夜<rt>よる</rt></ruby></p>",
      [f"<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ます",
       f"<ruby>寝<rt>ね</rt></ruby>ます<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby>に",
       f"に<ruby>十時<rt>じゅうじ</rt></ruby><ruby>夜<rt>よる</rt></ruby><ruby>寝<rt>ね</rt></ruby>ます",
       f"<ruby>十時<rt>じゅうじ</rt></ruby><ruby>夜<rt>よる</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ます"],
      f"<ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby>に<ruby>寝<rt>ね</rt></ruby>ます",
      f"<p><strong><ruby>夜<rt>よる</rt></ruby><ruby>十時<rt>じゅうじ</rt></ruby>に"
      f"<ruby>寝<rt>ね</rt></ruby>ます</strong> — «kechqurun soat oʻnda uxlayman». "
      f"Vaqt kattadan kichikka boradi — avval <ruby>夜<rt>よる</rt></ruby>, "
      f"keyin soat — feʼl esa doim gap oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>アフソナ:</strong> "
      f"{KY}で{NG}を___か。</p><p><strong>シェルベク:</strong> はい。</p>",
      ["<ruby>勉強<rt>べんきょう</rt></ruby>します",
       "<ruby>勉強<rt>べんきょう</rt></ruby>すります",
       "<ruby>勉強<rt>べんきょう</rt></ruby>しるます",
       "<ruby>勉強<rt>べんきょう</rt></ruby>さます"],
      "<ruby>勉強<rt>べんきょう</rt></ruby>します",
      f"<p><strong><ruby>勉強<rt>べんきょう</rt></ruby>します</strong>. "
      f"<ruby>勉強<rt>べんきょう</rt></ruby> — ot; unga する qoʻshilsa feʼl "
      f"boʻladi va u III guruhda qoladi. Yuzlab feʼl shu qolipda yasaladi: "
      f"<ruby>電話<rt>でんわ</rt></ruby>します, "
      f"<ruby>掃除<rt>そうじ</rt></ruby>します.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-25 Mashq: い-sifatlar, ularning inkori va oʻtgan zamoni",
        "tutorial":    "PJ-25:",
        "description": "い-sifat otga の siz yopishadi, zamonni esa oʻzi tashiydi: "
                       "い → くない, い → かった. Va いい — yagona tartibsizi.",
        "questions":   Q_PJ25,
        **DEFAULTS,
    },
    {
        "title":       "PJ-26 Mashq: な-sifatlar — nega ular boshqacha tuslanadi",
        "tutorial":    "PJ-26:",
        "description": "な-sifat ot kabi tuslanadi va otdan oldin な oladi. "
                       "Ichida 〜が好きです qolipi va い bilan tugaydigan な-sifatlar.",
        "questions":   Q_PJ26,
        **DEFAULTS,
    },
    {
        "title":       "PJ-27 Mashq: Uchta feʼl guruhi — 五段, 一段, 不規則",
        "tutorial":    "PJ-27:",
        "description": "Guruhni aniqlash va har biridan ます yasash. "
                       "Ichida beshta tuzoq feʼl: 帰る, 入る, 走る, 知る, 切る.",
        "questions":   Q_PJ27,
        **DEFAULTS,
    },
]
