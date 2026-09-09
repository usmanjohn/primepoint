# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-22 … PJ-24.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_22_24.py --master=prime \\
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

KY  = "<ruby>教室<rt>きょうしつ</rt></ruby>"
GK  = "<ruby>学校<rt>がっこう</rt></ruby>"
IE  = "<ruby>家<rt>いえ</rt></ruby>"
SE  = "<ruby>先生<rt>せんせい</rt></ruby>"
HO  = "<ruby>本<rt>ほん</rt></ruby>"
IK  = "<ruby>行<rt>い</rt></ruby>きます"
YM  = "<ruby>読<rt>よ</rt></ruby>みます"
BK  = "<ruby>勉強<rt>べんきょう</rt></ruby>します"
TB  = "<ruby>食<rt>た</rt></ruby>べます"
KN  = "<ruby>昨日<rt>きのう</rt></ruby>"
NG  = "<ruby>日本語<rt>にほんご</rt></ruby>"
YJ  = "<ruby>四時<rt>よじ</rt></ruby>"
KJ  = "<ruby>九時<rt>くじ</rt></ruby>"
GJ  = "<ruby>五時<rt>ごじ</rt></ruby>"
GY  = "<ruby>月曜日<rt>げつようび</rt></ruby>"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


Q_PJ22 = [
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KY}___{BK}。</strong></p>",
      ["に", "で", "へ", "を"], "で",
      f"<p><strong>で</strong> — {BK} harakat feʼli, ish oʻsha yerda "
      f"<strong>bajarilyapti</strong>.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KY}___{SE}がいます。</strong></p>",
      ["で", "に", "へ", "から"], "に",
      "<p><strong>に</strong> — います mavjudlikni bildiradi, harakatni emas.</p>"),
    q("<p>に va で ni qanday tez ajratasiz?</p>",
      ["Joyning kattaligiga qarab", "Feʼlga qarab: あります/います → に, harakat → で",
       "Gapning uzunligiga qarab", "Vaqt soʻziga qarab"],
      "Feʼlga qarab: あります/います → に, harakat → で",
      "<p><strong>Feʼl hal qiladi.</strong> Boshqa hech narsani oʻylash "
      "kerak emas.</p>"),
    q("<p>へ qanday oʻqiladi?</p>",
      ["he", "e", "we", "ha"], "e",
      "<p><strong>[e]</strong>. は [wa] va を [o] bilan bir qatorda — uchta "
      "eski qoʻshimcha, faqat qoʻshimcha sifatida shunday oʻqiladi.</p>"),
    q("<p>«Avtobusda boraman» ni tanlang.</p>",
      [f"バスで{IK}", f"バスに{IK}", f"バスへ{IK}", f"バスを{IK}"],
      f"バスで{IK}",
      "<p><strong>で</strong> — vosita: nima yordamida. Transport, asbob va "
      "til hammasi で oladi.</p>"),
    q("<p>で ning ikkita asosiy vazifasi qaysi?</p>",
      ["Joy va vaqt", "Ish bajarilgan joy va vosita",
       "Ega va toʻldiruvchi", "Yoʻnalish va manzil"],
      "Ish bajarilgan joy va vosita",
      f"<p><strong>{KY}で{BK}</strong> — ish joyi. <strong>バスで{IK}</strong> "
      f"— vosita.</p>"),
    q("<p>«Piyoda» qanday aytiladi?</p>",
      ["<ruby>足<rt>あし</rt></ruby>で", "<ruby>歩<rt>ある</rt></ruby>いて",
       "<ruby>歩<rt>ある</rt></ruby>で", "<ruby>足<rt>あし</rt></ruby>に"],
      "<ruby>歩<rt>ある</rt></ruby>いて",
      "<p><strong><ruby>歩<rt>ある</rt></ruby>いて</strong> — alohida ibora, "
      "で olmaydi. Oyoq vosita emas, harakatning oʻzi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>鉛筆<rt>えんぴつ</rt></ruby>___<ruby>書<rt>か</rt></ruby>きます。</strong></p>",
      ["に", "で", "を", "へ"], "で",
      "<p><strong>で</strong> — asbob ham vosita: «qalam<em>da</em> yozaman».</p>"),
    q("<p>に va へ orasidagi farq nima?</p>",
      ["に manzil, へ tomon — amalda deyarli bir xil",
       "に vaqt, へ joy", "に rasmiy, へ kundalik", "Farqi yoʻq, へ eskirgan"],
      "に manzil, へ tomon — amalda deyarli bir xil",
      "<p>Farq shu qadar nozikki, yaponlar ham almashtirib ishlatadi. "
      "<strong>へ</strong> biroz rasmiyroq va xat/manzillarda koʻproq "
      "uchraydi. Boshlovchi <strong>に</strong> ni tanlasa boʻladi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IE}___{HO}を{YM}。</strong></p>",
      ["に", "で", "へ", "から"], "で",
      f"<p><strong>で</strong> — {YM} harakat feʼli.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{IE}___{HO}があります。</strong></p>",
      ["で", "に", "へ", "を"], "に",
      "<p><strong>に</strong> — あります mavjudlik. Bir xil joy, boshqa feʼl, "
      "boshqa qoʻshimcha.</p>"),
    q("<p>Nega oʻzbek oʻquvchi に/で farqida adashadi?</p>",
      ["Qoʻshimchalar oʻxshash", "Oʻzbekchada bitta «-da» ikkala ishni ham bajaradi",
       "で juda kam uchraydi", "に faqat yozuvda ishlatiladi"],
      "Oʻzbekchada bitta «-da» ikkala ishni ham bajaradi",
      "<p>«Kutubxona<em>da</em> kitob bor» va «kutubxona<em>da</em> oʻqiyman» — "
      "oʻzbekchada bir xil. Yaponchada esa <strong>に</strong> va "
      "<strong>で</strong>. Sezgi yordam bermaydi, shuning uchun feʼlga "
      "qarash kerak.</p>"),
    q(f"<p>«Yaponchada gaplashaman» ni tanlang.</p>",
      [f"{NG}で<ruby>話<rt>はな</rt></ruby>します",
       f"{NG}に<ruby>話<rt>はな</rt></ruby>します",
       f"{NG}を<ruby>話<rt>はな</rt></ruby>します",
       f"{NG}へ<ruby>話<rt>はな</rt></ruby>します"],
      f"{NG}で<ruby>話<rt>はな</rt></ruby>します",
      "<p>Til ham <strong>vosita</strong> — で oladi.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{KY}で{BK}", f"{KY}に{BK}",
       f"{KY}に{SE}がいます", f"バスで{IK}"],
      f"{KY}に{BK}",
      f"<p>{BK} harakat feʼli, demak <strong>で</strong> kerak.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{KY}に{SE}がいます", f"{KY}で{SE}がいます",
       f"{IE}で{YM}", f"{GK}へ{IK}"],
      f"{KY}で{SE}がいます",
      "<p>います mavjudlik bildiradi — <strong>に</strong> kerak.</p>"),
    q("<p>へ ni «he» deb oʻqish nega xato?</p>",
      ["へ har doim [e]", "Qoʻshimcha boʻlganda [e] deb oʻqiladi",
       "へ oʻqilmaydi", "へ katakanaga tegishli"],
      "Qoʻshimcha boʻlganda [e] deb oʻqiladi",
      "<p>Soʻz ichida へ oddiy «he» boʻlib qoladi. Faqat "
      "<strong>qoʻshimcha</strong> sifatida [e] boʻladi — は va を bilan "
      "aynan bir xil hodisa.</p>"),
    q(f"<p>«Har kuni avtobusda maktabga boraman» — nechta で bor?</p>",
      ["Bitta", "Ikkita", "Uchta", "Hech qanday"], "Bitta",
      f"<p><strong>Bitta</strong>: «バスで» — vosita. Maktab bu yerda "
      f"<strong>yoʻnalish</strong>, shuning uchun に yoki へ oladi, で emas.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>公園<rt>こうえん</rt></ruby>___<ruby>友達<rt>ともだち</rt></ruby>と<ruby>話<rt>はな</rt></ruby>します。</strong></p>",
      ["に", "で", "へ", "まで"], "で",
      "<p><strong>で</strong> — gaplashish harakat, bogʻ esa ish bajarilayotgan "
      "joy.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {GK}へ<ruby>何<rt>なに</rt></ruby>で{IK}か。</strong></p>"
      f"<p><strong>B: ___。</strong></p>",
      ["バスに<ruby>行<rt>い</rt></ruby>きます", f"バスで{IK}",
       "バスへ<ruby>行<rt>い</rt></ruby>きます", "バスを<ruby>行<rt>い</rt></ruby>きます"],
      f"バスで{IK}",
      "<p>Savol «<ruby>何<rt>なに</rt></ruby>で» — vosita soʻralyapti, demak "
      "javob ham <strong>で</strong> bilan.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{IK} · バスで · {GK}へ · <ruby>毎日<rt>まいにち</rt></ruby></strong></p>",
      [f"<ruby>毎日<rt>まいにち</rt></ruby>バスで{GK}へ{IK}",
       f"バスで<ruby>毎日<rt>まいにち</rt></ruby>{IK}{GK}へ",
       f"{GK}へバスで{IK}<ruby>毎日<rt>まいにち</rt></ruby>",
       f"{IK}<ruby>毎日<rt>まいにち</rt></ruby>バスで{GK}へ"],
      f"<ruby>毎日<rt>まいにち</rt></ruby>バスで{GK}へ{IK}",
      "<p>Vaqt → vosita → yoʻnalish → feʼl. Feʼl <strong>oxirida</strong>.</p>"),
]


