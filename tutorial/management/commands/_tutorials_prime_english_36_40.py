# -*- coding: utf-8 -*-
"""Prime English — Block C, lessons 36–40 (the rest of the Perfect family).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_36_40.py --author=prime
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
        "title": "PE-36: Present Perfect Continuous",
        "category": "english",
        "order": 36,
        "summary": (
            "The tense of visible effort: have been + -ing. For an activity that started in "
            "the past and is still going — or has just stopped and left traces."
        ),
        "stories": ["The Man Who Has Been Planting Trees"],
        "content": """
<h2>PE-36: Present Perfect Continuous</h2>

<p>Your friend walks in with red eyes and a tired face. You ask what happened, and the natural
English answer is not <em>"I studied"</em> — it is <em>"I<b>'ve been studying</b> all
night."</em> This tense puts the spotlight on the <mark>activity itself</mark>: how long it
went on, how much effort it took, and what traces it has left on you right now.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>have / has + been + verb-ing</b></li>
    <li>Two jobs: an activity still going, and one that has just stopped</li>
    <li>How <b>for</b> and <b>since</b> work with it</li>
    <li>Which verbs can never be used in this tense</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">have / has</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">been</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
</div>

LEGEND_HERE

<h3>1. The picture: a long activity reaching now</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:76%"></span>
    <span class="pe-tl-band" style="left:18%;width:58%"></span>
    <span class="pe-tl-tag" style="left:30%">I've been waiting…</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>A long, continuous band that touches NOW. Compare it with PE-32: the Present Perfect Simple
shows you a <b>dot</b> (the completed action) with a result; this one shows you the
<b>line</b> — the activity in progress.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">have been</span>
     <span class="pe-hl pe-hl--v">waiting</span> for two hours!</p>
  <p class="pe-ex__uz">Ikki soatdan beri kutyapman!</p>
  <p class="pe-ex__why">The waiting started two hours ago and I am <em>still</em> waiting.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu zamon oʻzbekchadagi "<b>...dan beri ...yapman</b>" qolipiga juda aniq mos keladi:
  <em>ikki soatdan beri kut<b>yapman</b></em> → <em>I <b>have been waiting</b> for two
  hours</em>. Yaʼni oʻzbekchada "beri" + hozirgi davomli zamon boʻlsa, ingliz tilida
  deyarli doim <b>have been + -ing</b> ishlatiladi.
</div>

<h3>2. Job one: it is still happening</h3>

<p>The activity started in the past and continues at this moment. This is where <b>for</b> and
<b>since</b> (PE-31, PE-33) come back.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>has been studying</b> Korean <b>since</b> January. She
     <b>has been working</b> very hard.</p>
  <p class="pe-ex__uz">Afsona yanvardan beri koreys tilini oʻrganyapti. U juda tirishqoqlik
     bilan ishlayapti.</p>
</div>

<p>The question form asks about duration: <em><b>How long have</b> you <b>been</b> learning
English?</em> — and the answer takes <em>for</em> or <em>since</em>.</p>

<h3>3. Job two: it has just stopped, and I can see the traces</h3>

<p>The activity is over — perhaps a minute ago — but the evidence is in front of you right
now. This is the job learners forget, and it is extremely common in speech.</p>

<div class="pe-ex">
  <p class="pe-ex__en">The ground is wet. It <b>has been raining</b>.</p>
  <p class="pe-ex__uz">Yer hoʻl. Yomgʻir yogʻgan ekan.</p>
  <p class="pe-ex__why">The rain has stopped — but you can still see what it did.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Your hands are dirty! What <b>have</b> you <b>been doing</b>?</p>
  <p class="pe-ex__uz">Qoʻllaring kir! Nima qilayotgan eding?</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  This is the tense of visible causes. When you see a state and want to explain <em>why</em> —
  tired eyes, wet ground, dirty hands, a red face — reach for <b>have been + -ing</b>. It is
  one of the most natural-sounding things a learner can say.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkinchi vazifa oʻzbekchadagi "<b>-gan ekan</b>" shakliga juda yaqin: <em>Yomgʻir
  yogʻ<b>gan ekan</b></em> — yaʼni oʻzim koʻrmadim, lekin izidan bilyapman. Ingliz tilida
  aynan shu maʼno <b>have been + -ing</b> bilan beriladi: <em>It <b>has been raining</b></em>.
  Koʻrinib turgan iz bor — quruq xabar emas.
</div>

<h3>4. Negatives, questions and the three parts</h3>

<ol class="pe-steps">
  <li><b>Negative:</b> <em>I <b>haven't been</b> sleeping well.</em></li>
  <li><b>Question:</b> <em><b>Have</b> you <b>been</b> waiting long?</em></li>
  <li><b>Short answer:</b> <em>Yes, I have. / No, I haven't.</em></li>
  <li><b>Never drop a part:</b> the sentence needs <b>have</b> + <b>been</b> + <b>-ing</b> —
      all three, every time.</li>
</ol>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  The word <b>been</b> is not optional and never changes.
  <s>I have waiting</s> ✗ · <s>I have been wait</s> ✗ · <s>I am waiting since two hours</s> ✗
  → <b>I have been waiting for two hours</b> ✓.
</div>

<h3>5. Verbs that refuse it</h3>

