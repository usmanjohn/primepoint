# -*- coding: utf-8 -*-
"""Prime English — Block G, lessons 86–90 (advanced style and vocabulary building).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_86_90.py --author=prime
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
        "title": "PE-86: Participle Clauses",
        "category": "english",
        "order": 86,
        "summary": (
            "How to join two sentences without a conjunction — the -ing and -ed openers that "
            "make written English shorter and more elegant."
        ),
        "content": """
<h2>PE-86: Participle Clauses</h2>

<p>Compare these two: <em>"Because I was tired, I went to bed early."</em> and
<em>"<b>Being tired</b>, I went to bed early."</em> The second is shorter, smoother, and sounds
like a book. That is a <mark>participle clause</mark> — a way of joining ideas without any
conjunction at all. It is one of the fastest ways to make your writing look advanced.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>-ing</b> clauses for active meaning</li>
    <li><b>-ed</b> clauses for passive meaning</li>
    <li><b>Having + V3</b> for something that happened earlier</li>
    <li>The one rule that stops the classic "dangling" mistake</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two types</span>
  <span class="pe-chip pe-chip--v">-ing</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">active</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">-ed / V3</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">passive</span>
</div>

LEGEND_HERE

<h3>1. The -ing clause: active</h3>

<p>Use it when the subject of both halves is the <b>same person</b> and that person is
<b>doing</b> something. Drop the conjunction and the subject, and turn the verb into
<b>-ing</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><em>While I was walking home, I met my teacher.</em> →
     <span class="pe-hl pe-hl--v">Walking home</span>, I met my teacher.</p>
  <p class="pe-ex__uz">Uyga ketayotib, oʻqituvchimni uchratdim.</p>
  <p class="pe-ex__why">Both halves are about <em>I</em>, so the subject appears only once.</p>
</div>

<p>It can carry several different meanings, and the reader works them out from the context:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>At the same time</p>
    <p><em><b>Sitting</b> in the garden, she read a book.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Reason (= because)</p>
    <p><em><b>Being</b> ill, he stayed at home.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Result</p>
    <p><em>He fell, <b>breaking</b> his arm.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>After a preposition</p>
    <p><em><b>After finishing</b>, we went out.</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxshi xabar: oʻzbek tilida bu qurilma juda tanish! <b>-b / -ib / -ayotib</b>
  qoʻshimchalari aynan shu vazifani bajaradi: <em>Uyga ketayot<b>ib</b>, oʻqituvchimni
  uchratdim</em> → <em><b>Walking</b> home, I met my teacher</em>. Yaʼni oʻzbekchada
  ravishdosh boʻlgan joyda ingliz tilida <b>-ing</b> shakli keladi.
</div>

<h3>2. The -ed clause: passive</h3>

<p>When the subject <b>receives</b> the action, use the V3 (past participle) instead.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><em>The house, which was built in 1890, is still beautiful.</em> →
     The house, <b>built in 1890</b>, is still beautiful.</p>
  <p class="pe-ex__uz">1890-yilda qurilgan uy hamon chiroyli.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Written</b> in simple English, the book is easy to read. —
     <b>Surprised</b> by the news, she said nothing.</p>
  <p class="pe-ex__uz">Sodda ingliz tilida yozilgani uchun kitobni oʻqish oson. — Yangilikdan
     hayron boʻlib, u hech narsa demadi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">-ing → the subject does it</p>
    <ul>
      <li><em><b>Opening</b> the door, he went in.</em></li>
      <li><em><b>Feeling</b> tired, I sat down.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">-ed → the subject receives it</p>
    <ul>
      <li><em><b>Opened</b> in 1990, the shop closed last year.</em></li>
      <li><em><b>Invited</b> to the party, I bought a present.</em></li>
    </ul>
  </div>
</div>

<h3>3. Having + V3 — something earlier</h3>

<p>To show that one action finished <b>before</b> the other, use <b>having + V3</b>. It replaces
the Past Perfect (PE-38) in this compact style.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><em>After I had finished my homework, I watched TV.</em> →
     <b>Having finished</b> my homework, I watched TV.</p>
  <p class="pe-ex__uz">Uy vazifamni tugatgach, televizor koʻrdim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Having lived</b> in Nukus for ten years, Afsona knows the city well.</p>
  <p class="pe-ex__uz">Nukusda oʻn yil yashagani uchun Afsona shaharni yaxshi biladi.</p>
</div>

<h3>4. The one rule: same subject</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  The participle must belong to the <b>subject of the main clause</b>. If it doesn't, you create
  a "dangling participle" — and the sentence says something absurd.
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Walking down the street, the shop was closed.</s> <em>(the shop was
     walking?)</em></p>
  <p class="pe-good"><b>Walking</b> down the street, <b>I saw</b> that the shop was closed.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Being very old, I helped my grandmother up the stairs.</s></p>
  <p class="pe-good"><b>Because she was</b> very old, I helped my grandmother up the stairs.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tekshiruv juda oddiy: ravishdosh qismini oʻqib, <b>"buni kim qilyapti?"</b> deb soʻrang.
  Javob asosiy gapning <b>egasi</b> boʻlishi kerak. <em>"Walking down the street, the shop
  was closed"</em> — koʻcha boʻylab doʻkon ketyaptimi? Yoʻq. Demak gap notoʻgʻri. Bu xato
  oʻzbekchada ham xuddi shunday kulgili chiqadi.
</div>

