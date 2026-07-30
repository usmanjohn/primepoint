# -*- coding: utf-8 -*-
"""Prime English — Block F, lessons 76–80 (prepositions, phrasal verbs, quantity, articles).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_76_80.py --author=prime
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
        "title": "PE-76: Adjective + Preposition, Verb + Preposition",
        "category": "english",
        "order": 76,
        "summary": (
            "The fixed partners you simply have to know — good at, depend on, listen to — plus "
            "the verbs that need no preposition at all, where Uzbek expects one."
        ),
        "content": """
<h2>PE-76: Adjective + Preposition, Verb + Preposition</h2>

<p>Why <em>good <b>at</b></em> maths but <em>interested <b>in</b></em> maths? Why do you
<em>listen <b>to</b></em> music but <em>discuss</em> a problem with no preposition at all? There
is no logic to find — these are <mark>fixed partners</mark>, and the only way is to learn the
pair as one unit. The good news: there are not many, and they repeat constantly.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The essential <b>adjective + preposition</b> pairs</li>
    <li>The essential <b>verb + preposition</b> pairs</li>
    <li>The verbs that take <b>no</b> preposition — a classic Uzbek-speaker trap</li>
    <li>Why a verb after these prepositions must take <b>-ing</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Learn them as pairs</span>
  <span class="pe-chip pe-chip--s">good at</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">depend on</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">afraid of</span>
</div>

LEGEND_HERE

<h3>1. Adjective + preposition</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Preposition</th><th>Adjectives</th><th>Example</th></tr>
  <tr><td><b>at</b></td><td>good, bad, brilliant, terrible</td><td>She's <b>good at</b> maths.</td></tr>
  <tr><td><b>in</b></td><td>interested</td><td>I'm <b>interested in</b> history.</td></tr>
  <tr><td><b>of</b></td><td>afraid, proud, full, tired, aware</td><td>He's <b>afraid of</b> dogs.</td></tr>
  <tr><td><b>about</b></td><td>worried, excited, sorry, angry</td><td>I'm <b>worried about</b> the exam.</td></tr>
  <tr><td><b>for</b></td><td>famous, late, ready, sorry</td><td>Bukhara is <b>famous for</b> its mosques.</td></tr>
  <tr><td><b>to</b></td><td>similar, married, kind, rude</td><td>She's <b>married to</b> a doctor.</td></tr>
  <tr><td><b>from</b></td><td>different, absent</td><td>Mine is <b>different from</b> yours.</td></tr>
  <tr><td><b>with</b></td><td>pleased, satisfied, bored</td><td>I'm <b>pleased with</b> my mark.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona is <b>good at</b> languages and <b>interested in</b> Korean, but
     she's <b>worried about</b> the exam.</p>
  <p class="pe-ex__uz">Afsona tillarni yaxshi biladi va koreys tiliga qiziqadi, lekin
     imtihondan xavotirda.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>married to</b>, not <s>married with</s>. This is one of the most common errors worldwide:
  <em>She's married <b>to</b> an engineer</em> ✓. And <b>different from</b> is the standard form
  (though <em>different to</em> is heard in Britain).
</div>

<h3>2. Verb + preposition</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Preposition</th><th>Verbs</th><th>Example</th></tr>
  <tr><td><b>to</b></td><td>listen, belong, happen, talk, reply</td><td><b>Listen to</b> me!</td></tr>
  <tr><td><b>for</b></td><td>wait, look (= search), ask, pay, apologise</td><td>I'm <b>waiting for</b> the bus.</td></tr>
  <tr><td><b>on</b></td><td>depend, rely, concentrate, spend</td><td>It <b>depends on</b> the weather.</td></tr>
  <tr><td><b>at</b></td><td>look, laugh, shout, arrive (small places)</td><td>Don't <b>laugh at</b> him.</td></tr>
  <tr><td><b>about</b></td><td>think, worry, complain, talk, dream</td><td>I'm <b>thinking about</b> you.</td></tr>
  <tr><td><b>with</b></td><td>agree, argue, help, share</td><td>I <b>agree with</b> you.</td></tr>
  <tr><td><b>in</b></td><td>believe, succeed, arrive (cities)</td><td>Do you <b>believe in</b> luck?</td></tr>
  <tr><td><b>from</b></td><td>borrow, suffer, escape, differ</td><td>I <b>borrowed</b> it <b>from</b> Jasur.</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu juftliklarni <b>mantiq bilan topib boʻlmaydi</b> — ular tarixiy jihatdan shunday
  shakllangan. Yechim: soʻzni alohida emas, <b>predlogi bilan birga</b> yodlang va ovoz
  chiqarib ayting: "<em>good <b>at</b></em>", "<em>depend <b>on</b></em>",
  "<em>listen <b>to</b></em>". Oʻzbekchada "musiqa tinglash" — predlogsiz, ingliz tilida
  esa <b>to</b> shart.
</div>

<h3>3. The verbs that need NO preposition</h3>

<p>Here is the trap that catches Uzbek speakers most often. Because Uzbek adds a case ending
(<em>...ni, ...ga, ...da</em>), it feels natural to add a preposition in English too. These verbs
take a <b>direct object</b> with nothing in front of it.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✗ Wrong — no preposition needed</p>
    <ul>
      <li><s>discuss about the problem</s></li>
      <li><s>enter into the room</s></li>
      <li><s>marry with him</s></li>
      <li><s>phone to me</s> · <s>answer to the question</s></li>
      <li><s>reach to the station</s> · <s>tell to me</s></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✓ Right</p>
    <ul>
      <li><b>discuss</b> the problem</li>
      <li><b>enter</b> the room</li>
      <li><b>marry</b> him</li>
      <li><b>phone</b> me · <b>answer</b> the question</li>
      <li><b>reach</b> the station · <b>tell</b> me</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">We <b>discussed the plan</b> and then <b>entered the hall</b>. Please
     <b>answer my question</b> and <b>tell me</b> the truth.</p>
  <p class="pe-ex__uz">Rejani muhokama qildik, keyin zalga kirdik. Savolimga javob bering va
     menga haqiqatni aytingi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sabab aniq: oʻzbekchada "xona<b>ga</b> kirdim", "savol<b>ga</b> javob berdim",
  "men<b>ga</b> aytdi" — hamma joyda qoʻshimcha bor. Shuning uchun ingliz tilida ham
  <em>to</em> qoʻshib yuborish oson. Lekin bu feʼllar predlogsiz ishlatiladi:
  <b>enter</b> the room, <b>answer</b> the question, <b>tell</b> me. Roʻyxatni yodlab
  qoʻyish arziydi.