<p>The stative-verb rule from PE-13 is still in force, in every tense. Verbs of knowing,
liking, wanting and belonging cannot take <b>-ing</b>, so they use the Present Perfect Simple
instead.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>I have been knowing him for ten years.</s></p>
  <p class="pe-good">I <b>have known</b> him for ten years.</p>
</div>

<p>The verbs that love this tense are the long, effortful ones: <em>work, study, learn, wait,
live, play, run, read, look for, try, rain, snow, talk</em>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani eslash uchun savol bering: <b>bu ish davom etadigan jarayonmi?</b> "Kutmoq",
  "oʻrganmoq", "ishlamoq" — ha, davom etadi, demak <b>have been -ing</b> boʻladi.
  "Bilmoq", "yoqtirmoq", "ega boʻlmoq" — bu holat, jarayon emas, shuning uchun faqat
  <b>have + V3</b>: <em>I <b>have known</b></em>, <s>I have been knowing</s> emas.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I am living here since 2019.</s></p>
  <p class="pe-good">I <b>have been living</b> here since 2019.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has been work all morning.</s></p>
  <p class="pe-good">She <b>has been working</b> all morning.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How long are you waiting?</s></p>
  <p class="pe-good"><b>How long have you been waiting?</b></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>They have been played football since two hours.</s></p>
  <p class="pe-good">They <b>have been playing</b> football <b>for</b> two hours.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I have been wanting a new phone for a year.</s></p>
  <p class="pe-good">I <b>have wanted</b> a new phone for a year.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>Sherbek is very tired. He <span class="pe-blank">?</span> (run) for an
     hour.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>has been running</strong> — his tiredness is the visible trace of a long
         activity.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>I am learning English since five years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I have been learning English for five years.</strong></p>
      <p>Two fixes: the tense (<em>am learning</em> → <em>have been learning</em>) and
         <em>since</em> → <em>for</em>, because five years is a length.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Explain the situation: <em>Her eyes are red. She has been crying.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The crying has stopped, but the red eyes remain.</strong> This is job two:
         a recently finished activity with visible traces.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which is wrong, and why? <em>(a) I've been having a bike since 2020. (b) I've had a bike
     since 2020.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) is wrong.</strong> Here <em>have</em> means "own" — a state, not an
         activity — so it cannot take <b>-ing</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Answer about yourself: <em>How long have you been studying at your school?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I<b>'ve been studying</b> at this school <b>for</b> six
         years</em> / <em><b>since</b> the first form.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Present Perfect Continuous</b><span>hozirgi tugallangan davomli zamon</span></li>
  <li><b>Activity</b><span>faoliyat, jarayon</span></li>
  <li><b>Duration</b><span>davomiylik</span></li>
  <li><b>Trace / evidence</b><span>iz, belgi</span></li>
  <li><b>To last</b><span>davom etmoq</span></li>
  <li><b>Effort</b><span>harakat, mehnat</span></li>
  <li><b>To look for</b><span>qidirmoq</span></li>
  <li><b>To cry</b><span>yigʻlamoq</span></li>
  <li><b>Wet</b><span>hoʻl</span></li>
  <li><b>Dirty</b><span>kir, iflos</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>have / has + been + verb-ing</b> — all three parts, always.</li>
    <li>Job 1: an activity that started earlier and is <b>still going</b>.</li>
    <li>Job 2: an activity that has <b>just stopped</b> and left visible traces.</li>
    <li>Uzbek "<b>...dan beri ...yapman</b>" is your signal for this tense.</li>
    <li>Stative verbs (<b>know, have, like, want</b>) never take it.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-37: Present Perfect Simple vs Continuous",
        "category": "english",
        "order": 37,
        "summary": (
            "Finished result or ongoing activity? How many or how long? One question separates "
            "'I've painted the kitchen' from 'I've been painting the kitchen'."
        ),
        "stories": ["Somebody Has Been Eating My Plov"],
        "content": """
<h2>PE-37: Present Perfect Simple vs Continuous</h2>

<p>Two sentences, one afternoon: <em>"I<b>'ve painted</b> the kitchen"</em> and
<em>"I<b>'ve been painting</b> the kitchen."</em> The first invites you to come and look — the
job is done. The second explains why there is paint in my hair. Same past, same present,
completely different focus: <mark>the result, or the activity</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The core split: <b>result</b> vs <b>activity</b></li>
    <li><b>How many</b> → Simple · <b>How long</b> → Continuous</li>
    <li>When both are correct and the difference disappears</li>
    <li>The verbs that only allow the Simple</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The question to ask yourself</span>
  <span class="pe-chip pe-chip--s">What is finished?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">have + V3</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">What have I been busy with?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">have been + -ing</span>
</div>

<h3>1. Result or activity?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Simple — look at the result</p>
    <ul>
      <li>I<b>'ve painted</b> the kitchen. <em>(it's finished — come and see)</em></li>
      <li>She<b>'s written</b> three emails.</li>
      <li>We<b>'ve eaten</b> all the bread.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Continuous — look at the activity</p>
    <ul>
      <li>I<b>'ve been painting</b> the kitchen. <em>(that's why I'm dirty)</em></li>
      <li>She<b>'s been writing</b> emails all morning.</li>
      <li>We<b>'ve been eating</b> — that's why we're late.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Jasur <b>has read</b> that book. — Jasur <b>has been reading</b> that
     book.</p>
  <p class="pe-ex__uz">Jasur u kitobni oʻqib chiqdi. — Jasur u kitobni oʻqiyotgan edi (hali
     tugatmagan).</p>
  <p class="pe-ex__why">Sentence 1: he finished it and knows the story. Sentence 2: he is in
     the middle of it.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni oʻzbekchada ham koʻrsatish mumkin: <b>Simple</b> — "oʻqib <b>chiqdim</b>",
  "yozib <b>boʻldim</b>" (natija bor, ish tugagan). <b>Continuous</b> — "oʻqi<b>yotgan
  edim</b>", "yoz<b>ib oʻtirgan edim</b>" (jarayon, tugagani muhim emas). Yaʼni savol:
  <b>natija muhimmi yoki jarayonmi?</b>
</div>

<h3>2. How many vs how long</h3>

<p>This is the fastest test in an exam. A <b>number</b> pulls the sentence into the Simple; a
<b>length of time</b> pulls it into the Continuous.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'ve written</b> <b>three</b> letters today. — I<b>'ve been
     writing</b> letters <b>all day</b>.</p>
  <p class="pe-ex__uz">Bugun uchta xat yozdim. — Kun boʻyi xat yozdim.</p>
  <p class="pe-ex__why">You can count letters, but you cannot count "all day". Numbers →
     Simple.</p>
</div>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Simple signals</p>
    <p><em>how many, three times, twice, already, yet, just, ever, never</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Continuous signals</p>
    <p><em>how long, all day, all morning, lately, recently, for hours</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Simple = complete</p>
    <p>The action reached its end. <em>I've finished.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Continuous = maybe unfinished</p>
    <p>It may still be going on. <em>I've been finishing it.</em></p>
  </div>
</div>

<h3>3. When both are correct</h3>

<p>With a few "long state" verbs — <b>live, work, study, teach, learn</b> — plus <em>for</em>
or <em>since</em>, both forms are correct and mean practically the same thing.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'ve lived</b> here for ten years. = I<b>'ve been living</b> here
     for ten years.</p>
  <p class="pe-ex__uz">Bu yerda oʻn yildan beri yashayman.</p>
  <p class="pe-ex__why">The Continuous just feels slightly more temporary or more personal.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Do not freeze in an exam over these five verbs — either answer is accepted. Save your
  attention for the pairs that really differ: <em>painted / been painting</em>,
  <em>read / been reading</em>, <em>written three / been writing all day</em>.
</div>

<h3>4. The verbs that only allow the Simple</h3>

<p>Stative verbs, one final time: <em>know, understand, believe, like, love, hate, want, need,
belong, own, have (= own)</em>. They have no Continuous form in any tense.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>I've been knowing her since school.</s></p>
  <p class="pe-good">I<b>'ve known</b> her since school.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bir jumlada ikkalasi ham uchrashi mumkin, va bu juda tabiiy eshitiladi:
  <em>I<b>'ve been studying</b> all evening and I<b>'ve finished</b> two chapters</em> —
  "Kechqurun boʻyi oʻqidim (jarayon) va ikkita boʻlimni tugatdim (natija)". Jarayon uchun
  Continuous, sanoqli natija uchun Simple.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Baʼzi feʼllar <b>bir lahzada</b> sodir boʻladi va shuning uchun jarayon shaklini
  olmaydi: <em>topmoq</em> (find), <em>sindirmoq</em> (break), <em>yoʻqotmoq</em> (lose),
  <em>boshlamoq</em> (start). Ularni soatlab qilib boʻlmaydi — shuning uchun
  <s>I've been finding</s> emas, <b>I've found</b>. Jarayonni aytmoqchi boʻlsangiz,
  boshqa feʼl oling: <b>I've been looking for</b> ("qidirayotgan edim").
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have been reading three books this month.</s></p>
  <p class="pe-good">I <b>have read</b> three books this month. <em>(a number → Simple)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How long have you finished your homework?</s></p>
  <p class="pe-good"><b>How long have you been doing</b> your homework?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has been breaking her leg.</s></p>
  <p class="pe-good">She <b>has broken</b> her leg. <em>(one instant action, not an activity)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I've been washing the car — come and look how clean it is!</s></p>
  <p class="pe-good">I<b>'ve washed</b> the car — come and look! <em>(the result matters)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I have been needing help for weeks.</s></p>
  <p class="pe-good">I <b>have needed</b> help for weeks.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>Afsona <span class="pe-blank">?</span> (make) five cakes for the party.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>has made</strong> — <em>five</em> is a number, so the focus is the finished
         result.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>Afsona <span class="pe-blank">?</span> (bake) since this morning — the whole
     house smells wonderful.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>has been baking</strong> — <em>since this morning</em> is a duration, and the
         smell is the visible trace of the activity.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) I've cleaned my room. (b) I've been cleaning my
     room.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) It is clean now</strong> — the job is done.
         <strong>(b) I have been busy with it</strong> — perhaps it is still not finished, and
         that is why I am tired and dusty.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Both gaps: <em>I <span class="pe-blank">?</span> (study) all evening and I
     <span class="pe-blank">?</span> (learn) forty new words.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>have been studying … have learned.</strong></p>
      <p>The activity takes the Continuous; the countable result takes the Simple. This is the
         most typical exam sentence for this pair.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Why can't we say <em>"I've been finding my keys"</em>?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because "find" happens in one instant</strong> — it is not an activity you
         can do for an hour. Say <em>I<b>'ve been looking for</b> my keys</em> (the activity)
         or <em>I<b>'ve found</b> them</em> (the result).</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Result</b><span>natija</span></li>
  <li><b>Activity</b><span>jarayon</span></li>
  <li><b>Complete</b><span>tugallangan</span></li>
  <li><b>Incomplete</b><span>tugallanmagan</span></li>
  <li><b>How many</b><span>nechta</span></li>
  <li><b>How long</b><span>qancha vaqt</span></li>
  <li><b>Lately / recently</b><span>soʻnggi paytda</span></li>
  <li><b>To bake</b><span>pishirmoq (non, tort)</span></li>
  <li><b>Chapter</b><span>bob</span></li>
  <li><b>Instant</b><span>bir lahzalik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Simple</b> = the finished result · <b>Continuous</b> = the activity itself.</li>
    <li><b>How many / a number</b> → Simple. <b>How long / all day</b> → Continuous.</li>
    <li>With <b>live, work, study</b> + for/since, both are correct.</li>
    <li>Instant verbs (<b>find, break, lose, start</b>) take the Simple.</li>
    <li>Stative verbs have <b>no</b> Continuous form at all.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-38: Past Perfect: The Past Before the Past",
        "category": "english",
        "order": 38,
        "summary": (
            "When two things happened in the past, this tense says which one came first — "
            "had + V3, the same for every person."
        ),
        "stories": ["By the Time the Train Came"],
        "content": """