<h3>5. Where to use it</h3>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Participle clauses belong to <b>writing</b>, not chatting. Use one or two in an essay or a
  story to vary your sentence length — a page of them becomes hard to read. In speech, the
  ordinary version with <em>because</em> or <em>when</em> is far more natural.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Story style: <em><b>Hearing</b> a noise outside, Sherbek opened the
     window. <b>Seeing</b> nothing, he went back to bed.</em></p>
  <p class="pe-ex__uz">Tashqaridan shovqin eshitib, Sherbek derazani ochdi. Hech narsa
     koʻrmagach, yana yotib uxladi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uslub eslatmasi: ravishdosh oborotlar <b>yozma nutq</b> uchun. Insho va hikoyada
  jumlalarni xilma-xil qiladi, ammo suhbatda <em>because</em>, <em>when</em> bilan
  aytish tabiiyroq. Bir xatboshida bittasi yetarli — koʻp boʻlsa, oʻqish qiyinlashadi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Being tired, my mother made me tea.</s></p>
  <p class="pe-good"><b>Because I was</b> tired, my mother made me tea.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Build in 1890, the house is old.</s></p>
  <p class="pe-good"><b>Built</b> in 1890, the house is old.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Having finish my work, I went out.</s></p>
  <p class="pe-good"><b>Having finished</b> my work, I went out.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>While walking home, it started to rain on me.</s></p>
  <p class="pe-good"><b>While I was walking</b> home, it started to rain.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Invited to the party, my new shoes were dirty.</s></p>
  <p class="pe-good"><b>Invited</b> to the party, <b>I</b> cleaned my new shoes.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Shorten it: <em>While she was waiting for the bus, she read the news.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Waiting for the bus, she read the news.</strong></p>
      <p>Same subject in both halves, so the <b>-ing</b> clause works.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     -ing or -ed: <em>___ in Bukhara, the carpet is very valuable.</em> (make)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Made in Bukhara</strong> — the carpet <em>receives</em> the action, so the
         passive form (V3) is needed.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Use <em>having</em>: <em>After I had eaten breakfast, I left the house.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Having eaten breakfast, I left the house.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What is absurd here? <em>Running to school, my bag fell open.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The bag appears to be running.</strong> Fix it: <em>While I was running to
         school, my bag fell open.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Combine into one sentence: <em>Jasur heard the alarm. He jumped out of bed.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Hearing the alarm, Jasur jumped out of bed.</strong></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Participle clause</b><span>ravishdosh oborot</span></li>
  <li><b>Participle</b><span>sifatdosh / ravishdosh</span></li>
  <li><b>Dangling participle</b><span>egasiz ravishdosh</span></li>
  <li><b>Elegant</b><span>nafis, chiroyli</span></li>
  <li><b>Compact</b><span>ixcham</span></li>
  <li><b>Valuable</b><span>qimmatli</span></li>
  <li><b>Alarm (clock)</b><span>budilnik</span></li>
  <li><b>Absurd</b><span>bemaʼni</span></li>
  <li><b>To vary</b><span>xilma-xil qilmoq</span></li>
  <li><b>Stairs</b><span>zinapoya</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>-ing</b> clause = the subject <b>does</b> it · <b>-ed / V3</b> clause = the subject
        <b>receives</b> it.</li>
    <li><b>Having + V3</b> = it happened earlier.</li>
    <li>The participle must belong to the <b>subject of the main clause</b>.</li>
    <li>Uzbek <b>-ib / -ayotib</b> is your equivalent.</li>
    <li>Use them in <b>writing</b>, one or two at a time — not in conversation.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-87: The Unreal Past: It's time, would rather, as if",
        "category": "english",
        "order": 87,
        "summary": (
            "More places where English uses a past tense for something that isn't past — it's "
            "time you went, I'd rather you stayed, he acts as if he knew."
        ),
        "content": """
<h2>PE-87: The Unreal Past: It's time, would rather, as if</h2>

<p>You met the idea in PE-54 and PE-57: English signals <b>unreality</b> by stepping one tense
backwards. <em>If I <b>had</b> a car…</em> · <em>I wish I <b>knew</b>…</em> Now meet three more
structures that do exactly the same thing — and once you notice the pattern, all of them stop
feeling strange.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>It's time</b> + past tense</li>
    <li><b>would rather</b> — two different structures</li>
    <li><b>as if / as though</b> for unreal comparisons</li>
    <li>Why they all use a past form for a present idea</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The pattern behind all three</span>
  <span class="pe-chip pe-chip--s">not real / not yet</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">step one tense back</span>
</div>

LEGEND_HERE

<h3>1. It's time…</h3>

<p>Two forms, two shades of meaning. With <b>to + verb</b> it is neutral; with a <b>past
tense</b> it adds a note of criticism — "this should have happened already".</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">It's time to… — neutral</p>
    <ul>
      <li><em>It's time <b>to go</b>.</em></li>
      <li><em>It's time <b>for us to leave</b>.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">It's time + past — slight criticism</p>
    <ul>
      <li><em>It's time you <b>went</b> home.</em></li>
      <li><em>It's <b>high</b> time she <b>found</b> a job.</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">It's time you <span class="pe-hl pe-hl--v">started</span> revising —
     the exam is next week!</p>
  <p class="pe-ex__uz">Takrorlashni boshlashing kerak edi — imtihon kelasi haftada!</p>
  <p class="pe-ex__why">The verb is past, but the meaning is <b>now</b>: you have not started
     yet, and you should have.</p>
</div>

<p><b>It's high time</b> makes the criticism stronger still.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>It's time you went</b> oʻzbekchadagi "<b>Endi ketsang boʻladi</b>" yoki
  "<b>Ketishing kerak edi</b>" ohangiga toʻgʻri keladi — yaʼni ozgina taʼna bor.
  <em>It's time to go</em> esa shunchaki "Ketish vaqti boʻldi" — betaraf. Feʼl oʻtgan
  zamonda boʻlsa ham, gap <b>hozir</b> haqida.
</div>

<h3>2. would rather — two structures</h3>

<p>The trap here is that <b>would rather</b> behaves differently depending on <b>who</b> does the
action.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Who acts</th><th>Structure</th><th>Example</th></tr>
  <tr>
    <td><b>I</b> do it</td><td>would rather + <b>base verb</b></td>
    <td>I<b>'d rather stay</b> at home.</td>
  </tr>
  <tr>
    <td><b>Somebody else</b> does it</td><td>would rather + <b>past tense</b></td>
    <td>I<b>'d rather you stayed</b> at home.</td>
  </tr>
  <tr>
    <td>Negative (me)</td><td>would rather <b>not</b> + verb</td>
    <td>I<b>'d rather not</b> talk about it.</td>
  </tr>
  <tr>
    <td>Negative (them)</td><td>would rather + <b>didn't</b></td>
    <td>I<b>'d rather you didn't</b> smoke.</td>
  </tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'d rather walk</b> than take a taxi. — I<b>'d rather you didn't</b>
     tell anybody.</p>
  <p class="pe-ex__uz">Taksi olgandan koʻra piyoda ketganim maʼqul. — Hech kimga aytmaganingizni
     xohlardim.</p>
  <p class="pe-ex__why">Note <b>than</b> for the comparison, and no <em>to</em> after
     <em>rather</em>.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <em>"I'd rather you didn't"</em> is one of the most polite ways in English to refuse
  something. It is far gentler than <em>"Don't do that"</em> — remember it as a whole phrase.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat qiling: <b>would rather</b> dan keyin <b>to</b> qoʻyilmaydi
  (<em>I'd rather <b>stay</b></em>, <s>I'd rather to stay</s>), va taqqoslashda
  <b>than</b> ishlatiladi (<em>rather walk <b>than</b> take a taxi</em>), <em>that</em>
  emas. Oʻzbekchada "...gandan koʻra ...ganim maʼqul" — "koʻra" soʻzi <em>than</em> ga
  toʻgʻri keladi.
</div>

<h3>3. as if / as though</h3>

<p>Use these to compare with something imaginary. If the comparison is <b>unreal</b>, the verb
steps back into the past.</p>

<div class="pe-ex">
  <p class="pe-ex__en">He talks <b>as if he knew</b> everything. <em>(he doesn't)</em> —
     She looks <b>as though she had seen</b> a ghost. <em>(she hasn't)</em></p>
  <p class="pe-ex__uz">U hammasini bilgandek gapiradi. — U arvoh koʻrgandek qarayapti.</p>
</div>

<p>But if the comparison might be <b>true</b>, an ordinary present tense is used:</p>

<div class="pe-ex">
  <p class="pe-ex__en">It looks <b>as if it's going</b> to rain. <em>(it probably is)</em></p>
  <p class="pe-ex__uz">Yomgʻir yogʻadiganga oʻxshaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>as if / as though</b> oʻzbekchadagi "<b>-gandek</b>", "<b>goʻyo</b>" shakllariga
  toʻgʻri keladi: <em>bilgan<b>dek</b> gapiradi</em> → <em>talks <b>as if he knew</b></em>.
  Eʼtibor bering: haqiqat boʻlmasa — oʻtgan zamon (<em>knew</em>), haqiqat boʻlishi mumkin
  boʻlsa — hozirgi zamon (<em>it's going to rain</em>).
</div>

<h3>4. The pattern in one place</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Second conditional</p>
    <p><em>If I <b>had</b> money…</em> (PE-54)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>wish / if only</p>
    <p><em>I wish I <b>knew</b>.</em> (PE-57)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>It's time</p>
    <p><em>It's time you <b>left</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>would rather / as if</p>
    <p><em>I'd rather you <b>stayed</b>. He acts as if he <b>owned</b> it.</em></p>
  </div>
</div>

<p>Four structures, one idea: <b>a past form marks something that is not real</b>.</p>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>It's time you go home.</s></p>
  <p class="pe-good">It's time you <b>went</b> home. / It's time <b>to go</b> home.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'd rather to stay here.</s></p>
  <p class="pe-good">I'd rather <b>stay</b> here.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'd rather you don't come late.</s></p>
  <p class="pe-good">I'd rather you <b>didn't</b> come late.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'd rather walk that take the bus.</s></p>
  <p class="pe-good">I'd rather walk <b>than</b> take the bus.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He speaks as if he is a professor.</s> <em>(he isn't)</em></p>
  <p class="pe-good">He speaks as if he <b>were</b> a professor.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>It's time you <span class="pe-blank">?</span> (start) doing your
     homework.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>started</strong> — past form for a present situation, with a note of "you
         should have already".</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>I'd rather <span class="pe-blank">?</span> (not go) out tonight.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>not go</strong> — when <em>I</em> am the one acting, the base verb follows,
         and <em>not</em> comes before it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Refuse politely: <em>Your friend wants to borrow your new phone.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'd rather you didn't, if you don't mind.</strong></p>
      <p>Far gentler than <em>No</em> or <em>Don't</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Choose: <em>He behaves as if he <span class="pe-blank">?</span> (be) the boss.</em>
     (he isn't)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>were</strong> — the comparison is unreal, so the verb steps back, and
         <em>were</em> is used for all persons.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What is the difference? <em>(a) It's time to leave. (b) It's time you left.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) Neutral</strong> — we should all go now. <strong>(b) Slight
         criticism</strong> — you have stayed too long already.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Unreal past</b><span>shartli oʻtgan zamon</span></li>
  <li><b>It's high time</b><span>allaqachon vaqti boʻldi</span></li>
  <li><b>Would rather</b><span>...ganim maʼqul</span></li>
  <li><b>As if / as though</b><span>...gandek, goʻyo</span></li>
  <li><b>To behave</b><span>oʻzini tutmoq</span></li>
  <li><b>Criticism</b><span>taʼna, tanqid</span></li>
  <li><b>Neutral</b><span>betaraf</span></li>
  <li><b>To refuse politely</b><span>muloyim rad etmoq</span></li>
  <li><b>To revise</b><span>takrorlamoq</span></li>
  <li><b>Preference</b><span>afzallik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>It's time + past</b> = it should have happened already (a little criticism).</li>
    <li><b>would rather + base verb</b> (me) · <b>would rather + past</b> (somebody else).</li>
    <li><b>I'd rather you didn't</b> — the politest refusal in English.</li>
    <li><b>as if + past</b> = not true · <b>as if + present</b> = probably true.</li>
    <li>One idea behind all of them: a <b>past form marks unreality</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-88: Linking Words for Writing: however, therefore, although",
        "category": "english",
        "order": 88,
        "summary": (
            "The words that hold an essay together — how to add, contrast, explain and conclude, "
            "and the punctuation each one needs."
        ),
        "content": """
