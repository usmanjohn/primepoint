# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-16 … PJ-18.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_16_18.py --master=prime \\
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

W   = "<ruby>私<rt>わたし</rt></ruby>"
HO  = "<ruby>本<rt>ほん</rt></ruby>"
SE  = "<ruby>先生<rt>せんせい</rt></ruby>"
NE  = "<ruby>猫<rt>ねこ</rt></ruby>"
TS  = "<ruby>机<rt>つくえ</rt></ruby>"
UE  = "<ruby>上<rt>うえ</rt></ruby>"
SH  = "<ruby>下<rt>した</rt></ruby>"
NA  = "<ruby>中<rt>なか</rt></ruby>"
KB  = "<ruby>鞄<rt>かばん</rt></ruby>"
KY  = "<ruby>教室<rt>きょうしつ</rt></ruby>"
DA  = "<ruby>誰<rt>だれ</rt></ruby>"
NG  = "<ruby>日本語<rt>にほんご</rt></ruby>"
TM  = "<ruby>友達<rt>ともだち</rt></ruby>"
KU  = "<ruby>車<rt>くるま</rt></ruby>"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


Q_PJ16 = [
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{KY}に{SE}が___。</strong></p>",
      ["あります", "います", "です", "ありません"], "います",
      "<p><strong>います</strong> — odam <strong>jonli</strong>. あります faqat "
      "jonsiz narsalar uchun ishlatiladi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{TS}の{UE}に{HO}が___。</strong></p>",
      ["います", "あります", "です", "いません"], "あります",
      "<p><strong>あります</strong> — kitob jonsiz narsa.</p>"),
    q("<p>Mashina uchun qaysi feʼl ishlatiladi?</p>",
      ["います", "あります", "Ikkalasi ham", "Hech qaysisi"], "あります",
      "<p><strong>あります</strong>. Mashina harakatlanadi, lekin <em>oʻz irodasi "
      "bilan</em> emas — shuning uchun jonsiz sanaladi. Qoida: oʻz irodasi bilan "
      "harakatlanadimi?</p>"),
    q("<p>«Bu yer» qanday aytiladi?</p>",
      ["これ", "この", "ここ", "こちら"], "ここ",
      "<p><strong>ここ</strong>. これ narsa, この ot bilan, こちら esa hurmatli "
      "shakl yoki «bu tomon».</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>ここ___{NE}がいます。</strong></p>",
      ["は", "に", "の", "が"], "に",
      "<p><strong>に</strong> — joy qoʻshimchasi, «bu yer<em>da</em>». "
      "Oʻzbekchadagi oʻrin-payt kelishigi bilan aynan bir xil ish.</p>"),
    q("<p>います ning inkori qaysi?</p>",
      ["ありません", "いません", "ではありません", "いです"], "いません",
      "<p><strong>いません</strong>. あります ning inkori esa ありません.</p>"),
    q(f"<p>«{NE}は どこですか» savoliga toʻgʻri javob qaysi?</p>",
      [f"{NE}は{KB}の{NA}にいます", f"{KB}の{NA}に{NE}がいます",
       f"{NE}が{KB}の{NA}にいます", f"{KB}は{NE}の{NA}にいます"],
      f"{NE}は{KB}の{NA}にいます",
      "<p>Mushuk allaqachon maʼlum (savolda aytilgan), shuning uchun u "
      "<strong>は</strong> oladi va gap boshiga chiqadi. Qolip: "
      "<strong>NARSA は JOY に います</strong>.</p>"),
    q(f"<p>«{KY}に{DA}がいますか» savoli nimani soʻrayapti?</p>",
      ["Sinf qayerda", "Sinfda kim bor", "Sinf qanday", "Sinf kimniki"],
      "Sinfda kim bor",
      "<p>Joy maʼlum (sinf), <strong>kim</strong> ekani nomaʼlum. Shuning uchun "
      "qolip <strong>JOY に NARSA が</strong> — yangi maʼlumot が oladi.</p>"),
    q("<p>«Stol tagida» ni tanlang.</p>",
      [f"{TS}の{SH}に", f"{SH}の{TS}に", f"{TS}に{SH}の", f"{SH}に{TS}の"],
      f"{TS}の{SH}に",
      "<p><strong>Ot → の → joy soʻzi → に</strong>. Oʻzbekchada ham xuddi "
      "shunday tartib: «stol<em>ning</em> tag<em>ida</em>».</p>"),
    q("<p>Baliq uchun qaysi feʼl ishlatiladi?</p>",
      ["あります", "います", "です", "ありません"], "います",
      "<p><strong>います</strong> — baliq tirik jonzot, oʻz irodasi bilan "
      "harakatlanadi.</p>"),
    q("<p>Daraxt uchun qaysi feʼl ishlatiladi?</p>",
      ["います", "あります", "Ikkalasi ham", "Feʼl kerak emas"], "あります",
      "<p><strong>あります</strong>. Oʻsimlik tirik boʻlsa ham, yapon tilida "
      "jonsiz sanaladi — u oʻz irodasi bilan harakatlanmaydi.</p>"),
    q("<p>どちら soʻzining ikkita maʼnosi qaysi?</p>",
      ["«Qaysi» va «qanday»", "«Qayer» (muloyim) va «ikkitadan qaysi biri»",
       "«Kim» va «qayer»", "«Qachon» va «qayer»"],
      "«Qayer» (muloyim) va «ikkitadan qaysi biri»",
      "<p>どちら — どこ ning muloyim shakli, va PJ-15 dagi «ikkitadan qaysi "
      "biri» maʼnosi ham shu soʻzda.</p>"),
    q("<p>Qaysi juftlik toʻgʻri?</p>",
      ["kitob — います", "odam — あります", "mushuk — います", "stol — います"],
      "mushuk — います",
      "<p>Mushuk jonli → <strong>います</strong>. Kitob va stol jonsiz → "
      "あります. Odam jonli → います, «odam — あります» notoʻgʻri.</p>"),
    q(f"<p>Inkor gapda が odatda nimaga almashadi?</p>",
      ["に", "は", "の", "を"], "は",
      f"<p><strong>は</strong>. «ここに{NE}<strong>は</strong>いません» — "
      f"«mushukka kelsak, u yoʻq». Bu juda keng tarqalgan va tabiiy eshitiladi.</p>"),
    q("<p>«Sumka ichida» ni tanlang.</p>",
      [f"{KB}の{NA}に", f"{NA}の{KB}に", f"{KB}に{NA}の", f"{NA}に{KB}に"],
      f"{KB}の{NA}に",
      f"<p><strong>{KB}の{NA}に</strong> — ot, keyin の, keyin joy soʻzi, "
      f"oxirida に.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{KY}に{SE}がいます", f"{KY}に{SE}があります",
       f"{TS}の{UE}に{HO}があります", f"ここに{NE}がいます"],
      f"{KY}に{SE}があります",
      "<p>Odam <strong>jonli</strong>, shuning uchun います kerak. あります "
      "faqat jonsiz narsalar uchun.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"ここに{NE}がいます", f"ここは{NE}がいます",
       f"{NE}はここにいます", f"そこに{HO}があります"],
      f"ここは{NE}がいます",
      "<p>Joyni koʻrsatish uchun <strong>に</strong> kerak, は emas. "
      f"Toʻgʻrisi: «ここ<strong>に</strong>{NE}がいます».</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HO}は{KY}___あります。</strong></p>",
      ["は", "が", "に", "の"], "に",
      "<p><strong>に</strong> — joy qoʻshimchasi. Bu qolip «kitob qayerda?» "
      "degan savolga javob: narsa maʼlum, joy yangi.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {NE}は どこですか。</strong></p>"
      f"<p><strong>B: ___です。</strong></p>",
      ["あれ", "あの", "あそこ", "あちらの"], "あそこ",
      "<p><strong>あそこ</strong> — «u yer». Savol どこ (joy) boʻlgani uchun "
      "javob ham joy soʻzi boʻlishi kerak. あれ narsani bildiradi.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>あります · に · {HO}が · {TS}の{UE}</strong></p>",
      [f"{TS}の{UE}に{HO}があります", f"{HO}が{TS}の{UE}にあります",
       f"あります{TS}の{UE}に{HO}が", f"に{TS}の{UE}{HO}があります"],
      f"{TS}の{UE}に{HO}があります",
      "<p><strong>JOY に NARSA が あります</strong> — joy oldin, narsa keyin, "
      "feʼl oxirida. Yapon gapi doim feʼl bilan tugaydi.</p>"),
]


