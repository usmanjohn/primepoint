# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-55 … PJ-57.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchda ikki narsa jim sinadi:
  * PJ-55 — て-shaklining toʻgʻri yasalishi (ot va な-sifat <b>で</b>
    oladi, い-sifat <b>くて</b>, inkor <b>なくて</b>);
  * PJ-57 — なる ga ulanish (い-sifat <b>く</b>, ot <b>に</b>, feʼl
    <b>ように</b>). Uchala ulanish ham `verify_pj_55_57_forms.py` da
    qoidadan qayta hisoblanadi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_55_57.py --master=prime \\
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


# ── feʼllar: lugʻat · て · ても ────────────────────────────────────────
IKU,   ITTE,   ITTEMO   = r("行","い")+"く",    r("行","い")+"って",    r("行","い")+"っても"
IKIMASU                 = r("行","い")+"きます"
IKANAI, IKANAKUTEMO     = r("行","い")+"かない",  r("行","い")+"かなくても"
KURU,  KITE,   KITEMO   = r("来","く")+"る",     r("来","き")+"て",      r("来","き")+"ても"
KONAKUTEMO              = r("来","こ")+"なくても"
YOMU,  YONDE,  YONDEMO  = r("読","よ")+"む",     r("読","よ")+"んで",    r("読","よ")+"んでも"
TABERU, TABETE, TABETEMO = r("食","た")+"べる",  r("食","た")+"べて",    r("食","た")+"べても"
FURU,  FUTTE,  FUTTEMO  = r("降","ふ")+"る",     r("降","ふ")+"って",    r("降","ふ")+"っても"
SAGASU, SAGASHITEMO     = r("探","さが")+"す",   r("探","さが")+"しても"
HANASU                  = r("話","はな")+"す"
HANASERU                = r("話","はな")+"せる"
YOMERU                  = r("読","よ")+"める"
WASURERU, WASURENAI     = r("忘","わす")+"れる", r("忘","わす")+"れない"
HATARAKU                = r("働","はたら")+"く"
HASHIRU                 = r("走","はし")+"る"
HASHIRIMASU             = r("走","はし")+"ります"
HASHITTEIMASU           = r("走","はし")+"っています"
HATARAKIMASU            = r("働","はたら")+"きます"
BENKYOU_SHITEIMASU      = r("勉強","べんきょう")+"しています"
HANASHIMASU             = r("話","はな")+"します"
TAMERU                  = r("貯","た")+"める"
TAMETEIMASU             = r("貯","た")+"めています"
KAU                     = r("買","か")+"う"
BENKYOU_SURU            = r("勉強","べんきょう")+"する"
OKURERU_NAI             = r("遅","おく")+"れない"
WAKARU                  = r("分","わ")+"かる"
NARU                    = "なる"
NARIMASHITA             = "なりました"
KIMERU                  = r("決","き")+"める"
KIMARU                  = r("決","き")+"まる"
KEKKON_SURU             = r("結婚","けっこん")+"する"

# ── sifat va otlar ───────────────────────────────────────────────────
TAKAI, TAKAKUTEMO   = r("高","たか")+"い",    r("高","たか")+"くても"
YASUI               = r("安","やす")+"い"
SAMUI               = r("寒","さむ")+"い"
ATSUI               = r("暑","あつ")+"い"
MUZUKASHII          = r("難","むずか")+"しい"
SHIZUKA, SHIZUKADEMO = r("静","しず")+"か",   r("静","しず")+"かでも"
GENKI               = r("元気","げんき")
BENRI               = r("便利","べんり")
GAKUSEI, GAKUSEIDEMO = r("学生","がくせい"),  r("学生","がくせい")+"でも"
SENSEI              = r("先生","せんせい")
KODOMO              = r("子","こ")+"ども"
AME                 = r("雨","あめ")
HON                 = r("本","ほん")
KANJI               = r("漢字","かんじ")
NIHONGO             = r("日本語","にほんご")
NIHON               = r("日本","にほん")
YASAI               = r("野菜","やさい")
KENKOU              = r("健康","けんこう")
KURUMA              = r("車","くるま")
JIKO                = r("事故","じこ")
DENSHA              = r("電車","でんしゃ")
SHIAI               = r("試合","しあい")
RENSHUU             = r("練習","れんしゅう")
SHINBUN             = r("新聞","しんぶん")
RAIGETSU            = r("来月","らいげつ")
MAINICHI            = r("毎日","まいにち")
DARE                = "だれ"


