# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-19 … PJ-21.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.
Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_19_21.py --master=prime \\
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
G   = "<ruby>学生<rt>がくせい</rt></ruby>"
HO  = "<ruby>本<rt>ほん</rt></ruby>"
KB  = "<ruby>鞄<rt>かばん</rt></ruby>"
TM  = "<ruby>友達<rt>ともだち</rt></ruby>"
GK  = "<ruby>学校<rt>がっこう</rt></ruby>"
IK  = "<ruby>行<rt>い</rt></ruby>きます"
TB  = "<ruby>食<rt>た</rt></ruby>べます"
NM  = "<ruby>飲<rt>の</rt></ruby>みます"
YM  = "<ruby>読<rt>よ</rt></ruby>みます"
OK  = "<ruby>起<rt>お</rt></ruby>きます"
MN  = "<ruby>毎日<rt>まいにち</rt></ruby>"
AS  = "<ruby>明日<rt>あした</rt></ruby>"
NK  = "<ruby>肉<rt>にく</rt></ruby>"
MZ  = "<ruby>水<rt>みず</rt></ruby>"
SJ  = "<ruby>七時<rt>しちじ</rt></ruby>"


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


Q_PJ19 = [
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{W}___{G}です。(«Men ham talabaman»)</strong></p>",
      ["はも", "もは", "も", "がも"], "も",
      "<p><strong>も</strong> yolgʻiz turadi — u <strong>は ni siqib "
      "chiqaradi</strong>. «はも» yoki «もは» degan shakl yapon tilida "
      "mavjud emas.</p>"),
    q("<p>も qaysi qoʻshimchalarni siqib chiqaradi?</p>",
      ["に va と", "は va が", "を va に", "Hech qaysisini"], "は va が",
      f"<p><strong>は va が</strong>. Boshqalar bilan birga turadi: "
      f"{GK}にも, {TM}とも.</p>"),
    q("<p>と va や orasidagi farq nima?</p>",
      ["と rasmiy, や kundalik", "と toʻliq roʻyxat, や ochiq roʻyxat",
       "と otlar uchun, や feʼllar uchun", "Farqi yoʻq"],
      "と toʻliq roʻyxat, や ochiq roʻyxat",
      "<p><strong>と</strong> — faqat sanalganlar. <strong>や</strong> — «va "
      "shunga oʻxshash boshqalar», roʻyxat namuna xolos.</p>"),
    q(f"<p>«{HO}や{KB}があります» nimani anglatadi?</p>",
      ["Faqat kitob va sumka bor", "Kitob, sumka va boshqa narsalar ham bor",
       "Kitob yoki sumka bor", "Kitob sumkaning ichida"],
      "Kitob, sumka va boshqa narsalar ham bor",
      "<p>や roʻyxatni <strong>ochiq</strong> qoldiradi. と ishlatilganda "
      "roʻyxat toʻliq boʻlardi.</p>"),
    q("<p>と gaplarni bogʻlay oladimi?</p>",
      ["Ha", "Yoʻq — faqat otlarni bogʻlaydi", "Faqat savolda", "Faqat inkorda"],
      "Yoʻq — faqat otlarni bogʻlaydi",
      "<p>Oʻzbekchada «va» gaplarni ham bogʻlaydi, yaponchada esa と buni "
      "qila olmaydi. Gaplarni bogʻlashni PJ-33 da koʻramiz.</p>"),
    q(f"<p>{TM}と{GK}にいます — bu yerda と nima degani?</p>",
      ["Va", "Bilan", "Ham", "Yoki"], "Bilan",
      "<p><strong>«Bilan»</strong>. と dan keyin yana ot kelsa «va», kesim "
      "kelsa «bilan» maʼnosini beradi — kontekst hal qiladi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GK}___{HO}があります。(«Maktabda ham»)</strong></p>",
      ["も", "にも", "はも", "がも"], "にも",
      "<p><strong>にも</strong> — も boshqa qoʻshimchalar bilan <strong>birga "
      "turadi</strong>. Faqat は va が ni siqib chiqaradi.</p>"),
    q("<p>Uchta narsani sanaganda nechta と kerak?</p>",
      ["Bitta, oxirida", "Ikkita — har juftlik orasida", "Uchta", "Kerak emas"],
      "Ikkita — har juftlik orasida",
      "<p>Yapon tilida <strong>と har bir juftlik orasida takrorlanadi</strong>: "
      f"{HO}と{KB}と<ruby>時計<rt>とけい</rt></ruby>. Oʻzbekchada esa «va» "
      "faqat oxirida turadi.</p>"),
    q(f"<p>«{W}も{G}ではありません» nima degani?</p>",
      ["Men ham talabaman", "Men ham talaba emasman",
       "Men talaba emasman", "Faqat men talaba emasman"],
      "Men ham talaba emasman",
      "<p>も inkor bilan ham xuddi shunday ishlaydi: «boshqasi ham emas, men "
      "ham emas».</p>"),
    q("<p>«Yolgʻiz» qanday aytiladi?</p>",
      ["<ruby>一人<rt>ひとり</rt></ruby>で", "<ruby>一人<rt>ひとり</rt></ruby>と",
       "<ruby>一人<rt>ひとり</rt></ruby>に", "<ruby>一人<rt>ひとり</rt></ruby>も"],
      "<ruby>一人<rt>ひとり</rt></ruby>で",
      "<p><strong><ruby>一人<rt>ひとり</rt></ruby>で</strong> — «yolgʻiz». "
      "と «bilan» ning teskarisi.</p>"),
    q("<p>Roʻyxat oxirida と qolishi mumkinmi?</p>",
      ["Ha", "Yoʻq — と ikki tomonni bogʻlaydi, undan keyin nimadir kelishi kerak",
       "Faqat yozuvda", "Faqat savolda"],
      "Yoʻq — と ikki tomonni bogʻlaydi, undan keyin nimadir kelishi kerak",
      "<p>や da esa boshqacha: u roʻyxat oxirida ham qolishi mumkin, chunki "
      "«va boshqalar» degan maʼno allaqachon ichida.</p>"),
    q(f"<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{W}も{G}です", f"{W}はも{G}です",
       f"{GK}にも{HO}があります", f"{TM}とも{IK}"],
      f"{W}はも{G}です",
      "<p>も は bilan birga tura olmaydi — u uning <strong>oʻrnini</strong> "
      "egallaydi.</p>"),
    q("<p>Qaysi holatda や ishlatiladi?</p>",
      ["Roʻyxat toʻliq boʻlganda", "Roʻyxat namuna boʻlganda",
       "Gaplarni bogʻlaganda", "Inkor qilganda"],
      "Roʻyxat namuna boʻlganda",
      "<p>や «va shunga oʻxshash boshqalar» degan maʼno qoʻshadi. Toʻliq "
      "roʻyxat uchun <strong>と</strong> ishlatiladi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HO}___{KB}があります。(faqat shu ikkitasi)</strong></p>",
      ["や", "と", "も", "に"], "と",
      "<p><strong>と</strong> — roʻyxat toʻliq. や boʻlsa «va boshqalar» "
      "degan maʼno chiqardi.</p>"),
    q("<p>Nega oʻzbek oʻquvchi も bilan adashadi?</p>",
      ["Oʻzbekchada «ham» yoʻq",
       "Oʻzbekchada «ham» qoʻshilganda hech narsa tushmaydi, yaponchada esa は tushadi",
       "も juda qisqa", "Oʻzbekchada «ham» feʼl bilan ishlaydi"],
      "Oʻzbekchada «ham» qoʻshilganda hech narsa tushmaydi, yaponchada esa は tushadi",
      "<p>Oʻzbekchada ega qoʻshimchasiz turadi, shuning uchun «men ham» "
      "deganda hech narsa oʻzgarmaydi. Yaponchada esa gapda <strong>bitta "
      "joy</strong> bor va は, が, も oʻsha joy uchun raqobat qiladi.</p>"),
    q(f"<p>Qaysi gap <strong>notoʻgʻri</strong>?</p>",
      [f"{W}も{IK}", f"{W}がも{IK}",
       f"{GK}にも{IK}", f"{TM}と{IK}"],
      f"{W}がも{IK}",
      "<p>も <strong>が</strong> ni ham siqib chiqaradi. Toʻgʻrisi: "
      f"«{W}も{IK}».</p>"),
    q(f"<p>«Kitob va sumka va soat bor» ni tanlang.</p>",
      [f"{HO}と{KB}と<ruby>時計<rt>とけい</rt></ruby>があります",
       f"{HO}{KB}<ruby>時計<rt>とけい</rt></ruby>と があります",
       f"{HO}と{KB}<ruby>時計<rt>とけい</rt></ruby>があります",
       f"と{HO}と{KB}<ruby>時計<rt>とけい</rt></ruby>があります"],
      f"{HO}と{KB}と<ruby>時計<rt>とけい</rt></ruby>があります",
      "<p>と <strong>har juftlik orasida</strong> takrorlanadi va roʻyxat "
      "oxirida qolmaydi.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {W}は{G}です。</strong></p>"
      f"<p><strong>B: {W}___{G}です。</strong></p>",
      ["は", "が", "も", "と"], "も",
      "<p><strong>も</strong> — «men ham». Bu も ning eng tipik ishlatilishi: "
      "birov aytgan narsani oʻzingizga ham nisbat berasiz.</p>"),
    q(f"<p>{TM}とも{IK} — bu nima degani?</p>",
      ["Doʻstim bilan boraman", "Doʻstim bilan ham boraman",
       "Doʻstim ham boradi", "Doʻstim va men boramiz"],
      "Doʻstim bilan ham boraman",
      "<p>と («bilan») va も («ham») <strong>birga</strong> ishlagan. も faqat "
      "は va が ni siqib chiqaradi, と ni emas.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>です · も · {G} · {W}</strong></p>",
      [f"{W}も{G}です", f"{W}{G}もです",
       f"も{W}{G}です", f"{G}も{W}です"],
      f"{W}も{G}です",
      "<p>も ega qoʻshimchasi oʻrnida — yaʼni ega bilan kesim orasida, "
      "ega ga yopishgan holda.</p>"),
]


