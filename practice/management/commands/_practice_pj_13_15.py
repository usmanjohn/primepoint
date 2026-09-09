# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-13 … PJ-15 (birinchi gaplar).

PJ-13 dan boshlab testlar 20 savoldan iborat (yozuv bloki 12 savol edi).
Written with STYLE_GUIDE_PJ_PRACTICE.md · lesson list in toc_pj_practices.txt.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_13_15.py --master=prime \\
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

W  = "<ruby>私<rt>わたし</rt></ruby>"
G  = "<ruby>学生<rt>がくせい</rt></ruby>"
SE = "<ruby>先生<rt>せんせい</rt></ruby>"
NJ = "<ruby>日本人<rt>にほんじん</rt></ruby>"
DA = "<ruby>誰<rt>だれ</rt></ruby>"
HO = "<ruby>本<rt>ほん</rt></ruby>"
YA = "<ruby>山田<rt>やまだ</rt></ruby>"
TO = "<ruby>時計<rt>とけい</rt></ruby>"
NN = "<ruby>何<rt>なん</rt></ruby>"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


Q_PJ13 = [
    # 1-5 tanish
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{W}は{G}___。</strong></p>",
      ["です", "ですか", "ではありません", "さん"], "です",
      f"<p><strong>です</strong> — «…dir». Bu gap oddiy xabar: «Men talabaman». "
      f"ですか savol yasardi, ではありません esa inkor qilardi.</p>"),
    q("<p>です qanday oʻqiladi?</p>",
      ["[desu]", "[des]", "[dezu]", "[de]"], "[des]",
      "<p><strong>[des]</strong> — soʻz oxiridagi す dagi «u» jarangsiz undosh "
      "yonida ovozini yoʻqotadi (PJ-2). Yozilishi です, oʻqilishi [des].</p>"),
    q("<p>Gapni savolga aylantirish uchun nima qilinadi?</p>",
      ["Soʻz tartibi oʻzgartiriladi", "Gap oxiriga か qoʻshiladi",
       "Ohang koʻtariladi", "です olib tashlanadi"], "Gap oxiriga か qoʻshiladi",
      "<p>Faqat <strong>か</strong> qoʻshiladi. Soʻz tartibi oʻzgarmaydi va ohang "
      "koʻtarilmaydi — bu ingliz tilidan katta farq. Savol belgisi ham odatda "
      "qoʻyilmaydi, chunki か ning oʻzi savolni bildiradi.</p>"),
    q("<p>です shaxsga qarab oʻzgaradimi?</p>",
      ["Ha, har shaxs uchun boshqa shakl", "Yoʻq, hamma shaxs uchun bitta shakl",
       "Faqat koʻplikda oʻzgaradi", "Faqat savolda oʻzgaradi"],
      "Yoʻq, hamma shaxs uchun bitta shakl",
      "<p><strong>Oʻzgarmaydi.</strong> Oʻzbekchada kesim oʻzgaradi "
      "(«talabaman / talabasan»), yaponchada esa です hamma uchun bitta. "
      "Yapon feʼllari umuman shaxsga qarab tuslanmaydi.</p>"),
    q(f"<p>«Men Afsonaman» ni tanlang.</p>",
      [f"{W}はアフソナです", f"{W}がアフソナです",
       f"アフソナは{W}です", f"{W}アフソナです"], f"{W}はアフソナです",
      f"<p><strong>{W}はアフソナです</strong> — oddiy tanishuv uchun は. "
      f"が bilan «boshqa emas, aynan men!» degan maʼno chiqadi, "
      f"qoʻshimchasiz esa gap grammatik jihatdan toʻliq emas.</p>"),
    # 6-12 qoʻllash
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{W}は{SE}___。{G}です。</strong></p>",
      ["です", "ではありません", "ですか", "じゃ"], "ではありません",
      f"<p><strong>ではありません</strong> — «emas». Ikkinchi gap «{G}です» "
      f"boʻlgani uchun birinchisi inkor boʻlishi kerak: «Men oʻqituvchi emasman. "
      f"Talabaman».</p>"),
    q("<p>では qanday oʻqiladi?</p>",
      ["[deha]", "[dewa]", "[dega]", "[deba]"], "[dewa]",
      "<p><strong>[dewa]</strong> — は grammatik qoʻshimcha boʻlgani uchun [wa] "
      "boʻlib oʻqiladi. Kundalik nutqda u qisqarib <strong>じゃ</strong> boʻladi, "
      "shundan じゃありません shakli chiqqan.</p>"),
    q("<p>ではありません ning kundalik shakli qaysi?</p>",
      ["じゃありません", "でわありません", "ではあります", "ではありましたか"],
      "じゃありません",
      "<p><strong>じゃありません</strong>. では tez gapirganda じゃ ga qisqaradi. "
      "Maʼnosi bir xil, uslubi kundalikroq.</p>"),
    q(f"<p>«{G}ですか» savoliga tasdiq javob qaysi?</p>",
      ["はい、そうです", "いいえ、ちがいます", "はい、ちがいます", "いいえ、そうです"],
      "はい、そうです",
      "<p><strong>はい、そうです</strong> — «ha, shunday». Inkor javob "
      "«いいえ、ちがいます». Bu ikkalasi universal: soʻralgan soʻzni takrorlamasdan "
      "qisqa javob berasiz.</p>"),
    q("<p>ちがいます nima degani?</p>",
      ["Ha, shunday", "Yoʻq, boshqacha", "Bilmayman", "Kechirasiz"],
      "Yoʻq, boshqacha",
      "<p><strong>«Yoʻq, boshqacha»</strong> — いいえ bilan birga ishlatiladigan "
      "inkor javob. そうです esa «shunday».</p>"),
    q("<p>さん qoʻshimchasi qayerda ishlatiladi?</p>",
      ["Oʻz ismiga", "Boshqa odamning ismiga", "Har qanday otga", "Faqat familiyaga"],
      "Boshqa odamning ismiga",
      "<p><strong>Boshqa odamga.</strong> Oʻz ismingizga さん qoʻshish — «men "
      "hurmatli Afsonaman» degandek eshitiladi. Oʻzingiz haqingizda doim "
      "さん siz gapirasiz.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>アフソナさん___{NJ}ですか。</strong></p>",
      ["は", "が", "の", "か"], "は",
      "<p><strong>は</strong> — mavzu qoʻshimchasi. «Afsonaga kelsak, u yaponmi?» "
      "Bu oddiy savol, «kim aynan» degan savol emas, shuning uchun が emas.</p>"),
    # 13-16 farqlash
    q("<p>Qaysi gap <strong>savol</strong>?</p>",
      [f"{G}です", f"{G}ですか", f"{G}ではありません", f"{G}でした"],
      f"{G}ですか",
      "<p><strong>か</strong> gap oxirida — bu savol belgisi. Qolganlari: "
      "xabar, inkor va oʻtgan zamon.</p>"),
    q("<p>Qaysi juftlik toʻgʻri moslashgan?</p>",
      ["です — inkor", "ではありません — tasdiq", "か — savol", "さん — oʻz ismiga"],
      "か — savol",
      "<p><strong>か — savol</strong>. です tasdiq, ではありません inkor, "
      "さん esa faqat boshqa odamning ismiga qoʻshiladi.</p>"),
    q(f"<p>«{W}は» nega koʻpincha tushirib qoldiriladi?</p>",
      ["Grammatik xato boʻlgani uchun", "Kontekstdan kim gapirayotgani aniq boʻlgani uchun",
       "Juda uzun boʻlgani uchun", "Faqat yozuvda ishlatilgani uchun"],
      "Kontekstdan kim gapirayotgani aniq boʻlgani uchun",
      f"<p>Kim haqida gapirilayotgani aniq boʻlsa, mavzuni takrorlash "
      f"<strong>ortiqcha</strong> sanaladi. «{G}です» ning oʻzi «Talabaman» "
      f"degan maʼnoni beradi.</p>"),
    q("<p>あなた soʻzi haqida qaysi gap toʻgʻri?</p>",
      ["Har doim ishlatiladi", "Yaponlar uni kam ishlatadi va ism bilan almashtiradi",
       "Faqat rasmiy nutqda", "Faqat yozuvda"],
      "Yaponlar uni kam ishlatadi va ism bilan almashtiradi",
      "<p>Yaponlar «siz» oʻrniga odamning <strong>ismini</strong> aytadi: "
      "«アフソナさんは…». あなた ni koʻp ishlatish gʻalati eshitiladi.</p>"),
    # 17-18 xato topish
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{W}は{G}です", f"{W}は{G}は です",
       f"{W}は{G}ではありません", f"{G}ですか"],
      f"{W}は{G}は です",
      "<p>は gapda <strong>bir marta</strong>, mavzudan keyin turadi. Ikkinchi は "
      "ortiqcha va gapni buzadi.</p>"),
    q("<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
      [f"{YA}さんは{SE}です", f"{W}はアフソナさんです",
       f"{W}はアフソナです", f"{YA}さんは{G}ではありません"],
      f"{W}はアフソナさんです",
      "<p>Oʻz ismiga <strong>さん qoʻshilmaydi</strong>. Toʻgʻrisi: "
      f"«{W}はアフソナです».</p>"),
    # 19-20 tuzish
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>です · は · {G} · {W}</strong></p>",
      [f"{W}は{G}です", f"{G}は{W}です",
       f"です{W}は{G}", f"は{W}{G}です"], f"{W}は{G}です",
      f"<p><strong>{W}は{G}です</strong> — mavzu, keyin kesim, oxirida です. "
      f"Yapon gapi doim kesim bilan tugaydi.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {NJ}ですか。</strong></p>"
      f"<p><strong>B: いいえ、___。</strong></p>",
      [f"{NJ}です", f"{NJ}ではありません",
       f"{NJ}ですか", "そうです"], f"{NJ}ではありません",
      "<p>いいえ bilan boshlangan javob <strong>inkor</strong> boʻlishi kerak. "
      "«いいえ、そうです» yoki «いいえ、…です» mantiqsiz chiqadi.</p>"),
]


