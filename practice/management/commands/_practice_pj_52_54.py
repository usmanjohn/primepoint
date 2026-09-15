# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-52 … PJ-54.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Batchning oʻqitish oʻqi — bitta soʻzning qoʻshnisiga qarab kiyinishi.
Bitta {SHIZUKA} toʻrt joyda toʻrt xil:
    と oldida  → だ      (PJ-46)
    ot oldida  → な      (PJ-48)
    なら oldida → quruq  (PJ-52)
    から/ので  → だから / なので   (PJ-53)
Uchala test ham shu jadvalga qaytadi, `verify_pj_52_54_copula.py` esa
har bir kalitni oʻsha jadvaldan qayta hisoblaydi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_52_54.py --master=prime \\
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


# ── feʼllar ──────────────────────────────────────────────────────────
IKU,   ITTA    = r("行","い")+"く",    r("行","い")+"った"
IKIMASU        = r("行","い")+"きます"
KURU,  KITA    = r("来","く")+"る",    r("来","き")+"た"
KAU,   KATTA   = r("買","か")+"う",    r("買","か")+"った"
KAIMASU        = r("買","か")+"います"
YOMU,  YONDA   = r("読","よ")+"む",    r("読","よ")+"んだ"
TOMARU, TOMATTA = r("止","と")+"まる",  r("止","と")+"まった"
OKURERU, OKURETA = r("遅","おく")+"れる", r("遅","おく")+"れました"
ERABU          = r("選","えら")+"ぶ"
ARU            = "ある"
YOMIMASHITA    = r("読","よ")+"みました"
ERABIMASU      = r("選","えら")+"びます"
ERABIMASHITA   = r("選","えら")+"びました"
KAIMASEN       = r("買","か")+"いません"
KIMASUKA       = r("来","き")+"ますか"

# ── sifat va otlar ───────────────────────────────────────────────────
TAKAI, YASUI   = r("高","たか")+"い",  r("安","やす")+"い"
MUZUKASHII     = r("難","むずか")+"しい"
OMOSHIROI      = r("面白","おもしろ")+"い"
NAGAI          = r("長","なが")+"い"
ABUNAI         = r("危","あぶ")+"ない"
SHIZUKA        = r("静","しず")+"か"
BENRI          = r("便利","べんり")
GENKI          = r("元気","げんき")
GAKUSEI        = r("学生","がくせい")
AME            = r("雨","あめ")
HON            = r("本","ほん")
HEYA           = r("部屋","へや")
EKI            = r("駅","えき")
DENSHA         = r("電車","でんしゃ")
BYOUKI         = r("病気","びょうき")
NIHON          = r("日本","にほん")
NIHONGO        = r("日本語","にほんご")
KYOTO          = r("京都","きょうと")
RYOKOU         = r("旅行","りょこう")
SHIAI          = r("試合","しあい")
OKANE          = "お" + r("金","かね")
NAMAE          = r("名前","なまえ")
SHITSUREI      = r("失礼","しつれい")
RIYUU          = r("理由","りゆう")
KYOU           = r("今日","きょう")
ASHITA         = r("明日","あした")
SUKI           = r("好","す")+"き"