Q_PJ17 = [
    q(f"<p>«Mening kitobim» ni tanlang.</p>",
      [f"{HO}の{W}", f"{W}の{HO}", f"{W}{HO}の", f"{W}は{HO}"],
      f"{W}の{HO}",
      f"<p><strong>{W}の{HO}</strong> — <strong>ega oldin</strong>, keyin の, "
      f"keyin narsa. Oʻzbekchadagi tartib bilan bir xil.</p>"),
    q("<p>の qoʻshimchasining asosiy qoidasi qaysi?</p>",
      ["A の B = «B ning A si»", "A の B = «A ning B si»",
       "A の B = «A va B»", "A の B = «A yoki B»"],
      "A の B = «A ning B si»",
      "<p>Aniqlovchi <strong>oldin</strong> turadi. Uzun zanjirda ham shu: "
      "asosiy narsa doim <strong>oxirgi</strong> soʻz.</p>"),
    q(f"<p>{NG}の{SE} nima degani?</p>",
      ["Oʻqituvchining yapon tili", "Yapon tili oʻqituvchisi",
       "Yapon oʻqituvchi", "Oʻqituvchi va yapon tili"],
      "Yapon tili oʻqituvchisi",
      "<p>Bu yerda の egalikni emas, <strong>«nima haqida»</strong> degan "
      "munosabatni bildiryapti. Asosiy soʻz — oxirgisi, yaʼni oʻqituvchi.</p>"),
    q(f"<p>«これは{W}のです» nima degani?</p>",
      ["Bu mening kitobim", "Bu meniki", "Bu men", "Bu menda"],
      "Bu meniki",
      "<p>の dan keyingi ot <strong>tushirib qoldirilgan</strong>, chunki nima "
      "haqida gapirilayotgani aniq. Shunda の ning oʻzi «…niki» maʼnosini "
      "oladi.</p>"),
    q("<p>Oʻzbekcha «mening kitobim» da nechta egalik belgisi bor?</p>",
      ["Bitta", "Ikkita — «men-ning» va «kitob-im»", "Uchta", "Hech qanday"],
      "Ikkita — «men-ning» va «kitob-im»",
      f"<p>Oʻzbekchada egalik <strong>ikki marta</strong> belgilanadi. "
      f"Yaponchada esa <strong>bitta</strong> の yetadi: {W}の{HO}. Yaʼni "
      f"ikkinchi qoʻshimchani unutish kerak, qoʻshish emas.</p>"),
    q(f"<p>{W}の{TM}の{HO} zanjirida asosiy narsa qaysi?</p>",
      [W, TM, HO, "Uchalasi teng"], HO,
      "<p><strong>Oxirgi soʻz</strong> asosiy. Chapdan oʻngga oʻqing: men → "
      "doʻstim → kitob. Gap kitob haqida.</p>"),
    q(f"<p>«Bu sumka kimniki?» ni tanlang.</p>",
      [f"この{KB}は{DA}のですか", f"これ{KB}は{DA}のですか",
       f"この{KB}は{DA}ですか", f"この{KB}の{DA}ですか"],
      f"この{KB}は{DA}のですか",
      "<p>Ikkita narsa birga: この otga yopishgan (PJ-15), va "
      f"<strong>{DA}の</strong> — otsiz の, «kimniki».</p>"),
    q("<p>Nega この ortidan albatta ot kerak?</p>",
      ["Bu istisno", "この aslida こ + の, va の bogʻlovchi — ikkinchi tomon kerak",
       "この juda qisqa", "この faqat yozuvda ishlatiladi"],
      "この aslida こ + の, va の bogʻlovchi — ikkinchi tomon kerak",
      "<p>これ da の yoʻq, shuning uchun u yolgʻiz tura oladi. Qoida: "
      "<strong>の bor — ot kerak, の yoʻq — ot kerak emas</strong>.</p>"),
    q(f"<p>«Yogʻoch stol» ni tanlang.</p>",
      [f"<ruby>木<rt>き</rt></ruby>の{TS}", f"{TS}の<ruby>木<rt>き</rt></ruby>",
       f"<ruby>木<rt>き</rt></ruby>{TS}", f"{TS}<ruby>木<rt>き</rt></ruby>の"],
      f"<ruby>木<rt>き</rt></ruby>の{TS}",
      "<p>«Nimadan yasalgan» ham の bilan beriladi, va aniqlovchi "
      "(yogʻoch) oldin turadi.</p>"),
    q("<p>の sifat bilan ishlatiladimi?</p>",
      ["Ha, har doim", "Yoʻq — の faqat ikki OTNI bogʻlaydi",
       "Faqat rasmiy nutqda", "Faqat savolda"],
      "Yoʻq — の faqat ikki OTNI bogʻlaydi",
      f"<p>Sifat otga <strong>toʻgʻridan-toʻgʻri</strong> yopishadi: "
      f"«<ruby>大<rt>おお</rt></ruby>きい{HO}», の <em>siz</em>. Lekin ot + ot "
      f"boʻlsa の kerak: «<ruby>木<rt>き</rt></ruby>の{TS}».</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{TS}___{UE}に{HO}があります。</strong></p>",
      ["は", "が", "の", "に"], "の",
      "<p><strong>の</strong> — ikki otni bogʻlaydi: «stolning usti». "
      "Joy soʻzlari doim shu tuzilishda ishlatiladi.</p>"),
    q(f"<p>«{W}の» dan keyin ot boʻlmasa, u nimani anglatadi?</p>",
      ["«Men»", "«Meniki»", "«Menda»", "«Menga»"], "«Meniki»",
      "<p>Ot tushib qolganda の ning oʻzi <strong>«…niki»</strong> maʼnosini "
      "oladi. Bu juda keng tarqalgan va tabiiy.</p>"),
    q("<p>Nechta の ketma-ket ishlatish tabiiy sanaladi?</p>",
      ["Bitta", "Ikkitagacha", "Beshtagacha", "Cheklov yoʻq"],
      "Ikkitagacha",
      "<p>Grammatik jihatdan koʻproq ham mumkin, lekin yaponlar buni "
      "yoqtirmaydi. Uch bosqichdan uzun zanjirni <strong>ikki gapga "
      "boʻlish</strong> ancha tabiiyroq. Bu uslub masalasi, xato emas.</p>"),
    q(f"<p>{KU}の<ruby>中<rt>なか</rt></ruby> nima degani?</p>",
      ["Mashinaning ichi", "Ichkaridagi mashina", "Mashina va ich", "Mashinaga"],
      "Mashinaning ichi",
      "<p>Aniqlovchi oldin: mashina → ning → ich. Asosiy soʻz oxirgisi.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{W}の{HO}です", f"{HO}の{W}です",
       f"{NG}の{SE}です", f"これは{W}のです"],
      f"{HO}の{W}です",
      f"<p>Ega <strong>oldin</strong> turadi. «{HO}の{W}» — «kitobning meni», "
      f"maʼnosiz. Toʻgʻrisi: «{W}の{HO}».</p>"),
    q("<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
      [f"この{HO}", f"これの{HO}", f"その{KB}", f"あの{KU}"],
      f"これの{HO}",
      "<p>これ da の <strong>allaqachon yoʻq</strong> va uni qoʻshib boʻlmaydi. "
      f"Ot bilan <strong>この</strong> ishlatiladi: «この{HO}».</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>この{KB}は{DA}___ですか。</strong></p>",
      ["は", "が", "の", "に"], "の",
      "<p><strong>の</strong> — «kimniki». Ot tushirilgan の konstruksiyasi.</p>"),
    q(f"<p>{W}の{TM}の{HO} ni oʻzbekchaga tarjima qiling.</p>",
      ["Mening doʻstim va kitobim", "Mening doʻstimning kitobi",
       "Doʻstimning meni va kitobi", "Kitobimning doʻsti"],
      "Mening doʻstimning kitobi",
      "<p>Chapdan oʻngga torayadi: men → doʻstim → kitob.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: この{HO}は{DA}のですか。</strong></p>"
      f"<p><strong>B: ___です。</strong></p>",
      [f"{W}", f"{W}の", f"{W}は", f"{W}に"], f"{W}の",
      f"<p><strong>{W}の</strong> — «meniki». Savol «{DA}の» shaklida "
      f"berilgani uchun javob ham の bilan tugashi kerak. «{W}です» boʻlsa "
      f"«men — kitobman» degan maʼno chiqardi.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>です · の · {SE} · {NG}</strong></p>",
      [f"{NG}の{SE}です", f"{SE}の{NG}です",
       f"{NG}{SE}のです", f"の{NG}{SE}です"],
      f"{NG}の{SE}です",
      "<p>Aniqlovchi oldin: «yapon tili» → の → «oʻqituvchi». Asosiy soʻz "
      "oxirida.</p>"),
]