Q_PJ23 = [
    q(f"<p>{TB} ning oʻtgan zamoni qaysi?</p>",
      ["<ruby>食<rt>た</rt></ruby>べました", "<ruby>食<rt>た</rt></ruby>べませんでした",
       "<ruby>食<rt>た</rt></ruby>べます", "<ruby>食<rt>た</rt></ruby>べでした"],
      "<ruby>食<rt>た</rt></ruby>べました",
      "<p><strong>ます → ました</strong>. Istisno yoʻq — hamma feʼl uchun "
      "bitta qoida.</p>"),
    q("<p>«Bormadim» ni tanlang.</p>",
      ["<ruby>行<rt>い</rt></ruby>きませんでした", "<ruby>行<rt>い</rt></ruby>きました",
       "<ruby>行<rt>い</rt></ruby>きません", "<ruby>行<rt>い</rt></ruby>きませんした"],
      "<ruby>行<rt>い</rt></ruby>きませんでした",
      "<p><strong>ません</strong> (inkor) + <strong>でした</strong> (oʻtgan). "
      "«ませんした» degan shakl yoʻq — でした toʻliq boʻlak.</p>"),
    q("<p>です ning oʻtgan shakli qaysi?</p>",
      ["でした", "ですた", "でしません", "ではありません"], "でした",
      "<p><strong>でした</strong> — «…edi». Oʻtgan inkor esa "
      "<strong>ではありませんでした</strong>.</p>"),
    q("<p>Yapon tilida nechta zamon bor?</p>",
      ["Uchta: oʻtgan, hozirgi, kelasi", "Ikkita: oʻtgan va oʻtmagan",
       "Toʻrtta", "Bitta"],
      "Ikkita: oʻtgan va oʻtmagan",
      "<p>Kelasi zamon alohida shaklga ega emas — uni <strong>vaqt "
      "soʻzi</strong> koʻrsatadi. Shuning uchun «zamon» oʻrniga «oʻtgan / "
      "oʻtmagan» deb oʻylash toʻgʻriroq.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KN}<ruby>映画<rt>えいが</rt></ruby>を___。</strong></p>",
      ["<ruby>見<rt>み</rt></ruby>ます", "<ruby>見<rt>み</rt></ruby>ました",
       "<ruby>見<rt>み</rt></ruby>ません", "<ruby>見<rt>み</rt></ruby>でした"],
      "<ruby>見<rt>み</rt></ruby>ました",
      f"<p>{KN} («kecha») — oʻtgan zamon vaqt soʻzi, demak feʼl ham oʻtgan "
      f"zamonda.</p>"),
    q("<p>«Oʻtgan yil» qanday aytiladi?</p>",
      ["<ruby>先年<rt>せんねん</rt></ruby>", "<ruby>去年<rt>きょねん</rt></ruby>",
       "<ruby>昨年<rt>さくねん</rt></ruby>だけ", "<ruby>先月<rt>せんげつ</rt></ruby>"],
      "<ruby>去年<rt>きょねん</rt></ruby>",
      "<p><strong><ruby>去年<rt>きょねん</rt></ruby></strong>. "
      "<ruby>先<rt>せん</rt></ruby> faqat hafta va oy bilan ishlaydi "
      "(<ruby>先週<rt>せんしゅう</rt></ruby>, <ruby>先月<rt>せんげつ</rt></ruby>), "
      "yil bilan emas.</p>"),
    q("<p>あります ning oʻtgan shakli qaysi?</p>",
      ["ありました", "いました", "ありませんでした", "ありでした"], "ありました",
      "<p><strong>ありました</strong> — «bor edi». Jonli narsa uchun esa "
      "<strong>いました</strong>. Jonli/jonsiz farqi oʻtgan zamonda ham "
      "saqlanadi.</p>"),
    q(f"<p>{KN} ga に qoʻyiladimi?</p>",
      ["Ha", "Yoʻq — u oʻzi vaqtni bildiradi", "Faqat inkorda", "Faqat savolda"],
      "Yoʻq — u oʻzi vaqtni bildiradi",
      f"<p>{KN}, <ruby>明日<rt>あした</rt></ruby>, "
      f"<ruby>毎日<rt>まいにち</rt></ruby> ga に qoʻyilmaydi (PJ-21). "
      f"に faqat <strong>son bilan</strong> aytilgan vaqtga.</p>"),
    q("<p>Nega yaponcha oʻtgan zamon oson?</p>",
      ["Kam ishlatiladi", "Feʼl oʻzagi qimirlamaydi, faqat qoʻshimcha almashadi",
       "Faqat yozuvda ishlatiladi", "Uchta shakli bor"],
      "Feʼl oʻzagi qimirlamaydi, faqat qoʻshimcha almashadi",
      "<p>Yapon feʼli <strong>agglutinativ</strong> — oʻzak qimirlamaydi, "
      "qoʻshimchalar ketma-ket yopishadi. Oʻzbekchadagi «bor-ma-di-m» bilan "
      "bir xil mantiq.</p>"),
    q("<p>«Yakshanba edi» ni tanlang.</p>",
      ["<ruby>日曜日<rt>にちようび</rt></ruby>です", "<ruby>日曜日<rt>にちようび</rt></ruby>でした",
       "<ruby>日曜日<rt>にちようび</rt></ruby>ました", "<ruby>日曜日<rt>にちようび</rt></ruby>ませんでした"],
      "<ruby>日曜日<rt>にちようび</rt></ruby>でした",
      "<p>Kesim uchun <strong>でした</strong>, feʼl uchun ました. Ikkalasi "
      "ham でした/ました boʻlagini ishlatadi.</p>"),
    q("<p>います ning oʻtgan inkori qaysi?</p>",
      ["いませんでした", "ありませんでした", "いました", "いでした"],
      "いませんでした",
      "<p>ません + でした. Jonsiz narsa uchun esa "
      "<strong>ありませんでした</strong>.</p>"),
    q("<p>«…emas edi» ni tanlang.</p>",
      ["ではありません", "ではありませんでした", "でしたではない", "ませんでした"],
      "ではありませんでした",
      "<p><strong>ではありません + でした</strong>. Uzun koʻrinadi, lekin u "
      "shunchaki ikki boʻlakning qoʻshilishi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>先週<rt>せんしゅう</rt></ruby>{GK}へ___。</strong></p>",
      [IK, "<ruby>行<rt>い</rt></ruby>きました",
       "<ruby>行<rt>い</rt></ruby>きません", "<ruby>行<rt>い</rt></ruby>きましょう"],
      "<ruby>行<rt>い</rt></ruby>きました",
      "<p><ruby>先週<rt>せんしゅう</rt></ruby> («oʻtgan hafta») oʻtgan zamon "
      "talab qiladi.</p>"),
    q("<p>Savol yasash usuli oʻtgan zamonda oʻzgaradimi?</p>",
      ["Ha, boshqa qoʻshimcha kerak", "Yoʻq — か oʻsha joyda qoladi",
       "Ha, ohang koʻtariladi", "Savol yasab boʻlmaydi"],
      "Yoʻq — か oʻsha joyda qoladi",
      "<p>«<ruby>行<rt>い</rt></ruby>きました<strong>か</strong>» — gap "
      "oxiriga か, xuddi hozirgi zamondagi kabi.</p>"),
    q("<p>Qaysi shakl <strong>notoʻgʻri</strong>?</p>",
      ["<ruby>行<rt>い</rt></ruby>きました", "<ruby>行<rt>い</rt></ruby>きませんでした",
       "<ruby>行<rt>い</rt></ruby>きませんした", "<ruby>行<rt>い</rt></ruby>きません"],
      "<ruby>行<rt>い</rt></ruby>きませんした",
      "<p><strong>でした</strong> toʻliq boʻlak — «した» ga qisqartirib "
      "boʻlmaydi.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{KN}<ruby>行<rt>い</rt></ruby>きました", f"{KN}に<ruby>行<rt>い</rt></ruby>きました",
       f"<ruby>七時<rt>しちじ</rt></ruby>に<ruby>起<rt>お</rt></ruby>きました",
       "<ruby>先月<rt>せんげつ</rt></ruby><ruby>買<rt>か</rt></ruby>いました"],
      f"{KN}に<ruby>行<rt>い</rt></ruby>きました",
      f"<p>{KN} ga に qoʻyilmaydi — u oʻzi vaqtni bildiradi.</p>"),
    q("<p><ruby>一昨日<rt>おととい</rt></ruby> nima degani?</p>",
      ["Kecha", "Avvalgi kun", "Ertaga", "Oʻtgan hafta"], "Avvalgi kun",
      "<p><strong><ruby>一昨日<rt>おととい</rt></ruby></strong> — kechadan "
      "oldingi kun.</p>"),
    q("<p>«Uchrashdim» ni tanlang.</p>",
      ["<ruby>会<rt>あ</rt></ruby>いました", "<ruby>会<rt>あ</rt></ruby>います",
       "<ruby>会<rt>あ</rt></ruby>いませんでした", "<ruby>会<rt>あ</rt></ruby>でした"],
      "<ruby>会<rt>あ</rt></ruby>いました",
      "<p><ruby>会<rt>あ</rt></ruby>います → <ruby>会<rt>あ</rt></ruby>いました. "
      "Oʻsha bitta qoida.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {KN}{BK}か。</strong></p>"
      f"<p><strong>B: いいえ、___。</strong></p>",
      ["しました", "しませんでした", "しません", "しませんした"],
      "しませんでした",
      "<p>いいえ + oʻtgan zamon = <strong>しませんでした</strong>. Savol "
      "oʻtgan zamonda berilgan, javob ham shunday boʻlishi kerak.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong><ruby>見<rt>み</rt></ruby>ました · を · {KN} · <ruby>映画<rt>えいが</rt></ruby></strong></p>",
      [f"{KN}<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ました",
       f"<ruby>映画<rt>えいが</rt></ruby>を{KN}<ruby>見<rt>み</rt></ruby>ました",
       f"{KN}を<ruby>映画<rt>えいが</rt></ruby><ruby>見<rt>み</rt></ruby>ました",
       f"<ruby>見<rt>み</rt></ruby>ました{KN}<ruby>映画<rt>えいが</rt></ruby>を"],
      f"{KN}<ruby>映画<rt>えいが</rt></ruby>を<ruby>見<rt>み</rt></ruby>ました",
      "<p>Vaqt → toʻldiruvchi → feʼl. Feʼl oxirida.</p>"),
]