# ══════════════════════════════════════════════════════════════════════
# PJ-55 — 〜ても
# ══════════════════════════════════════════════════════════════════════
Q_PJ55 = [
    # 1–5 tanish
    q(f"<p>〜ても qaysi shaklga qoʻshiladi?</p>",
      ["て-shakliga", "た-shakliga", "Lugʻat shakliga", "ます-shakliga"],
      "て-shakliga",
      f"<p>て-shakli (PJ-29, PJ-30) + <strong>も</strong>. Xuddi "
      f"PJ-50 dagi た + ら kabi — eski shakl, yangi qoʻshimcha.</p>"),

    q(f"<p>{YOMU} ning ても shakli qaysi?</p>",
      [YONDEMO, f"{YOMU}ても", f"{r('読','よ')}みても", f"{r('読','よ')}んだも"],
      YONDEMO,
      f"<p>て-shakli <strong>{YONDE}</strong> (I guruh, む → んで), "
      f"unga も.</p>"),

    q(f"<p>{TAKAI} ning ても shakli qaysi?</p>",
      [TAKAKUTEMO, f"{TAKAI}ても", f"{r('高','たか')}いでも",
       f"{r('高','たか')}かっても"],
      TAKAKUTEMO,
      f"<p>い-sifatning て-shakli <strong>くて</strong>, demak "
      f"くても.</p>"),

    q(f"<p>{GAKUSEI} ning ても shakli qaysi?</p>",
      [GAKUSEIDEMO, f"{GAKUSEI}てても", f"{GAKUSEI}くても",
       f"{GAKUSEI}だても"],
      GAKUSEIDEMO,
      f"<p>Otning て-shakli <strong>で</strong> (PJ-29), demak "
      f"でも. Bu bir qarashda boshqa qoidadek koʻrinadi, aslida "
      f"oʻsha bitta て-shakli.</p>"),

    q(f"<p>{IKANAI} ning ても shakli qaysi?</p>",
      [IKANAKUTEMO, f"{IKANAI}ても", f"{r('行','い')}かなくでも",
       f"{r('行','い')}かないでも"],
      IKANAKUTEMO,
      f"<p>ない い-sifat, demak uning て-shakli "
      f"<strong>なくて</strong> — va ustiga も.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{AME}が{FUTTEMO}、{IKIMASU}» ni tarjima qiling.</p>",
      ["Yomgʻir yogʻsa ham boraman", "Yomgʻir yogʻsa bormayman",
       "Yomgʻir yogʻdi, shuning uchun boraman",
       "Yomgʻir yoqqanda boraman"],
      "Yomgʻir yogʻsa ham boraman",
      f"<p>ても da natija shartga <strong>qaramaydi</strong>. "
      f"«{AME}が{r('降','ふ')}ったら{r('行','い')}きません» esa "
      f"buning teskarisi.</p>"),

    q(f"<p>«{KONAKUTEMO}いいです» nimani anglatadi?</p>",
      ["Kelish shart emas", "Kelmang", "Albatta keling",
       "Kelsangiz yaxshi boʻlardi"],
      "Kelish shart emas",
      f"<p>Bu <strong>taqiq emas, erkinlik</strong>. Taqiq — "
      f"{r('来','き')}てはいけません (PJ-33).</p>"),

    q(f"<p>PJ-32 dagi «{TABETEMO}いいです» aslida nima?</p>",
      ["«Yesangiz ham — yaxshi», yaʼni ruxsat",
       "«Yeyish kerak», yaʼni majburiyat",
       "«Yemang», yaʼni taqiq",
       "«Yedim», yaʼni oʻtgan zamon"],
      "«Yesangiz ham — yaxshi», yaʼni ruxsat",
      f"<p>Qolip <strong>ても + いい</strong> dan yasalgan. "
      f"Oʻzbekcha «yesang ham boʻladi» ham aynan shu yoʻldan "
      f"boradi — ruxsat emas, eʼtiroz yoʻqligi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>いくら"
      f"{SAGASHITEMO}、___。</strong></p>",
      [f"{r('見','み')}つかりませんでした", f"{r('見','み')}つかりました",
       f"{r('見','み')}つけます", f"{r('見','み')}つかるでしょう"],
      f"{r('見','み')}つかりませんでした",
      f"<p>«いくら〜ても» — «qancha …sa ham». Undan keyin odatda "
      f"<strong>kutilmagan yoki teskari</strong> natija keladi.</p>"),

    q(f"<p>«{DARE}が{KITEMO}» ni tarjima qiling.</p>",
      ["Kim kelsa ham", "Kim keladi?", "Kimdir keldi",
       "Kelgan odam"],
      "Kim kelsa ham",
      f"<p>Soʻroq soʻzi + ても = <strong>«farqi yoʻq»</strong>. "
      f"Oʻzbekchada ham soʻroq soʻzi oldinda, «-sa ham» "
      f"orqada.</p>"),

    q(f"<p>«{SHIZUKADEMO}» — bu qaysi soʻz turidan yasalgan?</p>",
      ["な-sifat", "い-sifat", "Feʼl", "Soʻroq soʻzi"],
      "な-sifat",
      f"<p>な-sifat ham ot kabi <strong>で</strong> oladi, demak "
      f"でも. Bu PJ-26 dan beri davom etayotgan qoida: な-sifat "
      f"ot kabi tuslanadi.</p>"),

    q(f"<p>でも («lekin») qayerdan kelgan?</p>",
      ["で + も — «shunday boʻlsa ham»", "だ + も", "て + も + は",
       "です + も"],
      "で + も — «shunday boʻlsa ham»",
      f"<p>PJ-54 dagi でも aslida shu darsning qolipi. Gap boshiga "
      f"chiqqanda u «lekin» boʻlib qoladi.</p>"),

    # 13–16 farqlash
    q(f"<p>«{FUTTEMO}{IKIMASU}» va «{r('降','ふ')}ったら"
      f"{r('行','い')}きません» — farqi nima?</p>",
      ["Birinchisida natija shartga qaramaydi, ikkinchisida qaraydi",
       "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
       "Birinchisi muloyim, ikkinchisi oddiy",
       "Farqi yoʻq"],
      "Birinchisida natija shartga qaramaydi, ikkinchisida qaraydi",
      f"<p>ても — shartning teskarisi. たら shart qoʻyadi, ても esa "
      f"shartni <strong>bekor qiladi</strong>.</p>"),

    q(f"<p>«{IKANAKUTEMO}いいです» va «{r('行','い')}ってはいけません» "
      f"— farqi nima?</p>",
      ["Birinchisi «shart emas», ikkinchisi «mumkin emas»",
       "Ikkalasi bir xil",
       "Birinchisi muloyimroq, maʼnosi bir xil",
       "Birinchisi oʻtgan zamon"],
      "Birinchisi «shart emas», ikkinchisi «mumkin emas»",
      f"<p>Erkinlik va taqiq — butunlay boshqa narsa. Toʻrttalik "
      f"jadval: ても いい (ruxsat) · なくても いい (shart emas) · "
      f"ては いけません (taqiq) · なければ なりません "
      f"(majburiyat).</p>"),

    q(f"<p>Qaysi soʻz turi ても oldida <strong>で</strong> oladi?</p>",
      ["Ot va な-sifat", "い-sifat", "Feʼl", "Soʻroq soʻzi"],
      "Ot va な-sifat",
      f"<p>{GAKUSEIDEMO} · {SHIZUKADEMO}. い-sifat esa "
      f"<strong>くて</strong>: {TAKAKUTEMO}.</p>"),

    q(f"<p>«{r('高','たか')}くなくても» nimani anglatadi?</p>",
      ["Qimmat boʻlmasa ham", "Qimmat boʻlsa ham",
       "Qimmat emas", "Qimmat boʻlgani uchun"],
      "Qimmat boʻlmasa ham",
      f"<p>い-sifatning inkori くない, uning て-shakli "
      f"<strong>くなくて</strong>, ustiga も.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{GAKUSEI}てても", GAKUSEIDEMO, TAKAKUTEMO, IKANAKUTEMO],
      f"{GAKUSEI}てても",
      f"<p>Otning て-shakli <strong>で</strong>, demak "
      f"{GAKUSEIDEMO}.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{IKANAI} → {r('行','い')}かないても",
       f"{TAKAI} → {TAKAKUTEMO}",
       f"{SHIZUKA} → {SHIZUKADEMO}",
       f"{YOMU} → {YONDEMO}"],
      f"{IKANAI} → {r('行','い')}かないても",
      f"<p>Toʻgʻrisi — <strong>{IKANAKUTEMO}</strong>. ない "
      f"い-sifat, demak なくて.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{RENSHUU}します · {SHIAI}が · ても · "
      f"ない</strong> — «musobaqa boʻlmasa ham mashq qilamiz»</p>",
      [f"{SHIAI}がなくても{RENSHUU}します",
       f"{RENSHUU}しますても{SHIAI}がない",
       f"ても{SHIAI}がない{RENSHUU}します",
       f"{SHIAI}がないても{RENSHUU}します"],
      f"{SHIAI}がなくても{RENSHUU}します",
      f"<p>ない → <strong>なくて</strong> → なくても. Shart "
      f"oldinda, natija keyin.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ムニラ:</strong> {r('明日','あした')}は{AME}です。"
      f"{RENSHUU}はありますか。</p>"
      f"<p><strong>イノム:</strong> ___</p>",
      [f"はい、{AME}が{FUTTEMO}します。", f"はい、{AME}が{r('降','ふ')}ったらします。",
       f"はい、{AME}が{r('降','ふ')}るでもします。", f"はい、{AME}が{FUTTE}します。"],
      f"はい、{AME}が{FUTTEMO}します。",
      f"<p>«Yomgʻir yogʻsa <strong>ham</strong> qilamiz» — natija "
      f"shartga qaramaydi. «たら» boʻlsa maʼno teskari "
      f"boʻlardi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-56 — 〜ために va 〜ように