<h2>PE-38: Past Perfect: The Past Before the Past</h2>

<p><em>"When I arrived at the station, the train <b>had left</b>."</em> Two past events, and
the grammar alone tells you the order: the train left <b>first</b>, and I arrived to find an
empty platform. That is the entire job of the <mark>Past Perfect</mark> — it steps one level
further back and says "this happened before that".</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>had + V3</b> — one form for every person</li>
    <li>How it shows which past action came first</li>
    <li>The words it travels with: <em>when, after, before, by the time, already</em></li>
    <li>When you do <b>not</b> need it</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The earlier past</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">had</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
  <span class="pe-chip pe-chip--opt">I had · she had · they had</span>
</div>

LEGEND_HERE

<h3>1. The picture: two dots in the past</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:82%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:16%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:46%"></span>
    <span class="pe-tl-tag" style="left:16%">train left</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>Two past moments. The <b>earlier</b> one takes <b>had + V3</b>; the later one is a normal
Past Simple. Without the Past Perfect, an English listener cannot tell which came first.</p>

<div class="pe-ex">
  <p class="pe-ex__en">When I <span class="pe-hl pe-hl--v">arrived</span>, the train
     <span class="pe-hl pe-hl--aux">had</span>
     <span class="pe-hl pe-hl--v">left</span>.</p>
  <p class="pe-ex__uz">Men yetib borganimda, poyezd joʻnab ketgan edi.</p>
  <p class="pe-ex__why">Compare: <em>When I arrived, the train <b>left</b></em> would mean it
     left <em>after</em> I got there.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Past Perfect oʻzbekchadagi "<b>-gan edi</b>" shakliga toʻgʻri keladi:
  <em>ket<b>gan edi</b></em> → <em>had left</em>, <em>oʻqi<b>gan edim</b></em> →
  <em>had read</em>. Oʻzbekcha jumlangizda "edi" boʻlsa va u <b>boshqa oʻtgan ishdan
  oldin</b> boʻlgan boʻlsa — ingliz tilida <b>had + V3</b> kerak.
