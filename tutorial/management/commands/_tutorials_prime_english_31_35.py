# -*- coding: utf-8 -*-
"""Prime English — end of Block B (31) and start of Block C, the Perfect tenses (32–35).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_31_35.py --author=prime
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
        "title": "PE-31: Time Expressions: ago, for, since, by, until",
        "category": "english",
        "order": 31,
        "summary": (
            "The small words that pin a sentence to a moment: how long, since when, by when — "
            "and the for/since pair that decides half the marks in an exam."
        ),
        "stories": ["Two Years and Eleven Days"],
        "content": """
<h2>PE-31: Time Expressions: ago, for, since, by, until</h2>

<p>You know the tenses of the past and the future now. This short lesson gives you the words
that <b>fix them in time</b> — and it is the last stop before the Perfect tenses, where two of
these words (<em>for</em> and <em>since</em>) become absolutely essential. Learn them properly
here and Block C will feel easy.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>ago</b> — counting backwards from now</li>
    <li><b>for</b> vs <b>since</b> — how long, and since when</li>
    <li><b>by</b> vs <b>until</b> — the deadline and the whole period</li>
    <li><b>during</b> vs <b>while</b>, and <b>in</b> for the future</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The two questions</span>
  <span class="pe-chip pe-chip--s">How long?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">for + period</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">Since when?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">since + point</span>
</div>

<h3>1. ago — counting back from now</h3>

<p><b>Ago</b> measures backwards from this moment, and it always goes <b>after</b> the period
of time. It lives with the Past Simple.</p>

<div class="pe-ex">
  <p class="pe-ex__en">We moved to this city <b>three years ago</b>. I saw him <b>a moment
     ago</b>.</p>
  <p class="pe-ex__uz">Biz bu shaharga uch yil oldin koʻchib keldik. Uni bir lahza oldin
     koʻrdim.</p>
  <p class="pe-ex__why">Never <s>ago three years</s> — the number comes first, exactly as in
     Uzbek.</p>
</div>

<h3>2. for vs since — the pair that matters most</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">for + a length of time</p>
    <ul>
      <li><b>for</b> two hours</li>
      <li><b>for</b> three days</li>
      <li><b>for</b> a long time</li>
      <li><b>for</b> ages</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">since + when it started</p>
    <ul>
      <li><b>since</b> 2020</li>
      <li><b>since</b> Monday</li>
      <li><b>since</b> nine o'clock</li>
      <li><b>since</b> I was a child</li>
    </ul>
  </div>
</div>

<p>The test is simple: if you can answer <em>How long?</em> with it, use <b>for</b>. If it
answers <em>Since when?</em> — a date, a day, a clock time, an event — use <b>since</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I waited <b>for</b> twenty minutes. — I have known Jasur
     <b>since</b> primary school.</p>
  <p class="pe-ex__uz">Yigirma daqiqa kutdim. — Jasurni boshlangʻich sinfdan beri bilaman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu juftlikni oʻzbekcha orqali eslash juda oson: <b>since</b> = "<b>-dan beri</b>"
  (<em>2020-yildan beri</em> → <em>since 2020</em>), <b>for</b> = "<b>davomida</b>" yoki
  shunchaki muddat (<em>ikki soat</em> → <em>for two hours</em>). Agar oʻzbekchada "beri"
  desangiz — <b>since</b>, aytmasangiz — <b>for</b>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qaysi birini tanlashni bilish uchun oʻzingizga oʻzbekcha savol bering:
  <b>"Qancha vaqt?"</b> deb soʻrayapsizmi — javob <b>for</b> bilan
  (<em>ikki soat</em> → <em>for two hours</em>). <b>"Qachondan beri?"</b> deb
  soʻrayapsizmi — javob <b>since</b> bilan (<em>dushanbadan beri</em> →
  <em>since Monday</em>). Savolni topsangiz, predlog oʻzi keladi.
</div>

<h3>3. by vs until — deadline or whole period?</h3>

<p>Both can be translated with the Uzbek "-gacha", which is exactly why they get mixed up.
The difference is what happens <b>during</b> the time.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">by = not later than (a deadline)</p>
    <ul>
      <li>Finish the work <b>by</b> Friday.<br><em>(Friday is the last possible moment)</em></li>
      <li>I'll be home <b>by</b> ten.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">until / till = up to that moment</p>
    <ul>
      <li>I'll wait <b>until</b> Friday.<br><em>(the waiting continues all the time)</em></li>
      <li>She slept <b>until</b> ten.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkalasi ham "-gacha" deb tarjima qilinadi, lekin maʼno boshqacha. <b>by</b> — ish
  <b>oʻsha vaqtgacha tugashi kerak</b> ("jumagacha tugating"). <b>until</b> — ish
  <b>oʻsha vaqtgacha davom etadi</b> ("jumagacha kutaman"). Tekshiruv savoli: harakat
  davom etadimi (until) yoki tugashi kerakmi (by)?
</div>

<h3>4. during vs while</h3>

<p>They mean the same thing, but they are followed by different kinds of words:
<b>during + a noun</b>, <b>while + a whole clause</b> (subject + verb).</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>During</b> the lesson we spoke only English. =
     <b>While</b> we were in the lesson, we spoke only English.</p>
  <p class="pe-ex__uz">Dars davomida faqat ingliz tilida gaplashdik.</p>
  <p class="pe-ex__why">Never <s>during I was reading</s> — that needs <b>while</b>.</p>
</div>

<h3>5. Two more you will need</h3>

<ul>
  <li><b>in + a period</b> = after that much time, from now: <em>The bus leaves <b>in</b> ten
      minutes.</em></li>
  <li><b>from … to / till</b> = the two ends of a period: <em>We study <b>from</b> eight
      <b>to</b> two.</em></li>