<h2>PE-88: Linking Words for Writing: however, therefore, although</h2>

<p>Two essays can contain the same ideas and receive very different marks. The difference is
usually <mark>linking words</mark> — the signposts that tell your reader where the argument is
going. <em>However</em>, <em>therefore</em>, <em>in addition</em>, <em>for example</em>. They cost
nothing to learn and they lift a piece of writing immediately.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The five families: adding, contrasting, explaining, giving examples, concluding</li>
    <li>The punctuation each type needs</li>
    <li><b>although</b> vs <b>however</b> vs <b>despite</b> — the grammar differs</li>
    <li>How many to use, and where</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Five jobs</span>
  <span class="pe-chip pe-chip--s">add</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">contrast</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">explain</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">exemplify</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">conclude</span>
</div>

LEGEND_HERE

<h3>1. The five families</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Job</th><th>Linking words</th></tr>
  <tr><td><b>Adding</b></td><td>In addition, Moreover, Furthermore, Also, What is more</td></tr>
  <tr><td><b>Contrasting</b></td><td>However, Nevertheless, On the other hand, In contrast</td></tr>
  <tr><td><b>Explaining / result</b></td><td>Therefore, As a result, Consequently, For this reason</td></tr>
  <tr><td><b>Examples</b></td><td>For example, For instance, such as, In particular</td></tr>
  <tr><td><b>Concluding</b></td><td>In conclusion, To sum up, Overall, All in all</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Learning English opens many doors. <b>In addition</b>, it improves your
     memory. <b>However</b>, it takes time. <b>Therefore</b>, you need patience.
     <b>In conclusion</b>, the effort is worth it.</p>
  <p class="pe-ex__uz">Ingliz tilini oʻrganish koʻp imkoniyat beradi. Bundan tashqari, u
     xotirani yaxshilaydi. Biroq, bu vaqt talab qiladi. Shuning uchun sabr kerak. Xulosa
     qilib aytganda, mehnat oʻzini oqlaydi.</p>
  <p class="pe-ex__why">Five sentences, five signposts — the reader always knows where they
     are.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu soʻzlarning oʻzbekcha muqobillarini bilib qoʻying, keyin ularni ishlatish oson boʻladi:
  <em>However</em> = "biroq", <em>Therefore</em> = "shuning uchun", <em>In addition</em> =
  "bundan tashqari", <em>For example</em> = "masalan", <em>In conclusion</em> = "xulosa
  qilib aytganda". Inshoda har bir xatboshini shulardan biri bilan boshlash — eng oson
  ball toʻplash usuli.
