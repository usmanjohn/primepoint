# -*- coding: utf-8 -*-
"""KO-22 — «Qoʻl oʻrgandi, koʻz oʻrganmadi»  ·  TUTILGAN XATO  ·  TOPIK

Manba: examprep TOPIK — 읽기, «TOPIK Reading 4: Koʻp oʻqing, kam tarjima
qiling». Har bir daʼvo oʻsha darsning oʻzidan: «koʻzingizni mashq qildiring,
qoʻlingizni emas»; «koʻpchilik otlarni yodlaydi, lekin javoblarni koʻpincha
sifat, ravish va feʼllar hal qiladi»; «ajoyib jumlani yozib qoʻying — uni
쓰기 da ishlatasiz».

The fourth TOPIK film, and the band's rotation of the KIND of mistake
continues: ko13 lost marks with good Korean (a register), ko14 with perfect
Korean (a clock), ko15 with no Korean at all (one row on the answer sheet).
This one is lost BEFORE the exam -- a study habit that feels like work and
trains the wrong organ. An hour a night, for months, copying words into a
notebook, when the paper never once asks you to write a word from memory.

That is why it belongs to «Tutilgan xato» rather than to a tips list: the
pupil is not lazy and is not ignorant. They are diligent in the wrong
direction, which is the most expensive mistake on this list.

⚠️ The narration says «ot», «sifat», «ravish» in Uzbek and leaves 명사 ·
형용사 · 부사 on the screen, exactly as ko13 left 문어체 on the screen. A
pupil who cannot yet read those terms hears three identical noises where the
film's whole argument lives.
"""

from spec import Video, narrate
from scenes import (cover, says, consequence, correct, versus, pairs, echo,
                    rule, ask, practice, outro)

K  = '<span class="ko">%s</span>'
KQ = '<span class="ko" style="font-size:72px">%s</span>'

VIDEO = Video(
    slug="ko22",
    lesson="TOPIK 읽기",
    title="Qoʻl oʻrgandi, koʻz oʻrganmadi",
    story="examprep TOPIK — 읽기 metodi",
    subject="korean",
    scenes=[
        cover('<span class="strike">노력 노력</span>', "Qoʻl emas — koʻz",
              kicker="Tutilgan xato · TOPIK",
              ko="한국어",
              context="Daftarga oʻn marta koʻchirdingiz. Keyin?",
              strike=False,
              note="MUQOVA: notoʻgʻri narsa — daftarga qayta-qayta koʻchirilgan "
                   "soʻz, ustidan chiziq. Vaʼda toʻrt soʻz va u butun filmni "
                   "koʻtaradi."),

        says("Sherbek", [("Har kuni bir soat:", "lbl"),
                         ("Daftarga koʻchiraman", "expr")],
             mood="smile",
             note="Mehnat bor, natija yoʻq. Bu — dangasalik emas, "
                  "notoʻgʻri tomonga qilingan mehnat."),

        consequence("Sherbek", "Imtihonda tanimadim.",
                    mood="shock", close=True,
                    note="Xatoning bahosi. U soʻzni YOZA olardi — "
                         "imtihon esa TANISHNI soʻradi."),

        correct("yozib yodlash", "koʻrib tanish",
                because="Imtihon soʻzni yozishni emas, tanishni soʻraydi.",
                shake=True,
                note="Filmning bitta jumlasi. YANGI: xato qimirlaydi, "
                     "toʻgʻrisi tepadan tushib qotadi."),

        versus({"name": "KOʻPCHILIK YODLAYDI",
                "qty": KQ % "명사",
                "price": "otlar",
                "tag": "stol · kitob · maktab"},
               {"name": "JAVOBNI HAL QILADI",
                "qty": KQ % "형용사 · 부사",
                "price": "sifat va ravish",
                "tag": "oqilona · muntazam · samarali"},
               title="Qaysi soʻz turini oʻrganasiz",
               verdict="Javob koʻpincha sifatda turadi",
               dur=12.5,
               note="Darsning oʻz kuzatuvi. Ot matnning mavzusini aytadi, "
                    "sifat va ravish esa savolning javobini."),

        echo("꾸준히", gloss="muntazam",
             note="JIM sahna. Ravish — imtihon matnlarining eng koʻp "
                  "uchraydigan turi."),

        pairs([("합리적이다", "oqilona"),
               ("자연스럽게", "tabiiy ravishda"),
               ("존중하다", "hurmat qilmoq"),
               ("이루다", "erishmoq")],
              head="Javobni hal qiladigan soʻzlar",
              tail="Ot emas — sifat, ravish, feʼl",
              note="Toʻrttasi ham darsning oʻz roʻyxatidan. Hech biri ot "
                   "emas — bu qatorning butun gapi shu."),

        echo("존중하다", gloss="hurmat qilmoq",
             note="JIM sahna. Feʼl — ikkinchi eng foydali tur."),

        rule("Koʻp oʻqing, kam tarjima qiling",
             strip="qoʻlni mashq qildirish → yozish   ·   "
                   "koʻzni mashq qildirish → " + K % "읽기",
             meaning="Soʻzni daftarga koʻchirish qoʻlni oʻrgatadi. Imtihonda "
                     "esa soʻzni koʻrasiz va bir soniyada tanishingiz kerak. "
                     "Shuning uchun mashq ham koʻrish boʻlsin: matnni bir "
                     "necha kundan keyin qaytadan oʻqing.",
             dur=10.5),

        ask("Bugun oʻqigan matningizdan qaysi bitta jumlani yozib qoʻyasiz?",
            dur=7.4,
            note="Javobni aytmang. Bu — koʻchirma savol: film jumla "
                 "yigʻishni aytdi, qaysi jumlani — yoʻq."),

        practice("TOPIK · Oʻqish metodi",
                 sub="powerty.uz → Examprep → TOPIK → Oʻqish", dur=5.4,
                 note="Metodning oʻzi — oʻqish boʻlimining toʻrtinchi darsi."),

        outro(line2="koreys tili · TOPIK"),
    ],
)

narrate(VIDEO, [
    "Sherbek har kuni bir soat lugʻat yodladi. | Daftarga koʻchirib. "
    "|| Imtihonda esa soʻzlarni tanimadi.",

    "Mehnat bor edi. | Natija yoʻq.",

    "Chunki u soʻzni yoza olardi.",

    "Imtihon esa yozishni emas, tanishni soʻraydi.",

    "Yana bir narsa. | Koʻpchilik otlarni yodlaydi. "
    "|| Javobni esa koʻpincha sifat va ravish hal qiladi.",

    None,   # echo(꾸준히) — jim sahna, koreyscha ovoz

    "Mana shunaqa soʻzlar: oqilona, tabiiy ravishda, hurmat qilmoq, "
    "erishmoq. || Birortasi ham ot emas.",

    None,   # echo(존중하다) — jim sahna, koreyscha ovoz

    "Shuning uchun qoida bitta: koʻp oʻqing, kam tarjima qiling. "
    "|| Oʻqigan matnni bir necha kundan keyin qayta oching.",

    "Endi oʻzingiz oʻylang. Bugun oʻqigan matningizdan qaysi jumlani "
    "yozib qoʻyasiz? || Izohda kutamiz.",

    "Oʻqish metodining oʻzi Powertyda: Ekzamprep, Topik, oʻqish. "
    "| Havola profilda.",

    None,   # outro — jim
])
