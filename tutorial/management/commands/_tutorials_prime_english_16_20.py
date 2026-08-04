# -*- coding: utf-8 -*-
"""Prime English — end of Block A (16–18) and start of Block B (19–20).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_16_20.py --author=prime
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
        "title": "PE-16: Prepositions of Place: in, on, at",
        "category": "english",
        "order": 16,
        "summary": (
            "Three tiny words that Uzbek covers with one ending. Learn the zoom logic — at a "
            "point, on a surface, in a space — and the phrases you must simply know."
        ),
        "stories": ["The Shop on the Corner"],
        "content": """
<h2>PE-16: Prepositions of Place: in, on, at</h2>

<p>Uzbek is generous here: <em>stol<b>da</b></em>, <em>xona<b>da</b></em>,
<em>bekat<b>da</b></em> — one ending, <b>-da</b>, does all the work. English makes you choose
between <b>in</b>, <b>on</b> and <b>at</b> every single time. The good news is that the choice
follows a picture, and once you see the picture you stop guessing.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The zoom logic: <b>at</b> = a point, <b>on</b> = a surface, <b>in</b> = inside a space</li>
    <li>The fixed phrases every learner needs (<em>at home, on the left, in bed</em>)</li>
    <li>Why you travel <b>in</b> a car but <b>on</b> a bus</li>
    <li>The other place words: <em>under, between, next to, in front of, opposite</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The zoom logic</span>
  <span class="pe-chip pe-chip--s">at = a point</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">on = a surface</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">in = inside</span>
</div>

<h3>1. The three pictures</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">at</span>a point on the map</p>
    <p>Where exactly? <em>at the door, at the bus stop, at the corner, at the top of the page</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">on</span>touching a surface or a line</p>
    <p><em>on the table, on the wall, on the floor, on the second floor, on the left</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">in</span>inside something with walls or edges</p>
    <p><em>in the box, in the room, in the garden, in Tashkent, in Uzbekistan</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The keys are <b>on</b> the table, the money is <b>in</b> my bag, and
     Jasur is waiting <b>at</b> the gate.</p>
  <p class="pe-ex__uz">Kalitlar stolda, pul sumkamda, Jasur esa darvoza oldida kutyapti.</p>
  <p class="pe-ex__why">Three "-da" in Uzbek, three different prepositions in English.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada <b>-da</b> qoʻshimchasi uchalasini ham qoplaydi, shuning uchun tarjima qilib
  topib boʻlmaydi. Yechim: <b>soʻzni yolgʻiz emas, ibora bilan yodlang</b> — <em>at
  school</em>, <em>on the wall</em>, <em>in bed</em>. Bitta soʻz emas, butun boʻlakni
  xotirangizga oling.
</div>

<h3>2. Cities, buildings, and the "point vs inside" pair</h3>

<p>Big places (cities, countries) are always <b>in</b>. A building can be either, and the
choice tells your listener what you mean.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">at = the place as an address / activity</p>
    <ul>
      <li>I'll meet you <b>at</b> the cinema. <em>(the meeting point)</em></li>
      <li>She is <b>at</b> school. <em>(studying)</em></li>
      <li>He is <b>at</b> work.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">in = physically inside the walls</p>
    <ul>
      <li>It's raining, so we are <b>in</b> the cinema.</li>
      <li>The chairs are <b>in</b> the school.</li>
      <li>He is <b>in</b> his office.</li>
    </ul>
  </div>
</div>

<p>Some very common phrases drop the article completely (remember PE-4): <b>at home, at
school, at work, at university, in bed, in hospital, in prison</b>.</p>

<h3>3. Transport: in or on?</h3>

<p>The rule is beautifully practical: if you can <b>stand up and walk around</b> inside it,
use <b>on</b>. If you have to sit down and stay there, use <b>in</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>on</b> a bus, <b>on</b> a train, <b>on</b> a plane, <b>on</b> a bike,
     <b>on</b> a horse — but <b>in</b> a car, <b>in</b> a taxi.</p>
  <p class="pe-ex__uz">Avtobusda, poyezdda, samolyotda, velosipedda — lekin mashinada,
     taksida.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Transport qoidasi: ichida <b>yurib ketish mumkin boʻlsa</b> — <b>on</b> (avtobus, poyezd,
  samolyot). <b>Oʻtirib qolasiz</b>, yurolmaysiz — <b>in</b> (mashina, taksi). Velosiped va
  ot ustiga <b>minib</b> olinadi, shuning uchun ular ham <b>on</b>. Bitta qoida — oʻnta ibora.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>at home</b>, <b>at school</b>, <b>at work</b>, <b>in bed</b> — bu iboralarda artikl
  <b>umuman qoʻyilmaydi</b> (PE-4 ni eslang). <s>at the home</s>, <s>in the bed</s> deyish —
  juda tez-tez uchraydigan xato. Bu iboralar joyni emas, <b>holatni</b> bildiradi: "uyda",
  "oʻqishda", "ishda", "uxlab yotgan".
</div>

<h3>4. The other place words</h3>

<ul>
  <li><b>under</b> — ostida: <em>The ball is under the bed.</em></li>
  <li><b>over / above</b> — ustida (tegmasdan): <em>A lamp hangs above the table.</em></li>
  <li><b>between</b> (two) / <b>among</b> (many): <em>between Ali and Vali</em>,
      <em>among the trees</em></li>
  <li><b>next to / beside</b> — yonida · <b>near</b> — yaqinida</li>
  <li><b>in front of</b> — oldida ≠ <b>opposite</b> — roʻparasida</li>
  <li><b>behind</b> — orqasida</li>