</div>

<h3>4. arrive at, arrive in — and a method for learning</h3>

<p>One pair deserves its own note. <b>Arrive</b> never takes <em>to</em>: it takes <b>at</b> for
small places and <b>in</b> for cities and countries.</p>

<div class="pe-ex">
  <p class="pe-ex__en">We <b>arrived at</b> the station at six and <b>arrived in</b> Samarkand
     an hour later.</p>
  <p class="pe-ex__uz">Soat oltida vokzalga yetib keldik va bir soatdan keyin Samarqandga yetib
     bordik.</p>
  <p class="pe-ex__why">Never <s>arrive to</s>. But note: <em>get <b>to</b></em> and
     <em>go <b>to</b></em> ✓ — different verbs, different partners.</p>
</div>

<p>And here is the method that actually works for all of these pairs:</p>

<ol class="pe-steps">
  <li><b>Never write the word alone</b> in your vocabulary notebook. Write
      <em>good <u>at</u></em>, <em>depend <u>on</u></em> — the preposition is part of the
      word.</li>
  <li><b>Group by preposition,</b> not by verb. Say the <em>on</em> family aloud:
      <em>depend on, rely on, concentrate on, spend on</em>.</li>
  <li><b>Learn the no-preposition list separately</b> — it is short, and it is where Uzbek
      speakers lose the most marks.</li>
  <li><b>Use each one in a sentence about yourself</b> the same day.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Amaliy maslahat: lugʻat daftaringizga soʻzni <b>yolgʻiz yozmang</b>. "good" emas,
  "<b>good at</b>" deb yozing; "depend" emas, "<b>depend on</b>". Predlog — soʻzning
  bir qismi. Shu bitta odat bilan bu mavzudagi xatolaringiz keskin kamayadi.
</div>

<h3>5. After these prepositions, use -ing</h3>

<p>Remember the unbreakable rule from PE-64: a verb straight after any preposition takes
<b>-ing</b>. That applies to every pair in this lesson.</p>