</ul>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Do not confuse <b>in</b> and <b>for</b> in the future. <em>I'll be ready <b>in</b> five
  minutes</em> = five minutes from now. <em>I worked <b>for</b> five minutes</em> = the work
  lasted five minutes. One points at a moment, the other measures a length.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have been here since three hours.</s></p>
  <p class="pe-good">I have been here <b>for</b> three hours.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has worked here for 2019.</s></p>
  <p class="pe-good">She has worked here <b>since</b> 2019.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I met him ago two days.</s></p>
  <p class="pe-good">I met him two days <b>ago</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Please send the letter until Monday.</s></p>
  <p class="pe-good">Please send the letter <b>by</b> Monday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>During I was cooking, the phone rang.</s></p>
  <p class="pe-good"><b>While</b> I was cooking, the phone rang.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     for or since: <em>Afsona has studied English <span class="pe-blank">?</span> five years,
     and <span class="pe-blank">?</span> September she has studied Korean too.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>for … since.</strong> <em>Five years</em> is a length (How long?);
         <em>September</em> is a starting point (Since when?).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     by or until: <em>The shop is open <span class="pe-blank">?</span> nine, so buy the bread
     <span class="pe-blank">?</span> then.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>until … by.</strong> The shop stays open the whole time (<em>until</em>);
         your shopping must be finished no later than nine (<em>by</em>).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>My grandfather died ago ten years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My grandfather died ten years ago.</strong></p>
      <p><em>Ago</em> always follows the period of time — the same order as Uzbek "oʻn yil
         oldin".</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     during or while: <em>___ the film, nobody spoke. ___ we were watching, nobody
     spoke.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>During the film … While we were watching.</strong></p>
      <p><em>During</em> takes a noun; <em>while</em> takes a subject and a verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What is the difference? <em>(a) I'll finish it in an hour. (b) I'll finish it by an
     hour.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) is correct</strong> = one hour from now. <strong>(b) is wrong</strong> —
         <em>by</em> needs a clock time or a day: <em>by five o'clock</em>, <em>by
         Friday</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Ago</b><span>...oldin</span></li>
  <li><b>For</b><span>...davomida</span></li>
  <li><b>Since</b><span>...dan beri</span></li>
  <li><b>By</b><span>...gacha (muddat)</span></li>
  <li><b>Until / till</b><span>...gacha (davom etib)</span></li>
  <li><b>During</b><span>...davomida (ot bilan)</span></li>
  <li><b>Deadline</b><span>oxirgi muddat</span></li>
  <li><b>Period</b><span>davr, muddat</span></li>
  <li><b>For ages</b><span>juda uzoq vaqtdan beri</span></li>
  <li><b>Starting point</b><span>boshlanish nuqtasi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>ago</b> comes <b>after</b> the period, with the Past Simple.</li>
    <li><b>for</b> = how long · <b>since</b> = since when (Uzbek "-dan beri").</li>
    <li><b>by</b> = a deadline, finish before it · <b>until</b> = the action continues to it.</li>
    <li><b>during</b> + noun · <b>while</b> + subject and verb.</li>
    <li><b>in</b> ten minutes = from now · <b>for</b> ten minutes = how long it lasted.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-32: Present Perfect: Form and the Idea of \"It Matters Now\"",
        "category": "english",
        "order": 32,
        "summary": (
            "The tense Uzbek does not have. Learn have/has + V3 and the one idea behind it: a "
            "past action whose result you can still feel today."
        ),
        "stories": ["Somebody Has Found It"],
        "content": """
<h2>PE-32: Present Perfect: Form and the Idea of "It Matters Now"</h2>

<p>Now we reach the tense that makes learners from Uzbekistan work hardest — <b>because there
is no Uzbek equivalent at all</b>. In Uzbek, <em>kalitimni yoʻqotdim</em> is simply the past.
English gives you a choice, and that choice carries meaning: <em>I lost my keys</em> tells a
story about yesterday; <em><b>I've lost</b> my keys</em> means <mark>I still can't get into my
house right now</mark>. The Present Perfect is a past action <b>with a present
consequence</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>have / has + V3</b> (past participle)</li>
    <li>Where V3 comes from, for regular and irregular verbs</li>
    <li>Three jobs: a result now, life experience, an unfinished time period</li>
    <li>The one word you must <b>never</b> put in this tense</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">I / you / we / they</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">have</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">he / she / it</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">has</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
</div>

LEGEND_HERE

<h3>1. The picture: a bridge from then to now</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:74%"></span>
    <span class="pe-tl-band" style="left:20%;width:54%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:26%"></span>
    <span class="pe-tl-tag" style="left:22%">I lost them…</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The action happened back there — but the band reaches all the way to NOW, because the
<b>result</b> is still here. That band is the whole idea of the tense.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">have</span>
     <span class="pe-hl pe-hl--v">lost</span> my keys. <em>(= I don't have them now)</em></p>
  <p class="pe-ex__uz">Kalitlarimni yoʻqotib qoʻydim. (yaʼni hozir ular menda yoʻq)</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida bu zamon <b>yoʻq</b> — "yoʻqotdim" ham Past Simple, ham Present Perfect
  boʻlishi mumkin. Shuning uchun tarjima qilib tanlab boʻlmaydi. Oʻzingizga boshqa savol
  bering: <b>"qachon boʻlgani muhimmi, yoki hozirgi natijasi muhimmi?"</b> Natija muhim
  boʻlsa — Present Perfect. Eng yaqin oʻzbekcha shakl — "<b>...ib qoʻyganman / ...ib
  boʻlganman</b>".
</div>

<h3>2. V3 — the third form</h3>

<p>The Present Perfect needs the <b>past participle</b>, which we call V3. For regular verbs it
is identical to V2 — just <b>-ed</b>. Only irregular verbs need extra memory, and this is why
PE-21 told you to learn them in threes.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>V1 (base)</th><th>V2 (past)</th><th>V3 (participle)</th><th>Oʻzbekcha</th></tr>
  <tr><td>work</td><td>worked</td><td><b>worked</b></td><td>ishlamoq</td></tr>
  <tr><td>go</td><td>went</td><td><b>gone</b></td><td>bormoq</td></tr>
  <tr><td>see</td><td>saw</td><td><b>seen</b></td><td>koʻrmoq</td></tr>
  <tr><td>do</td><td>did</td><td><b>done</b></td><td>qilmoq</td></tr>
  <tr><td>eat</td><td>ate</td><td><b>eaten</b></td><td>yemoq</td></tr>
  <tr><td>write</td><td>wrote</td><td><b>written</b></td><td>yozmoq</td></tr>
  <tr><td>take</td><td>took</td><td><b>taken</b></td><td>olmoq</td></tr>
  <tr><td>be</td><td>was/were</td><td><b>been</b></td><td>boʻlmoq</td></tr>
  <tr><td>have</td><td>had</td><td><b>had</b></td><td>ega boʻlmoq</td></tr>
</table>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Never put V2 after <em>have</em>. <s>I have went</s>, <s>I have saw</s>, <s>I have did</s>
  are the commonest errors in this whole tense. It is
  <b>I have gone / seen / done</b>.
</div>

<h3>3. Negatives, questions and the short forms</h3>

<ol class="pe-steps">
  <li><b>Short forms:</b> <em>I've, you've, we've, they've</em> · <em>he's, she's, it's</em>
      (here <b>'s = has</b>, as you learned in PE-14).</li>
  <li><b>Negative:</b> <em>I <b>haven't</b> finished. She <b>hasn't</b> arrived.</em></li>
  <li><b>Question:</b> <em><b>Have</b> you finished? <b>Has</b> she arrived?</em></li>
  <li><b>Short answers:</b> <em>Yes, I have. / No, I haven't.</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>Have</b> you <b>done</b> your homework? — No, I
     <b>haven't finished</b> it. Sherbek <b>hasn't started</b> his at all.</p>
  <p class="pe-ex__uz">— Uy vazifangni qildingmi? — Yoʻq, tugatmadim. Sherbek esa umuman
     boshlamagan.</p>
  <p class="pe-ex__why">Only <em>have/has</em> moves or takes <em>not</em> — the V3 never
     changes.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat, <b>'s</b> qisqartmasi yana chalgʻitishi mumkin (PE-14 ni eslang):
  <em>He<b>'s</b> gone</em> = <em>he <b>has</b> gone</em> (V3 keladi), lekin
  <em>He<b>'s</b> going</em> = <em>he <b>is</b> going</em> (-ing keladi). Qoida oddiy:
  <b>'s</b> dan keyin <b>V3</b> boʻlsa — <em>has</em>, <b>-ing</b> boʻlsa — <em>is</em>.
</div>

<h3>4. The three jobs</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>A result you can see now</p>
    <p><em>She <b>has broken</b> her arm.</em> (it is in plaster today)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Life experience — when is not said</p>
    <p><em>I <b>have been</b> to Bukhara three times.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>A time period that isn't over</p>
    <p><em>I <b>have written</b> two letters today.</em> (today isn't finished)</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek <b>has passed</b> his driving test, so now he can drive.</p>
  <p class="pe-ex__uz">Sherbek haydovchilik imtihonidan oʻtdi, shuning uchun endi mashina
     hayday oladi.</p>
  <p class="pe-ex__why">The exam is finished; the licence is the present result.</p>
</div>

<h3>5. The forbidden word</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  <b>Never</b> put a finished past time with the Present Perfect. If the sentence contains
  <em>yesterday, last week, in 2019, two days ago, when?</em> — you must use the Past Simple.
  <s>I have seen him yesterday</s> ✗ → <b>I saw him yesterday</b> ✓.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sabab oddiy: Present Perfect "hozirgi ahamiyat" haqida, <em>yesterday</em> esa gapni
  butunlay oʻtmishga bogʻlab qoʻyadi — ikkalasi bir gapda yashay olmaydi. Shuning uchun
  <b>"Qachon?"</b> degan savolga ham hech qachon Present Perfect bilan javob berilmaydi:
  <s>When have you come?</s> emas, <b>When did you come?</b>
</div>

<h3>6. gone or been?</h3>

<p>A small but very useful difference:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">has gone to = went and is still there</p>
    <p><em>Jasur <b>has gone to</b> Tashkent.</em><br>(he is in Tashkent now)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">has been to = went and came back</p>
    <p><em>Jasur <b>has been to</b> Tashkent.</em><br>(he visited it; he is here now)</p>
  </div>
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have went to the shop.</s></p>
  <p class="pe-good">I <b>have gone</b> to the shop. <em>(V3, not V2)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He have finished his homework.</s></p>
  <p class="pe-good">He <b>has</b> finished his homework.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I have seen that film last night.</s></p>
  <p class="pe-good">I <b>saw</b> that film last night.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did you have ever been to Samarkand?</s></p>
  <p class="pe-good"><b>Have you ever been</b> to Samarkand?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has been to Nukus, so she isn't here now.</s></p>
  <p class="pe-good">She <b>has gone to</b> Nukus, so she isn't here now.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>I can't come in — I <span class="pe-blank">?</span> (lose) my key.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>have lost</strong> — the losing happened in the past, but the problem
         (no key) is happening right now.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Give the V3: <em>write · take · be · do · see</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>written · taken · been · done · seen.</strong></p>
      <p>Notice how many end in <b>-en</b> — that is a useful family.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which is wrong, and why? <em>(a) I have finished my work. (b) I have finished my work
     two hours ago.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) is wrong.</strong> <em>Two hours ago</em> is a finished past time, so it
         needs the Past Simple: <em>I <b>finished</b> my work two hours ago.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     gone or been? <em>— Where is your sister? — She ___ to the market.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>has gone</strong> — she is at the market now, which is exactly why she is not
         here.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one sentence about a result you can see in your room right now.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Somebody <b>has opened</b> the window — the room is
         cold.</em></p>
      <p>Past action + present result. That is the test for this tense.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Present Perfect</b><span>hozirgi tugallangan zamon</span></li>
  <li><b>Past participle (V3)</b><span>uchinchi shakl</span></li>
  <li><b>Result</b><span>natija</span></li>
  <li><b>Consequence</b><span>oqibat</span></li>
  <li><b>Experience</b><span>tajriba, boshdan kechirish</span></li>
  <li><b>Unfinished period</b><span>tugamagan davr</span></li>
  <li><b>To lose</b><span>yoʻqotmoq</span></li>
  <li><b>To pass an exam</b><span>imtihondan oʻtmoq</span></li>
  <li><b>To break</b><span>sindirmoq</span></li>
  <li><b>Relevant now</b><span>hozir ahamiyatli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>have / has + V3</b> — and <b>has</b> only for he/she/it.</li>
    <li>Meaning: a past action whose <b>result matters now</b>.</li>
    <li>V3 ≠ V2: <b>I have gone</b>, not <s>I have went</s>.</li>
    <li>Three jobs: present result · life experience · unfinished time period.</li>
    <li><b>Never</b> with <em>yesterday, last week, ago</em> or the question <em>When?</em></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-33: Present Perfect with for and since",
        "category": "english",
        "order": 33,
        "summary": (
            "How long have you lived here? The structure for something that started in the past "
            "and is STILL true — where Uzbek uses the present and English does not."
        ),
        "stories": ["The Dog Who Waited at the Station"],
        "content": """