Q_PJ24 = [
    q("<p>Soat 4 qanday aytiladi?</p>",
      ["よんじ", "よじ", "しじ", "しちじ"], "よじ",
      "<p><strong>よじ</strong>. Na «よんじ», na «しじ». Oylarda 4 «し» edi "
      "(<ruby>四月<rt>しがつ</rt></ruby>), soatda esa «よ» — har sanoq soʻzi "
      "bilan alohida yodlanadi.</p>"),
    q("<p>Soat 9 qanday aytiladi?</p>",
      ["きゅうじ", "くじ", "ここのじ", "きゅじ"], "くじ",
      "<p><strong>くじ</strong> — oylardagi <ruby>九月<rt>くがつ</rt></ruby> "
      "bilan bir xil.</p>"),
    q(f"<p>«Toʻqqizdan beshgacha» ni tanlang.</p>",
      [f"{KJ}から{GJ}まで", f"{KJ}に{GJ}まで",
       f"{KJ}から{GJ}に", f"{KJ}まで{GJ}から"],
      f"{KJ}から{GJ}まで",
      "<p><strong>から … まで</strong> — «…dan …gacha». に qoʻshilmaydi.</p>"),
    q("<p>«Yarim» qanday aytiladi?</p>",
      ["<ruby>半<rt>はん</rt></ruby>", "<ruby>分<rt>ふん</rt></ruby>",
       "<ruby>半分<rt>はんぶん</rt></ruby>だけ", "<ruby>時<rt>じ</rt></ruby>"],
      "<ruby>半<rt>はん</rt></ruby>",
      "<p><strong><ruby>七時半<rt>しちじはん</rt></ruby></strong> = «yetti "
      "yarim». <ruby>三十分<rt>さんじゅっぷん</rt></ruby> deyishdan ancha "
      "qulayroq va yaponlar deyarli doim shuni ishlatadi.</p>"),
    q(f"<p>{GY} ga に qoʻyiladimi?</p>",
      ["Ha — hafta kuni aniq nuqta", "Yoʻq", "Faqat inkorda", "Faqat savolda"],
      "Ha — hafta kuni aniq nuqta",
      "<p>Qoida oʻzgarmadi: <strong>aniq</strong> vaqtga に qoʻyiladi. "
      "<ruby>毎週<rt>まいしゅう</rt></ruby> esa oʻzi vaqtni bildiradi va "
      "に olmaydi.</p>"),
    q("<p><ruby>毎週<rt>まいしゅう</rt></ruby> ga に qoʻyiladimi?</p>",
      ["Ha", "Yoʻq", "Faqat oʻtgan zamonda", "Faqat kelasi zamonda"], "Yoʻq",
      "<p><ruby>毎日<rt>まいにち</rt></ruby> kabi — oʻzi vaqtni bildiradi. "
      "<strong>Son bor — に bor, son yoʻq — に yoʻq.</strong></p>"),
    q("<p>から va まで faqat vaqt bilan ishlaydimi?</p>",
      ["Ha", "Yoʻq — joy bilan ham", "Faqat hafta kunlari bilan", "Faqat soat bilan"],
      "Yoʻq — joy bilan ham",
      f"<p>{IE}から{GK}まで — «uydan maktabgacha». Ular oraliqni bildiradi, "
      f"oraliq esa vaqtda ham, fazoda ham boʻladi.</p>"),
    q("<p><ruby>午前<rt>ごぜん</rt></ruby> nima degani?</p>",
      ["Tushdan keyin", "Tushdan oldin", "Kechqurun", "Yarim tun"],
      "Tushdan oldin",
      "<p><strong><ruby>午前<rt>ごぜん</rt></ruby></strong> — tushdan oldin, "
      "<strong><ruby>午後<rt>ごご</rt></ruby></strong> — tushdan keyin. "
      "Ikkalasi ham soatdan <strong>oldin</strong> turadi.</p>"),
    q("<p>«Soat necha?» qanday soʻraladi?</p>",
      ["<ruby>何時<rt>なにじ</rt></ruby>", "<ruby>何時<rt>なんじ</rt></ruby>",
       "<ruby>何<rt>なに</rt></ruby>の<ruby>時<rt>じ</rt></ruby>", "いつじ"],
      "<ruby>何時<rt>なんじ</rt></ruby>",
      "<p><strong>なんじ</strong> — sanoq soʻzi bilan doim <strong>なん</strong> "
      "(PJ-18).</p>"),
    q("<p>10 daqiqa qanday oʻqiladi?</p>",
      ["じゅうふん", "じゅっぷん", "とおふん", "じゅうぷん"], "じゅっぷん",
      "<p><strong>じゅっぷん</strong> — daqiqada tovush oʻzgaradi: ふん → ぷん. "
      "Bu PJ-12 dagi ひゃく → ぴゃく bilan bir xil hodisa.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KJ}___<ruby>始<rt>はじ</rt></ruby>まります。</strong></p>",
      ["から", "に", "まで", "で"], "に",
      "<p><strong>に</strong> — yolgʻiz turgan aniq vaqt. Agar «<ruby>九時<rt>くじ</rt></ruby>"
      "<strong>から</strong>» boʻlsa, から oʻzi munosabatni bildiradi va に "
      "kerak boʻlmaydi.</p>"),
    q("<p>から yolgʻiz ishlatilishi mumkinmi?</p>",
      ["Yoʻq — doim まで bilan juft", "Ha — «…dan boshlab»",
       "Faqat joy bilan", "Faqat savolda"],
      "Ha — «…dan boshlab»",
      "<p>«<ruby>九時<rt>くじ</rt></ruby>から<ruby>始<rt>はじ</rt></ruby>まります» — "
      "«toʻqqizdan boshlanadi». まで ham yolgʻiz turishi mumkin.</p>"),
    q("<p>Soat 7 qanday aytiladi?</p>",
      ["ななじ", "しちじ", "なのじ", "しじ"], "しちじ",
      "<p><strong>しちじ</strong> — oylardagi <ruby>七月<rt>しちがつ</rt></ruby> "
      "bilan bir xil.</p>"),
    q(f"<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{KJ}から{GJ}まで<ruby>働<rt>はたら</rt></ruby>きます",
       f"{KJ}から{GJ}までに<ruby>働<rt>はたら</rt></ruby>きます",
       f"{GY}に{IK}", f"{KJ}に<ruby>始<rt>はじ</rt></ruby>まります"],
      f"{KJ}から{GJ}までに<ruby>働<rt>はたら</rt></ruby>きます",
      "<p>から va まで <strong>oʻzi</strong> vaqt munosabatini bildiradi — "
      "に ortiqcha.</p>"),
    q("<p>Qaysi oʻqilish <strong>notoʻgʻri</strong>?</p>",
      ["<ruby>四時<rt>よじ</rt></ruby>", "<ruby>七時<rt>しちじ</rt></ruby>",
       "<ruby>九時<rt>きゅうじ</rt></ruby>", "<ruby>十時<rt>じゅうじ</rt></ruby>"],
      "<ruby>九時<rt>きゅうじ</rt></ruby>",
      "<p>Soat 9 — <strong>くじ</strong>, «きゅうじ» emas.</p>"),
    q("<p>Kunning qismlariga に qoʻyiladimi?</p>",
      ["Ha, har doim", "Yoʻq — <ruby>朝<rt>あさ</rt></ruby>, <ruby>夜<rt>よる</rt></ruby> oʻzi vaqtni bildiradi",
       "Faqat <ruby>朝<rt>あさ</rt></ruby> ga", "Faqat <ruby>夜<rt>よる</rt></ruby> ga"],
      "Yoʻq — <ruby>朝<rt>あさ</rt></ruby>, <ruby>夜<rt>よる</rt></ruby> oʻzi vaqtni bildiradi",
      "<p>«<ruby>朝<rt>あさ</rt></ruby>コーヒーを<ruby>飲<rt>の</rt></ruby>みます» — に "
      "yoʻq. Qoida: <strong>son bor — に bor</strong>.</p>"),
    q(f"<p>«Dushanbadan jumagacha» ni tanlang.</p>",
      [f"{GY}から<ruby>金曜日<rt>きんようび</rt></ruby>まで",
       f"{GY}に<ruby>金曜日<rt>きんようび</rt></ruby>まで",
       f"{GY}から<ruby>金曜日<rt>きんようび</rt></ruby>に",
       f"{GY}まで<ruby>金曜日<rt>きんようび</rt></ruby>から"],
      f"{GY}から<ruby>金曜日<rt>きんようび</rt></ruby>まで",
      "<p>から … まで hafta kunlari bilan ham ishlaydi, va に qoʻshilmaydi.</p>"),
    q("<p>1 daqiqa qanday oʻqiladi?</p>",
      ["いちふん", "いっぷん", "ひとふん", "いちぷん"], "いっぷん",
      "<p><strong>いっぷん</strong> — kichik っ va ぷん. Daqiqada tovush "
      "oʻzgarishlari koʻp, shuning uchun ularni yodlab qoʻyish kerak.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: <ruby>何時<rt>なんじ</rt></ruby>から<ruby>何時<rt>なんじ</rt></ruby>まで{BK}か。</strong></p>"
      f"<p><strong>B: ___。</strong></p>",
      [f"{KJ}に{GJ}まで", f"{KJ}から{GJ}まで",
       f"{KJ}まで{GJ}から", f"{KJ}で{GJ}まで"],
      f"{KJ}から{GJ}まで",
      "<p>Savol «から…まで» shaklida — javob ham shunday boʻlishi kerak.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong><ruby>働<rt>はたら</rt></ruby>きます · {GJ}まで · {KJ}から · <ruby>毎日<rt>まいにち</rt></ruby></strong></p>",
      [f"<ruby>毎日<rt>まいにち</rt></ruby>{KJ}から{GJ}まで<ruby>働<rt>はたら</rt></ruby>きます",
       f"{KJ}から<ruby>毎日<rt>まいにち</rt></ruby>{GJ}まで<ruby>働<rt>はたら</rt></ruby>きます",
       f"<ruby>働<rt>はたら</rt></ruby>きます<ruby>毎日<rt>まいにち</rt></ruby>{KJ}から{GJ}まで",
       f"{GJ}まで{KJ}から<ruby>毎日<rt>まいにち</rt></ruby><ruby>働<rt>はたら</rt></ruby>きます"],
      f"<ruby>毎日<rt>まいにち</rt></ruby>{KJ}から{GJ}まで<ruby>働<rt>はたら</rt></ruby>きます",
      "<p>Umumiy vaqt → oraliq boshi → oraliq oxiri → feʼl.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-22 Mashq: で va へ",
        "description": "20 savol — に/で farqi, で ning vosita maʼnosi, へ ning oʻqilishi.",
        "tutorial":    "PJ-22:",
        "level":       "easy",
        "questions":   Q_PJ22,
    },
    {
        "title":       "PJ-23 Mashq: 〜ました / 〜ませんでした",
        "description": "20 savol — oʻtgan zamon, oʻtgan inkor, でした va vaqt soʻzlari.",
        "tutorial":    "PJ-23:",
        "level":       "easy",
        "questions":   Q_PJ23,
    },
    {
        "title":       "PJ-24 Mashq: Vaqt — soat, hafta kunlari, から〜まで",
        "description": "20 savol — soatning istisnolari, daqiqa, から〜まで va に qoidasi.",
        "tutorial":    "PJ-24:",
        "level":       "easy",
        "questions":   Q_PJ24,
    },
]