<div class="pe-ex">
  <p class="pe-ex__en">She's good <b>at drawing</b>. — I'm tired <b>of waiting</b>. — Thank you
     <b>for helping</b>. — He apologised <b>for being</b> late.</p>
  <p class="pe-ex__uz">U rasm chizishda zoʻr. — Kutishdan charchadim. — Yordam berganingiz
     uchun rahmat. — U kechikkani uchun kechirim soʻradi.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>We discussed about the homework.</s></p>
  <p class="pe-good">We <b>discussed the homework</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My sister is married with a teacher.</s></p>
  <p class="pe-good">My sister is <b>married to</b> a teacher.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'm listening music.</s></p>
  <p class="pe-good">I'm <b>listening to</b> music.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He's good in football.</s></p>
  <p class="pe-good">He's <b>good at</b> football.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'm interested to learn Korean.</s></p>
  <p class="pe-good">I'm <b>interested in learning</b> Korean.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Fill in: <em>Sherbek is afraid <span class="pe-blank">?</span> spiders but proud
     <span class="pe-blank">?</span> his brother.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>of … of.</strong> Both <em>afraid</em> and <em>proud</em> take <b>of</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>Let's discuss about our plans and then phone to Afsona.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Let's discuss our plans and then phone Afsona.</strong></p>
      <p>Neither verb takes a preposition — this is the Uzbek case-ending habit showing
         through.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Fill in: <em>It depends <span class="pe-blank">?</span> the weather, so don't rely
     <span class="pe-blank">?</span> me.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>on … on.</strong> <em>Depend</em> and <em>rely</em> share the same
         partner.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Complete: <em>I'm not very good <span class="pe-blank">?</span> (cook), but I'm
     interested <span class="pe-blank">?</span> (learn).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>at cooking … in learning.</strong> Both prepositions force the <b>-ing</b>
         form.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which is right? <em>(a) Wait me! (b) Wait for me!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) Wait for me!</strong> <em>Wait</em> always takes <b>for</b> before a
         person or thing.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Dependent preposition</b><span>bogʻliq predlog</span></li>
  <li><b>Fixed pair</b><span>doimiy juftlik</span></li>
  <li><b>To depend on</b><span>bogʻliq boʻlmoq</span></li>
  <li><b>To rely on</b><span>ishonmoq, tayanmoq</span></li>
  <li><b>To apologise for</b><span>...uchun kechirim soʻramoq</span></li>
  <li><b>Proud of</b><span>...dan faxrlanadigan</span></li>
  <li><b>Similar to</b><span>...ga oʻxshash</span></li>
  <li><b>Different from</b><span>...dan farqli</span></li>
  <li><b>To discuss</b><span>muhokama qilmoq</span></li>
  <li><b>Direct object</b><span>vositasiz toʻldiruvchi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>These prepositions have <b>no logic</b> — learn the pair as one unit.</li>
    <li>Key pairs: <b>good at, interested in, afraid of, worried about, married to</b>.</li>
    <li><b>listen to, wait for, depend on, agree with, laugh at, belong to</b>.</li>
    <li><b>No preposition</b>: discuss, enter, marry, phone, answer, reach, tell.</li>
    <li>After any preposition, a verb takes <b>-ing</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-77: Phrasal Verbs: How They Actually Work",
        "category": "english",
        "order": 77,
        "summary": (
            "Why 'get up', 'get on' and 'get over' mean completely different things — the four "
            "types of phrasal verb and the pronoun rule that decides word order."
        ),
        "content": """
<h2>PE-77: Phrasal Verbs: How They Actually Work</h2>

<p>Take the small verb <em>get</em>. Add one word and you get <em>get <b>up</b></em> (leave your
bed), <em>get <b>on</b></em> (board a bus), <em>get <b>over</b></em> (recover from), <em>get
<b>on with</b></em> (have a good relationship). This is how English quietly builds thousands of
verbs from a handful of small ones — and native speakers use them constantly. This lesson gives
you the <mark>system</mark> behind them.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What a phrasal verb is and why the meaning changes</li>
    <li>The <b>four types</b>, and which ones can be split</li>
    <li>The pronoun rule — the single most useful thing here</li>
    <li>How to learn them by <b>particle</b> instead of one by one</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">A phrasal verb</span>
  <span class="pe-chip pe-chip--v">verb</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">particle (up, off, out…)</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">new meaning</span>
</div>

LEGEND_HERE

<h3>1. The meaning is often not literal</h3>

<div class="pe-ex">
  <p class="pe-ex__en">Literal: <em>She <b>looked up</b> at the sky.</em> — Idiomatic:
     <em>She <b>looked up</b> the word in a dictionary.</em></p>
  <p class="pe-ex__uz">U osmonga qaradi. — U soʻzni lugʻatdan qidirib topdi.</p>
  <p class="pe-ex__why">Same two words, completely different meanings. Context decides.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Frazali feʼlni <b>soʻzma-soʻz</b> tarjima qilib boʻlmaydi. <em>look</em> = qaramoq,
  <em>up</em> = yuqoriga, lekin <em>look up</em> = "lugʻatdan qidirmoq". Shuning uchun
  ularni <b>yangi soʻz</b> sifatida yodlang — xuddi oʻzbekchadagi "koʻz yugurtirmoq" yoki
  "qoʻl urmoq" kabi iboralarni alohida oʻrgangandek.
</div>

<h3>2. The four types</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>No object</p>
    <p><em>get up, sit down, grow up, break down</em><br>
       <em>My car <b>broke down</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Separable</p>
    <p><em>turn on, pick up, put off, throw away</em><br>
       <em>Turn <b>the TV</b> on.</em> = <em>Turn on <b>the TV</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Inseparable</p>
    <p><em>look after, look for, get on, deal with</em><br>
       <em>Look after <b>the baby</b>.</em> only</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Three words</p>
    <p><em>put up with, look forward to, run out of</em><br>
       Never split.</p>
  </div>
</div>

<h3>3. The pronoun rule — the key practical point</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  With a <b>separable</b> phrasal verb, a <b>pronoun</b> (it, him, them…) must go
  <b>in the middle</b>. It can never follow the particle.
  <em>Turn <b>it</b> on</em> ✓ · <s>Turn on it</s> ✗
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">With a noun — both orders fine</p>
    <ul>
      <li>Turn on <b>the light</b>. ✓</li>
      <li>Turn <b>the light</b> on. ✓</li>
      <li>Pick up <b>your bag</b>. ✓</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">With a pronoun — middle only</p>
    <ul>
      <li>Turn <b>it</b> on. ✓ / <s>Turn on it</s> ✗</li>
      <li>Pick <b>it</b> up. ✓ / <s>Pick up it</s> ✗</li>
      <li>Throw <b>them</b> away. ✓</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— Where are my glasses? — <b>Put them on</b>, they're on your head! —
     I'll <b>pick you up</b> at eight.</p>
  <p class="pe-ex__uz">— Koʻzoynagim qani? — Kiyib ol, boshingda-ku! — Seni soat sakkizda olib
     ketaman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qoidani albatta yodlang, chunki u <b>juda tez-tez</b> kerak boʻladi: olmosh
  (<em>it, him, her, them, me, you</em>) <b>doim oʻrtada</b> turadi. <em>Pick <b>me</b>
  up</em>, <em>Turn <b>it</b> off</em>, <em>Call <b>her</b> back</em>. Ot boʻlsa esa
  ikki xil ham boʻladi. Faqat inseparable feʼllar (<em>look after</em>) bundan mustasno.
</div>

<h3>4. Inseparable ones never split</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I'm looking my keys for.</s> · <s>She looks the baby after.</s></p>
  <p class="pe-good">I'm <b>looking for</b> my keys. · She <b>looks after</b> the baby.</p>
</div>

<p>How do you know which is which? Usually, if the particle is a real preposition
(<em>for, after, at, to, with</em>), the verb is <b>inseparable</b>. If it is a direction word
(<em>up, down, on, off, out, away</em>), it is often separable. A dictionary confirms it — look
for the mark <em>(sth)</em> in the middle.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Feʼl ajratiladigan yoki yoʻqligini bilishning oson usuli: uni <b>olmosh bilan sinab
  koʻring</b>. <em>Turn <b>it</b> on</em> — quloqqa toʻgʻri eshitiladi, demak
  <b>ajratiladi</b>. <em>Look <b>it</b> after</em> — gʻalati eshitiladi, demak
  <b>ajratilmaydi</b> (<em>look after it</em> boʻladi). Lugʻatlarda ham bu
  <em>(sth)</em> belgisi bilan koʻrsatiladi.
</div>

<h3>5. Learn by particle, not one by one</h3>

<p>The particles carry rough meanings of their own. Noticing that turns memorising into
understanding.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Particle</th><th>Rough idea</th><th>Examples</th></tr>
  <tr><td><b>up</b></td><td>completely, finished</td><td>eat up, drink up, use up, finish up</td></tr>
  <tr><td><b>off</b></td><td>away, separating</td><td>take off, set off, turn off, cut off</td></tr>
  <tr><td><b>on</b></td><td>continuing, connecting</td><td>carry on, go on, put on, turn on</td></tr>
  <tr><td><b>out</b></td><td>outward, to the end</td><td>find out, work out, go out, run out</td></tr>
  <tr><td><b>down</b></td><td>reducing, recording</td><td>slow down, write down, break down</td></tr>
  <tr><td><b>away</b></td><td>removing</td><td>throw away, give away, put away</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Eat up</b> your soup! — We <b>set off</b> at dawn. — Please
     <b>write down</b> the new words. — I need to <b>find out</b> the answer.</p>
  <p class="pe-ex__uz">Shoʻrvani ichib boʻl! — Tong saharda yoʻlga chiqdik. — Yangi soʻzlarni
     yozib oling. — Javobni bilib olishim kerak.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Can you turn off it, please?</s></p>
  <p class="pe-good">Can you <b>turn it off</b>, please?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'm looking forward to see you.</s></p>
  <p class="pe-good">I'm looking forward <b>to seeing</b> you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She looked the word in the dictionary up.</s></p>
  <p class="pe-good">She <b>looked up the word</b> / <b>looked the word up</b> in the
     dictionary.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I can't put with this noise up.</s></p>
  <p class="pe-good">I can't <b>put up with</b> this noise. <em>(never split)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My car broke down it yesterday.</s></p>
  <p class="pe-good">My car <b>broke down</b> yesterday. <em>(no object at all)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Rewrite with a pronoun: <em>Please turn off the radio.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Please turn it off.</strong> The pronoun must go in the middle.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Which is wrong? <em>(a) I'm looking after them. (b) I'm looking them after.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) is wrong.</strong> <em>Look after</em> is inseparable — nothing ever goes
         between the two words, not even a pronoun.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What does <em>up</em> add? <em>Drink up your tea!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Completely — finish it all.</strong> <em>Drink your tea</em> is neutral;
         <em>drink it up</em> means to the last drop.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which type? <em>My computer broke down.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Type 1 — no object.</strong> You cannot "break down something" in this
         meaning, so nothing can follow it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>I'll call back you tomorrow.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'll call you back tomorrow.</strong> <em>Call back</em> is separable, and a
         pronoun goes in the middle.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Phrasal verb</b><span>frazali feʼl</span></li>
  <li><b>Particle</b><span>qoʻshimcha soʻz</span></li>
  <li><b>Separable</b><span>ajratiladigan</span></li>
  <li><b>Inseparable</b><span>ajratilmaydigan</span></li>
  <li><b>Literal</b><span>soʻzma-soʻz</span></li>
  <li><b>Idiomatic</b><span>koʻchma maʼnoli</span></li>
  <li><b>To look up</b><span>lugʻatdan qidirmoq</span></li>
  <li><b>To put up with</b><span>chidamoq</span></li>
  <li><b>To break down</b><span>buzilmoq</span></li>
  <li><b>To set off</b><span>yoʻlga chiqmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>A phrasal verb = verb + particle with a <b>new meaning</b> — learn it as one word.</li>
    <li>Four types: no object · separable · inseparable · three-word.</li>
    <li><b>Pronouns always go in the middle</b>: <em>turn it off</em>, never <s>turn off
        it</s>.</li>
    <li>Inseparable ones (<b>look after, put up with</b>) never split.</li>
    <li>Learn by particle: <b>up</b> = completely, <b>off</b> = away, <b>out</b> = to the
        end.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-78: 40 Everyday Phrasal Verbs by Topic",
        "category": "english",
        "order": 78,
        "summary": (
            "The phrasal verbs you will actually use, grouped by situation — morning routine, "
            "school, friendships, travel, problems and phone calls."
        ),
        "content": """
