# -*- coding: utf-8 -*-
"""Prime Japanese mashqlar — PJ-37 … PJ-39.

20 savoldan iborat testlar. Written with STYLE_GUIDE_PJ_PRACTICE.md.

⚠️ Har bir qolip OʻZ oʻzagini talab qiladi — bu batchning butun mazmuni shu.
Shuning uchun har bir feʼl toʻrtta konstanta bilan yoziladi: lugʻat, て, た va
ます oʻzagi.

Import:
    python manage.py import_practices \\
        practice/management/commands/_practice_pj_37_39.py --master=prime \\
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

# lugʻat · て · た · ます-oʻzagi
NERU,   NETE,   NETA,   NE     = r("寝","ね")+"る", r("寝","ね")+"て", r("寝","ね")+"た", r("寝","ね")
DERU,   DETE,   DETA,   DE     = r("出","で")+"る", r("出","で")+"て", r("出","で")+"た", r("出","で")
TABERU, TABETE, TABETA, TABE   = r("食","た")+"べる", r("食","た")+"べて", r("食","た")+"べた", r("食","た")+"べ"
OKIRU,  OKITE,  OKITA,  OKI    = r("起","お")+"きる", r("起","お")+"きて", r("起","お")+"きた", r("起","お")+"き"
MIRU,   MITE,   MITA,   MI     = r("見","み")+"る", r("見","み")+"て", r("見","み")+"た", r("見","み")
YOMU,   YONDE,  YONDA,  YOMI   = r("読","よ")+"む", r("読","よ")+"んで", r("読","よ")+"んだ", r("読","よ")+"み"
KIKU,   KIITE,  KIITA,  KIKI   = r("聞","き")+"く", r("聞","き")+"いて", r("聞","き")+"いた", r("聞","き")+"き"
IKU,    ITTE,   ITTA,   IKI    = r("行","い")+"く", r("行","い")+"って", r("行","い")+"った", r("行","い")+"き"
ARUKU,  ARUITE, ARUITA, ARUKI  = r("歩","ある")+"く", r("歩","ある")+"いて", r("歩","ある")+"いた", r("歩","ある")+"き"
HATARAKU,HATARAITE,HATARAITA,HATARAKI = r("働","はたら")+"く", r("働","はたら")+"いて", r("働","はたら")+"いた", r("働","はたら")+"き"
HANASU, HANASHITE, HANASHITA, HANASHI = r("話","はな")+"す", r("話","はな")+"して", r("話","はな")+"した", r("話","はな")+"し"
YASUMU, YASUNDE, YASUNDA, YASUMI = r("休","やす")+"む", r("休","やす")+"んで", r("休","やす")+"んだ", r("休","やす")+"み"
AU,     ATTE,   ATTA,   AI     = r("会","あ")+"う", r("会","あ")+"って", r("会","あ")+"った", r("会","あ")+"い"
KAERU,  KAETTE, KAETTA, KAERI  = r("帰","かえ")+"る", r("帰","かえ")+"って", r("帰","かえ")+"った", r("帰","かえ")+"り"
ARAU,   ARATTE, ARATTA, ARAI   = r("洗","あら")+"う", r("洗","あら")+"って", r("洗","あら")+"った", r("洗","あら")+"い"
KURU,   KITE,   KITA,   KI     = r("来","く")+"る", r("来","き")+"て", r("来","き")+"た", r("来","き")
SURU,   SHITE,  SHITA,  SHI    = "する", "して", "した", "し"

def kara(te):     return te + "から"
def maeni(dic):   return dic + "まえに"
def atode(ta):    return ta + "あとで"
def nagara(st):   return st + "ながら"
def tai(st):      return st + "たいです"
def takunai(st):  return st + "たくないです"
def takatta(st):  return st + "たかったです"

BENKYOU = r("勉強","べんきょう")
HON, GK, KY, SE = r("本","ほん"), r("学校","がっこう"), r("教室","きょうしつ"), r("先生","せんせい")
NG, WA, IE = r("日本語","にほんご"), r("私","わたし"), r("家","いえ")
ONGAKU, SHUKUDAI, JUGYOU = r("音楽","おんがく"), r("宿題","しゅくだい"), r("授業","じゅぎょう")
SHOKUJI, NIHON, JITENSHA = r("食事","しょくじ"), r("日本","にほん"), r("自転車","じてんしゃ")
OKANE, JIKAN, KAO = "お"+r("金","かね"), r("時間","じかん"), r("顔","かお")


def q(text, choices, correct, explanation):
    return {"text": text, "choices": choices, "correct": correct,
            "explanation": explanation}


# ══════════════════════════════════════════════════════════════════════
# PJ-37 — ish tartibi
# ══════════════════════════════════════════════════════════════════════
Q_PJ37 = [
    q("<p>〜まえに oldida qaysi shakl turadi?</p>",
      ["Lugʻat shakli", "た-shakli", "て-shakli", "ます oʻzagi"],
      "Lugʻat shakli",
      f"<p><strong>{maeni(NERU)}</strong> — «uxlashdan oldin». Gap oʻtgan "
      f"zamonda boʻlsa ham, まえに oldidagi feʼl oʻzgarmaydi.</p>"),

    q("<p>〜あとで oldida qaysi shakl turadi?</p>",
      ["た-shakli", "Lugʻat shakli", "て-shakli", "ない-shakli"],
      "た-shakli",
      f"<p><strong>{atode(TABETA)}</strong> — «yegandan keyin». Bu ham "
      f"gapning zamoniga qaramaydi.</p>"),

    q("<p>〜てから oldida qaysi shakl turadi?</p>",
      ["て-shakli", "た-shakli", "Lugʻat shakli", "ます oʻzagi"],
      "て-shakli",
      f"<p><strong>{kara(OKITE)}</strong> — «turgandan keyin». から bu yerda "
      f"PJ-24 dagi «…dan» ning oʻzi: boshlanish nuqtasi.</p>"),

    q(f"<p>«Uydan chiqishdan oldin» ni tanlang.</p>",
      [f"{IE}を{maeni(DERU)}", f"{IE}を{maeni(DETA)}",
       f"{IE}を{DETE}まえに", f"{IE}を{DE}まえに"],
      f"{IE}を{maeni(DERU)}",
      f"<p><strong>{maeni(DERU)}</strong> — lugʻat shakli. Chiqish hali "
      f"boʻlmagan, shuning uchun tugallanmagan shakl.</p>"),

    q(f"<p>«Nonushta qilgandan keyin» ni あとで bilan tanlang.</p>",
      [f"{atode(TABETA)}", f"{atode(TABERU)}",
       f"{TABETE}あとで", f"{TABE}あとで"],
      f"{atode(TABETA)}",
      f"<p><strong>{atode(TABETA)}</strong> — た-shakli. Yeyish boʻlib "
      f"boʻlgan, shuning uchun tugallangan shakl.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{r('昨日','きのう')}"
      f"___{HON}を{r('読','よ')}みました。</strong> («Kecha uxlashdan oldin "
      f"kitob oʻqidim.»)</p>",
      [maeni(NERU), maeni(NETA), f"{NETE}まえに", f"{NE}まえに"],
      maeni(NERU),
      f"<p>Gap oʻtgan zamonda, lekin まえに oldida baribir <strong>lugʻat "
      f"shakli</strong> turadi. Zamonni faqat oxirgi feʼl "
      f"({r('読','よ')}みました) tashiydi.</p>"),

    q(f"<p>«Darsdan keyin» — ot bilan qanday aytiladi?</p>",
      [f"{JUGYOU}のあとで", f"{JUGYOU}あとで",
       f"{JUGYOU}をあとで", f"{JUGYOU}にあとで"],
      f"{JUGYOU}のあとで",
      f"<p>あと va まえ ning oʻzi ham ot, shuning uchun ular oldidagi otga "
      f"<strong>の</strong> bilan ulanadi. Feʼl oldida esa の qoʻyilmaydi.</p>"),

    q(f"<p>«Ovqatdan oldin» ni tanlang.</p>",
      [f"{SHOKUJI}のまえに", f"{SHOKUJI}まえに",
       f"{SHOKUJI}のまえで", f"{SHOKUJI}をまえに"],
      f"{SHOKUJI}のまえに",
      f"<p>Ot + <strong>の</strong> + まえに. で emas — bu joy emas, "
      f"vaqt.</p>"),

    q(f"<p>{ARAU} dan «yuvgandan keyin» ni てから bilan tanlang.</p>",
      [kara(ARATTE), f"{r('洗','あら')}いてから",
       f"{ARAU}から", f"{ARATTA}から"],
      kara(ARATTE),
      f"<p><strong>{kara(ARATTE)}</strong> — う → って, keyin から.</p>"),

    q(f"<p>Qaysi oʻzak gapning zamoniga qarab oʻzgaradi?</p>",
      ["Hech qaysi — oʻzakni qolip tanlaydi",
       "まえに oldidagi", "あとで oldidagi", "Hammasi"],
      "Hech qaysi — oʻzakni qolip tanlaydi",
      f"<p>Har uchala qolipning oʻzagi qatʼiy. Zamonni faqat gapning "
      f"<strong>oxirgi</strong> feʼli tashiydi.</p>"),

    q(f"<p>Nega まえに lugʻat shaklini, あとで esa た-shaklini oladi?</p>",
      ["Chunki oldingisi hali boʻlmagan, keyingisi esa boʻlib boʻlgan",
       "Chunki まえに qisqaroq soʻz",
       "Chunki あとで doim oʻtgan zamonda ishlatiladi",
       "Bu tartibsizlik, yodlanadi"],
      "Chunki oldingisi hali boʻlmagan, keyingisi esa boʻlib boʻlgan",
      f"<p>Oʻzbekchada ham shu farq bor: «chiq<strong>ish</strong>dan oldin» "
      f"va «chiq<strong>qan</strong>dan keyin». Shakl oʻsha ishning "
      f"tugagan-tugamaganiga qarab tanlanadi.</p>"),

    q("<p>〜てから va 〜たあとで farqi nima?</p>",
      ["てから birinchi ish tugashini taʼkidlaydi, あとで shunchaki tartibni",
       "あとで birinchi ish tugashini taʼkidlaydi",
       "てから faqat oʻtgan zamonda ishlatiladi",
       "Farqi yoʻq, ikkalasi bir xil"],
      "てから birinchi ish tugashini taʼkidlaydi, あとで shunchaki tartibni",
      f"<p>«Qoʻlni yuvgandan keyin ovqatlanaman» da てから tabiiyroq — "
      f"yuvish <em>shart</em>. «Darsdan keyin uyga boraman» da esa "
      f"あとで.</p>"),

    q(f"<p>{KURU} dan «kelishdan oldin» ni tanlang.</p>",
      [f"{maeni(KURU)}", f"{maeni(KITA)}", f"{KITE}まえに", f"{KI}まえに"],
      f"{maeni(KURU)}",
      f"<p><strong>{maeni(KURU)}</strong> — lugʻat shakli, demak oʻqilishi "
      f"ham lugʻat shaklidagidek: «くる».</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{kara(SHITE)}テレビを{r('見','み')}ます",
       f"{SURU}からテレビを{r('見','み')}ます",
       f"{SHITA}からテレビを{r('見','み')}ます",
       f"{SHI}からテレビを{r('見','み')}ます"],
      f"{kara(SHITE)}テレビを{r('見','み')}ます",
      f"<p>てから <strong>て-shaklini</strong> oladi: する → して → "
      f"<strong>してから</strong>.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{JUGYOU}のあとで{GK}へ{r('行','い')}きます",
       f"{JUGYOU}あとで{GK}へ{r('行','い')}きます",
       f"{JUGYOU}のあとに{GK}へ{r('行','い')}きます",
       f"{JUGYOU}をあとで{GK}へ{r('行','い')}きます"],
      f"{JUGYOU}のあとで{GK}へ{r('行','い')}きます",
      f"<p>Ot bilan ulanganda <strong>の</strong> kerak, va qolip "
      f"<strong>あとで</strong> — «あとに» emas.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{maeni(NERU)}{HON}を{r('読','よ')}みます",
       f"{atode(TABETA)}{GK}へ{r('行','い')}きます",
       f"{maeni(NETA)}{HON}を{r('読','よ')}みました",
       f"{kara(OKITE)}{KAO}を{r('洗','あら')}います"],
      f"{maeni(NETA)}{HON}を{r('読','よ')}みました",
      f"<p>まえに oldida <strong>lugʻat shakli</strong> turishi kerak: "
      f"<strong>{maeni(NERU)}</strong>. Gap oʻtgan zamonda boʻlishi buni "
      f"oʻzgartirmaydi.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{OKITE} → {kara(OKITE)}", f"{TABETA} → {atode(TABETA)}",
       f"{DERU} → {maeni(DETA)}", f"{ITTE} → {kara(ITTE)}"],
      f"{DERU} → {maeni(DETA)}",
      f"<p>まえに <strong>lugʻat shaklini</strong> oladi: "
      f"<strong>{maeni(DERU)}</strong>, «{maeni(DETA)}» emas.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {r('読','よ')}みます · "
      f"を · {HON} · {maeni(NERU)}</p>",
      [f"{maeni(NERU)}{HON}を{r('読','よ')}みます",
       f"{NERU}を{HON}まえに{r('読','よ')}みます",
       f"{r('読','よ')}みます{maeni(NERU)}{HON}を",
       f"を{HON}{maeni(NERU)}{r('読','よ')}みます"],
      f"{maeni(NERU)}{HON}を{r('読','よ')}みます",
      f"<p>まえに oʻz feʼliga yopishadi ({maeni(NERU)}), toʻldiruvchi esa "
      f"を oladi. Qolgan uchtasida qoʻshimchalar yoki feʼl notoʻgʻri "
      f"joyda.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{SHUKUDAI}を___テレビを"
      f"{r('見','み')}ます。</strong> («Uy vazifasini qilgandan keyin "
      f"televizor koʻraman.»)</p>",
      [kara(SHITE), maeni(SURU), f"{SHI}から", f"{SHITA}から"],
      kara(SHITE),
      f"<p><strong>{kara(SHITE)}</strong> — «qilgandan keyin». "
      f"«{maeni(SURU)}» esa «qilishdan oldin» — teskari maʼno.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>ラノ:</strong> "
      f"{JUGYOU}のあとで{r('何','なに')}をしますか。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"{r('友','とも')}だちに{ATTE}から{r('帰','かえ')}ります",
       f"{r('友','とも')}だちに{AI}から{r('帰','かえ')}ります",
       f"{r('友','とも')}だちに{AU}から{r('帰','かえ')}ります",
       f"{r('友','とも')}だちに{ATTA}から{r('帰','かえ')}ります"],
      f"{r('友','とも')}だちに{ATTE}から{r('帰','かえ')}ります",
      f"<p>てから <strong>て-shaklini</strong> oladi: {AU} → {ATTE} → "
      f"<strong>{kara(ATTE)}</strong>.</p>"),
]

# ══════════════════════════════════════════════════════════════════════
# PJ-38 — 〜ながら
# ══════════════════════════════════════════════════════════════════════
Q_PJ38 = [
    q("<p>〜ながら oldida qaysi shakl turadi?</p>",
      ["ます oʻzagi", "て-shakli", "た-shakli", "Lugʻat shakli"],
      "ます oʻzagi",
      f"<p>ます ni olib tashlang, qolgani oʻzak: {KIKI} + ながら = "
      f"<strong>{nagara(KIKI)}</strong>.</p>"),

    q(f"<p>{KIKU} dan ながら yasang.</p>",
      [nagara(KIKI), f"{KIKU}ながら", f"{KIITE}ながら", f"{KIITA}ながら"],
      nagara(KIKI),
      f"<p><strong>{nagara(KIKI)}</strong> — ます shakli "
      f"{r('聞','き')}きます, oʻzagi {KIKI}.</p>"),

    q(f"<p>{TABERU} dan ながら yasang.</p>",
      [nagara(TABE), f"{TABERU}ながら", f"{TABETE}ながら", f"{r('食','た')}べりながら"],
      nagara(TABE),
      f"<p><strong>{nagara(TABE)}</strong> — II guruhda oʻzak る siz "
      f"qolgan qism: {TABE}.</p>"),

    q(f"<p>{ARUKU} dan ながら yasang.</p>",
      [nagara(ARUKI), f"{ARUKU}ながら", f"{ARUITE}ながら", f"{r('歩','ある')}かながら"],
      nagara(ARUKI),
      f"<p><strong>{nagara(ARUKI)}</strong> — く い qatoriga tushadi: "
      f"{ARUKI}. Bu oʻsha ます oʻzagi.</p>"),

    q(f"<p>{SURU} va {KURU} dan ながら yasang.</p>",
      [f"{nagara(SHI)} · {nagara(KI)}", f"するながら · {r('来','く')}るながら",
       f"してながら · {r('来','き')}てながら", f"したながら · {r('来','き')}たながら"],
      f"{nagara(SHI)} · {nagara(KI)}",
      f"<p>ます shakllari します va {r('来','き')}ます, demak oʻzaklari "
      f"<strong>し</strong> va <strong>{r('来','き')}</strong>.</p>"),

    q(f"<p>«{ONGAKU}を{nagara(KIKI)}{BENKYOU}します» — asosiy ish qaysi?</p>",
      ["Oʻqish", "Musiqa tinglash", "Ikkalasi teng", "Aniqlab boʻlmaydi"],
      "Oʻqish",
      f"<p>Asosiy ish har doim <strong>oxirgi feʼl</strong>da. ながら bilan "
      f"belgilangan ish fon boʻlib qoladi.</p>"),

    q(f"<p>«{BENKYOU}{nagara(SHI)}{ONGAKU}を{r('聞','き')}きます» — asosiy ish "
      f"qaysi?</p>",
      ["Musiqa tinglash", "Oʻqish", "Ikkalasi teng", "Hech qaysi"],
      "Musiqa tinglash",
      f"<p>Bu safar oxirgi feʼl — {r('聞','き')}きます. Oʻrinlarni "
      f"almashtirsangiz, asosiy ish ham almashadi.</p>"),

    q("<p>ながら ning eng qatʼiy cheklovi nima?</p>",
      ["Ikkala ishning egasi bitta boʻlishi shart",
       "Ikkala ish ham oʻtgan zamonda boʻlishi shart",
       "Ikkala feʼl ham I guruhda boʻlishi shart",
       "Ikkitadan koʻp ish boʻlmasligi shart"],
      "Ikkala ishning egasi bitta boʻlishi shart",
      f"<p>Ikki egali gapni ながら bilan tuzib boʻlmaydi. «Men oʻqiyapman, "
      f"singlim televizor koʻryapti» — bu qolipga toʻgʻri kelmaydi.</p>"),

    q("<p>ながら bilan ulanadigan ishlar qanday boʻlishi kerak?</p>",
      ["Ikkalasi ham vaqt oladigan (davomli) ish",
       "Ikkalasi ham bir zumda tugaydigan ish",
       "Biri davomli, ikkinchisi bir zumlik",
       "Farqi yoʻq"],
      "Ikkalasi ham vaqt oladigan (davomli) ish",
      f"<p>Yurish, tinglash, yeyish, gaplashish — davomli. "
      f"{r('入','はい')}る kabi bir zumda tugaydigan ish bu qolipga "
      f"toʻgʻri kelmaydi.</p>"),

    q(f"<p>Boʻsh joyga nima tushadi?</p><p><strong>{ONGAKU}を___"
      f"{SHUKUDAI}をします。</strong></p>",
      [nagara(KIKI), f"{KIITE}から", f"{KIKU}まえに", f"{KIITA}あとで"],
      nagara(KIKI),
      f"<p><strong>{nagara(KIKI)}</strong> — ikki ish <strong>bir "
      f"vaqtda</strong>. Qolgan uchtasi ketma-ketlikni bildiradi.</p>"),

    q("<p>〜て va 〜ながら farqi nima?</p>",
      ["〜て ketma-ket, 〜ながら bir vaqtda",
       "〜て bir vaqtda, 〜ながら ketma-ket",
       "〜ながら faqat oʻtgan zamonda",
       "Farqi yoʻq"],
      "〜て ketma-ket, 〜ながら bir vaqtda",
      f"<p>{TABETE}、{r('行','い')}きます — avval yedim, keyin bordim. "
      f"{nagara(TABE)}{MIRU} — ikkalasi bir vaqtda.</p>"),

    q(f"<p>«{nagara(HATARAKI)}{BENKYOU}しています» nima maʼnoni beradi?</p>",
      ["Ishlaydi va shu bilan birga oʻqiydi — hayotining bir davri",
       "Ayni daqiqada ish joyida oʻqiyapti",
       "Ishlagandan keyin oʻqiydi",
       "Ishlashni xohlaydi"],
      "Ishlaydi va shu bilan birga oʻqiydi — hayotining bir davri",
      f"<p>ながら uzun muddatga ham yaraydi. «Ishlagandan keyin» boʻlsa "
      f"<strong>{kara(HATARAITE)}</strong> deyilardi.</p>"),

    q(f"<p>ながら zamon oladimi?</p>",
      ["Yoʻq — zamonni oxirgi feʼl tashiydi", "Ha, ながらました boʻladi",
       "Ha, ながらです boʻladi", "Faqat inkorda"],
      "Yoʻq — zamonni oxirgi feʼl tashiydi",
      f"<p>{nagara(ARUKI)}{r('話','はな')}しました — ながら oʻzgarmadi, "
      f"oʻtgan zamonni {r('話','はな')}しました tashidi.</p>"),

    q(f"<p>ながら oldidagi oʻzak boshqa qaysi qolipda ishlatiladi?</p>",
      ["〜たいです", "〜てから", "〜たあとで", "〜ないでください"],
      "〜たいです",
      f"<p>Ikkalasi ham <strong>ます oʻzagini</strong> oladi: "
      f"{nagara(IKI)} va {tai(IKI)}. Qolgan uchtasi boshqa oʻzaklardan.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{nagara(ARUKI)}{r('話','はな')}しました",
       f"{ARUKU}ながら{r('話','はな')}しました",
       f"{ARUITE}ながら{r('話','はな')}しました",
       f"{nagara(ARUKI)}{r('話','はな')}しましたながら"],
      f"{nagara(ARUKI)}{r('話','はな')}しました",
      f"<p>ながら <strong>ます oʻzagiga</strong> qoʻshiladi va zamon "
      f"olmaydi.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"テレビを{nagara(MI)}{r('食','た')}べます",
       f"テレビを{MIRU}ながら{r('食','た')}べます",
       f"テレビを{MITE}ながら{r('食','た')}べます",
       f"テレビを{MITA}ながら{r('食','た')}べます"],
      f"テレビを{nagara(MI)}{r('食','た')}べます",
      f"<p>{MIRU} ning ます oʻzagi — <strong>{MI}</strong> (bitta tovush), "
      f"demak {nagara(MI)}.</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{nagara(KIKI)}{BENKYOU}します",
       f"{nagara(TABE)}テレビを{r('見','み')}ます",
       f"{ARUKU}ながら{r('話','はな')}します",
       f"{nagara(HATARAKI)}{BENKYOU}します"],
      f"{ARUKU}ながら{r('話','はな')}します",
      f"<p>ながら lugʻat shakliga qoʻshilmaydi. Toʻgʻrisi — "
      f"<strong>{nagara(ARUKI)}</strong>.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{KIKU} → {nagara(KIKI)}", f"{TABERU} → {nagara(TABE)}",
       f"{SURU} → {SURU}ながら", f"{KURU} → {nagara(KI)}"],
      f"{SURU} → {SURU}ながら",
      f"<p>する ning ます oʻzagi — <strong>し</strong>, demak "
      f"<strong>{nagara(SHI)}</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {BENKYOU}します · を · "
      f"{ONGAKU} · {nagara(KIKI)}</p>",
      [f"{ONGAKU}を{nagara(KIKI)}{BENKYOU}します",
       f"{nagara(KIKI)}{ONGAKU}を{BENKYOU}します",
       f"を{ONGAKU}{nagara(KIKI)}{BENKYOU}します",
       f"{ONGAKU}{nagara(KIKI)}を{BENKYOU}します"],
      f"{ONGAKU}を{nagara(KIKI)}{BENKYOU}します",
      f"<p>Toʻldiruvchi va uning を qoʻshimchasi oʻz feʼlidan "
      f"({nagara(KIKI)}) oldin turadi, asosiy feʼl esa oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イノム:</strong> "
      f"パリさんは{ONGAKU}を{nagara(KIKI)}{BENKYOU}しますか。</p>"
      f"<p><strong>パリ:</strong> ___</p>",
      [f"はい、いつも{nagara(KIKI)}{BENKYOU}します",
       f"はい、いつも{KIKU}ながら{BENKYOU}します",
       f"はい、いつも{KIITE}から{BENKYOU}します",
       f"はい、いつも{nagara(KIKI)}{BENKYOU}しますながら"],
      f"はい、いつも{nagara(KIKI)}{BENKYOU}します",
      f"<p>Savol qaysi shaklda berilsa, javob ham shu shaklda qaytadi. "
      f"«{kara(KIITE)}» esa «tinglagandan keyin» — boshqa maʼno.</p>"),
]


# ══════════════════════════════════════════════════════════════════════
# PJ-39 — xohish
# ══════════════════════════════════════════════════════════════════════
Q_PJ39 = [
    q("<p>〜たい oldida qaysi shakl turadi?</p>",
      ["ます oʻzagi", "Lugʻat shakli", "て-shakli", "た-shakli"],
      "ます oʻzagi",
      f"<p>{IKI} + たい = <strong>{tai(IKI)}</strong>. Bu ながら bilan "
      f"bir xil oʻzak.</p>"),

    q(f"<p>{IKU} dan «bormoqchiman» ni tanlang.</p>",
      [tai(IKI), f"{IKU}たいです", f"{ITTE}たいです", f"{ITTA}たいです"],
      tai(IKI),
      f"<p><strong>{tai(IKI)}</strong> — ます oʻzagi {IKI}, keyin たいです.</p>"),

    q(f"<p>{YASUMU} dan «dam olmoqchiman» ni tanlang.</p>",
      [tai(YASUMI), f"{YASUMU}たいです", f"{YASUNDE}たいです",
       f"{r('休','やす')}またいです"],
      tai(YASUMI),
      f"<p><strong>{tai(YASUMI)}</strong> — む い qatoriga tushadi: "
      f"{YASUMI}.</p>"),

    q("<p>たい qanday tuslanadi?</p>",
      ["い-sifat kabi", "な-sifat kabi", "Feʼl kabi", "Ot kabi"],
      "い-sifat kabi",
      f"<p>たい い bilan tugaydi va PJ-25 dagi qoida boʻyicha tuslanadi: "
      f"い → くない, い → かった.</p>"),

    q(f"<p>«Bormoqchi emasman» ni tanlang.</p>",
      [takunai(IKI), f"{IKI}たいではありません",
       f"{IKI}たいません", f"{IKI}たないです"],
      takunai(IKI),
      f"<p><strong>{takunai(IKI)}</strong> — い → <strong>くない</strong>, "
      f"xuddi {r('安','やす')}い → {r('安','やす')}くない kabi.</p>"),

    q(f"<p>«Bormoqchi edim» ni tanlang.</p>",
      [takatta(IKI), f"{IKI}たいでした",
       f"{IKI}たいました", f"{IKI}たくでした"],
      takatta(IKI),
      f"<p><strong>{takatta(IKI)}</strong> — たい い-sifat, demak zamonni "
      f"<strong>oʻzi</strong> tashiydi. «たいでした» notoʻgʻri.</p>"),

    q("<p>〜がほしいです oldida nima turadi?</p>",
      ["Ot", "Feʼlning ます oʻzagi", "て-shakli", "Lugʻat shakli"],
      "Ot",
      f"<p>ほしい — <strong>narsa</strong> uchun: {JITENSHA}がほしいです. "
      f"Ish uchun esa たい ishlatiladi.</p>"),

    q(f"<p>«Velosiped kerak» ni tanlang.</p>",
      [f"{JITENSHA}がほしいです", f"{JITENSHA}をほしいです",
       f"{JITENSHA}にほしいです", f"{JITENSHA}がほしいます"],
      f"{JITENSHA}がほしいです",
      f"<p>ほしい — <strong>い-sifat</strong>, feʼl emas: を olmaydi va "
      f"います ham olmaydi. Kerak boʻlgan narsa <strong>が</strong> oladi.</p>"),

    q(f"<p>Nega ほしい が oladi, を emas?</p>",
      ["Chunki ほしい sifat, feʼl emas",
       "Chunki ほしい uzun soʻz",
       "Chunki が doim narsalar bilan keladi",
       "Chunki を faqat odamlar bilan keladi"],
      "Chunki ほしい sifat, feʼl emas",
      f"<p>を — feʼlning toʻldiruvchisi. ほしい esa {r('好','す')}き kabi "
      f"sifat, shuning uchun kerak boʻlgan narsa gapda <strong>ega</strong> "
      f"boʻlib turadi.</p>"),

    q(f"<p>«Pul kerak edi» ni tanlang.</p>",
      [f"{OKANE}がほしかったです", f"{OKANE}がほしいでした",
       f"{OKANE}をほしかったです", f"{OKANE}がほしくでした"],
      f"{OKANE}がほしかったです",
      f"<p>ほしい ham い-sifat: い → <strong>かった</strong>.</p>"),

    q(f"<p>たい va ほしい farqi nima?</p>",
      ["たい ish uchun (feʼl bilan), ほしい narsa uchun (ot bilan)",
       "たい narsa uchun, ほしい ish uchun",
       "たい muloyimroq",
       "Farqi yoʻq"],
      "たい ish uchun (feʼl bilan), ほしい narsa uchun (ot bilan)",
      f"<p>{HON}が{tai(YOMI)} — «kitob oʻqimoqchiman». {HON}がほしいです — "
      f"«kitob kerak».</p>"),

    q(f"<p>«Sushi yemoqchiman» da toʻldiruvchi qaysi qoʻshimchani oladi?</p>",
      ["が yoki を — ikkalasi ham toʻgʻri", "Faqat を", "Faqat に", "Faqat で"],
      "が yoki を — ikkalasi ham toʻgʻri",
      f"<p>すしが{tai(TABE)} va すしを{tai(TABE)} — ikkalasi ham ishlatiladi. "
      f"が biroz anʼanaviyroq va sifat mantiqiga mos.</p>"),

    q(f"<p>Nega «{r('彼','かれ')}は{tai(IKI)}» deyilmaydi?</p>",
      ["Xohish — ichki tuygʻu; boshqa odamning ichi bilgandek gapirilmaydi",
       "Chunki 彼 juda rasmiy soʻz",
       "Chunki たい faqat oʻtgan zamonda ishlatiladi",
       "Chunki 行く — I guruh feʼli"],
      "Xohish — ichki tuygʻu; boshqa odamning ichi bilgandek gapirilmaydi",
      f"<p>Siz faqat <strong>oʻzingiz</strong> haqingizda ishlatasiz. "
      f"Savolda esa mumkin: <strong>{IKI}たいですか</strong>.</p>"),

    q(f"<p>Ustozdan kitob soʻramoqchisiz. Qaysi biri toʻgʻriroq?</p>",
      [f"{HON}を{r('借','か')}りてもいいですか",
       f"{HON}が{r('借','か')}りたいです",
       f"{HON}がほしいです",
       f"{HON}を{r('借','か')}りたくないです"],
      f"{HON}を{r('借','か')}りてもいいですか",
      f"<p>Katta yoshli odamdan soʻraganda <strong>xohish emas, "
      f"ruxsat</strong> soʻraladi. «たいです» oʻz xohishini roʻyxatga olib "
      f"qoʻygandek eshitiladi.</p>"),

    q(f"<p>{KURU} dan «kelmoqchiman» — <strong>来たいです</strong> — qanday "
      f"oʻqiladi?</p>",
      ["きたいです", "くたいです", "こたいです", "きりたいです"],
      "きたいです",
      f"<p>ます oʻzagi — <strong>{KI}</strong>, demak oʻqilishi ham ます "
      f"shaklidagidek: «きたいです». Bu kanji endi beshta oʻqilishga ega.</p>"),

    q(f"<p>Qaysi gap toʻgʻri?</p>",
      [f"{NIHON}へ{tai(IKI)}", f"{NIHON}へ{IKU}たいです",
       f"{NIHON}へ{IKI}たいでした", f"{NIHON}へ{ITTE}たいです"],
      f"{NIHON}へ{tai(IKI)}",
      f"<p>たい <strong>ます oʻzagiga</strong> qoʻshiladi va い-sifat kabi "
      f"tuslanadi — «たいでした» emas, «たかったです».</p>"),

    q(f"<p>Qaysi gapda xato bor?</p>",
      [f"{OKANE}がほしいです", f"{JITENSHA}をほしいです",
       f"{JIKAN}がほしかったです", f"{HON}が{tai(YOMI)}"],
      f"{JITENSHA}をほしいです",
      f"<p>ほしい sifat — <strong>が</strong> oladi, を emas.</p>"),

    q(f"<p>Qaysi qatorda xato bor?</p>",
      [f"{TABERU} → {tai(TABE)}", f"{YOMU} → {tai(YOMI)}",
       f"{IKU} → {IKI}たいでした", f"{SURU} → {tai(SHI)}"],
      f"{IKU} → {IKI}たいでした",
      f"<p>たい い-sifat, zamonni oʻzi tashiydi: "
      f"<strong>{takatta(IKI)}</strong>.</p>"),

    q(f"<p>Soʻzlarni toʻgʻri tartibda joylashtiring: {tai(IKI)} · へ · "
      f"{NIHON}</p>",
      [f"{NIHON}へ{tai(IKI)}", f"へ{NIHON}{tai(IKI)}",
       f"{tai(IKI)}{NIHON}へ", f"{NIHON}{tai(IKI)}へ"],
      f"{NIHON}へ{tai(IKI)}",
      f"<p>Yoʻnalish qoʻshimchasi へ oʻz otidan keyin turadi, feʼl esa "
      f"gap oxirida.</p>"),

    q(f"<p>Suhbatni toʻldiring.</p><p><strong>イムロン:</strong> "
      f"{r('夏休','なつやす')}みに{r('何','なに')}がしたいですか。</p>"
      f"<p><strong>ムニラ:</strong> ___</p>",
      [f"{NIHON}へ{tai(IKI)}。でも{OKANE}がほしいです",
       f"{NIHON}へ{tai(IKI)}。でも{OKANE}をほしいです",
       f"{NIHON}へ{IKU}たいです。でも{OKANE}がほしいです",
       f"{NIHON}へ{IKI}たいでした。でも{OKANE}がほしいです"],
      f"{NIHON}へ{tai(IKI)}。でも{OKANE}がほしいです",
      f"<p>Ish uchun <strong>たい</strong>, narsa uchun <strong>が"
      f"ほしい</strong> — va ikkalasi ham hozirgi zamonda.</p>"),
]


PRACTICES = [
    {
        "title":       "PJ-37 Mashq: 〜てから, 〜まえに, 〜あとで",
        "tutorial":    "PJ-37:",
        "description": "Ish tartibi. Uchta qolip, uchta har xil oʻzak — va "
                       "oʻzakni qolip tanlaydi, gapning zamoni emas.",
        "questions":   Q_PJ37,
        **DEFAULTS,
    },
    {
        "title":       "PJ-38 Mashq: 〜ながら — bir vaqtda ikki ish",
        "tutorial":    "PJ-38:",
        "description": "ます oʻzagi + ながら. Asosiy ish har doim oxirgi feʼl, "
                       "va ikkala ishning egasi bitta boʻlishi shart.",
        "questions":   Q_PJ38,
        **DEFAULTS,
    },
    {
        "title":       "PJ-39 Mashq: 〜たいです va 〜がほしいです",
        "tutorial":    "PJ-39:",
        "description": "Xohish. Ikkalasi ham い-sifat kabi tuslanadi va "
                       "ikkalasi ham が oladi.",
        "questions":   Q_PJ39,
        **DEFAULTS,
    },
]