# ══════════════════════════════════════════════════════════════════════
Q_PJ56 = [
    # 1–5 tanish
    q(f"<p>ために va ように ni ajratadigan savol qaysi?</p>",
      ["Maqsaddagi ishni men qilamanmi va boshqara olamanmi?",
       "Gap oʻtgan zamondami?",
       "Gap muloyim shakldami?",
       "Maqsad yaxshimi yoki yomonmi?"],
      "Maqsaddagi ishni men qilamanmi va boshqara olamanmi?",
      f"<p>Ha — <strong>ために</strong>. Yoʻq — "
      f"<strong>ように</strong>. «Yoʻq» uchta shaklda keladi: "
      f"boshqa odam · qobiliyat · inkor.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KANJI}を"
      f"{WASURENAI}___、{MAINICHI}{r('書','か')}いています。</strong></p>",
      ["ように", "ために", "ので", "から"],
      "ように",
      f"<p><strong>Inkor doim ように</strong> — unutmaslik "
      f"boshqarib boʻladigan narsa emas. Oʻzbekchada ham "
      f"«unutmasligim uchun».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KURUMA}を{KAU}___、"
      f"{HATARAKIMASU}。</strong></p>",
      ["ために", "ように", "ても", "なら"],
      "ために",
      f"<p>Sotib olish — <strong>men qiladigan ish</strong>, demak "
      f"ために. Lugʻat shakli + ために.</p>"),

    q(f"<p>«{KENKOU}» ni ために bilan ulang.</p>",
      [f"{KENKOU}のために", f"{KENKOU}ために", f"{KENKOU}なために",
       f"{KENKOU}だために"],
      f"{KENKOU}のために",
      f"<p>Ot ために oldida <strong>の</strong> oladi.</p>"),

    q(f"<p>Potensial shakl qaysi birini oladi?</p>",
      ["ように", "ために", "Ikkalasini ham", "Hech qaysini"],
      "ように",
      f"<p>Qobiliyat — qaror emas, <strong>natija</strong>. Siz "
      f"«ertaga oʻqiy oladigan boʻlaman» deb qaror qila "
      f"olmaysiz.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{NIHONGO}の{SHINBUN}が{YOMERU}ように、{KANJI}を"
      f"{BENKYOU_SHITEIMASU}» ni tarjima qiling.</p>",
      ["Yaponcha gazeta oʻqiy olishim uchun kanji oʻrganyapman",
       "Yaponcha gazeta oʻqish uchun kanji oʻrganyapman",
       "Yaponcha gazetani oʻqidim va kanji oʻrgandim",
       "Kanji oʻrgansam, gazeta oʻqiyman"],
      "Yaponcha gazeta oʻqiy olishim uchun kanji oʻrganyapman",
      f"<p>Potensial shakl — «oʻqiy ol<strong>ishim</strong>». "
      f"Oʻzbekchadagi egalik qoʻshimchasi ham shuni koʻrsatadi: "
      f"bu men qiladigan ish emas, men bilan boʻladigan "
      f"narsa.</p>"),

    q(f"<p>«{KODOMO}が{WAKARU}ように、ゆっくり{HANASHIMASU}» — nega "
      f"ように?</p>",
      ["Chunki tushunadigan boshqa odam — men emas",
       f"Chunki {KODOMO} ot", "Chunki gap muloyim shaklda",
       f"Chunki {WAKARU} II guruh feʼli"],
      "Chunki tushunadigan boshqa odam — men emas",
      f"<p>Maqsaddagi ishni <strong>boshqa odam</strong> qiladi, "
      f"demak menga bogʻliq emas. Oʻzbekchada ham «tushunsin "
      f"deb» — «tushunish uchun» emas.</p>"),

    q(f"<p>«{JIKO}のために、{DENSHA}が{r('止','と')}まりました» — bu "
      f"maqsadmi?</p>",
      ["Yoʻq, sabab — hodisa maqsad boʻla olmaydi",
       "Ha, maqsad", "Bu shart gap", "Bu qarama-qarshilik"],
      "Yoʻq, sabab — hodisa maqsad boʻla olmaydi",
      f"<p>Ot bilan kelganda ために baʼzan sabab bildiradi. "
      f"Ajratish oson: maqsad <strong>kelajakda</strong>, sabab "
      f"<strong>oʻtmishda</strong>.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{OKURERU_NAI}___"
      f"{r('早','はや')}く{r('出','で')}ます。</strong></p>",
      ["ように", "ために", "なら", "ても"],
      "ように",
      f"<p>Yana inkor — <strong>ように</strong>. «Kechikmasligim "
      f"uchun erta chiqaman.»</p>"),

    q(f"<p>«{MAINICHI}{YASAI}を{r('食','た')}べるようにしています» ni "
      f"tarjima qiling.</p>",
      ["Har kuni sabzavot yeyishga harakat qilaman",
       "Har kuni sabzavot yeyman",
       "Har kuni sabzavot yeydigan boʻldim",
       "Har kuni sabzavot yeyishga qaror qildim"],
      "Har kuni sabzavot yeyishga harakat qilaman",
      f"<p>〜ようにしています — <strong>ongli saʼy-harakat</strong>. "
      f"Oddiy «{r('食','た')}べています» shunchaki odatni "
      f"bildiradi.</p>"),

    q(f"<p>Qaysi gap notoʻgʻri?</p>",
      [f"{WASURENAI}ために{r('書','か')}きます",
       f"{WASURENAI}ように{r('書','か')}きます",
       f"{KAU}ために{HATARAKIMASU}",
       f"{KENKOU}のために{HASHIRIMASU}"],
      f"{WASURENAI}ために{r('書','か')}きます",
      f"<p><strong>ために dan oldin inkor turmaydi.</strong> "
      f"Toʻgʻrisi — {WASURENAI}ように.</p>"),

    q(f"<p>«{NIHON}へ{IKU}ために、お{r('金','かね')}を{TAMETEIMASU}» "
      f"— nega ために?</p>",
      ["Chunki borish — men tanlaydigan va boshqara oladigan ish",
       f"Chunki {NIHON} ot", f"Chunki {TAMERU} II guruh feʼli",
       "Chunki gap davomiy shaklda"],
      "Chunki borish — men tanlaydigan va boshqara oladigan ish",
      f"<p>Bu boshqarib boʻladigan maqsad, shuning uchun "
      f"<strong>ために</strong>. Qobiliyat yoki inkor boʻlganda "
      f"<strong>ように</strong> kerak boʻlardi.</p>"),

    # 13–16 farqlash
    q(f"<p>«{YOMERU}ように» va «{YOMU}ために» — farqi nima?</p>",
      ["Birinchisi qobiliyat, ikkinchisi ish",
       "Birinchisi oʻtgan zamon, ikkinchisi hozirgi",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Farqi yoʻq"],
      "Birinchisi qobiliyat, ikkinchisi ish",
      f"<p>«Oʻqiy olishim uchun» va «oʻqish uchun». Qobiliyat "
      f"boshqarilmaydi, shuning uchun ように.</p>"),

    q(f"<p>Quyidagilardan qaysi biri <strong>ために</strong> "
      f"oladi?</p>",
      [f"{KAU} — men sotib olaman",
       f"{YOMERU} — oʻqiy olaman",
       f"{WASURENAI} — unutmayman",
       f"{KODOMO}が{WAKARU} — bola tushunadi"],
      f"{KAU} — men sotib olaman",
      f"<p>Faqat birinchisi <strong>men boshqara oladigan</strong> "
      f"ish. Qolgan uchtasi — qobiliyat, inkor va boshqa odam — "
      f"hammasi ように.</p>"),

    q(f"<p>Ot ために oldida nima oladi?</p>",
      ["の", "な", "だ", "hech nima"],
      "の",
      f"<p>{KENKOU}<strong>の</strong>ために. «{KENKOU}ために» "
      f"notoʻgʻri.</p>"),

    q(f"<p>ために oldida feʼl qaysi shaklda turadi?</p>",
      ["Lugʻat shaklida", "ます-shaklida", "た-shaklida",
       "て-shaklida"],
      "Lugʻat shaklida",
      f"<p>{BENKYOU_SURU}ために ✓ · «{r('勉強','べんきょう')}します"
      f"ために» ✗.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{YOMERU}ために", f"{YOMERU}ように", f"{KAU}ために",
       f"{KENKOU}のために"],
      f"{YOMERU}ために",
      f"<p>Potensial shakl <strong>ように</strong> oladi — "
      f"qobiliyat boshqarilmaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{KENKOU}のために{MAINICHI}{HASHITTEIMASU}",
       f"{KENKOU}ために{MAINICHI}{HASHITTEIMASU}",
       f"{KENKOU}なために{MAINICHI}{HASHITTEIMASU}",
       f"{KENKOU}だために{MAINICHI}{HASHITTEIMASU}"],
      f"{KENKOU}のために{MAINICHI}{HASHITTEIMASU}",
      f"<p>Ot + <strong>の</strong> + ために.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{r('書','か')}いています · {KANJI}を{WASURENAI} · "
      f"ように · {MAINICHI}</strong></p>",
      [f"{KANJI}を{WASURENAI}ように、{MAINICHI}{r('書','か')}いています",
       f"{MAINICHI}{r('書','か')}いていますように、{KANJI}を{WASURENAI}",
       f"ように{KANJI}を{WASURENAI}、{MAINICHI}{r('書','か')}いています",
       f"{KANJI}を{MAINICHI}{WASURENAI}ように{r('書','か')}いています"],
      f"{KANJI}を{WASURENAI}ように、{MAINICHI}{r('書','か')}いています",
      f"<p>Maqsad oldinda, ish keyin — sabab gapidagi kabi "
      f"tartib.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>せんせい:</strong> なぜ{r('毎朝','まいあさ')}"
      f"{HASHITTEIMASU}か。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"{KENKOU}のために{HASHITTEIMASU}。",
       f"{KENKOU}ために{HASHITTEIMASU}。",
       f"{KENKOU}のように{HASHITTEIMASU}。",
       f"{KENKOU}なために{HASHITTEIMASU}。"],
      f"{KENKOU}のために{HASHITTEIMASU}。",
      f"<p>Ot + <strong>の</strong> + ために, va yugurish — "
      f"boshqarib boʻladigan ish.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-57 — 〜ようになります va 〜ことにします