<h2>PE-33: Present Perfect with for and since</h2>

<p>Here is the single most useful thing the Present Perfect does, and the place where Uzbek
speakers most often say something wrong without noticing. In Uzbek: <em>Men bu yerda oʻn
yildan beri <b>yashayman</b></em> — present tense. Translate that word for word and you get
<s>I live here for ten years</s>, which is wrong in English. The correct sentence is
<em>I <b>have lived</b> here for ten years.</em></p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The structure <b>have/has + V3 + for / since</b></li>
    <li>Why English uses a past-looking tense for something still true</li>
    <li>How to ask and answer <b>How long …?</b></li>
    <li>The difference between <em>I lived</em> and <em>I have lived</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Started before, still true</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">have / has</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">for / since</span>
</div>

LEGEND_HERE

<h3>1. The picture: still going</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:76%"></span>
    <span class="pe-tl-band" style="left:14%;width:62%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:14%"></span>
    <span class="pe-tl-tag" style="left:20%">since 2016 — and still now</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The band starts at a point in the past and <b>touches NOW</b>. Nothing has stopped. That is
why English refuses to use the Past Simple here — the past would close the band before it
reached today.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">We</span>
     <span class="pe-hl pe-hl--aux">have lived</span> in this house
     <span class="pe-hl pe-hl--adv">for ten years</span>. <em>(we live here now)</em></p>
  <p class="pe-ex__uz">Biz bu uyda oʻn yildan beri yashaymiz. (hozir ham shu yerdamiz)</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu — eng muhim farq butun kursda. Oʻzbekchada bunday gaplar <b>hozirgi zamonda</b>
  tuziladi: "beshinchi sinfdan beri <b>oʻqiyman</b>", "ikki yildan beri bu yerda
  <b>ishlayman</b>". Ingliz tilida esa <b>Present Perfect</b> kerak:
  <em>I <b>have studied</b>…</em>, <em>I <b>have worked</b>…</em>
  <s>I work here for two years</s> — bu ingliz quloqqa xato eshitiladi.