<h2>PE-78: 40 Everyday Phrasal Verbs by Topic</h2>

<p>PE-77 gave you the machinery. Now the useful part: <b>which ones to learn first</b>. There are
thousands of phrasal verbs, but a small group does most of the daily work. Here are forty,
grouped by the situation where you will meet them — because learning them by topic sticks far
better than learning them alphabetically.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>40 high-frequency phrasal verbs, grouped by topic</li>
    <li>How to use each one in a natural sentence</li>
    <li>Which ones are separable and which are not</li>
    <li>A method for learning them in small daily batches</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Six topics</span>
  <span class="pe-chip pe-chip--s">routine</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">study</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">people</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--adv">travel</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">problems</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">phone</span>
</div>

<h3>1. Your daily routine</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Phrasal verb</th><th>Oʻzbekcha</th><th>Example</th></tr>
  <tr><td>wake up</td><td>uygʻonmoq</td><td>I <b>wake up</b> at six.</td></tr>
  <tr><td>get up</td><td>oʻrnidan turmoq</td><td>Then I <b>get up</b> slowly.</td></tr>
  <tr><td>put on</td><td>kiymoq</td><td><b>Put on</b> your coat.</td></tr>
  <tr><td>take off</td><td>yechmoq</td><td><b>Take</b> your shoes <b>off</b>.</td></tr>
  <tr><td>get dressed</td><td>kiyinmoq</td><td>I <b>get dressed</b> quickly.</td></tr>
  <tr><td>tidy up</td><td>tartibga solmoq</td><td><b>Tidy up</b> your room!</td></tr>
  <tr><td>go to bed</td><td>yotmoq</td><td>I <b>go to bed</b> at ten.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>wake up</b> at six, <b>get up</b>, <b>put on</b> my uniform and
     <b>set off</b> for school.</p>
  <p class="pe-ex__uz">Soat oltida uygʻonaman, oʻrnimdan turaman, formamni kiyaman va maktabga
     joʻnayman.</p>
</div>

<h3>2. School and study</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Phrasal verb</th><th>Oʻzbekcha</th><th>Example</th></tr>
  <tr><td>look up</td><td>lugʻatdan qidirmoq</td><td><b>Look</b> the word <b>up</b>.</td></tr>
  <tr><td>write down</td><td>yozib olmoq</td><td><b>Write down</b> the date.</td></tr>
  <tr><td>hand in</td><td>topshirmoq</td><td><b>Hand in</b> your essays.</td></tr>
  <tr><td>find out</td><td>bilib olmoq</td><td>I want to <b>find out</b> the truth.</td></tr>
  <tr><td>catch up (with)</td><td>yetib olmoq</td><td>I must <b>catch up with</b> the class.</td></tr>
  <tr><td>work out</td><td>hisoblab chiqmoq</td><td>Can you <b>work out</b> the answer?</td></tr>
  <tr><td>revise for</td><td>takrorlamoq</td><td>I'm <b>revising for</b> the test.</td></tr>
</table>
</div>

<h3>3. People and friendships</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Phrasal verb</th><th>Oʻzbekcha</th><th>Example</th></tr>
  <tr><td>get on (with)</td><td>chiqishmoq</td><td>I <b>get on well with</b> my sister.</td></tr>
  <tr><td>fall out (with)</td><td>urishib qolmoq</td><td>They <b>fell out</b> last week.</td></tr>
  <tr><td>make up</td><td>yarashmoq</td><td>Then they <b>made up</b>.</td></tr>
  <tr><td>grow up</td><td>ulgʻaymoq</td><td>I <b>grew up</b> in Nukus.</td></tr>
  <tr><td>look after</td><td>qaramoq</td><td>She <b>looks after</b> her grandmother.</td></tr>
  <tr><td>bring up</td><td>tarbiyalamoq</td><td>My aunt <b>brought</b> me <b>up</b>.</td></tr>
  <tr><td>take after</td><td>oʻxshamoq</td><td>He <b>takes after</b> his father.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>gets on</b> well with everybody, and she really
     <b>takes after</b> her mother.</p>
  <p class="pe-ex__uz">Afsona hamma bilan yaxshi chiqishadi va u onasiga juda oʻxshaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eʼtibor bering: <b>take after</b> "keyin olmoq" degani <b>emas</b>, balki
  "<b>oʻxshamoq</b>" degani. <b>bring up</b> ham "olib chiqmoq" emas,
  "<b>tarbiyalamoq</b>". Aynan shu sabab frazali feʼllarni soʻzma-soʻz tarjima qilish
  xatoga olib keladi — ularni <b>bitta yangi soʻz</b> deb qabul qiling.