</ul>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona sits <b>next to</b> me, <b>in front of</b> the window, and
     <b>opposite</b> the door.</p>
  <p class="pe-ex__uz">Afsona yonimda, deraza oldida va eshikning roʻparasida oʻtiradi.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  <b>In front of</b> and <b>opposite</b> are not the same. <em>In front of</em> = on the front
  side of something, facing the same way. <em>Opposite</em> = on the other side, facing you.
  A car parks <em>in front of</em> the house; the bank is <em>opposite</em> the school.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I live at Samarkand.</s></p>
  <p class="pe-good">I live <b>in</b> Samarkand. <em>(cities are always "in")</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We went to school on the car.</s></p>
  <p class="pe-good">We went to school <b>in</b> the car / <b>by</b> car.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The picture is in the wall.</s></p>
  <p class="pe-good">The picture is <b>on</b> the wall. <em>(a surface)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She is in the home.</s></p>
  <p class="pe-good">She is <b>at home</b>. <em>(fixed phrase, no article)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My room is in the third floor.</s></p>
  <p class="pe-good">My room is <b>on</b> the third floor.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     in / on / at: <em>Sherbek is waiting <span class="pe-blank">?</span> the bus stop
     <span class="pe-blank">?</span> the corner of our street.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>at … at.</strong> Both are exact points on the map, not surfaces or
         containers.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Why <em>in a car</em> but <em>on a bus</em>?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because you can stand up and walk on a bus.</strong> Vehicles you can move
         around in take <b>on</b>; vehicles where you stay seated take <b>in</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) The children are at school. (b) The children are in the
     school.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) They are studying</strong> — the normal meaning.
         <strong>(b) They are physically inside the building</strong>, perhaps at night, or
         sheltering from rain.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>My books are in the shelf, and my bag is in the floor.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My books are on the shelf, and my bag is on the floor.</strong></p>
      <p>Both are flat surfaces you put things on. <em>(Oʻzbekcha: ikkalasi ham yuza,
         shuning uchun <b>on</b>.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Describe where you are sitting, using three different prepositions.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I am sitting <b>at</b> my desk, <b>in</b> my room. My
         phone is <b>on</b> the table, <b>next to</b> my books, and my bag is
         <b>under</b> the chair.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Preposition</b><span>predlog</span></li>
  <li><b>Surface</b><span>yuza</span></li>
  <li><b>Point</b><span>nuqta</span></li>
  <li><b>Inside</b><span>ichida</span></li>
  <li><b>Under</b><span>ostida</span></li>
  <li><b>Between</b><span>orasida</span></li>
  <li><b>Next to</b><span>yonida</span></li>
  <li><b>In front of</b><span>oldida</span></li>
  <li><b>Opposite</b><span>roʻparasida</span></li>
  <li><b>Behind</b><span>orqasida</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>at</b> = a point · <b>on</b> = a surface or line · <b>in</b> = inside a space.</li>
    <li>Cities and countries: always <b>in</b>. Floors and streets: <b>on</b>.</li>
    <li>Fixed phrases have no article: <b>at home, at school, at work, in bed</b>.</li>
    <li>Transport: <b>on</b> if you can walk around, <b>in</b> if you stay seated.</li>
    <li>Learn prepositions inside whole phrases, never as single words.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-17: Prepositions of Time: in, on, at",
        "category": "english",
        "order": 17,
        "summary": (
            "The same three words, a new logic: at for clock times, on for days and dates, in "
            "for longer periods — and the time words that take no preposition at all."
        ),
        "stories": ["On Sunday, in April, at Nine"],
        "content": """
<h2>PE-17: Prepositions of Time: in, on, at</h2>

<p>Same three little words as the last lesson, completely different job. This time they do not
draw a map — they draw a <b>calendar</b>. And there is a very neat way to remember them: they
zoom <em>outwards</em>, from the smallest slice of time to the biggest.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The zoom-out logic: <b>at</b> a moment → <b>on</b> a day → <b>in</b> a long period</li>
    <li>The exact phrases for clock times, days, dates, months, seasons and years</li>
    <li>The time words that take <b>no preposition</b> — a very common mistake</li>
    <li>The special cases: <em>at night, in the morning, on Monday morning</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Zooming out</span>
  <span class="pe-chip pe-chip--s">at 7 o'clock</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">on Monday</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">in May / in 2026</span>
</div>

<h3>1. AT — a point in time</h3>

<p>Use <b>at</b> for exact clock times and for short moments the whole culture treats as one
point.</p>

<div class="pe-ex">
  <p class="pe-ex__en">The lesson starts <b>at</b> 8:30. I go to bed <b>at</b> midnight.
     We don't study <b>at</b> night.</p>
  <p class="pe-ex__uz">Dars 8:30 da boshlanadi. Men yarim tunda uxlayman. Kechasi
     oʻqimaymiz.</p>
</div>

<p>The full <b>at</b> family: <em>at 5 o'clock, at noon, at midnight, at night, at lunchtime,
at the moment, at the same time, at the weekend</em> (British), <em>at Navruz</em>.</p>

<h3>2. ON — a day or a date</h3>

<div class="pe-ex">
  <p class="pe-ex__en">We have English <b>on</b> Monday. My birthday is <b>on</b> 12 March.
     She was born <b>on</b> a cold winter day.</p>
  <p class="pe-ex__uz">Dushanba kuni ingliz tili bor. Tugʻilgan kunim 12-mart. U sovuq qish
     kunida tugʻilgan.</p>
  <p class="pe-ex__why">If the word "day" is anywhere inside the idea, <b>on</b> is your
     preposition.</p>
</div>

<p>That includes days plus a part of the day: <b>on Monday morning</b>, <b>on Friday
evening</b> — the day wins over the part.</p>

<h3>3. IN — a longer period</h3>

<div class="pe-ex">
  <p class="pe-ex__en">It's hot <b>in</b> July. We met <b>in</b> 2019. Birds sing
     <b>in</b> spring. I study <b>in</b> the evening.</p>
  <p class="pe-ex__uz">Iyulda issiq. Biz 2019-yilda tanishganmiz. Bahorda qushlar sayraydi.
     Men kechqurun oʻqiyman.</p>
</div>

<p>The <b>in</b> family: months, years, centuries, seasons, and the three parts of the day —
<em>in the morning, in the afternoon, in the evening</em>. <b>In</b> also means "after this
much time": <em>The film starts <b>in</b> ten minutes.</em></p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Look at this odd family: <b>in</b> the morning, <b>in</b> the afternoon, <b>in</b> the
  evening — but <b>at</b> night. Night is the exception, and you simply have to remember it.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda ham oʻzbekchada bitta <b>-da</b> ishlaydi: <em>soat yetti<b>da</b></em>,
  <em>dushanba<b>da</b></em>, <em>may<b>da</b></em>. Ingliz tilida esa <b>oʻlchamga</b>
  qarang: aniq daqiqa — <b>at</b>, kun yoki sana — <b>on</b>, oy/yil/fasl — <b>in</b>.
  Kichikdan kattaga: <b>at → on → in</b>.
</div>

<h3>4. The zero preposition — this is where marks are lost</h3>

<p>Some time words already contain the idea of "when", so English adds <b>no preposition at
all</b>. Putting one in is one of the most frequent learner mistakes.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✗ Never use in / on / at with…</p>
    <ul>
      <li><b>this</b> week, <b>this</b> morning</li>
      <li><b>next</b> month, <b>next</b> year</li>
      <li><b>last</b> night, <b>last</b> summer</li>
      <li><b>every</b> day, <b>every</b> Sunday</li>
      <li><b>yesterday</b>, <b>today</b>, <b>tomorrow</b></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✓ How they look in a sentence</p>
    <ul>
      <li>I saw him <b>last night</b>.</li>
      <li>We have a test <b>next week</b>.</li>
      <li>She calls me <b>every evening</b>.</li>
      <li>I'll finish it <b>tomorrow</b>.</li>
      <li>He arrived <b>this morning</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu tuzoq oʻzbek tilidan keladi: biz "kelasi hafta<b>da</b>", "oʻtgan kecha<b>si</b>"
  deymiz — qoʻshimcha bor. Shuning uchun <s>in next week</s>, <s>at last night</s> deb yozib
  qoʻyish juda oson. Ingliz tilida <b>next, last, this, every, tomorrow, yesterday</b>
  soʻzlaridan oldin predlog <b>umuman qoʻyilmaydi</b>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oy va sanani adashtirmang: <b>oyning oʻzi</b> — <em><b>in</b> May</em> ("mayda"), lekin
  <b>aniq sana</b> — <em><b>on</b> 5 May</em> ("5-mayda"). Yil ham <b>in</b> bilan:
  <em><b>in</b> 2026</em>. Qoida oddiy: sana kun hisoblanadi, kun esa doim <b>on</b>.
</div>

<h3>5. Two more you will need soon</h3>

<ul>
  <li><b>from … to / until</b> — <em>We study <b>from</b> 8 <b>to</b> 2.</em></li>
  <li><b>before / after</b> — <em>I do my homework <b>after</b> dinner.</em></li>
  <li><b>during</b> + a noun — <em><b>During</b> the lesson we spoke only English.</em></li>
  <li><b>for</b> + how long — <em>I studied <b>for</b> two hours.</em> (full lesson: PE-33)</li>
</ul>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Two easy sound checks. <b>in</b> ten minutes = from now, in the future. <b>for</b> ten
  minutes = how long it lasted. <em>"I'll be ready in ten minutes"</em> ≠ <em>"I waited for
  ten minutes."</em>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I will visit you in next week.</s></p>
  <p class="pe-good">I will visit you <b>next week</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We have a test in Monday.</s></p>
  <p class="pe-good">We have a test <b>on</b> Monday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My birthday is at May.</s></p>
  <p class="pe-good">My birthday is <b>in</b> May. <em>(but: <b>on</b> 5 May)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I don't sleep in night.</s></p>
  <p class="pe-good">I don't sleep <b>at night</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She came at last Friday.</s></p>
  <p class="pe-good">She came <b>last Friday</b>.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     in / on / at: <em>The concert is <span class="pe-blank">?</span> Saturday
     <span class="pe-blank">?</span> 7 p.m., <span class="pe-blank">?</span> September.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>on … at … in.</strong> A day → <b>on</b>, a clock time → <b>at</b>, a month
         → <b>in</b>. All three in one sentence, zooming from day to hour to month.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>I'm going to Bukhara in next Sunday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'm going to Bukhara next Sunday.</strong></p>
      <p><em>Next</em> already tells us when, so no preposition is used.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Fill in: <em>I study <span class="pe-blank">?</span> the evening, but I never study
     <span class="pe-blank">?</span> night.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>in … at.</strong> Parts of the day take <b>in</b> — except <em>night</em>,
         which is the one exception in the family.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What's the difference? <em>(a) I'll come in an hour. (b) I waited for an hour.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) after one hour from now</strong> (bir soatdan keyin).
         <strong>(b) how long the waiting lasted</strong> (bir soat davomida).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Choose: <em>We usually visit our grandparents <span class="pe-blank">?</span> Sunday
     morning.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>on</strong> — when a part of the day is attached to a named day, the day
         wins: <em>on Sunday morning</em>, not <s>in Sunday morning</s>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Preposition of time</b><span>payt predlogi</span></li>
  <li><b>Clock time</b><span>soat vaqti</span></li>
  <li><b>Date</b><span>sana</span></li>
  <li><b>Season</b><span>fasl</span></li>
  <li><b>Century</b><span>asr</span></li>
  <li><b>At night</b><span>kechasi</span></li>
  <li><b>At the weekend</b><span>dam olish kunlari</span></li>
  <li><b>During</b><span>davomida</span></li>
  <li><b>Until</b><span>gacha</span></li>
  <li><b>Zero preposition</b><span>predlogsiz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>at</b> a clock time · <b>on</b> a day or date · <b>in</b> a month, season or year.</li>
    <li>If a named day is involved, <b>on</b> wins: <em>on Monday morning</em>.</li>
    <li>Parts of the day take <b>in</b> — except <b>at night</b>.</li>
    <li><b>No preposition</b> with <em>this, next, last, every, today, tomorrow,
        yesterday</em>.</li>
    <li><b>in</b> ten minutes = from now · <b>for</b> ten minutes = how long.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-18: Question Words: who, what, where, when, why, how",
        "category": "english",
        "order": 18,
        "summary": (
            "Six words that open any conversation, the word order that must follow them, and "
            "the English habit of leaving the preposition at the end."
        ),
        "stories": ["Twenty Questions"],
        "content": """
<h2>PE-18: Question Words: who, what, where, when, why, how</h2>

<p>A person who can ask questions can hold a conversation with anybody, in any country. Six
words do almost all of the work in English — and they all follow one word order. There is only
one genuinely strange thing about English questions, and it comes at the very end of the
sentence. Let's get to it.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What each question word asks for</li>
    <li>The fixed order: <b>Wh- + helper + subject + verb</b></li>
    <li>The <b>How + adjective</b> family: how old, how many, how far, how often</li>
    <li>Why English says <em>"Who are you waiting <b>for</b>?"</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The order that never changes</span>
  <span class="pe-chip pe-chip--adv">Wh- word</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">helper</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
  <span class="pe-op">?</span>
</div>

LEGEND_HERE

<h3>1. The six words</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>who — kim</p>
    <p><em>Who is your teacher?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>what — nima</p>
    <p><em>What do you want?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>where — qayerda</p>
    <p><em>Where do they live?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>when — qachon</p>
    <p><em>When does the film start?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>why — nima uchun</p>
    <p><em>Why are you late?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">6</span>how — qanday</p>
    <p><em>How do you go to school?</em></p>
  </div>
</div>

<p>Three more join the family often: <b>whose</b> (kimning), <b>which</b> (qaysi biri, from a
limited choice) and <b>whom</b> (formal object form, rare in speech).</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Whose</b> bag is this? — <b>Which</b> do you prefer, tea or coffee?</p>
  <p class="pe-ex__uz">Bu kimning sumkasi? — Qaysi birini afzal koʻrasan, choymi yoki qahva?</p>
  <p class="pe-ex__why"><b>What</b> = open choice from everything; <b>which</b> = choice from
     a small known group.</p>
</div>

<h3>2. The word order</h3>

<p>You already built this in PE-10 — the question word simply goes in front of the question
you already know how to make.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--adv">Where</span>
     <span class="pe-hl pe-hl--aux">does</span>
     <span class="pe-hl pe-hl--s">your sister</span>
     <span class="pe-hl pe-hl--v">work</span>?</p>
  <p class="pe-ex__uz">Opangiz qayerda ishlaydi?</p>
</div>

<p>With <em>to be</em> and other helpers there is no <em>do/does</em> — the helper itself
jumps in front of the subject:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Why are</b> you sad? <b>Where is</b> my pen? <b>What are</b> they
     doing?</p>
  <p class="pe-ex__uz">Nega xafasan? Ruchkam qayerda? Ular nima qilishyapti?</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada soʻroq soʻzi gapning oʻrtasida ham turishi mumkin: "Sen <b>qayerda</b>
  yashaysan?" Ingliz tilida esa u <b>doim birinchi</b> boʻladi va undan keyin <b>yordamchi
  feʼl</b> keladi: <em><b>Where do</b> you live?</em> <s>Where you live?</s> — bu eng
  koʻp uchraydigan xato.
</div>

<h3>3. The How family</h3>

<p><b>How</b> is the most productive question word: put an adjective after it and you get a
new question.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Question</th><th>Asks about</th><th>Example</th></tr>
  <tr><td>How old</td><td>age</td><td>How old are you?</td></tr>
  <tr><td>How many</td><td>countable number</td><td>How many brothers have you got?</td></tr>
  <tr><td>How much</td><td>uncountable / price</td><td>How much water? How much is it?</td></tr>
  <tr><td>How long</td><td>length of time</td><td>How long does it take?</td></tr>
  <tr><td>How often</td><td>frequency</td><td>How often do you swim?</td></tr>
  <tr><td>How far</td><td>distance</td><td>How far is the school?</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>How many</b> pupils are there in your class? — <b>How much</b>
     does this book cost?</p>
  <p class="pe-ex__uz">Sinfingizda nechta oʻquvchi bor? — Bu kitob qancha turadi?</p>
  <p class="pe-ex__why">The countable/uncountable rule from PE-2 comes back here.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>How many</b> va <b>how much</b> orasidagi farq oʻzbekchada ham bor: <em><b>nechta</b>
  kitob?</em> (sanaladigan) va <em><b>qancha</b> suv?</em> (sanalmaydigan). Shuning uchun
  "nechta" desangiz — <b>how many</b>, "qancha" desangiz — <b>how much</b>. Narx soʻraganda
  ham <b>how much</b>: <em>How much is it?</em>
</div>

<h3>4. Where the preposition goes</h3>

<p>Here is the genuinely English habit. When a question needs a preposition, everyday English
leaves it <b>at the end</b> of the sentence, far from its question word.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Natural English</p>
    <ul>
      <li><b>Who</b> are you waiting <b>for</b>?</li>
      <li><b>What</b> are you thinking <b>about</b>?</li>
      <li><b>Who</b> did you go <b>with</b>?</li>
      <li><b>Where</b> are you <b>from</b>?</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Very formal (writing only)</p>
    <ul>
      <li><b>For whom</b> are you waiting?</li>
      <li><b>About what</b> are you thinking?</li>
      <li><b>With whom</b> did you go?</li>
      <li>—</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada koʻmakchi soʻz bilan birga turadi: "<b>Kim bilan</b> bording?" Ingliz tilida esa
  u <b>gap oxiriga</b> tashlanadi: "<b>Who</b> did you go <b>with</b>?" Bu gʻalati tuyuladi,
  lekin aynan shu — jonli ingliz tili. "Qayerdansan?" ham shunday: <em>Where are you
  <b>from</b>?</em>
</div>

<h3>5. Two traps</h3>

<p><b>Subject questions.</b> If <em>who</em> or <em>what</em> is the subject, drop the helper
(PE-10): <em><b>Who wants</b> tea?</em>, not <s>Who does want tea?</s></p>

<p><b>What does … mean?</b> Uzbek says "Bu soʻz nima <b>degani</b>?", which pushes learners
into <s>What means this word?</s> English needs the full structure:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>What means "attitude"?</s></p>
  <p class="pe-good"><b>What does "attitude" mean?</b></p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Where you are going?</s></p>
  <p class="pe-good"><b>Where are you</b> going?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Why you didn't call me?</s></p>
  <p class="pe-good"><b>Why didn't you</b> call me?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How much brothers have you got?</s></p>
  <p class="pe-good"><b>How many</b> brothers have you got?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How old you are?</s></p>
  <p class="pe-good"><b>How old are you?</b></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>With who you went to the cinema?</s></p>
  <p class="pe-good"><b>Who did you go to the cinema with?</b></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make a question for this answer: <em>— … ? — I go to school by bus.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>How do you go to school?</strong> The answer describes the manner, so the
         question word is <em>how</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>What means this sentence?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>What does this sentence mean?</strong></p>
      <p><em>Mean</em> is an ordinary verb, so it needs the helper <b>does</b>, and the
         subject comes between them.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     how many / how much: <em>___ money do you need? ___ books did you buy?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>How much money … How many books.</strong> <em>Money</em> is uncountable
         (PE-2), <em>books</em> are countable.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Ask about the underlined part: <em>Afsona is talking to <u>her cousin</u>.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Who is Afsona talking to?</strong></p>
      <p>The preposition <em>to</em> stays at the end — that is normal English.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which needs no helper, and why? <em>(a) Who ___ you invite? (b) Who ___ the window?</em>
     (broke)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) Who broke the window?</strong> — <em>who</em> is the subject, so no
         helper. In (a) you are the subject, so: <em>Who <b>did</b> you invite?</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Question word</b><span>soʻroq soʻzi</span></li>
  <li><b>Whose</b><span>kimning</span></li>
  <li><b>Which</b><span>qaysi biri</span></li>
  <li><b>How far</b><span>qanchalik uzoq</span></li>
  <li><b>How long</b><span>qancha vaqt</span></li>
  <li><b>Distance</b><span>masofa</span></li>
  <li><b>To mean</b><span>maʼno anglatmoq</span></li>
  <li><b>To prefer</b><span>afzal koʻrmoq</span></li>
  <li><b>Manner</b><span>usul, tarz</span></li>
  <li><b>Formal</b><span>rasmiy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Order: <b>Wh- + helper + subject + verb?</b> The Wh- word is always first.</li>
    <li>With <b>to be</b>, no <em>do/does</em>: <b>Where is he?</b>, <b>Why are you late?</b></li>
    <li><b>How</b> + adjective builds a whole family: <em>how old, how many, how far</em>.</li>
    <li>The preposition goes to the <b>end</b>: <em>Who are you waiting for?</em></li>
    <li>If <b>who/what</b> is the subject, use no helper: <em>Who broke it?</em></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-19: Past Simple of \"to be\": was / were",
        "category": "english",
        "order": 19,
        "summary": (
            "Your first step into the past. Only two forms to learn — was and were — plus "
            "there was / there were and the time words that send a sentence backwards."
        ),
        "stories": ["It Was Only a Photo"],
        "content": """
<h2>PE-19: Past Simple of "to be": was / were</h2>

<p>Everything you have learned so far lives in the present. From this lesson, Prime English
turns towards the past — and English gives you a gentle first step, because the past of
<b>to be</b> has only <b>two forms</b> in the whole language: <b>was</b> and <b>were</b>.
Learn those two words and you can already talk about yesterday.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Which subjects take <b>was</b> and which take <b>were</b></li>
    <li>Negatives (<b>wasn't / weren't</b>) and questions — no helper verb needed</li>
    <li><b>There was / There were</b> for describing the past</li>
    <li>The time expressions that tell you a sentence is in the past</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Past of "to be"</span>
  <span class="pe-chip pe-chip--s">I / he / she / it</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">was</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">you / we / they</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">were</span>
</div>

LEGEND_HERE

<h3>1. The picture: a finished point in the past</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:72%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:28%"></span>
    <span class="pe-tl-tag" style="left:28%">I was at home</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The moment is finished and it does not touch the present. That is why the Past Simple always
comes with a time word like <em>yesterday</em> or <em>last night</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">was</span> at home yesterday, but
     <span class="pe-hl pe-hl--s">my parents</span>
     <span class="pe-hl pe-hl--v">were</span> at work.</p>
  <p class="pe-ex__uz">Kecha men uyda edim, ota-onam esa ishda edilar.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Was / were</b> — bu oʻzbekchadagi <b>edi</b> soʻzi: <em>Men uyda <b>edim</b></em> =
  <em>I <b>was</b> at home</em>. Yaxshi xabar: oʻzbekchada shaxsga qarab "edim / eding /
  edi" oʻzgaradi, ingliz tilida esa faqat <b>ikkita</b> shakl bor — <b>was</b> va
  <b>were</b>. Buni yodlash juda oson.
</div>

<h3>2. Which one goes where</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">was — the singular ones</p>
    <ul>
      <li>I <b>was</b> tired.</li>
      <li>He / She / It <b>was</b> late.</li>
      <li>Jasur <b>was</b> at school.</li>
      <li>The weather <b>was</b> cold.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">were — the plural ones + you</p>
    <ul>
      <li>You <b>were</b> right.</li>
      <li>We / They <b>were</b> happy.</li>
      <li>My friends <b>were</b> here.</li>
      <li>The shops <b>were</b> closed.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>I was</b>, but <b>you were</b> — even when "you" means one person. English has used the
  plural form for "you" for 400 years, so <s>you was</s> is always wrong.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng koʻp uchraydigan xato — <s>you was</s>. Oʻzbekchada "sen ed<b>ing</b>" birlik, shuning
  uchun ingliz tilida ham birlik shakl qoʻyilib yuboriladi. Ammo <b>you</b> soʻzi bilan
  <b>doim were</b> ishlatiladi — bitta odamga aytilsa ham: <em>You <b>were</b> right,
  Jasur.</em>
</div>

<h3>3. Negatives and questions</h3>

<p>Exactly like the present <em>to be</em> (PE-6): add <b>not</b>, or swap the first two
words. No <em>did</em> anywhere — that helper belongs to other verbs, and you meet it in
PE-22.</p>

<ol class="pe-steps">
  <li><b>Negative:</b> <em>I <b>was not</b> → I <b>wasn't</b>. They <b>were not</b> →
      They <b>weren't</b>.</em></li>
  <li><b>Question:</b> <em><b>Was</b> he at home? <b>Were</b> you tired?</em></li>
  <li><b>Short answers:</b> <em>Yes, I <b>was</b>. / No, I <b>wasn't</b>. Yes, they
      <b>were</b>. / No, they <b>weren't</b>.</em></li>
  <li><b>Wh- questions:</b> <em><b>Where were</b> you last night? <b>Why was</b> she
      angry?</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>Were</b> you at the party? — No, I <b>wasn't</b>. I
     <b>was</b> ill.</p>
  <p class="pe-ex__uz">— Bazmda edingmi? — Yoʻq, edim emas. Kasal edim.</p>
</div>

<h3>4. There was / There were</h3>

<p>The <em>there is / there are</em> structure from PE-7 simply moves into the past. The same
agreement rule applies — the verb matches the noun that follows.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>There was</b> a big tree in our garden, and <b>there were</b> two
     benches under it.</p>
  <p class="pe-ex__uz">Bogʻimizda katta daraxt bor edi va uning tagida ikkita skameyka bor
     edi.</p>
  <p class="pe-ex__why">Singular noun → <em>there was</em>; plural noun → <em>there were</em>.</p>
</div>

<h3>5. Time expressions of the past</h3>

<p>These words are your signal that the sentence must go backwards: <em>yesterday, last night,
last week / month / year, two days ago, in 2019, when I was a child, at that time, in those
days</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>When I was</b> a child, we <b>were</b> very poor, but we
     <b>were</b> happy.</p>
  <p class="pe-ex__uz">Bolaligimda juda kambagʻal edik, lekin baxtli edik.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat: <b>ago</b> soʻzi oʻzbekchadagi "<b>...oldin</b>" ga toʻgʻri keladi va u
  <b>sondan keyin</b> yoziladi: <em>two days <b>ago</b></em> = "ikki kun oldin",
  <s>ago two days</s> emas. Shuningdek <em>last night</em> oldidan predlog qoʻyilmaydi
  (PE-17 ni eslang).
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>You was at school yesterday.</s></p>
  <p class="pe-good">You <b>were</b> at school yesterday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>They was very tired.</s></p>
  <p class="pe-good">They <b>were</b> very tired.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Did you was at the cinema?</s></p>
  <p class="pe-good"><b>Were you</b> at the cinema? <em>(no "did" with "to be")</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I was borned in 2010.</s></p>
  <p class="pe-good">I <b>was born</b> in 2010.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>There were a lot of noise.</s></p>
  <p class="pe-good">There <b>was</b> a lot of noise. <em>(noise is uncountable)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     was / were: <em>Sherbek and I <span class="pe-blank">?</span> at the stadium, but the
     match <span class="pe-blank">?</span> boring.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>were … was.</strong> <em>Sherbek and I</em> = we (plural) → <b>were</b>;
         <em>the match</em> is singular → <b>was</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it a question and a negative: <em>She was at home.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Was she at home? / She wasn't at home.</strong></p>
      <p>Swap for the question, add <em>not</em> for the negative — no <em>did</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     There was / There were: <em>___ many people at the bazaar, but ___ no fruit.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>There were many people … there was no fruit.</strong></p>
      <p><em>People</em> is plural; <em>fruit</em> here is uncountable.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>Where you was last Sunday?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Where were you last Sunday?</strong></p>
      <p>Two fixes: the verb must be <em>were</em> with <em>you</em>, and it must come
         <b>before</b> the subject in a question.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write two sentences about your childhood using <em>was</em> and <em>were</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>When I <b>was</b> seven, my best friend <b>was</b>
         Afsona. We <b>were</b> in the same class and we <b>were</b> always together.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Past Simple</b><span>oʻtgan oddiy zamon</span></li>
  <li><b>Was / were</b><span>edi</span></li>
  <li><b>Yesterday</b><span>kecha</span></li>
  <li><b>Last night</b><span>kecha kechqurun</span></li>
  <li><b>Ago</b><span>...oldin</span></li>
  <li><b>Childhood</b><span>bolalik</span></li>
  <li><b>To be born</b><span>tugʻilmoq</span></li>
  <li><b>At that time</b><span>oʻsha paytda</span></li>
  <li><b>Closed</b><span>yopiq</span></li>
  <li><b>Noise</b><span>shovqin</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>I / he / she / it → was.</b> <b>You / we / they → were.</b> Only two forms.</li>
    <li>Negative: <b>wasn't / weren't</b>. Question: swap the first two words.</li>
    <li><b>Never</b> use <em>did</em> with <em>to be</em>: <s>Did you was?</s> ✗</li>
    <li><b>There was</b> + singular · <b>there were</b> + plural.</li>
    <li><b>I was born</b> — not <s>I was borned</s>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-20: Past Simple: Regular Verbs and the -ed Ending",
        "category": "english",
        "order": 20,
        "summary": (
            "One ending for every person — the past is easier than the present. Includes the "
            "-ed spelling rules and the three sounds that ending can make."
        ),
        "stories": ["The Day the Bakery Opened"],
        "content": """