</div>

<h3>2. for and since — applied</h3>

<p>You met the pair in PE-31; here it does its real work. <b>for</b> answers <em>How long?</em>
and <b>since</b> answers <em>Since when?</em></p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">for + a length</p>
    <ul>
      <li>I've known her <b>for</b> six years.</li>
      <li>He's been ill <b>for</b> a week.</li>
      <li>We've waited <b>for</b> two hours.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">since + a starting point</p>
    <ul>
      <li>I've known her <b>since</b> 2019.</li>
      <li>He's been ill <b>since</b> Monday.</li>
      <li>We've waited <b>since</b> two o'clock.</li>
    </ul>
  </div>
</div>

<p><b>Since</b> can also be followed by a whole clause — and that clause takes the
<b>Past Simple</b>, because it names the moment when everything started.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>have wanted</b> to be a doctor <b>since I was</b> a child.
     Afsona <b>hasn't called</b> me <b>since she moved</b> to Tashkent.</p>
  <p class="pe-ex__uz">Bolaligimdan beri shifokor boʻlishni xohlayman. Afsona Toshkentga
     koʻchib ketganidan beri menga qoʻngʻiroq qilmadi.</p>
  <p class="pe-ex__why">Two tenses in one sentence: Present Perfect + <em>since</em> + Past
     Simple.</p>
</div>

<h3>3. Asking How long?</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Question</span>
  <span class="pe-chip pe-chip--adv">How long</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">have / has</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
  <span class="pe-op">?</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>How long have</b> you <b>studied</b> English? — <b>For</b> four
     years. / <b>Since</b> the fifth form.</p>
  <p class="pe-ex__uz">— Ingliz tilini qancha vaqtdan beri oʻrganasiz? — Toʻrt yildan beri. /
     Beshinchi sinfdan beri.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Some verbs are so common in this pattern that you should learn them as ready phrases:
  <em>I've known…, I've had…, I've lived…, I've worked…, I've been…, I've wanted…</em>
  In an interview or an exam these five will carry you a long way.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Since</b> dan keyin butun gap kelsa, u <b>Past Simple</b> da boʻladi — chunki u
  boshlangan <b>bir lahzani</b> koʻrsatadi: <em>since I <b>moved</b></em>
  ("koʻchib kelganimdan beri"), <s>since I have moved</s> emas. Yaʼni bitta gapda
  ikkita zamon yonma-yon turadi: <b>have V3</b> ... <b>since</b> ... <b>V2</b>.