</div>

<h3>2. The punctuation</h3>

<ol class="pe-steps">
  <li><b>At the start of a sentence → comma after it:</b>
      <em><b>However,</b> the plan failed.</em></li>
  <li><b>In the middle → commas around it:</b>
      <em>The plan<b>, however,</b> failed.</em></li>
  <li><b>Never join two sentences with just a comma</b> before them (PE-81):
      <s>It rained, however we went.</s> ✗ → <em>It rained. <b>However,</b> we went.</em></li>
  <li><b>Semicolon is possible:</b> <em>It rained<b>; however,</b> we went.</em></li>
</ol>

<h3>3. although vs however vs despite</h3>

<p>All three mean "contrast", but they take <b>different grammar</b> — and this is what exams
test.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Word</th><th>What follows</th><th>Example</th></tr>
  <tr>
    <td><b>although / though</b></td><td>a full clause (subject + verb)</td>
    <td><b>Although it rained</b>, we went out.</td>
  </tr>
  <tr>
    <td><b>however</b></td><td>a new sentence</td>
    <td>It rained. <b>However,</b> we went out.</td>
  </tr>
  <tr>
    <td><b>despite / in spite of</b></td><td>a noun or <b>-ing</b></td>
    <td><b>Despite the rain</b>, we went out.</td>
  </tr>
  <tr>
    <td><b>but</b></td><td>joins two clauses</td>
    <td>It rained, <b>but</b> we went out.</td>
  </tr>
</table>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Despite it rained, we went out.</s></p>
  <p class="pe-good"><b>Despite the rain</b>, we went out. / <b>Although it rained</b>, we went
     out.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni yodda tuting: <b>although</b> dan keyin <b>toʻliq gap</b> keladi
  (<em>although it <b>rained</b></em>), <b>despite / in spite of</b> dan keyin esa faqat
  <b>ot yoki -ing</b> (<em>despite <b>the rain</b></em>, <em>despite <b>raining</b></em>).
  Oʻzbekchada ikkalasi ham "garchi / qaramay" boʻlgani uchun aralashtirish oson —
  shuning uchun <b>keyingi soʻzga</b> qarab tanlang.
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Although</b> the city is crowded, I love it. — The city is crowded.
     <b>However,</b> I love it. — <b>Despite</b> the crowds, I love it.</p>
  <p class="pe-ex__uz">Shahar gavjum boʻlsa ham, men uni yaxshi koʻraman.</p>
  <p class="pe-ex__why">One idea, three structures — and each one needs a different thing after
     it.</p>
</div>

<h3>4. Don't overload</h3>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Aim for <b>one linking word per paragraph</b>, not one per sentence. Examiners notice
  overuse: a paragraph with <em>Moreover… Furthermore… In addition…</em> in three consecutive
  sentences looks memorised rather than thought through. Quality beats quantity here.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Weak: <em>Firstly, I like it. Moreover, it is cheap. Furthermore, it is
     fast. In addition, it is safe.</em><br>
     Better: <em>I like it because it is cheap and fast. <b>Moreover</b>, it is completely
     safe.</em></p>
  <p class="pe-ex__uz">Bu menga yoqadi, chunki arzon va tez. Bundan tashqari, u butunlay
     xavfsiz.</p>
</div>

<h3>5. A few more worth knowing</h3>