</div>

<h3>2. One form for everybody</h3>

<p>A small gift from English: unlike the Present Perfect (<em>have/has</em>), the Past Perfect
has only <b>had</b> — for I, you, he, she, it, we and they alike.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>had</b> finished · She <b>had</b> finished · They <b>had</b>
     finished. Short form: <em>I'd, she'd, they'd</em>.</p>
  <p class="pe-ex__uz">Men tugatgan edim · U tugatgan edi · Ular tugatgan edilar.</p>
</div>

<ol class="pe-steps">
  <li><b>Negative:</b> <em>I <b>hadn't</b> seen him before that day.</em></li>
  <li><b>Question:</b> <em><b>Had</b> you <b>met</b> her before the party?</em></li>
  <li><b>Short answers:</b> <em>Yes, I had. / No, I hadn't.</em></li>
  <li><b>V3 again:</b> it is the same third form as the Present Perfect —
      <em>had gone, had seen, had written</em>, never <s>had went</s>.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxshi xabar: PE-21 da yodlagan <b>V3</b> shakllari endi <b>toʻrtta joyda</b> ishlaydi —
  Present Perfect (<em>have gone</em>), Past Perfect (<em>had gone</em>), Future Perfect
  (<em>will have gone</em>) va keyinroq majhul nisbatda (<em>was written</em>, PE-60).
  Yaʼni bir marta qilingan mehnat toʻrt barobar foyda beradi.
</div>

<h3>3. The words it travels with</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>when</p>
    <p><em>When we got home, the guests <b>had already gone</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>by the time</p>
    <p><em>By the time the film started, we <b>had eaten</b> everything.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>after / before</p>
    <p><em>After she <b>had finished</b>, she went out.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>already, just, never</p>
    <p><em>I <b>had never seen</b> the sea before that summer.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek <b>had never travelled</b> by plane before he
     <b>went</b> to Turkey.</p>
  <p class="pe-ex__uz">Sherbek Turkiyaga borishidan oldin hech qachon samolyotda
     uchmagan edi.</p>