</div>

<h3>4. "I lived" vs "I have lived"</h3>

<p>Both are correct English — they simply describe different lives.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Past Simple = finished</p>
    <p><em>I <b>lived</b> in Bukhara for five years.</em></p>
    <p>I don't live there any more.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Present Perfect = still true</p>
    <p><em>I <b>have lived</b> in Bukhara for five years.</em></p>
    <p>I still live there today.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni koʻrsatuvchi savol bitta: <b>hozir ham davom etyaptimi?</b> Davom etsa — Present
  Perfect ("hali ham shu yerda yashayman"). Tugagan boʻlsa — Past Simple ("oʻsha paytda
  yashagan edim, endi yoʻq"). Oʻzbekcha tarjimasi ikkalasida ham deyarli bir xil, shuning
  uchun <b>maʼnoga</b> qarang, soʻzga emas.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I am here since Monday.</s></p>
  <p class="pe-good">I <b>have been</b> here since Monday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I know Jasur for ten years.</s></p>
  <p class="pe-good">I <b>have known</b> Jasur for ten years.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has worked here since three years.</s></p>
  <p class="pe-good">She has worked here <b>for</b> three years.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How long do you live in this city?</s></p>
  <p class="pe-good"><b>How long have you lived</b> in this city?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I haven't seen him since he has left.</s></p>
  <p class="pe-good">I haven't seen him <b>since he left</b>. <em>(Past Simple after "since")</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Correct it: <em>My father works in this factory for twenty years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My father has worked in this factory for twenty years.</strong></p>
      <p>He started twenty years ago and still works there — so English needs the Present
         Perfect, even though Uzbek uses the present.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     for or since: <em>We have been friends <span class="pe-blank">?</span> we were six,
     that is <span class="pe-blank">?</span> almost ten years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>since … for.</strong> <em>We were six</em> is the starting moment;
         <em>almost ten years</em> is the length.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) Sherbek played football for five years.
     (b) Sherbek has played football for five years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) He has stopped</strong> — those five years are over.
         <strong>(b) He still plays</strong> — the five years reach today.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Ask the question: <em>— … ? — I have had this phone for two years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>How long have you had this phone?</strong></p>
      <p><em>How long</em> + <em>have</em> + subject + V3 — and <em>have</em> appears twice
         here, once as helper and once as the main verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Translate: <em>Men uni beshinchi sinfdan beri bilaman.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I have known him since the fifth form.</strong></p>
      <p>Uzbek "bilaman" is present, but English must use <b>have known</b> — the knowing
         started then and continues now.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>How long?</b><span>qancha vaqtdan beri?</span></li>
  <li><b>For</b><span>...davomida</span></li>
  <li><b>Since</b><span>...dan beri</span></li>
  <li><b>To continue</b><span>davom etmoq</span></li>
  <li><b>Still true</b><span>hozir ham shunday</span></li>
  <li><b>To move (house)</b><span>koʻchib oʻtmoq</span></li>
  <li><b>Interview</b><span>suhbat, intervyu</span></li>
  <li><b>To be ill</b><span>kasal boʻlmoq</span></li>
  <li><b>Factory</b><span>zavod, fabrika</span></li>
  <li><b>Almost</b><span>deyarli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Started in the past + <b>still true now</b> → <b>have/has + V3</b>, never the present
        tense.</li>
    <li>Uzbek says "yashayman", English says "<b>have lived</b>" — this one habit fixes many
        sentences.</li>
    <li><b>for</b> + length · <b>since</b> + starting point · <b>since</b> + Past Simple
        clause.</li>
    <li>Ask with <b>How long have you …?</b></li>
    <li><em>I lived there</em> = finished · <em>I have lived there</em> = still there.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-34: Present Perfect with already, yet, just, still, ever, never",
        "category": "english",
        "order": 34,
        "summary": (
            "Six small words that give the Present Perfect its colour — and the exact position "
            "each one takes in the sentence."
        ),
        "stories": ["Has the Tortoise Finished Yet?"],
        "content": """
<h2>PE-34: Present Perfect with already, yet, just, still, ever, never</h2>

<p>The Present Perfect almost never travels alone. It brings a small companion word that tells
your listener <em>how</em> you feel about the news: sooner than expected, a second ago, not
happening despite waiting, or never in your whole life. Six words, each with its own fixed
position in the sentence.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What each of the six words adds to the meaning</li>
    <li>Where each one stands — middle of the sentence or the end</li>
    <li>Which belong to questions, which to negatives</li>
    <li>Why <b>never</b> must not have a second negative next to it</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two positions</span>
  <span class="pe-chip pe-chip--aux">have</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">already / just / never</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">yet</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">at the end</span>
</div>

LEGEND_HERE

<h3>1. The six words at a glance</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>already — allaqachon</p>
    <p>Sooner than expected. Positive sentences. <em>I've <b>already</b> eaten.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>yet — hali</p>
    <p>Questions and negatives, at the end. <em>Have you finished <b>yet</b>?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>just — hozirgina</p>
    <p>A moment ago. <em>She has <b>just</b> left.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>still — hamon</p>
    <p>Expected but not happened. <em>He <b>still</b> hasn't called.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>ever — biror marta</p>
    <p>In questions about life. <em>Have you <b>ever</b> been to Khiva?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">6</span>never — hech qachon</p>
    <p>Negative by itself. <em>I have <b>never</b> seen snow.</em></p>
  </div>
</div>

<h3>2. already, just, never, ever — in the middle</h3>

<p>These four sit <b>between</b> the helper (<em>have/has</em>) and the V3. That position never
changes.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--aux">has</span>
     <span class="pe-hl pe-hl--adv">already</span>
     <span class="pe-hl pe-hl--v">done</span> her homework, and she
     <span class="pe-hl pe-hl--aux">has</span>
     <span class="pe-hl pe-hl--adv">just</span>
     <span class="pe-hl pe-hl--v">started</span> reading.</p>
  <p class="pe-ex__uz">Afsona uy vazifasini allaqachon qilib boʻldi va hozirgina kitob oʻqishni
     boshladi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Have</b> you <b>ever eaten</b> Korean food? — No, I <b>have never
     tried</b> it.</p>
  <p class="pe-ex__uz">Hech koreys taomini yeb koʻrganmisiz? — Yoʻq, hech qachon yeb
     koʻrmaganman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Never</b> — bu allaqachon inkor soʻz, shuning uchun yoniga ikkinchi inkor qoʻyilmaydi:
  <em>I <b>have never</b> been</em> ✓, <s>I haven't never been</s> ✗. Bu qoidani PE-11 da
  koʻrgan edingiz: oʻzbekchada "hech qachon <b>bormaganman</b>" — ikkita inkor, ingliz
  tilida esa <b>bittasi</b> yetarli.
</div>

<h3>3. yet — at the end, and only in questions and negatives</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">already → positive</p>
    <ul>
      <li>I've <b>already</b> seen this film.</li>
      <li>They've <b>already</b> arrived.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">yet → question / negative, at the end</p>
    <ul>
      <li>Have you seen this film <b>yet</b>?</li>
      <li>They haven't arrived <b>yet</b>.</li>
    </ul>
  </div>
</div>

<p>There is one useful exception: <em>already</em> can appear in a question to show
<b>surprise</b> — <em>"Have you finished <b>already</b>?"</em> means "So fast? I didn't expect
that!"</p>

<h3>4. still — the one that goes before the helper</h3>

<p><b>Still</b> means something you expected has <em>not</em> happened, and you are getting
impatient. Its position is different from all the others: it comes <b>before</b> the negative
helper.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I sent the letter a month ago and he <b>still hasn't</b> replied.</p>
  <p class="pe-ex__uz">Xatni bir oy oldin yuborganman, u hamon javob yozmadi.</p>
  <p class="pe-ex__why">Compare: <em>He hasn't replied <b>yet</b></em> is neutral;
     <em><b>still</b> hasn't replied</em> sounds annoyed.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>yet</b> va <b>still</b> ikkalasi ham "hali" deb tarjima qilinadi, lekin ohangi
  boshqacha. <em>He hasn't come <b>yet</b></em> — xolis xabar ("hali kelmadi").
  <em>He <b>still</b> hasn't come</em> — sabrsizlik, norozilik ("hamon kelmadi-ya!").
  Va oʻrni ham farq qiladi: <b>yet</b> — gap oxirida, <b>still</b> — <em>hasn't</em>
  dan oldin.
</div>

<h3>5. All six in one conversation</h3>

<p>Here is how they actually sound together. Read it aloud — this is a completely normal
exchange between two friends.</p>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>Have</b> you <b>ever tried</b> making plov yourself?<br>
     — Yes! I've <b>just</b> made one, actually. <b>Have</b> you eaten <b>yet</b>?<br>
     — No, I <b>still haven't</b> had lunch. But my brother has <b>already</b> eaten
     everything, and I've <b>never</b> seen him so full.</p>
  <p class="pe-ex__uz">— Hech oʻzingiz palov pishirib koʻrganmisiz?<br>
     — Ha! Hozirgina pishirdim. Siz ovqatlandingizmi?<br>
     — Yoʻq, hamon tushlik qilmadim. Akam esa hammasini allaqachon yeb boʻlibdi, uni hech
     qachon bunchalik toʻygan holda koʻrmaganman.</p>
  <p class="pe-ex__why">Six words, six positions — and not one of them could move somewhere
     else.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu soʻzlarni alohida emas, <b>tayyor iboralar</b> sifatida yodlang, chunki ular deyarli
  doim bir xil shaklda uchraydi: <em>Have you ever…?</em> ("Hech...ganmisiz?"),
  <em>I've never…</em> ("Hech qachon...maganman"), <em>I've just…</em> ("Hozirgina..."),
  <em>Have you … yet?</em> ("...dingizmi?"). Butun boʻlakni yodlasangiz, oʻrni haqida
  oʻylab ham oʻtirmaysiz.
</div>

<h3>6. Position summary</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Word</th><th>Position</th><th>Sentence type</th><th>Example</th></tr>
  <tr><td>already</td><td>have + <b>already</b> + V3</td><td>positive</td><td>I've already eaten.</td></tr>
  <tr><td>just</td><td>have + <b>just</b> + V3</td><td>positive</td><td>He has just gone.</td></tr>
  <tr><td>never</td><td>have + <b>never</b> + V3</td><td>negative meaning</td><td>I've never flown.</td></tr>
  <tr><td>ever</td><td>have + subject + <b>ever</b> + V3</td><td>question</td><td>Have you ever flown?</td></tr>
  <tr><td>yet</td><td>at the <b>end</b></td><td>question / negative</td><td>Has it started yet?</td></tr>
  <tr><td>still</td><td><b>before</b> hasn't / haven't</td><td>negative</td><td>She still hasn't come.</td></tr>
</table>
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have yet finished my homework.</s></p>
  <p class="pe-good">I have <b>already</b> finished my homework. / I haven't finished it
     <b>yet</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Have you already eaten yet?</s></p>
  <p class="pe-good">Have you eaten <b>yet</b>?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I haven't never been to Tashkent.</s></p>
  <p class="pe-good">I <b>have never been</b> to Tashkent.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has still not arrived — I mean, she hasn't still arrived.</s></p>
  <p class="pe-good">She <b>still hasn't</b> arrived.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did you ever been to Samarkand?</s></p>
  <p class="pe-good"><b>Have you ever been</b> to Samarkand?</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Put <em>already</em> in the right place: <em>Jasur has finished his lunch.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur has already finished his lunch.</strong> Between the helper and the
         V3.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     already or yet: <em>— Have you done the washing-up <span class="pe-blank">?</span>
     — Yes, I've <span class="pe-blank">?</span> done it.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>yet … already.</strong> <em>Yet</em> ends the question; <em>already</em> sits
         in the middle of the positive answer.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference in feeling? <em>(a) The bus hasn't come yet. (b) The bus still
     hasn't come.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) neutral information · (b) impatience</strong> — you have been waiting too
         long and you are not happy about it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>I have never not seen such a beautiful place.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I have never seen such a beautiful place.</strong></p>
      <p><em>Never</em> is already the negative — English allows only one per sentence.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a question with <em>ever</em> and answer it with <em>never</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>— <b>Have</b> you <b>ever ridden</b> a horse?
         — No, I <b>have never ridden</b> one.</em></p>
      <p>Both words sit in the same slot: between the helper and the V3.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Already</b><span>allaqachon</span></li>
  <li><b>Yet</b><span>hali (savol/inkor)</span></li>
  <li><b>Just</b><span>hozirgina</span></li>
  <li><b>Still</b><span>hamon</span></li>
  <li><b>Ever</b><span>biror marta</span></li>
  <li><b>Never</b><span>hech qachon</span></li>
  <li><b>Position</b><span>oʻrni</span></li>
  <li><b>To reply</b><span>javob bermoq</span></li>
  <li><b>Impatient</b><span>sabrsiz</span></li>
  <li><b>Washing-up</b><span>idish yuvish</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>already, just, never, ever</b> → between <b>have</b> and <b>V3</b>.</li>
    <li><b>yet</b> → at the <b>end</b>, in questions and negatives only.</li>
    <li><b>still</b> → <b>before</b> <em>hasn't/haven't</em>, and it sounds impatient.</li>
    <li><b>already</b> in a question = surprise: <em>Have you finished already?</em></li>
    <li>One negative per sentence: <b>I have never been</b>, not <s>haven't never</s>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-35: Present Perfect vs Past Simple — The Big Decision",
        "category": "english",
        "order": 35,
        "summary": (
            "The choice that decides more exam marks than any other in English — with one "
            "reliable test, the signal-word lists, and the news pattern used by every reporter."
        ),
        "stories": ["The Watch in the Second Drawer"],
        "content": """
