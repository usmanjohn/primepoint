# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-43 … PJ-45.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

⚠️ PJ-43 — FAKTLAR darsi, PJ-12 dagi sonlar kabi. Har bir sanoq soʻzi
oʻqilishi alohida `verify_pj43_counters.py` bilan qoidalardan qayta
hisoblanadi: 1/6/8/10 sokuon, 3 va 何 jaranglashish.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_43_45.py --master=prime \\
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

# ── PJ-43 sanoq soʻzlari ─────────────────────────────────────────────
IPPON, NIHON_C, SANBON = r("一本","いっぽん"), r("二本","にほん"), r("三本","さんぼん")
ROPPON, HAPPON, JUPPON = r("六本","ろっぽん"), r("八本","はっぽん"), r("十本","じゅっぽん")
NANBON = r("何本","なんぼん")
IPPIKI, NIHIKI, SANBIKI = r("一匹","いっぴき"), r("二匹","にひき"), r("三匹","さんびき")
ROPPIKI, NANBIKI = r("六匹","ろっぴき"), r("何匹","なんびき")
IKKO, NIKO, SANKO, ROKKO = r("一個","いっこ"), r("二個","にこ"), r("三個","さんこ"), r("六個","ろっこ")
ICHIMAI, SANMAI, ROKUMAI = r("一枚","いちまい"), r("三枚","さんまい"), r("六枚","ろくまい")
HITORI, FUTARI, SANNIN, YONIN = r("一人","ひとり"), r("二人","ふたり"), r("三人","さんにん"), r("四人","よにん")
ICHIDAI, SANDAI = r("一台","いちだい"), r("三台","さんだい")
NANNIN, NANMAI = r("何人","なんにん"), r("何枚","なんまい")