</div>

<h3>4. When you do NOT need it</h3>

<p>If the words <b>after</b> or <b>before</b> already make the order obvious, English usually
relaxes and uses two Past Simples. Both versions are correct.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>After</b> I <b>finished</b> my homework, I <b>watched</b> TV. =
     After I <b>had finished</b> my homework, I watched TV.</p>
  <p class="pe-ex__uz">Uy vazifamni tugatgandan keyin televizor koʻrdim.</p>
</div>

<p>And when two actions simply happen one after another in a story, you do <b>not</b> use the
Past Perfect at all — that would be like stepping backwards for no reason:</p>

<div class="pe-fix">
  <p class="pe-bad"><s>I had opened the door and I had walked into the room.</s></p>
  <p class="pe-good">I <b>opened</b> the door and <b>walked</b> into the room.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Use the Past Perfect only when the order would otherwise be <b>unclear</b> or when you are
  deliberately <b>jumping back</b> in a story. A whole paragraph of <em>had</em> sounds heavy
  and unnatural — one or two are usually enough.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Muhim qoida: har bir oʻtgan zamon gapiga "edi" qoʻshib chiqmang. Past Perfect faqat
  <b>ikkita oʻtgan ish bor va qaysi biri oldin boʻlganini koʻrsatish kerak</b> boʻlganda
  ishlatiladi. Oddiy hikoyada ketma-ket voqealar uchun Past Simple yetarli:
  <em>eshikni ochdim va ichkariga kirdim</em>.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>When I arrived, he already left.</s></p>
  <p class="pe-good">When I arrived, he <b>had already left</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I had went to bed before you called.</s></p>
  <p class="pe-good">I <b>had gone</b> to bed before you called. <em>(V3!)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has finished her work before the teacher came.</s></p>
  <p class="pe-good">She <b>had finished</b> her work before the teacher came.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>By the time we had arrived, the concert had started.</s></p>
  <p class="pe-good">By the time we <b>arrived</b>, the concert <b>had started</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I had eaten breakfast and had gone to school.</s></p>
  <p class="pe-good">Yesterday I <b>ate</b> breakfast and <b>went</b> to school.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>When we got to the cinema, the film <span class="pe-blank">?</span>
     (already / start).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>had already started</strong> — it began before we got there, and
         <em>already</em> sits between <em>had</em> and the V3.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What is the difference? <em>(a) When I arrived, she made tea. (b) When I arrived, she had
     made tea.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) She made it after I arrived.</strong>
         <strong>(b) The tea was already made when I walked in.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>I hadn't never seen such a big fish before that day.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I had never seen such a big fish before that day.</strong></p>
      <p>One negative only — <em>never</em> already does the work.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Is the Past Perfect necessary here? <em>I got up, washed my face and had eaten
     breakfast.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>No — it is wrong here.</strong> These are three events in order, so all three
         take the Past Simple: <em>I got up, washed my face and <b>ate</b> breakfast.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Join with <em>by the time</em>: <em>The bus left at 7. I got to the stop at 7:05.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>By the time I got to the stop, the bus had left.</strong></p>
      <p><em>By the time</em> + Past Simple, main clause + <b>had + V3</b>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Past Perfect</b><span>oʻtgan tugallangan zamon</span></li>
  <li><b>Earlier</b><span>oldinroq</span></li>
  <li><b>By the time</b><span>...gunga qadar</span></li>
  <li><b>Order of events</b><span>voqealar tartibi</span></li>
  <li><b>To realise</b><span>anglab yetmoq</span></li>
  <li><b>Platform</b><span>perron</span></li>
  <li><b>Guest</b><span>mehmon</span></li>
  <li><b>To travel by plane</b><span>samolyotda uchmoq</span></li>
  <li><b>Unclear</b><span>noaniq</span></li>
  <li><b>Sequence</b><span>ketma-ketlik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>had + V3</b> — one form for every person; short form <b>'d</b>.</li>
    <li>It marks the <b>earlier</b> of two past actions; the later one is Past Simple.</li>
    <li>Uzbek "<b>-gan edi</b>" is your signal.</li>
    <li>Travels with <em>when, by the time, after, before, already, never</em>.</li>
    <li>Do <b>not</b> use it for a simple sequence of events in a story.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-39: Past Perfect Continuous",
        "category": "english",
        "order": 39,
        "summary": (
            "How long something had been going on before another past moment — had been + -ing, "
            "the tense that explains why things were the way they were."
        ),
        "stories": ["She Had Been Saving for Eleven Months"],
        "content": """
<h2>PE-39: Past Perfect Continuous</h2>

<p><em>"His eyes were red because he <b>had been crying</b>."</em> Notice what this sentence
does: it takes you back to a moment in the past, and then explains what had been happening
<b>before</b> it. This is the last of the Perfect tenses, and it is the natural partner of
PE-38 — where <em>had + V3</em> gives the earlier <b>event</b>, this gives the earlier
<b>activity</b> and how long it lasted.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>had been + verb-ing</b></li>
    <li>Two jobs: duration before a past moment, and the cause of a past situation</li>
    <li>How it differs from the Past Continuous</li>
    <li>Where <b>for</b> and <b>since</b> fit in</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The earlier activity</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">had been</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
</div>

LEGEND_HERE

<h3>1. The picture: a band that ends before a past point</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:84%"></span>
    <span class="pe-tl-band" style="left:10%;width:38%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:52%"></span>
    <span class="pe-tl-tag" style="left:16%">had been waiting</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The band is the long activity. The red dot after it is the past moment we are talking about.
The activity was going on <b>up to</b> that moment.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">We</span>
     <span class="pe-hl pe-hl--aux">had been waiting</span> for an hour when the bus finally
     <span class="pe-hl pe-hl--v">came</span>.</p>
  <p class="pe-ex__uz">Avtobus nihoyat kelganda biz bir soatdan beri kutayotgan edik.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu zamon oʻzbekchadagi "<b>...yotgan edim</b>" yoki "<b>...dan beri ... edim</b>" shakliga
  toʻgʻri keladi: <em>kutayotgan edik</em> → <em>had been waiting</em>. Past Perfect
  (PE-38) "<b>-gan edi</b>" boʻlsa, bu — "<b>-yotgan edi</b>". Farqi: birinchisi tugagan
  <b>ish</b>, ikkinchisi davom etgan <b>jarayon</b>.
</div>

<h3>2. Job one: how long, before a past moment</h3>

<p>Use it with <b>for</b> and <b>since</b> to measure an activity that ran up to a point in the
past.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>had been studying</b> Korean <b>for three years</b> before she
     went to Seoul.</p>
  <p class="pe-ex__uz">Afsona Seulga borishidan oldin uch yildan beri koreys tilini
     oʻrganayotgan edi.</p>
  <p class="pe-ex__why">Everything is in the past: the studying, and the trip that ended it.</p>
</div>

<h3>3. Job two: explaining a past situation</h3>

<p>Just like the Present Perfect Continuous explains a situation now (PE-36), this one explains
a situation <b>then</b>. It answers the question "why was it like that?"</p>

<div class="pe-ex">
  <p class="pe-ex__en">The ground was wet because it <b>had been raining</b> all night.</p>
  <p class="pe-ex__uz">Yer hoʻl edi, chunki tun boʻyi yomgʻir yogʻgan edi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Jasur was out of breath. He <b>had been running</b>.</p>
  <p class="pe-ex__uz">Jasurning nafasi yetmayotgan edi. U yugurgan edi.</p>
  <p class="pe-ex__why">The running had stopped — but its effect was still visible at that past
     moment.</p>
</div>

<h3>4. Past Continuous or Past Perfect Continuous?</h3>

<p>Both describe activities in the past, but they sit in different places on the timeline.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Past Continuous — AT that moment</p>
    <ul>
      <li>When I saw him, he <b>was crying</b>.<br><em>(tears at that second)</em></li>
      <li>She <b>was cooking</b> when I arrived.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Past Perfect Cont. — BEFORE that moment</p>
    <ul>
      <li>When I saw him, he <b>had been crying</b>.<br><em>(red eyes; the crying had
          stopped)</em></li>
      <li>She was tired — she <b>had been cooking</b> all day.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni bitta savol hal qiladi: <b>oʻsha paytda ish davom etayotganmidi</b> (Past
  Continuous — "yigʻlayotgan edi"), <b>yoki undan oldin boʻlib, tugaganmidi</b> (Past
  Perfect Continuous — "yigʻlagan edi, koʻzlari qizargan edi")? Birinchisi — oʻsha
  lahzaning ichida, ikkinchisi — undan oldingi davr.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oson yoʻli: PE-36 dagi gapni oling va <b>have been</b> ni <b>had been</b> ga
  almashtiring — butun gap oʻtmishga koʻchadi. <em>I <b>have been</b> waiting for an
  hour</em> ("hozir kutyapman") → <em>I <b>had been</b> waiting for an hour</em>
  ("oʻsha paytda kutayotgan edim"). Boshqa hech narsa oʻzgarmaydi.
</div>

<h3>5. Form details</h3>

<ol class="pe-steps">
  <li><b>Same for everyone:</b> <em>I / she / they <b>had been</b> working.</em></li>
  <li><b>Negative:</b> <em>He <b>hadn't been</b> sleeping well.</em></li>
  <li><b>Question:</b> <em><b>Had</b> you <b>been</b> waiting long?</em> ·
      <em><b>How long had</b> she <b>been</b> working there?</em></li>
  <li><b>Four parts:</b> <b>had</b> + <b>been</b> + verb + <b>-ing</b>. Missing one breaks the
      sentence.</li>
</ol>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Stative verbs are still excluded — in this tense too. <s>I had been knowing him for
  years</s> ✗ → <b>I had known him for years</b> ✓.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I had been work there for two years before I left.</s></p>
  <p class="pe-good">I <b>had been working</b> there for two years before I left.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She was tired because she had cooking all day.</s></p>
  <p class="pe-good">… because she <b>had been cooking</b> all day.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>They had been waiting since two hours.</s></p>
  <p class="pe-good">They had been waiting <b>for</b> two hours.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I have been waiting for an hour when he finally arrived.</s></p>
  <p class="pe-good">I <b>had been waiting</b> for an hour when he finally arrived.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He had been having a car before he sold it.</s></p>
  <p class="pe-good">He <b>had had</b> a car before he sold it.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>Sherbek <span class="pe-blank">?</span> (play) football for two hours, so
     he was exhausted.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>had been playing</strong> — the long activity explains his past state
         (exhausted).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What is the difference? <em>(a) When I came in, she was crying. (b) When I came in, she
     had been crying.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) She was crying at that moment</strong> — I saw the tears.
         <strong>(b) She had stopped</strong> — I saw only the red eyes.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>We had been driven for six hours before we stopped.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>We had been driving for six hours before we stopped.</strong></p>
      <p>After <em>had been</em> comes the <b>-ing</b> form, not the V3.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Explain the past situation: <em>The kitchen was full of smoke.</em> (cook)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>The kitchen was full of smoke because my brother
         <b>had been cooking</b>.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which tense, and why? <em>Afsona ___ (wait) for an hour when the doctor finally called
     her name.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>had been waiting</strong> — the waiting had been going on for an hour
         <em>before</em> the past moment when the doctor called.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Past Perfect Continuous</b><span>oʻtgan tugallangan davomli zamon</span></li>
  <li><b>Duration</b><span>davomiylik</span></li>
  <li><b>Cause</b><span>sabab</span></li>
  <li><b>Out of breath</b><span>nafasi yetmayotgan</span></li>
  <li><b>Exhausted</b><span>holdan toygan</span></li>
  <li><b>Smoke</b><span>tutun</span></li>
  <li><b>To stop</b><span>toʻxtamoq</span></li>
  <li><b>Finally</b><span>nihoyat</span></li>
  <li><b>Before that</b><span>undan oldin</span></li>
  <li><b>Situation</b><span>vaziyat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>had been + verb-ing</b> — four parts, same for every person.</li>
    <li>Job 1: <b>how long</b> an activity lasted before a past moment (for / since).</li>
    <li>Job 2: the <b>cause</b> of a past situation — red eyes, wet ground, tiredness.</li>
    <li>Past Continuous = <b>at</b> that moment · Past Perfect Continuous = <b>before</b>
        it.</li>
    <li>Uzbek "<b>-yotgan edi</b>" is your signal; stative verbs are still excluded.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-40: Future Perfect and Future Perfect Continuous",
        "category": "english",
        "order": 40,
        "summary": (
            "By this time next year, what will you have done? Standing in the future and "
            "looking back — will have + V3, and will have been + -ing."
        ),
        "stories": ["The Letters They Will Have Forgotten"],
        "content": """