</div>

<h3>4. Travel and moving around</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Phrasal verb</th><th>Oʻzbekcha</th><th>Example</th></tr>
  <tr><td>set off</td><td>yoʻlga chiqmoq</td><td>We <b>set off</b> early.</td></tr>
  <tr><td>get on / get off</td><td>chiqmoq / tushmoq</td><td><b>Get on</b> the bus here.</td></tr>
  <tr><td>get in / get out of</td><td>(mashinaga) kirmoq / chiqmoq</td><td><b>Get in</b> the car.</td></tr>
  <tr><td>pick up</td><td>olib ketmoq</td><td>I'll <b>pick you up</b> at eight.</td></tr>
  <tr><td>drop off</td><td>tashlab ketmoq</td><td><b>Drop</b> me <b>off</b> here, please.</td></tr>
  <tr><td>check in</td><td>roʻyxatdan oʻtmoq</td><td>We <b>checked in</b> at the hotel.</td></tr>
  <tr><td>take off</td><td>(samolyot) uchmoq</td><td>The plane <b>took off</b> late.</td></tr>
</table>
</div>

<h3>5. Problems and solutions</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Phrasal verb</th><th>Oʻzbekcha</th><th>Example</th></tr>
  <tr><td>break down</td><td>buzilmoq</td><td>The car <b>broke down</b>.</td></tr>
  <tr><td>run out of</td><td>tugab qolmoq</td><td>We've <b>run out of</b> bread.</td></tr>
  <tr><td>give up</td><td>tashlamoq, taslim boʻlmoq</td><td>Don't <b>give up</b>!</td></tr>
  <tr><td>put off</td><td>keyinga qoldirmoq</td><td>They <b>put off</b> the meeting.</td></tr>
  <tr><td>sort out</td><td>hal qilmoq</td><td>I'll <b>sort it out</b>.</td></tr>
  <tr><td>deal with</td><td>shugʻullanmoq</td><td>Who <b>deals with</b> complaints?</td></tr>
  <tr><td>put up with</td><td>chidamoq</td><td>I can't <b>put up with</b> this noise.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Our bus <b>broke down</b>, so we had to <b>put off</b> the trip — but
     Jasur <b>sorted it out</b> and we didn't <b>give up</b>.</p>
  <p class="pe-ex__uz">Avtobusimiz buzilib qoldi, shuning uchun sayohatni keyinga qoldirdik —
     lekin Jasur muammoni hal qildi va biz taslim boʻlmadik.</p>
</div>

<h3>6. On the phone</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Phrasal verb</th><th>Oʻzbekcha</th><th>Example</th></tr>
  <tr><td>call back</td><td>qayta qoʻngʻiroq qilmoq</td><td>I'll <b>call you back</b>.</td></tr>
  <tr><td>hang up</td><td>goʻshakni qoʻymoq</td><td>Don't <b>hang up</b>!</td></tr>
  <tr><td>hold on</td><td>kutib turmoq</td><td><b>Hold on</b> a moment.</td></tr>
  <tr><td>speak up</td><td>balandroq gapirmoq</td><td>Can you <b>speak up</b>?</td></tr>
  <tr><td>get through (to)</td><td>ulanmoq</td><td>I couldn't <b>get through</b>.</td></tr>
  <tr><td>cut off</td><td>uzilib qolmoq</td><td>We were <b>cut off</b>.</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Telefon iboralari <b>tayyor holda</b> yodlanadi, chunki ular suhbatda juda tez kerak
  boʻladi: <em>Hold on</em> ("bir daqiqa"), <em>I'll call you back</em> ("keyin qoʻngʻiroq
  qilaman"), <em>Can you speak up?</em> ("balandroq gapira olasizmi?"). Bu uchtasini
  bilsangiz, ingliz tilida telefonda gaplashish ancha oson boʻladi.
</div>

<h3>7. How to learn them</h3>