# ── otlar ────────────────────────────────────────────────────────────
NEKO, INU, ENPITSU = r("猫","ねこ"), r("犬","いぬ"), r("鉛筆","えんぴつ")
KAMI, TAMAGO, KURUMA = r("紙","かみ"), r("卵","たまご"), r("車","くるま")
GAKUSEI, HON_N, MISE = r("学生","がくせい"), r("本","ほん"), r("店","みせ")
DENSHA, YAMA, NATSU = r("電車","でんしゃ"), r("山","やま"), r("夏","なつ")
JITENSHA, KY = r("自転車","じてんしゃ"), r("教室","きょうしつ")
TAKAI, YASUI, HAYAI = r("高","たか")+"い", r("安","やす")+"い", r("速","はや")+"い"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-43 — sanoq soʻzlari
# ══════════════════════════════════════════════════════════════════════
Q_PJ43 = [
    q(f"<p>{NEKO} qaysi sanoq soʻzi bilan sanaladi?</p>",
      [r("匹","ひき"), r("本","ほん"), r("枚","まい"), r("台","だい")],
      r("匹","ひき"),
      f"<p><strong>{r('匹','ひき')}</strong> — kichik hayvonlar uchun: "
      f"{NEKO}, {INU}, {r('魚','さかな')}.</p>"),

    q(f"<p>{ENPITSU} qaysi sanoq soʻzi bilan sanaladi?</p>",
      [r("本","ほん"), r("枚","まい"), r("個","こ"), r("匹","ひき")],
      r("本","ほん"),
      f"<p><strong>{r('本','ほん')}</strong> — <em>uzun</em> narsalar uchun. "
      f"Diqqat: bu «kitob» degani emas; kitob {r('冊','さつ')} bilan "
      f"sanaladi.</p>"),

    q(f"<p>{KAMI} qaysi sanoq soʻzi bilan sanaladi?</p>",
      [r("枚","まい"), r("本","ほん"), r("台","だい"), r("個","こ")],
      r("枚","まい"),
      f"<p><strong>{r('枚','まい')}</strong> — yassi narsalar: qogʻoz, "
      f"koʻylak, rasm.</p>"),

    q(f"<p>«Uchta qalam» — <strong>{ENPITSU}三本</strong> — qanday "
      f"oʻqiladi?</p>",
      ["さんぼん", "さんほん", "さんぽん", "さんびき"], "さんぼん",
      f"<p><strong>{SANBON}</strong> — 3 は qatorini <strong>ば</strong> ga "
      f"aylantiradi. «さんほん» ni ogʻizda chiqarish qiyin, til oʻz-oʻzidan "
      f"«ぼ» ga oʻtadi.</p>"),

    q(f"<p>{IPPIKI} nega «いちひき» emas?</p>",
      ["1, 6, 8, 10 kichik っ qoʻshadi va は qatorini ぱ ga oʻtkazadi",
       "匹 doim jaranglashadi",
       "1 har doim tartibsiz",
       "猫 tirik boʻlgani uchun"],
      "1, 6, 8, 10 kichik っ qoʻshadi va は qatorini ぱ ga oʻtkazadi",
      f"<p>Shu bitta qoida {IPPON}, {IPPIKI}, {IKKO}, {ROPPON}, {ROKKO} — "
      f"hammasini tushuntiradi.</p>"),

    q(f"<p>«Oltita tuxum» — <strong>{TAMAGO}六個</strong> — qanday "
      f"oʻqiladi?</p>",
      ["ろっこ", "ろくこ", "ろっご", "ろくご"], "ろっこ",
      f"<p><strong>{ROKKO}</strong> — か qatorida ham 1, 6, 8, 10 sokuon "
      f"oladi, lekin jaranglashish <em>yoʻq</em>: «ろっご» emas.</p>"),

    q(f"<p>Qaysi sanoq soʻzi umuman oʻzgarmaydi?</p>",
      [r("枚","まい"), r("本","ほん"), r("匹","ひき"), r("個","こ")],
      r("枚","まい"),
      f"<p><strong>{r('枚','まい')}</strong> va {r('台','だい')} ま va だ "
      f"qatorida — ular oʻzgarmaydi. Faqat は va か qatoridagilari "
      f"oʻzgaradi.</p>"),

    q(f"<p>«Toʻrt kishi» — <strong>四人</strong> — qanday oʻqiladi?</p>",
      ["よにん", "よんにん", "しにん", "よっつにん"], "よにん",
      f"<p><strong>{YONIN}</strong> — よん emas, <strong>よ</strong>. Bu "
      f"{r('人','にん')} ning uchinchi istisnosi, {HITORI} va {FUTARI} dan "
      f"keyin.</p>"),

    q(f"<p><strong>一人</strong> va <strong>二人</strong> qanday "
      f"oʻqiladi?</p>",
      ["ひとり・ふたり", "いちにん・ににん", "ひとつ・ふたつ", "ひとり・ににん"],
      "ひとり・ふたり",
      f"<p>Ikkalasi ham tartibsiz va ikkalasi ham sizga PJ-22 dan tanish — "
      f"oʻqish matnlarida koʻp marta uchragan. 3 dan boshlab hammasi oddiy "
      f"holga qaytadi: {SANNIN}.</p>"),

    q(f"<p>{NANBON} nega «なんほん» emas?</p>",
      ["3 va 何 は qatorini jaranglashtiradi",
       "何 doim sokuon oladi",
       "何 tartibsiz soʻz",
       "Savolda har doim jaranglashish boʻladi"],
      "3 va 何 は qatorini jaranglashtiradi",
      f"<p>Bir qoida ikki joyda: {SANBON} va {NANBON}, {SANBIKI} va "
      f"{NANBIKI}.</p>"),

    q(f"<p>«Uchta mushuk bor» ni tanlang.</p>",
      [f"{NEKO}が{SANBIKI}います", f"{NEKO}が{SANBON}います",
       f"{NEKO}が{SANKO}います", f"{NEKO}が{SANNIN}います"],
      f"{NEKO}が{SANBIKI}います",
      f"<p>Tirik jonzot <strong>{r('匹','ひき')}</strong> bilan sanaladi, "
      f"va 3 uni <strong>びき</strong> ga aylantiradi.</p>"),

    q(f"<p>Sanoq soʻzi gapda qayerda turadi?</p>",
      ["Otdan keyin, feʼldan oldin — va qoʻshimcha olmaydi",
       "Otdan oldin", "Gap oxirida", "Feʼldan keyin"],
      "Otdan keyin, feʼldan oldin — va qoʻshimcha olmaydi",
      f"<p>りんごを{SANKO}{r('買','か')}いました — «を{SANKO}を» emas. "
      f"Sanoq soʻziga hech qanday qoʻshimcha qoʻshilmaydi.</p>"),

    q("<p>«ふたつ» qaysi tizimga tegishli?</p>",
      ["Yaponcha sonlar — 〜つ sanogʻi", "Xitoycha sonlar",
       "Sanoq soʻzi", "Soʻroq soʻzi"],
      "Yaponcha sonlar — 〜つ sanogʻi",
      f"<p>ひとつ, ふたつ, みっつ… — yaponcha sonlar, PJ-12 dagi "
      f"{r('一','いち')}, {r('二','に')} esa xitoycha. Shuning uchun ular "
      f"butunlay boshqacha eshitiladi va 10 da tugaydi.</p>"),

    q("<p>Sanoq soʻzini bilmasangiz nima qilasiz?</p>",
      ["〜つ ni ishlataman", "本 ni ishlataman",
       "Sanoq soʻzsiz aytaman", "Sonni aytmayman"],
      "〜つ ni ishlataman",
      f"<p>ひとつ, ふたつ, みっつ… 10 gacha ishlaydi va deyarli hech qachon "
      f"xato boʻlmaydi. Doʻkonda «ふたつ ください» kifoya.</p>"),

    q(f"<p>«Nechta mushuk?» ni tanlang.</p>",
      [f"{NEKO}が{NANBIKI}いますか", f"{NEKO}が{NANBON}いますか",
       f"{NEKO}が{NANNIN}いますか", f"{NEKO}が{NANMAI}いますか"],
      f"{NEKO}が{NANBIKI}いますか",
      f"<p><strong>{NANBIKI}</strong> — {r('何','なん')} ham は qatorini "
      f"jaranglashtiradi, xuddi 3 kabi.</p>"),

    q(f"<p>«Sakkiz nafar talaba» — <strong>{GAKUSEI}八人</strong> — qanday "
      f"oʻqiladi?</p>",
      ["はちにん", "はっにん", "はっぽん", "やっつにん"], "はちにん",
      f"<p>{r('人','にん')} な qatorida — u <strong>oʻzgarmaydi</strong>. "
      f"8 sokuon faqat は va か qatorida oladi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{NEKO}が{SANBIKI}います", f"{KAMI}を{SANMAI}",
       f"{ENPITSU}を{SANKO}", f"{KURUMA}が{SANDAI}"],
      f"{ENPITSU}を{SANKO}",
      f"<p>Qalam — <em>uzun</em> narsa, demak <strong>{SANBON}</strong>. "
      f"{r('個','こ')} kichik, dumaloq buyumlar uchun.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"1 + {r('本','ほん')} → {IPPON}", f"3 + {r('匹','ひき')} → {SANBIKI}",
       f"6 + {r('枚','まい')} → {r('六枚','ろくまい')}",
       f"1 + {r('個','こ')} → {r('一個','いちこ')}"],
      f"1 + {r('個','こ')} → {r('一個','いちこ')}",
      f"<p>か qatorida ham 1 sokuon oladi: <strong>{IKKO}</strong>. "
      f"{r('枚','まい')} esa haqiqatan ham oʻzgarmaydi.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {r('買','か')}いました · "
      f"を · りんご · {SANKO}</p>",
      [f"りんごを{SANKO}{r('買','か')}いました", f"りんご{SANKO}を{r('買','か')}いました",
       f"{SANKO}りんごを{r('買','か')}いました", f"りんごを{r('買','か')}いました{SANKO}"],
      f"りんごを{SANKO}{r('買','か')}いました",
      f"<p>Ot va uning を qoʻshimchasi, keyin sanoq soʻzi, keyin feʼl. "
      f"Sanoq soʻzi <strong>qoʻshimcha olmaydi</strong>.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"{r('子猫','こねこ')}は___いますか。</p>"
      f"<p><strong>ムニラ:</strong> {SANBIKI}です。</p>",
      [NANBIKI, NANBON, NANNIN, NANMAI], NANBIKI,
      f"<p>Javob {r('匹','ひき')} bilan berilgan, demak savol ham "
      f"<strong>{NANBIKI}</strong> boʻlishi kerak.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-44 — taqqoslash
