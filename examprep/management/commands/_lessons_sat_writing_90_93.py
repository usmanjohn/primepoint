# -*- coding: utf-8 -*-
"""
SAT Reading & Writing — WRITING lessons 90-93.

"Yakuniy aralash amaliyot (Full Mixed Practice)" — the last topic of the whole
course. Nothing new is taught here: every question is one the pupil has already met
a rule for, and the only new thing is that nobody says which rule.

W90 drills Standard English Conventions against the clock, W91 does the same for
Expression of Ideas, W92 is a full 14-question writing half-module in the exam's own
domain order, and W93 is the triage lesson — which questions to bank first when five
minutes are left.

⚠️ This is the OTHER half of the same 54-question section. Its two domains are
Standard English Conventions (~26%) and Expression of Ideas (~20%). There is no
essay and nothing is written by the pupil — every question is a four-choice MCQ,
exactly as in the reading half. See toc_sat_writing.txt and STYLE_GUIDE_SAT_RW.md.
"""

TRACK = {
    "name":    "SAT",
    "summary": "Digital SAT — Reading and Writing bo'limiga savol turlari bo'yicha "
               "tayyorgarlik. Imtihonning matematik yarmi Prime SAT Math kursida.",
    "icon":    "bi-mortarboard",
    "color":   "#7c3aed",
    "order":   3,
}

TOPIC_MIX = {
    "title":   "Yakuniy aralash amaliyot (Full Mixed Practice)",
    "summary": "Butun yozuv yarmi aralash: hech kim savol turini aytmaydi. "
               "Vaqt bilan ishlash, to'liq modul va oxirgi besh daqiqa taktikasi.",
    "icon":    "bi-flag-fill",
    "order":   9,
}

TIP   = ('<div style="background:#ecfdf5;border-left:4px solid #10b981;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>💡 Maslahat:</strong> {}</div>')
WARN  = ('<div style="background:#fffbeb;border-left:4px solid #f59e0b;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>⚠️ Tuzoq:</strong> {}</div>')
NOTE  = ('<div style="background:#eff6ff;border-left:4px solid #3b82f6;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📌 Eslatma:</strong> {}</div>')
EXAMP = ('<div style="background:#faf5ff;border-left:4px solid #a855f7;padding:12px 16px;'
         'border-radius:8px;margin:16px 0;"><strong>📝 Namuna:</strong> {}</div>')


def why(rows):
    """Build an .sr-why choice autopsy. rows = [(ok, choice_text, uzbek_reason), ...]

    The choice text MUST start with the choice's own opening words — the pupil finds
    the row by scanning it against a shuffled list (guide §6).
    """
    out = ['<div class="sr-why">']
    for ok, choice, reason in rows:
        kind = 'ok' if ok else 'no'
        tag = "TO‘G‘RI" if ok else "TUZOQ"
        out.append(
            f'<div class="sr-why__row sr-why__row--{kind}">'
            f'<span class="sr-why__tag">{tag}</span>'
            f'<span class="sr-why__text"><b>{choice}</b> — {reason}</span></div>'
        )
    out.append('</div>')
    return ''.join(out)


def q(passage, stem):
    return f'<div class="sr-passage">{passage}</div><p><strong>{stem}</strong></p>'


def conv_q(passage):
    """Standard English Conventions: the stem never varies."""
    return q(passage, "Which choice completes the text so that it conforms to the "
                      "conventions of Standard English?")


def precise_q(passage):
    """Word Choice / precision: the stem the exam uses when a vague pronoun is the fault."""
    return q(passage, "Which choice completes the text with the most logical and precise "
                      "word or phrase?")


def trans_q(passage):
    """Transitions: the stem never varies either."""
    return q(passage, "Which choice completes the text with the most logical "
                      "transition?")


def notes_q(head, bullets, goal):
    """Rhetorical Synthesis: the research-notes card, then the goal sentence."""
    items = ''.join(f'<li>{b}</li>' for b in bullets)
    return ('<div class="sr-notes">'
            f'<p class="sr-notes__head">{head}</p><ul>{items}</ul></div>'
            f'<p><strong>{goal}</strong></p>')


def choices_html(items):
    """The static A/B/C/D list used in a WORKED example (not a shuffled choices block)."""
    return '<ol type="A">' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>'


def qnum(n, kind):
    return (f'<p style="margin:0 0 4px;"><span style="background:#ede9fe;color:#5b21b6;'
            f'border-radius:999px;padding:2px 10px;font-size:.82rem;font-weight:600;">'
            f'{n}-savol · {kind}</span></p>')


