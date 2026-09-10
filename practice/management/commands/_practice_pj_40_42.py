# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-40 … PJ-42.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

⚠️ PJ-42 kursdagi BIRINCHI haqiqiy yangi tuslanish — potensial shakl. U
え qatorini oladi (ます い ni, ない あ ni oladi), shuning uchun har bir feʼl
uchun toʻrtinchi konstanta qoʻshiladi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_40_42.py --master=prime \\
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

# lugʻat · ます-oʻzagi · potensial
IKU,   IKI,   IKERU   = r("行","い")+"く", r("行","い")+"き", r("行","い")+"ける"
YOMU,  YOMI,  YOMERU  = r("読","よ")+"む", r("読","よ")+"み", r("読","よ")+"める"
KAKU,  KAKI,  KAKERU  = r("書","か")+"く", r("書","か")+"き", r("書","か")+"ける"
OYOGU, OYOGI, OYOGERU = r("泳","およ")+"ぐ", r("泳","およ")+"ぎ", r("泳","およ")+"げる"
HANASU,HANASHI,HANASERU = r("話","はな")+"す", r("話","はな")+"し", r("話","はな")+"せる"
KAU,   KAI,   KAERU_P = r("買","か")+"う", r("買","か")+"い", r("買","か")+"える"
MATSU, MACHI, MATERU  = r("待","ま")+"つ", r("待","ま")+"ち", r("待","ま")+"てる"
HIKU,  HIKI,  HIKERU  = r("弾","ひ")+"く", r("弾","ひ")+"き", r("弾","ひ")+"ける"
UTAU,  UTAI,  UTAERU  = r("歌","うた")+"う", r("歌","うた")+"い", r("歌","うた")+"える"
YASUMU,YASUMI,YASUMERU = r("休","やす")+"む", r("休","やす")+"み", r("休","やす")+"める"
AU,    AI,    AERU    = r("会","あ")+"う", r("会","あ")+"い", r("会","あ")+"える"
TABERU,TABE,  TABERARERU = r("食","た")+"べる", r("食","た")+"べ", r("食","た")+"べられる"
MIRU,  MI,    MIRARERU = r("見","み")+"る", r("見","み"), r("見","み")+"られる"
OKIRU, OKI,   OKIRARERU = r("起","お")+"きる", r("起","お")+"き", r("起","お")+"きられる"
SURU,  SHI,   DEKIRU  = "する", "し", "できる"
KURU,  KI,    KORARERU = r("来","く")+"る", r("来","き"), r("来","こ")+"られる"

def mashou(st):   return st + "ましょう"
def mashouka(st): return st + "ましょうか"
def masenka(st):  return st + "ませんか"
def kotoga(dic):  return dic + "ことができます"
def kotonai(dic): return dic + "ことができません"
def potmasu(pot): return pot[:-1] + "ます"
def potnai(pot):  return pot[:-1] + "ません"