<ol class="pe-steps">
  <li><b>Five a day, by topic</b> — not forty at once. One topic a week is plenty.</li>
  <li><b>Write your own sentence</b> for each, about your own life. A verb you have used is
      worth ten you have read.</li>
  <li><b>Note the type</b> (PE-77): separable or not? Try it with a pronoun —
      <em>pick it up</em>, <em>look after her</em>.</li>
  <li><b>Watch for them</b> in films and songs. Once you know a phrasal verb, you start hearing
      it everywhere.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Muhim maslahat: frazali feʼllar <b>ogʻzaki nutqda</b> koʻproq ishlatiladi. Rasmiy insho
  yozayotganda esa ularning "jiddiy" muqobili afzal: <em>put off</em> → <em>postpone</em>,
  <em>find out</em> → <em>discover</em>, <em>sort out</em> → <em>resolve</em>. Ikkalasini
  ham bilsangiz, har qanday vaziyatga moslashasiz.
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>We've <span class="pe-blank">?</span> milk — can you buy some?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>run out of</strong> — it means the supply is finished.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What does this mean? <em>He really takes after his grandfather.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He resembles him</strong> — in looks or character. Nothing to do with taking
         or following.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>I'll pick up you at seven.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'll pick you up at seven.</strong> A pronoun goes in the middle of a
         separable phrasal verb (PE-77).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Choose: <em>They ___ last month but ___ yesterday.</em> (fall out / make up)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>They fell out last month but made up yesterday.</strong> Note both are
         irregular in the past: <em>fell</em>, <em>made</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Describe your morning in three phrasal verbs.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I <b>wake up</b> at half past six, <b>get up</b>
         immediately and <b>put on</b> my school uniform.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>To take after</b><span>oʻxshamoq</span></li>
  <li><b>To bring up</b><span>tarbiyalamoq</span></li>
  <li><b>To get on with</b><span>chiqishmoq</span></li>
  <li><b>To fall out</b><span>urishib qolmoq</span></li>
  <li><b>To run out of</b><span>tugab qolmoq</span></li>
  <li><b>To put off</b><span>keyinga qoldirmoq</span></li>
  <li><b>To sort out</b><span>hal qilmoq</span></li>
  <li><b>To hand in</b><span>topshirmoq</span></li>
  <li><b>To hold on</b><span>kutib turmoq</span></li>
  <li><b>To speak up</b><span>balandroq gapirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Learn them <b>by topic</b>, five at a time — not alphabetically.</li>
    <li>Never translate word by word: <b>take after</b> = resemble, <b>bring up</b> = raise.</li>
    <li>Pronouns still go in the middle: <em>pick <b>you</b> up</em>, <em>sort <b>it</b>
        out</em>.</li>
    <li>Three for the phone: <b>hold on, call back, speak up</b>.</li>
    <li>In formal writing, prefer the single-word version: <b>postpone</b>, <b>discover</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-79: Countable and Uncountable Revisited: Expressions of Quantity",
        "category": "english",
        "order": 79,
        "summary": (
            "The container words that let you count the uncountable — a piece of, a loaf of, a "
            "pair of — plus nouns that change meaning when they change side."
        ),
        "content": """
<h2>PE-79: Countable and Uncountable Revisited: Expressions of Quantity</h2>

<p>Back in PE-2 you learned that you cannot say <em>two breads</em>. The solution was to count
the container instead: <em>two <b>loaves of</b> bread</em>. Now let's build the full toolkit,
because English has a surprisingly precise word for almost every kind of portion — and a set of
nouns that quietly change meaning when they cross from uncountable to countable.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The container and measure words, grouped by what they measure</li>
    <li>The <b>a pair of</b> family for always-plural nouns</li>
    <li>Nouns that exist on <b>both</b> sides — with different meanings</li>
    <li>How the verb agrees with these expressions</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Counting the uncountable</span>
  <span class="pe-chip pe-chip--s">a / two</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">container word</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">of</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">noun</span>
</div>

LEGEND_HERE

<h3>1. Food and drink</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Expression</th><th>Used with</th><th>Oʻzbekcha</th></tr>
  <tr><td>a <b>loaf</b> of</td><td>bread</td><td>bir non</td></tr>
  <tr><td>a <b>slice</b> of</td><td>bread, cheese, cake, meat</td><td>bir tilim</td></tr>
  <tr><td>a <b>piece</b> of</td><td>cake, fruit, meat</td><td>bir boʻlak</td></tr>
  <tr><td>a <b>bottle</b> / <b>glass</b> / <b>cup</b> of</td><td>water, milk, tea</td><td>bir shisha / stakan / piyola</td></tr>
  <tr><td>a <b>bowl</b> of</td><td>soup, rice, salad</td><td>bir kosa</td></tr>
  <tr><td>a <b>bar</b> of</td><td>chocolate, soap</td><td>bir plitka / bir dona</td></tr>
  <tr><td>a <b>packet</b> / <b>tin</b> / <b>jar</b> of</td><td>biscuits, fish, jam</td><td>bir paket / banka</td></tr>
  <tr><td>a <b>kilo</b> / <b>spoonful</b> of</td><td>rice, sugar</td><td>bir kilo / bir qoshiq</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Please buy <b>two loaves of</b> bread, <b>a kilo of</b> rice and
     <b>three bottles of</b> water.</p>
  <p class="pe-ex__uz">Iltimos, ikkita non, bir kilo guruch va uchta shisha suv olib kel.</p>
  <p class="pe-ex__why">The container takes the plural, never the substance:
     <em>two <b>loaves</b> of bread</em>, not <s>two breads</s>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida ham xuddi shunday sanoq soʻzlari bor: <b>bir dona</b>, <b>bir tilim</b>,
  <b>bir bosh</b> (sarimsoq), <b>bir bogʻ</b> (koʻkat), <b>bir qoshiq</b>. Yaʼni bu tushuncha
  sizga tanish — faqat ingliz tilidagi mos soʻzni topish kerak. Diqqat: koʻplik
  <b>sanoq soʻziga</b> qoʻshiladi, moddaga emas.
</div>

<h3>2. Other everyday measures</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>a piece of</p>
    <p>The universal one: <em>advice, information, news, furniture, paper, music</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>a sheet of</p>
    <p><em>paper</em> — <em>Give me a sheet of paper.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>a bunch of</p>
    <p><em>flowers, grapes, keys, bananas</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>a drop / grain of</p>
    <p><em>a drop of water, a grain of rice, a grain of sand</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Let me give you <b>a piece of advice</b> — and could you pass me
     <b>a sheet of paper</b>?</p>
  <p class="pe-ex__uz">Sizga bir maslahat beraman — va bir varaq qogʻoz uzatib yubora
     olasizmi?</p>
  <p class="pe-ex__why"><b>A piece of</b> rescues almost any uncountable noun. When you cannot
     remember the exact word, use it.</p>
</div>

<h3>3. The a pair of family</h3>

<p>Some things are always plural in English because they have two parts (PE-8). To count them,
use <b>a pair of</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>a pair of</b> trousers · <b>a pair of</b> jeans · <b>a pair of</b>
     glasses · <b>two pairs of</b> scissors · <b>a pair of</b> shoes</p>
  <p class="pe-ex__uz">bir shim · bir jinsi · bir koʻzoynak · ikki qaychi · bir juft tufli</p>
  <p class="pe-ex__why">The verb agrees with <em>pair</em>: <em>This pair of shoes <b>is</b>
     new</em>, but <em>These shoes <b>are</b> new</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Agar aniq sanoq soʻzini eslay olmasangiz, <b>a piece of</b> ni ishlating — u deyarli
  hamma sanalmaydigan otga mos keladi: <em>a piece of advice / news / information /
  furniture / paper / music / cake</em>. Bu — "qutqaruvchi ibora": xato boʻlmaydi va
  suhbat toʻxtab qolmaydi.
</div>

<h3>4. Nouns that live on both sides</h3>

<p>This is the elegant part. Some nouns are uncountable in one meaning and countable in another —
and the difference is worth knowing precisely.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Noun</th><th>Uncountable</th><th>Countable</th></tr>
  <tr><td>glass</td><td>material — <em>made of glass</em></td><td><em>a glass</em> = a drinking vessel</td></tr>
  <tr><td>paper</td><td>material — <em>a sheet of paper</em></td><td><em>a paper</em> = a newspaper / an essay</td></tr>
  <tr><td>room</td><td>space — <em>Is there room for me?</em></td><td><em>a room</em> = in a house</td></tr>
  <tr><td>time</td><td>the clock — <em>I have no time</em></td><td><em>three times</em> = occasions</td></tr>
  <tr><td>hair</td><td>all of it — <em>her hair is long</em></td><td><em>a hair</em> = one single hair</td></tr>
  <tr><td>work</td><td>labour — <em>I have work to do</em></td><td><em>a work</em> = a work of art</td></tr>
  <tr><td>experience</td><td>skill — <em>He has experience</em></td><td><em>an experience</em> = an event</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Is there <b>room</b> in the car? — I've booked <b>a room</b> at the
     hotel.</p>
  <p class="pe-ex__uz">Mashinada joy bormi? — Mehmonxonada xona band qildim.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>room</b> misolini yodda tuting: artiklsiz — "<b>joy</b>" (<em>Is there room?</em> —
  "joy bormi?"), artikl bilan — "<b>xona</b>" (<em>a room</em>). Xuddi shunday
  <b>time</b>: <em>no time</em> — "vaqt yoʻq", <em>three times</em> — "uch marta". Yaʼni
  artikl maʼnoni oʻzgartiradi, faqat grammatikani emas.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Please buy two breads and three waters.</s></p>
  <p class="pe-good">Please buy <b>two loaves of bread</b> and <b>three bottles of water</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He gave me two advices.</s></p>
  <p class="pe-good">He gave me <b>two pieces of advice</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I need a new trousers.</s></p>
  <p class="pe-good">I need <b>a new pair of trousers</b> / <b>some new trousers</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Can I have a paper to write on?</s> <em>(if you mean material)</em></p>
  <p class="pe-good">Can I have <b>a sheet of paper</b> to write on?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Two slice of cake, please.</s></p>
  <p class="pe-good">Two <b>slices</b> of cake, please.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Add the right expression: <em>___ chocolate · ___ paper · ___ scissors</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a bar of chocolate · a sheet of paper · a pair of scissors.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>She told me three informations about the trip.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She told me three pieces of information about the trip.</strong></p>
      <p><em>A piece of</em> is the rescue phrase for uncountable nouns.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) Is there room? (b) Is there a room?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) Is there space?</strong> <strong>(b) Is there a bedroom available?</strong>
         One article, two different questions.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     is or are: <em>This pair of jeans <span class="pe-blank">?</span> too big.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — the subject is <em>this pair</em>, which is singular. But
         <em>These jeans <b>are</b> too big</em> ✓.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a short shopping list with four quantity expressions.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>two loaves of bread, a kilo of rice, a bottle of oil, a
         bunch of grapes.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>A loaf of</b><span>bir non</span></li>
  <li><b>A slice of</b><span>bir tilim</span></li>
  <li><b>A piece of</b><span>bir boʻlak / bir dona</span></li>
  <li><b>A bar of</b><span>bir plitka</span></li>
  <li><b>A bunch of</b><span>bir bogʻ / bir shoda</span></li>
  <li><b>A sheet of</b><span>bir varaq</span></li>
  <li><b>A pair of</b><span>bir juft</span></li>
  <li><b>A drop of</b><span>bir tomchi</span></li>
  <li><b>A grain of</b><span>bir dona (guruch)</span></li>
  <li><b>Room (space)</b><span>joy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Count the <b>container</b>, not the substance: <em>two loaves of bread</em>.</li>
    <li>The plural goes on the container word: <b>slices</b>, <b>bottles</b>, <b>pieces</b>.</li>
    <li><b>a piece of</b> rescues almost any uncountable noun.</li>
    <li>Always-plural things take <b>a pair of</b> — and the verb follows <em>pair</em>.</li>
    <li>Some nouns change meaning with the article: <b>room</b>, <b>paper</b>, <b>time</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-80: Articles: The Advanced Cases",
        "category": "english",
        "order": 80,
        "summary": (
            "PE-4 gave you the system; here are the cases that still catch people — the USA, "
            "Lake Aral, the piano, twice a week, and the poor."
        ),
        "content": """