LESSONS = [
# ═══════════════════════════════════════════════════════════════════════════
# Writing 90
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_MIX,
    "title": "SAT R&W W90: Mixed Practice 1 — Conventions Under Time (25 seconds a question)",
    "summary": "Sakkiz Standard English Conventions savoli, hech biri o'z turini "
               "aytmaydi. Maqsad — javobni topish emas, uni tez topish.",
    "order": 90,
    "blocks": [
        {"rich_text": (
            "<h2>Nega 25 soniya</h2>"
            "<p>Modulda 27 savol va 32 daqiqa bor — o'rtacha "
            "<strong>71 soniya</strong>. Lekin Rhetorical Synthesis "
            "va uzun matnli savollar ikki daqiqagacha oladi, va bu "
            "vaqtni kimdir tejashi kerak.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Standard "
                "English Conventions savollari — vaqt "
                "bankingiz.</strong> Ular qoidaga tayanadi, matnni "
                "talqin qilishni talab qilmaydi, va o'rgangan odam "
                "uchun <u>25-40 soniya</u> yetadi.</p>")
            + "<p>Har biriga sarflagan har bir ortiqcha soniya — "
            "Rhetorical Synthesis'dan o'g'irlangan soniya.</p>"
            + '<span class="sr-time">⏱ 8 savol · 4 daqiqa</span>'
        )},

        {"rich_text": (
            "<h3>Tezlikning bitta siri: variantlarni birinchi o'qing</h3>"
            + '<div class="pp-steps" data-pp-steps data-pp-more="Keyingi qadam ▸">'
            + "<div class=\"pp-step\"><p><strong>1. To'rt variantga "
              "qarang</strong> va ular <u>nima bilan</u> farq qilishini "
              "ayting. Bu savol turini bepul beradi.</p></div>"
            + "<div class=\"pp-step\"><p><strong>2. Faqat kerakli "
              "joyni o'qing.</strong> Vergul savoli uchun bo'sh joyning "
              "ikki tomoni yetadi; moslashuv uchun ega; zamon uchun "
              "abzats.</p></div>"
            + "<div class=\"pp-step\"><p><strong>3. Qoidani ayting, "
              "keyin belgilang.</strong> «Chunki shunday "
              "eshitiladi» — bu javob emas, bu taxmin.</p></div>"
            + '</div>'
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Variantlar farqi</th><th>Tur</th>"
              "<th>Qayerga qaraysiz</th></tr></thead>"
              "<tbody>"
              "<tr><td>. ; , va —</td><td>chegara</td>"
              "<td>bo'sh joyning ikki tomoni: ikkovi ham to'liq "
              "gapmi?</td></tr>"
              "<tr><td>vergul bor / yo'q</td><td>qo'shimcha bo'lak</td>"
              "<td>ikkinchi vergul qayerda</td></tr>"
              "<tr><td><em>is / are / was</em></td><td>moslashuv</td>"
              "<td>haqiqiy ega</td></tr>"
              "<tr><td><em>has / had / will have</em></td><td>zamon</td>"
              "<td>abzatsdagi vaqt so'zlari</td></tr>"
              "<tr><td><em>-ing / shaxsli fe'l</em></td><td>kesim</td>"
              "<td>gapda boshqa kesim bormi</td></tr>"
              "<tr><td><em>its / their / whom</em></td><td>olmosh</td>"
              "<td>antecedent</td></tr>"
              "<tr><td><em>-s / -'s / -s'</em></td><td>apostrof</td>"
              "<td>keyin ot bormi, egasi nechta</td></tr>"
              "<tr><td>butun gaplar</td><td>osilib qolgan bo'lak</td>"
              "<td>faqat birinchi ot</td></tr>"
              "</tbody></table>"
            + '</div></div>'
        )},

        {
            "rich_text": qnum(1, "Conventions") + conv_q(
                "<p>The stone used for the cathedral came from a quarry eleven miles away "
                "and was moved in winter on sledges over frozen "
                "<span class=\"sr-blank\"></span> a loaded cart would have sunk to the "
                "axle on the same route in any other season.</p>"),
            "choices": [
                {"text": "ground;", "is_correct": True},
                {"text": "ground,", "is_correct": False},
                {"text": "ground", "is_correct": False},
                {"text": "ground, which", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joyning ikki tomoni ham to'liq gap: "
                "<em>The stone … was moved</em> va <em>a loaded cart "
                "would have sunk</em>. Ikki mustaqil gapni "
                "bog'lovchisiz ulaydigan yagona belgi — "
                "<mark>nuqtali vergul</mark>.</p>"
                + why([
                    (True, "ground;",
                     "nuqtali vergul ikki mustaqil gapni "
                     "bog'lovchisiz ulaydi."),
                    (False, "ground,",
                     "vergul splaysi."),
                    (False, "ground",
                     "belgisiz qo'shilish (run-on)."),
                    (False, "ground, which",
                     "nisbiy olmosh ikkinchi gapni ergash gapga "
                     "aylantiradi, lekin unda allaqachon o'z egasi "
                     "bor (<em>a loaded cart</em>) — natijada "
                     "gap buziladi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Conventions") + conv_q(
                "<p>The list of ships lost in the gale of 1881, compiled from the customs "
                "books of four ports and never published in full, "
                "<span class=\"sr-blank\"></span> a hundred and thirty names, of which "
                "nineteen belonged to the same village.</p>"),
            "choices": [
                {"text": "runs to", "is_correct": True},
                {"text": "run to", "is_correct": False},
                {"text": "running to", "is_correct": False},
                {"text": "have run to", "is_correct": False},
            ],
            "explanation": (
                "<p>Predlogli birikmalarni va vergulli qo'shimchani "
                "o'chiring: <em>The list</em> <s>of ships lost…</s> "
                "<s>, compiled from…,</s> <mark>runs to</mark>.</p>"
                "<p>Ega — <em>The list</em>, birlik. Va gapda boshqa "
                "asosiy kesim yo'q, demak shaxsli shakl "
                "kerak.</p>"
                + why([
                    (True, "runs to",
                     "birlik shaxsli kesim — ikkala talab ham."),
                    (False, "run to",
                     "ko'plik: <em>ships</em>, <em>books</em> yoki "
                     "<em>ports</em> ga moslashgan."),
                    (False, "running to",
                     "sifatdosh — gap fragment bo'lib qoladi."),
                    (False, "have run to",
                     "ko'plik yordamchi, va perfect uchun asos "
                     "yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Conventions") + conv_q(
                "<p>Left in the ground over winter and lifted only after the first hard "
                "frost, <span class=\"sr-blank\"></span> The change is not in the sugar "
                "itself but in what the cold does to the starch already in the "
                "root.</p>"),
            "choices": [
                {"text": "parsnips taste noticeably sweeter.", "is_correct": True},
                {"text": "the sweetness of parsnips is noticeably greater.",
                 "is_correct": False},
                {"text": "there is a noticeable sweetness to parsnips.",
                 "is_correct": False},
                {"text": "gardeners find parsnips noticeably sweeter.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>NIMA yerda qoldirilgan?</strong> "
                "<mark>Sabzi-pasternak.</mark> Shirinlik ham, "
                "bog'bonlar ham emas.</p>"
                + why([
                    (True, "parsnips taste noticeably sweeter",
                     "verguldan keyingi birinchi ot — "
                     "<em>parsnips</em>."),
                    (False, "the sweetness of parsnips is",
                     "ega — <em>the sweetness</em>; shirinlik yerda "
                     "qishlamaydi."),
                    (False, "there is a noticeable sweetness",
                     "<em>there</em> hech narsani "
                     "bildirmaydi."),
                    (False, "gardeners find parsnips",
                     "bog'bonlar yerda qoldirilmagan — bu variant "
                     "ma'noda mantiqiy tuyuladi, grammatikada "
                     "kulgili."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Conventions") + conv_q(
                "<p>The two dialects are separated by about forty miles of moorland, and "
                "each keeps words the other lost. Speakers on the northern side still use "
                "eleven terms for kinds of snow, and <span class=\"sr-blank\"></span> "
                "vocabulary for peat cutting is the richer of the two by a wide "
                "margin.</p>"),
            "choices": [
                {"text": "their", "is_correct": True},
                {"text": "they're", "is_correct": False},
                {"text": "there", "is_correct": False},
                {"text": "its", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyin darrov ot "
                "(<em>vocabulary</em>) — egalik kerak. "
                "Antecedent — <em>Speakers</em>, "
                "<mark>ko'plik</mark>.</p>"
                + why([
                    (True, "their",
                     "ko'plik egalik olmoshi, otdan oldin."),
                    (False, "they're",
                     "<em>they are vocabulary</em> — yoyish sinovi "
                     "darrov rad qiladi."),
                    (False, "there",
                     "joy so'zi; egalikni bildirmaydi."),
                    (False, "its",
                     "egalik, lekin birlik — antecedent "
                     "<em>Speakers</em>."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Conventions") + conv_q(
                "<p>A hand-set page was locked into its frame with wedges, and the "
                "compositor tested it by lifting one corner: if a single letter fell out, "
                "the whole page had to be tightened again. The "
                "<span class=\"sr-blank\"></span> speed was measured in letters an hour, "
                "and a good one set about fifteen hundred.</p>"),
            "choices": [
                {"text": "compositor's", "is_correct": True},
                {"text": "compositors", "is_correct": False},
                {"text": "compositors'", "is_correct": False},
                {"text": "compositors's", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyin ot (<em>speed</em>) — egalik "
                "kerak. Egasi nechta? Matn butun abzatsda "
                "<em>the compositor</em> — <mark>birlik</mark> — "
                "haqida gapiradi, va davomi ham "
                "<em>a good <u>one</u></em> deydi.</p>"
                + why([
                    (True, "compositor's",
                     "birlik egalik shakli — abzatsning o'zi bilan "
                     "mos."),
                    (False, "compositors'",
                     "ko'p egali shakl; matn bitta ishchining "
                     "ishini tasvirlaydi."),
                    (False, "compositors",
                     "egalikni bildirmaydi."),
                    (False, "compositors's",
                     "bunday shakl yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Conventions") + conv_q(
                "<p>The habit of building a boat for this coast with two keels rather than "
                "<span class=\"sr-blank\"></span> from a single practical fact: the "
                "harbour dries out completely at low water, and a boat with one keel "
                "would fall on its side in the mud twice a day.</p>"),
            "choices": [
                {"text": "one comes", "is_correct": True},
                {"text": "one, comes", "is_correct": False},
                {"text": "one comes,", "is_correct": False},
                {"text": "one, comes,", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Ega:</strong> <em>The habit of building a boat "
                "for this coast with two keels rather than one</em> — "
                "o'n olti so'zlik uzun birikma. <strong>Kesim:</strong> "
                "<em>comes</em>.</p>"
                "<p>Ega qanchalik uzun bo'lsa ham, uni kesimidan "
                "<mark>vergul ajratmaydi</mark> (44-dars). Nafas "
                "olgingiz kelgani vergul qo'yish uchun asos "
                "emas.</p>"
                + why([
                    (True, "one comes",
                     "vergulsiz: ega bevosita kesimga "
                     "ulanadi."),
                    (False, "one, comes",
                     "<strong>eng ko'p tanlanadigan xato:</strong> "
                     "uzun eganing oxiriga vergul qo'yish."),
                    (False, "one comes,",
                     "kesim bilan to'ldiruvchi orasiga vergul — "
                     "yana taqiqlangan o'rin."),
                    (False, "one, comes,",
                     "kesimni ikki tomondan vergulga olish uni "
                     "qo'shimcha bo'lakka aylantiradi; kesim "
                     "qo'shimcha bo'lolmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(7, "Conventions") + conv_q(
                "<p>Rye was sown in September and cut in July, wheat was sown a month "
                "later and cut at the same time, and <span class=\"sr-blank\"></span> in "
                "the spring on land that had carried neither of them. The rotation was "
                "fixed by the manor court and did not change for two centuries.</p>"),
            "choices": [
                {"text": "barley was sown", "is_correct": True},
                {"text": "barley being sown", "is_correct": False},
                {"text": "with barley sown", "is_correct": False},
                {"text": "the sowing of barley", "is_correct": False},
            ],
            "explanation": (
                "<p>Ro'yxatning oldingi ikki bo'lagi — to'liq gaplar: "
                "<em>Rye <u>was sown</u>…</em>, <em>wheat "
                "<u>was sown</u>…</em>. Uchinchisi ham "
                "<mark>ega + shaxsli kesim</mark> bo'lishi "
                "kerak.</p>"
                + why([
                    (True, "barley was sown",
                     "ega + shaxsli kesim, va aynan boshqa "
                     "ikkitasi kabi majhul nisbatda."),
                    (False, "barley being sown",
                     "sifatdosh bo'lagi; parallellik "
                     "buziladi."),
                    (False, "with barley sown",
                     "predlogli birikma."),
                    (False, "the sowing of barley",
                     "ot birikmasi."),
                ])
            ),
        },

        {
            "rich_text": qnum(8, "Conventions") + conv_q(
                "<p>The <span class=\"sr-blank\"></span> names are cut into the waist of a "
                "bell rather than the crown, which is why they survive on bells that have "
                "been re-hung twice and had the whole top of the casting replaced.</p>"),
            "choices": [
                {"text": "founders'", "is_correct": True},
                {"text": "founders", "is_correct": False},
                {"text": "founders's", "is_correct": False},
                {"text": "founder", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyin ot (<em>names</em>) — egalik "
                "kerak. Egasi — quyuvchilar, va <em>names</em> "
                "ko'plikda: <mark>ko'p egalik</mark>. Muntazam "
                "ko'plik <em>-s</em> bilan tugagani uchun faqat "
                "apostrof.</p>"
                + why([
                    (True, "founders'",
                     "ko'p egali egalik shakli."),
                    (False, "founders",
                     "egalikni bildirmaydi."),
                    (False, "founders's",
                     "<em>-s</em> bilan tugagan ko'plikka ikkinchi "
                     "<em>s</em> qo'shilmaydi."),
                    (False, "founder",
                     "birlik va egaliksiz."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>O'zingizni tekshiring</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Savol</th><th>Tur</th><th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td>1</td><td>chegara: ikki mustaqil gap</td><td>30-32</td></tr>"
              "<tr><td>2</td><td>moslashuv + shaxsli kesim</td><td>50-51, 54</td></tr>"
              "<tr><td>3</td><td>osilib qolgan bo'lak</td><td>72</td></tr>"
              "<tr><td>4</td><td>their / they're / there</td><td>61</td></tr>"
              "<tr><td>5</td><td>apostrof: birlik egalik</td><td>70</td></tr>"
              "<tr><td>6</td><td>ega bilan kesim orasida vergul yo'q</td>"
              "<td>44</td></tr>"
              "<tr><td>7</td><td>parallellik</td><td>73</td></tr>"
              "<tr><td>8</td><td>apostrof: ko'p egalik</td><td>70-71</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Xato qilgan savolingizni turi bo'yicha belgilang va "
                "<u>o'sha darsga</u> qayting. Ikki xato bir turdan "
                "chiqsa — bu tasodif emas, bu teshik.")
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Avval <strong>variantlarga</strong> qarang — ular "
              "savol turini bepul aytadi.</li>"
              "<li>Matnning faqat kerakli qismini o'qing.</li>"
              "<li>Qoidani ovoz chiqarmay ayting, keyin "
              "belgilang.</li>"
              "<li>Conventions — bu sizning <strong>vaqt "
              "bankingiz</strong>. Uni tejang, "
              "Synthesis'ga sarflang.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 91
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_MIX,
    "title": "SAT R&W W91: Mixed Practice 2 — Expression of Ideas Under Time",
    "summary": "Sakkiz Expression of Ideas savoli: bog'lovchi so'zlar va "
               "Rhetorical Synthesis. Bu savollar sekinroq — va shunday bo'lishi kerak.",
    "order": 91,
    "blocks": [
        {"rich_text": (
            "<h2>Bu yerda shoshilmang</h2>"
            "<p>90-dars Conventions'ni 25 soniyaga siqishni "
            "o'rgatdi. Bu darsning maqsadi teskari: tejalgan vaqtni "
            "<strong>shu yerga</strong> sarflash.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Savol turi</th><th>Realistik vaqt</th>"
              "<th>Nega</th></tr></thead>"
              "<tbody>"
              "<tr><td>Standard English Conventions</td><td>25-40 s</td>"
              "<td>qoida; talqin yo'q</td></tr>"
              "<tr><td>Transitions</td><td>50-70 s</td>"
              "<td>ikki gap orasidagi munosabatni aniqlash</td></tr>"
              "<tr><td>Rhetorical Synthesis</td><td>90-120 s</td>"
              "<td>maqsad + qaydlar + to'rt variant</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "<strong>Rhetorical Synthesis'da maqsad gapini "
                "birinchi o'qing, qaydlarni keyin.</strong> Qaydlar "
                "ataylab ko'p — maqsadni bilmasdan o'qish "
                "vaqtni ikki barobar oshiradi.")
            + '<span class="sr-time">⏱ 8 savol · 9 daqiqa</span>'
        )},

        {
            "rich_text": qnum(1, "Transition") + trans_q(
                "<p>A lock raises a boat by filling a chamber with water from the reach "
                "above it, and the water is not pumped: it simply falls. Every boat that "
                "goes up therefore empties a lock's worth of water down the canal. "
                "<span class=\"sr-blank\"></span> a summit level with heavy traffic needs "
                "a reservoir behind it, and several English canals were built with two.</p>"),
            "choices": [
                {"text": "As a result,", "is_correct": True},
                {"text": "Nevertheless,", "is_correct": False},
                {"text": "For example,", "is_correct": False},
                {"text": "In contrast,", "is_correct": False},
            ],
            "explanation": (
                "<p>Oldingi gap: har bir qayiq suvni pastga oqizadi. "
                "Keyingi gap: shuning uchun yuqori qismga suv "
                "ombori kerak.</p>"
                "<p>Bu <mark>sabab → oqibat</mark> munosabati.</p>"
                + why([
                    (True, "As a result,",
                     "oqibatni bildiradi — matnning aynan "
                     "harakati."),
                    (False, "Nevertheless,",
                     "qarshilik bildiradi; bu yerda hech qanday "
                     "kutilmagan burilish yo'q."),
                    (False, "For example,",
                     "misol emas: ikkinchi gap birinchisining "
                     "namunasi emas, natijasi."),
                    (False, "In contrast,",
                     "qarama-qarshilik bildiradi; ikki gap "
                     "bir yo'nalishda."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Transition") + trans_q(
                "<p>Ash trees grown in the open put on wide rings and make timber that "
                "splits easily, which suits a tool handle. Trees of the same age grown in "
                "a dense wood put on narrow rings and are far harder to split. "
                "<span class=\"sr-blank\"></span> a handle maker buying standing timber "
                "asks where it grew before he asks how old it is.</p>"),
            "choices": [
                {"text": "For this reason,", "is_correct": True},
                {"text": "By contrast,", "is_correct": False},
                {"text": "Similarly,", "is_correct": False},
                {"text": "Admittedly,", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikki gap faktni beradi (ochiq joyda o'sgan yog'och "
                "boshqacha), uchinchisi esa o'sha faktdan kelib "
                "chiqadigan <mark>amaliy xulosani</mark> "
                "aytadi.</p>"
                + why([
                    (True, "For this reason,",
                     "sababdan xulosaga o'tadi."),
                    (False, "By contrast,",
                     "qarama-qarshilik oldingi <u>ikki</u> gap "
                     "orasida edi, uchinchisi bilan emas."),
                    (False, "Similarly,",
                     "o'xshashlik bildiradi; uchinchi gap yangi "
                     "o'xshash misol emas, xulosa."),
                    (False, "Admittedly,",
                     "e'tirofni bildiradi — matn hech narsani tan "
                     "olmayapti."),
                ])
                + WARN.format(
                    "Qarama-qarshilik bildiruvchi so'zlar tuzoq bo'lib "
                    "turadi, chunki abzatsda <u>qayerdadir</u> "
                    "qarama-qarshilik bo'ladi. Savol esa faqat "
                    "<strong>bo'sh joyning ikki tomoni</strong> "
                    "haqida.")
            ),
        },

        {
            "rich_text": qnum(3, "Transition") + trans_q(
                "<p>A sundial tells solar time, which runs ahead of clock time for part "
                "of the year and behind it for the rest, by as much as a quarter of an "
                "hour either way. A well-made dial is therefore never wrong in the way a "
                "slow clock is wrong. <span class=\"sr-blank\"></span> it is answering a "
                "different question, and the table of corrections engraved on the better "
                "ones turns one answer into the other.</p>"),
            "choices": [
                {"text": "Rather,", "is_correct": True},
                {"text": "Likewise,", "is_correct": False},
                {"text": "Consequently,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p>Oldingi gap nimanidir <u>rad etadi</u> "
                "(«noto'g'ri emas»), keyingisi esa uning o'rniga "
                "to'g'ri tavsifni beradi («boshqa savolga javob "
                "beradi»).</p>"
                "<p>Bu <mark>«bu emas, balki bu»</mark> "
                "munosabati.</p>"
                + why([
                    (True, "Rather,",
                     "rad etilgan fikr o'rniga to'g'risini "
                     "qo'yadi — aynan shu harakat."),
                    (False, "Likewise,",
                     "o'xshashlik: ikkinchi gap birinchisining "
                     "takrori emas."),
                    (False, "Consequently,",
                     "oqibat: quyoshsoatning boshqa savolga javob "
                     "berishi oldingi gapdan <u>kelib chiqmaydi</u> "
                     "— aksincha, uning sababi."),
                    (False, "Meanwhile,",
                     "vaqt bildiradi; bu yerda ikki bir vaqtda "
                     "sodir bo'layotgan voqea yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Transition") + trans_q(
                "<p>Most of the county's hedges were planted between 1750 and 1850, when "
                "the open fields were divided, and a planted hedge usually holds one or "
                "two woody species. <span class=\"sr-blank\"></span> may hold ten or twelve, "
                "because it was there long before the "
                "fields were divided and had centuries to gather them.</p>"),
            "choices": [
                {"text": "A hedge on a parish boundary, however,", "is_correct": True},
                {"text": "A hedge on a parish boundary, for instance,", "is_correct": False},
                {"text": "A hedge on a parish boundary, therefore,", "is_correct": False},
                {"text": "A hedge on a parish boundary, in addition,", "is_correct": False},
            ],
            "explanation": (
                "<p>Oldingi gap: ekilgan jonli devorda 1-2 tur. "
                "Keyingisi: chegara devorida 10-12. Bu "
                "<mark>istisno</mark>.</p>"
                "<p>Diqqat: bu savolda bo'sh joy butun ega bilan "
                "birga keladi, shuning uchun to'rt variant bir xil "
                "so'zlar bilan boshlanadi — farq faqat "
                "bog'lovchida.</p>"
                + why([
                    (True, "A hedge on a parish boundary, however,",
                     "<em>however</em> qarama-qarshilikni "
                     "bildiradi: umumiy qoida, keyin istisno."),
                    (False, "A hedge on a parish boundary, for instance,",
                     "misol emas — chegara devori qoidaning "
                     "namunasi emas, uning aksi."),
                    (False, "A hedge on a parish boundary, therefore,",
                     "oqibat emas: 10-12 tur oldingi gapdan kelib "
                     "chiqmaydi."),
                    (False, "A hedge on a parish boundary, in addition,",
                     "qo'shimcha emas: ikkinchi gap birinchisiga "
                     "yana bir fakt qo'shmayapti, uni "
                     "cheklamoqda."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Rhetorical Synthesis") + notes_q(
                "Talaba quyidagi qaydlarni to'plagan:",
                ["A lime kiln burns limestone to make quicklime.",
                 "Quicklime was spread on acid fields to raise the pH.",
                 "Kilns were built into a bank so carts could tip stone in at the top.",
                 "Fuel and stone were loaded in alternate layers.",
                 "A kiln at Bratton was worked from 1802 to 1911.",
                 "The Bratton kiln burned about one ton of coal for every four tons of stone."],
                "Talaba pechning qurilishini qanday ishlaganini "
                "tushuntirmoqchi. Qaysi variant bu maqsadga eng mos "
                "keladi?"),
            "choices": [
                {"text": "Built into a bank so that carts could tip stone in at the top, a "
                         "lime kiln was filled with alternate layers of fuel and stone.",
                 "is_correct": True},
                {"text": "The kiln at Bratton, which was worked from 1802 to 1911, burned "
                         "about one ton of coal for every four tons of stone.",
                 "is_correct": False},
                {"text": "Quicklime, which a lime kiln makes by burning limestone, was "
                         "spread on acid fields to raise the pH.",
                 "is_correct": False},
                {"text": "Lime kilns were worked for more than a century, and the one at "
                         "Bratton was built into a bank.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> pechning "
                "<u>qurilishi</u> qanday ishlaganini tushuntirish. "
                "Demak javob <mark>shakl</mark> va "
                "<mark>yuklash tartibi</mark> haqida bo'lishi "
                "kerak.</p>"
                + why([
                    (True, "Built into a bank so that carts could tip",
                     "ikkala tegishli qaydni birlashtiradi: qiyalikka "
                     "qurilgani (nega) va qatlab yuklangani "
                     "(qanday)."),
                    (False, "The kiln at Bratton, which was worked",
                     "raqamlar to'g'ri, lekin ular "
                     "<u>samaradorlik</u> haqida, qurilish "
                     "haqida emas."),
                    (False, "Quicklime, which a lime kiln makes",
                     "mahsulotning qo'llanilishi haqida — pech "
                     "qanday ishlagani emas."),
                    (False, "Lime kilns were worked for more than a century",
                     "ikki qaydni qo'shadi, lekin ikkovi ham "
                     "maqsadga tegishli emas: davomiylik + bitta "
                     "pechning joylashuvi."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Rhetorical Synthesis") + notes_q(
                "Talaba quyidagi qaydlarni to'plagan:",
                ["Two surveys of the same moor were made, in 1946 and 2021.",
                 "The 1946 survey counted 41 breeding pairs of curlew.",
                 "The 2021 survey counted 9 breeding pairs.",
                 "The moor was drained for forestry between 1968 and 1974.",
                 "Curlew nest on open ground and avoid ground within 300 metres of trees.",
                 "About a third of the moor is now under conifers."],
                "Talaba ikki tadqiqot natijasini taqqoslamoqchi. "
                "Qaysi variant bu maqsadga eng mos keladi?"),
            "choices": [
                {"text": "The moor held 41 breeding pairs of curlew in 1946 but only 9 in "
                         "2021.",
                 "is_correct": True},
                {"text": "Curlew nest on open ground and avoid ground within 300 metres of "
                         "trees.",
                 "is_correct": False},
                {"text": "The moor was drained for forestry between 1968 and 1974, and "
                         "about a third of it is now under conifers.",
                 "is_correct": False},
                {"text": "Two surveys of the same moor were made, one in 1946 and one in "
                         "2021.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> ikki tadqiqot "
                "<u>natijasini</u> taqqoslash. Demak javobda "
                "<mark>ikkala raqam</mark> ham bo'lishi va ular "
                "qarshilantirilishi shart.</p>"
                + why([
                    (True, "The moor held 41 breeding pairs",
                     "ikkala son, ikkala sana va <em>but</em> — "
                     "taqqoslashning o'zi."),
                    (False, "Curlew nest on open ground",
                     "sababni tushuntiradi, natijani "
                     "taqqoslamaydi."),
                    (False, "The moor was drained for forestry",
                     "yana sabab: o'rmonlashtirish. Tadqiqot "
                     "natijalari umuman aytilmaydi."),
                    (False, "Two surveys of the same moor were made",
                     "tadqiqotlar borligini aytadi, lekin ularning "
                     "natijasini emas — taqqoslash uchun hech "
                     "narsa qolmaydi."),
                ])
                + TIP.format(
                    "Synthesis savolida <strong>maqsad gapidagi "
                    "fe'lni</strong> ajratib oling: "
                    "<em>compare · emphasise · explain · introduce · "
                    "describe</em>. Har biri boshqa qaydlarni "
                    "talab qiladi, va noto'g'ri variantlar odatda "
                    "<u>to'g'ri faktlar, noto'g'ri ish</u> "
                    "bo'ladi.")
            ),
        },

        {
            "rich_text": qnum(7, "Rhetorical Synthesis") + notes_q(
                "Talaba quyidagi qaydlarni to'plagan:",
                ["A pantile is an S-shaped clay roof tile.",
                 "Pantiles came to eastern England from the Low Countries in the 1600s.",
                 "They arrived as ballast in ships returning empty from the grain trade.",
                 "A pantile roof needs about 180 tiles per 100 square feet.",
                 "A plain tile roof of the same area needs about 700.",
                 "Fewer tiles means a lighter roof and a lighter frame beneath it."],
                "Talaba pantile tomining nima uchun arzonroq "
                "bo'lganini tushuntirmoqchi. Qaysi variant bu "
                "maqsadga eng mos keladi?"),
            "choices": [
                {"text": "A pantile roof needs about 180 tiles per 100 square feet where a "
                         "plain tile roof needs about 700, so the frame beneath it can be "
                         "lighter.",
                 "is_correct": True},
                {"text": "Pantiles reached eastern England from the Low Countries in the "
                         "1600s, carried as ballast in ships returning empty from the grain "
                         "trade.",
                 "is_correct": False},
                {"text": "A pantile is an S-shaped clay tile, and a pantile roof needs about "
                         "180 tiles per 100 square feet.",
                 "is_correct": False},
                {"text": "Because they arrived as ballast, pantiles were cheap in the ports "
                         "of eastern England.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> nega pantile tomi "
                "<u>arzonroq</u> bo'lgan. Qaydlarda buning ikki "
                "bo'g'ini bor: <mark>kamroq cherepitsa</mark> va "
                "<mark>yengilroq karkas</mark>.</p>"
                + why([
                    (True, "A pantile roof needs about 180 tiles",
                     "ikkala raqamni qarshilantiradi va xarajat "
                     "zanjirini oxirigacha olib boradi: kamroq "
                     "cherepitsa → yengilroq karkas."),
                    (False, "Pantiles reached eastern England",
                     "tarixni aytadi, narxni emas."),
                    (False, "A pantile is an S-shaped clay tile",
                     "ta'rif + bitta raqam. Taqqoslash yo'q, "
                     "shuning uchun 180 ko'pmi yoki ozmi — "
                     "noma'lum."),
                    (False, "Because they arrived as ballast",
                     "bu ham arzonlik sababi, lekin qaydlarda "
                     "ballast narxi haqida hech narsa yo'q — "
                     "variant qaydlardan chiqmaydigan xulosa "
                     "yasaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(8, "Transition") + trans_q(
                "<p>Salt was cut from the rock in some places and boiled out of brine in "
                "others, and the two methods left completely different landscapes behind "
                "them. <span class=\"sr-blank\"></span> the brine districts subsided as "
                "the underground cavities collapsed, and whole streets in Cheshire were "
                "jacked up or rebuilt in the nineteenth century.</p>"),
            "choices": [
                {"text": "In particular,", "is_correct": True},
                {"text": "Otherwise,", "is_correct": False},
                {"text": "Instead,", "is_correct": False},
                {"text": "Even so,", "is_correct": False},
            ],
            "explanation": (
                "<p>Oldingi gap umumiy da'vo qiladi: ikki usul "
                "boshqa-boshqa manzara qoldirgan. Keyingisi "
                "<mark>ikkitasidan bittasini</mark> olib, uni "
                "batafsil ochadi.</p>"
                "<p>Bu — umumiydan xususiyga o'tish.</p>"
                + why([
                    (True, "In particular,",
                     "umumiy da'voni bitta aniq holat bilan "
                     "ochadi."),
                    (False, "Otherwise,",
                     "«aks holda» degani — bu yerda hech qanday "
                     "shart yo'q."),
                    (False, "Instead,",
                     "almashtirishni bildiradi: ikkinchi gap "
                     "birinchisining o'rniga kelmaydi, uni "
                     "davom ettiradi."),
                    (False, "Even so,",
                     "qarshilik bildiradi; ikki gap bir "
                     "yo'nalishda."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>O'zingizni tekshiring</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Savol</th><th>Munosabat / maqsad</th>"
              "<th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td>1</td><td>sabab → oqibat</td><td>11</td></tr>"
              "<tr><td>2</td><td>faktdan xulosaga</td><td>11</td></tr>"
              "<tr><td>3</td><td>«bu emas, balki bu»</td><td>13</td></tr>"
              "<tr><td>4</td><td>umumiy qoida → istisno</td><td>12</td></tr>"
              "<tr><td>5</td><td>Synthesis: tushuntirish</td><td>21</td></tr>"
              "<tr><td>6</td><td>Synthesis: taqqoslash</td><td>22</td></tr>"
              "<tr><td>7</td><td>Synthesis: sababni ko'rsatish</td><td>23</td></tr>"
              "<tr><td>8</td><td>umumiydan xususiyga</td><td>12</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Bog'lovchi so'z <strong>faqat bo'sh joyning ikki "
              "tomonini</strong> bog'laydi — butun abzatsni "
              "emas.</li>"
              "<li>Synthesis'da <strong>maqsad gapidagi fe'l</strong> "
              "qaysi qaydlar kerakligini aytadi.</li>"
              "<li>Noto'g'ri Synthesis variantlari deyarli har doim "
              "<u>to'g'ri faktlar</u> bilan <u>noto'g'ri "
              "ish</u> qiladi.</li>"
              "<li>Vaqtni Conventions'dan tejang va shu yerga "
              "sarflang.</li>"
              "</ul>"
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 92
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_MIX,
    "title": "SAT R&W W92: Mixed Practice 3 — A Full Writing Half-Module (14 Questions)",
    "summary": "O'n to'rt savol, imtihonning o'z tartibida: avval Standard "
               "English Conventions, keyin Expression of Ideas. 17 daqiqa.",
    "order": 92,
    "blocks": [
        {"rich_text": (
            "<h2>Bu — yarim modul</h2>"
            "<p>Haqiqiy modulda 27 savol bor va ular ikki yarmga "
            "bo'linadi: o'qish (Craft and Structure, Information "
            "and Ideas) va yozuv (Standard English Conventions, "
            "Expression of Ideas). Yozuv yarmi taxminan "
            "<strong>modulning yarmini</strong> egallaydi. Bu dars "
            "— o'sha yarim, imtihonning o'z tartibida.</p>"
            + EXAMP.format(
                "<p style=\"margin:0;\"><strong>Modul tartibi "
                "doimiy:</strong> Craft and Structure → Information "
                "and Ideas → <u>Standard English Conventions</u> → "
                "<u>Expression of Ideas</u>. Ya'ni grammatika "
                "savollari <strong>oxirgi yarmida</strong> "
                "keladi.</p>")
            + "<p>Shuning uchun boshda sekin ketgan odam bu yerga "
            "yetib kelganda vaqti qolmaydi — va aynan shu savollar "
            "eng tez olinadigan ballardir.</p>"
            + WARN.format(
                "Tartib doimiy, lekin <u>kafolat emas</u>: College "
                "Board tartibni rasman e'lon qilmagan va Bluebook "
                "amalda shu ketma-ketlikni ko'rsatadi. Rejangizni "
                "shunga qurishingiz mumkin, lekin unga "
                "bog'lanib qolmang.")
            + '<span class="sr-time">⏱ 14 savol · 17 daqiqa · to\'xtamang</span>'
        )},

        {
            "rich_text": qnum(1, "Conventions") + conv_q(
                "<p>A watermark is made by a wire design sewn onto the mould, which "
                "presses the pulp thinner where it lies. Held up to the light, "
                "<span class=\"sr-blank\"></span>, and a mill's whole output can often be "
                "dated from it to within five years.</p>"),
            "choices": [
                {"text": "the sheet shows the design as a pale line", "is_correct": True},
                {"text": "the design shows as a pale line in the sheet", "is_correct": False},
                {"text": "there is a pale line where the design lay", "is_correct": False},
                {"text": "a pale line is visible in the sheet", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>NIMA yorug'likka tutiladi?</strong> "
                "<mark>Varaq.</mark> Naqsh ham, chiziq ham "
                "emas.</p>"
                + why([
                    (True, "the sheet shows the design",
                     "verguldan keyingi birinchi ot — "
                     "<em>the sheet</em>."),
                    (False, "the design shows as a pale line",
                     "naqsh yorug'likka tutilmaydi; u qolipda."),
                    (False, "there is a pale line",
                     "<em>there</em> hech narsani bildirmaydi."),
                    (False, "a pale line is visible",
                     "chiziq yorug'likka tutilmaydi — u "
                     "natijasi."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "Conventions") + conv_q(
                "<p>The set of hand tools that the last wheelwright in the village left to "
                "the museum <span class=\"sr-blank\"></span> two hundred and six pieces, "
                "and forty of them have no modern name.</p>"),
            "choices": [
                {"text": "numbers", "is_correct": True},
                {"text": "number", "is_correct": False},
                {"text": "numbering", "is_correct": False},
                {"text": "have numbered", "is_correct": False},
            ],
            "explanation": (
                "<p>Ega — <em>The set</em>, birlik. "
                "<em>of hand tools</em> va <em>that the last "
                "wheelwright … left</em> — ikkovi ham "
                "oraliq.</p>"
                + why([
                    (True, "numbers", "birlik shaxsli kesim."),
                    (False, "number",
                     "ko'plik — <em>tools</em> ga moslashgan."),
                    (False, "numbering",
                     "sifatdosh; gapda asosiy kesim "
                     "qolmaydi."),
                    (False, "have numbered",
                     "ko'plik va perfect uchun asos yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "Conventions") + conv_q(
                "<p>Cold water holds more dissolved oxygen than warm water "
                "<span class=\"sr-blank\"></span> a trout stream that warms by three "
                "degrees in a dry summer can lose a fifth of its oxygen without losing a "
                "drop of its flow.</p>"),
            "choices": [
                {"text": "does, and", "is_correct": True},
                {"text": "does and", "is_correct": False},
                {"text": "does,", "is_correct": False},
                {"text": "does", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikki tomon ham mustaqil gap: <em>Cold water "
                "holds…</em> va <em>a trout stream … can "
                "lose…</em>.</p>"
                "<p>Ikki mustaqil gapni bog'lovchi bilan ulasangiz, "
                "bog'lovchidan <u>oldin vergul</u> "
                "kerak.</p>"
                + why([
                    (True, "does, and",
                     "vergul + bog'lovchi — to'liq va to'g'ri "
                     "ulanish."),
                    (False, "does and",
                     "vergulsiz: ikki uzun mustaqil gap "
                     "yopishib qoladi."),
                    (False, "does,",
                     "vergul splaysi — bog'lovchi yo'q."),
                    (False, "does",
                     "belgisiz qo'shilish."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "Conventions") + conv_q(
                "<p>The bell was cast in 1623 by a founder whose work survives in eleven "
                "parishes, and <span class=\"sr-blank\"></span> initials appear on the "
                "waist under a band of lettering that nobody has yet read in full.</p>"),
            "choices": [
                {"text": "his", "is_correct": True},
                {"text": "their", "is_correct": False},
                {"text": "its", "is_correct": False},
                {"text": "they're", "is_correct": False},
            ],
            "explanation": (
                "<p>Antecedent — <em>a founder</em>, bitta odam, va "
                "matn uni <em>whose</em> bilan izohlaydi. Bo'sh "
                "joydan keyin ot (<em>initials</em>) — "
                "egalik.</p>"
                + why([
                    (True, "his",
                     "birlik egalik olmoshi, odam uchun."),
                    (False, "their",
                     "ko'plik: <em>parishes</em> ga "
                     "moslashgan."),
                    (False, "its",
                     "birlik, lekin narsalar uchun — bosh "
                     "harflar quyuvchiniki, "
                     "qo'ng'iroqniki emas."),
                    (False, "they're",
                     "<em>they are initials appear</em> — yoyish "
                     "sinovi darrov rad qiladi."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "Conventions") + conv_q(
                "<p>By the time the surveyors reached the last of the four valleys in "
                "October, the river <span class=\"sr-blank\"></span> its course twice "
                "since their first visit, and two of the boundary stones they had set were "
                "under water.</p>"),
            "choices": [
                {"text": "had changed", "is_correct": True},
                {"text": "changed", "is_correct": False},
                {"text": "has changed", "is_correct": False},
                {"text": "changes", "is_correct": False},
            ],
            "explanation": (
                "<p><em>By the time …</em> — past perfect'ning eng "
                "aniq belgisi. O'zgarish o'tgan zamondagi "
                "nuqtadan (oktabr) <mark>oldin</mark> sodir "
                "bo'lgan.</p>"
                "<p>Tasdiq: <em>they <u>had set</u></em> ham past "
                "perfect.</p>"
                + why([
                    (True, "had changed", "past perfect."),
                    (False, "changed",
                     "oddiy o'tgan zamon — tartibni "
                     "ko'rsatmaydi."),
                    (False, "has changed",
                     "present perfect bugungacha yetadi; "
                     "voqea tugagan o'tmishda."),
                    (False, "changes",
                     "hozirgi zamon."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "Conventions") + conv_q(
                "<p>The bindery kept three kinds of thread, four weights of board and two "
                "colours of headband, and every job book entry names "
                "<span class=\"sr-blank\"></span> was used. The entries are what allow a "
                "binding to be matched to a shop two centuries later.</p>"),
            "choices": [
                {"text": "which of them", "is_correct": True},
                {"text": "which of they", "is_correct": False},
                {"text": "who of them", "is_correct": False},
                {"text": "whom of them", "is_correct": False},
            ],
            "explanation": (
                "<p>Narsalar haqida gap ketyapti → "
                "<em>which</em>, <em>who/whom</em> "
                "emas. Va <em>of</em> predlogidan keyin "
                "to'ldiruvchi shakl kerak → "
                "<mark><em>them</em></mark>.</p>"
                + why([
                    (True, "which of them",
                     "narsa + predlogdan keyin to'ldiruvchi "
                     "shakl."),
                    (False, "which of they",
                     "<em>they</em> — ega shakli; predlogdan "
                     "keyin turolmaydi."),
                    (False, "who of them",
                     "<em>who</em> odamlar uchun."),
                    (False, "whom of them",
                     "yana odamlar uchun."),
                ])
            ),
        },

        {
            "rich_text": qnum(7, "Conventions") + conv_q(
                "<p>A drystone wall is built in two skins with small stones packed between "
                "them, tied every yard by a long through stone and "
                "<span class=\"sr-blank\"></span> with a row of flat slabs set on edge "
                "along the top. Nothing in it is mortared, and a good wall stands for a "
                "hundred and fifty years.</p>"),
            "choices": [
                {"text": "finished", "is_correct": True},
                {"text": "finishing", "is_correct": False},
                {"text": "it is finished", "is_correct": False},
                {"text": "to finish", "is_correct": False},
            ],
            "explanation": (
                "<p>Ro'yxatning oldingi bo'lagi — <em><u>tied</u> "
                "every yard</em>, ya'ni <em>-ed</em> sifatdosh. "
                "Uchinchisi ham shunday bo'lishi "
                "kerak.</p>"
                "<p>Ikkovi ham <em>A drystone wall is built …</em> "
                "ga bog'lanadi.</p>"
                + why([
                    (True, "finished",
                     "<em>tied</em> bilan bir shaklda va bir "
                     "otga tegishli."),
                    (False, "finishing",
                     "faol shakl: devor o'zini "
                     "tugatmaydi."),
                    (False, "it is finished",
                     "to'liq gap — ro'yxatning a'zosi "
                     "bo'lolmaydi."),
                    (False, "to finish",
                     "infinitiv — shakl mos kelmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(8, "Conventions") + conv_q(
                "<p>The <span class=\"sr-blank\"></span> hall stands at the end of a lane "
                "that leads nowhere else, which is why so little of it was ever pulled "
                "down. Six of the seven medieval guild halls in the city went between 1840 "
                "and 1890.</p>"),
            "choices": [
                {"text": "weavers'", "is_correct": True},
                {"text": "weaver's", "is_correct": False},
                {"text": "weavers", "is_correct": False},
                {"text": "weavers's", "is_correct": False},
            ],
            "explanation": (
                "<p>Bo'sh joydan keyin ot (<em>hall</em>) — egalik. "
                "Gildiya zali — bir <u>guruh</u> "
                "hunarmandniki, ya'ni "
                "<mark>ko'plik</mark>.</p>"
                + why([
                    (True, "weavers'",
                     "ko'p egali egalik: to'quvchilar "
                     "gildiyasining zali."),
                    (False, "weaver's",
                     "bitta to'quvchiniki — gildiya zali "
                     "bunday bo'lmaydi."),
                    (False, "weavers",
                     "egalikni bildirmaydi."),
                    (False, "weavers's",
                     "bunday shakl yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(9, "Expression of Ideas") + trans_q(
                "<p>A cathedral clock of the fourteenth century had no face and no hands: "
                "it existed to strike a bell, and the bell told the town when to pray. "
                "<span class=\"sr-blank\"></span> the earliest surviving dials were added "
                "to mechanisms that had already been running for fifty or sixty years.</p>"),
            "choices": [
                {"text": "In fact,", "is_correct": True},
                {"text": "Otherwise,", "is_correct": False},
                {"text": "In contrast,", "is_correct": False},
                {"text": "Meanwhile,", "is_correct": False},
            ],
            "explanation": (
                "<p>Ikkinchi gap birinchisini <mark>kuchaytiradi</mark>: "
                "sifat yo'q edi degan da'voni tasdiqlovchi dalil "
                "bilan qo'llab-quvvatlaydi.</p>"
                + why([
                    (True, "In fact,",
                     "da'voni kuchaytiruvchi dalilni "
                     "kiritadi."),
                    (False, "Otherwise,",
                     "«aks holda» — bu yerda shart yo'q."),
                    (False, "In contrast,",
                     "ikkinchi gap birinchisiga qarshi "
                     "chiqmaydi, uni tasdiqlaydi."),
                    (False, "Meanwhile,",
                     "bir vaqtda kechayotgan ikki voqea yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(10, "Expression of Ideas") + trans_q(
                "<p>Peat cores from the bog hold pollen in the order it fell, so a "
                "centimetre of peat is a decade of vegetation. The elm pollen in cores "
                "from all over north-west Europe drops away sharply at about the same "
                "depth. <span class=\"sr-blank\"></span> nobody has yet shown whether the "
                "cause was disease, climate or clearance by farmers.</p>"),
            "choices": [
                {"text": "However,", "is_correct": True},
                {"text": "Therefore,", "is_correct": False},
                {"text": "Likewise,", "is_correct": False},
                {"text": "For instance,", "is_correct": False},
            ],
            "explanation": (
                "<p>Oldingi gap kuchli, aniq natijani beradi; "
                "keyingisi esa <mark>bu natija sababini "
                "tushuntirmasligini</mark> aytadi. Bu — "
                "cheklov.</p>"
                + why([
                    (True, "However,",
                     "aniq dalil, keyin uning cheki: "
                     "qarama-qarshilik."),
                    (False, "Therefore,",
                     "sabab bilmaslik dalildan kelib "
                     "chiqmaydi."),
                    (False, "Likewise,",
                     "o'xshashlik yo'q."),
                    (False, "For instance,",
                     "ikkinchi gap misol emas."),
                ])
            ),
        },

        {
            "rich_text": qnum(11, "Expression of Ideas") + notes_q(
                "Talaba quyidagi qaydlarni to'plagan:",
                ["A tide mill is driven by water trapped behind a gate at high tide.",
                 "It can be worked for about five hours of every twelve.",
                 "Its working hours therefore move forward by about fifty minutes a day.",
                 "The miller's family worked whatever hours the tide gave them.",
                 "A river mill of the same period worked daylight hours.",
                 "One Essex tide mill was still grinding commercially in 1940."],
                "Talaba tegirmonda ishlash tartibini daryo tegirmoni "
                "bilan taqqoslamoqchi. Qaysi variant bu maqsadga eng "
                "mos keladi?"),
            "choices": [
                {"text": "A river mill worked daylight hours, but a tide mill worked "
                         "whatever hours the tide gave it, moving forward by about fifty "
                         "minutes a day.",
                 "is_correct": True},
                {"text": "A tide mill is driven by water trapped behind a gate at high "
                         "tide and can be worked for about five hours of every twelve.",
                 "is_correct": False},
                {"text": "One Essex tide mill was still grinding commercially in 1940, long "
                         "after most river mills had stopped.",
                 "is_correct": False},
                {"text": "The working hours of a tide mill move forward by about fifty "
                         "minutes a day.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> ish tartibini daryo "
                "tegirmoni bilan <u>taqqoslash</u>. Javobda "
                "<mark>ikkala tegirmon</mark> ham bo'lishi "
                "shart.</p>"
                + why([
                    (True, "A river mill worked daylight hours",
                     "ikkala tegirmon, ikkala tartib va "
                     "<em>but</em> — taqqoslashning o'zi."),
                    (False, "A tide mill is driven by water",
                     "faqat bitta tegirmon: mexanizmni "
                     "tushuntiradi, taqqoslamaydi."),
                    (False, "One Essex tide mill was still grinding",
                     "taqqoslash bor, lekin <u>ish tartibi</u> "
                     "emas, <u>umri</u> haqida."),
                    (False, "The working hours of a tide mill",
                     "yana faqat bitta tegirmon."),
                ])
            ),
        },

        {
            "rich_text": qnum(12, "Expression of Ideas") + notes_q(
                "Talaba quyidagi qaydlarni to'plagan:",
                ["A bee's waggle dance encodes the direction and distance of a food source.",
                 "The angle of the waggle run from vertical equals the angle from the sun.",
                 "The duration of the run encodes distance: about 75 milliseconds per 100 m.",
                 "The dance was decoded by Karl von Frisch, who published on it from 1946.",
                 "Bees dance on a vertical comb in the dark.",
                 "Followers read the dance by touch and by the sound of the wingbeat."],
                "Talaba raqs masofani qanday ifodalashini "
                "tushuntirmoqchi. Qaysi variant bu maqsadga eng mos "
                "keladi?"),
            "choices": [
                {"text": "The length of the waggle run encodes distance, at roughly 75 "
                         "milliseconds for every 100 metres.",
                 "is_correct": True},
                {"text": "The angle of the waggle run from vertical is equal to the angle "
                         "of the food source from the sun.",
                 "is_correct": False},
                {"text": "Bees dance on a vertical comb in the dark, and followers read the "
                         "dance by touch.",
                 "is_correct": False},
                {"text": "The waggle dance, decoded by Karl von Frisch from 1946, encodes "
                         "both direction and distance.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>Maqsad:</strong> <u>masofa</u> qanday "
                "ifodalanadi. Qaydlar ichida bunga tegishlisi "
                "bitta: <mark>davomiylik</mark>.</p>"
                + why([
                    (True, "The length of the waggle run encodes distance",
                     "aynan masofa mexanizmini beradi, raqam "
                     "bilan."),
                    (False, "The angle of the waggle run",
                     "bu <u>yo'nalish</u> mexanizmi — to'g'ri "
                     "fakt, noto'g'ri savol."),
                    (False, "Bees dance on a vertical comb",
                     "raqs qanday o'qilishi haqida, nima "
                     "kodlanishi haqida emas."),
                    (False, "The waggle dance, decoded by Karl von Frisch",
                     "masofa kodlanishini <u>aytadi</u>, lekin "
                     "qanday ekanini tushuntirmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(13, "Expression of Ideas") + precise_q(
                "<p>The society printed its transactions on rag paper until 1878 and on "
                "wood-pulp paper afterwards, because the newer paper cost a third as much. "
                "<span class=\"sr-blank\"></span> is now brown and brittle at the edges, "
                "while the volumes printed before that date can still be opened flat "
                "without damage.</p>"),
            "choices": [
                {"text": "The wood-pulp paper", "is_correct": True},
                {"text": "The rag paper", "is_correct": False},
                {"text": "The society", "is_correct": False},
                {"text": "It", "is_correct": False},
            ],
            "explanation": (
                "<p>Gapning ikkinchi yarmi 1878-dan <u>oldingi</u> "
                "jildlarni sog'lom deb aytadi. Demak buzilgani — "
                "<mark>keyingi qog'oz</mark>.</p>"
                + why([
                    (True, "The wood-pulp paper",
                     "1878-dan keyingi qog'oz — aynan sarg'aygan "
                     "va mo'rt bo'lgani."),
                    (False, "The rag paper",
                     "matn buni aksincha aytadi: eski jildlar "
                     "hali ham ochiladi."),
                    (False, "The society",
                     "jamiyat mo'rt bo'lmaydi."),
                    (False, "It",
                     "ikkita qog'oz ham, jamiyat ham birlik — "
                     "olmosh hech narsani ajratmaydi."),
                ])
            ),
        },

        {
            "rich_text": qnum(14, "Expression of Ideas") + trans_q(
                "<p>Sound carries further over water at night because the air just above "
                "the surface cools faster than the air higher up, and sound bends towards "
                "the cooler, slower layer. <span class=\"sr-blank\"></span> a conversation "
                "on one bank of a wide estuary can be followed word for word on the other, "
                "which is why smugglers worked in silence.</p>"),
            "choices": [
                {"text": "Consequently,", "is_correct": True},
                {"text": "Nonetheless,", "is_correct": False},
                {"text": "By comparison,", "is_correct": False},
                {"text": "Admittedly,", "is_correct": False},
            ],
            "explanation": (
                "<p>Birinchi gap fizik sababni beradi, ikkinchisi "
                "uning <mark>amaliy oqibatini</mark>.</p>"
                + why([
                    (True, "Consequently,", "sabab → oqibat."),
                    (False, "Nonetheless,",
                     "qarshilik: ikki gap bir yo'nalishda."),
                    (False, "By comparison,",
                     "taqqoslash uchun ikkinchi holat kerak — "
                     "bu yerda yo'q."),
                    (False, "Admittedly,",
                     "e'tirof: matn hech narsani tan "
                     "olmayapti."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Natijangizni o'qish</h3>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>To'g'ri</th><th>Nima demak</th>"
              "<th>Keyingi qadam</th></tr></thead>"
              "<tbody>"
              "<tr><td>13-14</td><td>yozuv yarmi tayyor</td>"
              "<td>vaqtga ishlang: 17 daqiqadan 15 ga tushiring</td></tr>"
              "<tr><td>10-12</td><td>qoidalar bor, tezlik "
              "yetishmaydi</td>"
              "<td>xatolarni turi bo'yicha guruhlang</td></tr>"
              "<tr><td>7-9</td><td>bitta-ikkita mavzu "
              "oqsayapti</td>"
              "<td>o'sha ikki darsni qayta o'qing, keyin "
              "90-91 ga qayting</td></tr>"
              "<tr><td>&lt;7</td><td>hali mustahkamlanmagan</td>"
              "<td>30-74 darslarini tartib bilan qayta "
              "o'ting</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Savol</th><th>Tur</th><th>Dars</th></tr></thead>"
              "<tbody>"
              "<tr><td>1</td><td>osilib qolgan bo'lak</td><td>72</td></tr>"
              "<tr><td>2</td><td>moslashuv</td><td>50-51</td></tr>"
              "<tr><td>3</td><td>vergul + bog'lovchi</td><td>31</td></tr>"
              "<tr><td>4</td><td>olmosh moslashuvi</td><td>60</td></tr>"
              "<tr><td>5</td><td>past perfect</td><td>53</td></tr>"
              "<tr><td>6</td><td>nisbiy olmosh + kelishik</td><td>63</td></tr>"
              "<tr><td>7</td><td>parallellik</td><td>73</td></tr>"
              "<tr><td>8</td><td>apostrof</td><td>70</td></tr>"
              "<tr><td>9</td><td>kuchaytirish</td><td>13</td></tr>"
              "<tr><td>10</td><td>cheklov</td><td>12</td></tr>"
              "<tr><td>11</td><td>Synthesis: taqqoslash</td><td>22</td></tr>"
              "<tr><td>12</td><td>Synthesis: mexanizm</td><td>21</td></tr>"
              "<tr><td>13</td><td>aniq ot, noaniq olmosh emas</td><td>62</td></tr>"
              "<tr><td>14</td><td>sabab → oqibat</td><td>11</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Yarim modulni <strong>to'xtamasdan</strong> "
                "yechish — bu darsning asosiy mashqi. Bitta savolda "
                "qotib qolsangiz, belgilang va o'ting: 14-savol "
                "1-savol bilan bir xil ball beradi, va u sizni "
                "kutmaydi.")
        )},
    ],
},

# ═══════════════════════════════════════════════════════════════════════════
# Writing 93
# ═══════════════════════════════════════════════════════════════════════════
{
    "skill": "writing",
    "topic": TOPIC_MIX,
    "title": "SAT R&W W93: The Last Five Minutes — Banking the Grammar Marks",
    "summary": "Besh daqiqa qoldi va oltita savol bor. Qaysi biriga tegasiz, "
               "qaysi birini tashlab ketasiz, va nega bo'sh qoldirmaysiz.",
    "order": 93,
    "blocks": [
        {"rich_text": (
            "<h2>Uchta fakt, keyin taktika</h2>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<tbody>"
              "<tr><td><strong>1</strong></td>"
              "<td>Har bir savol <u>bir xil</u> ball beradi. Eng "
              "og'iri ham, eng yengili ham.</td></tr>"
              "<tr><td><strong>2</strong></td>"
              "<td>Noto'g'ri javob uchun <u>jarima yo'q</u>. Bo'sh "
              "qoldirilgan savol nol beradi, taxmin qilingani "
              "esa 25%.</td></tr>"
              "<tr><td><strong>3</strong></td>"
              "<td>Savollar tur bo'yicha guruhlangan, shuning "
              "uchun oxirida qolganlar odatda "
              "<u>Expression of Ideas</u> — eng sekinlari.</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + EXAMP.format(
                "<p style=\"margin:0;font-size:1.06em;\"><strong>Taktika: "
                "besh daqiqa qolganda oxirgi savoldan emas, "
                "<u>eng arzon</u> savoldan boshlang.</strong></p>")
            + '<span class="sr-time">⏱ 6 savol · 3 daqiqa</span>'
        )},

        {"rich_text": (
            "<h3>Uch soniyalik saralash</h3>"
            "<p>Savol matnini emas — <strong>variantlar "
            "ro'yxatini</strong> ko'ring. U savolning narxini "
            "darrov aytadi.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Variantlar</th><th>Narxi</th>"
              "<th>Qaror</th></tr></thead>"
              "<tbody>"
              "<tr><td>bitta so'z, faqat tinish belgisi bilan farq "
              "qiladi</td><td>~20 s</td>"
              "<td><strong>darrov oling</strong></td></tr>"
              "<tr><td><em>its / it's / their</em>, "
              "<em>-s / -'s / -s'</em></td><td>~20 s</td>"
              "<td><strong>darrov oling</strong></td></tr>"
              "<tr><td><em>is / are / was / were</em></td>"
              "<td>~30 s</td><td><strong>oling</strong></td></tr>"
              "<tr><td>bitta bog'lovchi so'z "
              "(<em>However / Therefore</em>)</td><td>~60 s</td>"
              "<td>vaqt qolsa</td></tr>"
              "<tr><td>to'rtta uzun gap + qaydlar kartasi</td>"
              "<td>~120 s</td><td><strong>taxmin qiling va "
              "o'ting</strong></td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + WARN.format(
                "<strong>Hech qachon bo'sh qoldirmang.</strong> "
                "Vaqt tugashiga o'n soniya qolganda qolgan hamma "
                "savolga bir xil harfni belgilang. Bu strategiya "
                "emas, bu arifmetika: nol ball 25% dan "
                "yomonroq.")
            + TIP.format(
                "Bluebook'da har bir savolni <strong>belgilab "
                "qo'yish</strong> (flag) va oxirida ular "
                "ro'yxatiga qaytish mumkin. Belgilangan savolga "
                "qaytish — ikkinchi marta noldan o'qishdan "
                "tezroq.")
        )},

        {
            "rich_text": qnum(1, "~20 soniya") + conv_q(
                "<p>The tower leans a little more each decade, and the crack that runs up "
                "the south face has been measured every spring since 1954. "
                "<span class=\"sr-blank\"></span> width has increased by rather less than "
                "the thickness of a coin in all that time.</p>"),
            "choices": [
                {"text": "Its", "is_correct": True},
                {"text": "It's", "is_correct": False},
                {"text": "Their", "is_correct": False},
                {"text": "They're", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>3 soniyalik tell:</strong> "
                "<em>its / it's / their / they're</em> — bu "
                "61-dars, apostrof savoli. Yoyib "
                "ko'ring.</p>"
                "<p><em>It is width has increased</em> — ma'nosiz. "
                "Bo'sh joydan keyin ot bor "
                "(<em>width</em>) → egalik. Antecedent — "
                "<em>the crack</em>, birlik.</p>"
                + why([
                    (True, "Its", "birlik egalik, apostrofsiz."),
                    (False, "It's",
                     "<em>it is / it has</em> — qisqartma."),
                    (False, "Their",
                     "egalik, lekin ko'plik."),
                    (False, "They're",
                     "qisqartma va ko'plik."),
                ])
            ),
        },

        {
            "rich_text": qnum(2, "~20 soniya") + conv_q(
                "<p>The three <span class=\"sr-blank\"></span> that survive from the yard "
                "are all for the same class of barge, and two of them are signed by the "
                "foreman rather than the owner.</p>"),
            "choices": [
                {"text": "half-models", "is_correct": True},
                {"text": "half-model's", "is_correct": False},
                {"text": "half-models'", "is_correct": False},
                {"text": "half-models's", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>3 soniyalik tell:</strong> "
                "<em>-s / -'s / -s'</em> — bu 70-dars.</p>"
                "<p>Bo'sh joydan keyin <em>that survive</em> — "
                "nisbiy gap, ot emas. Egalik yo'q, "
                "apostrof kerak emas. <em>The three</em> "
                "ko'plikni talab qiladi.</p>"
                + why([
                    (True, "half-models", "oddiy ko'plik."),
                    (False, "half-model's",
                     "egalik va birlik — ikki jihatdan "
                     "noto'g'ri."),
                    (False, "half-models'",
                     "egalik: keyin ot kerak bo'lardi."),
                    (False, "half-models's",
                     "bunday shakl yo'q."),
                ])
            ),
        },

        {
            "rich_text": qnum(3, "~30 soniya") + conv_q(
                "<p>The row of cottages built for the men who dug the tunnel "
                "<span class=\"sr-blank\"></span> at the top of the cutting, a hundred "
                "yards from the mouth and forty feet above it.</p>"),
            "choices": [
                {"text": "stands", "is_correct": True},
                {"text": "stand", "is_correct": False},
                {"text": "standing", "is_correct": False},
                {"text": "have stood", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>3 soniyalik tell:</strong> "
                "<em>stands / stand</em> — moslashuv, "
                "50-dars.</p>"
                "<p>Predlogli birikma va nisbiy gapni o'chiring: "
                "<em>The row</em> <s>of cottages</s> <s>built for "
                "the men</s> <s>who dug the tunnel</s> "
                "<mark>stands</mark>. Ega birlik.</p>"
                + why([
                    (True, "stands", "birlik shaxsli kesim."),
                    (False, "stand",
                     "ko'plik: <em>cottages</em> yoki "
                     "<em>men</em> ga moslashgan."),
                    (False, "standing",
                     "sifatdosh — gapda kesim qolmaydi."),
                    (False, "have stood",
                     "ko'plik yordamchi."),
                ])
            ),
        },

        {
            "rich_text": qnum(4, "~20 soniya") + conv_q(
                "<p>The kiln was fired only twice a year and each firing took nine days "
                "and nights <span class=\"sr-blank\"></span> the whole village smelled of "
                "woodsmoke for a fortnight afterwards.</p>"),
            "choices": [
                {"text": "of stoking;", "is_correct": True},
                {"text": "of stoking,", "is_correct": False},
                {"text": "of stoking", "is_correct": False},
                {"text": "of stoking:", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>3 soniyalik tell:</strong> variantlar "
                "faqat tinish belgisi bilan farq qiladi — "
                "chegara savoli, 30-32-darslar.</p>"
                "<p>Ikki tomon ham to'liq gap → bog'lovchisiz "
                "ulanish uchun <mark>nuqtali vergul</mark>.</p>"
                + why([
                    (True, "of stoking;",
                     "ikki mustaqil gapni bog'lovchisiz "
                     "ulaydi."),
                    (False, "of stoking,",
                     "vergul splaysi."),
                    (False, "of stoking",
                     "belgisiz qo'shilish."),
                    (False, "of stoking:",
                     "ikki nuqta izoh yoki ro'yxat kiritadi; "
                     "ikkinchi gap birinchisini izohlamaydi, "
                     "unga yangi fakt qo'shadi."),
                ])
            ),
        },

        {
            "rich_text": qnum(5, "~30 soniya") + conv_q(
                "<p>Left open to the weather for thirty years after the roof fell in, "
                "<span class=\"sr-blank\"></span> Only the vaulted undercroft, which had "
                "two feet of rubble over it, came through undamaged.</p>"),
            "choices": [
                {"text": "the abbey lost most of its carved stonework.",
                 "is_correct": True},
                {"text": "most of the abbey's carved stonework was lost.",
                 "is_correct": False},
                {"text": "there was little carved stonework left in the abbey.",
                 "is_correct": False},
                {"text": "frost destroyed most of the abbey's carved stonework.",
                 "is_correct": False},
            ],
            "explanation": (
                "<p><strong>3 soniyalik tell:</strong> to'rtta "
                "variant ham butun gap va har biri boshqa ot bilan "
                "boshlanadi — osilib qolgan bo'lak, "
                "72-dars.</p>"
                "<p><strong>NIMA ochiq qolgan?</strong> "
                "<mark>Abbatlik.</mark> Faqat birinchi otga "
                "qarang; qolgan so'zlarni o'qish shart "
                "emas.</p>"
                + why([
                    (True, "the abbey lost most of its carved",
                     "verguldan keyingi birinchi ot — "
                     "<em>the abbey</em>."),
                    (False, "most of the abbey's carved stonework was",
                     "ega — <em>most … stonework</em>; egalik "
                     "shakli abbatlikni ega qilmaydi."),
                    (False, "there was little carved stonework",
                     "<em>there</em> hech narsani "
                     "bildirmaydi."),
                    (False, "frost destroyed most of the abbey's",
                     "ega — <em>frost</em>; sovuq ochiq "
                     "qoldirilmagan."),
                ])
            ),
        },

        {
            "rich_text": qnum(6, "~20 soniya") + conv_q(
                "<p>The ledger records the name of every man who worked on the aqueduct, "
                "the days he worked and what he was paid, and "
                "<span class=\"sr-blank\"></span> is the only document of its kind to "
                "survive from the whole scheme.</p>"),
            "choices": [
                {"text": "it", "is_correct": True},
                {"text": "they", "is_correct": False},
                {"text": "them", "is_correct": False},
                {"text": "these", "is_correct": False},
            ],
            "explanation": (
                "<p><strong>3 soniyalik tell:</strong> "
                "<em>it / they / them / these</em> — olmosh "
                "savoli, 60-dars.</p>"
                "<p><strong>Nima yagona hujjat?</strong> "
                "<em>The ledger</em> — <mark>birlik</mark>. Va "
                "kesim ham buni aytadi: <em>___ <u>is</u></em>.</p>"
                + why([
                    (True, "it",
                     "birlik, ega o'rnida — <em>is</em> bilan "
                     "mos."),
                    (False, "they",
                     "ko'plik: <em>days</em> yoki <em>men</em> "
                     "ga moslashgan."),
                    (False, "them",
                     "to'ldiruvchi shakli — ega bo'lolmaydi."),
                    (False, "these",
                     "ko'plik ko'rsatish olmoshi."),
                ])
            ),
        },

        {"rich_text": (
            "<h3>Bu — kursning oxirgi darsi</h3>"
            "<p>To'qson uch dars orqada qoldi: o'qish yarmi "
            "(1-93) matnni qanday o'qishni, yozuv yarmi "
            "(W1-W93) esa jumlaning o'zini o'rgatdi. Endi "
            "qoladigan narsa — takrorlash va vaqt.</p>"
            + '<div class="sr-data"><div class="sr-data__scroll">'
            + "<table>"
              "<thead><tr><th>Imtihonga qadar</th><th>Nima qilish</th>"
              "</tr></thead>"
              "<tbody>"
              "<tr><td>Uzoq bo'lsa</td>"
              "<td>Har hafta bitta aralash mashq (W64, W74, W90, "
              "W91) va xato qilgan turingizning darsi</td></tr>"
              "<tr><td>Bir oy</td>"
              "<td>W92 ni haftada bir marta vaqt bilan; Bluebook'da "
              "to'liq mashq testi</td></tr>"
              "<tr><td>Bir hafta</td>"
              "<td>Faqat xatolaringiz ro'yxati. Yangi mavzu "
              "boshlamang</td></tr>"
              "<tr><td>Kechqurun</td>"
              "<td>Hech narsa. Uxlang. Ertalab miya "
              "tezligi tayyorgarlikdan muhimroq</td></tr>"
              "</tbody></table>"
            + '</div></div>'
            + TIP.format(
                "Imtihon xonasida esda tutadigan uchta jumla: "
                "<strong>variantlarni birinchi o'qing</strong>, "
                "<strong>qoidani ayting</strong>, "
                "<strong>hech qachon bo'sh qoldirmang</strong>. "
                "Qolganini bilib bo'ldingiz.")
            + "<h3>Kalit so'zlar — Key vocabulary</h3>"
            + '<div class="pp-flashcards" data-pp-flashcards>'
            + '<div class="pp-card"><div class="pp-card-front">to flag a question</div><div class="pp-card-back">savolni belgilab qo\'ymoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a guessing penalty</div><div class="pp-card-back">taxmin uchun jarima (SATda yo\'q)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a cutting (railway)</div><div class="pp-card-back">qazilgan yo\'l o\'yig\'i</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a half-model</div><div class="pp-card-back">kemaning yarim maketi</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">to stoke</div><div class="pp-card-back">pechga o\'tin tashlamoq</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an undercroft</div><div class="pp-card-back">yerto\'la (gumbazli)</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">an aqueduct</div><div class="pp-card-back">suv o\'tkazgich ko\'prik</div></div>'
            + '<div class="pp-card"><div class="pp-card-front">a scheme (project)</div><div class="pp-card-back">yirik qurilish loyihasi</div></div>'
            + "</div>"
            + "<h3>Xulosa</h3>"
            + "<ul>"
              "<li>Har bir savol bir xil ball beradi — "
              "<strong>eng arzonidan boshlang</strong>.</li>"
              "<li>Variantlar ro'yxati savolning narxini uch "
              "soniyada aytadi.</li>"
              "<li>Tinish belgisi, apostrof va moslashuv "
              "savollari — 20-30 soniyalik ballar.</li>"
              "<li>Rhetorical Synthesis — oxirgi besh daqiqada "
              "eng qimmat savol; taxmin qiling va "
              "o'ting.</li>"
              "<li><strong>Bo'sh savol nol beradi. Har doim "
              "belgilang.</strong></li>"
              "</ul>"
        )},
    ],
},
]