<h2>PE-20: Past Simple: Regular Verbs and the -ed Ending</h2>

<p>Here is a piece of good news you have earned. In the present tense you had to remember the
<b>-s</b> for <em>he/she/it</em>. In the past, that worry disappears: <mark>every person takes
exactly the same form</mark>. <em>I worked, you worked, he worked, we worked, they worked.</em>
One ending, no exceptions — for regular verbs, which are the large majority.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>How to build the Past Simple of regular verbs</li>
    <li>The four spelling rules for <b>-ed</b></li>
    <li>The three different sounds of <b>-ed</b>: /t/, /d/ and /ɪd/</li>
    <li>The time words that require this tense</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive — the same for everybody</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ed</span>
  <span class="pe-chip pe-chip--opt">(no -s, ever)</span>
</div>

LEGEND_HERE

<h3>1. The picture: finished, and over</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:72%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:22%"></span>
    <span class="pe-tl-tag" style="left:22%">I finished my homework</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The action happened at a definite time in the past and is completely finished. English
almost always names that time — <em>yesterday, last week, in 2020, two hours ago</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--v">finished</span> her homework and
     <span class="pe-hl pe-hl--v">watched</span> a film last night.</p>
  <p class="pe-ex__uz">Afsona kecha kechqurun uy vazifasini tugatdi va kino koʻrdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>-ed</b> qoʻshimchasi oʻzbekchadagi <b>-di</b> ga toʻgʻri keladi: <em>ishla<b>di</b></em> →
  <em>work<b>ed</b></em>. Va mana bu yerda ingliz tili oʻzbek tilidan ham osonroq: oʻzbekchada
  shaxsga qarab "ishladim / ishlading / ishladi" deb oʻzgaradi, ingliz tilida esa
  <b>hamma shaxs uchun bitta shakl</b> — <em>worked</em>.
