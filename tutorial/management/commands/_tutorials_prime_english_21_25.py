# -*- coding: utf-8 -*-
"""Prime English — Block B, lessons 21–25 (the past tenses).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_21_25.py --author=prime
"""

PLAYLIST = {
    "title": "Prime English",
    "category": "english",
    "description": (
        "English grammar from zero to fluent — 100 lessons with colour-coded sentence "
        "patterns, Uzbek explanations and practice you can check yourself."
    ),
}

LEGEND = """
<div class="pe-legend">
  <span><i style="background:#2563eb"></i>subject — ega</span>
  <span><i style="background:#16a34a"></i>verb — kesim</span>
  <span><i style="background:#d97706"></i>object — toʻldiruvchi</span>
  <span><i style="background:#8b5cf6"></i>helper verb — yordamchi feʼl</span>
</div>
"""

TUTORIALS = [
    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-21: Past Simple: Irregular Verbs",
        "category": "english",
        "order": 21,
        "summary": (
            "The 180 verbs that refuse -ed — and they are the ones you need most. Learn them "
            "in sound families instead of one long alphabetical list."
        ),
        "content": """
<h2>PE-21: Past Simple: Irregular Verbs</h2>

<p>You learned the friendly rule in PE-20: add <b>-ed</b>. Now meet the rebels. About
<b>180</b> English verbs change their shape instead — <em>go → went</em>, <em>see → saw</em>,
<em>buy → bought</em>. And here is the annoying part: they are the <mark>most common verbs in
the language</mark>. Old, short, everyday words resist change, in every language. The good
news is that they are not random — they come in families of sound.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Why irregular verbs exist and why they are worth the effort</li>
    <li>Six sound families that make memorising three times faster</li>
    <li>The 25 verbs you truly cannot live without</li>
    <li>The <em>read → read</em> trap: same spelling, different sound</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence — same for every person</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">past form (V2)</span>
  <span class="pe-chip pe-chip--opt">I went · she went · they went</span>
</div>

LEGEND_HERE

<h3>1. The good news first</h3>

<p>Irregular verbs look frightening, but they only change in <b>one</b> place — the positive
sentence. And like regular verbs, the form is identical for every person.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">went</span> to the bazaar and
     <span class="pe-hl pe-hl--v">bought</span> some bread.
     <span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--v">came</span> with me.</p>
  <p class="pe-ex__uz">Men bozorga bordim va non sotib oldim. Afsona men bilan keldi.</p>
  <p class="pe-ex__why"><em>Went</em>, <em>bought</em>, <em>came</em> — no <b>-s</b>, no
     <b>-ed</b>, nothing to adjust.</p>
</div>

<h3>2. The sound families</h3>

<p>Do not learn irregular verbs alphabetically — that is the slowest possible method. Learn
them by the sound they make. Your ear remembers patterns far better than your eye remembers
lists.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>No change at all</p>
    <p><em>cut, put, let, hit, shut, cost, hurt, read</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>i → a</p>
    <p><em>drink→drank, sing→sang, swim→swam, begin→began, ring→rang, sit→sat</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>i → o</p>
    <p><em>drive→drove, write→wrote, ride→rode, rise→rose</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>ee/ea → e + t</p>
    <p><em>keep→kept, sleep→slept, feel→felt, leave→left, meet→met, mean→meant</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>the -ought / -aught family</p>
    <p><em>buy→bought, bring→brought, think→thought, teach→taught, catch→caught</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">6</span>completely different</p>
    <p><em>go→went, see→saw, do→did, take→took, come→came</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yodlash usuli: alifbo tartibida emas, <b>tovush guruhlari</b> boʻyicha oʻrganing. Masalan
  5-guruhni ovoz chiqarib ayting: <em>bought — brought — thought — taught — caught</em>.
  Hammasi bir xil eshitiladi, shuning uchun bittasini eslasangiz, qolgan toʻrttasi oʻzi
  keladi. Kuniga bitta guruh — bir haftada asosiylari tugaydi.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Say family 5 aloud: <b>buy → bought</b>, <b>bring → brought</b>,
     <b>think → thought</b>, <b>teach → taught</b>, <b>catch → caught</b>.</p>
  <p class="pe-ex__uz">Sotib olmoq, olib kelmoq, oʻylamoq, oʻrgatmoq, ushlamoq.</p>
  <p class="pe-ex__why">Five verbs, one sound. Remember the sound and you remember all five.</p>
</div>

<h3>3. The 25 you cannot live without</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Base</th><th>Past</th><th>Oʻzbekcha</th><th>Base</th><th>Past</th><th>Oʻzbekcha</th></tr>
  <tr><td>be</td><td><b>was/were</b></td><td>boʻlmoq</td><td>know</td><td><b>knew</b></td><td>bilmoq</td></tr>
  <tr><td>go</td><td><b>went</b></td><td>bormoq</td><td>think</td><td><b>thought</b></td><td>oʻylamoq</td></tr>
  <tr><td>have</td><td><b>had</b></td><td>ega boʻlmoq</td><td>tell</td><td><b>told</b></td><td>aytmoq</td></tr>
  <tr><td>do</td><td><b>did</b></td><td>qilmoq</td><td>say</td><td><b>said</b></td><td>demoq</td></tr>
  <tr><td>see</td><td><b>saw</b></td><td>koʻrmoq</td><td>find</td><td><b>found</b></td><td>topmoq</td></tr>
  <tr><td>get</td><td><b>got</b></td><td>olmoq</td><td>give</td><td><b>gave</b></td><td>bermoq</td></tr>
  <tr><td>make</td><td><b>made</b></td><td>yasamoq</td><td>eat</td><td><b>ate</b></td><td>yemoq</td></tr>
  <tr><td>take</td><td><b>took</b></td><td>olmoq</td><td>drink</td><td><b>drank</b></td><td>ichmoq</td></tr>
  <tr><td>come</td><td><b>came</b></td><td>kelmoq</td><td>write</td><td><b>wrote</b></td><td>yozmoq</td></tr>
  <tr><td>buy</td><td><b>bought</b></td><td>sotib olmoq</td><td>read</td><td><b>read</b></td><td>oʻqimoq</td></tr>
  <tr><td>bring</td><td><b>brought</b></td><td>olib kelmoq</td><td>run</td><td><b>ran</b></td><td>yugurmoq</td></tr>
  <tr><td>leave</td><td><b>left</b></td><td>ketmoq</td><td>sleep</td><td><b>slept</b></td><td>uxlamoq</td></tr>
  <tr><td>meet</td><td><b>met</b></td><td>uchrashmoq</td><td>speak</td><td><b>spoke</b></td><td>gapirmoq</td></tr>
</table>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>read → read.</b> The spelling never changes, but the sound does: present <em>/riːd/</em>
  (like "reed"), past <em>/red/</em> (like the colour). Only the sentence tells you which one
  it is: <em>I <b>read</b> a book every week</em> vs <em>I <b>read</b> that book last
  year</em>.
</div>

<h3>4. Where the irregular form is used — and where it is not</h3>

<p>This is the point that saves you from the most common error of all. The special past form
appears <b>only in positive sentences</b>. As soon as you add the helper <em>did</em> (PE-22),
the verb goes back to its plain base form.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✓ Positive → the past form</p>
    <ul>
      <li>I <b>went</b> to school.</li>
      <li>She <b>bought</b> a phone.</li>
      <li>They <b>saw</b> the film.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✓ With <em>did</em> → the base form</p>
    <ul>
      <li>I <b>didn't go</b> to school.</li>
      <li><b>Did</b> she <b>buy</b> a phone?</li>
      <li>They <b>didn't see</b> the film.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani shunday eslang: oʻtgan zamon belgisi gapda <b>faqat bir marta</b> boʻladi. Agar
  <b>did</b> bor boʻlsa, oʻtganlik allaqachon koʻrsatilgan — shuning uchun asosiy feʼl
  <b>asl shakliga</b> qaytadi: <s>I didn't went</s> emas, <b>I didn't go</b>. Bu PE-10 dagi
  "bitta koptok" qoidasi bilan bir xil.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Last year my uncle <b>taught</b> me to drive. I <b>drove</b> his old
     car and <b>felt</b> like a real adult.</p>
  <p class="pe-ex__uz">Oʻtgan yili amakim menga haydashni oʻrgatdi. Uning eski mashinasini
     haydadim va oʻzimni katta odamdek his qildim.</p>
  <p class="pe-ex__why">Three families in one sentence: <em>-aught</em>, <em>i → o</em>, and
     <em>ee → e + t</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Feʼlni <b>uchtalik</b> qilib yodlang: <em>go – went – gone</em>. Uchinchi shakl (V3) hozir
  kerak emas, lekin PE-32 da kerak boʻladi va uni keyin qaytadan oʻrganish ikki barobar
  koʻp vaqt oladi. Yana bir ogohlantirish: <b>V2 va V3 ni aralashtirmang</b> —
  <em>I <b>went</b></em> ✓, <s>I have went</s> ✗ (toʻgʻrisi <em>I have <b>gone</b></em>).
</div>

<h3>5. How to actually learn them</h3>

<ol class="pe-steps">
  <li><b>Learn in threes from the start</b> — <em>go, went, gone</em>. The third form
      (participle) is needed in PE-32, so learning it now costs nothing extra.</li>
  <li><b>Say them aloud in family chains</b>, not silently: <em>think–thought,
      bring–brought, buy–bought</em>.</li>
  <li><b>Use them the same day</b> in one sentence about your own life. A verb you have used
      once is worth ten you have only read.</li>
  <li><b>Keep a small list of your personal enemies</b> — the five that keep escaping you —
      and revise only those.</li>
</ol>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I goed to my grandmother's house.</s></p>
  <p class="pe-good">Yesterday I <b>went</b> to my grandmother's house.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She buyed a new dress and catched the bus.</s></p>
  <p class="pe-good">She <b>bought</b> a new dress and <b>caught</b> the bus.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I thinked about your question.</s></p>
  <p class="pe-good">I <b>thought</b> about your question.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He didn't went to the party.</s></p>
  <p class="pe-good">He <b>didn't go</b> to the party.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>They eated everything and drinked all the tea.</s></p>
  <p class="pe-good">They <b>ate</b> everything and <b>drank</b> all the tea.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Give the past forms: <em>bring · sleep · swim · put · take</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>brought</strong> (-ought family), <strong>slept</strong> (ee → e+t),
         <strong>swam</strong> (i → a), <strong>put</strong> (no change),
         <strong>took</strong> (its own).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Put into the past: <em>Sherbek gets up at six, has breakfast and goes to school.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sherbek got up at six, had breakfast and went to school.</strong></p>
      <p>Three irregulars in one sentence — and none of them keeps the <b>-s</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which family does each belong to? <em>teach · begin · keep</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>teach → taught</strong> (-aught family), <strong>begin → began</strong>
         (i → a), <strong>keep → kept</strong> (ee → e + t).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     How do you say <b>read</b> in each sentence? <em>(a) I read books every night.
     (b) I read your letter yesterday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) /riːd/</strong> — present. <strong>(b) /red/</strong> — past, like the
         colour. Same five letters, two different words in speech.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Find the mistake: <em>My father teached me to swim when I was six.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My father taught me to swim when I was six.</strong></p>
      <p><em>Teach</em> belongs to the <b>-aught</b> family, together with <em>catch →
         caught</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Irregular verb</b><span>qoidasiz feʼl</span></li>
  <li><b>Base form</b><span>asl shakl</span></li>
  <li><b>Past form (V2)</b><span>oʻtgan zamon shakli</span></li>
  <li><b>Participle (V3)</b><span>sifatdosh shakli</span></li>
  <li><b>Pattern</b><span>qolip, namuna</span></li>
  <li><b>To memorise</b><span>yodlamoq</span></li>
  <li><b>To catch</b><span>ushlamoq, yetib olmoq</span></li>
  <li><b>To bring</b><span>olib kelmoq</span></li>
  <li><b>To leave</b><span>ketmoq, tashlab ketmoq</span></li>
  <li><b>Spelling</b><span>imlo</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Irregular verbs change shape instead of taking <b>-ed</b> — and they are the commonest
        verbs.</li>
    <li>The past form is the <b>same for every person</b>: <em>I went, she went, they went</em>.</li>
    <li>Learn them in <b>sound families</b>, and always in threes: <em>go, went, gone</em>.</li>
    <li>After <b>did / didn't</b> the verb returns to its base form.</li>
    <li><b>read → read</b>: same spelling, the past sounds like "red".</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-22: Past Simple: Negatives and Questions",
        "category": "english",
        "order": 22,
        "summary": (
            "One helper verb — did — handles every person and every verb, regular or "
            "irregular. Plus the rule that stops 'Did you went?' forever."
        ),
        "content": """
<h2>PE-22: Past Simple: Negatives and Questions</h2>

<p>Now the reward for all that irregular-verb work. To ask or deny anything in the past,
English uses <b>one single helper</b>: <mark>did</mark>. Not <em>do/does</em> depending on the
person — just <b>did</b>, for everybody. And it works identically for regular and irregular
verbs, so all those forms you memorised suddenly get simpler, not harder.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Negatives with <b>didn't</b> and questions with <b>Did</b></li>
    <li>The rule that the main verb goes back to its <b>base form</b></li>
    <li>Short answers and Wh- questions in the past</li>
    <li>The two cases where <b>did</b> must <b>not</b> appear</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Negative</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">didn't</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
</div>
<div class="pe-formula">
  <span class="pe-formula__label">Question</span>
  <span class="pe-chip pe-chip--aux">Did</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
  <span class="pe-op">?</span>
</div>

LEGEND_HERE

<h3>1. One helper for everybody</h3>

<p>Compare the present and the past for a moment, and you will see how much easier the past
is:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Present — two helpers</p>
    <ul>
      <li>I <b>don't</b> work. / He <b>doesn't</b> work.</li>
      <li><b>Do</b> you work? / <b>Does</b> he work?</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Past — one helper</p>
    <ul>
      <li>I <b>didn't</b> work. / He <b>didn't</b> work.</li>
      <li><b>Did</b> you work? / <b>Did</b> he work?</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--aux">didn't</span>
     <span class="pe-hl pe-hl--v">come</span> to school yesterday. —
     <span class="pe-hl pe-hl--aux">Did</span>
     <span class="pe-hl pe-hl--s">she</span>
     <span class="pe-hl pe-hl--v">call</span> you?</p>
  <p class="pe-ex__uz">Afsona kecha maktabga kelmadi. — U senga qoʻngʻiroq qildimi?</p>
</div>

<h3>2. The golden rule, again</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  <b>Did</b> is already the past. So the main verb drops all past marking and returns to its
  base form — no <b>-ed</b>, and no irregular form either.
  <em>I <b>didn't watch</b></em> ✓ · <em>I <b>didn't go</b></em> ✓ ·
  <s>I didn't watched</s> · <s>Did you went?</s>
</div>

<p>Watch the change happen. The past marking moves backwards onto the helper and the main verb
relaxes:</p>

<div class="pe-ex">
  <p class="pe-ex__en">She <b>bought</b> a car. → She <b>didn't buy</b> a car. →
     <b>Did</b> she <b>buy</b> a car?</p>
  <p class="pe-ex__uz">U mashina sotib oldi. → U mashina sotib olmadi. → U mashina sotib
     oldimi?</p>
  <p class="pe-ex__why">Follow the past: <em>bought</em> → <em>did</em> + <em>buy</em>.
     It never appears twice.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada inkor feʼlning ichida yasaladi: <em>bor<b>di</b></em> → <em>bor<b>ma</b>di</em>.
  Ingliz tilida esa <b>alohida yordamchi feʼl</b> keladi va u oʻtganlikni oʻz zimmasiga
  oladi: <em>went</em> → <em><b>didn't go</b></em>. Shuning uchun asosiy feʼlni yana oʻtgan
  zamonga qoʻysangiz — bu <b>ikki marta</b> oʻtgan zamon boʻlib qoladi, va bu xato.
</div>

<h3>3. Short answers and Wh- questions</h3>

<p>Short answers repeat the helper — never the main verb. This is the natural, polite way to
answer in English.</p>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>Did</b> you enjoy the film? — <b>Yes, I did.</b> /
     <b>No, I didn't.</b></p>
  <p class="pe-ex__uz">— Kino senga yoqdimi? — Ha. / Yoʻq.</p>
  <p class="pe-ex__why">Not <s>Yes, I enjoyed</s> — the helper carries the answer.</p>
</div>

<p>Wh- questions put the question word in front, and everything else stays exactly the same:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Where did</b> you go? <b>What did</b> you buy? <b>Why didn't</b>
     you tell me?</p>
  <p class="pe-ex__uz">Qayerga bording? Nima sotib olding? Nega menga aytmading?</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Soʻroq soʻzli gaplarda <b>did</b> ni tushirib qoldirmang. Oʻzbekchada "Qayerga bording?"
  da yordamchi soʻz yoʻq, shuning uchun <s>Where you went?</s> deb yozib qoʻyish juda oson.
  Toʻgʻri tartib: <b>soʻroq soʻzi → did → ega → asl feʼl</b>:
  <em><b>Where did you go</b>?</em>
</div>

<h3>4. Two places where "did" must NOT appear</h3>

<ol class="pe-steps">
  <li><b>With was / were.</b> The verb <em>to be</em> never takes a helper —
      it inverts by itself: <em><b>Were</b> you at home?</em>, not <s>Did you were</s>.
      (PE-19)</li>
  <li><b>In subject questions.</b> When <em>who</em> or <em>what</em> is the subject, there is
      nothing to invert: <em><b>Who broke</b> the window?</em>, not <s>Who did break</s>.
      Notice that the verb keeps its past form here.</li>
</ol>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Asking about the object → did</p>
    <p><b>Who did</b> Afsona <b>invite</b>?</p>
    <p>(Afsona invited somebody — who?)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Asking about the subject → no did</p>
    <p><b>Who invited</b> Afsona?</p>
    <p>(Somebody invited Afsona — who?)</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ingliz tilida <b>did</b> yana bir vazifada ishlatiladi — <b>taʼkidlash</b> uchun:
  <em>I <b>did</b> tell you!</em> = "Men senga <b>aytdim-ku</b>!" Bu yerda <em>did</em>
  inkor ham, savol ham emas, balki "haqiqatan ham" degan maʼnoni kuchaytiradi. Uni
  gapirganda urgʻu bilan aytiladi.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Did you went to the party?</s></p>
  <p class="pe-good"><b>Did you go</b> to the party?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I didn't saw him yesterday.</s></p>
  <p class="pe-good">I <b>didn't see</b> him yesterday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Where you went last summer?</s></p>
  <p class="pe-good"><b>Where did you go</b> last summer?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did she was at home?</s></p>
  <p class="pe-good"><b>Was she</b> at home?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Who did break the window?</s></p>
  <p class="pe-good"><b>Who broke</b> the window?</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make negative: <em>Jasur ate all the plov.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur didn't eat all the plov.</strong></p>
      <p><em>Ate</em> → <b>eat</b>: the helper takes the past, so the irregular form
         disappears.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make a question: <em>They finished the project last week.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Did they finish the project last week?</strong></p>
      <p>The <b>-ed</b> is gone, because <em>did</em> is already past.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which one is correct, and why? <em>(a) Who did win the game? (b) Who won the game?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) Who won the game?</strong> — <em>Who</em> is the subject, so there is no
         inversion and no helper; the verb keeps its past form.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Fix two mistakes: <em>Did your sister was at the wedding? — No, she didn't.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Was your sister at the wedding? — No, she wasn't.</strong></p>
      <p><em>To be</em> takes no helper, and the short answer must repeat the same verb —
         <b>wasn't</b>, not <em>didn't</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Ask about the underlined part: <em>Sherbek went to Samarkand <u>by train</u>.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>How did Sherbek go to Samarkand?</strong></p>
      <p>Question word first, then <em>did</em>, then the subject, then the <b>base</b>
         verb.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Helper verb</b><span>yordamchi feʼl</span></li>
  <li><b>Base form</b><span>asl shakl</span></li>
  <li><b>Negative</b><span>inkor gap</span></li>
  <li><b>Question form</b><span>soʻroq shakli</span></li>
  <li><b>Short answer</b><span>qisqa javob</span></li>
  <li><b>Subject question</b><span>egaga savol</span></li>
  <li><b>Emphasis</b><span>taʼkid</span></li>
  <li><b>To enjoy</b><span>zavq olmoq</span></li>
  <li><b>To invite</b><span>taklif qilmoq</span></li>
  <li><b>To win</b><span>yutmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>didn't + base verb</b> · <b>Did + subject + base verb?</b> — one helper for all
        persons.</li>
    <li>The past appears once: if <b>did</b> is there, the main verb is bare.</li>
    <li>Short answers repeat the helper: <b>Yes, I did. / No, I didn't.</b></li>
    <li>No <b>did</b> with <b>was/were</b>, and no <b>did</b> in subject questions.</li>
    <li><b>did</b> can also add emphasis: <em>I did tell you!</em></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-23: Past Continuous: The Interrupted Moment",
        "category": "english",
        "order": 23,
        "summary": (
            "What were you doing at eight o'clock last night? The tense that paints the "
            "background of a story: was/were + verb-ing."
        ),
        "content": """
<h2>PE-23: Past Continuous: The Interrupted Moment</h2>

<p>"What <b>were</b> you <b>doing</b> at eight o'clock last night?" You cannot answer that
question with the Past Simple, because it does not ask what you <em>did</em> — it asks what
was <b>in progress</b> at that moment. This is the tense that sets scenes, paints backgrounds,
and makes stories feel alive instead of like a list.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The formula <b>was / were + verb-ing</b></li>
    <li>Four jobs: a past moment, two parallel actions, a background, an interrupted action</li>
    <li>Negatives, questions and the signal words</li>
    <li>Why stative verbs still refuse the <b>-ing</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">was / were</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
</div>

LEGEND_HERE

<h3>1. The picture: a band around a past moment</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:82%"></span>
    <span class="pe-tl-band" style="left:14%;width:38%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:33%"></span>
    <span class="pe-tl-tag" style="left:33%">8 p.m. — I was reading</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The action started <b>before</b> eight o'clock and finished <b>after</b> it. At eight
o'clock itself, it was simply in the middle. That "middle" is exactly what this tense
expresses.</p>

<div class="pe-ex">
  <p class="pe-ex__en">At nine o'clock last night <span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">was</span>
     <span class="pe-hl pe-hl--v">doing</span> my homework and my sister
     <span class="pe-hl pe-hl--aux">was</span>
     <span class="pe-hl pe-hl--v">watching</span> TV.</p>
  <p class="pe-ex__uz">Kecha soat toʻqqizda men uy vazifamni qilayotgan edim, singlim esa
     televizor koʻrayotgan edi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Past Continuous oʻzbekchadagi <b>-ayotgan edi / -yotgan edim</b> shakliga toʻgʻri keladi:
  <em>oʻqi<b>yotgan edim</b></em> = <em>I <b>was reading</b></em>. Eʼtibor bering, oʻzbekchada
  ham ikkita boʻlak bor — "oʻqiyotgan" va "edim". Ingliz tilida ham shunday:
  <b>was/were</b> + <b>-ing</b>. Biri tushib qolmasin.
</div>

<h3>2. The four jobs</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>At a past moment</p>
    <p><em>At 7 a.m. I <b>was sleeping</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Two actions at once</p>
    <p><em>She <b>was cooking</b> while he <b>was cleaning</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Background of a story</p>
    <p><em>The sun <b>was shining</b> and the birds <b>were singing</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Interrupted action</p>
    <p><em>I <b>was walking</b> home when it started to rain.</em></p>
  </div>
</div>

<p>Job 3 is why every good story in English starts in this tense. It builds the scene before
anything happens — and then the Past Simple arrives and something <em>does</em> happen.</p>

<div class="pe-ex">
  <p class="pe-ex__en">It <b>was getting</b> dark and a cold wind <b>was blowing</b>.
     Suddenly, someone <b>knocked</b> at the door.</p>
  <p class="pe-ex__uz">Qorongʻi tushayotgan va sovuq shamol esayotgan edi. Toʻsatdan kimdir
     eshikni taqillatdi.</p>
  <p class="pe-ex__why">Two sentences of background, then one short action. That is the shape
     of a story.</p>
</div>

<h3>3. Negatives and questions</h3>

<p>The first word is <em>was</em> or <em>were</em>, so you already know the rest from PE-19:
add <b>not</b>, or swap the first two words. No <em>did</em> anywhere.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>wasn't sleeping</b> — I <b>was studying</b>. —
     <b>Were</b> you <b>waiting</b> long? — No, I <b>wasn't</b>.</p>
  <p class="pe-ex__uz">Men uxlayotganim yoʻq edi — oʻqiyotgan edim. — Uzoq kutdingizmi? —
     Yoʻq.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  The <b>-ing</b> word never changes and never carries the past. Only <em>was/were</em> does
  the work: <s>I was played</s> ✗, <s>They was playing</s> ✗ →
  <b>I was playing</b>, <b>They were playing</b> ✓.
</div>

<h3>4. Stative verbs are still forbidden</h3>

<p>The rule from PE-13 does not change when you move into the past. Verbs of thinking, feeling,
belonging and the senses stay in the Simple even when the moment is clearly "in progress".</p>

<div class="pe-fix">
  <p class="pe-bad"><s>I was knowing the answer, but I was wanting to think more.</s></p>
  <p class="pe-good">I <b>knew</b> the answer, but I <b>wanted</b> to think more.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda ham oʻzbekcha mantiqingiz toʻgʻri ishlaydi: siz "bil<b>ayotgan edim</b>" yoki
  "xohla<b>yotgan edim</b>" demaysiz — <em>bilardim</em>, <em>xohlardim</em> deysiz. Ingliz
  tilida ham xuddi shunday: <b>I knew</b>, <b>I wanted</b>. Holat feʼllari hech qachon
  <b>-ing</b> olmaydi — na hozirgi, na oʻtgan zamonda.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ehtiyot boʻling — bu zamonni haddan ortiq ishlatmang. "Kecha maktabga bordim" kabi
  <b>tugallangan</b> ish uchun Past Simple kerak: <em>I <b>went</b> to school</em>,
  <s>I was going to school</s> emas. Past Continuous faqat "oʻsha paytda <b>davom
  etayotgan</b>" ishni bildiradi.
</div>

<h3>5. Signal words</h3>

<p>These phrases usually mean Past Continuous: <em>at 8 o'clock last night, at that moment,
all day yesterday, all morning, while, as, when … was/were, the whole evening</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>was studying all day</b> yesterday, and at midnight she
     <b>was still working</b>.</p>
  <p class="pe-ex__uz">Afsona kecha kun boʻyi oʻqidi va yarim tunda hamon ishlayotgan edi.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>They was playing in the yard.</s></p>
  <p class="pe-good">They <b>were</b> playing in the yard.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I was play football at five.</s></p>
  <p class="pe-good">I <b>was playing</b> football at five.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did you were watching TV?</s></p>
  <p class="pe-good"><b>Were you watching</b> TV?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She was seeing a bird in the garden.</s></p>
  <p class="pe-good">She <b>saw</b> a bird in the garden. <em>(stative verb)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I was going to school and I was studying English.</s></p>
  <p class="pe-good">Yesterday I <b>went</b> to school and <b>studied</b> English.
     <em>(finished actions → Past Simple)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>At six o'clock yesterday my mother <span class="pe-blank">?</span> (cook)
     dinner.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>was cooking</strong> — the question asks what was in progress at that exact
         past moment.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it a question and a negative: <em>They were waiting for the bus.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Were they waiting for the bus? / They weren't waiting for the bus.</strong></p>
      <p>Only <em>were</em> moves or takes <em>not</em>; <em>waiting</em> stays untouched.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which is wrong? <em>(a) I was hearing a strange noise. (b) I heard a strange noise.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) is wrong.</strong> <em>Hear</em> is a stative verb. If you want the
         "in progress" idea, change the verb: <em>I <b>was listening</b> to a strange
         noise.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Write the background of a story in two sentences (Past Continuous only).</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>It <b>was raining</b> heavily and the streets
         <b>were getting</b> empty. Nobody <b>was walking</b> outside.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Two mistakes: <em>What did you doing when I was call you?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>What were you doing when I called you?</strong></p>
      <p>(1) The Continuous uses <em>were</em>, never <em>did</em>. (2) The short interrupting
         action takes the Past Simple — that is exactly PE-24.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Past Continuous</b><span>oʻtgan davomli zamon</span></li>
  <li><b>In progress</b><span>davom etayotgan</span></li>
  <li><b>Background</b><span>fon, orqa manzara</span></li>
  <li><b>To interrupt</b><span>boʻlmoq, xalaqit bermoq</span></li>
  <li><b>At that moment</b><span>oʻsha lahzada</span></li>
  <li><b>Suddenly</b><span>toʻsatdan</span></li>
  <li><b>To shine</b><span>porlamoq</span></li>
  <li><b>To blow (wind)</b><span>esmoq</span></li>
  <li><b>Still</b><span>hamon</span></li>
  <li><b>The whole evening</b><span>butun kechqurun</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>was / were + verb-ing</b> — both parts, and only <em>was/were</em> shows the past.</li>
    <li>It shows an action <b>in the middle</b> of a past moment, not a finished one.</li>
    <li>Perfect for story backgrounds and for two actions happening at once.</li>
    <li>Questions and negatives work like <b>to be</b> — never use <em>did</em>.</li>
    <li>Stative verbs (<b>know, want, hear, see</b>) still refuse <b>-ing</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-24: Past Simple vs Past Continuous: when and while",
        "category": "english",
        "order": 24,
        "summary": (
            "The long action and the short one: how English tells a story with two tenses, and "
            "which of them follows 'when' and which follows 'while'."
        ),
        "content": """