Q_PJ18 = [
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>これは<ruby>何<rt>?</rt></ruby>ですか。</strong></p>",
      ["なに", "なん", "Ikkalasi ham", "Farqi yoʻq"], "なん",
      "<p><strong>なん</strong>. です dan oldin doim なん — «なんです» tilga "
      "yengilroq tushadi, chunki ん va で ikkalasi ham til uchi bilan chiqadi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>何<rt>?</rt></ruby>がありますか。</strong></p>",
      ["なん", "なに", "だれ", "どこ"], "なに",
      "<p><strong>なに</strong>. が dan oldin なに ishlatiladi. Qoida "
      "talaffuzga asoslangan: なん faqat です・の va sanoq soʻzlaridan oldin.</p>"),
    q("<p>Soʻroq soʻzi gapning qayerida turadi?</p>",
      ["Doim gap boshida", "Javob turadigan joyda", "Doim gap oxirida",
       "Feʼldan oldin"],
      "Javob turadigan joyda",
      f"<p>Gapni qayta qurish kerak emas. «{KY}は<strong>どこ</strong>ですか» → "
      f"«{KY}は<strong>あそこ</strong>です» — bitta soʻz almashdi, xolos.</p>"),
    q("<p>«Qachon?» qanday aytiladi?</p>",
      ["どこ", "いつ", "どう", "いくら"], "いつ",
      "<p><strong>いつ</strong> — «qachon». どこ «qayer», どう «qanday», "
      "いくら «qancha (narx)».</p>"),
    q("<p>«Qancha turadi?» qanday soʻraladi?</p>",
      ["どうですか", "いくらですか", "いつですか", "どちらですか"],
      "いくらですか",
      "<p><strong>いくらですか</strong> — narx haqidagi savol. Doʻkonda eng "
      "koʻp kerak boʻladigan gaplardan biri.</p>"),
    q("<p>Soʻroq soʻzlarining yarmi qaysi tizimdan keladi?</p>",
      ["Sonlar tizimi", "ko-so-a-do jadvalining ど ustuni",
       "Kanji radikallari", "Sanoq soʻzlari"],
      "ko-so-a-do jadvalining ど ustuni",
      "<p>どこ, どれ, どの, どちら, どう — hammasi PJ-15 dagi jadvalning "
      "oxirgi qatori. Yaʼni siz ularni allaqachon tizim sifatida bilasiz.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{DA}___{SE}ですか。</strong></p>",
      ["は", "が", "の", "に"], "が",
      f"<p><strong>が</strong>. Soʻroq soʻzi bilan doim が — «{DA}は» degan "
      f"birikma yapon tilida mavjud emas.</p>"),
    q(f"<p>Nega «{KY}はどこですか» da は ishlatilgan?</p>",
      ["Qoida buzilgan", "Qoida soʻroq soʻzining OʻZIGA tegishli — どこ は olmaydi, sinf esa oladi",
       "どこ har doim は oladi", "Bu istisno"],
      "Qoida soʻroq soʻzining OʻZIGA tegishli — どこ は olmaydi, sinf esa oladi",
      "<p>Sinf — maʼlum narsa, shuning uchun u bemalol は oladi. Taqiq faqat "
      "<strong>soʻroq soʻzining oʻziga</strong> tegishli.</p>"),
    q(f"<p><ruby>何<rt>なん</rt></ruby>の{HO} — nega なん?</p>",
      ["が dan oldin", "の dan oldin", "を dan oldin", "は dan oldin"],
      "の dan oldin",
      "<p><strong>の dan oldin</strong> なん oʻqiladi. Qoida: です, の va sanoq "
      "soʻzlaridan oldin なん; が, を dan oldin なに.</p>"),
    q("<p><ruby>何人<rt>?</rt></ruby> qanday oʻqiladi?</p>",
      ["なにじん", "なんにん", "なにひと", "なんひと"], "なんにん",
      "<p><strong>なんにん</strong> — «necha kishi». Sanoq soʻzi doim "
      "<strong>なん</strong> ni talab qiladi.</p>"),
    q("<p>«Qanday? / Qay ahvolda?» qanday soʻraladi?</p>",
      ["どこ", "どう", "どれ", "いつ"], "どう",
      f"<p><strong>どう</strong> — fikr soʻraydi: «{NG}はどうですか» = «Yapon "
      f"tili qanday?». Yaponlar bu savolni juda koʻp ishlatadi.</p>"),
    q("<p>お<ruby>国<rt>くに</rt></ruby>はどちらですか — bu nima degani?</p>",
      ["Mamlakatingiz qaysi tomonda?", "Qayerdansiz?",
       "Mamlakatingiz kattami?", "Qaysi mamlakatni yoqtirasiz?"],
      "Qayerdansiz?",
      "<p>どちら bu yerda どこ ning <strong>muloyim</strong> shakli. Boshidagi "
      "<strong>お</strong> — hurmat belgisi, boshqa odamning narsasi haqida "
      "gapirganda qoʻshiladi.</p>"),
    q("<p>Soʻroq gapda ohang koʻtariladimi?</p>",
      ["Ha, har doim", "Yoʻq — か ning oʻzi savolni bildiradi",
       "Faqat rasmiy nutqda", "Faqat か boʻlmaganda"],
      "Yoʻq — か ning oʻzi savolni bildiradi",
      "<p>Ohang koʻtarilmaydi va savol belgisi ham odatda qoʻyilmaydi — "
      "yaponlar gap oxiriga <strong>。</strong> qoʻyadi.</p>"),
    q(f"<p>Qaysi oʻqilish toʻgʻri?</p>",
      ["<ruby>何<rt>なに</rt></ruby>ですか", "<ruby>何<rt>なん</rt></ruby>ですか",
       "<ruby>何<rt>なん</rt></ruby>がありますか", "<ruby>何<rt>なに</rt></ruby>の<ruby>本<rt>ほん</rt></ruby>"],
      "<ruby>何<rt>なん</rt></ruby>ですか",
      "<p>です dan oldin <strong>なん</strong>. Qolgan uchtasi teskari: "
      "が dan oldin なに, の dan oldin なん boʻlishi kerak edi.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{KY}はどこですか", f"どこは{KY}ですか",
       f"{DA}が{SE}ですか", "これは<ruby>何<rt>なん</rt></ruby>ですか"],
      f"どこは{KY}ですか",
      "<p>Soʻroq soʻzi <strong>javob turadigan joyda</strong> turadi va gap "
      f"boshiga koʻchmaydi. Toʻgʻrisi: «{KY}はどこですか».</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{DA}が{SE}ですか", f"{DA}は{SE}ですか",
       f"{KY}はどこですか", "いつですか"],
      f"{DA}は{SE}ですか",
      "<p>Soʻroq soʻzi は <strong>olmaydi</strong> — doim が.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>試験<rt>しけん</rt></ruby>は___ですか。</strong></p>",
      ["どこ", "いつ", "だれ", "いくら"], "いつ",
      "<p><strong>いつ</strong> — imtihon <em>qachon</em>. どこ joy, だれ odam, "
      "いくら narx haqida soʻraydi.</p>"),
    q("<p>Sanoq soʻzi bilan <ruby>何<rt>?</rt></ruby> qanday oʻqiladi?</p>",
      ["Doim なに", "Doim なん", "Sanoq soʻziga bogʻliq", "Oʻqilmaydi"],
      "Doim なん",
      "<p><strong>Doim なん</strong>: <ruby>何人<rt>なんにん</rt></ruby>, "
      "<ruby>何時<rt>なんじ</rt></ruby>, <ruby>何歳<rt>なんさい</rt></ruby>. "
      "Bu qoidaning eng foydali tomoni — sanoq soʻzi koʻrsangiz, oʻqilishi "
      "aniq.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {KY}はどこですか。</strong></p>"
      f"<p><strong>B: ___です。</strong></p>",
      ["あれ", "あそこ", "あの", "どこ"], "あそこ",
      "<p>Savol どこ (joy) boʻlgani uchun javob ham <strong>joy</strong> soʻzi: "
      "あそこ. あれ narsani bildiradi.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>ですか · {SE} · が · {DA}</strong></p>",
      [f"{DA}が{SE}ですか", f"{SE}が{DA}ですか",
       f"{DA}{SE}がですか", f"が{DA}{SE}ですか"],
      f"{DA}が{SE}ですか",
      f"<p><strong>{DA}が{SE}ですか</strong> — «Kim oʻqituvchi?». Soʻroq soʻzi "
      f"ega oʻrnida, が bilan, keyin kesim.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-16 Mashq: ここ・そこ・あそこ va あります / います",
        "description": "20 savol — joy soʻzlari, に qoʻshimchasi, jonli/jonsiz farqi.",
        "tutorial":    "PJ-16:",
        "level":       "easy",
        "questions":   Q_PJ16,
    },
    {
        "title":       "PJ-17 Mashq: の — egalik va ikki otni bogʻlash",
        "description": "20 savol — egalik, ot bogʻlash, «…niki» shakli va zanjir.",
        "tutorial":    "PJ-17:",
        "level":       "easy",
        "questions":   Q_PJ17,
    },
    {
        "title":       "PJ-18 Mashq: Soʻroq soʻzlari",
        "description": "20 savol — butun soʻroq toʻplami, なに/なん farqi, soʻroq soʻzi bilan が.",
        "tutorial":    "PJ-18:",
        "level":       "easy",
        "questions":   Q_PJ18,
    },
]