</div>

<h3>2. The spelling rules</h3>

<ol class="pe-steps">
  <li><b>Most verbs: + ed</b> — <em>work → worked, play → played, open → opened,
      watch → watched</em></li>
  <li><b>Verb already ends in -e: + d only</b> — <em>like → liked, live → lived,
      close → closed, dance → danced</em></li>
  <li><b>Consonant + y → ied</b> — <em>study → studied, carry → carried, try → tried</em>
      (but <em>play → played</em>, because <em>a</em> is a vowel)</li>
  <li><b>Short verb, one vowel + one consonant: double the consonant</b> —
      <em>stop → stopped, plan → planned, travel → travelled</em> (British)</li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Rules 3 and 4 are the same ones you already used for <b>-ing</b> in PE-12 and for the
  present <b>-s</b> in PE-9. You are not learning new rules here — you are reusing rules you
  already own. English spelling is more consistent than it looks.
</div>

<h3>3. The three sounds of -ed</h3>

<p>The spelling is always <b>-ed</b>, but your mouth produces three different sounds. Nobody
needs to memorise lists: your tongue chooses automatically once you notice the pattern.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>/ɪd/ — an extra syllable</p>
    <p>after <b>t</b> or <b>d</b>: <em>wanted, needed, started, decided</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>/t/ — a soft tap</p>
    <p>after voiceless sounds (p, k, f, s, sh, ch): <em>helped, worked, washed, watched</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>/d/ — a buzz</p>
    <p>after everything else: <em>played, opened, lived, called</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>wanted</b> (2 syllables) to help, so I <b>helped</b>
     (1 syllable) and then I <b>called</b> (1 syllable) her.</p>
  <p class="pe-ex__uz">Yordam bermoqchi edim, shuning uchun yordam berdim va keyin unga
     qoʻngʻiroq qildim.</p>
  <p class="pe-ex__why">Only group 1 adds a syllable. <em>Helped</em> is <b>not</b>
     "hel-ped".</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻp oʻquvchilar <em>worked</em> ni "vor-ked", <em>helped</em> ni "help-ed" deb ikki
  boʻgʻin qilib aytadi — bu talaffuzdagi eng sezilarli xato. Faqat <b>t</b> va <b>d</b> bilan
  tugagan feʼllarga qoʻshimcha boʻgʻin qoʻshiladi (<em>want<b>ed</b></em>,
  <em>need<b>ed</b></em>). Qolganlarida <b>-ed</b> bitta tovush boʻlib qoʻshilib ketadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bitta gapda oʻtgan zamon <b>ikki marta</b> koʻrsatilmaydi. Oʻzbekchada "qildim" bitta
  qoʻshimcha oladi — ingliz tilida ham shunday: yordamchi feʼl <b>did</b> boʻlsa, asosiy
  feʼl <b>-ed</b> ni yoʻqotadi. <em>I <b>didn't watch</b></em>, <s>I didn't watched</s>.
  Bu — PE-10 dagi "bitta koptok" qoidasining oʻtgan zamondagi koʻrinishi.