# ══════════════════════════════════════════════════════════════════════
Q_PJ57 = [
    # 1–5 tanish
    q(f"<p>{SAMUI} ni なる bilan ulang.</p>",
      [f"{r('寒','さむ')}くなります", f"{SAMUI}になります",
       f"{SAMUI}なります", f"{r('寒','さむ')}にになります"],
      f"{r('寒','さむ')}くなります",
      f"<p>い-sifat い → <strong>く</strong> + なる. に olmaydi.</p>"),

    q(f"<p>{SENSEI} ni なる bilan ulang.</p>",
      [f"{SENSEI}になります", f"{SENSEI}くなります", f"{SENSEI}なります",
       f"{SENSEI}のなります"],
      f"{SENSEI}になります",
      f"<p>Ot + <strong>に</strong> + なる.</p>"),

    q(f"<p>{GENKI} ni なる bilan ulang.</p>",
      [f"{GENKI}になります", f"{GENKI}くなります", f"{GENKI}なります",
       f"{GENKI}だになります"],
      f"{GENKI}になります",
      f"<p>な-sifat ham ot kabi <strong>に</strong> oladi — PJ-26 "
      f"dan beri davom etayotgan qoida.</p>"),

    q(f"<p>Feʼl なる ga qanday ulanadi?</p>",
      ["ように orqali", "に orqali", "く orqali", "で orqali"],
      "ように orqali",
      f"<p>{HANASERU}<strong>ように</strong>なりました. «{HANASERU}"
      f"になりました» notoʻgʻri.</p>"),

    q(f"<p>«{HANASERU}ようになりました» ni tarjima qiling.</p>",
      ["Gapiradigan boʻldim", "Gapirdim", "Gapirmoqchiman",
       "Gapirishga qaror qildim"],
      "Gapiradigan boʻldim",
      f"<p>Oʻzbekcha «-adigan boʻldim» — bu qolipning aynan "
      f"nusxasi: sifatdosh + «boʻldim», <strong>ように</strong> + "
      f"<strong>なる</strong>.</p>"),

    # 6–12 qoʻllash
    q(f"<p>«{YASAI}を{r('食','た')}べるようになりました» — bu nimani "
      f"bildiradi?</p>",
      ["Ilgari yemas edim, endi yeyman — odat oʻzgardi",
       "Sabzavot yeyishga qaror qildim",
       "Sabzavot yeya olaman",
       "Sabzavot yedim"],
      "Ilgari yemas edim, endi yeyman — odat oʻzgardi",
      f"<p>ようになる — qobiliyat yoki <strong>odat</strong> "
      f"oʻzgarishi. Qaror emas: qaror ことにする bilan "
      f"aytiladi.</p>"),

    q(f"<p>«{MAINICHI}{HASHIRU}ことにしました» ni tarjima qiling.</p>",
      ["Har kuni yugurishga qaror qildim",
       "Har kuni yuguradigan boʻldim",
       "Har kuni yuguraman",
       "Har kuni yugurish kerak boʻldi"],
      "Har kuni yugurishga qaror qildim",
      f"<p>ことにする — <strong>mening qarorim</strong>. "
      f"ようになる esa oʻz-oʻzidan boʻlgan oʻzgarish.</p>"),

    q(f"<p>«{RAIGETSU}{NIHON}へ{IKU}ことになりました» — kim qaror "
      f"qilgan?</p>",
      ["Boshqa kuch — yoki gapiruvchi kamtarlik qilyapti",
       "Gapiruvchining oʻzi, aniq",
       "Hech kim, bu taxmin",
       "Buni gapdan bilib boʻlmaydi, chunki shakl notoʻgʻri"],
      "Boshqa kuch — yoki gapiruvchi kamtarlik qilyapti",
      f"<p>ことになる — «shunday boʻlib qoldi». Yaponchada "
      f"qarorni oʻzingiz qilgan boʻlsangiz ham koʻpincha shunday "
      f"eʼlon qilinadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IKANAI}___"
      f"しました。</strong> — «bormaslikka qaror qildim»</p>",
      ["ことに", "ように", "ために", "ても"],
      "ことに",
      f"<p>Inkor + <strong>ことにする</strong>. ない-shakli "
      f"toʻgʻridan-toʻgʻri こと oldiga turaveradi.</p>"),

    q(f"<p>Nega yaponlar «{KEKKON_SURU}ことになりました» deydi?</p>",
      ["Chunki «men qaror qildim» oʻzini oldinga surishdek eshitiladi",
       "Chunki toʻyni ota-ona hal qiladi",
       "Chunki ことにする yozma tilda ishlatilmaydi",
       f"Chunki {r('結婚','けっこん')} III guruh feʼli"],
      "Chunki «men qaror qildim» oʻzini oldinga surishdek eshitiladi",
      f"<p>Bu kamtarlik. Oʻzbekcha «toʻy boʻladigan boʻldik» ham "
      f"aynan shunday ishlaydi.</p>"),

    q(f"<p>«{r('決','き')}める» va «{r('決','き')}まる» — farqi nima?</p>",
      [f"{KIMERU} — men hal qilaman; {KIMARU} — hal boʻladi",
       f"{KIMERU} — oʻtgan zamon; {KIMARU} — hozirgi",
       f"{KIMERU} — rasmiy; {KIMARU} — oddiy",
       "Farqi yoʻq"],
      f"{KIMERU} — men hal qilaman; {KIMARU} — hal boʻladi",
      f"<p>Bu ham する / なる juftligi. Yapon tilida bunday "
      f"juftliklar oʻnlab, va ular ayni shu chiziq boʻyicha "
      f"ajraladi.</p>"),

    q(f"<p>«Yemaydigan boʻldim» ning eng tabiiy shakli qaysi?</p>",
      [f"{r('食','た')}べなくなりました", f"{r('食','た')}べないになりました",
       f"{r('食','た')}べなくてなりました", f"{r('食','た')}べないことになりました"],
      f"{r('食','た')}べなくなりました",
      f"<p>Inkorda ように koʻpincha tushib qoladi: ない → "
      f"<strong>なく</strong> + なる — ない い-sifat boʻlgani "
      f"uchun.</p>"),

    # 13–16 farqlash
    q(f"<p>«{IKU}ことにしました» va «{IKU}ことになりました» — farqi?</p>",
      ["Birinchisida men qaror qildim, ikkinchisida shunday boʻlib qoldi",
       "Birinchisi kelasi zamon, ikkinchisi oʻtgan",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Farqi yoʻq"],
      "Birinchisida men qaror qildim, ikkinchisida shunday boʻlib qoldi",
      f"<p>する = men qildim; なる = shunday boʻldi. Bu butun "
      f"darsning oʻqi.</p>"),

    q(f"<p>«{HANASERU}ようになりました» va «{HANASU}ことにしました» — "
      f"farqi?</p>",
      ["Birinchisi qobiliyat oʻzgardi, ikkinchisi qaror qilindi",
       "Birinchisi qaror, ikkinchisi qobiliyat",
       "Ikkalasi ham qaror", "Ikkalasi ham qobiliyat"],
      "Birinchisi qobiliyat oʻzgardi, ikkinchisi qaror qilindi",
      f"<p>ようになる — oʻz-oʻzidan kelgan oʻzgarish. "
      f"ことにする — ongli tanlov.</p>"),

    q(f"<p>«ことにしました» va «ことにしています» — farqi?</p>",
      ["Birinchisi qaror qilingan paytga, ikkinchisi qaror hali kuchdaligiga ishora qiladi",
       "Birinchisi rasmiy, ikkinchisi oddiy",
       "Birinchisi inkor, ikkinchisi tasdiq",
       "Farqi yoʻq"],
      "Birinchisi qaror qilingan paytga, ikkinchisi qaror hali kuchdaligiga ishora qiladi",
      f"<p>PJ-31 dagi ています ning oʻsha ishi — davom etayotgan "
      f"holat.</p>"),

    q(f"<p>«{r('少','すこ')}しずつ{MUZUKASHII}くなりました» ni tarjima "
      f"qiling.</p>",
      ["Asta-sekin qiyinlashdi", "Asta-sekin qiyin qildim",
       "Qiyinlashtirishga qaror qildim", "Qiyin boʻlsa ham qildim"],
      "Asta-sekin qiyinlashdi",
      f"<p>い-sifat + <strong>く</strong> + なる — hech kim "
      f"qilmadi, oʻzi shunday boʻldi.</p>"),

    # 17–18 xato topish
    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{SAMUI}になります", f"{r('寒','さむ')}くなります",
       f"{SENSEI}になります", f"{HANASERU}ようになります"],
      f"{SAMUI}になります",
      f"<p>い-sifat <strong>く</strong> ga tushadi: "
      f"{r('寒','さむ')}くなります. に faqat ot va な-sifat "
      f"uchun.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{IKU}ことにしました", f"{IKIMASU}ことにしました",
       f"{ITTE}ことにしました", f"{IKU}のことにしました"],
      f"{IKU}ことにしました",
      f"<p>こと — <strong>ot</strong>, demak oldida oddiy shakl "
      f"turadi (PJ-48). ます hech qachon emas.</p>"),

    # 19–20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>なりました · {NIHONGO}が · ように · "
      f"{HANASERU}</strong></p>",
      [f"{NIHONGO}が{HANASERU}ようになりました",
       f"{HANASERU}ように{NIHONGO}がなりました",
       f"ように{NIHONGO}が{HANASERU}なりました",
       f"{NIHONGO}がように{HANASERU}なりました"],
      f"{NIHONGO}が{HANASERU}ようになりました",
      f"<p>Potensial shaklda toʻldiruvchi <strong>が</strong> "
      f"oladi (PJ-42), keyin ように, oxirida なりました.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p>"
      f"<p><strong>ラノ:</strong> {RAIGETSU}から{r('新','あたら')}しい"
      f"{r('学校','がっこう')}ですか。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"はい、{r('転校','てんこう')}することになりました。",
       f"はい、{r('転校','てんこう')}するようになりました。",
       f"はい、{r('転校','てんこう')}しますことになりました。",
       f"はい、{r('転校','てんこう')}することによりました。"],
      f"はい、{r('転校','てんこう')}することになりました。",
      f"<p>Maktab oʻzgarishi — oila hal qilgan, va yaponchada "
      f"bunday xabar doim <strong>ことになりました</strong> bilan "
      f"beriladi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-55 Mashq: 〜ても",
        "tutorial":    "PJ-55:",
        "description": "て-shakli + も. Ot va な-sifat で oladi, "
                       "い-sifat くて, inkor なくて. Va 〜てもいいです "
                       "aslida shu qolip.",
        "questions":   Q_PJ55,
        **DEFAULTS,
    },
    {
        "title":       "PJ-56 Mashq: Maqsad — 〜ために va 〜ように",
        "tutorial":    "PJ-56:",
        "description": "Bitta savol: irodam yetadimi? Inkor va potensial "
                       "shakl doim ように, ot ために oldida の oladi.",
        "questions":   Q_PJ56,
        **DEFAULTS,
    },
    {
        "title":       "PJ-57 Mashq: 〜ようになります va 〜ことにします",
        "tutorial":    "PJ-57:",
        "description": "なる ga ulanish: い-sifat く, ot に, feʼl ように. "
                       "Va する / なる — qaror va oʻzgarish.",
        "questions":   Q_PJ57,
        **DEFAULTS,
    },
]