<ul>
  <li><b>Firstly, Secondly, Finally</b> — for ordering points</li>
  <li><b>In fact, Actually</b> — for correcting or strengthening</li>
  <li><b>On the whole, Generally speaking</b> — for careful generalisations</li>
  <li><b>That is to say, In other words</b> — for rephrasing</li>
</ul>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Insho tuzilishi uchun eng foydali toʻplam: <b>Firstly / Secondly / Finally</b>
  (fikrlarni tartibga solish), <b>For example</b> (misol), <b>However</b> (qarama-qarshi
  fikr), <b>In conclusion</b> (xulosa). Shu toʻrttasi bilan har qanday insho aniq
  tuzilishga ega boʻladi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Although it was expensive, but I bought it.</s></p>
  <p class="pe-good"><b>Although</b> it was expensive, I bought it. <em>(PE-52)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>However the weather was bad, we went.</s></p>
  <p class="pe-good"><b>Although</b> the weather was bad, we went.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>In spite of the rain was heavy, we walked.</s></p>
  <p class="pe-good"><b>In spite of the heavy rain</b>, we walked.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Therefore we must act now.</s> <em>(no comma)</em></p>
  <p class="pe-good"><b>Therefore,</b> we must act now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I like tea, however I don't like coffee.</s></p>
  <p class="pe-good">I like tea. <b>However,</b> I don't like coffee.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     although or despite: <em>___ the traffic, we arrived on time. ___ there was heavy
     traffic, we arrived on time.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Despite the traffic … Although there was heavy traffic.</strong></p>
      <p><em>Despite</em> + noun; <em>although</em> + clause.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Punctuate: <em>The test was difficult however I passed it.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The test was difficult. However, I passed it.</strong> (or <em>…difficult;
         however, I passed it.</em>)</p>
      <p><em>However</em> cannot join two sentences with a comma alone.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which linking word? <em>Studying abroad is expensive. ___ , it gives you experience you
     cannot get at home.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>However</strong> (or <em>On the other hand</em>) — the second sentence
         contrasts with the first.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>Although he studied hard, but he failed.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Although he studied hard, he failed.</strong> One contrast marker only —
         the Uzbek <em>garchi…lekin</em> habit again (PE-52).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a two-sentence argument using <em>For example</em> and <em>Therefore</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Reading improves your vocabulary. <b>For example</b>, one
         novel can teach you hundreds of new words. <b>Therefore</b>, students should read
         every day.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Linking word</b><span>bogʻlovchi soʻz</span></li>
  <li><b>However</b><span>biroq</span></li>
  <li><b>Therefore</b><span>shuning uchun</span></li>
  <li><b>Moreover</b><span>bundan tashqari</span></li>
  <li><b>Nevertheless</b><span>shunga qaramay</span></li>
  <li><b>Despite / in spite of</b><span>...ga qaramay</span></li>
  <li><b>For instance</b><span>masalan</span></li>
  <li><b>In conclusion</b><span>xulosa qilib</span></li>
  <li><b>To sum up</b><span>yakunlab aytganda</span></li>
  <li><b>Argument</b><span>dalil, fikr</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Five jobs: <b>add · contrast · explain · exemplify · conclude</b>.</li>
    <li>At the start of a sentence, a linking word takes a <b>comma after</b> it.</li>
    <li><b>although</b> + clause · <b>despite</b> + noun/-ing · <b>however</b> + new
        sentence.</li>
    <li>Never <b>although … but</b> in the same sentence.</li>
    <li>One per paragraph — overuse looks memorised.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-89: Word Formation: Prefixes and Suffixes",
        "category": "english",
        "order": 89,
        "summary": (
            "How one word becomes six — the prefixes that reverse meaning and the suffixes that "
            "change a word's job. The fastest way to grow your vocabulary."
        ),
        "content": """
<h2>PE-89: Word Formation: Prefixes and Suffixes</h2>

<p>Learn the word <em>care</em> and you have learned one word. Learn how English builds on it and
you get six: <em>careful, carefully, careless, carelessly, carelessness, uncaring</em>. This is
<mark>word formation</mark>, and it is by far the fastest way to grow your vocabulary — not by
memorising more words, but by understanding how the ones you know can be reshaped.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The <b>prefixes</b> that reverse or change meaning</li>
    <li>The <b>suffixes</b> that turn a word into a noun, adjective, verb or adverb</li>
    <li>How to build a whole word family from one root</li>
    <li>Why this is the best trick for exams</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two directions</span>
  <span class="pe-chip pe-chip--neg">prefix</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--opt">changes the meaning</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">suffix</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--opt">changes the word's job</span>
</div>

LEGEND_HERE

<h3>1. Prefixes that mean "not"</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Prefix</th><th>Used before</th><th>Examples</th></tr>
  <tr><td><b>un-</b></td><td>the commonest one</td><td>unhappy, unfair, unusual, unable</td></tr>
  <tr><td><b>in-</b></td><td>many Latin words</td><td>incorrect, invisible, informal</td></tr>
  <tr><td><b>im-</b></td><td>before m and p</td><td>impossible, impatient, impolite</td></tr>
  <tr><td><b>ir-</b></td><td>before r</td><td>irregular, irresponsible</td></tr>
  <tr><td><b>il-</b></td><td>before l</td><td>illegal, illogical</td></tr>
  <tr><td><b>dis-</b></td><td>reversing an action</td><td>disagree, dishonest, disappear</td></tr>
  <tr><td><b>non-</b></td><td>neutral "not"</td><td>non-stop, non-smoking</td></tr>
</table>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  There is a sound pattern in <b>im- / ir- / il-</b>: the prefix copies the first letter of the
  word. <em>im</em>possible (p), <em>ir</em>regular (r), <em>il</em>legal (l). Your mouth finds
  it easier — and so does your memory.
</div>

<h3>2. Other useful prefixes</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>re- = again</p>
    <p><em>rewrite, rebuild, return, repeat</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>mis- = wrongly</p>
    <p><em>misunderstand, misspell, mistake</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>over- / under-</p>
    <p><em>overcook, oversleep · underpaid, underestimate</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>pre- / post-</p>
    <p><em>preview, prepare · postpone, postgraduate</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>misunderstood</b> the question, so I had to <b>rewrite</b> my answer.
     It was <b>impossible</b> to finish, and I felt <b>unhappy</b>.</p>
  <p class="pe-ex__uz">Savolni notoʻgʻri tushundim, shuning uchun javobimni qaytadan yozishga
     toʻgʻri keldi. Tugatish imkonsiz edi va oʻzimni yomon his qildim.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida ham shunga oʻxshash qoʻshimchalar bor: <b>be-</b> (bemaʼni, betartib),
  <b>no-</b> (nomaʼlum, notoʻgʻri), <b>-siz</b> (aqlsiz, foydasiz). Yaʼni "inkor
  qoʻshimchasi" tushunchasi sizga tanish. Farqi: ingliz tilida <b>qaysi prefiks</b> mos
  kelishini soʻzning oʻzi belgilaydi — shuning uchun soʻzni <b>prefiksi bilan birga</b>
  yodlash kerak.
</div>

<h3>3. Suffixes change the word's job</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>To make a…</th><th>Suffixes</th><th>Examples</th></tr>
  <tr><td><b>noun</b> (thing/idea)</td><td>-ment, -tion, -ness, -ity, -ance</td><td>development, education, happiness, ability</td></tr>
  <tr><td><b>noun</b> (person)</td><td>-er, -or, -ist, -ian</td><td>teacher, actor, scientist, musician</td></tr>
  <tr><td><b>adjective</b></td><td>-ful, -less, -able, -ive, -ous, -al</td><td>useful, useless, comfortable, creative</td></tr>
  <tr><td><b>verb</b></td><td>-ise / -ize, -en, -ify</td><td>modernise, widen, simplify</td></tr>
  <tr><td><b>adverb</b></td><td>-ly</td><td>quickly, carefully, happily</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">She is a <b>scientist</b>. Her <b>scientific</b> work is very
     <b>creative</b>, and she works <b>carefully</b>.</p>
  <p class="pe-ex__uz">U olim. Uning ilmiy ishi juda ijodiy va u sinchkovlik bilan ishlaydi.</p>
</div>

<h3>4. Building a whole family</h3>

<p>Take one root and walk around it. This is the single best exercise for vocabulary growth.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Verb</th><th>Noun (thing)</th><th>Noun (person)</th><th>Adjective</th><th>Adverb</th></tr>
  <tr><td>to educate</td><td>education</td><td>educator</td><td>educational</td><td>educationally</td></tr>
  <tr><td>to succeed</td><td>success</td><td>—</td><td>successful</td><td>successfully</td></tr>
  <tr><td>to decide</td><td>decision</td><td>—</td><td>decisive</td><td>decisively</td></tr>
  <tr><td>to care</td><td>care</td><td>carer</td><td>careful / careless</td><td>carefully</td></tr>
  <tr><td>to differ</td><td>difference</td><td>—</td><td>different</td><td>differently</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Imtihonlarda (IELTS, milliy sertifikat) <b>soʻz yasash</b> topshiriqlari doim boʻladi:
  qavs ichida <em>success</em> beriladi, siz <em>successful</em> yoki <em>successfully</em>
  yozishingiz kerak. Yechim: yangi soʻz oʻrganganingizda uni <b>butun oilasi bilan</b>
  daftaringizga yozing — feʼl, ot, sifat, ravish. Bir soʻz oʻrniga toʻrttasini olasiz.
</div>

<h3>5. The -ly trap: adverbs that misbehave</h3>

<p>Most adverbs simply add <b>-ly</b>, but a few important ones do not — and one pair changes
meaning completely.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Adjective</th><th>Adverb</th><th>Note</th></tr>
  <tr><td>good</td><td><b>well</b></td><td>not <s>goodly</s></td></tr>
  <tr><td>fast</td><td><b>fast</b></td><td>no change</td></tr>
  <tr><td>hard</td><td><b>hard</b></td><td>works hard</td></tr>
  <tr><td>—</td><td><b>hardly</b></td><td>= almost not!</td></tr>
  <tr><td>late</td><td><b>late</b></td><td>arrived late</td></tr>
  <tr><td>—</td><td><b>lately</b></td><td>= recently</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">He works <b>hard</b>. <em>(a lot of effort)</em> — He <b>hardly</b>
     works. <em>(almost never!)</em></p>
  <p class="pe-ex__uz">U qattiq ishlaydi. — U deyarli ishlamaydi.</p>
  <p class="pe-ex__why">One <b>-ly</b> reverses the whole meaning. Be careful with this pair.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu juftlik juda xavfli: <b>hard</b> = "qattiq, tirishib", <b>hardly</b> = "deyarli
  emas". <em>He works hard</em> — maqtov, <em>He hardly works</em> — tanqid! Xuddi shunday
  <b>late</b> ("kech") va <b>lately</b> ("soʻnggi paytda"). Bir harf butun maʼnoni
  oʻzgartiradi.
</div>

<h3>6. Which form does the sentence need?</h3>

<ol class="pe-steps">
  <li><b>Before a noun</b> → an adjective: <em>a <b>successful</b> student</em>.</li>
  <li><b>After a verb, describing how</b> → an adverb: <em>She sang <b>beautifully</b></em>.</li>
  <li><b>After the / a / an, or as the subject</b> → a noun: <em>The <b>decision</b> was
      hard</em>.</li>
  <li><b>After am/is/are/was</b> → usually an adjective: <em>He is <b>careful</b></em>.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">Her <b>decision</b> was <b>surprising</b>, but she explained it
     <b>clearly</b> and everybody <b>accepted</b> it.</p>
  <p class="pe-ex__uz">Uning qarori hayratlanarli edi, lekin u buni aniq tushuntirdi va hamma
     qabul qildi.</p>
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He is a very success businessman.</s></p>
  <p class="pe-good">He is a very <b>successful</b> businessman.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She speaks English very good.</s></p>
  <p class="pe-good">She speaks English very <b>well</b>. <em>(adverb)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It's unpossible to finish today.</s></p>
  <p class="pe-good">It's <b>impossible</b> to finish today.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The different between them is big.</s></p>
  <p class="pe-good">The <b>difference</b> between them is big.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I disagree with your decide.</s></p>
  <p class="pe-good">I disagree with your <b>decision</b>.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make the opposite: <em>possible · legal · regular · honest · usual</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>impossible · illegal · irregular · dishonest · unusual.</strong></p>
      <p>Notice how the prefix copies the first letter in <em>impossible, illegal,
         irregular</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>She won the competition. It was a great
     <span class="pe-blank">?</span>.</em> (succeed)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>success</strong> — after <em>a great</em> a noun is needed.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Complete: <em>He explained it very <span class="pe-blank">?</span>.</em> (clear)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>clearly</strong> — it describes <em>how</em> he explained, so an adverb is
         needed.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Build the family: <em>care</em> → noun, two adjectives, adverb.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>care · careful / careless · carefully.</strong> Also <em>carer</em>
         (person) and <em>carelessness</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What does each prefix add? <em>rewrite · misspell · oversleep</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>re- = again · mis- = wrongly · over- = too much.</strong> So: write it again,
         spell it wrongly, sleep too long.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Word formation</b><span>soʻz yasalishi</span></li>
  <li><b>Prefix</b><span>oldingi qoʻshimcha</span></li>
  <li><b>Suffix</b><span>keyingi qoʻshimcha</span></li>
  <li><b>Root</b><span>oʻzak</span></li>
  <li><b>Word family</b><span>soʻz oilasi</span></li>
  <li><b>To reverse</b><span>teskari qilmoq</span></li>
  <li><b>To misunderstand</b><span>notoʻgʻri tushunmoq</span></li>
  <li><b>To oversleep</b><span>uxlab qolmoq</span></li>
  <li><b>Successful</b><span>muvaffaqiyatli</span></li>
  <li><b>Decision</b><span>qaror</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Prefixes</b> change meaning: <b>un-, in-, im-, ir-, il-, dis-, re-, mis-,
        over-</b>.</li>
    <li><b>im-/ir-/il-</b> copy the first letter: <em>impossible, irregular, illegal</em>.</li>
    <li><b>Suffixes</b> change the job: <b>-tion/-ment</b> noun · <b>-ful/-less</b> adjective ·
        <b>-ly</b> adverb.</li>
    <li>Learn every new word with its <b>whole family</b>.</li>
    <li>Check the slot: before a noun → adjective; after a verb → adverb.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-90: Collocations: Words That Live Together",
        "category": "english",
        "order": 90,
        "summary": (
            "Why you make a mistake but do your homework — the word partnerships that make the "
            "difference between correct English and natural English."
        ),
        "content": """