HON, GK, KY, SE = r("本","ほん"), r("学校","がっこう"), r("教室","きょうしつ"), r("先生","せんせい")
NG, WA, UMI = r("日本語","にほんご"), r("私","わたし"), r("海","うみ")
MADO, MATSURI, ISSHO = r("窓","まど"), r("祭","まつ")+"り", r("一緒","いっしょ")+"に"
RYOURI, JOUZU, HETA = r("料理","りょうり"), r("上手","じょうず"), r("下手","へた")
EIGA, SHUUMATSU = r("映画","えいが"), r("週末","しゅうまつ")


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-40 — taklif qilish
# ══════════════════════════════════════════════════════════════════════
Q_PJ40 = [
    q("<p>〜ましょう oldida qaysi shakl turadi?</p>",
      ["ます oʻzagi", "Lugʻat shakli", "て-shakli", "た-shakli"],
      "ます oʻzagi",
      f"<p>{IKI} + ましょう = <strong>{mashou(IKI)}</strong>. Bu ながら va "
      f"たい bilan bir xil oʻzak.</p>"),

    q(f"<p>{TABERU} dan «yeylik» ni tanlang.</p>",
      [mashou(TABE), f"{TABERU}ましょう", f"{r('食','た')}べてましょう",
       f"{r('食','た')}べたましょう"],
      mashou(TABE),
      f"<p><strong>{mashou(TABE)}</strong> — ます oʻrniga ましょう.</p>"),

    q(f"<p>«Kino koʻrmaysizmi?» ni tanlang.</p>",
      [f"{EIGA}を{masenka(MI)}", f"{EIGA}を{mashou(MI)}",
       f"{EIGA}を{MIRU}ませんか", f"{EIGA}を{r('見','み')}ましたか"],
      f"{EIGA}を{masenka(MI)}",
      f"<p><strong>{masenka(MI)}</strong> — shakli inkor, maʼnosi "
      f"<strong>taklif</strong>. Oʻzbekchada ham «choy ichmaysizmi?» rad "
      f"emas, taklif.</p>"),

    q("<p>ましょう va ませんか — qaysi biri muloyimroq?</p>",
      ["ませんか", "ましょう", "Ikkalasi teng", "ましょうか"],
      "ませんか",
      f"<p><strong>ませんか</strong> suhbatdoshga «yoʻq» deyish uchun joy "
      f"qoldiradi. ましょう esa javobni deyarli hal qilib qoʻyadi.</p>"),

    q(f"<p>Yangi tanishga taklifni qanday berasiz?</p>",
      [f"{ISSHO}{masenka(IKI)}", f"{ISSHO}{mashou(IKI)}",
       f"{ISSHO}{IKI}ましょうよ", f"{ISSHO}{IKU}ましょう"],
      f"{ISSHO}{masenka(IKI)}",
      f"<p>Begona yoki kattaroq odamga taklif <strong>savol</strong> "
      f"shaklida beriladi: ませんか.</p>"),

    q(f"<p>«{mashouka(r('持','も')+'ち')}» nima maʼnoni beradi?</p>",
      ["Men koʻtarib berayinmi?", "Birga koʻtaraylik",
       "Koʻtaring, iltimos", "Koʻtarish mumkin emas"],
      "Men koʻtarib berayinmi?",
      f"<p>ましょう ga <strong>か</strong> qoʻshilsa, maʼno birga qilish "
      f"emas, <strong>oʻzim</strong> yordam berishni taklif qilish boʻladi.</p>"),

    q(f"<p>«Derazani ochayinmi?» ni tanlang.</p>",
      [f"{MADO}を{mashouka(r('開','あ')+'け')}", f"{MADO}を{mashou(r('開','あ')+'け')}",
       f"{MADO}を{masenka(r('開','あ')+'け')}", f"{MADO}を{r('開','あ')}けてください"],
      f"{MADO}を{mashouka(r('開','あ')+'け')}",
      f"<p><strong>ましょうか</strong> — men qilayinmi. «てください» esa "
      f"«oching» — yoʻnalish teskari.</p>"),

    q(f"<p>{SURU} va {KURU} dan ましょう yasang.</p>",
      [f"{mashou(SHI)} · {mashou(KI)}", f"するましょう · {KURU}ましょう",
       f"してましょう · {r('来','き')}てましょう", f"したましょう · {r('来','き')}たましょう"],
      f"{mashou(SHI)} · {mashou(KI)}",
      f"<p>ます shakllari します va {r('来','き')}ます, demak oʻzaklari "
      f"<strong>し</strong> va <strong>{KI}</strong>.</p>"),

    q("<p>Taklifga rozilik qanday bildiriladi?</p>",
      ["いいですね", "すみません、ちょっと…", "ちがいます", "そうですか"],
      "いいですね",
      f"<p><strong>いいですね</strong> yoki <strong>ぜひ</strong>. Yordamga "
      f"rozilik esa — お{r('願','ねが')}いします.</p>"),

    q("<p>«すみません、ちょっと…» taklifga javob sifatida nima?</p>",
      ["Muloyim rad javobi", "Rozilik", "Savol", "Kechirim soʻrash"],
      "Muloyim rad javobi",
      f"<p>Gap ataylab tugatilmaydi. Bu — PJ-32 dagi rad javobining "
      f"oʻzi: yapon tilida «yoʻq» deyishning yoʻli bitta va u har joyda "
      f"ishlaydi.</p>"),

    q(f"<p>Odatiy suhbatda qaysi tartib toʻgʻri?</p>",
      ["Avval ませんか bilan taklif, keyin ましょう bilan reja",
       "Avval ましょう bilan taklif, keyin ませんか bilan reja",
       "Faqat ましょう ishlatiladi",
       "Faqat ませんか ishlatiladi"],
      "Avval ませんか bilan taklif, keyin ましょう bilan reja",
      f"<p>{masenka(IKI)} → «いいですね» → {mashou(AI)}. Bu deyarli qolipga "
      f"aylangan tartib.</p>"),

    q(f"<p>«<ruby>気<rt>き</rt></ruby>をつけましょう» koʻcha belgisida nima "
      f"maʼnoni beradi?</p>",
      ["Ehtiyot boʻlaylik — umumiy chaqiriq", "Ehtiyot boʻling — buyruq",
       "Ehtiyot boʻlish mumkin emas", "Ehtiyot boʻlaymi?"],
      "Ehtiyot boʻlaylik — umumiy chaqiriq",
      f"<p>Eʼlonlarda ましょう hech kimni chaqirmaydi — u <strong>umumiy "
      f"chaqiriq</strong>. Yaponcha eʼlonlarning odatiy ohangi: buyruq "
      f"emas, birgalikka chaqiriq.</p>"),

    q(f"<p>«Birga» degan soʻz qaysi?</p>",
      [ISSHO, "いつも", "ときどき", "とても"], ISSHO,
      f"<p><strong>{ISSHO}</strong> — taklifni ancha issiqroq qiladi va "
      f"odatda gap boshida turadi.</p>"),

    q(f"<p>«Doʻstim bilan birga» ni tanlang.</p>",
      [f"{r('友','とも')}だちと{ISSHO}", f"{r('友','とも')}だちを{ISSHO}",
       f"{r('友','とも')}だちに{ISSHO}", f"{r('友','とも')}だちで{ISSHO}"],
      f"{r('友','とも')}だちと{ISSHO}",
      f"<p><strong>と</strong> — PJ-19 dagi «va, bilan». U {ISSHO} bilan "
      f"juft yuradi va shu tartibda turadi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{SHUUMATSU}に{UMI}へ{masenka(IKI)}", f"{SHUUMATSU}に{UMI}へ{IKU}ませんか",
       f"{SHUUMATSU}に{UMI}へ{r('行','い')}ってませんか",
       f"{SHUUMATSU}に{UMI}へ{r('行','い')}ったませんか"],
      f"{SHUUMATSU}に{UMI}へ{masenka(IKI)}",
      f"<p>ませんか <strong>ます oʻzagiga</strong> qoʻshiladi, lugʻat "
      f"shakliga emas.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{r('六時','ろくじ')}に{mashou(AI)}", f"{r('六時','ろくじ')}に{AU}ましょう",
       f"{r('六時','ろくじ')}に{r('会','あ')}ってましょう",
       f"{r('六時','ろくじ')}に{mashou(AI)}でした"],
      f"{r('六時','ろくじ')}に{mashou(AI)}",
      f"<p>ましょう zamon olmaydi — u doim kelajakka qaraydi, shuning uchun "
      f"«でした» qoʻshilmaydi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{ISSHO}{masenka(TABE)}", f"{MADO}を{mashouka(r('開','あ')+'け')}",
       f"{GK}へ{IKU}ましょう", f"{HON}を{mashou(YOMI)}"],
      f"{GK}へ{IKU}ましょう",
      f"<p>ましょう ます oʻzagiga qoʻshiladi: <strong>{mashou(IKI)}</strong>, "
      f"«{IKU}ましょう» emas.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TABERU} → {mashou(TABE)}", f"{YOMU} → {mashou(YOMI)}",
       f"{SURU} → するましょう", f"{OYOGU} → {mashou(OYOGI)}"],
      f"{SURU} → するましょう",
      f"<p>する ning ます oʻzagi — <strong>し</strong>, demak "
      f"<strong>{mashou(SHI)}</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {masenka(IKI)} · へ · "
      f"{MATSURI} · {ISSHO}</p>",
      [f"{ISSHO}{MATSURI}へ{masenka(IKI)}", f"{ISSHO}{MATSURI}を{masenka(IKI)}",
       f"へ{MATSURI}{ISSHO}{masenka(IKI)}", f"{masenka(IKI)}{ISSHO}{MATSURI}へ"],
      f"{ISSHO}{MATSURI}へ{masenka(IKI)}",
      f"<p>Manzil <strong>へ</strong> oladi, を emas — {r('行','い')}く "
      f"harakat feʼli. {ISSHO} gap boshida, feʼl esa oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"{SHUUMATSU}に{EIGA}を{masenka(MI)}。</p>"
      f"<p><strong>ムニラ:</strong> いいですね。___</p>",
      [f"{r('六時','ろくじ')}に{mashou(AI)}", f"{r('六時','ろくじ')}に{masenka(AI)}",
       f"{r('六時','ろくじ')}に{r('会','あ')}いました", f"{r('六時','ろくじ')}に{AU}ましょう"],
      f"{r('六時','ろくじ')}に{mashou(AI)}",
      f"<p>Rozilik berilgan, demak endi <strong>reja</strong> tuziladi — "
      f"bu ましょう ning ishi. Yana bir ませんか qoʻyish taklifni "
      f"takrorlash boʻlardi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-41 — 〜ことができます