<h2>PE-35: Present Perfect vs Past Simple — The Big Decision</h2>

<p>This is the most tested pair in English grammar, and for Uzbek speakers it is the hardest,
because <b>one Uzbek form covers both</b>. <em>Kitobni oʻqidim</em> can mean <em>I read the
book</em> (last summer, a finished story) or <em>I have read the book</em> (so I can tell you
about it now). The good news: there is one clean test, and it works nearly every time.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The one test question that decides between the two tenses</li>
    <li>The signal words that belong to each</li>
    <li>Finished vs unfinished time periods</li>
    <li>The news pattern: announce, then explain</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The test question</span>
  <span class="pe-chip pe-chip--s">Is the time finished?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">Past Simple</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">Does it matter now?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">Present Perfect</span>
</div>

<h3>1. Two pictures</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:80%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:16%"></span>
    <span class="pe-tl-band" style="left:44%;width:36%"></span>
    <span class="pe-tl-tag" style="left:16%">I broke it (2019)</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The lonely red dot is the Past Simple — closed, finished, dated. The band that reaches NOW
is the Present Perfect — still connected to today.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Past Simple — a closed box</p>
    <ul>
      <li>I <b>broke</b> my arm <b>last year</b>.</li>
      <li>She <b>lived</b> in Nukus <b>from 2015 to 2019</b>.</li>
      <li>We <b>saw</b> him <b>yesterday</b>.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Present Perfect — reaching now</p>
    <ul>
      <li>I<b>'ve broken</b> my arm. <em>(it hurts today)</em></li>
      <li>She<b>'s lived</b> in Nukus <b>for four years</b>.</li>
      <li>We <b>haven't seen</b> him <b>this week</b>.</li>
    </ul>
  </div>
