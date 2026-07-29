# -*- coding: utf-8 -*-
"""Prime English — Block D, lessons 46–50 (modal verbs continued).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_46_50.py --author=prime
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
        "title": "PE-46: should, ought to, had better: Advice",
        "category": "english",
        "order": 46,
        "summary": (
            "How to tell someone what to do without ordering them — three levels of advice, "
            "from a gentle suggestion to a serious warning."
        ),
        "content": """
<h2>PE-46: should, ought to, had better: Advice</h2>

<p>A friend has a headache. In Uzbek you would say <em>"Dam olsang yaxshi boʻlardi"</em>. In
English you reach for <b>should</b> — the single most useful modal for everyday kindness:
<em>"You <b>should</b> rest."</em> This lesson gives you that word, plus two stronger
neighbours for when gentle advice is not enough.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>should</b> — advice, opinion and expectation</li>
    <li><b>ought to</b> — the one modal that keeps its <em>to</em></li>
    <li><b>had better</b> — advice with a warning attached</li>
    <li>Where each one sits on the strength scale</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Advice</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">should / ought to / had better</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
</div>

LEGEND_HERE

<h3>1. should — your everyday advice word</h3>

<p>It follows all the modal rules from PE-42: no <b>-s</b>, no <em>to</em>, questions by
inversion, negative with <em>not</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <span class="pe-hl pe-hl--aux">should</span>
     <span class="pe-hl pe-hl--v">drink</span> more water. You
     <span class="pe-hl pe-hl--aux">shouldn't</span>
     <span class="pe-hl pe-hl--v">stay</span> up so late.</p>
  <p class="pe-ex__uz">Koʻproq suv ichishing kerak. Bunchalik kech yotmasliging kerak.</p>
</div>

<p><b>Should</b> also asks for advice, and this is how you will use it most often in real
conversation: <em><b>What should I</b> do? <b>Should I</b> tell her the truth?</em></p>

<p>And it has a second, quieter job — <b>expectation</b>: something you believe is probably
true. <em>The train <b>should</b> arrive at six</em> means "according to the timetable, I
expect it to."</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda ehtiyot boʻling: oʻzbekchada <b>"kerak"</b> soʻzi ham <em>should</em>, ham
  <em>must</em> uchun ishlatiladi. Farqni maʼnodan toping: <b>maslahat</b> berayotgan
  boʻlsangiz ("yaxshi boʻlardi", "kerak deb oʻylayman") — <b>should</b>.
  <b>Majburiyat</b> boʻlsa ("shart", "majbursiz") — <b>must</b> yoki <b>have to</b>.
  Maslahatni <em>must</em> bilan aytsangiz, buyruqdek eshitiladi.
</div>

<h3>2. ought to — the polite twin</h3>

<p><b>Ought to</b> means almost exactly the same as <em>should</em>, just a little more formal
and rather less common in speech. It is famous for one thing: it is the <b>only</b> modal that
keeps <em>to</em> in front of the verb.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <b>ought to</b> apologise. = You <b>should</b> apologise.</p>
  <p class="pe-ex__uz">Kechirim soʻrashing kerak.</p>
  <p class="pe-ex__why">Note: <em>ought <b>to</b> apologise</em>, but <em>should
     apologise</em> — no <em>to</em>.</p>
</div>

<h3>3. had better — advice with a warning</h3>