<h2>PE-24: Past Simple vs Past Continuous: when and while</h2>

<p><em>I was walking home <b>when</b> I met my old teacher.</em> Two actions, two different
tenses — and the choice is not decoration. It tells your listener which action was the
<b>long background</b> and which one was the <b>short event that cut into it</b>. Get this
pair right and your storytelling in English becomes instantly natural.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The long-action / short-action rule</li>
    <li>Which tense follows <b>when</b> and which follows <b>while</b></li>
    <li>What changes when both verbs are in the same tense</li>
    <li>How to punctuate these sentences</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The interruption</span>
  <span class="pe-chip pe-chip--aux">was/were + -ing</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">long background</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">verb + ed / V2</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">short interruption</span>
</div>

<h3>1. The picture</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:84%"></span>
    <span class="pe-tl-band" style="left:12%;width:46%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:38%"></span>
    <span class="pe-tl-tag" style="left:20%">I was walking home</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The band is the long action, already in progress. The red dot is the short action that
happened <b>inside</b> it. In English, the band is Past Continuous and the dot is Past
Simple — always.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--aux">I was cooking</span> dinner
     <b>when</b> <span class="pe-hl pe-hl--v">the lights went out</span>.</p>
  <p class="pe-ex__uz">Men kechki ovqat pishirayotganimda chiroq oʻchdi.</p>
  <p class="pe-ex__why">Cooking took a long time; the lights went out in one second.</p>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  <b>Long action → Past Continuous. Short action → Past Simple.</b> The long one usually
  started earlier and did not finish; the short one happened at one point inside it.