# ══════════════════════════════════════════════════════════════════════
# PJ-52 — 〜なら
# ══════════════════════════════════════════════════════════════════════
Q_PJ52 = [
    # 1–5 tanish
    q(f"<p>{GAKUSEI} ni なら qolipiga qoʻying.</p>",
      [f"{GAKUSEI}なら", f"{GAKUSEI}だなら", f"{GAKUSEI}のなら",
       f"{GAKUSEI}ななら"],
      f"{GAKUSEI}なら",
      f"<p>なら oldida ot <strong>だ ni tashlaydi</strong>. Sababi: "
      f"なら ning oʻzi だ dan yasalgan, unga ikkinchi だ kerak emas.</p>"),

    q(f"<p>{SHIZUKA} ni なら qolipiga qoʻying.</p>",
      [f"{SHIZUKA}なら", f"{SHIZUKA}だなら", f"{SHIZUKA}になら",
       f"{SHIZUKA}いなら"],
      f"{SHIZUKA}なら",
      f"<p>な-sifat ham だ ni tashlaydi. Diqqat: <strong>{SHIZUKA}"
      f"な{HEYA}</strong> (ot oldida な) bilan chalkashtirmang.</p>"),

    q(f"<p>{YASUI} ni なら qolipiga qoʻying.</p>",
      [f"{YASUI}なら", f"{r('安','やす')}くなら", f"{YASUI}だなら",
       f"{r('安','やす')}かったなら"],
      f"{YASUI}なら",
      f"<p>い-sifat oʻzi turadi — bu darsda hech narsa "
      f"oʻzgarmaydi.</p>"),

    q(f"<p>{IKIMASU} ni なら qolipiga qoʻying.</p>",
      [f"{IKU}なら", f"{IKIMASU}なら", f"{IKU}だなら", f"{ITTA}ら"],
      f"{IKU}なら",
      f"<p>なら dan oldin <strong>oddiy shakl</strong> turadi — "
      f"ます hech qachon emas.</p>"),

    q(f"<p>なら boshqa uch shartdan nimasi bilan farq qiladi?</p>",
      ["U birovning aytgan gapini koʻtarib oladi",
       "U faqat oʻtgan zamon bilan keladi",
       "U faqat feʼllar bilan keladi",
       "Undan keyin buyruq turolmaydi"],
      "U birovning aytgan gapini koʻtarib oladi",
      f"<p>Boshqa uchtasi olamni tasvirlaydi; <strong>なら</strong> "
      f"suhbatga javob beradi. Shuning uchun u deyarli doim maslahat "
      f"yoki fikr bilan keladi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{NIHON}へ{IKU}なら、カメラを{KAIMASU}» — kamera qayerda "
      f"olinadi?</p>",
      ["Joʻnashdan oldin, shu yerda", "Yaponiyada",
       "Yaponiyadan qaytgandan keyin", "Buni gapdan bilib boʻlmaydi"],
      "Joʻnashdan oldin, shu yerda",
      f"<p>Faqat なら da natija <strong>shartdan oldin</strong> "
      f"boʻlishi mumkin. «{NIHON}へ{ITTA}ら» boʻlsa kamera Yaponiyada "
      f"olinardi — bu ikki gap ikki boshqa reja haqida.</p>"),

    q(f"<p>«{NIHON}へ{ITTA}ら、カメラを{KAIMASU}» — kamera qayerda "
      f"olinadi?</p>",
      ["Yaponiyada", "Joʻnashdan oldin", "Aeroportda", "Farqi yoʻq"],
      "Yaponiyada",
      f"<p>たら da natija doim shartdan <strong>keyin</strong>. "
      f"Avval boradi, keyin oladi.</p>"),

    q(f"<p>A: この{HON}を{YOMIMASHITA}か。 B: その{HON}なら"
      f"{YOMIMASHITA}。 — B ning なら si nima qilyapti?</p>",
      ["Suhbatdoshning savolini mavzu qilib koʻtaryapti",
       "Shart qoʻyyapti", "Kelajak haqida gapiryapti",
       "Kitobni tavsiya qilyapti"],
      "Suhbatdoshning savolini mavzu qilib koʻtaryapti",
      f"<p>Bu <strong>mavzu koʻrsatuvchi なら</strong>: «U kitobnimi — "
      f"oʻqiganman». Oʻzbekchadagi «-nimi», «-ga kelsak» ohangi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{EKI}___、そこを"
      f"{r('右','みぎ')}へ{r('行','い')}ってください。</strong></p>",
      ["なら", "だから", "ので", "とき"],
      "なら",
      f"<p>Kimdir bekat qayerdaligini soʻragan — <strong>なら</strong> "
      f"oʻsha savolni koʻtarib oladi: «Bekatnimi — u yerdan "
      f"oʻngga».</p>"),

    q(f"<p>«{RYOKOU}に{IKU}なら、{KYOTO}がいいですよ» — bu gapni kim "
      f"aytadi?</p>",
      ["Sayohatga boraman deganga maslahat beradigan odam",
       "Sayohatga borayotgan odamning oʻzi",
       "Sayohatni taqiqlayotgan odam",
       "Kioto haqida hech nima bilmaydigan odam"],
      "Sayohatga boraman deganga maslahat beradigan odam",
      f"<p>なら dagi shart <strong>gapiruvchiniki emas</strong> — u "
      f"suhbatdoshdan olingan. Shuning uchun bu maslahat.</p>"),

    q(f"<p>Qaysi gapda なら oʻrinsiz?</p>",
      [f"{AME}が{r('降','ふ')}るなら、{r('家','いえ')}にいます — hech kim yomgʻir haqida gapirmagan",
       f"{NIHON}へ{IKU}なら、{KYOTO}がいいですよ",
       f"その{HON}なら{YOMIMASHITA}",
       f"{EKI}なら、そこです"],
      f"{AME}が{r('降','ふ')}るなら、{r('家','いえ')}にいます — hech kim yomgʻir haqida gapirmagan",
      f"<p>なら uchun suhbatdosh oldin bir narsa aytgan boʻlishi kerak. "
      f"Yolgʻiz ob-havo taxmini uchun <strong>たら</strong> "
      f"ishlatiladi.</p>"),

    q(f"<p>«{BENRI}» ni なら qolipiga qoʻying.</p>",
      [f"{BENRI}なら", f"{BENRI}だなら", f"{BENRI}になら", f"{BENRI}いなら"],
      f"{BENRI}なら",
      f"<p>{BENRI} — な-sifat («qulay»), demak だ tushadi.</p>"),

    # 13–16 farqlash
    q(f"<p>Bitta {SHIZUKA} soʻzi と, ot va なら oldida qanday "
      f"koʻrinadi?</p>",
      [f"{SHIZUKA}だと · {SHIZUKA}な{HEYA} · {SHIZUKA}なら",
       f"{SHIZUKA}なと · {SHIZUKA}だ{HEYA} · {SHIZUKA}だなら",
       f"{SHIZUKA}と · {SHIZUKA}{HEYA} · {SHIZUKA}なら",
       f"{SHIZUKA}だと · {SHIZUKA}だ{HEYA} · {SHIZUKA}だなら"],
      f"{SHIZUKA}だと · {SHIZUKA}な{HEYA} · {SHIZUKA}なら",
      f"<p>Bitta boglama, uch qoʻshni, uch kiyim: と oldida "
      f"<strong>だ</strong> (PJ-46), ot oldida <strong>な</strong> "
      f"(PJ-48), なら oldida <strong>quruq</strong> (PJ-52).</p>"),

    q(f"<p>Toʻrtta shartdan qaysi birida natija shartdan oldin "
      f"boʻlishi mumkin?</p>",
      ["〜なら", "〜たら", "〜ば", "〜と"],
      "〜なら",
      f"<p>Bu なら ning eng oʻtkir xususiyati. Qolgan uchtasida "
      f"natija doim shartdan keyin.</p>"),

    q(f"<p>Mashina yoki tabiat qonuni haqida qaysi shart "
      f"ishlatiladi?</p>",
      ["〜と", "〜なら", "〜たら", "〜ば"],
      "〜と",
      f"<p>と — «har doim shunday boʻladi» (PJ-51). なら esa "
      f"suhbatga javob beradi.</p>"),

    q(f"<p>Shubha boʻlsa qaysi shartni tanlash tavsiya qilinadi?</p>",
      ["〜たら", "〜なら", "〜ば", "〜と"],
      "〜たら",
      f"<p>たら da hech qanday cheklov yoʻq — undan keyin buyruq ham, "
      f"taklif ham, xohish ham kela oladi (PJ-50).</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{GAKUSEI}だなら", f"{GAKUSEI}なら", f"{SHIZUKA}なら",
       f"{YASUI}なら"],
      f"{GAKUSEI}だなら",
      f"<p>なら oldida だ <strong>tushadi</strong>. Toʻgʻrisi — "
      f"{GAKUSEI}なら.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{IKU}なら{ERABIMASU}", f"{IKIMASU}なら{ERABIMASU}",
       f"{IKU}だなら{ERABIMASU}", f"{ITTA}なら{ERABIMASHITA}"],
      f"{IKU}なら{ERABIMASU}",
      f"<p>なら dan oldin oddiy shakl, feʼlga だ qoʻshilmaydi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{KYOTO}がいいですよ · {NIHON}へ · {IKU}なら</strong></p>",
      [f"{NIHON}へ{IKU}なら、{KYOTO}がいいですよ",
       f"{KYOTO}がいいですよ、{NIHON}へ{IKU}なら",
       f"{IKU}なら{NIHON}へ、{KYOTO}がいいですよ",
       f"{NIHON}へ{KYOTO}がいいですよ{IKU}なら"],
      f"{NIHON}へ{IKU}なら、{KYOTO}がいいですよ",
      f"<p>Shart oldinda, maslahat keyin. Yapon gapi feʼl bilan "
      f"tugaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>イノム:</strong> {ASHITA}{r('山','やま')}へ"
      f"{IKIMASU}。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"{r('山','やま')}へ{IKU}なら、この{r('地図','ちず')}をどうぞ。",
       f"{r('山','やま')}へ{IKU}たら、この{r('地図','ちず')}をどうぞ。",
       f"{r('山','やま')}へ{IKIMASU}なら、この{r('地図','ちず')}をどうぞ。",
       f"{r('山','やま')}へ{ITTA}なら、この{r('地図','ちず')}をどうぞ。"],
      f"{r('山','やま')}へ{IKU}なら、この{r('地図','ちず')}をどうぞ。",
      f"<p>Munira Inomning gapini koʻtarib olyapti — demak "
      f"<strong>なら</strong>. Va xarita <em>ketishdan oldin</em> "
      f"beriladi, bu ham なら ning oʻz ishi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-53 — 〜から va 〜ので