<p>This one is stronger. <b>Had better</b> ('d better) says: do this, <b>or something bad will
happen</b>. It is about one specific situation, not general advice.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You<b>'d better</b> leave now, or you'll miss the bus. — We<b>'d better
     not</b> be late again.</p>
  <p class="pe-ex__uz">Hozir chiqsang yaxshi boʻladi, boʻlmasa avtobusga ulgurmaysan. —
     Yana kechikmaganimiz maʼqul.</p>
  <p class="pe-ex__why">Negative: <b>had better not</b> — the <em>not</em> goes after
     <em>better</em>.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  It is <b>had</b> better, never <s>would better</s>. The short form <b>'d</b> hides
  <em>had</em>, which is why so many learners write it wrong. And no <em>to</em>:
  <s>You'd better to go</s> ✗ → <b>You'd better go</b> ✓.
</div>

<h3>4. The strength scale</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>could / might</p>
    <p>A gentle suggestion. <em>You <b>could</b> ask the teacher.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>should / ought to</p>
    <p>Normal advice. <em>You <b>should</b> ask the teacher.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>had better</p>
    <p>Advice + warning. <em>You<b>'d better</b> ask the teacher.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>must / have to</p>
    <p>Obligation. <em>You <b>must</b> ask the teacher.</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kuch darajasini his qilib ishlating: <b>could</b> — "istasangiz ...sangiz ham boʻladi",
  <b>should</b> — "...ganingiz maʼqul", <b>had better</b> — "...maganingiz yaxshi, boʻlmasa
  yomon boʻladi", <b>must</b> — "shart". Doʻstingizga <em>had better</em> deyishdan oldin
  oʻylang: unda ogohlantirish ohangi bor.
</div>

<h3>5. Other ways to give advice</h3>

<p>Modals are not the only tool. These three phrases are extremely common in real
conversation, and using them makes your advice sound natural rather than textbook-like.</p>

<ul>
  <li><b>Why don't you …?</b> — friendly and light: <em>Why don't you ask your teacher?</em></li>
  <li><b>If I were you, I'd …</b> — the warmest of all: <em>If I were you, I'd apologise.</em>
      (You will meet this structure properly in PE-54.)</li>
  <li><b>It's a good idea to …</b> — neutral and safe: <em>It's a good idea to arrive
      early.</em></li>
</ul>

<div class="pe-ex">
  <p class="pe-ex__en">— I can't sleep before exams. — <b>Why don't you</b> read for half an
     hour? <b>If I were you, I'd</b> switch off my phone.</p>
  <p class="pe-ex__uz">— Imtihon oldidan uxlay olmayman. — Yarim soat kitob oʻqisang-chi?
     Men senning oʻrningda boʻlsam, telefonni oʻchirib qoʻyardim.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Amaliy maslahat: <b>ought to</b> ni bilib qoʻying, lekin gapirganda <b>should</b> ni
  ishlating — jonli nutqda <em>ought to</em> juda kam uchraydi. Kundalik suhbat uchun
  eng kerakli uchtasi: <b>should</b> (maslahat), <b>Why don't you…?</b> (taklif) va
  <b>If I were you, I'd…</b> ("sening oʻrningda boʻlsam"). Shu uchtasi yetarli.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>You should to see a doctor.</s></p>
  <p class="pe-good">You <b>should see</b> a doctor.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He shoulds study harder.</s></p>
  <p class="pe-good">He <b>should study</b> harder.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You would better hurry up.</s></p>
  <p class="pe-good">You<b>'d better</b> hurry up. <em>(had better)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You had better not to touch it.</s></p>
  <p class="pe-good">You<b>'d better not</b> touch it.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you think I should to call him?</s></p>
  <p class="pe-good">Do you think I <b>should call</b> him?</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Give advice: <em>Your friend is always tired in the morning.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>You <b>should</b> go to bed earlier. You
         <b>shouldn't</b> use your phone at night.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>You would better take an umbrella.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>You'd better take an umbrella.</strong> The <b>'d</b> is <em>had</em>, not
         <em>would</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which is stronger, and why? <em>(a) You should apologise. (b) You'd better
     apologise.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b)</strong> — <em>had better</em> carries a warning: if you don't, there
         will be trouble. <em>Should</em> is just an opinion.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which sentence is advice, and which is expectation?
     <em>(a) You should rest. (b) The parcel should arrive tomorrow.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) advice · (b) expectation</strong> — "I expect it to arrive; that's what
         normally happens."</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Rewrite with <em>ought to</em>: <em>We should help her.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>We ought to help her.</strong> Same meaning — but notice that <em>to</em>
         appears, which never happens with <em>should</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Advice</b><span>maslahat</span></li>
  <li><b>To advise</b><span>maslahat bermoq</span></li>
  <li><b>Suggestion</b><span>taklif</span></li>
  <li><b>Warning</b><span>ogohlantirish</span></li>
  <li><b>Expectation</b><span>kutilgan natija</span></li>
  <li><b>To apologise</b><span>kechirim soʻramoq</span></li>
  <li><b>To hurry up</b><span>shoshilmoq</span></li>
  <li><b>Parcel</b><span>pochta joʻnatmasi</span></li>
  <li><b>Consequence</b><span>oqibat</span></li>
  <li><b>Gentle</b><span>yumshoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>should + base verb</b> — advice, opinion, and expectation.</li>
    <li><b>ought to</b> = the same, more formal — and the only modal that keeps <b>to</b>.</li>
    <li><b>had better</b> ('d better) = advice with a warning; negative is <b>had better
        not</b>.</li>
    <li>Strength: could → should → had better → must.</li>
    <li>Uzbek "kerak" covers both <em>should</em> and <em>must</em> — choose by meaning.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-47: Modals of Deduction: must be, can't be, might be",
        "category": "english",
        "order": 47,
        "summary": (
            "Thinking like a detective in English: how to say how sure you are about something "
            "you cannot see — and why 'mustn't be' is never the opposite of 'must be'."
        ),
        "content": """
<h2>PE-47: Modals of Deduction: must be, can't be, might be</h2>

<p>The lights are off and nobody answers the door. You do not <em>know</em> what is happening
— but you can guess, and English has exact words for how confident your guess is.
<em>"They <b>must be</b> out."</em> <em>"They <b>can't be</b> asleep, it's midday."</em>
<em>"They <b>might be</b> in the garden."</em> This is <mark>deduction</mark>, and it is one
of the most grown-up things you can do in a foreign language.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>must be</b> — I'm almost certain it IS</li>
    <li><b>can't be</b> — I'm almost certain it ISN'T</li>
    <li><b>might / may / could be</b> — it's possible</li>
    <li>Why the opposite of <em>must be</em> is <b>can't be</b>, never <s>mustn't be</s></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Guessing about now</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">must / can't / might</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">be</span>
  <span class="pe-chip pe-chip--opt">(or any base verb)</span>
</div>

LEGEND_HERE

<h3>1. The certainty scale</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">95</span>must be</p>
    <p>I'm almost sure it's true. <em>He <b>must be</b> tired — he worked all night.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">50</span>might / may / could be</p>
    <p>Perhaps. <em>She <b>might be</b> at the library.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>can't be</p>
    <p>I'm almost sure it's false. <em>That <b>can't be</b> right.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">0</span>isn't</p>
    <p>I know. <em>He <b>isn't</b> at home — I've just seen him leave.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--aux">must be</span> very clever — she won the olympiad.</p>
  <p class="pe-ex__uz">Afsona juda aqlli boʻlsa kerak — u olimpiadada gʻolib boʻldi.</p>
  <p class="pe-ex__why">I have evidence, but I don't know her personally. That is a
     deduction.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu maʼnolar oʻzbekchada aniq bor: <b>must be</b> = "<b>boʻlsa kerak</b>" yoki
  "<b>shekilli</b>" (<em>He must be at home</em> — "Uyda boʻlsa kerak").
  <b>can't be</b> = "<b>boʻlishi mumkin emas</b>" (<em>He can't be at home</em> — "Uyda
  boʻlishi mumkin emas"). <b>might be</b> = "<b>boʻlishi mumkin</b>". Tarjimani topsangiz,
  toʻgʻri modalni ham topasiz.
</div>

<h3>2. The trap: must be and can't be</h3>

<p>In PE-44 you learned that <em>must</em> means obligation, and its negative <em>mustn't</em>
means prohibition. But in <b>deduction</b>, the negative of <em>must be</em> is completely
different. It is <b>can't be</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✓ Deduction</p>
    <ul>
      <li>He <b>must be</b> ill. <em>(I'm sure he is)</em></li>
      <li>He <b>can't be</b> ill — I saw him running. <em>(I'm sure he isn't)</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✗ Not deduction</p>
    <ul>
      <li><s>He mustn't be ill.</s></li>
      <li>That would mean "he is forbidden to be ill" — which makes no sense.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Remember two separate pairs:
  <b>Obligation:</b> must ↔ mustn't (forbidden) / don't have to (optional).
  <b>Deduction:</b> must be ↔ <b>can't be</b>. The same word <em>must</em>, two different
  jobs — the context tells you which.
</div>

<h3>3. Guessing about actions, not just states</h3>

<p>Deduction is not limited to <em>be</em>. Put any base verb after the modal — and use
<b>be + -ing</b> when you are guessing about what is happening right now.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Jasur isn't answering his phone. He <b>must be sleeping</b>, or he
     <b>might be studying</b>. He <b>can't be</b> at school — it's Sunday.</p>
  <p class="pe-ex__uz">Jasur telefonini olmayapti. Uxlayotgan boʻlsa kerak yoki oʻqiyotgandir.
     Maktabda boʻlishi mumkin emas — bugun yakshanba.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">She <b>must know</b> the answer — she's read the whole book.</p>
  <p class="pe-ex__uz">U javobni bilsa kerak — butun kitobni oʻqib chiqqan.</p>
  <p class="pe-ex__why">With a stative verb like <em>know</em>, no <b>-ing</b> is possible
     (PE-13).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Must</b> ning qaysi vazifada turganini qanday bilish mumkin? Oddiy tekshiruv:
  agar undan keyin <b>be + sifat/ot</b> kelsa va bu siz <b>nazorat qila olmaydigan</b>
  narsa boʻlsa — bu <b>taxmin</b> ("charchagan boʻlsangiz kerak"). Agar bu odam
  <b>bajarishi mumkin boʻlgan ish</b> boʻlsa — bu <b>majburiyat</b> ("borishingiz shart").
  <em>You must be tired</em> — taxmin; <em>You must go</em> — majburiyat.
</div>

<h3>4. How to build a deduction</h3>

<ol class="pe-steps">
  <li><b>Find your evidence.</b> What can you actually see or know?
      <em>The car isn't here.</em></li>
  <li><b>Decide how sure you are.</b> Almost certain? Possible? Impossible?</li>
  <li><b>Choose the modal:</b> <em>must be</em> · <em>might/may/could be</em> ·
      <em>can't be</em>.</li>
  <li><b>Add the evidence with "because" or a dash</b> — a deduction sounds much better with
      its reason: <em>They <b>must have</b> gone out — the car isn't here.</em></li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Taxminni <b>dalil bilan birga</b> ayting — ingliz tilida bu juda tabiiy eshitiladi:
  <em>He must be tired — <b>he worked all night</b></em>. Oʻzbekchada ham shunday qilamiz:
  "Charchagan boʻlsa kerak, chunki tun boʻyi ishladi". Faqat modalni aytib qoʻyish
  yetarli emas, sababini ham qoʻshing.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He mustn't be at home — his car has gone.</s></p>
  <p class="pe-good">He <b>can't be</b> at home — his car has gone.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She must to be very rich.</s></p>
  <p class="pe-good">She <b>must be</b> very rich.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>That doesn't can be true.</s></p>
  <p class="pe-good">That <b>can't be</b> true.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He must being tired.</s></p>
  <p class="pe-good">He <b>must be</b> tired. / He <b>must be feeling</b> tired.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He can't be knowing the answer.</s></p>
  <p class="pe-good">He <b>can't know</b> the answer. <em>(stative verb)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>The light is on in her room, so she <span class="pe-blank">?</span> at
     home.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>must be</strong> — the light is your evidence, so you are almost certain.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>You've just eaten a whole plate of plov — you
     <span class="pe-blank">?</span> hungry!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>can't be</strong> — the evidence makes it almost impossible. Never
         <s>mustn't be</s>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) You must be quiet. (b) You must be tired.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) is an obligation</strong> — I am telling you to be quiet.
         <strong>(b) is a deduction</strong> — I am guessing about how you feel. Same word,
         two jobs.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Make a deduction with evidence: <em>Sherbek's bag is here but he isn't in the
     classroom.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>He <b>must be</b> somewhere in the school — his bag is
         still here. He <b>can't have</b> gone home.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Order these from most to least certain: <em>might be · can't be · must be</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>must be (95%) → might be (50%) → can't be (5%).</strong></p>
      <p><em>Can't be</em> is at the bottom because it is certainty in the <b>negative</b>
         direction.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Deduction</b><span>xulosa, taxmin</span></li>
  <li><b>Evidence</b><span>dalil</span></li>
  <li><b>Certain / sure</b><span>ishonchi komil</span></li>
  <li><b>Must be</b><span>boʻlsa kerak</span></li>
  <li><b>Can't be</b><span>boʻlishi mumkin emas</span></li>
  <li><b>To guess</b><span>taxmin qilmoq</span></li>
  <li><b>Impossible</b><span>imkonsiz</span></li>
  <li><b>Olympiad</b><span>olimpiada</span></li>
  <li><b>Reason</b><span>sabab</span></li>
  <li><b>Context</b><span>kontekst, matn</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>must be</b> (95%) → <b>might/may/could be</b> (50%) → <b>can't be</b> (5%).</li>
    <li>The opposite of <em>must be</em> is <b>can't be</b> — never <s>mustn't be</s>.</li>
    <li><em>must</em> has two jobs: obligation and deduction. Context decides.</li>
    <li>Add <b>be + -ing</b> to guess about right now: <em>He must be sleeping.</em></li>
    <li>Always give the evidence — a deduction needs its reason.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-48: Modals in the Past: must have, should have, could have",
        "category": "english",
        "order": 48,
        "summary": (
            "Regret, criticism and detective work about yesterday — modal + have + V3, the "
            "structure that lets you talk about what did or didn't happen."
        ),
        "content": """
<h2>PE-48: Modals in the Past: must have, should have, could have</h2>

<p>Modals have no past tense of their own (PE-42). So how do you say <em>"I think he forgot"</em>
with confidence, or <em>"you made a mistake"</em> with kindness? English adds three words:
<mark>modal + have + V3</mark>. With that one pattern you can express regret, criticism, and
detective work about the past — and it is one of the most adult-sounding structures you will
learn.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The single formula <b>modal + have + V3</b></li>
    <li><b>must have / can't have / might have</b> — guessing about the past</li>
    <li><b>should have</b> — regret and gentle criticism</li>
    <li><b>could have</b> — it was possible, but it didn't happen</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Talking about the past</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">modal</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">have</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
</div>

LEGEND_HERE

<h3>1. One formula, many meanings</h3>

<p>Notice that <b>have</b> never changes — not <em>has</em>, not <em>had</em>. And the verb
after it is always the third form you learned in PE-32.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">She</span>
     <span class="pe-hl pe-hl--aux">must have</span>
     <span class="pe-hl pe-hl--v">forgotten</span> — she never misses a lesson.</p>
  <p class="pe-ex__uz">U unutgan boʻlsa kerak — u hech qachon darsni qoldirmaydi.</p>
</div>

<h3>2. Deduction about the past</h3>

<p>This is PE-47 moved backwards in time. Same three levels of certainty, same logic — you just
add <b>have + V3</b>.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">95</span>must have + V3</p>
    <p>I'm sure it happened. <em>He <b>must have missed</b> the bus.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">50</span>might / may / could have</p>
    <p>Perhaps it happened. <em>She <b>might have gone</b> home.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>can't have + V3</p>
    <p>I'm sure it didn't. <em>He <b>can't have said</b> that.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">!</span>Evidence first</p>
    <p>Give the reason: <em>— the door was open.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The window is broken. Somebody <b>must have thrown</b> a ball. It
     <b>can't have been</b> the wind.</p>
  <p class="pe-ex__uz">Deraza singan. Kimdir toʻp otgan boʻlsa kerak. Shamol boʻlishi mumkin
     emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>must have + V3</b> oʻzbekchadagi "<b>...gan boʻlsa kerak</b>" shakliga toʻgʻri keladi:
  <em>unut<b>gan boʻlsa kerak</b></em> → <em>must have forgotten</em>.
  <b>can't have + V3</b> esa "<b>...gan boʻlishi mumkin emas</b>". Ikkalasi ham
  oʻtmishdagi voqea haqidagi taxmin — siz u yerda boʻlmagansiz, lekin dalilga qarab
  xulosa chiqaryapsiz.
</div>

<h3>3. should have — regret and criticism</h3>

<p>This is the most emotionally useful one. <b>Should have + V3</b> means: it was the right
thing to do, and <b>it did not happen</b>. About yourself it is regret; about somebody else it
is criticism — so use it gently.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">should have — you didn't, and that was wrong</p>
    <ul>
      <li>I <b>should have studied</b> harder. <em>(I didn't)</em></li>
      <li>You <b>should have told</b> me. <em>(you didn't)</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">shouldn't have — you did, and that was wrong</p>
    <ul>
      <li>I <b>shouldn't have eaten</b> so much. <em>(I did)</em></li>
      <li>You <b>shouldn't have shouted</b> at him. <em>(you did)</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I failed the test. I <b>should have revised</b> more, and I
     <b>shouldn't have stayed</b> up all night.</p>
  <p class="pe-ex__uz">Testdan yiqildim. Koʻproq takrorlashim kerak edi va tun boʻyi
     uxlamasligim kerak edi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>should have + V3</b> = "<b>...ishim kerak edi</b>" (lekin qilmadim — afsus).
  <b>shouldn't have + V3</b> = "<b>...masligim kerak edi</b>" (lekin qilib qoʻydim).
  Diqqat: bu ikkalasi ham <b>faqat oʻtmish</b> haqida va har doim "aslida boshqacha
  boʻlishi kerak edi" degan maʼnoni beradi.
</div>

<h3>4. could have — the missed possibility</h3>

<p><b>Could have + V3</b> says something was possible, but it did not happen. It often carries
a note of "why didn't you?" or of relief that something bad was avoided.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <b>could have called</b> me — I was free all evening.
     — He <b>could have been</b> hurt! Luckily he wasn't.</p>
  <p class="pe-ex__uz">Menga qoʻngʻiroq qilsang boʻlardi — kechqurun boʻsh edim. —
     U jarohatlanishi mumkin edi! Yaxshiyamki, unday boʻlmadi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>could have + V3</b> oʻzbekchadagi "<b>...sang boʻlardi</b>" yoki "<b>...ishi mumkin
  edi</b>" shakliga toʻgʻri keladi: <em>You <b>could have called</b> me</em> — "Menga
  qoʻngʻiroq qilsang boʻlardi (lekin qilmading)". Yaʼni imkoniyat bor edi, ammo
  <b>amalga oshmadi</b>. Shuning uchun unda yengil taʼna ohangi bor.
</div>

<h3>5. The pronunciation trap</h3>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  In speech, <em>should have</em> sounds like <b>"should've"</b> — almost
  <em>"shoulda"</em>. That is why so many people write the terrible mistake
  <s>should of</s>. There is no <em>of</em> in this structure, ever. It is
  <b>should have</b> / <b>should've</b>.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I should went to the doctor.</s></p>
  <p class="pe-good">I <b>should have gone</b> to the doctor.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He must forgot my birthday.</s></p>
  <p class="pe-good">He <b>must have forgotten</b> my birthday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You should of asked me.</s></p>
  <p class="pe-good">You <b>should have</b> asked me.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She must has left already.</s></p>
  <p class="pe-good">She <b>must have</b> left already. <em>(never "has" here)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He mustn't have seen us — he didn't wave.</s></p>
  <p class="pe-good">He <b>can't have</b> seen us — he didn't wave.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>The ground is wet. It <span class="pe-blank">?</span> (rain) in the
     night.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>must have rained</strong> — the wet ground is strong evidence for something
         that happened earlier.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Express regret: <em>You didn't take an umbrella and you got wet.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I should have taken an umbrella.</strong></p>
      <p>The right action, which did not happen — that is exactly what <em>should have</em>
         expresses.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What does this mean? <em>You shouldn't have told her.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>You told her, and it was a mistake.</strong> The negative means the action
         <b>did</b> happen — and shouldn't have.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>He can't have went home — his coat is still here.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He can't have gone home — his coat is still here.</strong></p>
      <p>After <em>have</em> comes <b>V3</b> (<em>gone</em>), never V2 (<em>went</em>).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Choose: <em>Afsona isn't answering. She ___ her phone at home.</em>
     (must have left / should have left)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>must have left</strong> — you are guessing what happened.
         <em>Should have left</em> would mean it was a good idea that she didn't do.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Regret</b><span>afsus</span></li>
  <li><b>Criticism</b><span>tanqid</span></li>
  <li><b>To miss (a bus)</b><span>ulgurmay qolmoq</span></li>
  <li><b>To revise</b><span>takrorlamoq</span></li>
  <li><b>To fail (a test)</b><span>yiqilmoq</span></li>
  <li><b>To wave</b><span>qoʻl silkitmoq</span></li>
  <li><b>To avoid</b><span>oldini olmoq</span></li>
  <li><b>Luckily</b><span>yaxshiyamki</span></li>
  <li><b>To be hurt</b><span>jarohatlanmoq</span></li>
  <li><b>Mistake</b><span>xato</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>One formula for all of them: <b>modal + have + V3</b>. <em>have</em> never changes.</li>
    <li><b>must have</b> (sure it happened) · <b>might have</b> (perhaps) · <b>can't have</b>
        (sure it didn't).</li>
    <li><b>should have</b> = you didn't, and you should — regret or criticism.</li>
    <li><b>shouldn't have</b> = you did, and you shouldn't.</li>
    <li>It is <b>should've</b>, never <s>should of</s>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-49: Polite Requests, Offers and Permission",
        "category": "english",
        "order": 49,
        "summary": (
            "The same request at five levels of politeness — how to ask, offer and invite in "
            "English without ever sounding rude by accident."
        ),
        "content": """
<h2>PE-49: Polite Requests, Offers and Permission</h2>

<p>Here is something no grammar table will tell you: in English, being <b>direct</b> is often
felt as being <b>rude</b>. <em>"Give me your pen"</em> is perfect grammar and terrible
manners. English wraps its requests in modal verbs, and the longer the wrapping, the more
polite it sounds. This lesson gives you the whole ladder — for asking, offering, and asking
permission.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The politeness ladder for <b>requests</b></li>
    <li>How to ask for <b>permission</b> at every level</li>
    <li>How to make <b>offers</b> and <b>invitations</b></li>
    <li>The <em>Would you mind…?</em> trap, where "no" means "yes"</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The politeness ladder</span>
  <span class="pe-chip pe-chip--s">Can you…?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">Could you…?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">Would you…?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">Would you mind…?</span>
</div>

LEGEND_HERE

<h3>1. Asking somebody to do something</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Friends and family</p>
    <p><em><b>Can you</b> pass me the salt?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Neutral and safe</p>
    <p><em><b>Could you</b> help me, please?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>More formal</p>
    <p><em><b>Would you</b> open the window?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Most polite</p>
    <p><em><b>Would you mind</b> waiting a moment?</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Could you</b> tell me the way to the station, <b>please</b>?</p>
  <p class="pe-ex__uz">Vokzalga qanday borishni ayta olasizmi, iltimos?</p>
  <p class="pe-ex__why"><em>Could you</em> + <em>please</em> is the safest combination with a
     stranger.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida muloyimlik <b>-siz</b> va "iltimos" bilan beriladi: "och" → "oching" →
  "ochib yuborsangiz". Ingliz tilida esa <b>fe'lning oʻzi oʻzgarmaydi</b> — muloyimlik
  <b>modal feʼl</b> orqali qoʻshiladi: <em>can → could → would → would you mind</em>.
  Shuning uchun "please" qoʻshish yetarli emas; toʻgʻri modalni tanlang.
</div>

<h3>2. Asking for permission</h3>

<p>Here the subject changes to <b>I</b> — you are asking to do something yourself.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Everyday → formal</p>
    <ul>
      <li><b>Can I</b> borrow your pen?</li>
      <li><b>Could I</b> ask you something?</li>
      <li><b>May I</b> come in? <em>(most respectful)</em></li>
      <li><b>Do you mind if I</b> open the window?</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Ways to answer</p>
    <ul>
      <li><b>Yes:</b> Of course. / Certainly. / Sure. / Go ahead.</li>
      <li><b>No:</b> I'm afraid not. / Sorry, I'd rather you didn't.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>May I</b> leave early today? — <b>Of course</b>, no problem.</p>
  <p class="pe-ex__uz">— Bugun erta ketsam maylimi? — Albatta, muammo yoʻq.</p>
</div>

<h3>3. Offers and invitations</h3>

<p>Now you are the one giving. English uses <b>shall</b>, <b>would like</b> and <b>can</b>
here.</p>

<ol class="pe-steps">
  <li><b>Offering to do something:</b> <em><b>Shall I</b> carry that for you?</em> ·
      <em><b>Can I</b> help you?</em></li>
  <li><b>Offering a thing:</b> <em><b>Would you like</b> some tea?</em> ·
      <em><b>Would you like</b> a biscuit?</em></li>
  <li><b>Inviting:</b> <em><b>Would you like to</b> come to my birthday?</em></li>
  <li><b>Suggesting together:</b> <em><b>Shall we</b> go now?</em> ·
      <em><b>Why don't we</b> take a taxi?</em></li>
</ol>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <em>Do you want some tea?</em> is grammatically fine but sounds blunt to a guest. The warm,
  normal English offer is <b>Would you like…?</b> Learn it as one fixed phrase — it will make
  you sound polite instantly.
</div>

<h3>4. The "Would you mind…?" trap</h3>

<p>This phrase literally asks: "would it be a problem for you?" So the polite answer that means
<b>yes, I'll do it</b> is a <b>negative</b> one.</p>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>Would you mind</b> closing the door? — <b>Not at all.</b>
     <em>(= I'll close it happily)</em></p>
  <p class="pe-ex__uz">— Eshikni yopib yuborsangiz maylimi? — Albatta, bemalol.</p>
  <p class="pe-ex__why">Answering <em>"Yes"</em> here would mean "yes, it <b>is</b> a problem
     for me"!</p>
</div>

<p>Note the form too: after <b>mind</b> comes the <b>-ing</b> form, never the infinitive —
<em>Would you mind <b>waiting</b>?</em>, and for permission <em>Do you mind <b>if I</b>
wait?</em></p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Would you mind…?</b> soʻzma-soʻz "sizga malol kelmaydimi?" degani. Shuning uchun
  rozilik bildirish uchun <b>inkor</b> javob beriladi: <em>Not at all</em> / <em>Of course
  not</em> — "yoʻq, malol kelmaydi". Agar <em>Yes</em> desangiz, "ha, malol keladi" degan
  boʻlasiz. Va undan keyin feʼl <b>-ing</b> bilan keladi: <em>mind <b>waiting</b></em>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Rad etishni ham muloyim qilish kerak. Ingliz tilida quruq <em>No</em> juda qattiq
  eshitiladi — buning oʻrniga <b>I'm afraid…</b> ("afsuski...") bilan boshlang:
  <em><b>I'm afraid</b> I can't</em>, <em><b>I'm afraid not</b></em>,
  <em><b>Sorry, I'd rather you didn't</b></em>. Oʻzbekchadagi "uzr, iloji yoʻq" kabi
  yumshatuvchi iboraga oʻxshaydi.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Give me your book.</s> <em>(to a stranger)</em></p>
  <p class="pe-good"><b>Could you</b> lend me your book, <b>please</b>?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Would you mind to open the window?</s></p>
  <p class="pe-good">Would you mind <b>opening</b> the window?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you want to drink some tea?</s> <em>(to a guest)</em></p>
  <p class="pe-good"><b>Would you like</b> some tea?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Shall you help me?</s></p>
  <p class="pe-good"><b>Could you</b> help me? <em>(shall is only for I and we)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will like a coffee, please.</s></p>
  <p class="pe-good">I<b>'d like</b> a coffee, please. <em>(would like)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     You need a stranger to repeat something. What do you say?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Could you say that again, please?</strong> (or <em>Sorry, would you mind
         repeating that?</em>)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     — <em>Would you mind waiting five minutes?</em> How do you say yes?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Not at all.</strong> / <strong>Of course not.</strong> / <strong>No
         problem.</strong></p>
      <p>A negative answer means agreement, because the question asks whether it bothers
         you.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>Would you like coming to my party?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Would you like to come to my party?</strong></p>
      <p><em>Would like</em> takes <b>to + verb</b>; only <em>mind</em> takes <b>-ing</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Offer to help someone carrying heavy bags.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Shall I help you with those?</strong> / <strong>Can I give you a
         hand?</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which is most polite? <em>(a) Open the window. (b) Can you open the window?
     (c) Would you mind opening the window?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(c)</strong> is the most polite, <strong>(b)</strong> is normal and friendly,
         <strong>(a)</strong> is an order — fine for a close friend, rude to a stranger.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Request</b><span>iltimos</span></li>
  <li><b>Offer</b><span>taklif</span></li>
  <li><b>Invitation</b><span>taklifnoma</span></li>
  <li><b>Permission</b><span>ruxsat</span></li>
  <li><b>Polite</b><span>xushmuomala</span></li>
  <li><b>Rude / blunt</b><span>qoʻpol</span></li>
  <li><b>To mind</b><span>malol kelmoq</span></li>
  <li><b>Of course</b><span>albatta</span></li>
  <li><b>I'm afraid not</b><span>afsuski, yoʻq</span></li>
  <li><b>To give a hand</b><span>yordam bermoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Requests: <b>Can you → Could you → Would you → Would you mind…?</b></li>
    <li>Permission: <b>Can I → Could I → May I → Do you mind if I…?</b></li>
    <li>Offers: <b>Shall I…?</b> · <b>Would you like…?</b> — not <em>Do you want…?</em></li>
    <li>After <b>mind</b> use <b>-ing</b>; after <b>would like</b> use <b>to + verb</b>.</li>
    <li><em>Would you mind…?</em> — answer <b>"Not at all"</b> to say yes.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-50: shall, will, would: Willingness and Habit",
        "category": "english",
        "order": 50,
        "summary": (
            "Three related modals and their less obvious jobs — offering with shall, refusing "
            "with won't, being polite with would, and the 'd that hides two words."
        ),
        "content": """
<h2>PE-50: shall, will, would: Willingness and Habit</h2>

<p>You already use <b>will</b> for the future and <b>would</b> for polite requests. But these
three little words have quieter jobs that native speakers use every day and textbooks rarely
explain: offering, refusing, describing what people typically do — and one small trap where
<b>'d</b> can mean two completely different words.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>shall</b> for offers and suggestions</li>
    <li><b>will / won't</b> for willingness and refusal — even from objects</li>
    <li><b>would</b> for politeness, past habits and preferences</li>
    <li>The <b>'d</b> trap: <em>would</em> or <em>had</em>?</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three jobs</span>
  <span class="pe-chip pe-chip--s">Shall I / we …?</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">offer</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">won't</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">refuses</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">would like</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">want, politely</span>
</div>

LEGEND_HERE

<h3>1. shall — only with I and we</h3>

<p>In modern English, <b>shall</b> has one main living use: asking whether to do something. It
appears almost only in questions, and only with <b>I</b> and <b>we</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Shall I</b> close the window? — <b>Shall we</b> start? —
     What <b>shall we</b> do tonight?</p>
  <p class="pe-ex__uz">Derazani yopaymi? — Boshlaymizmi? — Bugun kechqurun nima qilamiz?</p>
  <p class="pe-ex__why"><em>Shall I…?</em> offers help; <em>Shall we…?</em> suggests doing
     something together.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Shall I…?</b> oʻzbekchadagi "<b>...aymi?</b>" shakliga toʻgʻri keladi: "Yopaymi?" →
  <em>Shall I close it?</em>, "Boshlaymizmi?" → <em>Shall we start?</em> Diqqat:
  <b>shall</b> faqat <b>I</b> va <b>we</b> bilan ishlatiladi — <s>Shall you…?</s>,
  <s>Shall he…?</s> degan gaplar yoʻq.
</div>

<h3>2. will — willingness, and won't — refusal</h3>

<p>Beyond the future, <b>will</b> expresses that somebody is <b>willing</b> to do something.
And its negative, <b>won't</b>, means an active <b>refusal</b> — a strong, human meaning.</p>

<div class="pe-ex">
  <p class="pe-ex__en">— Who wants to help? — I <b>will</b>! — She <b>won't</b> speak to me;
     she's still angry.</p>
  <p class="pe-ex__uz">— Kim yordam bermoqchi? — Men! — U men bilan gaplashmayapti; hamon
     xafa.</p>
</div>

<p>Beautifully, English extends this to <b>objects</b>, as if they had their own will:</p>

<div class="pe-ex">
  <p class="pe-ex__en">The door <b>won't</b> open. My computer <b>won't</b> start.</p>
  <p class="pe-ex__uz">Eshik ochilmayapti. Kompyuterim yoqilmayapti.</p>
  <p class="pe-ex__why">Not a prediction — it means "it refuses to", right now.</p>
</div>

<h3>3. will for typical behaviour</h3>

<p>There is one more quiet use. <b>Will</b> can describe what somebody <b>typically does</b> —
their character, not the future at all. It is close to the Present Simple, but it adds "that's
just how they are".</p>

<div class="pe-ex">
  <p class="pe-ex__en">My grandfather <b>will sit</b> in the garden for hours, just watching
     the birds.</p>
  <p class="pe-ex__uz">Bobom bogʻda soatlab oʻtiradi, shunchaki qushlarni tomosha qiladi.</p>
  <p class="pe-ex__why">Compare the past version, which you met in PE-25:
     <em>he <b>would</b> sit for hours</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>won't</b> ning "rad etadi" maʼnosi oʻzbekchada odatda <b>oʻzlik</b> shaklida
  beriladi: <em>The door <b>won't</b> open</em> = "Eshik <b>ochilmayapti</b>",
  <em>The engine <b>won't</b> start</em> = "Dvigatel <b>yurmayapti</b>". Bu kelasi zamon
  emas — <b>hozir</b> boʻlayotgan holat. Shuning uchun "eshik ochilmaydi" deb tarjima
  qilmang.
</div>

<h3>4. would — four everyday jobs</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Polite requests</p>
    <p><em><b>Would</b> you help me?</em> (PE-49)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>would like = want</p>
    <p><em>I<b>'d like</b> a coffee, please.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Past habits</p>
    <p><em>Every summer we <b>would</b> go to the village.</em> (PE-25)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Preference</p>
    <p><em>I<b>'d rather</b> stay at home.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>Would you like</b> tea or coffee? — I<b>'d like</b> tea, thanks.
     Actually, I<b>'d rather</b> have water.</p>
  <p class="pe-ex__uz">— Choy ichasizmi yoki qahva? — Choy ichsam boʻlardi, rahmat. Aslida,
     suv ichganim maʼqul.</p>
  <p class="pe-ex__why"><b>would rather</b> + base verb = "I prefer to" — no <em>to</em> after
     it.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>I want</b> ingliz tilida qoʻpolroq eshitiladi — restoran yoki doʻkonda deyarli har doim
  <b>I'd like</b> ishlatiladi ("...olsam boʻladimi", "...istardim").
  <b>I'd rather</b> esa "<b>...ganim maʼqul</b>" degani va undan keyin feʼl
  <b>toʻgʻridan-toʻgʻri</b> keladi: <em>I'd rather <b>stay</b></em>, <s>I'd rather to
  stay</s> emas.
</div>

<h3>5. The 'd trap</h3>

<p>The short form <b>'d</b> hides two different words. Look at what follows it:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">'d = would</p>
    <ul>
      <li>I<b>'d like</b> a coffee. <em>(would like)</em></li>
      <li>I<b>'d rather</b> walk. <em>(would rather)</em></li>
      <li>He<b>'d help</b> you. <em>(would help)</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">'d = had</p>
    <ul>
      <li>You<b>'d better</b> go. <em>(had better — PE-46)</em></li>
      <li>I<b>'d finished</b> by six. <em>(had + V3 — PE-38)</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Two quick tests. If <b>better</b> comes next, it is <em>had</em>. If a <b>V3</b> comes next,
  it is <em>had</em>. Anything else — a base verb, <em>like</em>, <em>rather</em> — it is
  <em>would</em>.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Shall you come with us?</s></p>
  <p class="pe-good"><b>Will you</b> come with us? / <b>Would you like to</b> come with us?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will like some water, please.</s></p>
  <p class="pe-good">I<b>'d like</b> some water, please.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I would rather to go home.</s></p>
  <p class="pe-good">I<b>'d rather go</b> home.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I would like going to the cinema tonight.</s></p>
  <p class="pe-good">I<b>'d like to go</b> to the cinema tonight.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The door doesn't want to open.</s></p>
  <p class="pe-good">The door <b>won't</b> open.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Offer to carry your friend's bag.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Shall I carry your bag?</strong> (or <em>Would you like me to carry
         it?</em>)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What does this mean? <em>My car won't start this morning.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It refuses to start — right now, not in the future.</strong> English treats
         the object as if it were unwilling.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     would or had? <em>(a) I'd better hurry. (b) I'd love to come.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) had</strong> (<em>had better</em>) · <strong>(b) would</strong>
         (<em>would love</em>).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Make it polite: <em>I want a cup of tea.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'd like a cup of tea, please.</strong></p>
      <p><em>I want</em> is not wrong grammar — it is just too direct for a guest or a
         shop.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Complete with <em>would rather</em>: <em>— Cinema or park? — I ___ (go) to the
     park.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'd rather go to the park.</strong></p>
      <p>No <em>to</em> after <em>would rather</em> — the base verb comes straight
         after it.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Willingness</b><span>xohish, rozilik</span></li>
  <li><b>To refuse</b><span>rad etmoq</span></li>
  <li><b>Offer</b><span>taklif</span></li>
  <li><b>Suggestion</b><span>taklif, maslahat</span></li>
  <li><b>Would like</b><span>...istardim</span></li>
  <li><b>Would rather</b><span>...ganim maʼqul</span></li>
  <li><b>Preference</b><span>afzallik</span></li>
  <li><b>Typical behaviour</b><span>odatiy xatti-harakat</span></li>
  <li><b>Actually</b><span>aslida</span></li>
  <li><b>Angry</b><span>xafa, gʻazablangan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Shall I / Shall we…?</b> = offers and suggestions — only with <em>I</em> and
        <em>we</em>.</li>
    <li><b>will</b> = willingness · <b>won't</b> = refuses, even for objects
        (<em>the door won't open</em>).</li>
    <li><b>would like</b> = the polite <em>want</em>; <b>would rather</b> = prefer, + base
        verb.</li>
    <li><b>'d</b> = <em>had</em> before <b>better</b> or a <b>V3</b>; otherwise
        <em>would</em>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