Q_PJ20 = [
    q(f"<p>{AS}{IK} — bu qaysi zamon?</p>",
      ["Hozirgi", "Kelasi", "Oʻtgan", "Zamonsiz"], "Kelasi",
      "<p><strong>Kelasi</strong> — lekin feʼl shakli hozirgi bilan bir xil. "
      "Yapon tilida alohida kelasi zamon <strong>yoʻq</strong>; zamonni "
      f"{AS} («ertaga») koʻrsatadi.</p>"),
    q(f"<p>{NM} ning inkori qaysi?</p>",
      ["<ruby>飲<rt>の</rt></ruby>みません", "<ruby>飲<rt>の</rt></ruby>ないです",
       "<ruby>飲<rt>の</rt></ruby>ます", "<ruby>飲<rt>の</rt></ruby>みませんでした"],
      "<ruby>飲<rt>の</rt></ruby>みません",
      "<p><strong>ます</strong> oʻrniga <strong>ません</strong>. Boshqa hech "
      "narsa oʻzgarmaydi.</p>"),
    q("<p>ます shakli shaxsga qarab oʻzgaradimi?</p>",
      ["Ha, har shaxs uchun boshqa", "Yoʻq — hamma shaxs uchun bitta shakl",
       "Faqat koʻplikda", "Faqat savolda"],
      "Yoʻq — hamma shaxs uchun bitta shakl",
      f"<p>Oʻzbekchada feʼl oʻzgaradi («ishlayman / ishlaysan / ishlaydi»), "
      f"yaponchada esa {IK} — men ham, sen ham, u ham. Kim ekanini "
      f"<strong>mavzu</strong> koʻrsatadi.</p>"),
    q("<p>します feʼli nega ayniqsa foydali?</p>",
      ["Eng qisqa feʼl", "Otlar bilan birikib yangi feʼl yasaydi",
       "Faqat u inkor boʻladi", "Barcha zamonlarda bir xil"],
      "Otlar bilan birikib yangi feʼl yasaydi",
      "<p><ruby>勉強<rt>べんきょう</rt></ruby>します, "
      "<ruby>電話<rt>でんわ</rt></ruby>します, "
      "<ruby>買<rt>か</rt></ruby>い<ruby>物<rt>もの</rt></ruby>します — bitta "
      "feʼl bilan oʻnlab yangi ish nomini aytasiz.</p>"),
    q("<p>Yaponcha gapda feʼl qayerda turadi?</p>",
      ["Boshida", "Oʻrtasida", "Oxirida", "Erkin"], "Oxirida",
      "<p><strong>Oxirida</strong> — bu yapon gapining eng qatʼiy qoidasi, "
      "oʻzbekchadagi kabi. Qolgan boʻlaklarning tartibi ancha erkin.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{MN}{HO}を___。(«har kuni oʻqiyman»)</strong></p>",
      [YM, "<ruby>読<rt>よ</rt></ruby>みません",
       "<ruby>読<rt>よ</rt></ruby>みますか", "<ruby>読<rt>よ</rt></ruby>です"],
      YM,
      "<p><strong>ます</strong> shakli — tasdiq. ません inkor, か savol "
      "yasagan boʻlardi.</p>"),
    q("<p>ます shakli qanday uslubda?</p>",
      ["Kundalik", "Muloyim", "Juda rasmiy", "Faqat yozma"], "Muloyim",
      "<p><strong>Muloyim</strong> (<ruby>丁寧体<rt>ていねいたい</rt></ruby>). "
      "Notanish odam bilan ham, oʻqituvchi bilan ham xavfsiz. Oddiy shaklni "
      "PJ-45 da koʻramiz.</p>"),
    q(f"<p>{OK} nima degani?</p>",
      ["Yotaman", "Turaman (uygʻonaman)", "Boraman", "Qaytaman"],
      "Turaman (uygʻonaman)",
      f"<p><strong>{OK}</strong> — uygʻonib turmoqdan. "
      f"<ruby>帰<rt>かえ</rt></ruby>ります «qaytaman», {IK} «boraman».</p>"),
    q(f"<p>«{MN}{IK}» va «{AS}{IK}» — feʼl shakli farq qiladimi?</p>",
      ["Ha, kelasi zamon uchun boshqa shakl", "Yoʻq — feʼl bir xil, faqat vaqt soʻzi oʻzgargan",
       f"Ha, {AS} bilan ません kerak", "Faqat yozuvda farq qiladi"],
      "Yoʻq — feʼl bir xil, faqat vaqt soʻzi oʻzgargan",
      "<p>Yapon tilida kelasi zamon yoʻq. Shuning uchun «zamon» oʻrniga "
      "<strong>«oʻtgan / oʻtmagan»</strong> deb oʻylash toʻgʻriroq.</p>"),
    q("<p><ruby>勉強<rt>べんきょう</rt></ruby>します nima degani?</p>",
      ["Ishlayman", "Oʻqiyman, shugʻullanaman", "Yozaman", "Tinglayman"],
      "Oʻqiyman, shugʻullanaman",
      "<p><ruby>勉強<rt>べんきょう</rt></ruby> («mashgʻulot») + します = "
      "«oʻqimoq». Bu — します ning eng koʻp uchraydigan birikmalaridan biri.</p>"),
    q(f"<p>Savol yasash uchun nima qilinadi?</p>",
      ["ます ni ません ga almashtiriladi", "Gap oxiriga か qoʻshiladi",
       "Soʻz tartibi oʻzgartiriladi", "Ohang koʻtariladi"],
      "Gap oxiriga か qoʻshiladi",
      f"<p>Oʻsha eski usul: «{IK}<strong>か</strong>». Soʻz tartibi "
      f"oʻzgarmaydi va ohang koʻtarilmaydi.</p>"),
    q(f"<p>«{IK}か» savoliga inkor javob qaysi?</p>",
      ["はい、<ruby>行<rt>い</rt></ruby>きます", "いいえ、<ruby>行<rt>い</rt></ruby>きません",
       "いいえ、<ruby>行<rt>い</rt></ruby>きます", "はい、<ruby>行<rt>い</rt></ruby>きません"],
      "いいえ、<ruby>行<rt>い</rt></ruby>きません",
      "<p>Yaponchada savoldagi feʼlni takrorlab javob berish juda tabiiy: "
      "«いいえ、<ruby>行<rt>い</rt></ruby>きません».</p>"),
    q(f"<p>{MN} nima degani?</p>",
      ["Bugun", "Ertaga", "Har kuni", "Hozir"], "Har kuni",
      f"<p><strong>{MN}</strong> — «har kuni». "
      f"<ruby>今日<rt>きょう</rt></ruby> «bugun», {AS} «ertaga», "
      f"<ruby>今<rt>いま</rt></ruby> «hozir».</p>"),
    q(f"<p>Vaqt soʻzi odatda gapning qayerida turadi?</p>",
      ["Feʼldan keyin", "Gap boshida yoki mavzudan keyin",
       "Doim eng oxirida", "Toʻldiruvchidan keyin"],
      "Gap boshida yoki mavzudan keyin",
      "<p>Yapon gapida <strong>faqat feʼlning oʻrni qatʼiy</strong>. Vaqt "
      "soʻzini gap boshiga ham, mavzudan keyin ham qoʻyish mumkin.</p>"),
    q(f"<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{W}は{MN}{YM}", f"{W}は{YM}{MN}",
       f"{MN}{W}は{YM}", f"{W}は{AS}{IK}"],
      f"{W}は{YM}{MN}",
      "<p>Feʼl <strong>oxirida</strong> turishi kerak. Vaqt soʻzini feʼldan "
      "keyin qoʻyib boʻlmaydi.</p>"),
    q(f"<p>Qaysi shakl <strong>notoʻgʻri</strong>?</p>",
      [TB, "<ruby>食<rt>た</rt></ruby>べません", "<ruby>食<rt>た</rt></ruby>べますか",
       "<ruby>食<rt>た</rt></ruby>べますない"],
      "<ruby>食<rt>た</rt></ruby>べますない",
      "<p>Inkor — <strong>ません</strong>, «ますない» degan shakl yoʻq.</p>"),
    q("<p>Feʼllarni hozircha qanday yodlash kerak?</p>",
      ["Lugʻat shaklida", "ます shaklida, tayyor soʻz sifatida",
       "Kanji bilan birga", "Faqat inkor shaklida"],
      "ます shaklida, tayyor soʻz sifatida",
      "<p>Ularning ichki tuzilishi va lugʻat shakli <strong>PJ-27 va "
      "PJ-28</strong> da ochiladi. Hozircha ular tayyor soʻzlar.</p>"),
    q(f"<p>«Ertaga maktabga bormayman» ni tanlang.</p>",
      [f"{AS}{GK}に<ruby>行<rt>い</rt></ruby>きません",
       f"{AS}{GK}に{IK}",
       f"{AS}に{GK}に<ruby>行<rt>い</rt></ruby>きません",
       f"{GK}に{AS}<ruby>行<rt>い</rt></ruby>ますん"],
      f"{AS}{GK}に<ruby>行<rt>い</rt></ruby>きません",
      f"<p>{AS} ga <strong>に qoʻyilmaydi</strong> — u oʻzi vaqtni bildiradi. "
      f"Inkor esa ません.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: {MN}<ruby>勉強<rt>べんきょう</rt></ruby>しますか。</strong></p>"
      f"<p><strong>B: いいえ、___。</strong></p>",
      ["します", "しません", "しますか", "しですか"], "しません",
      "<p>いいえ bilan boshlangan javob <strong>inkor</strong> boʻlishi kerak: "
      "しません.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{YM} · は · {MN} · {W} · {HO}を</strong></p>",
      [f"{W}は{MN}{HO}を{YM}", f"{W}は{HO}を{MN}{YM}",
       f"{MN}{HO}を{W}は{YM}", f"{W}は{MN}{YM}{HO}を"],
      f"{W}は{MN}{HO}を{YM}",
      "<p>Mavzu → vaqt → toʻldiruvchi → feʼl. Feʼl <strong>oxirida</strong>.</p>"),
]