<h2>PE-80: Articles: The Advanced Cases</h2>

<p>In PE-4 you learned the engine: <b>a/an</b> for new things, <b>the</b> for known things, and
nothing at all for general statements. That system handles most of English. But a set of specific
cases have to be learned as facts — why <em>the</em> USA but plain <em>Uzbekistan</em>, why
<em>Lake Aral</em> but <em>the</em> Amu Darya. Here they are, organised so you can actually
remember them.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Geography: which names take <b>the</b> and which do not</li>
    <li><b>the</b> + adjective = a whole group of people</li>
    <li>Instruments, decades, the media — and jobs with <b>a/an</b></li>
    <li>Three ways to make a general statement</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The geography rule of thumb</span>
  <span class="pe-chip pe-chip--v">plural or group names</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">the</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">single names</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--opt">no article</span>
</div>

LEGEND_HERE

<h3>1. Geography</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">the — groups and plurals</p>
    <ul>
      <li>rivers, seas, oceans: <b>the</b> Amu Darya, <b>the</b> Black Sea</li>
      <li>mountain <em>ranges</em>: <b>the</b> Tian Shan, <b>the</b> Alps</li>
      <li>deserts: <b>the</b> Kyzylkum</li>
      <li>plural countries: <b>the</b> USA, <b>the</b> Netherlands, <b>the</b> UAE</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">no article — single names</p>
    <ul>
      <li>single mountains: Mount Everest, Chimgan</li>
      <li>lakes: Lake Aral, Lake Baikal</li>
      <li>most countries: Uzbekistan, Korea, France</li>
      <li>cities, continents, streets: Tashkent, Asia, Navoi Street</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">We flew from <b>Uzbekistan</b> to <b>the USA</b>, over <b>the Black
     Sea</b> and <b>the Alps</b>.</p>
  <p class="pe-ex__uz">Oʻzbekistondan AQShga uchdik — Qora dengiz va Alp togʻlari ustidan.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani mantiq bilan eslash mumkin: agar nom <b>koʻplik</b> yoki <b>guruh</b> maʼnosini
  bersa — <b>the</b> qoʻyiladi (<em>the USA</em> = "Qoʻshma Shtatlar" — koʻplik!,
  <em>the Alps</em> = togʻ tizmasi). Agar <b>yagona nom</b> boʻlsa — artikl yoʻq
  (<em>Uzbekistan</em>, <em>Lake Aral</em>, <em>Mount Everest</em>).
</div>

<h3>2. the + adjective = a group of people</h3>

<p>A very useful pattern: put <b>the</b> in front of an adjective and it means "all the people
who are like that". The verb is <b>plural</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>The poor</b> need help. — <b>The young</b> often understand
     technology better. — <b>The unemployed</b> receive support.</p>
  <p class="pe-ex__uz">Kambagʻallarga yordam kerak. — Yoshlar texnologiyani koʻpincha yaxshiroq
     tushunadi. — Ishsizlar yordam oladi.</p>
  <p class="pe-ex__why">No noun and no <b>-s</b> — <s>the poors</s> ✗. And the verb is plural:
     <em>need</em>, not <em>needs</em>.</p>