<h2>PE-40: Future Perfect and Future Perfect Continuous</h2>

<p>Here is a strange and rather beautiful thing English can do: it can put you in the future
and let you look <b>backwards</b> from there. <em>"By June I <b>will have finished</b>
school."</em> June has not arrived, and neither has the finishing — yet you are already
standing in June, looking back at a completed action. These are the last two tenses of the
Perfect family.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>will have + V3</b> — finished before a future moment</li>
    <li><b>will have been + verb-ing</b> — how long, up to a future moment</li>
    <li>The signal word <b>by</b>, and the <em>by the time</em> rule</li>
    <li>How these two complete the whole tense system</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Finished before a future point</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">will have</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
</div>

LEGEND_HERE

<h3>1. The picture: standing in the future, looking back</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:20%"></span>
    <span class="pe-tl-dot" style="left:48%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:76%"></span>
    <span class="pe-tl-tag" style="left:48%">I finish school</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The blue dot is the action; the red dot further right is the future moment you are looking
back from. Everything is ahead of NOW — the action just happens <b>earlier</b> than the
deadline.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>By</b> next June <span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">will have</span>
     <span class="pe-hl pe-hl--v">finished</span> school.</p>
  <p class="pe-ex__uz">Kelasi iyunga qadar maktabni tugatgan boʻlaman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Future Perfect oʻzbekchadagi "<b>...gan boʻlaman</b>" shakliga toʻgʻri keladi:
  <em>tugat<b>gan boʻlaman</b></em> → <em>I <b>will have finished</b></em>. Uni tanish
  qilib turadigan soʻz — <b>by</b> ("...gacha, ...ga qadar"): <em>by Friday</em>,
  <em>by next year</em>, <em>by the time you arrive</em>.