</div>

<h3>2. The signal words</h3>

<p>In an exam, the fastest route to the right answer is to find the time expression. Each tense
has its own family, and they never mix.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Past Simple signals</p>
    <p><em>yesterday, last week/month/year, in 2019, two days ago, then, When…?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Present Perfect signals</p>
    <p><em>ever, never, already, yet, just, so far, recently, for, since</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Finished periods</p>
    <p><em>last night, in June</em> (if June is over) → Past Simple</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Unfinished periods</p>
    <p><em>today, this week, this year</em> (still going) → Present Perfect</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>have drunk</b> three cups of tea <b>today</b>. —
     I <b>drank</b> three cups of tea <b>yesterday</b>.</p>
  <p class="pe-ex__uz">Bugun uch piyola choy ichdim. — Kecha uch piyola choy ichdim.</p>
  <p class="pe-ex__why">Identical in Uzbek. In English, <em>today</em> is not over, but
     <em>yesterday</em> is.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada ikkala gap ham "ichdim" bilan tugaydi, shuning uchun <b>tarjima yordam
  bermaydi</b>. Buning oʻrniga vaqt soʻziga qarang: <em>bugun, shu hafta, shu yil</em>
  (hali tugamagan) → Present Perfect. <em>Kecha, oʻtgan hafta, 2019-yilda</em> (tugagan)
  → Past Simple. Bu — imtihonda eng tez ishlaydigan usul.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻp oʻquvchilar shubhaga borsa, doim Past Simple ni tanlaydi — "xavfsizroq" deb.
  Lekin uchta holatda bu <b>aniq xato</b> boʻladi: (1) gapda <em>ever, never, already,
  yet, just</em> boʻlsa; (2) <em>for / since</em> bilan hozir ham davom etayotgan ish
  boʻlsa; (3) <em>today, this week</em> kabi <b>tugamagan</b> davr boʻlsa. Shu uchtasini
  eslab qolsangiz, xatolaringiz keskin kamayadi.