</div>

<h3>3. The specific cases worth memorising</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Use the with…</th><th>Example</th></tr>
  <tr><td>musical instruments</td><td>She plays <b>the</b> piano.</td></tr>
  <tr><td>superlatives &amp; ordinals</td><td><b>the</b> best, <b>the</b> first time</td></tr>
  <tr><td>the media, the internet</td><td>I read it on <b>the</b> internet.</td></tr>
  <tr><td>decades &amp; centuries</td><td>in <b>the</b> 1990s, in <b>the</b> 21st century</td></tr>
  <tr><td>unique things</td><td><b>the</b> sun, <b>the</b> moon, <b>the</b> sky</td></tr>
  <tr><td>same / only / whole</td><td><b>the</b> same day, <b>the</b> only problem</td></tr>
</table>
</div>

<div class="pe-table-wrap">
<table>
  <tr><th>Use a/an with…</th><th>Example</th></tr>
  <tr><td>jobs</td><td>She's <b>a</b> doctor. (PE-4)</td></tr>
  <tr><td>rates — "per"</td><td>twice <b>a</b> week, 60 km <b>an</b> hour</td></tr>
  <tr><td>What a…! exclamations</td><td><b>What a</b> beautiful day!</td></tr>
  <tr><td>quantity phrases</td><td><b>a</b> lot of, <b>a</b> few, <b>a</b> couple of</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek plays <b>the</b> guitar twice <b>a</b> week, and he wants to be
     <b>a</b> musician. <b>What a</b> talent!</p>
  <p class="pe-ex__uz">Sherbek haftada ikki marta gitara chaladi va musiqachi boʻlishni
     xohlaydi. Qanday isteʼdod!</p>
</div>

<h3>4. Body parts take a possessive, not the</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>She broke the arm.</s> · <s>He put the hand in the pocket.</s></p>
  <p class="pe-good">She broke <b>her</b> arm. · He put <b>his</b> hand in <b>his</b> pocket.</p>
</div>

<p>English marks whose body part it is, where Uzbek uses the possessive suffix
(<em>qoʻl<b>ini</b></em>). One exception: after a preposition in fixed phrases —
<em>hit him on <b>the</b> head</em>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tana aʼzolari haqida gapirganda ingliz tilida <b>egalik olmoshi</b> ishlatiladi:
  <em><b>her</b> arm</em>, <em><b>his</b> hand</em> — <em>the</em> emas. Bu oʻzbekchadagi
  "qoʻl<b>i</b>ni", "boshi<b>ni</b>" qoʻshimchalariga toʻgʻri keladi. Yaʼni kimning
  aʼzosi ekanini <b>doim</b> koʻrsatish kerak.
</div>

<h3>5. Three ways to speak in general</h3>

<p>All three of these are correct English, and they differ only in tone:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Tigers are</b> dangerous. <em>(most natural)</em><br>
     <b>A tiger is</b> dangerous. <em>(any example of the type)</em><br>
     <b>The tiger is</b> a dangerous animal. <em>(scientific / formal)</em></p>
  <p class="pe-ex__uz">Yoʻlbarslar xavfli. — Yoʻlbars xavfli hayvon.</p>
  <p class="pe-ex__why">For everyday speech, choose the first: <b>plural, no article</b>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Umumiy fikr aytishning eng oson va eng tabiiy yoʻli — <b>koʻplik + artiklsiz</b>:
  <em>Dogs are loyal</em>, <em>Books are expensive</em>, <em>Children love stories</em>.
  Oʻzbekchada ham "Itlar sodiq" deb koʻplikda aytamiz. Shuning uchun shubhaga borsangiz,
  shu yoʻlni tanlang — <em>the</em> ni qoʻshib yubormang.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I want to visit the Uzbekistan and the Tashkent.</s></p>
  <p class="pe-good">I want to visit <b>Uzbekistan</b> and <b>Tashkent</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She plays piano very well.</s></p>
  <p class="pe-good">She plays <b>the</b> piano very well.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The poors need our help.</s></p>
  <p class="pe-good"><b>The poor need</b> our help.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I go to the gym three times in a week.</s></p>
  <p class="pe-good">I go to the gym three times <b>a</b> week.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He hurt the leg playing football.</s></p>
  <p class="pe-good">He hurt <b>his</b> leg playing football.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Add articles if needed: <em>___ Amu Darya flows through ___ Uzbekistan into ___ Aral
     Sea.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The Amu Darya flows through Uzbekistan into the Aral Sea.</strong></p>
      <p>Rivers and seas take <em>the</em>; countries usually don't.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>The rich peoples don't understand the poors.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The rich don't understand the poor.</strong></p>
      <p><em>The</em> + adjective needs no noun and no <b>-s</b>, and takes a plural verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Fill in: <em>I have English lessons twice <span class="pe-blank">?</span> week and I play
     <span class="pe-blank">?</span> violin on Sundays.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a week … the violin.</strong> Rates take <em>a</em>; instruments take
         <em>the</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Why <em>the</em> USA but plain <em>Uzbekistan</em>?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because "the United States" is a plural, group name.</strong> Countries whose
         names are plural or contain words like <em>Kingdom, Republic, Emirates</em> take
         <em>the</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Make it general: <em>The dogs are loyal animals.</em> (everyday style)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Dogs are loyal animals.</strong> For general statements, use the plural with
         <b>no article</b>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Mountain range</b><span>togʻ tizmasi</span></li>
  <li><b>Desert</b><span>sahro</span></li>
  <li><b>Ocean</b><span>okean</span></li>
  <li><b>Decade</b><span>oʻn yillik</span></li>
  <li><b>Century</b><span>asr</span></li>
  <li><b>Ordinal number</b><span>tartib son</span></li>
  <li><b>The unemployed</b><span>ishsizlar</span></li>
  <li><b>Rate (per)</b><span>tezlik, chastota</span></li>
  <li><b>Loyal</b><span>sodiq</span></li>
  <li><b>Talent</b><span>isteʼdod</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>the</b> for plural/group names: <b>the USA, the Alps, the Amu Darya</b>.</li>
    <li><b>No article</b> for single names: <b>Uzbekistan, Lake Aral, Mount Everest</b>.</li>
    <li><b>the + adjective</b> = a group of people, with a plural verb: <em>the poor need…</em></li>
    <li><b>the</b> piano · <b>twice a week</b> · <b>What a</b> day!</li>
    <li>Body parts take <b>my / his / her</b>, not <em>the</em>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