</div>

<h3>2. The signal word: by</h3>

<p>This tense almost always appears with <b>by</b> or <b>by the time</b>, because it needs a
deadline to look back from.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>by + a time</p>
    <p><em>I'll have read it <b>by</b> Friday.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>by then</p>
    <p><em>Come at six — I'll have cooked <b>by then</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>by the time + clause</p>
    <p><em><b>By the time</b> you arrive, we'll have eaten.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>in / before</p>
    <p><em>In two years he'll have graduated.</em></p>
  </div>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  After <b>by the time</b>, use the <b>Present Simple</b> — never <em>will</em>. This is the
  time-clause rule from PE-26 again:
  <em>By the time you <b>arrive</b>, we <b>will have finished</b>.</em>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>By the time</b> the guests <b>get</b> here, Afsona
     <b>will have made</b> the plov.</p>
  <p class="pe-ex__uz">Mehmonlar yetib kelguncha, Afsona palovni pishirib boʻlgan boʻladi.</p>
  <p class="pe-ex__why">Two futures in one sentence, but only one <em>will</em>.</p>
</div>

<h3>3. Future Perfect Continuous — how long, by then</h3>

<p>Add <b>been + -ing</b> and you get duration instead of completion: not "what will be
finished", but "how long it will have been going on".</p>

