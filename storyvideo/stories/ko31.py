# -*- coding: utf-8 -*-
"""KO-31 — «Oxirgi unli hal qiladi»  ·  TUTILGAN XATO  ·  GRAMMATIKA 03

Manba: Prime Korean PK-20 — oʻtgan zamon 았/었어요.

Grammatika yoʻlining uchinchisi. Kasallik turi ataylab almashtirildi
(SERIES.md §3): KO-29 oʻzbekcha odatning toʻqnashuvi edi, KO-30 kashfiyot,
bu esa **til ichidagi mexanizm** — oʻzbek tilida unga tayyorlaydigan hech
narsa yoʻq.

Oʻzbekchada oʻtgan zamon qoʻshimchasi oʻzgarmaydi: bor-DIM, kel-DIM,
oʻqi-DIM — oʻzak qanday unli bilan tugashi hech narsani hal qilmaydi.
Koreysda hal qiladi, va faqat ikkita unli: ㅏ va ㅗ. Qolgan hammasi — 었.

⚠️ 먹았어요 — mavjud boʻlmagan shakl. Muqovada chizib tashlanadi va ovozda
aytiladi (pupil xatoni eshitishi kerak), lekin `echo` GA BERILMAYDI —
koreys ovozi uydirma shaklni takrorlashi nuqson boʻlardi (SERIES.md §5).
"""

from spec import Video, narrate
from scenes import (cover, says, correct, pairs, check, echo, rule, ask,
                    practice, outro)

VIDEO = Video(
    slug="ko31",
    lesson="PK-20",
    title="Oxirgi unli hal qiladi",
    story="Prime Korean PK-20 — oʻtgan zamon",
    subject="korean",
    scenes=[
        cover("먹았어요", "Bitta unli hal qiladi",
              kicker="Tutilgan xato", ko="한국어",
              track="Grammatika", n=3, badge="big",
              context="Oʻtgan zamon. Bu shakl mavjud emas:",
              strike=True,
              note="MUQOVA: notoʻgʻri shakl chizib tashlangan. Qizil chiziq "
                   "butun soʻzni kesadi, chunki soʻzning OʻZI yoʻq."),

        says("Farrux", [("Kecha nima yeding?", "lbl"),
                        ("저는 밥을 먹았어요.", "expr ko")],
             mood="smile", dur=6.2,
             note="Mantiqiy xato: 밥 dagi ㅏ ni eshitib, 았 tanlagan. "
                  "Lekin qaraladigan unli — FEʼL oʻzagida."),

        correct("먹았어요", "먹었어요",
                because="먹 oʻzagining unlisi ㅓ — demak 었",
                lead="Feʼl oʻzagiga qarang:", shake=True, dur=9.0,
                note="Oʻzak 먹, unlisi ㅓ. ㅏ ham, ㅗ ham emas."),

        pairs([("ㅏ yoki ㅗ", "았어요 — 가다 → 갔어요, 오다 → 왔어요"),
               ("boshqa har qanday unli", "었어요 — 먹다 → 먹었어요"),
               ("하다", "했어요 — bu yodlanadi")],
              head="Feʼl oʻzagining OXIRGI unlisiga qarang",
              tail="Faqat ikkita unli 았 oladi. Qolgan hammasi — 었.",
              dur=13.5,
              note="Filmning dalili: uch qator butun tizimni qoplaydi. "
                   "Uchinchisi — istisno, va u bittagina."),

        check("마시다 → 마셨어요",
              parts=["oʻzak 마시", "oxirgi unli ㅣ", "ㅏ ham, ㅗ ham emas → 었",
                     "마시 + 었어요 qisqaradi → 마셨어요"],
              verdict="Qoida ishladi.",
              title="Tekshiramiz",
              dur=10.0,
              note="Qoidani pupil oʻzi qoʻllay oladimi — shu yerda "
                   "koʻrsatiladi. Qisqarish alohida hodisa, lekin tanlov "
                   "oʻsha qoidadan chiqdi."),

        echo("먹었어요", gloss="yedim",
             note="JIM sahna. FAQAT toʻgʻri shakl aytiladi."),

        rule("Oʻzakda ㅏ yoki ㅗ boʻlsa — 았, boʻlmasa — 었",
             strip="가다 → 갔어요   ·   먹다 → 먹었어요   ·   하다 → 했어요",
             meaning="Oʻzbekchada oʻtgan zamon qoʻshimchasi oʻzgarmaydi: "
                     "bordim, keldim, oʻqidim. Koreysda oʻzakning oxirgi "
                     "unlisi qoʻshimchani tanlaydi — shuning uchun feʼlni "
                     "yodlaganda oʻzagini ham yodlang.",
             dur=11.0),

        ask("놀다 — «oʻynamoq». | Oʻzagi 놀, unlisi ㅗ. "
            "Unda oʻtgan zamoni qanday boʻladi?",
            dur=7.2,
            note="Javobni aytmang. Qoida videoda bor, lekin 놀다 "
                 "hech qayerda tuslanmagan."),

        practice("Prime Korean · PK-20",
                 sub="powerty.uz → Darsliklar → Prime Korean",
                 dur=5.2),

        outro(line2="koreys tili"),
    ],
)

narrate(VIDEO, [
    "Koreys tilida oʻtgan zamon ikki xil yasaladi. "
    "|| Va bu shakl — 먹았어요 — mavjud emas.",

    "Farrux aytadi: 저는 밥을 먹았어요. "
    "| U 밥 soʻzidagi «a» ni eshitgan. || Lekin qaraladigan unli u yerda emas.",

    "Feʼl oʻzagiga qaraladi. | Oʻzak — 먹, unlisi «o». "
    "|| Demak 먹었어요.",

    "Qoida oddiy. | Oʻzakning oxirgi unlisi «a» yoki «oʻ» boʻlsa — 았어요. "
    "| Boshqa unli boʻlsa — 었어요. "
    "|| 하다 esa 했어요 boʻladi.",

    "Tekshiramiz. 마시다 — ichmoq. | Oʻzagi 마시, oxirgi unlisi «i». "
    "|| Demak 마셨어요.",

    None,   # echo(먹었어요)

    "Oʻzbekchada qoʻshimcha oʻzgarmaydi: bordim, keldim, oʻqidim. "
    "| Koreysda oʻzak qoʻshimchani tanlaydi. "
    "|| Shuning uchun feʼlni yodlaganda oʻzagini ham yodlang.",

    "Endi oʻzingiz oʻylang. 놀다 — oʻynamoq, oʻzagi 놀. "
    "| Oʻtgan zamoni qanday boʻladi? || Izohda kutamiz.",

    "Prime Korean — yuzta dars, boshidan. Powertyda, yigirmanchi dars.",

    None,   # outro
])
