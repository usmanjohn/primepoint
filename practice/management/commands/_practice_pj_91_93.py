# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-91 … PJ-93.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

Bu batchning uch tuzogʻi:
    1. INKORNING MAJBURIYLIGI (PJ-91). しか qoʻyilgan gapda feʼl
       ALBATTA inkorda: <ruby>千円</ruby>しかない. Oʻzbekcha tarjima
       esa tasdiqda («faqat ming iyena bor») — bu ikki tilning eng
       katta ohang farqlaridan biri, va testning yarmi shu ustunda.
    2. UCHTA ULANISH (PJ-92). がち va <ruby>気味</ruby> —
       ます-oʻzagi yoki ot; っぽい — ot, oʻzak yoki ます-oʻzagi, va
       natija I-SIFAT boʻlib tuslanadi (っぽかった, っぽくない).
    3. BAHONING YOʻNALISHI (PJ-93). おかげで yaxshi natija bilan,
       せいで yomon natija bilan. Oʻzbekcha «tufayli» ikkalasiga
       ham toʻgʻri keladi, shuning uchun savol har safar
       «natija yaxshimi yoki yomonmi?» deb soʻraydi.

⚠️ CUMULATIVE: PJ-91 mashqida がち・っぽい・気味 (92) va
おかげで・せいで (93) yoʻq. PJ-92 da おかげで・せいで hali yoʻq.
`verify_pj_practice_91_93.py` buni mexanik tekshiradi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_91_93.py --master=prime \\
        --expect-questions=20