# ══════════════════════════════════════════════════════════════════════
Q_PJ53 = [
    # 1–5 tanish
    q(f"<p>Yaponchada sabab va natija qanday tartibda turadi?</p>",
      ["Sabab oldinda, natija keyin", "Natija oldinda, sabab keyin",
       "Tartibi erkin", "Sabab doim gap oxirida"],
      "Sabab oldinda, natija keyin",
      f"<p>Oʻzbekchadagidek: «Poyezd toʻxta<em>gani uchun</em> kech "
      f"qoldim». から va ので sababning <strong>orqasiga</strong> "
      f"yopishadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHIZUKA}___ので、"
      f"よく{YOMU}めます。</strong></p>",
      ["な", "だ", "の", "い"],
      "な",
      f"<p>ので = <strong>の + で</strong>, va の — ot. Otdan oldin "
      f"な-sifat <strong>な</strong> kiyadi (PJ-48).</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{AME}___から、"
      f"{SHIAI}はありません。</strong></p>",
      ["だ", "な", "の", "で"],
      "だ",
      f"<p>から esa <strong>だ</strong> oladi. Ikkisi teskari: "
      f"{AME}だから ✓ · {AME}なので ✓.</p>"),

    q(f"<p>{GAKUSEI} ni ので bilan ulang.</p>",
      [f"{GAKUSEI}なので", f"{GAKUSEI}だので", f"{GAKUSEI}ので",
       f"{GAKUSEI}のので"],
      f"{GAKUSEI}なので",
      f"<p>Ot ham ので oldida <strong>な</strong> oladi.</p>"),

    q(f"<p>«どうして» degan savolga yolgʻiz sabab bilan javob "
      f"berganda gap qanday tugaydi?</p>",
      ["〜からです", "〜のでです", "〜からだです", "〜のでだ"],
      "〜からです",
      f"<p>«のでです» degan shakl <strong>yoʻq</strong>. Yolgʻiz sabab "
      f"doim からです bilan yopiladi.</p>"),

    # 6–12 qoʻllash
    q(f"<p>Ustozga kechikkaningizni tushuntiryapsiz. Qaysi biri "
      f"odobliroq?</p>",
      [f"{DENSHA}が{TOMATTA}ので、{OKURETA}",
       f"{DENSHA}が{TOMATTA}から、{OKURETA}",
       f"{OKURETA}、{DENSHA}が{TOMATTA}ので",
       f"{DENSHA}が{TOMATTA}なので、{OKURETA}"],
      f"{DENSHA}が{TOMATTA}ので、{OKURETA}",
      f"<p><strong>ので</strong> — bu holat, mening qarorim emas. "
      f"から bu yerda «men aybdor emasman» degandek eshitilishi "
      f"mumkin.</p>"),

    q(f"<p>«{ABUNAI}から、{KURU}ないでください» — nega bu yerda から?</p>",
      ["Chunki bu gapiruvchining oʻz hukmi va undan keyin iltimos turibdi",
       f"Chunki {ABUNAI} い-sifat",
       "Chunki ので faqat oʻtgan zamon bilan keladi",
       "Chunki gap inkorda"],
      "Chunki bu gapiruvchining oʻz hukmi va undan keyin iltimos turibdi",
      f"<p>から — «men shuni sabab deb hisobladim». U kuchli, aniq va "
      f"buyruq bilan yaxshi keladi.</p>"),

    q(f"<p>«{BYOUKI}だった___» — «kasal boʻlganim uchun» degan qisqa "
      f"javobni toʻldiring.</p>",
      ["からです", "のでです", "からだです", "なのでです"],
      "からです",
      f"<p>Natija aytilmaydi — u savolning oʻzida bor. Shuning uchun "
      f"<strong>からです</strong>.</p>"),

    q(f"<p>Ikki alohida gap yozmoqchisiz. Ikkinchisini qanday "
      f"boshlaysiz?</p>",
      ["ですから / だから", "なので", "からです", "ので"],
      "ですから / だから",
      f"<p>«{KYOU}は{AME}です。<strong>ですから</strong>、{SHIAI}は"
      f"ありません。» ので gap ichida qoladi, alohida gapni "
      f"boshlamaydi.</p>"),

    q(f"<p>から oldida です・ます turishi mumkinmi?</p>",
      ["Ha — から oddiy shakl ham, muloyim shakl ham qabul qiladi",
       "Yoʻq, faqat oddiy shakl",
       "Yoʻq, faqat ます",
       "Faqat yozma tilda mumkin"],
      "Ha — から oddiy shakl ham, muloyim shakl ham qabul qiladi",
      f"<p>{IKU}から ✓ va {IKIMASU}から ✓. ので esa oddiy shaklni "
      f"afzal koʻradi.</p>"),

    q(f"<p>«{BENRI}» ni から bilan ulang.</p>",
      [f"{BENRI}だから", f"{BENRI}なから", f"{BENRI}から", f"{BENRI}のから"],
      f"{BENRI}だから",
      f"<p>な-sifat から oldida <strong>だ</strong> oladi — ので "
      f"oldidagi な bilan chalkashtirmang.</p>"),

    q(f"<p>«{NIHONGO}が{SUKI}なので、{r('毎日','まいにち')}"
      f"{r('勉強','べんきょう')}します» — nega な?</p>",
      [f"Chunki {SUKI} な-sifat va ので dagi の ot",
       f"Chunki {SUKI} feʼl",
       "Chunki gap muloyim shaklda",
       f"Chunki {NIHONGO} ot"],
      f"Chunki {SUKI} な-sifat va ので dagi の ot",
      f"<p>{SUKI} — な-sifat. ので = の + で, demak undan oldin "
      f"PJ-48 ning qoidasi ishlaydi.</p>"),

    # 13–16 farqlash
    q(f"<p>から va ので ning asosiy farqi nima?</p>",
      ["から — mening hukmim; ので — shunchaki holat",
       "から — hozirgi zamon; ので — oʻtgan zamon",
       "から — ogʻzaki; ので — yozma",
       "Farqi yoʻq"],
      "から — mening hukmim; ので — shunchaki holat",
      f"<p>Shuning uchun ので kechirim va tushuntirishda yumshoqroq, "
      f"から esa buyruq va iltimosda kuchliroq eshitiladi.</p>"),

    q(f"<p>から <strong>だ</strong> oladi. ので nima oladi?</p>",
      ["な", "だ", "の", "hech nima"],
      "な",
      f"<p>{AME}<strong>だ</strong>から ✓ · {AME}<strong>な</strong>ので ✓. "
      f"«{AME}なから» ham, «{AME}だので» ham yoʻq.</p>"),

    q(f"<p>«のでです» shakli bormi?</p>",
      ["Yoʻq — yolgʻiz sabab doim からです",
       "Ha, u ancha muloyim",
       "Ha, lekin faqat yozma tilda",
       "Ha, ot bilan"],
      "Yoʻq — yolgʻiz sabab doim からです",
      f"<p>ので faqat gap ichida, natija bilan birga keladi.</p>"),

    q(f"<p>Iltimos yoki buyruq bilan qaysi biri tabiiyroq?</p>",
      ["から", "ので", "Ikkalasi ham notabiiy", "Farqi yoʻq"],
      "から",
      f"<p>«{ABUNAI}から、{KURU}ないでください» — から gapiruvchining "
      f"hukmini bildiradi, shuning uchun buyruq bilan mos tushadi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{SHIZUKA}だので", f"{SHIZUKA}なので", f"{SHIZUKA}だから",
       f"{YASUI}ので"],
      f"{SHIZUKA}だので",
      f"<p>ので oldida <strong>な</strong>: {SHIZUKA}なので. "
      f"Qolgan uchtasi toʻgʻri.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{DENSHA}が{TOMATTA}ので、{OKURETA}",
       f"{OKURETA}ので、{DENSHA}が{TOMATTA}",
       f"{DENSHA}が{TOMATTA}なので、{OKURETA}",
       f"{DENSHA}が{TOMATTA}のでです"],
      f"{DENSHA}が{TOMATTA}ので、{OKURETA}",
      f"<p>Sabab oldinda, feʼldan keyin な qoʻshilmaydi, va "
      f"«のでです» degan shakl yoʻq.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{SHIAI}はありません · {KYOU}は{AME}な · ので</strong></p>",
      [f"{KYOU}は{AME}なので、{SHIAI}はありません",
       f"{SHIAI}はありませんので、{KYOU}は{AME}な",
       f"ので{KYOU}は{AME}な、{SHIAI}はありません",
       f"{KYOU}は{SHIAI}はありませんので{AME}な"],
      f"{KYOU}は{AME}なので、{SHIAI}はありません",
      f"<p>Sabab oldinda, natija keyin. Ot ので oldida "
      f"<strong>な</strong> oladi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>せんせい:</strong> どうして{r('来','き')}ませんでしたか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"{BYOUKI}だったからです。", f"{BYOUKI}だったのでです。",
       f"{BYOUKI}だったなのでです。", f"{BYOUKI}からです。"],
      f"{BYOUKI}だったからです。",
      f"<p>Yolgʻiz sabab — <strong>からです</strong>, va oʻtgan zamon "
      f"{BYOUKI}<strong>だった</strong>.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-54 — 〜が va 〜けど