<h2>PE-90: Collocations: Words That Live Together</h2>

<p>You can say <em>"I did a mistake"</em> and every listener will understand you. But no English
speaker would ever say it — they say <em>"I <b>made</b> a mistake"</em>. Nothing about the grammar
is wrong; the <mark>partnership</mark> is wrong. These fixed word partnerships are called
<b>collocations</b>, and they are the last big step from correct English to natural English.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What a collocation is and why it matters more than grammar at this level</li>
    <li>The big pair: <b>make</b> or <b>do</b>?</li>
    <li>Collocations with <b>have, take, get, give, pay</b></li>
    <li>Adjective + noun and adverb + adjective partnerships</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Correct vs natural</span>
  <span class="pe-chip pe-chip--neg">do a mistake</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">make a mistake</span>
</div>

LEGEND_HERE

<h3>1. make or do?</h3>

<p>There is a rough logic. <b>Make</b> is for <b>creating</b> something; <b>do</b> is for
<b>activities and work</b>. But the lists are what you actually need.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">make — you produce something</p>
    <ul>
      <li>make a mistake · make a decision</li>
      <li>make progress · make an effort</li>
      <li>make friends · make a noise</li>
      <li>make money · make a plan</li>
      <li>make a phone call · make a mess</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">do — an activity or duty</p>
    <ul>
      <li>do homework · do exercise</li>
      <li>do the shopping · do the washing-up</li>
      <li>do your best · do a favour</li>
      <li>do research · do business</li>
      <li>do damage · do nothing</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>did her homework</b> carefully, so she only <b>made</b> two
     <b>mistakes</b>. She is <b>making good progress</b>.</p>
  <p class="pe-ex__uz">Afsona uy vazifasini sinchkovlik bilan bajardi, shuning uchun faqat
     ikkita xato qildi. U yaxshi natijaga erishyapti.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana muammoning sababi: oʻzbekchada <b>"qilmoq"</b> ikkalasini ham qoplaydi — "xato
  <b>qilmoq</b>", "uy vazifasini <b>qilmoq</b>". Ingliz tilida esa birinchisi
  <b>make</b>, ikkinchisi <b>do</b>. Shuning uchun "qilmoq" ni koʻrganda avtomatik
  <em>do</em> deb tarjima qilmang — juftlikni yodlash kerak.