# ══════════════════════════════════════════════════════════════════════
Q_PJ41 = [
    q("<p>〜ことができます oldida qaysi shakl turadi?</p>",
      ["Lugʻat shakli", "ます oʻzagi", "て-shakli", "た-shakli"],
      "Lugʻat shakli",
      f"<p><strong>{kotoga(OYOGU)}</strong> — feʼl umuman tuslanmaydi. "
      f"Shuning uchun uchala guruh ham bir xil.</p>"),

    q(f"<p>{YOMU} dan «oʻqiy olaman» ni tanlang.</p>",
      [kotoga(YOMU), f"{YOMI}ことができます",
       f"{r('読','よ')}んでことができます", f"{r('読','よ')}んだことができます"],
      kotoga(YOMU),
      f"<p><strong>{kotoga(YOMU)}</strong> — lugʻat shakli oʻzgarmaydi.</p>"),

    q(f"<p>{TABERU} dan «yeya olaman» ni tanlang.</p>",
      [kotoga(TABERU), f"{TABE}ことができます",
       f"{r('食','た')}べてことができます", f"{r('食','た')}べたことができます"],
      kotoga(TABERU),
      f"<p>II guruh ham xuddi shunday: lugʻat shakli + ことができます.</p>"),

    q("<p>こと bu qolipda nima qilyapti?</p>",
      ["Feʼlni otga aylantiryapti", "Feʼlni oʻtgan zamonga oʻtkazyapti",
       "Feʼlni inkor qilyapti", "Hech narsa — bezak"],
      "Feʼlni otga aylantiryapti",
      f"<p>こと — «ish, narsa» degan ot. Oʻzbekchadagi «-ish» ning oʻzi: "
      f"«suz<strong>ish</strong> mumkin». Shuning uchun u <strong>が</strong> "
      f"oladi.</p>"),

    q(f"<p>«Yapon tilini bilaman» ni ot bilan tanlang.</p>",
      [f"{NG}ができます", f"{NG}をできます",
       f"{NG}にできます", f"{NG}のことができます"],
      f"{NG}ができます",
      f"<p>Koʻnikma oti bilan こと kerak emas, va できます baribir "
      f"<strong>が</strong> oladi.</p>"),

    q(f"<p>Nega できます が oladi, を emas?</p>",
      ["Chunki u holat bildiradi — 好き va ほしい bilan bir qatorda",
       "Chunki できます — II guruh feʼli",
       "Chunki を faqat odamlar bilan keladi",
       "Chunki が qisqaroq"],
      "Chunki u holat bildiradi — 好き va ほしい bilan bir qatorda",
      f"<p>Yapon tilida «xohish, yoqish, uddalash» — <strong>holat</strong>, "
      f"ish emas. Holat gapida narsa ega boʻlib turadi.</p>"),

    q(f"<p>«Suza olmayman» ni tanlang.</p>",
      [kotonai(OYOGU), f"{kotoga(OYOGU)}ない",
       f"{OYOGI}ことができません", f"{OYOGU}ことをできません"],
      kotonai(OYOGU),
      f"<p>できます oddiy feʼl, shuning uchun odatdagidek "
      f"<strong>できません</strong> boʻladi.</p>"),

    q(f"<p>«Suza oldim» (oʻtgan zamon) ni tanlang.</p>",
      [f"{OYOGU}ことができました", f"{OYOGU}ことができますでした",
       f"{r('泳','およ')}いだことができます", f"{OYOGU}ことができでした"],
      f"{OYOGU}ことができました",
      f"<p>Zamonni <strong>できます</strong> tashiydi; lugʻat shakli "
      f"oʻzgarmaydi.</p>"),

    q(f"<p>{KURU} dan «kela olaman» ni tanlang.</p>",
      [f"{kotoga(KURU)}", f"{KI}ことができます",
       f"{r('来','き')}てことができます", f"{r('来','き')}ますことができます"],
      f"{kotoga(KURU)}",
      f"<p>Lugʻat shakli — <strong>{KURU}</strong>, oʻqilishi «くる». "
      f"Bu qolipda kanji oʻqilishi oʻzgarmaydi.</p>"),

    q(f"<p>Nega bu qolip yangi feʼl uchun ishonchli?</p>",
      ["Chunki feʼl umuman tuslanmaydi — guruhini bilmasangiz ham ishlaydi",
       "Chunki u qisqaroq",
       "Chunki u faqat I guruh bilan ishlaydi",
       "Chunki u kundalik nutqda koʻproq uchraydi"],
      "Chunki feʼl umuman tuslanmaydi — guruhini bilmasangiz ham ishlaydi",
      f"<p>Bu kursda kam uchraydigan holat: qolip <em>uzunroq</em>, lekin "
      f"<em>osonroq</em>.</p>"),

    q(f"<p>«{RYOURI}が{JOUZU}です» nima maʼnoni beradi?</p>",
      ["Ovqat pishirishga mohir", "Ovqat pishirishni xohlaydi",
       "Ovqat pishira olmaydi", "Ovqat pishirmoqchi"],
      "Ovqat pishirishga mohir",
      f"<p>{JOUZU} — な-sifat, va u ham <strong>が</strong> oladi. Uning "
      f"qarama-qarshisi — {HETA}.</p>"),

    q(f"<p>Oʻzingiz haqingizda «{JOUZU}です» deyish nega notoʻgʻri?</p>",
      ["Chunki yaponchada bu maqtanchoqlik boʻlib eshitiladi",
       "Chunki 上手 faqat oʻtgan zamonda ishlatiladi",
       "Chunki 上手 — feʼl",
       "Chunki 上手 が olmaydi"],
      "Chunki yaponchada bu maqtanchoqlik boʻlib eshitiladi",
      f"<p>Oʻzingiz haqingizda <strong>{HETA}</strong> yoki «まだ{JOUZU}では"
      f"ありません» deng. Kamtarlik bu yerda odat emas, <strong>qoida</strong>.</p>"),

    q(f"<p>«{NG}ができます» va «{NG}を{HANASU}ことができます» — farqi nima?</p>",
      ["Birinchisi kengroq — til biladi; ikkinchisi aniq bitta ish",
       "Ikkinchisi kengroq",
       "Farqi yoʻq",
       "Birinchisi notoʻgʻri"],
      "Birinchisi kengroq — til biladi; ikkinchisi aniq bitta ish",
      f"<p>Ot bilan aytilganda gap <strong>koʻnikma</strong> haqida; "
      f"feʼl bilan aytilganda esa aniq bir ish — gapirish — haqida.</p>"),

    q(f"<p>Bu qolip qayerda koʻproq uchraydi?</p>",
      ["Eʼlon va yozma tilda", "Faqat soʻzlashuvda",
       "Faqat savollarda", "Faqat oʻtgan zamonda"],
      "Eʼlon va yozma tilda",
      f"<p>U keyingi darsdagi qisqa shakldan biroz rasmiyroq eshitiladi — "
      f"odam odamga emas, tashkilot odamga gapirganda.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"ピアノを{kotoga(HIKU)}", f"ピアノを{HIKI}ことができます",
       f"ピアノを{HIKU}ことをできます", f"ピアノを{r('弾','ひ')}いてことができます"],
      f"ピアノを{kotoga(HIKU)}",
      f"<p>こと oldida lugʻat shakli, va こと <strong>が</strong> oladi — "
      f"を emas.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{WA}は{NG}ができます", f"{WA}は{NG}をできます",
       f"{WA}は{NG}にできます", f"{WA}は{NG}ができるます"],
      f"{WA}は{NG}ができます",
      f"<p>できます が oladi. Va u oddiy feʼl — «できるます» degan shakl "
      f"yoʻq.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{UMI}で{kotoga(OYOGU)}", f"{NG}ができます",
       f"{HON}を{YOMI}ことができます", f"{RYOURI}が{JOUZU}です"],
      f"{HON}を{YOMI}ことができます",
      f"<p>こと oldida <strong>lugʻat shakli</strong> turadi, ます oʻzagi "
      f"emas: <strong>{kotoga(YOMU)}</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{OYOGU} → {kotoga(OYOGU)}", f"{TABERU} → {kotoga(TABERU)}",
       f"{SURU} → {SHI}ことができます", f"{KURU} → {kotoga(KURU)}"],
      f"{SURU} → {SHI}ことができます",
      f"<p>Lugʻat shakli — <strong>{SURU}</strong>, demak "
      f"<strong>することができます</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: ことができます · を · "
      f"{HON} · {YOMU}</p>",
      [f"{HON}を{kotoga(YOMU)}", f"{kotoga(YOMU)}{HON}を",
       f"を{HON}{kotoga(YOMU)}", f"{HON}{kotoga(YOMU)}を"],
      f"{HON}を{kotoga(YOMU)}",
      f"<p>Toʻldiruvchi oʻz feʼlidan oldin turadi va <strong>を</strong> "
      f"saqlaydi; こと esa <strong>が</strong> oladi. Ikki qoʻshimcha bir "
      f"gapda.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>やまだ:</strong> "
      f"{r('何','なに')}ができますか。</p><p><strong>パリ:</strong> ___</p>",
      [f"ピアノを{kotoga(HIKU)}", f"ピアノを{HIKI}ことができます",
       f"ピアノを{kotoga(HIKU)}か", f"ピアノを{HIKU}ことをできます"],
      f"ピアノを{kotoga(HIKU)}",
      f"<p>Savolga javob — demak か kerak emas. こと oldida lugʻat shakli "
      f"va こと <strong>が</strong> oladi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-42 — potensial shakl