# ══════════════════════════════════════════════════════════════════════
Q_PJ54 = [
    # 1–5 tanish
    q(f"<p>«この{HON}が{SUKI}です» dagi が qanaqa が?</p>",
      ["Ega koʻrsatkichi — oldida ot turibdi",
       "Bogʻlovchi «lekin»", "Soʻroq qoʻshimchasi", "Joy koʻrsatkichi"],
      "Ega koʻrsatkichi — oldida ot turibdi",
      f"<p>Ajratish qoidasi bitta savolda: が dan oldin <strong>ot</strong> "
      f"turibdimi yoki <strong>tugallangan gap</strong>?</p>"),

    q(f"<p>«{YASUI}ですが、{KAIMASEN}» dagi が-chi?</p>",
      ["Bogʻlovchi «lekin» — oldida tugallangan gap turibdi",
       "Ega koʻrsatkichi", "Toʻldiruvchi koʻrsatkichi", "Soʻroq qoʻshimchasi"],
      "Bogʻlovchi «lekin» — oldida tugallangan gap turibdi",
      f"<p>«{YASUI}です» ot emas, u kesimli gap. Demak bu が — "
      f"<strong>«lekin»</strong>.</p>"),

    q(f"<p>が va けど gapda qayerda turadi?</p>",
      ["Birinchi gapning oxiriga yopishadi",
       "Ikkinchi gapning boshida turadi",
       "Gapning eng oxirida", "Tartibi erkin"],
      "Birinchi gapning oxiriga yopishadi",
      f"<p>Oʻzbekcha «lekin» ikkinchi gapning boshida turadi; yaponcha "
      f"が va けど esa <strong>birinchi gapga</strong> yopishadi — bir "
      f"gap chapda.</p>"),

    q(f"<p>Doʻstingizga gapiryapsiz. Qaysi bogʻlovchi tabiiyroq?</p>",
      ["けど", "が", "けれども", "ですが"],
      "けど",
      f"<p>けど — suhbat, doʻstlar, kundalik. が esa yozma til va "
      f"rasmiy nutq.</p>"),

    q(f"<p>«すみませんが、{EKI}はどこですか» — bu yerda が nima "
      f"qilyapti?</p>",
      ["Hech qanday qarama-qarshilik yoʻq — bu muloyim ochqich",
       "«Lekin» maʼnosini beryapti",
       "Ega koʻrsatyapti",
       "Savolni kuchaytiryapti"],
      "Hech qanday qarama-qarshilik yoʻq — bu muloyim ochqich",
      f"<p>«Kechirasiz, <em>lekin</em> bekat qayerda?» emas. Bu が "
      f"faqat <strong>odob</strong> — gapni yumshoq boshlash uchun.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«Yapon tili qiyin, lekin qiziqarli» ni rasmiy yozing.</p>",
      [f"{NIHONGO}は{MUZUKASHII}ですが、{OMOSHIROI}です",
       f"{NIHONGO}は{MUZUKASHII}です。が、{OMOSHIROI}です",
       f"{NIHONGO}は{MUZUKASHII}ですけど、{OMOSHIROI}",
       f"{NIHONGO}は{MUZUKASHII}、が{OMOSHIROI}です"],
      f"{NIHONGO}は{MUZUKASHII}ですが、{OMOSHIROI}です",
      f"<p>が birinchi gapga yopishadi va ikkalasi ham muloyim "
      f"shaklda qoladi.</p>"),

    q(f"<p>が va けど boshqa bogʻlovchilardan nimasi bilan farq "
      f"qiladi?</p>",
      ["Ular oldingi gapning muloyimligini oʻzgartirmaydi",
       "Ular doim oddiy shakl talab qiladi",
       "Ular doim ます talab qiladi",
       "Ular gap boshida turadi"],
      "Ular oldingi gapning muloyimligini oʻzgartirmaydi",
      f"<p>と (PJ-46), とき (PJ-49), ので (PJ-53) — hammasi oddiy shakl "
      f"talab qilgan edi. が va けど esa <strong>talab "
      f"qilmaydi</strong>.</p>"),

    q(f"<p>«{r('買','か')}いたいけど、{OKANE}がない» — bu qanday "
      f"uslub?</p>",
      ["Oddiy shakl — doʻstlar orasidagi gap",
       "Muloyim shakl", "Rasmiy yozma uslub", "Imtihon uslubi"],
      "Oddiy shakl — doʻstlar orasidagi gap",
      f"<p>Ikkala qism ham oddiy shaklda va bogʻlovchi けど — bu "
      f"kundalik suhbat.</p>"),

    q(f"<p>けど · けれど · けれども · が — bularni rasmiylik "
      f"boʻyicha tartiblang.</p>",
      ["けど → けれど → けれども → が",
       "が → けど → けれど → けれども",
       "けれども → けれど → けど → が",
       "が → けれども → けど → けれど"],
      "けど → けれど → けれども → が",
      f"<p>Qanchalik uzun boʻlsa, shunchalik rasmiy — va eng "
      f"rasmiysi qisqa <strong>が</strong>.</p>"),

    q(f"<p>«{r('行','い')}きたいですけど…» — nega gap tugamagan?</p>",
      ["Ataylab: bu «yoʻq» degan javobning eng odobli shakli",
       "Gapiruvchi soʻzni unutgan",
       "Bu yozma xato",
       "Chunki けど doim gap oxirida turadi"],
      "Ataylab: bu «yoʻq» degan javobning eng odobli shakli",
      f"<p>Davomi («…lekin vaqtim yoʻq») aytilmaydi. Siz fikringizni "
      f"oxirigacha aytmay, suhbatdoshga joy qoldirasiz.</p>"),

    q(f"<p>Inshoda gapni けど bilan tugatish mumkinmi?</p>",
      ["Yoʻq — bu faqat ogʻzaki nutqning uslubi",
       "Ha, agar gap qisqa boʻlsa",
       "Ha, bu muloyimlik belgisi",
       "Faqat birinchi xatboshida"],
      "Yoʻq — bu faqat ogʻzaki nutqning uslubi",
      f"<p>Insho va imtihonda gap toʻliq boʻlishi kerak, va bogʻlovchi "
      f"<strong>が</strong> boʻladi.</p>"),

    q(f"<p>«{SHITSUREI}ですが、お{NAMAE}は{r('何','なん')}ですか» ni "
      f"tarjima qiling.</p>",
      ["Uzr, ismingiz nima?", "Odobsiz, lekin ismingiz nima?",
       "Ismingiz nima, lekin uzr", "Ismingizni ayta olmayman"],
      "Uzr, ismingiz nima?",
      f"<p>Bu tayyor ibora. Yaponiyada begonaga murojaat qilishning "
      f"deyarli yagona yoʻli — <strong>すみませんが</strong> yoki "
      f"<strong>{SHITSUREI}ですが</strong>.</p>"),

    # 13–16 farqlash
    q(f"<p>Qaysi gapda が ega koʻrsatkichi?</p>",
      [f"{r('雨','あめ')}が{r('降','ふ')}っています",
       f"{TAKAI}ですが、{KAIMASU}",
       f"すみませんが、…",
       f"{NAGAI}ですが、{OMOSHIROI}です"],
      f"{r('雨','あめ')}が{r('降','ふ')}っています",
      f"<p>Undan oldin <strong>ot</strong> ({r('雨','あめ')}) turibdi. "
      f"Qolgan uchtasida が dan oldin kesimli gap bor.</p>"),

    q(f"<p>«{TAKAI}ですけど、{KAU}» — nima notabiiy?</p>",
      ["Gap oxiri oddiy shaklda, boshi esa muloyim — oxirini ham muloyim qilish kerak",
       "けど い-sifat bilan ishlatilmaydi",
       "けど oʻrniga が boʻlishi kerak",
       "Hech qanday xato yoʻq"],
      "Gap oxiri oddiy shaklda, boshi esa muloyim — oxirini ham muloyim qilish kerak",
      f"<p>Gapning eng oxiri butun gapning uslubini belgilaydi. "
      f"Toʻgʻrisi — {TAKAI}ですけど、{KAIMASU}.</p>"),

    q(f"<p>でも va けど orasidagi farq nima?</p>",
      ["でも yangi gapning boshida turadi, けど oldingi gapga yopishadi",
       "でも rasmiyroq", "けど faqat yozma tilda ishlatiladi",
       "Farqi yoʻq"],
      "でも yangi gapning boshida turadi, けど oldingi gapga yopishadi",
      f"<p>«{TAKAI}です。でも、{KAIMASU}» ✓ va «{TAKAI}ですけど、"
      f"{KAIMASU}» ✓ — bir maʼno, ikki joylashuv.</p>"),

    q(f"<p>が dan oldin qaysi shakl turishi mumkin?</p>",
      ["Oddiy shakl ham, です・ます ham",
       "Faqat oddiy shakl", "Faqat です・ます", "Faqat た-shakli"],
      "Oddiy shakl ham, です・ます ham",
      f"<p>Bu が va けど ning oʻziga xosligi: ular oldingi gapning "
      f"uslubiga <strong>tegmaydi</strong>.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{TAKAI}です。が、{KAIMASU}。",
       f"{TAKAI}ですが、{KAIMASU}。",
       f"{TAKAI}けど、{KAU}。",
       f"{TAKAI}です。でも、{KAIMASU}。"],
      f"{TAKAI}です。が、{KAIMASU}。",
      f"<p>が ikkinchi gapning boshida turolmaydi — u birinchi gapga "
      f"<strong>yopishadi</strong>. でも esa boshida turadi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{GAKUSEI}ですが、{r('働','はたら')}いています",
       f"{GAKUSEI}だですが、{r('働','はたら')}いています",
       f"{GAKUSEI}ですけど、{r('働','はたら')}いている",
       f"{GAKUSEI}が、{r('働','はたら')}いています"],
      f"{GAKUSEI}ですが、{r('働','はたら')}いています",
      f"<p>«だです» degan shakl yoʻq; uchinchisida uslub aralashgan; "
      f"toʻrtinchisida esa が ot bilan turibdi va ega koʻrsatkichidek "
      f"oʻqiladi.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{OMOSHIROI}です · この{HON}は{NAGAI}です · が</strong></p>",
      [f"この{HON}は{NAGAI}ですが、{OMOSHIROI}です",
       f"{OMOSHIROI}ですが、この{HON}は{NAGAI}です",
       f"が、この{HON}は{NAGAI}です{OMOSHIROI}です",
       f"この{HON}は{OMOSHIROI}です{NAGAI}ですが"],
      f"この{HON}は{NAGAI}ですが、{OMOSHIROI}です",
      f"<p>«Bu kitob uzun, lekin qiziqarli.» が birinchi gapga "
      f"yopishadi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ラノ:</strong> {ASHITA}、{KIMASUKA}。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"{r('行','い')}きたいですけど…", f"{r('行','い')}きたいけどです…",
       f"けど{r('行','い')}きたいです…", f"{r('行','い')}きたいですが{r('行','い')}きます。"],
      f"{r('行','い')}きたいですけど…",
      f"<p>Gapni けど da qoldirish — «yoʻq» degan javobning eng odobli "
      f"shakli. Davomi aytilmaydi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-52 Mashq: Shart 3 — 〜なら",
        "tutorial":    "PJ-52:",
        "description": "なら oldida だ tushadi, u birovning gapini "
                       "koʻtarib oladi, va faqat unda natija shartdan "
                       "oldin boʻla oladi.",
        "questions":   Q_PJ52,
        **DEFAULTS,
    },
    {
        "title":       "PJ-53 Mashq: Sabab — 〜から va 〜ので",
        "tutorial":    "PJ-53:",
        "description": "から だ oladi, ので esa な. Va kechirim "
                       "soʻraganda doim ので.",
        "questions":   Q_PJ53,
        **DEFAULTS,
    },
    {
        "title":       "PJ-54 Mashq: Qarama-qarshilik — 〜が va 〜けど",
        "tutorial":    "PJ-54:",
        "description": "«Lekin» birinchi gapga yopishadi. Va すみませんが "
                       "— bu qarama-qarshilik emas, odob.",
        "questions":   Q_PJ54,
        **DEFAULTS,
    },
]