</div>

<h3>2. have, take, get, give, pay</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Verb</th><th>Common partners</th></tr>
  <tr><td><b>have</b></td><td>have breakfast, have a shower, have a rest, have fun, have a problem, have a look</td></tr>
  <tr><td><b>take</b></td><td>take a photo, take a taxi, take an exam, take medicine, take care, take a break</td></tr>
  <tr><td><b>get</b></td><td>get a job, get married, get dressed, get angry, get better, get lost</td></tr>
  <tr><td><b>give</b></td><td>give advice, give a lift, give a speech, give an example, give birth</td></tr>
  <tr><td><b>pay</b></td><td>pay attention, pay a visit, pay a compliment, pay the bill</td></tr>
  <tr><td><b>keep</b></td><td>keep a secret, keep calm, keep in touch, keep a promise</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Please <b>pay attention</b>! We're going to <b>take an exam</b>
     tomorrow, so <b>take care</b> and <b>get</b> some sleep.</p>
  <p class="pe-ex__uz">Diqqat qilinglar! Ertaga imtihon topshiramiz, shuning uchun ehtiyot
     boʻling va yaxshi uxlang.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Three classic errors from direct translation: <s>make homework</s> → <b>do homework</b> ·
  <s>do a mistake</s> → <b>make a mistake</b> · <s>take a decision</s> → <b>make a
  decision</b> (British English strongly prefers <em>make</em>).