<div class="pe-formula">
  <span class="pe-formula__label">Duration up to a future point</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">will have been</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Next month I <b>will have been studying</b> English <b>for six
     years</b>.</p>
  <p class="pe-ex__uz">Kelasi oyda ingliz tilini oʻrganayotganimga olti yil boʻladi.</p>
  <p class="pe-ex__why">The studying continues; we are only measuring it from a future point.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">will have + V3 — completed</p>
    <ul>
      <li>By 2030 he <b>will have built</b> the house.</li>
      <li>I <b>will have written</b> ten pages by Friday.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">will have been + -ing — duration</p>
    <ul>
      <li>By 2030 he <b>will have been building</b> it for five years.</li>
      <li>By Friday I <b>will have been writing</b> for a week.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farq PE-37 dagi bilan bir xil, faqat kelajakda: <b>will have + V3</b> — ish
  <b>tugagan boʻladi</b> ("yozib boʻlgan boʻlaman"). <b>will have been + -ing</b> — ish
  <b>qancha vaqtdan beri davom etayotgani</b> ("yozayotganimga bir hafta boʻladi").
  Ikkinchisi kamroq ishlatiladi, lekin imtihonlarda uchraydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  PE-31 dagi <b>by</b> va <b>until</b> farqi shu yerda ish beradi: bu zamon <b>faqat
  by</b> bilan ishlatiladi, chunki u <b>muddat</b> talab qiladi. <em><b>By</b> Friday I
  will have finished</em> ✓ ("jumagacha tugatgan boʻlaman"), <s>until Friday I will have
  finished</s> ✗. <em>Until</em> davom etadigan ish uchun: <em>I will wait <b>until</b>
  Friday</em>.
</div>

<h3>4. Form details</h3>

<ol class="pe-steps">
  <li><b>Same for everyone:</b> <em>I / she / they <b>will have</b> finished.</em></li>
  <li><b>Negative:</b> <em>They <b>won't have</b> arrived by six.</em></li>
  <li><b>Question:</b> <em><b>Will</b> you <b>have finished</b> by then?</em></li>
  <li><b>Short answer:</b> <em>Yes, I will. / No, I won't.</em></li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  The Future Perfect is also the polite way to guess about the present:
  <em>"You <b>will have heard</b> the news by now, I expect."</em> It means "I assume you
  already know". You will meet this idea again in the modals of deduction, PE-47.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>By the time you will arrive, we will have eaten.</s></p>
  <p class="pe-good">By the time you <b>arrive</b>, we will have eaten.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will have finish my work by Friday.</s></p>
  <p class="pe-good">I will have <b>finished</b> my work by Friday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Next year I will have been study here for three years.</s></p>
  <p class="pe-good">Next year I will have been <b>studying</b> here for three years.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Until Friday I will have finished it.</s></p>
  <p class="pe-good"><b>By</b> Friday I will have finished it.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will have went home before you call.</s></p>
  <p class="pe-good">I will have <b>gone</b> home before you call.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>By ten o'clock tonight I <span class="pe-blank">?</span> (finish) all my
     homework.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>will have finished</strong> — <em>by ten o'clock</em> is the deadline you are
         looking back from.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>By the time the film will start, we will have bought the tickets.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>By the time the film starts, we will have bought the tickets.</strong></p>
      <p>After <em>by the time</em> comes the Present Simple — the same rule as after
         <em>when</em> and <em>if</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which one, and why? <em>In September, Jasur ___ (live) in Tashkent for ten years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>will have been living</strong> (or <em>will have lived</em>) — we are
         measuring <b>how long</b>, from a future point. With <em>live</em> both forms are
         accepted, as in PE-37.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Make it negative: <em>They will have arrived by six.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>They won't have arrived by six.</strong></p>
      <p>Only <em>will</em> becomes negative; <em>have</em> and the V3 stay exactly as they
         are.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one sentence about yourself starting with <em>By this time next year…</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>By this time next year I <b>will have taken</b> my final
         exams and I <b>will have started</b> at university.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Future Perfect</b><span>kelasi tugallangan zamon</span></li>
  <li><b>By then</b><span>oʻsha vaqtga qadar</span></li>
  <li><b>By the time</b><span>...gunga qadar</span></li>
  <li><b>Deadline</b><span>oxirgi muddat</span></li>
  <li><b>To graduate</b><span>bitirmoq</span></li>
  <li><b>To assume</b><span>taxmin qilmoq</span></li>
  <li><b>Final exams</b><span>yakuniy imtihonlar</span></li>
  <li><b>To build</b><span>qurmoq</span></li>
  <li><b>Completion</b><span>tugallanish</span></li>
  <li><b>To look back</b><span>orqaga nazar solmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>will have + V3</b> = finished <b>before</b> a future moment.</li>
    <li><b>will have been + -ing</b> = <b>how long</b> it will have been going on.</li>
    <li>Signal words: <b>by, by then, by the time, in two years</b>.</li>
    <li>After <b>by the time</b> → Present Simple, never <em>will</em>.</li>
    <li>Uzbek "<b>...gan boʻlaman</b>" is your signal for the Future Perfect.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