Q_PJ21 = [
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{HO}___{YM}。</strong></p>",
      ["に", "を", "は", "で"], "を",
      f"<p><strong>を</strong> — toʻldiruvchi qoʻshimchasi, oʻzbekchadagi "
      f"<em>-ni</em>: «kitob<strong>ni</strong> oʻqiyman».</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{GK}___{IK}。</strong></p>",
      ["を", "に", "は", "も"], "に",
      f"<p><strong>に</strong> — yoʻnalish, oʻzbekchadagi <em>-ga</em>: "
      f"«maktab<strong>ga</strong> boraman».</p>"),
    q("<p>を qanday oʻqiladi?</p>",
      ["wo", "o", "wa", "ho"], "o",
      "<p><strong>[o]</strong>. «wo» — belgining eski nomi va uni kompyuterda "
      "yozish usuli, xolos.</p>"),
    q("<p>に ning uch vazifasi qaysi?</p>",
      ["Ega, toʻldiruvchi, kesim", "Joy, yoʻnalish, aniq vaqt",
       "Savol, inkor, tasdiq", "Egalik, bogʻlash, taqqoslash"],
      "Joy, yoʻnalish, aniq vaqt",
      "<p>Uchalasi bitta gʻoyaga bogʻlanadi: に <strong>nuqtani</strong> "
      "koʻrsatadi — fazoda ham, vaqtda ham.</p>"),
    q(f"<p>{AS} ga に qoʻyiladimi?</p>",
      ["Ha, har doim", "Yoʻq — u oʻzi vaqtni bildiradi",
       "Faqat inkorda", "Faqat savolda"],
      "Yoʻq — u oʻzi vaqtni bildiradi",
      f"<p>{AS}, <ruby>今日<rt>きょう</rt></ruby>, {MN} ga に "
      f"<strong>qoʻyilmaydi</strong>. に faqat <strong>son bilan</strong> "
      f"aytilgan vaqtga qoʻyiladi: {SJ}に.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SJ}___{OK}。</strong></p>",
      ["を", "に", "は", "で"], "に",
      f"<p><strong>に</strong> — aniq vaqt (son bilan aytilgan). "
      f"«{SJ}<strong>に</strong>» = «soat yettida».</p>"),
    q(f"<p>Nega «{GK}を{IK}» notoʻgʻri?</p>",
      ["を faqat yozuvda ishlatiladi",
       f"{IK} «nimani?» savoliga javob bermaydi — toʻldiruvchi olmaydi",
       f"{GK} juda uzun soʻz", "を faqat odamlar bilan ishlaydi"],
      f"{IK} «nimani?» savoliga javob bermaydi — toʻldiruvchi olmaydi",
      "<p>«Maktabni boraman» maʼnosiz — oʻzbekchada ham. Bunday feʼl "
      "<strong>に</strong> bilan yoʻnalishni oladi.</p>"),
    q("<p>Qaysi feʼl を oladi?</p>",
      [IK, "<ruby>来<rt>き</rt></ruby>ます", YM, "<ruby>帰<rt>かえ</rt></ruby>ります"],
      YM,
      "<p>«Nimani oʻqiyman?» — savol maʼnoli, demak toʻldiruvchi bor. "
      "Qolgan uchtasi harakat feʼllari va <strong>に</strong> oladi.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{MZ}___{NM}。</strong></p>",
      ["に", "を", "で", "も"], "を",
      "<p><strong>を</strong> — «suv<em>ni</em> ichaman». Ichish oʻtimli "
      "feʼl.</p>"),
    q("<p>Oʻzbek oʻquvchi uchun bu dars nega oson?</p>",
      ["Qoʻshimchalar qisqa",
       "を va に oʻzbekcha -ni va -ga ga deyarli aynan mos tushadi",
       "Faqat ikkita qoʻshimcha bor", "Feʼl oʻzgarmaydi"],
      "を va に oʻzbekcha -ni va -ga ga deyarli aynan mos tushadi",
      "<p>Ikkala tilda ham qoʻshimcha <strong>soʻzga yopishadi</strong> va "
      "feʼl oxirida turadi. Ingliz tilida toʻldiruvchi hech qanday belgi "
      "olmaydi — shuning uchun u orqali oʻrganayotgan odam qiynaladi.</p>"),
    q(f"<p>Yaponcha gapda qaysi boʻlakning oʻrni qatʼiy?</p>",
      ["Mavzu", "Toʻldiruvchi", "Feʼl", "Vaqt soʻzi"], "Feʼl",
      "<p>Faqat <strong>feʼl</strong> — u oxirida. Gap qoʻshimchalar bilan "
      "ushlab turiladi, oʻrin bilan emas, shuning uchun qolgan boʻlaklarni "
      "surish maʼnoni buzmaydi.</p>"),
    q(f"<p>«{NK}を{TB}» ning inkori qaysi?</p>",
      [f"{NK}を<ruby>食<rt>た</rt></ruby>べません", f"{NK}に<ruby>食<rt>た</rt></ruby>べません",
       f"{NK}を<ruby>食<rt>た</rt></ruby>べますない", f"{NK}は<ruby>食<rt>た</rt></ruby>べます"],
      f"{NK}を<ruby>食<rt>た</rt></ruby>べません",
      "<p>Faqat feʼl inkorga oʻzgaradi; を joyida qoladi.</p>"),
    q("<p>«Nimani?» sinash usuli nima uchun kerak?</p>",
      ["Feʼlni topish uchun", "を yoki に kerakligini aniqlash uchun",
       "Zamonni aniqlash uchun", "Mavzuni topish uchun"],
      "を yoki に kerakligini aniqlash uchun",
      "<p>Feʼlga «nimani?» deb savol bering. Maʼnoli boʻlsa — "
      "<strong>を</strong>, maʼnosiz boʻlsa — <strong>に</strong>. Oʻzbek "
      "tilida ham shu farq bor va siz uni oʻylamasdan toʻgʻri ishlatasiz.</p>"),
    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong><ruby>家<rt>いえ</rt></ruby>___<ruby>帰<rt>かえ</rt></ruby>ります。</strong></p>",
      ["を", "に", "は", "や"], "に",
      "<p><strong>に</strong> — «uy<em>ga</em> qaytaman». Qaytish harakat "
      "feʼli, shuning uchun yoʻnalish oladi.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{HO}を{YM}", f"{HO}に{YM}",
       f"{GK}に{IK}", f"{MZ}を{NM}"],
      f"{HO}に{YM}",
      "<p>Kitob <strong>toʻldiruvchi</strong>, yoʻnalish emas. Oʻzbekchada "
      "ham «kitob<em>ni</em>», «kitob<em>ga</em>» emas.</p>"),
    q("<p>Qaysi gapda <strong>xato</strong> bor?</p>",
      [f"{SJ}に{OK}", f"{AS}に{IK}",
       f"{MN}{YM}", f"{GK}に{IK}"],
      f"{AS}に{IK}",
      f"<p>{AS} ga に qoʻyilmaydi — u oʻzi vaqtni bildiradi. Toʻgʻrisi: "
      f"«{AS}{IK}».</p>"),
    q(f"<p>{MN} va {SJ} — qaysi biriga に qoʻyiladi?</p>",
      [MN, SJ, "Ikkalasiga", "Hech qaysisiga"], SJ,
      f"<p><strong>{SJ}</strong> — son bilan aytilgan aniq vaqt. {MN} esa "
      f"oʻzi vaqtni bildiradi va に olmaydi.</p>"),
    q(f"<p>«Har ertalab kofe ichaman» ni tanlang.</p>",
      [f"<ruby>毎朝<rt>まいあさ</rt></ruby>コーヒーを{NM}",
       f"<ruby>毎朝<rt>まいあさ</rt></ruby>にコーヒーを{NM}",
       f"<ruby>毎朝<rt>まいあさ</rt></ruby>コーヒーに{NM}",
       f"コーヒーを<ruby>毎朝<rt>まいあさ</rt></ruby>{NM}に"],
      f"<ruby>毎朝<rt>まいあさ</rt></ruby>コーヒーを{NM}",
      "<p>Vaqt soʻzi boshida (に siz), toʻldiruvchi を bilan, feʼl oxirida.</p>"),
    q(f"<p>Suhbatni toʻldiring.</p><p><strong>A: <ruby>何<rt>なに</rt></ruby>を{TB}か。</strong></p>"
      f"<p><strong>B: パン___{TB}。</strong></p>",
      ["に", "を", "は", "で"], "を",
      "<p>Savol «<ruby>何<rt>なに</rt></ruby>を» shaklida — demak javob ham "
      "<strong>を</strong> bilan. Non toʻldiruvchi.</p>"),
    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring.</p>"
      f"<p><strong>{IK} · に · {GK} · {SJ} · に</strong></p>",
      [f"{SJ}に{GK}に{IK}", f"{GK}に{SJ}に{IK}",
       f"{SJ}に{IK}{GK}に", f"に{SJ}{GK}に{IK}"],
      f"{SJ}に{GK}に{IK}",
      "<p>Vaqt → yoʻnalish → feʼl. Ikkala に ham oʻz ishini bajaryapti: "
      "biri aniq vaqtni, ikkinchisi yoʻnalishni koʻrsatadi.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-19 Mashq: も, と, や",
        "description": "20 savol — も ning siqib chiqarishi, と toʻliq roʻyxat, や ochiq roʻyxat.",
        "tutorial":    "PJ-19:",
        "level":       "easy",
        "questions":   Q_PJ19,
    },
    {
        "title":       "PJ-20 Mashq: 〜ます / 〜ません",
        "description": "20 savol — muloyim feʼl shakli, kelasi zamon yoʻqligi, inkor va birinchi feʼllar.",
        "tutorial":    "PJ-20:",
        "level":       "easy",
        "questions":   Q_PJ20,
    },
    {
        "title":       "PJ-21 Mashq: を va に",
        "description": "20 savol — toʻldiruvchi va yoʻnalish, に ning uch vazifasi, vaqt bilan に.",
        "tutorial":    "PJ-21:",
        "level":       "easy",
        "questions":   Q_PJ21,
    },
]