</div>

<h3>3. Adjective + noun partnerships</h3>

<p>Adjectives have favourite nouns too. Using the expected one makes you sound fluent
immediately.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>strong / heavy</p>
    <p><em>strong coffee, strong accent · heavy rain, heavy traffic</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>high / big</p>
    <p><em>high price, high temperature · big mistake, big problem</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>close / best</p>
    <p><em>a close friend · your best friend</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>fast / quick</p>
    <p><em>a fast car · a quick answer</em></p>
  </div>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>There was a strong rain and a big traffic.</s></p>
  <p class="pe-good">There was <b>heavy rain</b> and <b>heavy traffic</b>.</p>
</div>

<h3>4. Adverb + adjective partnerships</h3>

<p>English does not use <em>very</em> with everything. Certain adverbs go with certain
adjectives, and choosing the right one sounds noticeably better.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>absolutely</b> perfect · <b>completely</b> different ·
     <b>highly</b> recommended · <b>deeply</b> sorry · <b>fully</b> aware ·
     <b>bitterly</b> cold</p>
  <p class="pe-ex__uz">butunlay mukammal · tamoman boshqacha · juda tavsiya etilgan ·
     chuqur afsusda · toʻliq xabardor · qattiq sovuq</p>
  <p class="pe-ex__why">Note: <em>very</em> does not work with absolute adjectives —
     <s>very perfect</s> ✗, <b>absolutely perfect</b> ✓.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada ham shunday juftliklar bor: "<b>qattiq</b> sovuq" deymiz, "kuchli sovuq"
  demaymiz; "<b>chuqur</b> hurmat" deymiz. Yaʼni tushuncha tanish — faqat ingliz tilidagi
  juftlarni alohida oʻrganish kerak. Eng yaxshi usul: oʻqiyotganda yoqqan iborani
  <b>butunligicha</b> daftaringizga koʻchirib qoʻying.
</div>

<h3>5. How to learn collocations</h3>

<ol class="pe-steps">
  <li><b>Never write single words</b> in your notebook. Write <em>make a decision</em>, not
      <em>decision</em>.</li>
  <li><b>Copy whole phrases</b> from things you read. If a phrase appears in a book, it is a
      real collocation.</li>
  <li><b>Learn by the verb:</b> spend one session on <em>make</em>, one on <em>take</em>, one on
      <em>get</em>.</li>
  <li><b>When unsure, choose the simple option.</b> <em>"I had a problem"</em> is safe;
      inventing a partnership rarely works.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng muhim odat: lugʻat daftaringizga <b>yolgʻiz soʻz yozmang</b>. "decision" emas,
  "<b>make a decision</b>" deb yozing; "attention" emas, "<b>pay attention</b>". Kitob
  yoki filmda yoqqan iborani <b>butunligicha</b> koʻchirib qoʻying — agar u kitobda
  boʻlsa, demak u haqiqiy juftlik. Shu bitta odat sizning ingliz tilingizni
  "toʻgʻri" darajadan "tabiiy" darajaga koʻtaradi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I must make my homework.</s></p>
  <p class="pe-good">I must <b>do</b> my homework.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She did a big mistake.</s></p>
  <p class="pe-good">She <b>made</b> a big mistake.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Please make attention to the board.</s></p>
  <p class="pe-good">Please <b>pay attention</b> to the board.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We had a strong rain yesterday.</s></p>
  <p class="pe-good">We had <b>heavy rain</b> yesterday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He gave me a good advice.</s></p>
  <p class="pe-good">He <b>gave me some good advice</b>. <em>(uncountable — PE-2)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     make or do: <em>___ your homework · ___ a decision · ___ the shopping · ___ progress</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>do your homework · make a decision · do the shopping · make progress.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>Can you ___ a photo of us?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>take</strong> — <em>take a photo</em> is the fixed partnership. <s>make a
         photo</s> ✗</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     strong or heavy: <em>___ coffee · ___ traffic · ___ rain · ___ accent</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>strong coffee · heavy traffic · heavy rain · strong accent.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>I want to make some exercise and take a decision about my future.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I want to do some exercise and make a decision about my future.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which adverb? <em>The two brothers are ___ different.</em> (very / completely)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>completely different</strong> — the natural partnership. <em>Very
         different</em> is possible but weaker.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Collocation</b><span>soʻz birikmasi (doimiy)</span></li>
  <li><b>Partnership</b><span>juftlik</span></li>
  <li><b>To make a mistake</b><span>xato qilmoq</span></li>
  <li><b>To make progress</b><span>natijaga erishmoq</span></li>
  <li><b>To pay attention</b><span>diqqat qilmoq</span></li>
  <li><b>To take care</b><span>ehtiyot boʻlmoq</span></li>
  <li><b>To keep in touch</b><span>aloqada boʻlmoq</span></li>
  <li><b>Heavy rain</b><span>kuchli yomgʻir</span></li>
  <li><b>Highly recommended</b><span>juda tavsiya etilgan</span></li>
  <li><b>Natural</b><span>tabiiy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Collocations are <b>fixed partnerships</b> — grammar can be right and the phrase still
        wrong.</li>
    <li><b>make</b> = create (a mistake, a decision) · <b>do</b> = activity (homework,
        shopping).</li>
    <li>Learn the families of <b>have, take, get, give, pay, keep</b>.</li>
    <li><b>heavy</b> rain, <b>strong</b> coffee, <b>completely</b> different — not
        <em>very</em> everything.</li>
    <li>Write <b>phrases</b> in your notebook, never single words.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