# ── PJ-14 ────────────────────────────────────────────────────────────
Q_PJ14 = [
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{DA}___{SE}ですか。</strong></p>",
      ["は", "が", "の", "も"], "が",
      f"<p><strong>が</strong>. Savol soʻzi bilan <strong>doim が</strong> — "
      f"«{DA}は» degan birikma yapon tilida mavjud emas.</p>"),
    q("<p>は qanday vazifa bajaradi?</p>",
      ["Egani belgilaydi", "Mavzuni belgilaydi — «nima haqida gapiryapmiz»",
       "Toʻldiruvchini belgilaydi", "Savol yasaydi"],
      "Mavzuni belgilaydi — «nima haqida gapiryapmiz»",
      "<p><strong>Mavzu</strong> qoʻshimchasi. Koʻpincha «…ga kelsak» deb "
      "tarjima qilish mumkin: «Afsonaga kelsak — u talaba».</p>"),
    q("<p>が qanday vazifa bajaradi?</p>",
      ["Mavzuni belgilaydi", "Egani belgilaydi — «aynan kim»",
       "Gapni bogʻlaydi", "Inkor qiladi"],
      "Egani belgilaydi — «aynan kim»",
      "<p><strong>Ega</strong> qoʻshimchasi. U yangi yoki ajratilgan maʼlumotni "
      "koʻrsatadi va «kim aynan?» degan savolga javob beradi.</p>"),
    q("<p>Nega savol soʻzi mavzu boʻla olmaydi?</p>",
      ["Juda qisqa boʻlgani uchun", "Mavzu maʼlum narsa boʻlishi kerak, savol soʻzi esa nomaʼlumni soʻraydi",
       "Grammatik istisno", "は faqat otlar bilan ishlaydi"],
      "Mavzu maʼlum narsa boʻlishi kerak, savol soʻzi esa nomaʼlumni soʻraydi",
      "<p>Mavzu — <strong>maʼlum</strong> narsa: «Afsona haqida gapiraylik» "
      "deyish uchun Afsona kimligini bilish kerak. Savol soʻzi esa aynan "
      "<strong>nomaʼlum</strong> narsani soʻraydi. Butun qoidaning sababi shu.</p>"),
    q(f"<p>«{DA}が{SE}ですか» savoliga toʻgʻri javob qaysi?</p>",
      [f"{YA}さんは{SE}です", f"{YA}さんが{SE}です",
       f"{SE}は{YA}さんです", f"{YA}さんの{SE}です"],
      f"{YA}さんが{SE}です",
      "<p>Savol soʻziga javobda ham <strong>が saqlanadi</strong>: «aynan "
      "Yamada». は bilan javob savolga toʻgʻri kelmaydi.</p>"),
    q(f"<p>«{W}が{G}です» qanday eshitiladi?</p>",
      ["Oddiy tanishuv", "«Aynan men talabaman» — boshqasi emas",
       "«Men talaba emasman»", "«Men talabami?»"],
      "«Aynan men talabaman» — boshqasi emas",
      "<p>が <strong>ajratadi</strong>: «boshqa emas, men». Bu «Kim talaba?» "
      "degan savolga javob. Oddiy tanishuvda は kerak.</p>"),
    q("<p>Bitta gapda ikkita は kelsa, u odatda nima maʼno beradi?</p>",
      ["Kuchaytirish", "Qarama-qarshi qoʻyish — «esa»", "Savol", "Inkor"],
      "Qarama-qarshi qoʻyish — «esa»",
      "<p><strong>Qarama-qarshi qoʻyish.</strong> «Yamada oʻqituvchi. Afsona "
      "<em>esa</em> talaba» — ikkita は ikkita mavzuni yonma-yon qoʻyadi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HO}___あります。</strong></p>",
      ["は", "が", "の", "か"], "が",
      "<p><strong>が</strong>. <strong>あります</strong> va <strong>います</strong> "
      "bilan doim が ishlatiladi — bu が ning ikkinchi katta vazifasi: "
      "mavjudlikni bildirgan gapda egani belgilash.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p>"
      f"<p><strong><ruby>日本語<rt>にほんご</rt></ruby>___<ruby>好<rt>す</rt></ruby>きです。</strong></p>",
      ["を", "が", "は", "に"], "が",
      "<p><strong>が</strong>. Oʻzbekchada «yapon tili<em>ni</em> yoqtiraman» — "
      "toʻldiruvchi. Yaponchada esa <ruby>好<rt>す</rt></ruby>きです aslida sifat, "
      "shuning uchun yoqtirilgan narsa <strong>ega</strong> boʻlib が oladi.</p>"),
    q(f"<p>Qaysi gap oddiy tanishuv uchun toʻgʻri?</p>",
      [f"{W}がアフソナです", f"{W}はアフソナです",
       f"{W}のアフソナです", f"アフソナが{W}です"], f"{W}はアフソナです",
      "<p>Oddiy xabar uchun <strong>は</strong>. が bilan «boshqa emas, aynan "
      "men!» degan ajratuvchi maʼno chiqadi va gʻalati eshitiladi.</p>"),
    q("<p>あります va います bilan qaysi qoʻshimcha ishlatiladi?</p>",
      ["は", "が", "を", "の"], "が",
      "<p><strong>が</strong>. Bu qoliplarni PJ-16 da toʻliq koʻramiz, lekin "
      "qoida hozirdan aniq: mavjudlik gaplarida ega が oladi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>友達<rt>ともだち</rt></ruby>___います。</strong></p>",
      ["は", "を", "が", "に"], "が",
      "<p><strong>が</strong> — «doʻstim bor». います jonli narsalar uchun, "
      "あります jonsiz narsalar uchun ishlatiladi.</p>"),
    q(f"<p>Qaysi gapda が <strong>notoʻgʻri</strong> ishlatilgan?</p>",
      [f"{DA}が{SE}ですか", f"{W}がアフソナです（tanishuvda）",
       f"{HO}があります", f"{YA}さんが{SE}です（savolga javob）"],
      f"{W}がアフソナです（tanishuvda）",
      "<p>Oddiy tanishuvda が ishlatilmaydi — u «boshqa emas, men!» degan "
      "maʼno beradi. Qolgan uchtasida が oʻrinli: savol soʻzi, mavjudlik, "
      "savolga javob.</p>"),
    q("<p>Qaysi birikma yapon tilida <strong>mavjud emas</strong>?</p>",
      [f"{DA}が", f"{DA}は", f"{DA}の", f"{DA}ですか"], f"{DA}は",
      f"<p><strong>{DA}は</strong> mavjud emas. Savol soʻzi hech qachon mavzu "
      f"boʻla olmaydi, chunki mavzu maʼlum narsa boʻlishi kerak.</p>"),
    q("<p>Qaysi holatda は ishlatiladi?</p>",
      ["Savol soʻzi bilan", "Savolga javob berganda",
       "Oddiy xabar berganda", "あります bilan"],
      "Oddiy xabar berganda",
      "<p><strong>Oddiy xabar</strong> — は ning asosiy vazifasi. Qolgan uch "
      "holatda が ishlatiladi.</p>"),
    q("<p>Amaliy qoidaga koʻra, gapda savol soʻzi boʻlsa qaysi qoʻshimcha kerak?</p>",
      ["は", "が", "の", "Farqi yoʻq"], "が",
      "<p><strong>が</strong>, istisnosiz. Bu — は/が farqidagi eng ishonchli "
      "qoida va uni birinchi boʻlib yodlash kerak.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{DA}は{SE}ですか", f"{DA}が{SE}ですか",
       f"{YA}さんが{SE}です", f"{YA}さんは{SE}です"],
      f"{DA}は{SE}ですか",
      f"<p>Savol soʻzi bilan は ishlatilmaydi. Toʻgʻrisi: «{DA}が{SE}ですか».</p>"),
    q("<p>は ni oʻqishda eng koʻp uchraydigan xato qaysi?</p>",
      ["«ba» deb oʻqish", "«ha» deb oʻqish", "«wa» deb oʻqish", "Umuman oʻqimaslik"],
      "«ha» deb oʻqish",
      "<p>Qoʻshimcha boʻlganda は <strong>[wa]</strong> deb oʻqiladi. «ha» deb "
      "oʻqish — butun kursdagi eng koʻp uchraydigan oʻqish xatosi.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {DA}が{G}ですか。</strong></p>"
      f"<p><strong>B: ___{G}です。</strong></p>",
      [f"{W}は", f"{W}が", f"{W}の", f"{W}も"], f"{W}が",
      "<p>Savol soʻziga javobda <strong>が saqlanadi</strong>: «aynan men». "
      "は bilan javob berish savolga toʻgʻri kelmaydi.</p>"),
    q(f"<p>Ikki gapni qarama-qarshi qoʻying.</p>"
      f"<p><strong>{YA}さん___{SE}です。アフソナさん___{G}です。</strong></p>",
      ["が / が", "は / は", "が / は", "の / の"], "は / は",
      "<p>Ikkita <strong>は</strong> ikkita mavzuni yonma-yon qoʻyadi va "
      "oʻzbekchadagi «esa» ning ishini bajaradi.</p>"),
]