# ══════════════════════════════════════════════════════════════════════
Q_PJ44 = [
    q("<p>Taqqoslashda yaponcha sifat oʻzgaradimi?</p>",
      ["Yoʻq — ishni qoʻshimchalar bajaradi", "Ha, «-roq» qoʻshiladi",
       "Ha, oxirgi い tushadi", "Faqat な-sifatlar oʻzgaradi"],
      "Yoʻq — ishni qoʻshimchalar bajaradi",
      f"<p>{TAKAI} taqqoslashda ham {TAKAI} boʻlib qoladi. Oʻzbekchada "
      f"«katta<strong>roq</strong>» sifatning oʻziga yopishadi; yaponchada "
      f"maʼnoni <strong>gapning tuzilishi</strong> beradi.</p>"),

    q("<p>〜より qaysi tomonni belgilaydi?</p>",
      ["Past tomonni", "Yuqori tomonni", "Ikkalasini", "Hech qaysini"],
      "Past tomonni",
      f"<p>より dan <em>oldingi</em> narsa kamroq. Shuning uchun "
      f"«{DENSHA}はバスより{HAYAI}です» — poyezd tezroq.</p>"),

    q(f"<p>«Poyezd avtobusdan tez» ni tanlang.</p>",
      [f"{DENSHA}はバスより{HAYAI}です", f"バスは{DENSHA}より{HAYAI}です",
       f"{DENSHA}よりバスは{HAYAI}です", f"{DENSHA}はバスが{HAYAI}です"],
      f"{DENSHA}はバスより{HAYAI}です",
      f"<p>より <strong>past</strong> tomonda — yaʼni avtobus sekinroq. "
      f"Ikkinchi variant teskari maʼno beradi.</p>"),

    q("<p>〜のほうが qaysi tomonni belgilaydi?</p>",
      ["Yuqori tomonni", "Past tomonni", "Ikkalasini", "Hech qaysini"],
      "Yuqori tomonni",
      f"<p>ほう — «tomon» degan ot. のほうが koʻproq boʻlgan tomonni "
      f"koʻrsatadi va koʻpincha より bilan bir gapda turadi.</p>"),

    q(f"<p>Ikki narsadan qaysi biri deb qanday soʻraysiz?</p>",
      ["A と B と、どちらが…ですか", "A と B と、<ruby>何<rt>なに</rt></ruby>が…ですか",
       "A と B と、どこが…ですか", "A と B と、いちばん…ですか"],
      "A と B と、どちらが…ですか",
      f"<p><strong>どちら</strong> — ikkitasidan bittasi. "
      f"{r('何','なに')} esa uchta va undan koʻp narsa uchun.</p>"),

    q(f"<p>«{NEKO}と{INU}と、どちらが{r('好','す')}きですか» ga javobni tanlang.</p>",
      [f"{NEKO}のほうが{r('好','す')}きです", f"{NEKO}より{r('好','す')}きです",
       f"{NEKO}がいちばん{r('好','す')}きです", f"{NEKO}は{r('好','す')}きです"],
      f"{NEKO}のほうが{r('好','す')}きです",
      f"<p>どちら savoliga javob <strong>のほうが</strong> bilan beriladi. "
      f"いちばん esa uchta va undan koʻp narsa uchun.</p>"),

    q("<p>Uch va undan koʻp narsadan eng ustunini qanday aytasiz?</p>",
      ["いちばん + sifat", "より + sifat", "のほうが + sifat", "どちら + sifat"],
      "いちばん + sifat",
      f"<p>いちばn aslida «birinchi oʻrin» degani, shuning uchun u sifatga "
      f"yopishmaydi — oldida alohida turadi.</p>"),

    q(f"<p>«Sinfda eng tez» ni tanlang.</p>",
      [f"クラスの{r('中','なか')}でいちばん{HAYAI}です",
       f"クラスの{r('中','なか')}でいちばん{HAYAI}いです",
       f"クラスより いちばん{HAYAI}です",
       f"クラスの{r('中','なか')}がいちばん{HAYAI}です"],
      f"クラスの{r('中','なか')}でいちばん{HAYAI}です",
      f"<p>«…lar ichida» — <strong>の{r('中','なか')}で</strong>, va sifat "
      f"oʻzgarmaydi: «{HAYAI}いです» emas.</p>"),

    q(f"<p>«{NATSU}がいちばん{r('好','す')}きです» — nega bu yerda は emas, が "
      f"ishlatilgan?</p>",
      ["Chunki taqqoslash va yoqtirish gaplarida narsa ega boʻlib turadi",
       "Chunki 夏 qisqa soʻz",
       "Chunki は faqat gap boshida keladi",
       "Chunki いちばん が talab qiladi"],
      "Chunki taqqoslash va yoqtirish gaplarida narsa ega boʻlib turadi",
      f"<p>Bu PJ-26 dan beri tanish qoida: {r('好','す')}き, ほしい, "
      f"できる va endi taqqoslash — hammasi <strong>が</strong> oladi.</p>"),

    q(f"<p>Sifat feʼlni taʼriflaganda nima boʻladi?</p>",
      ["い → く", "い → な", "い → だ", "Hech narsa"],
      "い → く",
      f"<p>{HAYAI}{DENSHA} («tez poyezd») — sifat otni taʼriflaydi, "
      f"oʻzgarmaydi. {r('速','はや')}く{r('泳','およ')}ぐ («tez suzmoq») — "
      f"feʼlni taʼriflaydi, <strong>く</strong> oladi.</p>"),

    q(f"<p>な-sifat feʼlni taʼriflaganda nima oladi?</p>",
      ["に", "く", "な", "の"], "に",
      f"<p>{r('静','しず')}か<strong>に</strong>{r('話','はな')}す — "
      f"«jimgina gapirmoq». い-sifat く oladi, な-sifat esa に.</p>"),

    q(f"<p>«{YAMA}はこの{YAMA}より{TAKAI}です» — qaysi biri baland?</p>",
      ["Birinchi togʻ", "Bu togʻ", "Ikkalasi bir xil", "Aniqlab boʻlmaydi"],
      "Birinchi togʻ",
      f"<p>より dan <em>keyingi</em> narsa pastroq. Bu qolipdagi eng koʻp "
      f"uchraydigan xato — より ni teskari tushunish.</p>"),

    q(f"<p>«どちら» kundalik nutqda qanday qisqaradi?</p>",
      ["どっち", "どこ", "どれ", "どう"], "どっち",
      f"<p><strong>どっち</strong> — sokuon bilan. Yozma tilda va rasmiy "
      f"suhbatda esa どちら qoladi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{DENSHA}のほうがバスより{HAYAI}です",
       f"{DENSHA}のほうがバスよりも{HAYAI}いです",
       f"{DENSHA}のほうはバスより{HAYAI}です",
       f"{DENSHA}のほうがバスが{HAYAI}です"],
      f"{DENSHA}のほうがバスより{HAYAI}です",
      f"<p>のほう<strong>が</strong> (yuqori tomon) va <strong>より</strong> "
      f"(past tomon) bir gapda tura oladi. Sifat esa oʻzgarmaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{MISE}の{r('中','なか')}でこれがいちばん{YASUI}です",
       f"{MISE}の{r('中','なか')}でこれがいちばん{YASUI}いです",
       f"{MISE}よりこれがいちばん{YASUI}です",
       f"{MISE}の{r('中','なか')}でこれはいちばん{YASUI}が"],
      f"{MISE}の{r('中','なか')}でこれがいちばん{YASUI}です",
      f"<p>の{r('中','なか')}で + いちばん + sifat + です. Sifat "
      f"oʻzgarmaydi va narsa <strong>が</strong> oladi.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{JITENSHA}はバスより{YASUI}です",
       f"{NEKO}と{INU}と、{r('何','なに')}が{r('好','す')}きですか",
       f"{NATSU}がいちばん{r('好','す')}きです",
       f"これのほうが{TAKAI}です"],
      f"{NEKO}と{INU}と、{r('何','なに')}が{r('好','す')}きですか",
      f"<p>Ikki narsadan tanlashda <strong>どちら</strong> ishlatiladi. "
      f"{r('何','なに')} uchta va undan koʻp narsa uchun.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TAKAI} → {r('高','たか')}く", f"{HAYAI} → {r('速','はや')}く",
       f"{r('静','しず')}か → {r('静','しず')}かく", f"{YASUI} → {r('安','やす')}く"],
      f"{r('静','しず')}か → {r('静','しず')}かく",
      f"<p>な-sifat <strong>に</strong> oladi, く emas: "
      f"<strong>{r('静','しず')}かに</strong>.</p>"),

    q(f"<p>«いちばん» ni sifatga qoʻshib yozish mumkinmi?</p>",
      ["Yoʻq — u alohida turadi", "Ha, sifatning oxiriga",
       "Ha, sifatning ichiga", "Faqat な-sifat bilan"],
      "Yoʻq — u alohida turadi",
      f"<p>いちばん aslida <strong>{r('一番','いちばん')}</strong> — "
      f"«birinchi oʻrin» degan ot. Shuning uchun u sifat oldida alohida "
      f"soʻz boʻlib turadi.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {HAYAI}です · より · "
      f"バス · {DENSHA}は</p>",
      [f"{DENSHA}はバスより{HAYAI}です", f"バスより{DENSHA}は{HAYAI}です",
       f"{DENSHA}はより バス{HAYAI}です", f"より バス{DENSHA}は{HAYAI}です"],
      f"{DENSHA}はバスより{HAYAI}です",
      f"<p>Mavzu (は) eng oldinda, keyin taqqoslanadigan narsa va uning "
      f"より qoʻshimchasi, sifat esa oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"{NEKO}と{INU}と、どちらが{r('好','す')}きですか。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"{NEKO}のほうが{r('好','す')}きです", f"{NEKO}がいちばん{r('好','す')}きです",
       f"{NEKO}より{r('好','す')}きです", f"どちらが{r('好','す')}きです"],
      f"{NEKO}のほうが{r('好','す')}きです",
      f"<p>どちら savoliga <strong>のほうが</strong> bilan javob beriladi. "
      f"いちばん uchta va undan koʻp narsa uchun.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-45 — 普通体