</div>

<h3>2. when or while?</h3>

<p>Both words join the two halves, but each one prefers a different tense next to it. This is
the part that decides marks in an exam.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">while + the LONG action</p>
    <ul>
      <li><b>While</b> I <b>was reading</b>, the phone rang.</li>
      <li><b>While</b> she <b>was sleeping</b>, we made lunch.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">when + the SHORT action</p>
    <ul>
      <li>I was reading <b>when</b> the phone <b>rang</b>.</li>
      <li>She was sleeping <b>when</b> we <b>arrived</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oddiy eslatma: <b>while</b> — "...ayotganimda", yaʼni undan keyin <b>uzun</b> ish keladi
  (<em>while I was reading</em>). <b>When</b> — "...qachonki", undan keyin <b>qisqa</b> ish
  keladi (<em>when the phone rang</em>). Oʻzbekchada ikkalasi ham "-ganda" bilan
  tarjima qilinadi, shuning uchun ingliz tilida qaysi biri qaysi ishga ulanishini alohida
  eslab qolish kerak.
</div>

<h3>3. When both verbs are the same tense</h3>

<p>The meaning changes completely depending on which tenses you pair. Look at these three
sentences — same words, three different stories.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Continuous + Simple</p>
    <p><em>I <b>was leaving</b> when he <b>arrived</b>.</em><br>
       I hadn't left yet — he caught me.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Simple + Simple</p>
    <p><em>When he <b>arrived</b>, I <b>left</b>.</em><br>
       First he arrived, then I left. A sequence.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Continuous + Continuous</p>
    <p><em>While I <b>was cooking</b>, he <b>was cleaning</b>.</em><br>
       Both long, both at the same time.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>When</b> the teacher <b>came in</b>, everybody <b>stood up</b>.</p>
  <p class="pe-ex__uz">Oʻqituvchi kirganda, hamma oʻrnidan turdi.</p>
  <p class="pe-ex__why">Two short actions in order — so both are Past Simple. No Continuous
     needed.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkala feʼl ham Past Simple boʻlsa — bu <b>ketma-ketlik</b>: avval biri, keyin ikkinchisi
  ("kirdi, keyin turdi"). Ikkalasi ham Past Continuous boʻlsa — bu <b>bir vaqtda</b>
  ketayotgan ikki ish ("men pishirayotgan edim, u tozalayotgan edi"). Yaʼni zamonlar
  tanlovi grammatika emas, <b>maʼno</b> masalasi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Zamon tanlovi maʼnoni butunlay oʻzgartiradi. <em>When I arrived, she <b>was making</b>
  tea</em> = men kelganimda choy <b>allaqachon damlanayotgan edi</b>. <em>When I arrived,
  she <b>made</b> tea</em> = men kelganimdan <b>keyin</b> choy damladi (ehtimol men uchun).
  Bitta soʻz oʻzgardi — voqea esa boshqacha boʻldi.
