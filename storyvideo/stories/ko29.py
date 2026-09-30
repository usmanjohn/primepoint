# -*- coding: utf-8 -*-
"""KO-29 — «Men esa keldim»  ·  TUTILGAN XATO  ·  GRAMMATIKA 01

Manba: Prime Korean PK-12 — 은/는 va 이/가.

Raqamlangan grammatika yoʻlining BIRINCHISI. Shuning uchun ataylab eng
boshidagi tugun tanlandi: oʻzbek tilida 은/는 ning majburiy muqobili yoʻq,
shuning uchun boshlovchi uni umuman koʻrmaydi va hamma joyda 는 qoʻyadi.

Oʻzbekcha tayanch — bu filmning butun gapi: 은/는 = **«esa»**, «-chi».
«Kim keldi?» degan savolga «Men esa keldim» deb javob berish oʻzbekchada ham
xuddi shunday gʻalati eshitiladi. Yaʼni xato koreyscha emas — u tarjima
qilinmagan oʻzbekcha odat. Buni aytish — darsning oʻzi.

⚠️ `echo` faqat haqiqiy shaklni aytadi (제가 왔어요). Notoʻgʻri «저는 왔어요»
grammatik jihatdan mavjud gap, lekin bu savolga javob emas — uni koreys ovozi
takrorlab aytishi pupilni chalgʻitadi, shuning uchun echo qilinmaydi.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, correct, pairs, echo,
                    rule, ask, practice, outro)

VIDEO = Video(
    slug="ko29",
    lesson="PK-12",
    title="Men esa keldim",
    story="Prime Korean PK-12 — 은/는 va 이/가",
    subject="korean",
    scenes=[
        cover("저는 / 제가", "Bittasi javob emas",
              kicker="Tutilgan xato", ko="한국어",
              track="Grammatika", n=1, badge="big",
              context="Ikkalasi ham «men» degani:",
              strike=False,
              note="MUQOVA: gʻalati narsa — bir xil maʼnoli ikki soʻzdan "
                   "biri javob boʻla olmaydi. Raqam: grammatika yoʻli "
                   "shu yerdan boshlanadi."),

        says("Otabek", [("Savol:", "lbl"), ("누가 왔어요?", "expr ko")],
             mood="smile", dur=5.6,
             note="«Kim keldi?» — savol aynan KIM ni soʻrayapti."),

        says("Sevara", [("Javob:", "lbl"), ("저는 왔어요.", "expr ko")],
             mood="smile", dur=5.8,
             note="Grammatik jihatdan buzuq emas. Lekin javob emas."),

        consequence("Otabek", "«Men esa keldim» — unda kim kelmadi?",
                    mood="think", close=True, dur=7.4,
                    note="Yaqin plan. 는 taqqoslash qoʻyadi, shuning uchun "
                         "tinglovchi ikkinchi odamni kutib qoladi."),

        correct("저는 왔어요", "제가 왔어요",
                because="«Kim?» soʻralsa — javobda 이/가",
                lead="Savol KIM ni soʻradi:", shake=True, dur=9.0,
                note="Xato chayqalib kiradi, toʻgʻrisi tepadan tushib "
                     "qotadi."),

        pairs([("은/는", "«esa», «-chi» — mavzu qoʻyadi"),
               ("이/가", "«kim?», «nima?» savolining javobi"),
               ("은/는", "va taqqoslaydi: «men esa bormadim»")],
              head="Oʻzbekchada bu ikkisi bitta qoʻshimcha emas",
              tail="Javob — 이/가. Mavzu — 은/는.",
              note="Jadval filmning dalili: oʻzbekchada 은/는 ning oʻrni "
                   "bor, lekin u majburiy emas — shuning uchun koʻrinmaydi."),

        echo("제가 왔어요", gloss="men keldim — «kim?» javobi",
             note="JIM sahna. Faqat toʻgʻri shakl aytiladi."),

        rule("Kim soʻralsa, javobda 이/가",
             strip="누가 왔어요?  →  제가 왔어요",
             meaning="Yangi xabar — 이/가. Allaqachon maʼlum mavzu yoki "
                     "taqqoslash — 은/는. Shubhalansangiz, oʻzbekchaga "
                     "«esa» qoʻshib koʻring: mos kelsa — 는, kelmasa — 가.",
             dur=10.5),

        ask("«저는 김치를 좋아해요» — bu gapda nega 는? "
            "Gapiruvchi yana nimanidir aytmoqchimi?",
            dur=7.4,
            note="Javobni aytmang. Videoda 는 ning taqqoslash vazifasi "
                 "bor, lekin bu gap sharhlanmagan."),

        practice("Prime Korean · PK-12",
                 sub="powerty.uz → Darsliklar → Prime Korean",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreysda «men» ikki xil aytiladi: 저는 va 제가. "
    "|| Ikkalasi ham toʻgʻri — lekin bittasi javob boʻla olmaydi.",

    "Otabek soʻraydi: 누가 왔어요? | Yaʼni *kim* keldi?",

    "Sevara javob beradi: 저는 왔어요.",

    "Va Otabek kutib qoladi. || Chunki u eshitgan gap — «men *esa* keldim». "
    "| Unda kim kelmadi?",

    "Savol kimni soʻragan boʻlsa, javobda 이/가 turadi. "
    "|| 저는 emas — *제가* 왔어요.",

    "Oʻzbekchada 는 ning oʻrni bor: u «esa». "
    "| «Men esa bormadim» — mana shu 는. "
    "|| Lekin oʻzbekchada uni qoʻyish majburiy emas, shuning uchun "
    "koreyschada ham koʻrinmay ketadi.",

    None,   # echo(제가 왔어요)

    "Shubhalansangiz, oʻzbekchaga «esa» qoʻshib koʻring. "
    "| Mos kelsa — 는. | Kelmasa — 가.",

    "Endi oʻzingiz oʻylang. 저는 김치를 좋아해요 — bu gapda nega 는? "
    "|| Izohda kutamiz.",

    "Prime Korean — yuzta dars, boshidan. Powertyda, oʻn ikkinchi dars.",

    None,   # outro
])