"""

SUBJECT = {
    "name":        "日本語",
    "description": "Yapon tili — grammatika va yozuv mashqlari",
    "icon":        "bi-brilliance",
    "color":       "#be123c",
}

DEFAULTS = {
    "level":                "hard",
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


# ── otlar ────────────────────────────────────────────────────────────
SENEN    = r("千円", "せんえん")
SAIFU    = r("財布", "さいふ")
MIZU     = r("水", "みず")
KODOMO   = r("子供", "こども")
WATASHI  = r("私", "わたし")
KUSURI   = r("薬", "くすり")
HITORI   = r("一人", "ひとり")
TOMODACHI = r("友", "とも") + "だち"
DENSHA   = r("電車", "でんしゃ")
KAZE     = r("風邪", "かぜ")
GIMI     = r("気味", "ぎみ")
KUMORI   = r("曇", "くも") + "り"
HI       = r("日", "ひ")
KOE      = r("声", "こえ")
KARADA   = r("体", "からだ")
SENSEI   = r("先生", "せんせい")
AME      = r("雨", "あめ")
SHIAI    = r("試合", "しあい")
CHUUSHI  = r("中止", "ちゅうし")
SHIKEN   = r("試験", "しけん")
GOUKAKU  = r("合格", "ごうかく")
HITO     = r("人", "ひと")
GENKI    = r("元気", "げんき")
YAKUSOKU = r("約束", "やくそく")
JIKAN    = r("時間", "じかん")
IMA      = r("今", "いま")
TOUKYOU  = r("東京", "とうきょう")

# ── sifatlar / feʼllar ───────────────────────────────────────────────
SHITTEIRU = r("知", "し") + "っている"
NOMU     = r("飲", "の") + "む"
NOMANAI  = r("飲", "の") + "まない"
NAORU    = r("治", "なお") + "る"
NAORIMASU = r("治", "なお") + "ります"
NOMEBA   = r("飲", "の") + "めば"
KURU     = r("来", "く") + "る"
KONAI    = r("来", "こ") + "ない"
WASURERU = r("忘", "わす") + "れる"
WASURE   = r("忘", "わす") + "れ"
OKURERU  = r("遅", "おく") + "れる"
OKURE    = r("遅", "おく") + "れ"
OKORU    = r("怒", "おこ") + "る"
OKORI    = r("怒", "おこ") + "り"
TSUKARERU = r("疲", "つか") + "れる"
TSUKARE  = r("疲", "つか") + "れ"
FUTORU   = r("太", "ふと") + "る"
FUTORI   = r("太", "ふと") + "り"
HATARAKU = r("働", "はたら") + "く"
HATARAKERU = r("働", "はたら") + "ける"
TETSUDATTE = r("手伝", "てつだ") + "ってくれた"
NEMUKU   = r("眠", "ねむ") + "く"
NESUGITA = r("寝", "ね") + "すぎた"
SHIRO    = r("白", "しろ")
HAJIMERU = r("始", "はじ") + "める"
TOKI     = r("時", "とき")
SAGASU   = r("探", "さが") + "す"

# ── tayyor qoliplar ──────────────────────────────────────────────────
SENEN_SHIKA_NAI  = SENEN + "しかありません"
SENEN_SHIKA_ARU  = SENEN + "しかあります"
SENEN_DAKE       = SENEN + "だけあります"
MIZU_SHIKA       = MIZU + "しか" + NOMANAI
MIZU_WO_SHIKA    = MIZU + "をしか" + NOMANAI
KODOMO_SAE       = KODOMO + "さえ" + SHITTEIRU
KUSURI_SAE_BA    = KUSURI + "さえ" + NOMEBA + NAORIMASU
KUSURI_SAE_TO    = KUSURI + "さえ" + NOMU + "と" + NAORIMASU
WASURE_GACHI     = WASURE + "がち"
WASURERU_GACHI   = WASURERU + "がち"
WASURE_PPOI      = WASURE + "っぽい"
KODOMO_PPOI      = KODOMO + "っぽい"
KODOMO_PPOKATTA  = KODOMO + "っぽかった"
KODOMO_PPOI_DESHITA = KODOMO + "っぽいでした"
KAZE_GIMI        = KAZE + GIMI + "です"
KAZE_NO_GIMI     = KAZE + "の" + GIMI + "です"
KUMORI_GACHI_NO  = KUMORI + "がちの" + HI
KUMORI_GACHI     = KUMORI + "がち" + HI
SENSEI_OKAGE     = SENSEI + "のおかげで" + GOUKAKU + "しました"
SENSEI_SEI       = SENSEI + "のせいで" + GOUKAKU + "しました"
AME_SEI          = AME + "のせいで" + SHIAI + "が" + CHUUSHI + "になりました"
AME_SEI_NASHI    = AME + "せいで" + SHIAI + "が" + CHUUSHI + "になりました"
AME_OKAGE        = AME + "のおかげで" + SHIAI + "が" + CHUUSHI + "になりました"
GENKI_NA_OKAGE   = GENKI + "なおかげで" + HATARAKERU
GENKI_NO_OKAGE   = GENKI + "のおかげで" + HATARAKERU
HITO_NO_SEI_NI   = HITO + "のせいにする"
HITO_NO_SEI_DE   = HITO + "のせいでする"


# ══════════════════════════════════════════════════════════════════════
# PJ-91 — 〜さえ, 〜こそ, 〜しか〜ない
# ══════════════════════════════════════════════════════════════════════
Q_PJ91 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜しか qoʻyilgan gapda feʼl qanday boʻladi?</p>",
      ["Albatta inkorda", "Albatta tasdiqda",
       "Albatta oʻtgan zamonda", "Albatta lugʻat shaklida"],
      "Albatta inkorda",
      f"<p><strong>Inkorda.</strong> {SENEN_SHIKA_NAI} — «faqat "
      f"ming iyena bor». Yaponcha feʼl inkorda, oʻzbekcha "
      f"tarjima esa tasdiqda. Sababi mantiqiy: しか «bundan "
      f"boshqa yoʻq» deb aytadi.</p>"),

    q("<p>〜さえ nimani bildiradi?</p>",
      ["Hatto … ham", "Aynan shu", "Faqat … (atigi)",
       "… sifatida"],
      "Hatto … ham",
      f"<p><strong>Hatto … ham</strong>: {KODOMO_SAE} — «buni "
      f"hatto bola ham biladi». さえ eng kutilmagan misolni "
      f"koʻrsatadi, va shundan «demak hamma biladi» degan "
      f"xulosa chiqadi.</p>"),

    q("<p>〜こそ nimani bildiradi?</p>",
      ["Aynan shu — boshqasini rad etib bittasini ajratadi",
       "Hatto … ham", "Faqat … (atigi)", "Tez-tez … boʻladi"],
      "Aynan shu — boshqasini rad etib bittasini ajratadi",
      f"<p><strong>Aynan shu.</strong> {IMA}こそ{HAJIMERU}"
      f"{TOKI}だ — «kecha emas, ertaga emas, aynan hozir». "
      f"こそ ichida rad etish yashiringan.</p>"),

    q(f"<p>«Hamyonda faqat ming iyena bor» — qaysi gap toʻgʻri?</p>",
      [f"{SAIFU}に{SENEN_SHIKA_NAI}",
       f"{SAIFU}に{SENEN_SHIKA_ARU}",
       f"{SAIFU}に{SENEN}しかです",
       f"{SAIFU}に{SENEN}しかあった"],
      f"{SAIFU}に{SENEN_SHIKA_NAI}",
      f"<p><strong>{SENEN_SHIKA_NAI}</strong>. «{SENEN_SHIKA_ARU}» "
      f"degan gap yaponchada yoʻq — しか har doim inkorni "
      f"talab qiladi, hatto tarjima tasdiq boʻlsa ham.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KODOMO}___"
      f"{SHITTEIRU}ことだ。</strong> («buni hatto bola ham "
      f"biladi»)</p>",
      ["さえ", "こそ", "しか", "だけ"],
      "さえ",
      f"<p><strong>{KODOMO_SAE}</strong>. Bola — bilishi eng kam "
      f"kutiladigan odam, va さえ aynan shu kutilmaganlikni "
      f"koʻrsatadi. こそ boʻlsa «aynan bola biladi» degan "
      f"boshqa gap chiqardi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KUSURI}さえ___、"
      f"{NAORIMASU}。</strong> («faqat dorini ichsangiz bas»)</p>",
      [f"{NOMEBA}", f"{NOMU}と", f"{NOMU}から", f"{NOMU}ので"],
      f"{NOMEBA}",
      f"<p><strong>{KUSURI_SAE_BA}</strong>. «Faqat … boʻlsa "
      f"bas» maʼnosi さえ va <strong>ば</strong> juftligidan "
      f"chiqadi. ば boʻlmasa, さえ «hatto … ham» boʻlib "
      f"qoladi.</p>"),

    q(f"<p>{MIZU}を{NOMU} gapiga しか qoʻshing.</p>",
      [MIZU_SHIKA, MIZU_WO_SHIKA,
       MIZU + "しか" + NOMU, MIZU + "がしか" + NOMANAI],
      MIZU_SHIKA,
      f"<p><strong>{MIZU_SHIKA}</strong>. Ikki narsa birdan "
      f"oʻzgaradi: <strong>を</strong> tushib qoladi va feʼl "
      f"inkorga oʻtadi. しか が ni ham xuddi shunday siqib "
      f"chiqaradi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HITORI}しか"
      f"___。</strong> («faqat bir kishi keldi»)</p>",
      [f"{KONAI[:-2]}ませんでした", f"{KURU[:-1]}ました",
       f"{KURU[:-1]}ます", f"{KURU}"],
      f"{KONAI[:-2]}ませんでした",
      f"<p><strong>{HITORI}しか{KONAI[:-2]}ませんでした</strong>. "
      f"Oʻtgan zamonda ham inkor shart. Oʻzbekcha «keldi» "
      f"degan tasdiq sizni adashtirmasin.</p>"),

    q(f"<p>«Aynan hozir boshlash vaqti» — qaysi gap toʻgʻri?</p>",
      [f"{IMA}こそ{HAJIMERU}{TOKI}だ",
       f"{IMA}さえ{HAJIMERU}{TOKI}だ",
       f"{IMA}しか{HAJIMERU}{TOKI}だ",
       f"{IMA}がこそ{HAJIMERU}{TOKI}だ"],
      f"{IMA}こそ{HAJIMERU}{TOKI}だ",
      f"<p><strong>{IMA}こそ</strong>. こそ boshqa paytlarni "
      f"rad etib, shu daqiqani ajratadi. Oxirgi variant "
      f"notoʻgʻri: こそ ham が ni siqib chiqaradi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{TOUKYOU}へ___"
      f"{r('行', 'い')}かない。</strong> («faqat Tokioga "
      f"boradi»)</p>",
      ["しか", "をしか", "がしか", "だけしか"],
      "しか",
      f"<p><strong>{TOUKYOU}へしか{r('行', 'い')}かない</strong>. "
      f"へ, に, と kabi qoʻshimchalar joyida qoladi va しか "
      f"ulardan <em>keyin</em> keladi — faqat が va を "
      f"tushib qoladi.</p>"),

    q("<p>«こちらこそ» qachon aytiladi?</p>",
      ["Rahmatga javoban — «asosiy men minnatdorman»",
       "Uzr soʻraganda", "Xayrlashganda", "Taklif qilganda"],
      "Rahmatga javoban — «asosiy men minnatdorman»",
      f"<p><strong>Rahmatga javoban.</strong> こそ bu yerda "
      f"«boshqasi emas, men» degan rad etishni olib yuradi. "
      f"Kundalik nutqda juda koʻp ishlatiladigan tayyor "
      f"ibora.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('忙', 'いそが')}"
      f"しくて、ごはんを{r('食', 'た')}べる{JIKAN}___ない。</strong></p>"
      f"<p>(«hatto ovqatlanishga ham vaqt yoʻq»)</p>",
      ["さえ", "しか", "だけ", "ばかり"],
      "さえ",
      f"<p><strong>{JIKAN}さえない</strong> — «hatto ovqatlanishga "
      f"ham vaqt yoʻq». さえ inkor bilan ayniqsa kuchli "
      f"chiqadi: eng zarur narsa ham yoʻq degani.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>{SENEN_DAKE} va {SENEN_SHIKA_NAI} — farqi nimada?</p>",
      ["だけ quruq xabar, しか〜ない esa «kam» degan baho beradi",
       "しか〜ない quruq xabar, だけ esa baho beradi",
       "Ikkalasi ham bir xil",
       "だけ faqat yozma tilda ishlatiladi"],
      "だけ quruq xabar, しか〜ない esa «kam» degan baho beradi",
      f"<p><strong>Kayfiyat.</strong> だけ — «ming iyena bor», "
      f"fakt. しか〜ない — «atigi ming iyena», gapiruvchi buni "
      f"yetarsiz deb hisoblaydi. Oʻzbekcha «atigi» va "
      f"«bor-yoʻgʻi» shu ohangni koʻtaradi.</p>"),

    q("<p>さえ ning ikki maʼnosini nima ajratadi?</p>",
      ["Gapda ば bor-yoʻqligi",
       "Gapning uzunligi",
       "Feʼlning zamoni",
       "Otning turi"],
      "Gapda ば bor-yoʻqligi",
      f"<p><strong>ば bor-yoʻqligi.</strong> ば bor — «faqat … "
      f"boʻlsa bas» ({KUSURI_SAE_BA}). ば yoʻq — «hatto … ham» "
      f"({KODOMO_SAE}). Uchinchi variant yoʻq, shuning uchun "
      f"koʻzingiz avval gapning oxiriga tushsin.</p>"),

    q(f"<p>«Faqat bir kishi keldi» degan gapni gapiruvchi KAM deb "
      f"hisoblasa, qaysi qolip?</p>",
      [f"{HITORI}しか{KONAI[:-2]}ませんでした",
       f"{HITORI}だけ{KURU[:-1]}ました",
       f"{HITORI}さえ{KURU[:-1]}ました",
       f"{HITORI}こそ{KURU[:-1]}ました"],
      f"{HITORI}しか{KONAI[:-2]}ませんでした",
      f"<p><strong>しか〜ない</strong>. Ikkala gap ham bitta "
      f"voqeani aytadi, lekin だけ befarq, しか〜ない esa "
      f"norozi. Tanlovni gapiruvchining kayfiyati "
      f"qiladi.</p>"),

    q("<p>Qaysi qolip が va を ni siqib chiqarmaydi?</p>",
      ["Hech qaysi — uchalasi ham siqib chiqaradi",
       "Faqat さえ", "Faqat こそ", "Faqat しか"],
      "Hech qaysi — uchalasi ham siqib chiqaradi",
      f"<p><strong>Uchalasi ham siqib chiqaradi.</strong> Bu "
      f"PJ-83 dagi ばかり bilan bir xil qoida. Qolgan "
      f"qoʻshimchalar (へ, に, と, で) esa joyida qoladi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [SENEN_SHIKA_ARU, SENEN_SHIKA_NAI, MIZU_SHIKA, KODOMO_SAE],
      SENEN_SHIKA_ARU,
      f"<p>Xato <strong>{SENEN_SHIKA_ARU}</strong> da: しか "
      f"qoʻyilgan gapda feʼl inkorda boʻlishi shart. Toʻgʻrisi "
      f"— <strong>{SENEN_SHIKA_NAI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [MIZU_SHIKA, MIZU_WO_SHIKA,
       MIZU + "がしか" + NOMANAI, MIZU + "しか" + NOMU],
      MIZU_SHIKA,
      f"<p><strong>{MIZU_SHIKA}</strong>. Ikki shart birga: "
      f"を tushadi va feʼl inkorga oʻtadi. Oxirgi variantda "
      f"を toʻgʻri tushgan, lekin feʼl tasdiqda "
      f"qolgan.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{SAIFU}に / "
      f"{SENEN} / しか / ありません</strong></p>",
      [f"{SAIFU}に{SENEN}しかありません",
       f"{SENEN}に{SAIFU}しかありません",
       f"しか{SAIFU}に{SENEN}ありません",
       f"ありません{SAIFU}に{SENEN}しか"],
      f"{SAIFU}に{SENEN}しかありません",
      f"<p><strong>{SAIFU}に{SENEN_SHIKA_NAI}</strong>. Joy "
      f"boshda, miqdor oʻrtada, kesim oxirida. しか oʻzi "
      f"ajratayotgan soʻzdan <em>keyin</em> turadi, hech "
      f"qachon undan oldin emas.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: "
      f"{r('手伝', 'てつだ')}ってくれて、ありがとう。</strong></p>"
      f"<p><strong>イムロン: ___</strong></p>",
      ["こちらこそ、ありがとう。", "こちらさえ、ありがとう。",
       "こちらしか、ありがとう。", "こちらだけ、ありがとう。"],
      "こちらこそ、ありがとう。",
      f"<p><strong>こちらこそ</strong> — «asosiy men "
      f"minnatdorman». Rahmatga beriladigan eng odatiy "
      f"javob, va こそ bu yerda «siz emas, men» degan rad "
      f"etishni olib yuradi.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-92 — 〜がち, 〜っぽい, 〜気味
# ══════════════════════════════════════════════════════════════════════
Q_PJ92 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜がち nimani bildiradi?</p>",
      ["Chastota — tez-tez shunday boʻladi",
       "Daraja — bir oz shunday",
       "Xususiyat — shunga oʻxshaydi",
       "Rol — … sifatida"],
      "Chastota — tez-tez shunday boʻladi",
      f"<p><strong>Chastota.</strong> この{DENSHA}は{OKURE}がち"
      f"だ — «bu poyezd tez-tez kechikadi». Har safar emas, "
      f"lekin koʻp. Ohangi deyarli doim salbiy.</p>"),

    q("<p>〜っぽい nimani bildiradi?</p>",
      ["Xususiyat — … ga oʻxshagan, … simon",
       "Chastota — tez-tez shunday boʻladi",
       "Daraja — bir oz shunday",
       "Sabab — … tufayli"],
      "Xususiyat — … ga oʻxshagan, … simon",
      f"<p><strong>Xususiyat.</strong> {KODOMO_PPOI} — "
      f"«bolalarcha». Gapiruvchi bola emas, u faqat bolaga "
      f"<em>oʻxshab</em> gapiryapti.</p>"),

    q(f"<p>〜{GIMI} nimani bildiradi?</p>",
      ["Daraja — bir oz shunday",
       "Chastota — tez-tez shunday boʻladi",
       "Xususiyat — … ga oʻxshagan",
       "Majburiyat — … kerak"],
      "Daraja — bir oz shunday",
      f"<p><strong>Daraja.</strong> {KAZE_GIMI} — «bir oz "
      f"shamollaganman». Holat bor, lekin kuchli emas, va "
      f"gap shu bilan yumshaydi.</p>"),

    q(f"<p>{WASURERU} feʼlini がち bilan qoʻshing.</p>",
      [WASURE_GACHI, WASURERU_GACHI,
       WASURE + "ますがち", WASURE + "てがち"],
      WASURE_GACHI,
      f"<p><strong>{WASURE_GACHI}</strong>. ます-shakli "
      f"{WASURE}ます, oʻzagi {WASURE} — oʻshanga ulanadi. "
      f"Lugʻat shakli ham, ます ham bu yerga tushmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('今日', 'きょう')}"
      f"は{KAZE}___です。</strong> («bugun bir oz "
      f"shamollaganman»)</p>",
      [f"{GIMI}", "がち", "っぽい", f"の{GIMI}"],
      f"{GIMI}",
      f"<p><strong>{KAZE_GIMI}</strong>. {GIMI} otga "
      f"<em>yalangʻoch</em> yopishadi — «{KAZE_NO_GIMI}» "
      f"notoʻgʻri. がち bu yerda «tez-tez shamollayman» "
      f"degan boshqa gap boʻlardi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>«Bolalarcha edi» — qaysi gap toʻgʻri?</p>",
      [KODOMO_PPOKATTA, KODOMO_PPOI_DESHITA,
       KODOMO + "っぽいだった", KODOMO + "っぽくでした"],
      KODOMO_PPOKATTA,
      f"<p><strong>{KODOMO_PPOKATTA}</strong>. っぽい "
      f"<strong>い-sifat</strong> boʻlib tuslanadi, shuning "
      f"uchun oʻtgan zamoni っぽかった, inkori esa っぽくない. "
      f"Bu PJ-25 dagi qoidaning oʻzi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KUMORI}がち___"
      f"{HI}が{r('多', 'おお')}い。</strong></p>",
      ["の", "な", "だ", "hech nima"],
      "の",
      f"<p><strong>{KUMORI_GACHI_NO}</strong>. がち otni "
      f"aniqlaganda oradan <strong>の</strong> tushadi. "
      f"«{KUMORI_GACHI}» notoʻgʻri.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('最近', 'さいきん')}"
      f"{FUTORI}___なので、{r('歩', 'ある')}くようにしています。</strong></p>",
      [f"{GIMI}", "がち", "っぽい", "そう"],
      f"{GIMI}",
      f"<p><strong>{FUTORI}{GIMI}</strong> — «biroz semirib "
      f"ketdim». «Semirdim» deyish qoʻpol; {GIMI} gapni "
      f"yumshatadi, va bu uning asosiy ishi.</p>"),

    q(f"<p>«U unutuvchan odam — tabiati shunday» — qaysi qolip?</p>",
      [WASURE_PPOI, WASURE_GACHI,
       WASURE + GIMI, WASURERU_GACHI],
      WASURE_PPOI,
      f"<p><strong>{WASURE_PPOI}</strong> — bu uning "
      f"<em>tabiati</em>, doimiy xususiyat. {WASURE_GACHI} "
      f"esa chastota haqida: «bu safar ham unutdi, tez-tez "
      f"shunday boʻladi».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>この{DENSHA}は"
      f"{OKURE}___だ。</strong> («bu poyezd tez-tez kechikadi»)</p>",
      ["がち", "っぽい", f"{GIMI}の", "そう"],
      "がち",
      f"<p><strong>{OKURE}がち</strong>. Chastota haqida gap "
      f"ketyapti — «koʻpincha, lekin har safar emas». がち "
      f"ni «har doim» deb tarjima qilmang.</p>"),

    q(f"<p>«Jizzaki» — qaysi gap toʻgʻri?</p>",
      [OKORI + "っぽい", OKORU + "っぽい",
       OKORI + "ますっぽい", OKORI + "てっぽい"],
      OKORI + "っぽい",
      f"<p><strong>{OKORI}っぽい</strong>. っぽい feʼlga "
      f"ulanganda ます-oʻzagini oladi: {OKORU} → {OKORI}ます "
      f"→ {OKORI}っぽい.</p>"),

    q(f"<p>{SHIRO}っぽい nimani bildiradi?</p>",
      ["Oqishroq", "Juda oq", "Oq emas", "Tez-tez oq boʻladi"],
      "Oqishroq",
      f"<p><strong>Oqishroq.</strong> っぽい rang bilan "
      f"ayniqsa qulay: {SHIRO}っぽい — «oqishroq», "
      f"{r('赤', 'あか')}っぽい — «qizgʻishroq». Oʻzbekcha "
      f"«-ish» qoʻshimchasi shu ishni qiladi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>{WASURE_GACHI} va {WASURE_PPOI} — farqi nimada?</p>",
      ["がち chastota, っぽい esa doimiy xususiyat",
       "っぽい chastota, がち esa doimiy xususiyat",
       "Ikkalasi ham bir xil",
       "がち faqat yozma tilda ishlatiladi"],
      "がち chastota, っぽい esa doimiy xususiyat",
      f"<p><strong>{WASURE_GACHI}</strong> — «tez-tez unutadi», "
      f"bu safar ham unutdi. <strong>{WASURE_PPOI}</strong> — "
      f"«unutuvchan», uning tabiati shunday. Bitta feʼl, "
      f"ikki boshqa gap.</p>"),

    q("<p>Qaysi qolip い-sifat boʻlib tuslanadi?</p>",
      ["〜っぽい", "〜がち", f"〜{GIMI}", "Uchalasi ham"],
      "〜っぽい",
      f"<p><strong>〜っぽい</strong>: っぽかった, っぽくない. "
      f"がち va {GIMI} esa な-sifat kabi ishlaydi — "
      f"{WASURE_GACHI}だ, {KAZE_GIMI}.</p>"),

    q(f"<p>«{r('上手', 'じょうず')}っぽいですね» ni maqtov sifatida "
      f"ishlatsa boʻladimi?</p>",
      ["Yoʻq — bu oila maqtov uchun emas, kinoya boʻlib chiqadi",
       "Ha — っぽい har doim maqtov",
       "Ha, lekin faqat yozma tilda",
       "Yoʻq — っぽい otga umuman ulanmaydi"],
      "Yoʻq — bu oila maqtov uchun emas, kinoya boʻlib chiqadi",
      f"<p><strong>Yoʻq.</strong> Bu uchlik deyarli faqat "
      f"yoqimsiz narsalar bilan keladi. Maqtov uchun PJ-73 "
      f"dagi <strong>そう</strong> kerak: "
      f"{r('上手', 'じょうず')}そうですね.</p>"),

    q(f"<p>«Tez-tez kasal boʻladigan» — qaysi gap toʻgʻri?</p>",
      [f"{r('病気', 'びょうき')}がち", f"{r('病気', 'びょうき')}っぽい",
       f"{r('病気', 'びょうき')}の{GIMI}", f"{r('病気', 'びょうき')}ますがち"],
      f"{r('病気', 'びょうき')}がち",
      f"<p><strong>{r('病気', 'びょうき')}がち</strong> — lugʻatda "
      f"alohida soʻz sifatida turadigan tayyor birikma. がち "
      f"otga ham, ます-oʻzagiga ham ulanadi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [WASURERU_GACHI, WASURE_GACHI, KODOMO_PPOKATTA, KAZE_GIMI],
      WASURERU_GACHI,
      f"<p>Xato <strong>{WASURERU_GACHI}</strong> da: がち "
      f"ます-oʻzagiga ulanadi, lugʻat shakliga emas. "
      f"Toʻgʻrisi — <strong>{WASURE_GACHI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [KAZE_GIMI, KAZE_NO_GIMI,
       KAZE + "な" + GIMI + "です", KAZE + "っぽ" + GIMI + "です"],
      KAZE_GIMI,
      f"<p><strong>{KAZE_GIMI}</strong>. {GIMI} otga "
      f"yalangʻoch yopishadi — の ham, な ham undan oldin "
      f"turmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>"
      f"{r('寝', 'ね')}{r('不足', 'ぶそく')}が / {r('続', 'つづ')}くと / "
      f"{WASURE}っぽく / なります</strong></p>",
      [f"{r('寝', 'ね')}{r('不足', 'ぶそく')}が{r('続', 'つづ')}くと"
       f"{WASURE}っぽくなります",
       f"{WASURE}っぽく{r('寝', 'ね')}{r('不足', 'ぶそく')}が"
       f"{r('続', 'つづ')}くとなります",
       f"{r('続', 'つづ')}くと{r('寝', 'ね')}{r('不足', 'ぶそく')}が"
       f"{WASURE}っぽくなります",
       f"なります{r('寝', 'ね')}{r('不足', 'ぶそく')}が"
       f"{r('続', 'つづ')}くと{WASURE}っぽく"],
      f"{r('寝', 'ね')}{r('不足', 'ぶそく')}が{r('続', 'つづ')}くと"
      f"{WASURE}っぽくなります",
      f"<p><strong>{r('寝', 'ね')}{r('不足', 'ぶそく')}が"
      f"{r('続', 'つづ')}くと{WASURE}っぽくなります</strong>. "
      f"Shart birinchi, natija keyin. っぽい い-sifat "
      f"boʻlgani uchun なる oldida っぽ<strong>く</strong> "
      f"ga oʻzgaradi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>パリ: "
      f"{r('顔色', 'かおいろ')}がよくないですね。</strong></p>"
      f"<p><strong>ラノ: ___</strong></p>",
      [f"ええ、{r('少', 'すこ')}し{KAZE}の{GIMI}です。",
       f"ええ、{r('少', 'すこ')}し{KAZE}{GIMI}です。",
       f"ええ、{r('少', 'すこ')}し{KAZE}がちです。",
       f"ええ、{r('少', 'すこ')}し{KAZE}っぽいでした。"],
      f"ええ、{r('少', 'すこ')}し{KAZE}{GIMI}です。",
      f"<p><strong>{KAZE_GIMI}</strong> — «bir oz "
      f"shamollaganman». がち qoʻyilsa «tez-tez "
      f"shamollayman» degan boshqa gap chiqadi, っぽいでした "
      f"esa grammatik jihatdan notoʻgʻri.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-93 — 〜おかげで va 〜せいで
# ══════════════════════════════════════════════════════════════════════
Q_PJ93 = [
    # ── 1–5 tanish ───────────────────────────────────────────────────
    q("<p>〜おかげで qanday natija bilan keladi?</p>",
      ["Yaxshi natija — gapda minnatdorchilik bor",
       "Yomon natija — gapda ayb bor",
       "Bahosiz natija",
       "Faqat kelasi zamon natijasi"],
      "Yaxshi natija — gapda minnatdorchilik bor",
      f"<p><strong>Yaxshi natija.</strong> {SENSEI_OKAGE} — "
      f"«ustoz sharofati bilan imtihondan oʻtdim». おかげ "
      f"soʻzining oʻzi «yordam, marhamat» degani.</p>"),

    q("<p>〜せいで qanday natija bilan keladi?</p>",
      ["Yomon natija — gapda ayb bor",
       "Yaxshi natija — gapda minnatdorchilik bor",
       "Bahosiz natija",
       "Faqat oʻtgan zamon natijasi"],
      "Yomon natija — gapda ayb bor",
      f"<p><strong>Yomon natija.</strong> せい soʻzining oʻzi "
      f"«ayb» degani: {AME_SEI} — «yomgʻir dastidan oʻyin "
      f"bekor qilindi».</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{AME}___せいで"
      f"{SHIAI}が{CHUUSHI}になりました。</strong></p>",
      ["の", "な", "だ", "hech nima"],
      "の",
      f"<p><strong>{AME}のせいで</strong>. せい — ot, shuning "
      f"uchun ot oldidan <strong>の</strong> oladi. "
      f"«{AME_SEI_NASHI}» notoʻgʻri.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GENKI}___おかげで"
      f"{HATARAKERU}。</strong></p>",
      ["な", "の", "だ", "hech nima"],
      "な",
      f"<p><strong>{GENKI_NA_OKAGE}</strong>. な-sifat おかげ "
      f"oldida <strong>な</strong> ni saqlaydi — aynan shu "
      f"ulanish PJ-81 dagi はず va PJ-85 dagi うち da ham "
      f"turadi.</p>"),

    q("<p>Neytral, bahosiz sabab uchun qaysi qolip?</p>",
      ["〜から yoki 〜ので", "〜おかげで", "〜せいで", "〜のために"],
      "〜から yoki 〜ので",
      f"<p><strong>〜から / 〜ので</strong> (PJ-53). おかげで va "
      f"せいで sababga <em>baho</em> qoʻshadi; ので esa faqat "
      f"xabar beradi.</p>"),

    # ── 6–12 qoʻllash ────────────────────────────────────────────────
    q(f"<p>«Ustoz sharofati bilan imtihondan oʻtdim» — qaysi gap "
      f"toʻgʻri?</p>",
      [SENSEI_OKAGE, SENSEI_SEI,
       SENSEI + "おかげで" + GOUKAKU + "しました",
       SENSEI + "なおかげで" + GOUKAKU + "しました"],
      SENSEI_OKAGE,
      f"<p><strong>{SENSEI_OKAGE}</strong>. Natija yaxshi, "
      f"demak minnatdorchilik qolipi; va ot おかげ oldidan "
      f"の oladi.</p>"),

    q(f"<p>«Yomgʻir dastidan oʻyin bekor qilindi» — qaysi gap "
      f"toʻgʻri?</p>",
      [AME_SEI, AME_OKAGE, AME_SEI_NASHI,
       AME + "なせいで" + SHIAI + "が" + CHUUSHI + "になりました"],
      AME_SEI,
      f"<p><strong>{AME_SEI}</strong>. Natija yomon — せいで. "
      f"おかげで qoʻyilsa, gap kinoya boʻlib eshitiladi.</p>"),

    q(f"<p>«Birovni ayblamoq» — qaysi ibora?</p>",
      [HITO_NO_SEI_NI, HITO_NO_SEI_DE,
       HITO + "のおかげにする", HITO + "にせいをする"],
      HITO_NO_SEI_NI,
      f"<p><strong>{HITO_NO_SEI_NI}</strong> — «aybni birovga "
      f"yuklamoq». Bu iborada で emas, <strong>に</strong> "
      f"turadi: せい<strong>に</strong>する.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{NESUGITA}___、"
      f"{YAKUSOKU}に{r('遅', 'おく')}れてしまった。</strong></p>",
      ["せいで", "おかげで", "のせいで", "のおかげで"],
      "せいで",
      f"<p><strong>{NESUGITA}せいで</strong>. Feʼl bilan "
      f"ulanganda oddiy shakl yalangʻoch turadi — の faqat "
      f"otga kerak. Natija yomon, demak せいで.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>みなさんが"
      f"{TETSUDATTE}___、{r('無事', 'ぶじ')}に{r('終', 'お')}わりました。"
      f"</strong></p>",
      ["おかげで", "せいで", "のおかげで", "なおかげで"],
      "おかげで",
      f"<p><strong>{TETSUDATTE}おかげで</strong>. Feʼlning "
      f"oddiy shakli (PJ-45) yalangʻoch ulanadi, va natija "
      f"yaxshi. Bu gap nutq va xatlarda deyarli tayyor "
      f"qolip.</p>"),

    q("<p>«おかげさまで» qachon aytiladi?</p>",
      ["«Qalaysiz?» degan savolga javoban — «rahmat, yaxshiman»",
       "Uzr soʻraganda",
       "Birovni ayblaganda",
       "Xayrlashganda"],
      "«Qalaysiz?» degan savolga javoban — «rahmat, yaxshiman»",
      f"<p><strong>Qalaysiz degan savolga javoban.</strong> "
      f"Uning ichida «sizning marhamatingiz bilan» degan "
      f"maʼno bor, va yaponlar buni rahmat aytadigan aniq "
      f"odam boʻlmasa ham ishlatadi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KUSURI}のせいで"
      f"___なりました。</strong></p>",
      [f"{NEMUKU}", f"{NAORU[:-1]}って", f"{GOUKAKU}に",
       f"{GENKI}に"],
      f"{NEMUKU}",
      f"<p><strong>{KUSURI}のせいで{NEMUKU}なりました</strong> — "
      f"«dori dastidan uyqum keldi». せいで dan keyin "
      f"<em>yomon</em> natija turadi; tuzalish yoki "
      f"sogʻayish esa おかげで ning ishi.</p>"),

    # ── 13–16 farqlash ───────────────────────────────────────────────
    q(f"<p>{SENSEI_SEI} — bu gap nega gʻalati?</p>",
      ["Natija yaxshi, lekin せいで yomon natija uchun",
       "せい otga の bilan ulanmaydi",
       f"{GOUKAKU} feʼli bu qolipni olmaydi",
       "せいで faqat oʻtgan zamonda ishlatiladi"],
      "Natija yaxshi, lekin せいで yomon natija uchun",
      f"<p><strong>Natija yaxshi.</strong> Imtihondan oʻtish — "
      f"quvonchli xabar, va せい «ayb» degani. Toʻgʻrisi — "
      f"<strong>{SENSEI_OKAGE}</strong>.</p>"),

    q(f"<p>Oʻzbekcha «tufayli» qaysi qolipga toʻgʻri keladi?</p>",
      ["Ikkalasiga ham — shuning uchun natijaga qarash kerak",
       "Faqat おかげで ga",
       "Faqat せいで ga",
       "Hech qaysiga — «tufayli» faqat ので ga toʻgʻri keladi"],
      "Ikkalasiga ham — shuning uchun natijaga qarash kerak",
      f"<p><strong>Ikkalasiga ham.</strong> «Ustoz tufayli "
      f"oʻtdim» ham, «yomgʻir tufayli bekor boʻldi» ham "
      f"toʻgʻri oʻzbekcha. Shuning uchun «tufayli» ni "
      f"koʻrganda toʻxtang va natija yaxshimi yoki yomonmi "
      f"deb soʻrang.</p>"),

    q(f"<p>{r('君', 'きみ')}のおかげで{r('遅', 'おく')}れたよ — bu gap "
      f"nima maʼnoni beradi?</p>",
      ["Kinoya — ochiq tanbeh",
       "Chin dildan minnatdorchilik",
       "Bahosiz xabar",
       "Iltimos"],
      "Kinoya — ochiq tanbeh",
      f"<p><strong>Kinoya.</strong> «Sening <em>sharofating</em> "
      f"bilan kech qoldim» — natija yomon, lekin おかげで "
      f"ishlatilgan. Oʻzbekchada ham aynan shunday "
      f"gʻalatilik kinoya boʻlib eshitiladi.</p>"),

    q("<p>Rasmiy matnda せいで oʻrniga nima ishlatiladi?</p>",
      ["〜によって yoki 〜ので", "〜おかげで", "〜のために", "〜として"],
      "〜によって yoki 〜ので",
      f"<p><strong>〜によって (PJ-87) yoki 〜ので.</strong> "
      f"せいで ochiq ayblash, va yaponchada bu juda kuchli "
      f"eshitiladi — shuning uchun rasmiy matnda uning "
      f"oʻrniga bahosiz qolip turadi.</p>"),

    # ── 17–18 xato topish ────────────────────────────────────────────
    q("<p>Qaysi gapda xato bor?</p>",
      [AME_SEI_NASHI, AME_SEI, SENSEI_OKAGE, GENKI_NA_OKAGE],
      AME_SEI_NASHI,
      f"<p>Xato <strong>{AME_SEI_NASHI}</strong> da: せい ot "
      f"boʻlgani uchun ot oldidan <strong>の</strong> oladi. "
      f"Toʻgʻrisi — <strong>{AME_SEI}</strong>.</p>"),

    q("<p>Qaysi gap toʻgʻri?</p>",
      [GENKI_NA_OKAGE, GENKI_NO_OKAGE,
       GENKI + "だおかげで" + HATARAKERU,
       GENKI + "おかげで" + HATARAKERU],
      GENKI_NA_OKAGE,
      f"<p><strong>{GENKI_NA_OKAGE}</strong>. な-sifat "
      f"<strong>な</strong> ni saqlaydi; の faqat otga, だ "
      f"esa umuman bu yerga tushmaydi.</p>"),

    # ── 19–20 tuzish ─────────────────────────────────────────────────
    q(f"<p>Soʻzlarni toʻgʻri tartibda tering.</p><p><strong>{AME}の / "
      f"せいで / {SHIAI}が / {CHUUSHI}になりました</strong></p>",
      [f"{AME}のせいで{SHIAI}が{CHUUSHI}になりました",
       f"{SHIAI}が{AME}のせいで{CHUUSHI}になりましたの",
       f"せいで{AME}の{SHIAI}が{CHUUSHI}になりました",
       f"{CHUUSHI}になりました{AME}のせいで{SHIAI}が"],
      f"{AME}のせいで{SHIAI}が{CHUUSHI}になりました",
      f"<p><strong>{AME_SEI}</strong>. Sabab birinchi, natija "
      f"keyin — bu tartib おかげで da ham, せいで da ham hech "
      f"qachon almashmaydi.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ムニラ: {SHIKEN}は"
      f"どうでしたか。</strong></p><p><strong>イノム: ___</strong></p>",
      [f"{SENSEI}のおかげで{GOUKAKU}しました。",
       f"{SENSEI}のせいで{GOUKAKU}しました。",
       f"{SENSEI}おかげで{GOUKAKU}しました。",
       f"{SENSEI}なおかげで{GOUKAKU}しました。"],
      f"{SENSEI}のおかげで{GOUKAKU}しました。",
      f"<p><strong>{SENSEI_OKAGE}</strong>. Natija yaxshi, "
      f"demak minnatdorchilik qolipi — va ot おかげ oldidan "
      f"の oladi, な emas.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-91 Mashq: 〜さえ, 〜こそ, 〜しか〜ない",
        "tutorial":    "PJ-91:",
        "description": "Ajratib koʻrsatuvchi qoʻshimchalar — va nega "
                       "しか har doim inkor bilan keladi.",
        "questions":   Q_PJ91,
        **DEFAULTS,
    },
    {
        "title":       "PJ-92 Mashq: 〜がち, 〜っぽい, 〜気味",
        "tutorial":    "PJ-92:",
        "description": "Chastota, xususiyat va daraja — uchta qolip, "
                       "uchta boshqa ulanish.",
        "questions":   Q_PJ92,
        **DEFAULTS,
    },
    {
        "title":       "PJ-93 Mashq: 〜おかげで va 〜せいで",
        "tutorial":    "PJ-93:",
        "description": "Bitta sabab, ikkita baho — va oʻzbekcha "
                       "«tufayli» nega yetarli emas.",
        "questions":   Q_PJ93,
        **DEFAULTS,
    },
]