# ── PJ-15 ────────────────────────────────────────────────────────────
Q_PJ15 = [
    q("<p>Oʻz qoʻlingizdagi narsani qanday koʻrsatasiz?</p>",
      ["これ", "それ", "あれ", "どれ"], "これ",
      "<p><strong>これ</strong> — «menga yaqin». それ suhbatdoshga yaqin, "
      "あれ ikkalasidan ham uzoq.</p>"),
    q("<p>Suhbatdoshingiz ushlab turgan narsani qanday koʻrsatasiz?</p>",
      ["これ", "それ", "あれ", "どの"], "それ",
      "<p><strong>それ</strong> — «SENGA yaqin». Yaponchada masofa <strong>ikki "
      "kishiga</strong> nisbatan oʻlchanadi, va yaponlar bu farqni juda aniq "
      "his qiladi.</p>"),
    q("<p>Ikkalangizdan ham uzoqdagi narsa qanday koʻrsatiladi?</p>",
      ["これ", "それ", "あれ", "どれ"], "あれ",
      "<p><strong>あれ</strong> — «anavi», ikkalamizdan ham uzoq.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>___{HO}は{W}のです。</strong></p>",
      ["これ", "この", "ここ", "どれ"], "この",
      f"<p><strong>この</strong> — ortidan ot ({HO}) kelgani uchun. これ yolgʻiz "
      f"turadi va ortidan ot qabul qilmaydi.</p>"),
    q("<p>これ va この ni nima ajratadi?</p>",
      ["Masofa", "これ yolgʻiz turadi, この ortidan albatta ot talab qiladi",
       "これ rasmiy, この kundalik", "Hech narsa"],
      "これ yolgʻiz turadi, この ortidan albatta ot talab qiladi",
      "<p>Oxirgi boʻgʻinga qarang: <strong>れ</strong> — toʻliq soʻz, oʻzi "
      "yetadi. <strong>の</strong> — bogʻlovchi, ortidan nimadir kelishi "
      "shart.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>___は{HO}です。</strong></p>",
      ["この", "これ", "ここ", "どの"], "これ",
      f"<p><strong>これ</strong> — ortidan darrov は kelyapti, ot yoʻq. "
      f"«この は…» deb yozib boʻlmaydi.</p>"),
    q("<p>«Bu yer» qanday aytiladi?</p>",
      ["これ", "この", "ここ", "こちら"], "ここ",
      "<p><strong>ここ</strong> — joy. ko-so-a-do tizimida joy soʻzlari "
      "ここ・そこ・あそこ・どこ.</p>"),
    q("<p>«Qayer?» qanday aytiladi?</p>",
      ["どれ", "どの", "どこ", "どちら"], "どこ",
      "<p><strong>どこ</strong> — «qayer». どれ «qaysi biri», どの «qaysi…», "
      "どちら esa «ikkitadan qaysi biri».</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>どれ___{W}の{HO}ですか。</strong></p>",
      ["は", "が", "の", "も"], "が",
      "<p><strong>が</strong> — どれ savol soʻzi, savol soʻzi bilan doim が "
      "(PJ-14). «どれは» degan birikma mavjud emas.</p>"),
    q("<p>Faqat ikki narsadan birini tanlash kerak boʻlsa, qaysi soʻz ishlatiladi?</p>",
      ["どれ", "どの", "どちら", "どこ"], "どちら",
      "<p><strong>どちら</strong>. どれ uch va undan koʻp narsa orasidan "
      "tanlaganda ishlatiladi. Oʻzbekchada bunday farq yoʻq, shuning uchun "
      "buni alohida eslab qolish kerak.</p>"),
    q(f"<p>«Bu nima?» ni tanlang.</p>",
      [f"これは{NN}ですか", f"この{NN}ですか",
       f"これ{NN}ですか", f"ここは{NN}ですか"], f"これは{NN}ですか",
      f"<p><strong>これは{NN}ですか</strong> — doʻkonda eng koʻp kerak "
      f"boʻladigan gap. これ yolgʻiz turadi, keyin は, keyin savol.</p>"),
    q("<p>この · その · あの ning umumiy xususiyati nima?</p>",
      ["Ular yolgʻiz turadi", "Ular ortidan albatta ot keladi",
       "Ular faqat savol yasaydi", "Ular joyni bildiradi"],
      "Ular ortidan albatta ot keladi",
      "<p>Uchalasi ham <strong>の</strong> bilan tugaydi — bu bogʻlovchi, "
      "ortidan ot talab qiladi. これ・それ・あれ esa yolgʻiz turadi.</p>"),
    q("<p>ko-so-a-do tizimida boshlangʻich harf nimani bildiradi?</p>",
      ["Soʻz turkumini", "Masofani", "Hurmat darajasini", "Zamonni"],
      "Masofani",
      "<p><strong>Masofani</strong>: こ menga yaqin, そ senga yaqin, あ uzoq, "
      "ど savol. Qolgan qismi esa soʻzning turini bildiradi (narsa, ot bilan, joy).</p>"),
    q("<p>Gap boshida yolgʻiz aytilgan あの nima maʼno beradi?</p>",
      ["«Anavi»", "«Kechirasiz…» — murojaatdan oldingi tovush",
       "«Qaysi?»", "«Shu yerda»"],
      "«Kechirasiz…» — murojaatdan oldingi tovush",
      "<p>Vergul bilan ajratilgan <strong>あの、</strong> — koʻrsatish emas, "
      "murojaat: «Kechirasiz…». Oʻzbekchada ham «anavi…» deb duduqlanamiz.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"これは{HO}です", f"この{HO}は{W}のです",
       f"この は{HO}です", f"あれは{TO}です"],
      f"この は{HO}です",
      "<p>この <strong>yolgʻiz qololmaydi</strong> — ortidan albatta ot kerak. "
      f"Toʻgʻrisi: «これは{HO}です» yoki «この{HO}は…».</p>"),
    q("<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
      [f"これ{HO}は{W}のです", f"この{HO}は{W}のです",
       f"これは{HO}です", f"その{HO}は{W}のです"],
      f"これ{HO}は{W}のです",
      "<p>Ot bilan これ emas, <strong>この</strong> ishlatiladi.</p>"),
    q(f"<p>Qaysi gapda qoʻshimcha <strong>xato</strong>?</p>",
      [f"どれが{HO}ですか", f"どれは{HO}ですか",
       f"どの{HO}が{W}のですか", f"これは{HO}です"],
      f"どれは{HO}ですか",
      "<p>どれ — savol soʻzi, shuning uchun <strong>が</strong> kerak. "
      "は bilan ishlatib boʻlmaydi.</p>"),
    q("<p>«Anavi soat» ni tanlang.</p>",
      [f"あれ{TO}", f"あの{TO}", f"あそこ{TO}", f"あれは{TO}"], f"あの{TO}",
      f"<p><strong>あの{TO}</strong> — ot bor, demak あの. «あれ{TO}» "
      f"notoʻgʻri, chunki あれ ortidan ot qabul qilmaydi.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: これは{NN}ですか。</strong></p>"
      f"<p><strong>B: ___は<ruby>傘<rt>かさ</rt></ruby>です。</strong></p>",
      ["これ", "それ", "あれ", "どれ"], "それ",
      "<p><strong>それ</strong>. Narsa A ning qoʻlida, shuning uchun B uchun u "
      "«senga yaqin» — それ. Bir narsa, ikki xil soʻz: masofa kimga nisbatan "
      "oʻlchanishiga qarab oʻzgaradi.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>です · は · {W}の · この{HO}</strong></p>",
      [f"この{HO}は{W}のです", f"{W}のはこの{HO}です",
       f"この{HO}の{W}はです", f"は この{HO}{W}のです"],
      f"この{HO}は{W}のです",
      f"<p><strong>この{HO}は{W}のです</strong> — «Bu kitob meniki». この darrov "
      f"otga yopishadi, keyin mavzu qoʻshimchasi は, oxirida kesim.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-13 Mashq: 〜です / 〜ではありません",
        "description": "20 savol — です qolipi, か bilan savol, ではありません bilan inkor.",
        "tutorial":    "PJ-13:",
        "level":       "easy",
        "questions":   Q_PJ13,
    },
    {
        "title":       "PJ-14 Mashq: は va が",
        "description": "20 savol — mavzu va ega farqi, savol soʻzi bilan が, qarama-qarshi qoʻyish.",
        "tutorial":    "PJ-14:",
        "level":       "easy",
        "questions":   Q_PJ14,
    },
    {
        "title":       "PJ-15 Mashq: これ・それ・あれ va この・その・あの",
        "description": "20 savol — uch masofa, ikki qator farqi, どれ va どの bilan savol.",
        "tutorial":    "PJ-15:",
        "level":       "easy",
        "questions":   Q_PJ15,
    },
]