</div>

<h3>4. The comma rule</h3>

<p>If the sentence <b>begins</b> with <em>when</em> or <em>while</em>, put a comma in the
middle. If the joining word sits in the middle, no comma is needed.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>While</b> I was walking home<b>,</b> I saw an accident. —
     I saw an accident <b>while</b> I was walking home.</p>
  <p class="pe-ex__uz">Uyga ketayotganimda, baxtsiz hodisani koʻrdim.</p>
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>While I watched TV, the phone was ringing.</s></p>
  <p class="pe-good"><b>While I was watching</b> TV, the phone <b>rang</b>. <em>(the tenses were swapped)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I was seeing him when I was going to school.</s></p>
  <p class="pe-good">I <b>saw</b> him <b>while I was going</b> to school.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>When I was doing my homework, my pen was breaking.</s></p>
  <p class="pe-good">When I <b>was doing</b> my homework, my pen <b>broke</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>While the accident happened, I was crossing the road.</s></p>
  <p class="pe-good"><b>When</b> the accident <b>happened</b>, I <b>was crossing</b> the road.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I was going to the market and I was buying fruit.</s></p>
  <p class="pe-good">Yesterday I <b>went</b> to the market and <b>bought</b> fruit.
     <em>(two finished actions)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>Jasur <span class="pe-blank">?</span> (ride) his bike when he
     <span class="pe-blank">?</span> (fall).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>was riding … fell.</strong> Riding is the long background; falling happened
         in one instant.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     when or while? <em>___ we were having dinner, the electricity went off.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>While</strong> — it is followed by the long action in the Past Continuous.
         You could also say: <em>We were having dinner <b>when</b> the electricity went
         off.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) When I arrived, she was making tea. (b) When I arrived,
     she made tea.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) She started before I arrived</strong> — the tea was already being made.
         <strong>(b) She started after I arrived</strong> — probably because I came.</p>
      <p>One tense, two completely different stories.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Fix it: <em>While I was walking in the park when I was meeting Afsona.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>While I was walking in the park, I met Afsona.</strong></p>
      <p>Use only one joining word, and the short action (<em>met</em>) takes the Past
         Simple.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one sentence about something that interrupted you yesterday.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I <b>was doing</b> my homework when my little brother
         <b>turned</b> on the TV.</em></p>
      <p>Check: long action in the Continuous, short action in the Simple, <em>when</em>
         before the short one.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>To interrupt</b><span>boʻlmoq</span></li>
  <li><b>Interruption</b><span>xalaqit</span></li>
  <li><b>Background action</b><span>fondagi harakat</span></li>
  <li><b>Sequence</b><span>ketma-ketlik</span></li>
  <li><b>At the same time</b><span>bir vaqtda</span></li>
  <li><b>While</b><span>...ayotganda</span></li>
  <li><b>To go out (lights)</b><span>oʻchmoq</span></li>
  <li><b>Accident</b><span>baxtsiz hodisa</span></li>
  <li><b>To cross</b><span>kesib oʻtmoq</span></li>
  <li><b>Comma</b><span>vergul</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Long action → Past Continuous · short action → Past Simple.</b></li>
    <li><b>while</b> + the long one · <b>when</b> + the short one.</li>
    <li>Simple + Simple = a <b>sequence</b>; Continuous + Continuous = <b>at the same
        time</b>.</li>
    <li>Comma only when the sentence starts with <em>when</em> or <em>while</em>.</li>
    <li>Don't tell a whole story in the Continuous — finished events need the Simple.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-25: used to and would: Past Habits",
        "category": "english",
        "order": 25,
        "summary": (
            "How to say what was true then but is not true now — the structure that turns any "
            "sentence into a memory, and the trap of 'be used to'."
        ),
        "content": """
<h2>PE-25: used to and would: Past Habits</h2>

<p><em>I <b>used to</b> be afraid of dogs.</em> Three little words, and your listener
immediately knows two things: it was true in the past, and it is <b>not true any more</b>.
That double meaning is why <b>used to</b> is one of the most useful structures in English for
talking about your childhood, your old school, your old self.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>used to + base verb</b> for past habits and past states</li>
    <li>The negative and question forms — and the missing <b>d</b></li>
    <li>When <b>would</b> can replace <em>used to</em>, and when it cannot</li>
    <li>The dangerous look-alike: <b>be used to</b> = "be accustomed to"</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Past habit or state — not true now</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">used to</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
</div>

LEGEND_HERE

<h3>1. What it really means</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:78%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:12%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:26%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:40%"></span>
    <span class="pe-tl-tag" style="left:26%">I used to play chess</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>Repeated dots in the past — and then nothing. The habit stopped. That gap between the last
dot and NOW is the whole meaning of <b>used to</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Sherbek</span>
     <span class="pe-hl pe-hl--aux">used to</span>
     <span class="pe-hl pe-hl--v">play</span> chess every day, but now he plays football.</p>
  <p class="pe-ex__uz">Sherbek har kuni shaxmat oʻynardi, ammo hozir futbol oʻynaydi.</p>
</div>

<p>It works for <b>habits</b> (repeated actions) and equally for <b>states</b> (long
situations):</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Habits — repeated actions</p>
    <ul>
      <li>We <b>used to walk</b> to school.</li>
      <li>She <b>used to call</b> me every night.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">States — long situations</p>
    <ul>
      <li>I <b>used to have</b> long hair.</li>
      <li>There <b>used to be</b> a cinema here.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Used to</b> oʻzbekchadagi <b>-ardim / -rdim</b> shakliga toʻgʻri keladi:
  <em>bor<b>ardim</b></em> = <em>I <b>used to go</b></em>, <em>oʻyna<b>rdim</b></em> =
  <em>I <b>used to play</b></em>. Va eng muhim maʼno ikkalasida ham bir xil: <b>oʻsha
  paytda shunday edi, hozir esa yoʻq</b>.
</div>

<h3>2. Negatives and questions — mind the missing "d"</h3>

<p>Here is a small spelling detail that catches almost everybody. In negatives and questions,
the helper <b>did</b> appears — and, following the golden rule you know from PE-22, the verb
goes back to its base form. <em>Used</em> loses its <b>-d</b> and becomes <b>use</b>.</p>

<ol class="pe-steps">
  <li><b>Positive:</b> <em>I <b>used to</b> smoke.</em></li>
  <li><b>Negative:</b> <em>I <b>didn't use to</b> smoke.</em> — not <s>didn't used to</s></li>
  <li><b>Question:</b> <em><b>Did</b> you <b>use to</b> smoke?</em> — not <s>Did you used
      to</s></li>
  <li><b>Short answer:</b> <em>Yes, I did. / No, I didn't.</em></li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In speech <em>used to</em> and <em>use to</em> sound exactly the same ("yoost-to"), so your
  ear will not help you here — only the rule will. If <b>did</b> is in the sentence, write
  <b>use</b>.
</div>

<h3>3. would — the same, but only for actions</h3>

<p>In stories and memories you will often meet <b>would</b> doing a similar job. It works for
repeated <b>actions</b>, but it cannot describe <b>states</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Every summer we <b>would go</b> to my grandmother's village. She
     <b>would make</b> fresh bread every morning.</p>
  <p class="pe-ex__uz">Har yozda buvimning qishlogʻiga borardik. U har tongda yangi non
     yopardi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>I would have a bike when I was ten.</s></p>
  <p class="pe-good">I <b>used to have</b> a bike when I was ten. <em>(having = a state)</em></p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>didn't use to</b> like reading, but now I read every day.</p>
  <p class="pe-ex__uz">Men oldin oʻqishni yoqtirmasdim, hozir esa har kuni oʻqiyman.</p>
  <p class="pe-ex__why">Negative form: <em>use</em> without the <b>d</b>, because
     <em>didn't</em> is already there.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu yerda oʻzbek tili sizni chalgʻitishi mumkin: oʻzbekchada <b>-ardim</b> ham
  harakat uchun ("bor<b>ardim</b>"), ham holat uchun ("bil<b>ardim</b>") ishlatiladi.
  Ingliz tilida esa <b>would</b> faqat <b>harakat</b> uchun: <em>we <b>would go</b></em> ✓,
  lekin <s>I would know</s> ✗. Holat uchun doim <b>used to</b>: <em>I <b>used to
  know</b></em>.
</div>

<p>A practical rule: <b>used to</b> always works. <b>Would</b> only works if you could put
"again and again" in front of the verb. When you are unsure, choose <em>used to</em>.</p>

<h3>4. The dangerous look-alike: be used to</h3>

<p>This is a different structure with a different meaning, and mixing them up changes your
sentence completely.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">used to + base verb</p>
    <p><em>I <b>used to live</b> in a village.</em></p>
    <p>= I lived there before, not now.<br>(oldin yashardim)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">be used to + noun / -ing</p>
    <p><em>I <b>am used to living</b> in a village.</em></p>
    <p>= It is normal for me now.<br>(odatlanib qolganman)</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkalasini farqlang: <b>used to</b> — "oldin shunday <b>qilardim</b>" (hozir yoʻq).
  <b>be used to</b> — "men bunga <b>oʻrganib qolganman</b>" (hozir ham shunday). Farqni
  koʻrsatuvchi belgi: <em>am/is/are</em> boʻlsa — ikkinchisi, va undan keyin feʼl
  <b>-ing</b> bilan keladi: <em>I <b>am used to getting</b> up early.</em>
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I used to went to that school.</s></p>
  <p class="pe-good">I <b>used to go</b> to that school.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She didn't used to like tea.</s></p>
  <p class="pe-good">She <b>didn't use to</b> like tea.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did you used to live in Nukus?</s></p>
  <p class="pe-good"><b>Did you use to</b> live in Nukus?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I use to play football when I was a child.</s></p>
  <p class="pe-good">I <b>used to</b> play football when I was a child. <em>(positive → with d)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I am used to go to bed late.</s></p>
  <p class="pe-good">I <b>am used to going</b> to bed late. <em>(be used to + -ing)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Rewrite with <em>used to</em>: <em>When I was small, I was afraid of the dark. Now I am
     not.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I used to be afraid of the dark.</strong></p>
      <p>One sentence now carries both ideas — it was true then, and it is not true now.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it negative and a question: <em>Afsona used to wear glasses.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona didn't use to wear glasses. / Did Afsona use to wear
         glasses?</strong></p>
      <p>The <b>d</b> disappears whenever <em>did</em> is present.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Can you use <em>would</em> here? <em>There used to be a big tree in our yard.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>No.</strong> "There being a tree" is a <b>state</b>, not a repeated action.
         <s>There would be a big tree</s> means something else entirely.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What is the difference? <em>(a) I used to work at night. (b) I am used to working at
     night.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I worked at night before, but not now.</strong>
         <strong>(b) I still work at night and it feels normal to me.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write two true sentences about your childhood with <em>used to</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I <b>used to be</b> very shy at school, and my family
         <b>used to live</b> in a small house near the river.</em></p>
      <p>Both are states — which is why <em>would</em> would not work in either.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Used to</b><span>...ardim (oldin)</span></li>
  <li><b>Be used to</b><span>oʻrganib qolgan</span></li>
  <li><b>Past habit</b><span>oʻtmishdagi odat</span></li>
  <li><b>State</b><span>holat</span></li>
  <li><b>No longer</b><span>endi emas</span></li>
  <li><b>Memory</b><span>xotira</span></li>
  <li><b>Childhood</b><span>bolalik</span></li>
  <li><b>Shy</b><span>uyatchan</span></li>
  <li><b>Afraid of</b><span>...dan qoʻrqadigan</span></li>
  <li><b>To get used to</b><span>koʻnikmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>used to + base verb</b> = true before, <b>not true now</b>. Habits and states both.</li>
    <li>With <b>did</b>, the <b>d</b> disappears: <em>didn't <b>use</b> to</em>,
        <em>Did you <b>use</b> to…?</em></li>
    <li><b>would</b> works only for repeated <b>actions</b>, never for states.</li>
    <li><b>be used to + -ing</b> is a different structure: "I am accustomed to it".</li>
    <li>When in doubt, <b>used to</b> is always safe.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