</div>

<h3>3. The three-step test</h3>

<ol class="pe-steps">
  <li><b>Is there a finished past time in the sentence</b> (<em>yesterday, ago, in 2019</em>)?
      → <b>Past Simple</b>. Stop here — this beats everything else.</li>
  <li><b>Am I asking or saying WHEN it happened?</b> → <b>Past Simple</b>.
      (<em>When did you arrive?</em>)</li>
  <li><b>Is it about the result now, my life experience, or a period that hasn't
      ended?</b> → <b>Present Perfect</b>.</li>
</ol>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  The question word <b>When?</b> can never take the Present Perfect, because it is asking for
  exactly the finished time this tense refuses to name.
  <s>When have you come?</s> → <b>When did you come?</b>
</div>

<h3>4. The news pattern — how English really uses both</h3>

<p>Listen to any news report and you will hear this shape: the <b>headline</b> in the Present
Perfect (this is new, it matters now), then the <b>details</b> in the Past Simple (here is the
finished story).</p>

<div class="pe-ex">
  <p class="pe-ex__en">Our team <b>has won</b> the championship! They <b>played</b> brilliantly
     and <b>scored</b> in the last minute.</p>
  <p class="pe-ex__uz">Jamoamiz chempionatda gʻalaba qozondi! Ular ajoyib oʻynashdi va oxirgi
     daqiqada gol urishdi.</p>
  <p class="pe-ex__why">Sentence 1 = the news. Sentences 2 and 3 = the finished details.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>has passed</b> her exam. She <b>studied</b> all night and
     <b>finished</b> the last question just in time.</p>
  <p class="pe-ex__uz">Afsona imtihondan oʻtdi. U tun boʻyi tayyorlandi va oxirgi savolni
     ayni vaqtida yozib tugatdi.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Copy this pattern when you write or speak. Start with <em>"I've just…"</em> or
  <em>"Something has happened…"</em>, then switch to the Past Simple for the story. It
  instantly makes you sound like a natural speaker instead of a textbook.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu naqshni yodda tuting: <b>yangilikni</b> Present Perfect bilan aytasiz ("Imtihondan
  oʻtdim!"), <b>tafsilotlarni</b> esa Past Simple bilan davom ettirasiz ("Kecha
  tayyorlandim, ertalab bordim..."). Suhbat va insho yozishda shu tartib sizni juda
  tabiiy koʻrsatadi.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have seen this film last week.</s></p>
  <p class="pe-good">I <b>saw</b> this film last week.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>When have you finished school?</s></p>
  <p class="pe-good"><b>When did you finish</b> school?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I didn't see him this week.</s></p>
  <p class="pe-good">I <b>haven't seen</b> him this week. <em>(the week isn't over)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did you ever visit Khiva?</s></p>
  <p class="pe-good"><b>Have you ever visited</b> Khiva? <em>(life experience)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My grandfather has died in 2010.</s></p>
  <p class="pe-good">My grandfather <b>died</b> in 2010.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>I <span class="pe-blank">?</span> (finish) my homework, so I can watch TV
     now.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>have finished</strong> — no past time is named, and the present result (I am
         free now) is the whole point.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>Sherbek <span class="pe-blank">?</span> (buy) a new bike two weeks
     ago.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>bought</strong> — <em>two weeks ago</em> is a finished past time, and that
         beats everything else.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Both gaps: <em>I <span class="pe-blank">?</span> (lose) my phone! I
     <span class="pe-blank">?</span> (leave) it on the bus this morning.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>have lost … left.</strong> The news comes first in the Present Perfect, then
         the finished detail in the Past Simple. That is the news pattern.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Why is this wrong? <em>I have visited my aunt yesterday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because "yesterday" is a finished time.</strong> The Present Perfect refuses
         to name a finished moment: <em>I <b>visited</b> my aunt yesterday.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Explain the difference: <em>(a) Have you seen my keys? (b) Did you see my keys?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I am looking for them right now</strong> — the result matters.
         <strong>(b) I am asking about a particular past moment</strong>, for example
         "when you were in my room this morning".</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Finished time</b><span>tugagan vaqt</span></li>
  <li><b>Unfinished period</b><span>tugamagan davr</span></li>
  <li><b>Signal word</b><span>ishora soʻz</span></li>
  <li><b>Life experience</b><span>hayotiy tajriba</span></li>
  <li><b>So far</b><span>hozirgacha</span></li>
  <li><b>Recently</b><span>yaqinda</span></li>
  <li><b>Headline</b><span>sarlavha, asosiy xabar</span></li>
  <li><b>Details</b><span>tafsilotlar</span></li>
  <li><b>To score</b><span>gol urmoq</span></li>
  <li><b>Just in time</b><span>ayni vaqtida</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>A <b>finished past time</b> in the sentence → Past Simple. This rule beats all
        others.</li>
    <li><b>When …?</b> is always Past Simple.</li>
    <li>Result now · life experience · unfinished period → <b>Present Perfect</b>.</li>
    <li><em>today, this week</em> = not over → Perfect · <em>yesterday, last week</em> = over
        → Simple.</li>
    <li>News pattern: <b>headline in the Perfect, details in the Simple</b>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