# ══════════════════════════════════════════════════════════════════════
Q_PJ42 = [
    q("<p>I guruh feʼlining potensial shaklida oxirgi tovush qaysi qatorga "
      "koʻtariladi?</p>",
      ["え qatori", "あ qatori", "い qatori", "お qatori"],
      "え qatori",
      f"<p>{YOMU} → <strong>{YOMERU}</strong>. Bu toʻrtinchi qator: ます い "
      f"ni, ない あ ni, potensial esa <strong>え</strong> ni oladi.</p>"),

    q(f"<p>{OYOGU} ning potensial shaklini tanlang.</p>",
      [OYOGERU, f"{r('泳','およ')}がれる", f"{r('泳','およ')}ぎれる",
       f"{r('泳','およ')}ぐれる"],
      OYOGERU,
      f"<p><strong>{OYOGERU}</strong> — ぐ え qatoriga: げ, keyin る.</p>"),

    q(f"<p>{KAKU} ning potensial shaklini tanlang.</p>",
      [KAKERU, f"{r('書','か')}かれる", f"{r('書','か')}きれる", f"{r('書','か')}くれる"],
      KAKERU,
      f"<p><strong>{KAKERU}</strong> — く → け + る.</p>"),

    q(f"<p>{KAU} ning potensial shaklini tanlang.</p>",
      [KAERU_P, f"{r('買','か')}われる", f"{r('買','か')}いれる", f"{r('買','か')}うれる"],
      KAERU_P,
      f"<p><strong>{KAERU_P}</strong> — う → <strong>え</strong>. Diqqat: "
      f"ない-shaklida <strong>わ</strong> edi ({r('買','か')}わない), bu yerda "
      f"esa oddiy え.</p>"),

    q(f"<p>{TABERU} ning potensial shaklini tanlang.</p>",
      [TABERARERU, f"{r('食','た')}べれる", f"{r('食','た')}べえる",
       f"{r('食','た')}べらる"],
      TABERARERU,
      f"<p><strong>{TABERARERU}</strong> — II guruhda る oʻrniga られる. "
      f"«{r('食','た')}べれる» kundalik nutqda eshitiladi, lekin u "
      f"ら{r('抜','ぬ')}き{r('言葉','ことば')} — imtihonda ら ni "
      f"tashlamang.</p>"),

    q(f"<p>{SURU} ning potensial shakli qaysi?</p>",
      [DEKIRU, "すられる", "しられる", "せる"], DEKIRU,
      f"<p><strong>{DEKIRU}</strong> — va siz uni oʻtgan darsdan "
      f"ことが<strong>できます</strong> ichida bilasiz. U oʻsha feʼlning "
      f"oʻzi.</p>"),

    q(f"<p>{KURU} ning potensial shakli — <strong>来られる</strong> — qanday "
      f"oʻqiladi?</p>",
      ["こられる", "きられる", "くられる", "けられる"], "こられる",
      f"<p><strong>こられる</strong> — bu kanji yana oʻqilishini "
      f"oʻzgartiradi. Endi u くる, きます, きて, こない va こられる "
      f"boʻlib oʻqiladi.</p>"),

    q("<p>Potensial shakl qaysi guruhga tegishli boʻlib chiqadi?</p>",
      ["II guruh", "I guruh", "III guruh", "Hech qaysi"],
      "II guruh",
      f"<p>Natija <strong>る</strong> bilan tugaydi va oldida え yoki い "
      f"turadi. Demak {potmasu(YOMERU)}, {potnai(YOMERU)} — hammasi "
      f"tanish.</p>"),

    q(f"<p>{YOMERU} ning ます shaklini tanlang.</p>",
      [potmasu(YOMERU), f"{YOMERU}ます", f"{r('読','よ')}めります",
       f"{r('読','よ')}めれます"],
      potmasu(YOMERU),
      f"<p><strong>{potmasu(YOMERU)}</strong> — II guruh feʼli, demak る "
      f"tushadi va ます qoʻshiladi.</p>"),

    q(f"<p>Potensial gapda toʻldiruvchi qaysi qoʻshimchani oladi?</p>",
      ["が", "を", "に", "で"], "が",
      f"<p>{HON}<strong>が</strong>{potmasu(YOMERU)} — imkoniyat "
      f"<strong>holat</strong>, ish emas. 好き, ほしい, できる bilan bir "
      f"qatorda.</p>"),

    q(f"<p>«Kitob oʻqiy olaman» ni tanlang.</p>",
      [f"{HON}が{potmasu(YOMERU)}", f"{HON}を{potmasu(YOMERU)}",
       f"{HON}に{potmasu(YOMERU)}", f"{HON}が{r('読','よ')}みます"],
      f"{HON}が{potmasu(YOMERU)}",
      f"<p>Potensial gapda を emas, <strong>が</strong>. Bu qoida butun "
      f"kursni bogʻlaydi.</p>"),

    q(f"<p>{HANASU} ning potensial shaklini tanlang.</p>",
      [HANASERU, f"{r('話','はな')}される", f"{r('話','はな')}しれる",
       f"{r('話','はな')}すれる"],
      HANASERU,
      f"<p><strong>{HANASERU}</strong> — す → せ + る.</p>"),

    q(f"<p>«{r('食','た')}べれる» haqida nima toʻgʻri?</p>",
      ["Kundalik nutqda eshitiladi, lekin yozma tilda ら tashlanmaydi",
       "Bu yagona toʻgʻri shakl",
       "Bu butunlay notoʻgʻri va hech qayerda ishlatilmaydi",
       "Bu oʻtgan zamon shakli"],
      "Kundalik nutqda eshitiladi, lekin yozma tilda ら tashlanmaydi",
      f"<p>Bu — ら{r('抜','ぬ')}き{r('言葉','ことば')}, yoshlar orasida keng "
      f"tarqalgan. Imtihonda va yozma tilda <strong>{TABERARERU}</strong> "
      f"toʻgʻri.</p>"),

    q("<p>Potensial shakl va 〜ことができます — farqi nima?</p>",
      ["Maʼnosi bir xil; potensial qisqa va kundalik, ikkinchisi rasmiyroq",
       "Potensial faqat oʻtgan zamonda",
       "ことができます faqat I guruh bilan",
       "Potensial kuchliroq imkoniyat"],
      "Maʼnosi bir xil; potensial qisqa va kundalik, ikkinchisi rasmiyroq",
      f"<p>Xato qilish qiyin. Yangi feʼl uchrasa va guruhiga ishonchingiz "
      f"komil boʻlmasa — <strong>ことができます</strong> bilan ayting, u "
      f"har doim toʻgʻri.</p>"),

    q(f"<p>{MIRU} ning potensial shaklini tanlang.</p>",
      [MIRARERU, f"{r('見','み')}れる", f"{r('見','み')}りられる", f"{r('見','み')}らる"],
      MIRARERU,
      f"<p><strong>{MIRARERU}</strong> — II guruh: る → られる.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{UMI}で{potmasu(OYOGERU)}", f"{UMI}で{OYOGERU}ます",
       f"{UMI}で{r('泳','およ')}げれます", f"{UMI}で{r('泳','およ')}がれます"],
      f"{UMI}で{potmasu(OYOGERU)}",
      f"<p>Potensial shakl II guruh feʼli, demak る tushadi: "
      f"<strong>{potmasu(OYOGERU)}</strong>.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{NG}が{potmasu(HANASERU)}", f"{HON}を{potmasu(YOMERU)}",
       f"{potmasu(TABERARERU)}", f"ピアノが{potmasu(HIKERU)}"],
      f"{HON}を{potmasu(YOMERU)}",
      f"<p>Potensial gapda toʻldiruvchi <strong>が</strong> oladi: "
      f"<strong>{HON}が{potmasu(YOMERU)}</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{YOMU} → {YOMERU}", f"{TABERU} → {TABERARERU}",
       f"{KAU} → {r('買','か')}われる", f"{SURU} → {DEKIRU}"],
      f"{KAU} → {r('買','か')}われる",
      f"<p>Potensialda う <strong>え</strong> ga koʻtariladi: "
      f"<strong>{KAERU_P}</strong>. わ faqat ない-shaklida.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {potmasu(YOMERU)} · が · "
      f"{HON}</p>",
      [f"{HON}が{potmasu(YOMERU)}", f"が{HON}{potmasu(YOMERU)}",
       f"{potmasu(YOMERU)}{HON}が", f"{HON}{potmasu(YOMERU)}が"],
      f"{HON}が{potmasu(YOMERU)}",
      f"<p>Ega va uning が qoʻshimchasi feʼldan oldin turadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イムロン:</strong> "
      f"{r('去年','きょねん')}は{potnai(OYOGERU)}でしたね。</p>"
      f"<p><strong>イノム:</strong> はい。でも<ruby>今<rt>いま</rt></ruby>は"
      f"___。</p>",
      [potmasu(OYOGERU), potnai(OYOGERU),
       f"{r('泳','およ')}ぎます", f"{OYOGERU}ます"],
      potmasu(OYOGERU),
      f"<p>«でも» qarama-qarshilikni bildiradi: avval suza olmasdi, endi "
      f"<strong>suza oladi</strong>. «{r('泳','およ')}ぎます» esa shunchaki "
      f"«suzaman» — imkoniyat haqida emas.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-40 Mashq: 〜ましょう va 〜ませんか",
        "tutorial":    "PJ-40:",
        "description": "Taklif qilish. Ikkalasi ham ます oʻzagidan, lekin "
                       "ませんか muloyimroq — u «yoʻq» uchun joy qoldiradi.",
        "questions":   Q_PJ40,
        **DEFAULTS,
    },
    {
        "title":       "PJ-41 Mashq: 〜ことができます",
        "tutorial":    "PJ-41:",
        "description": "Imkoniyatning uzun yoʻli. Feʼl umuman tuslanmaydi, "
                       "shuning uchun uchala guruh ham bir xil.",
        "questions":   Q_PJ41,
        **DEFAULTS,
    },
    {
        "title":       "PJ-42 Mashq: Potensial shakl",
        "tutorial":    "PJ-42:",
        "description": "え qatori + る, られる, できる. Natija doim II guruh "
                       "feʼli boʻlib chiqadi, va toʻldiruvchi が oladi.",
        "questions":   Q_PJ42,
        **DEFAULTS,
    },
]