# ══════════════════════════════════════════════════════════════════════
IKU_D, IKANAI, ITTA, IKANAKATTA = (r("行","い")+"く", r("行","い")+"かない",
                                   r("行","い")+"った", r("行","い")+"かなかった")
TABERU_D, TABENAI, TABETA, TABENAKATTA = (r("食","た")+"べる", r("食","た")+"べない",
                                          r("食","た")+"べた", r("食","た")+"べなかった")
YASUI_D, YASUKUNAI, YASUKATTA = r("安","やす")+"い", r("安","やす")+"くない", r("安","やす")+"かった"
GAKUSEI_D = r("学生","がくせい")
SHIZUKA = r("静","しず")+"か"

Q_PJ45 = [
    q("<p><ruby>普通体<rt>ふつうたい</rt></ruby> qayerda ishlatiladi?</p>",
      ["Oila, yaqin doʻst, kundalik, kitob", "Ustoz bilan suhbatda",
       "Ishda va xizmatda", "Begona odam bilan"],
      "Oila, yaqin doʻst, kundalik, kitob",
      f"<p>Yapon kitobi, gazetasi va romani shu uslubda yoziladi. "
      f"Ustoz va begona bilan esa <ruby>丁寧体<rt>ていねいたい</rt></ruby>.</p>"),

    q(f"<p>{r('行','い')}きます ning oddiy shakli qaysi?</p>",
      [IKU_D, IKANAI, ITTA, f"{r('行','い')}きだ"], IKU_D,
      f"<p><strong>{IKU_D}</strong> — bu lugʻat shaklining oʻzi, PJ-28 dan "
      f"tanish.</p>"),

    q(f"<p>{r('行','い')}きません ning oddiy shakli qaysi?</p>",
      [IKANAI, IKU_D, IKANAKATTA, f"{r('行','い')}かないだ"], IKANAI,
      f"<p><strong>{IKANAI}</strong> — ない-shakli, PJ-34 dan tanish.</p>"),

    q(f"<p>{r('行','い')}きました ning oddiy shakli qaysi?</p>",
      [ITTA, IKU_D, IKANAKATTA, f"{r('行','い')}ったです"], ITTA,
      f"<p><strong>{ITTA}</strong> — た-shakli, PJ-35 dan tanish.</p>"),

    q(f"<p>{r('行','い')}きませんでした ning oddiy shakli qaysi?</p>",
      [IKANAKATTA, f"{IKANAI}だった", f"{ITTA}ない", f"{IKANAI}でした"],
      IKANAKATTA,
      f"<p><strong>{IKANAKATTA}</strong> — feʼldagi <em>yagona</em> yangi "
      f"shakl. U ない ning oʻtgan zamoni: ない い-sifat, demak い → かった.</p>"),

    q(f"<p>{YASUI_D}です ning oddiy shakli qaysi?</p>",
      [YASUI_D, f"{YASUI_D}だ", f"{r('安','やす')}だ", YASUKATTA],
      YASUI_D,
      f"<p>い-sifat eng oson: <strong>です ni olib tashlang</strong>. "
      f"だ qoʻshilmaydi.</p>"),

    q(f"<p>{GAKUSEI_D}です ning oddiy shakli qaysi?</p>",
      [f"{GAKUSEI_D}だ", GAKUSEI_D, f"{GAKUSEI_D}い", f"{GAKUSEI_D}な"],
      f"{GAKUSEI_D}だ",
      f"<p>Ot bilan <strong>だ</strong> paydo boʻladi — です ning oddiy "
      f"shakli.</p>"),

    q(f"<p>{GAKUSEI_D}ではありません ning oddiy shakli qaysi?</p>",
      [f"{GAKUSEI_D}じゃない", f"{GAKUSEI_D}だない",
       f"{GAKUSEI_D}くない", f"{GAKUSEI_D}だじゃない"],
      f"{GAKUSEI_D}じゃない",
      f"<p><strong>じゃない</strong> — じゃ bu では ning qisqargani. "
      f"Rasmiyroq shakli ではない ham toʻgʻri.</p>"),

    q(f"<p>{GAKUSEI_D}でした ning oddiy shakli qaysi?</p>",
      [f"{GAKUSEI_D}だった", f"{GAKUSEI_D}でた",
       f"{GAKUSEI_D}かった", f"{GAKUSEI_D}だでした"],
      f"{GAKUSEI_D}だった",
      f"<p><strong>だった</strong> — でした ning oddiy shakli. な-sifat ham "
      f"shu yoʻldan boradi: {SHIZUKA}だった.</p>"),

    q(f"<p>Qaysi soʻz turiga だ qoʻshilMAYDI?</p>",
      ["い-sifat", "Ot", "な-sifat", "Hammasiga qoʻshiladi"],
      "い-sifat",
      f"<p>«{YASUI_D}だ» notoʻgʻri. だ faqat <strong>ot va な-sifat</strong> "
      f"bilan keladi, chunki い-sifat oʻzi kesim boʻla oladi.</p>"),

    q(f"<p>{SHIZUKA}です ning oddiy shakli qaysi?</p>",
      [f"{SHIZUKA}だ", SHIZUKA, f"{SHIZUKA}い", f"{SHIZUKA}な"],
      f"{SHIZUKA}だ",
      f"<p>な-sifat PJ-26 dan beri <strong>ot kabi</strong> tuslanadi, "
      f"demak u ham だ oladi.</p>"),

    q("<p>Ogʻzaki nutqda だ bilan nima boʻladi?</p>",
      ["Koʻpincha umuman aytilmaydi", "です ga aylanadi",
       "Har doim aytiladi", "だった ga aylanadi"],
      "Koʻpincha umuman aytilmaydi",
      f"<p>«{GAKUSEI_D}？» — だ tushadi va ohang savolni koʻrsatadi. "
      f"Feʼl bilan bunday boʻlmaydi: {IKU_D} hech qachon qisqarmaydi.</p>"),

    q(f"<p>{YASUI_D}くないです ning oddiy shakli qaysi?</p>",
      [YASUKUNAI, f"{YASUKUNAI}だ", f"{r('安','やす')}じゃない", YASUKATTA],
      YASUKUNAI,
      f"<p>Yana <strong>です ni olib tashlang</strong>. い-sifatga hech "
      f"qachon だ qoʻshilmaydi.</p>"),

    q("<p>Nega oddiy shaklni oʻrganish kerak?</p>",
      ["Chunki keyingi grammatikaning yarmi oldida uni talab qiladi",
       "Chunki u muloyimroq",
       "Chunki u qisqaroq",
       "Chunki imtihonda faqat u soʻraladi"],
      "Chunki keyingi grammatikaning yarmi oldida uni talab qiladi",
      f"<p>〜と{r('思','おも')}います, 〜とき, 〜たら, 〜ので — hammasi "
      f"oldida oddiy shaklni talab qiladi. Yaʼni u gapirish uchun emas, "
      f"<strong>gap qurish</strong> uchun kerak.</p>"),

    q(f"<p>«{r('明日','あした')}{r('雨','あめ')}が{r('降','ふ')}ると"
      f"{r('思','おも')}います» — nega ichkarida {r('降','ふ')}る turibdi?</p>",
      ["Chunki gap ichida doim oddiy shakl turadi",
       "Chunki 降る — I guruh feʼli",
       "Chunki gap kelasi zamonda",
       "Chunki 思う oddiy shakl talab qilmaydi"],
      "Chunki gap ichida doim oddiy shakl turadi",
      f"<p>Gapning <strong>tashqi kiyimi</strong> muloyim "
      f"({r('思','おも')}います), ichkarisi esa oddiy. Bu — Blok D ning "
      f"asosiy qolipi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{r('今日','きょう')}は{SHIZUKA}だった",
       f"{r('今日','きょう')}は{SHIZUKA}かった",
       f"{r('今日','きょう')}は{SHIZUKA}だでした",
       f"{r('今日','きょう')}は{SHIZUKA}いだった"],
      f"{r('今日','きょう')}は{SHIZUKA}だった",
      f"<p>な-sifat ot kabi: <strong>だった</strong>. «かった» "
      f"い-sifatlarniki.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{r('本','ほん')}を{TABETA}", f"{YASUI_D}だ",
       f"{GAKUSEI_D}じゃない", f"{IKANAKATTA}"],
      f"{YASUI_D}だ",
      f"<p>い-sifatga <strong>だ qoʻshilmaydi</strong>. Toʻgʻrisi — "
      f"shunchaki <strong>{YASUI_D}</strong>. (Birinchi variantdagi "
      f"{TABETA} — «yedim», u toʻgʻri.)</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{r('食','た')}べます → {TABERU_D}", f"{r('食','た')}べません → {TABENAI}",
       f"{r('食','た')}べませんでした → {TABENAI}だった",
       f"{r('食','た')}べました → {TABETA}"],
      f"{r('食','た')}べませんでした → {TABENAI}だった",
      f"<p>Toʻgʻrisi — <strong>{TABENAKATTA}</strong>. ない い-sifat, demak "
      f"い → かった; だった esa otlarniki.</p>"),

    q("<p>Shubha boʻlsa qaysi uslubni tanlaysiz?</p>",
      ["丁寧体 — です・ます", "普通体 — oddiy shakl",
       "Ikkalasini aralashtiraman", "Farqi yoʻq"],
      "丁寧体 — です・ます",
      f"<p>Ortiqcha muloyimlik hech qachon xato emas; yetarli boʻlmagan "
      f"muloyimlik esa haqoratdek eshitilishi mumkin.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p>Kundalikda yozyapsiz: "
      f"<strong>{r('今日','きょう')}{r('学校','がっこう')}へ___。</strong></p>",
      [ITTA, f"{r('行','い')}きました", f"{ITTA}です", f"{IKU_D}だ"],
      ITTA,
      f"<p>Kundalik — <ruby>普通体<rt>ふつうたい</rt></ruby>, demak "
      f"<strong>{ITTA}</strong>. «{r('行','い')}きました» muloyim shakl, "
      f"kundalikka toʻgʻri kelmaydi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-43 Mashq: Sanoq soʻzlari (助数詞)",
        "tutorial":    "PJ-43:",
        "description": "匹, 本, 枚, 個, 台, 人 — va tovush oʻzgarishi: "
                       "1/6/8/10 sokuon, 3 va 何 jaranglashish.",
        "questions":   Q_PJ43,
        **DEFAULTS,
    },
    {
        "title":       "PJ-44 Mashq: Taqqoslash — より, のほうが, いちばん",
        "tutorial":    "PJ-44:",
        "description": "Sifat oʻzgarmaydi — ishni qoʻshimchalar bajaradi. "
                       "より past tomonda, のほうが yuqori tomonda.",
        "questions":   Q_PJ44,
        **DEFAULTS,
    },
    {
        "title":       "PJ-45 Mashq: Oddiy shakl (普通体)",
        "tutorial":    "PJ-45:",
        "description": "丁寧体 dan 普通体 ga oʻtish. Feʼlda faqat bitta shakl "
                       "yangi, va だ faqat ot bilan な-sifatga qoʻshiladi.",
        "questions":   Q_PJ45,
        **DEFAULTS,
    },
]