</div>

<h3>4. Not every verb is regular</h3>

<p>About 180 very common English verbs do not take <b>-ed</b> at all — they change their
shape: <em>go → went, see → saw, have → had, come → came</em>. Those are the irregular verbs,
and they get a whole lesson of their own next (PE-21). For now, just be ready: if a verb feels
very common and very short, it is probably irregular.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I goed to the bazaar and buyed some fruit.</s></p>
  <p class="pe-good">Yesterday I <b>went</b> to the bazaar and <b>bought</b> some fruit.</p>
</div>

<h3>5. Time expressions</h3>

<p>These signal the Past Simple: <em>yesterday, last night / week / year, two days ago, in
2015, then, after that, when I was young</em>. Notice that <b>ago</b> comes <b>after</b> the
time: <em>three years <b>ago</b></em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">We <b>moved</b> to this city three years <b>ago</b>, and I
     <b>started</b> at this school last September.</p>
  <p class="pe-ex__uz">Biz bu shaharga uch yil oldin koʻchib keldik, men esa bu maktabda
     oʻtgan sentabrda oʻqiy boshladim.</p>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  Negatives and questions in the past use the helper <b>did</b>, and then the verb loses its
  <b>-ed</b>: <em>I <b>didn't watch</b> TV. <b>Did</b> you <b>watch</b> TV?</em> It is the
  same "one ball" logic as <em>does</em> in PE-10 — and it gets its own lesson in PE-22.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He studyed all evening.</s></p>
  <p class="pe-good">He <b>studied</b> all evening. <em>(consonant + y → ied)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The bus stoped near our house.</s></p>
  <p class="pe-good">The bus <b>stopped</b> near our house. <em>(double the consonant)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She likeed the present.</s></p>
  <p class="pe-good">She <b>liked</b> the present. <em>(the verb already ends in -e)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He worksed yesterday. / They workeds.</s></p>
  <p class="pe-good">He <b>worked</b> yesterday. <em>(never add -s in the past)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I did played football yesterday.</s></p>
  <p class="pe-good">I <b>played</b> football yesterday.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Write the past forms: <em>carry · stop · live · watch · travel</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>carried</strong> (consonant + y), <strong>stopped</strong> (double p),
         <strong>lived</strong> (+d only), <strong>watched</strong> (+ed),
         <strong>travelled</strong> (double l in British English).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Which of these has an extra syllable? <em>helped · wanted · played · decided</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>wanted and decided</strong> — both end in <b>t</b> or <b>d</b>, so
         <b>-ed</b> is pronounced /ɪd/. <em>Helped</em> and <em>played</em> stay one
         syllable.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Put into the past: <em>Jasur plays football and his sister watches him.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur played football and his sister watched him.</strong></p>
      <p>Notice that <em>watches</em> loses its <b>-es</b> completely — in the past there is
         no third-person form.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>Two years ago we moveed to Tashkent and I startd school there.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Two years ago we moved to Tashkent and I started school there.</strong></p>
      <p><em>Move</em> already ends in <b>-e</b> → just add <b>d</b>. <em>Start</em> needs the
         full <b>-ed</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write three sentences about what you did yesterday, using regular verbs only.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Yesterday I <b>walked</b> to school, <b>studied</b>
         English for two hours and <b>helped</b> my mother in the evening.</em></p>
      <p>Check the sounds: <em>walked</em> /t/, <em>studied</em> /d/, <em>helped</em> /t/ —
         no extra syllables.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Regular verb</b><span>qoidali feʼl</span></li>
  <li><b>Irregular verb</b><span>qoidasiz feʼl</span></li>
  <li><b>Past form</b><span>oʻtgan zamon shakli</span></li>
  <li><b>Ending</b><span>qoʻshimcha</span></li>
  <li><b>Syllable</b><span>boʻgʻin</span></li>
  <li><b>Voiceless sound</b><span>jarangsiz tovush</span></li>
  <li><b>To double</b><span>ikkilantirmoq</span></li>
  <li><b>Finished action</b><span>tugallangan ish</span></li>
  <li><b>To move (house)</b><span>koʻchib oʻtmoq</span></li>
  <li><b>To decide</b><span>qaror qilmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>verb + ed</b> — the same form for every person. No <b>-s</b> in the past, ever.</li>
    <li>Spelling: <b>+d</b> after <em>-e</em>, consonant + y → <b>-ied</b>, short verbs
        <b>double</b> the last consonant.</li>
    <li>Sounds: <b>/ɪd/</b> after t/d (extra syllable), <b>/t/</b> after voiceless,
        <b>/d/</b> after the rest.</li>
    <li>Signals: <b>yesterday, last week, in 2015, three years ago</b> — and <b>ago</b> comes
        after the time.</li>
    <li>About 180 common verbs are irregular — that is PE-21.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
