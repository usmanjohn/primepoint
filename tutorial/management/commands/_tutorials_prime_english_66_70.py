# -*- coding: utf-8 -*-
"""Prime English — end of Block E (66) and start of Block F, precision (67–70).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_66_70.py --author=prime
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
        "title": "PE-66: The Causative: have / get something done",
        "category": "english",
        "order": 66,
        "summary": (
            "You didn't do it — somebody did it for you. The structure behind 'I had my hair "
            "cut', which Uzbek expresses with -tirdim."
        ),
        "content": """
<h2>PE-66: The Causative: have / get something done</h2>

<p>Say <em>"I cut my hair yesterday"</em> to an English speaker and they will picture you with
scissors in front of a mirror. What you meant was <em>"I <b>had</b> my hair <b>cut</b>"</em> —
a barber did it for you. This is the <mark>causative</mark>, and Uzbek speakers have a real
advantage here: your language does exactly the same job with the suffix <b>-tirdim</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>have / get + object + V3</b></li>
    <li>Why the word order matters so much</li>
    <li>The second meaning: something bad happening to you</li>
    <li><b>have somebody do</b> and <b>get somebody to do</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Somebody did it for me</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">have / get</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">object</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
</div>

LEGEND_HERE

<h3>1. The meaning: I arranged it, somebody else did it</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Normal active — I did it myself</p>
    <ul>
      <li>I <b>cut</b> my hair. <em>(with my own scissors!)</em></li>
      <li>I <b>repaired</b> the car.</li>
      <li>She <b>painted</b> the house.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Causative — somebody did it for me</p>
    <ul>
      <li>I <b>had</b> my hair <b>cut</b>. <em>(at the barber's)</em></li>
      <li>I <b>had</b> the car <b>repaired</b>.</li>
      <li>She <b>had</b> the house <b>painted</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--aux">had</span>
     <span class="pe-hl pe-hl--o">her photo</span>
     <span class="pe-hl pe-hl--v">taken</span> for her passport.</p>
  <p class="pe-ex__uz">Afsona pasport uchun suratini oldirdi.</p>
  <p class="pe-ex__why">She did not take it herself — a photographer did.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu sizga tanish! Oʻzbek tilida bu maʼno <b>orttirma nisbat</b> qoʻshimchalari bilan
  beriladi: <em>sochimni ol<b>dir</b>dim</em> (oʻzim olmadim, sartarosh oldi),
  <em>mashinani taʼmirla<b>t</b>dim</em>, <em>uyni boʻya<b>t</b>di</em>. Ingliz tilida esa
  qoʻshimcha emas — <b>have + narsa + V3</b> qurilmasi ishlatiladi. Maʼno bir xil, shakl
  boshqacha.
</div>

<h3>2. Word order is everything</h3>

<p>The object must come <b>between</b> <em>have</em> and the V3. Put them in the wrong order and
you accidentally build a Past Perfect (PE-38) instead.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>I had cut my hair.</s> <em>(= Past Perfect: I had already cut it myself)</em></p>
  <p class="pe-good">I <b>had my hair cut</b>. <em>(a barber cut it)</em></p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Soʻz tartibi oʻzbekcha bilan <b>teskari</b> tuyulishi mumkin, shuning uchun uni qolip
  sifatida yodlang: <b>have</b> → <b>nimani</b> → <b>V3</b>. Yaʼni "sochim" soʻzi
  <em>had</em> va <em>cut</em> ning <b>oʻrtasida</b> turadi: <em>I had <u>my hair</u>
  cut</em>. Agar <em>cut</em> ni oldinga qoʻysangiz, gap butunlay boshqa maʼno beradi
  (Past Perfect).
</div>

<h3>3. It works in every tense</h3>

<p><b>Have</b> here is an ordinary verb, so it changes normally — and questions and negatives
need <em>do / does / did</em>.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Tense</th><th>Example</th></tr>
  <tr><td>Present Simple</td><td>I <b>have</b> my car <b>washed</b> every week.</td></tr>
  <tr><td>Present Continuous</td><td>I<b>'m having</b> my room <b>painted</b> at the moment.</td></tr>
  <tr><td>Past Simple</td><td>I <b>had</b> my hair <b>cut</b> yesterday.</td></tr>
  <tr><td>Present Perfect</td><td>I<b>'ve had</b> my phone <b>repaired</b>.</td></tr>
  <tr><td>Future</td><td>I<b>'ll have</b> the photos <b>printed</b> tomorrow.</td></tr>
  <tr><td>Modal</td><td>You <b>should have</b> your eyes <b>tested</b>.</td></tr>
  <tr><td>Question</td><td><b>Did</b> you <b>have</b> your bike <b>fixed</b>?</td></tr>
  <tr><td>Negative</td><td>I <b>didn't have</b> my hair <b>cut</b>.</td></tr>
</table>
</div>

<h3>4. get instead of have</h3>

<p><b>Get</b> means exactly the same thing and is more informal — very common in speech.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I need to <b>get my shoes repaired</b>. — We <b>got the windows
     cleaned</b> last week.</p>
  <p class="pe-ex__uz">Tuflilarimni taʼmirlatishim kerak. — Oʻtgan hafta derazalarni
     tozalatdik.</p>
</div>

<h3>5. The second meaning: something bad happened to you</h3>

<p>Same structure, but now you did not arrange anything — something unpleasant was done to you.
The context makes the meaning clear.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek <b>had his phone stolen</b> on the bus. — They <b>had their
     house broken into</b> last year.</p>
  <p class="pe-ex__uz">Sherbekning telefoni avtobusda oʻgʻirlanib ketdi. — Oʻtgan yili
     uylariga oʻgʻri tushdi.</p>
  <p class="pe-ex__why">Nobody chose this. The structure simply shows that it happened
     <b>to</b> them.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkinchi maʼnoni kontekst hal qiladi: <em>I had my hair cut</em> — oʻzim xohlab qildirdim.
  <em>I had my phone stolen</em> — hech kim buni xohlamaydi, yaʼni <b>boshimga tushdi</b>.
  Oʻzbekchada bu "<b>telefonim oʻgʻirlandi</b>" yoki "<b>oʻgʻirlanib ketdi</b>" deb
  aytiladi. Shakl bir xil — maʼnoni voqeaning oʻzi koʻrsatadi.
</div>

<h3>6. have somebody do / get somebody to do</h3>

<p>If you want to <b>name</b> the person who did it, two more patterns exist. Note that the
verb forms differ.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>had the plumber fix</b> the tap. <em>(have + person + base
     verb)</em><br>
     I <b>got my brother to help</b> me. <em>(get + person + to + verb)</em></p>
  <p class="pe-ex__uz">Suvchiga joʻmrakni tuzattirdim. — Akamni menga yordam berishga
     koʻndirdim.</p>
  <p class="pe-ex__why"><b>have</b> + person takes a <b>bare</b> verb; <b>get</b> + person takes
     <b>to</b>.</p>
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I cut my hair at the barber's.</s></p>
  <p class="pe-good">Yesterday I <b>had my hair cut</b> at the barber's.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I had repaired my car last week.</s> <em>(if you mean a mechanic did it)</em></p>
  <p class="pe-good">I <b>had my car repaired</b> last week.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She had her dress make by a tailor.</s></p>
  <p class="pe-good">She had her dress <b>made</b> by a tailor. <em>(V3)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Have you had cut your hair?</s></p>
  <p class="pe-good"><b>Have you had your hair cut?</b></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I got my brother help me.</s></p>
  <p class="pe-good">I got my brother <b>to help</b> me.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Rewrite: <em>A mechanic serviced my car yesterday.</em> (start with <em>I</em>)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I had my car serviced yesterday.</strong></p>
      <p>Object (<em>my car</em>) between <em>had</em> and the V3.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What is the difference? <em>(a) I painted my room. (b) I had my room painted.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I did the painting myself.</strong>
         <strong>(b) I paid or asked somebody else to do it.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make it a question: <em>You had your eyes tested.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Did you have your eyes tested?</strong></p>
      <p><em>Have</em> is an ordinary verb here, so it needs the helper <b>did</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which meaning? <em>Jasur had his bag stolen at the station.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Something bad happened to him</strong> — he certainly didn't arrange it. The
         context (a theft) makes it clear.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write two things you had done recently.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I <b>had my hair cut</b> last Saturday and I
         <b>got my phone screen repaired</b> on Monday.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Causative</b><span>orttirma nisbat</span></li>
  <li><b>To arrange</b><span>uyushtirmoq, tashkil qilmoq</span></li>
  <li><b>Barber</b><span>sartarosh</span></li>
  <li><b>Mechanic</b><span>avtousta</span></li>
  <li><b>Plumber</b><span>suvchi, santexnik</span></li>
  <li><b>Tailor</b><span>tikuvchi</span></li>
  <li><b>To service (a car)</b><span>texnik xizmat qilmoq</span></li>
  <li><b>To break into</b><span>oʻgʻirlik uchun kirmoq</span></li>
  <li><b>To test (eyes)</b><span>tekshirtirmoq</span></li>
  <li><b>Tap</b><span>joʻmrak</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>have / get + object + V3</b> = somebody else did it for you.</li>
    <li>Word order is critical: <em>had <b>my hair</b> cut</em>, not <s>had cut my hair</s>.</li>
    <li>It matches Uzbek <b>-tirdim / -tdim</b> (oldirdim, taʼmirlatdim).</li>
    <li>Same structure for bad events: <em>He had his phone stolen.</em></li>
    <li><b>have</b> + person + <b>bare verb</b> · <b>get</b> + person + <b>to</b> + verb.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-67: Comparatives and Superlatives",
        "category": "english",
        "order": 67,
        "summary": (
            "Bigger, biggest, more beautiful, the most beautiful — the rules, the spelling, the "
            "irregulars, and the double-comparative mistake."
        ),
        "content": """
<h2>PE-67: Comparatives and Superlatives</h2>

<p>Uzbek compares things with one tidy suffix: <em>katta<b>roq</b></em>, and the best of all is
<em><b>eng</b> katta</em>. English has two systems and makes you choose between them based on
how <b>long</b> the adjective is. Once you know where the border runs, the whole topic takes
fifteen minutes.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>When to use <b>-er / -est</b> and when to use <b>more / most</b></li>
    <li>The spelling changes: <em>big → bigger</em>, <em>easy → easier</em></li>
    <li>The irregulars: <em>good, bad, far</em></li>
    <li>How to make a comparison stronger, and the <em>more better</em> trap</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Short adjectives</span>
  <span class="pe-chip pe-chip--s">tall</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">taller than</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">the tallest</span>
</div>
<div class="pe-formula">
  <span class="pe-formula__label">Long adjectives</span>
  <span class="pe-chip pe-chip--s">beautiful</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">more beautiful than</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">the most beautiful</span>
</div>

LEGEND_HERE

<h3>1. Where the border runs</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Type of adjective</th><th>Comparative</th><th>Superlative</th></tr>
  <tr><td>1 syllable — <em>tall, cheap</em></td><td>tall<b>er</b></td><td>the tall<b>est</b></td></tr>
  <tr><td>1 syllable + e — <em>nice, large</em></td><td>nic<b>er</b></td><td>the nic<b>est</b></td></tr>
  <tr><td>vowel + consonant — <em>big, hot</em></td><td>bi<b>gger</b></td><td>the bi<b>ggest</b></td></tr>
  <tr><td>2 syllables ending -y — <em>easy, happy</em></td><td>eas<b>ier</b></td><td>the eas<b>iest</b></td></tr>
  <tr><td>2+ syllables — <em>modern, careful</em></td><td><b>more</b> modern</td><td>the <b>most</b> modern</td></tr>
  <tr><td>3+ syllables — <em>interesting</em></td><td><b>more</b> interesting</td><td>the <b>most</b> interesting</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Tashkent is <b>bigger than</b> Bukhara, but Bukhara is
     <b>more beautiful</b> — and Samarkand is <b>the most famous</b> city of all.</p>
  <p class="pe-ex__uz">Toshkent Buxorodan kattaroq, lekin Buxoro chiroyliroq — Samarqand esa
     hammasidan mashhur.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada bitta yoʻl bor: <b>-roq</b> (kattaroq, chiroyliroq) va <b>eng</b> (eng katta).
  Ingliz tilida esa <b>uzunlikka qarab</b> tanlanadi: qisqa sifat — <b>-er/-est</b>, uzun
  sifat — <b>more/most</b>. Chegara: <b>bir boʻgʻin</b> yoki <b>-y</b> bilan tugagan ikki
  boʻgʻin — qoʻshimcha oladi; qolganlari <em>more</em> bilan.
</div>

<h3>2. The irregulars — learn these five</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>good</p>
    <p><b>better</b> → the <b>best</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>bad</p>
    <p><b>worse</b> → the <b>worst</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>far</p>
    <p><b>further / farther</b> → the <b>furthest</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>many / much</p>
    <p><b>more</b> → the <b>most</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>little</p>
    <p><b>less</b> → the <b>least</b></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">!</span>Never double up</p>
    <p><s>more better</s>, <s>the most best</s> ✗</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>Never use both systems at once.</b> <s>more taller</s>, <s>more better</s>,
  <s>the most tallest</s> ✗. One adjective takes one marker: either <b>-er/-est</b>
  <b>or</b> <b>more/most</b>.
</div>

<h3>3. than and the</h3>

<ol class="pe-steps">
  <li><b>Comparatives take <em>than</em>:</b> <em>She is taller <b>than</b> me.</em></li>
  <li><b>Superlatives take <em>the</em>:</b> <em>He is <b>the</b> tallest in the class.</em></li>
  <li><b>Superlative + in</b> for places and groups: <em>the best <b>in</b> the school</em>.</li>
  <li><b>Superlative + of</b> for a number of things: <em>the best <b>of</b> the three</em>.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona is <b>the best student in</b> our class, and she is
     <b>more hard-working than</b> anybody I know.</p>
  <p class="pe-ex__uz">Afsona sinfimizdagi eng yaxshi oʻquvchi va u men bilgan hamma odamdan
     tirishqoqroq.</p>
</div>

<h3>4. Making a comparison stronger or weaker</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Stronger</p>
    <ul>
      <li><b>much</b> bigger · <b>far</b> better</li>
      <li><b>a lot</b> cheaper · <b>even</b> colder</li>
      <li><s>very bigger</s> ✗</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Weaker</p>
    <ul>
      <li><b>a bit</b> more expensive</li>
      <li><b>slightly</b> taller</li>
      <li><b>a little</b> older</li>
    </ul>
  </div>
</div>

<p>Notice that <b>very</b> cannot strengthen a comparative — use <b>much</b> or <b>far</b>
instead.</p>

<h3>5. Comparing amounts: more, fewer, less</h3>

<p>You can compare quantities as well as qualities. Here the countable / uncountable split from
PE-2 comes back one more time.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Countable</p>
    <ul>
      <li><b>more</b> books · <b>fewer</b> books</li>
      <li><em>I have fewer mistakes than last time.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Uncountable</p>
    <ul>
      <li><b>more</b> time · <b>less</b> time</li>
      <li><em>I have less time than before.</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">This year we have <b>fewer students</b> but <b>more classrooms</b>, so
     there is <b>less noise</b>.</p>
  <p class="pe-ex__uz">Bu yil oʻquvchilar kamroq, lekin sinfxonalar koʻproq, shuning uchun
     shovqin kamroq.</p>
  <p class="pe-ex__why"><b>More</b> works for both; only the "less" side splits into
     <em>fewer</em> / <em>less</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "<b>kamroq</b>" hamma narsa uchun bir xil: <em>kamroq kitob</em>,
  <em>kamroq vaqt</em>. Ingliz tilida esa ikkiga boʻlinadi: sanaladiganlar uchun
  <b>fewer</b> (fewer books), sanalmaydiganlar uchun <b>less</b> (less time).
  "Koʻproq" esa ikkalasi uchun ham bitta — <b>more</b>.
</div>

<h3>6. Two elegant patterns</h3>

<div class="pe-ex">
  <p class="pe-ex__en">It's getting <b>colder and colder</b>. — <b>The more</b> you practise,
     <b>the better</b> you get.</p>
  <p class="pe-ex__uz">Kundan kunga sovuqlashyapti. — Qancha koʻp mashq qilsangiz, shuncha
     yaxshi boʻlasiz.</p>
  <p class="pe-ex__why">Two comparatives joined by <em>and</em> = a growing change.
     <em>The more…, the better…</em> = two things rising together.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>The more…, the better…</b> qurilmasi oʻzbekchadagi "<b>qancha ... shuncha ...</b>"
  ga toʻgʻri keladi: <em>Qancha koʻp oʻqisangiz, shuncha koʻp bilasiz</em> →
  <em><b>The more</b> you read, <b>the more</b> you know</em>. Ikkala qismda ham
  <b>the</b> qoʻyilishini eslab qoling — bu yerda u artikl emas.
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>My brother is more taller than me.</s></p>
  <p class="pe-good">My brother is <b>taller</b> than me.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This film is more better.</s></p>
  <p class="pe-good">This film is <b>better</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She is the most intelligent girl of the class.</s></p>
  <p class="pe-good">… the most intelligent girl <b>in</b> the class.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Bukhara is more old that Tashkent.</s></p>
  <p class="pe-good">Bukhara is <b>older than</b> Tashkent.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This bag is very cheaper.</s></p>
  <p class="pe-good">This bag is <b>much</b> cheaper.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Give both forms: <em>hot · easy · expensive · good</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>hotter / the hottest</strong> (double the t), <strong>easier / the
         easiest</strong> (y → i), <strong>more expensive / the most expensive</strong>,
         <strong>better / the best</strong> (irregular).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>Winter in Tashkent is more colder than in Termez.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Winter in Tashkent is colder than in Termez.</strong></p>
      <p><em>Cold</em> is one syllable, so it takes <b>-er</b> alone — never with
         <em>more</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     in or of: <em>He is the tallest boy ___ the team, and the tallest ___ all my
     cousins.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>in the team … of all my cousins.</strong> Groups and places take <em>in</em>;
         a set of individuals takes <em>of</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Complete the pattern: <em>___ you sleep, ___ you feel.</em> (more / better)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The more you sleep, the better you feel.</strong></p>
      <p><em>The</em> is needed in both halves.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Compare two cities you know, using one comparative and one superlative.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Samarkand is <b>older than</b> Tashkent, but Tashkent is
         <b>the biggest</b> city in Uzbekistan.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Comparative</b><span>orttirma daraja (qiyosiy)</span></li>
  <li><b>Superlative</b><span>eng yuqori daraja</span></li>
  <li><b>Syllable</b><span>boʻgʻin</span></li>
  <li><b>Irregular</b><span>qoidasiz</span></li>
  <li><b>Than</b><span>...dan (qiyoslashda)</span></li>
  <li><b>Slightly</b><span>bir oz</span></li>
  <li><b>Even (colder)</b><span>hatto, yanada</span></li>
  <li><b>Hard-working</b><span>tirishqoq</span></li>
  <li><b>Expensive</b><span>qimmat</span></li>
  <li><b>Cheap</b><span>arzon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Short adjectives: <b>-er / the -est</b>. Long adjectives: <b>more / the most</b>.</li>
    <li>Spelling: double the consonant (<em>bigger</em>), y → i (<em>easier</em>).</li>
    <li>Irregulars: <b>good–better–best, bad–worse–worst, far–further–furthest</b>.</li>
    <li><b>Never both</b>: <s>more better</s>, <s>the most tallest</s>.</li>
    <li>Strengthen with <b>much / far / even</b> — not <em>very</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-68: as ... as, too, enough",
        "category": "english",
        "order": 68,
        "summary": (
            "Saying things are equal, excessive or sufficient — and the word-order rule that "
            "makes 'enough' go before nouns but after adjectives."
        ),
        "content": """
<h2>PE-68: as ... as, too, enough</h2>

<p>PE-67 compared things that were different. Now three structures for the rest of life: things
that are <b>the same</b> (<em>as tall as</em>), things that are <b>more than you want</b>
(<em>too hot</em>), and things that are <b>just right</b> (<em>hot enough</em>). All three are
short, all three are extremely common — and each hides one small trap.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>as … as</b> for equality, and <b>not as … as</b> for less</li>
    <li><b>too</b> — more than is wanted</li>
    <li><b>enough</b> — and why its position changes</li>
    <li>The patterns <b>too … to</b> and <b>enough … to</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three structures</span>
  <span class="pe-chip pe-chip--s">as tall as</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">too tall</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">tall enough</span>
</div>

LEGEND_HERE

<h3>1. as … as — they are equal</h3>

<div class="pe-ex">
  <p class="pe-ex__en">Jasur is <b>as tall as</b> his brother. — This book is <b>as
     interesting as</b> the film.</p>
  <p class="pe-ex__uz">Jasur akasidek baland boʻyli. — Bu kitob kino kabi qiziqarli.</p>
  <p class="pe-ex__why">The adjective in the middle never changes — no <b>-er</b>, no
     <em>more</em>.</p>
</div>

<p>To say <b>less</b>, make it negative: <b>not as … as</b> (or <em>not so … as</em>).</p>

<div class="pe-ex">
  <p class="pe-ex__en">Today isn't <b>as cold as</b> yesterday. = Today is <b>warmer than</b>
     yesterday.</p>
  <p class="pe-ex__uz">Bugun kechagidek sovuq emas. = Bugun kechadan iliqroq.</p>
</div>

<p>Useful extras: <b>twice as … as</b>, <b>half as … as</b>, <b>just as … as</b>, and the fixed
phrase <b>as soon as possible</b>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>as … as</b> oʻzbekchadagi "<b>-dek / -day / kabi</b>" ga toʻgʻri keladi:
  <em>akasi<b>dek</b> baland</em> → <em><b>as</b> tall <b>as</b> his brother</em>. Diqqat:
  ingliz tilida <b>ikkita as</b> boʻlishi shart — biri sifatdan oldin, biri keyin.
  Bittasini tushirib qoldirish eng koʻp uchraydigan xato.
</div>

<h3>2. too — more than you want</h3>

<p><b>Too</b> is always negative in feeling. It means "so much that there is a problem".</p>

<div class="pe-ex">
  <p class="pe-ex__en">This tea is <b>too hot</b> — I can't drink it. — The film was <b>too
     long</b>.</p>
  <p class="pe-ex__uz">Bu choy juda issiq — icholmayman. — Kino juda uzun edi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">too + adjective</p>
    <ul>
      <li><b>too</b> expensive · <b>too</b> difficult</li>
      <li><s>too much expensive</s> ✗</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">too much / too many + noun</p>
    <ul>
      <li><b>too much</b> sugar <em>(uncountable)</em></li>
      <li><b>too many</b> people <em>(countable)</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>too</b> is not the same as <b>very</b>. <em>Very hot</em> is a description — perhaps you
  like it. <em>Too hot</em> means there is a problem. <em>"The soup is very hot"</em> ✓ delicious;
  <em>"The soup is too hot"</em> ✗ can't eat it.
</div>

<h3>3. enough — just the right amount</h3>

<p>Here is the position rule that catches everybody: <b>enough</b> goes <b>after</b> an
adjective but <b>before</b> a noun.</p>

<div class="pe-ex">
  <p class="pe-ex__en">He isn't <b>old enough</b> to drive. <em>(after the adjective)</em><br>
     I don't have <b>enough money</b>. <em>(before the noun)</em></p>
  <p class="pe-ex__uz">U haydash uchun yoshi yetmagan. — Menda yetarli pul yoʻq.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>She isn't enough tall to reach the shelf.</s></p>
  <p class="pe-good">She isn't <b>tall enough</b> to reach the shelf.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "yetarli" doim <b>oldin</b> keladi: "<b>yetarli</b> pul", "<b>yetarli</b>
  baland". Ingliz tilida esa oʻrni <b>oʻzgaradi</b>: ot bilan — oldin (<em><b>enough</b>
  money</em>), sifat bilan — keyin (<em>tall <b>enough</b></em>). Shu bitta farqni yodda
  tutsangiz, <s>enough tall</s> xatosidan qutulasiz.
</div>

<h3>4. The …to patterns</h3>

<p>Both <em>too</em> and <em>enough</em> commonly continue with <b>to + verb</b>, explaining the
consequence.</p>

<div class="pe-ex">
  <p class="pe-ex__en">It's <b>too dark to read</b>. — Is the water <b>warm enough to
     swim</b> in? — I don't have <b>enough time to finish</b>.</p>
  <p class="pe-ex__uz">Oʻqish uchun juda qorongʻi. — Suv suzish uchun yetarlicha iliqmi? —
     Tugatish uchun yetarli vaqtim yoʻq.</p>
</div>

<p>You can name the person with <b>for</b>: <em>The box is <b>too heavy for me to</b>
lift.</em></p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yana bir qurilmani ham bilib qoʻying: <b>so … that</b> — "<b>shunchalik ... ki</b>".
  <em>The tea was <b>so hot that</b> I couldn't drink it</em> = "Choy shunchalik issiq
  ediki, icholmadim". Farqi: <b>too … to</b> dan keyin <b>feʼl</b> keladi
  (<em>too hot to drink</em>), <b>so … that</b> dan keyin esa <b>butun gap</b> keladi.
  <s>too hot that I couldn't drink</s> — bu ikkisini aralashtirish.
</div>

<h3>5. Two ways to say the same thing</h3>

<p>These three structures often describe the same situation from different angles — a very
useful skill for writing:</p>

<div class="pe-ex">
  <p class="pe-ex__en">He's <b>too young to</b> vote. = He <b>isn't old enough to</b> vote. =
     He <b>isn't as old as</b> the other voters.</p>
  <p class="pe-ex__uz">U ovoz berish uchun juda yosh. = Uning yoshi yetmagan.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>This exercise is too much difficult.</s></p>
  <p class="pe-good">This exercise is <b>too difficult</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She isn't enough strong to carry it.</s></p>
  <p class="pe-good">She isn't <b>strong enough</b> to carry it.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He is as taller as his father.</s></p>
  <p class="pe-good">He is <b>as tall as</b> his father.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The tea is too hot that I can't drink it.</s></p>
  <p class="pe-good">The tea is <b>too hot to</b> drink. / The tea is <b>so hot that</b>
     I can't drink it.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>There were too much people at the bazaar.</s></p>
  <p class="pe-good">There were <b>too many</b> people at the bazaar.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>Afsona runs <span class="pe-blank">?</span> fast
     <span class="pe-blank">?</span> her brother.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>as fast as.</strong> Both <em>as</em> words are needed, and the adverb in the
         middle stays in its plain form.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     too or enough: <em>This coat is ___ small for me. It isn't big ___ .</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>too small … big enough.</strong> Two ways to describe the same coat —
         note where each word sits.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Rewrite with <em>too</em>: <em>He isn't strong enough to lift the box.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He is too weak to lift the box.</strong></p>
      <p>Notice you must use the <b>opposite</b> adjective when you switch structures.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What is the difference? <em>(a) The room is very cold. (b) The room is too cold.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) A description</strong> — maybe that's fine.
         <strong>(b) A problem</strong> — we can't stay here.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>I don't have money enough for a taxi.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I don't have enough money for a taxi.</strong></p>
      <p><em>Enough</em> comes <b>before</b> a noun.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Equal</b><span>teng</span></li>
  <li><b>Enough</b><span>yetarli</span></li>
  <li><b>Too (much)</b><span>haddan ortiq</span></li>
  <li><b>Sufficient</b><span>kifoya qiladigan</span></li>
  <li><b>To reach</b><span>yetib bormoq, uzatmoq</span></li>
  <li><b>To lift</b><span>koʻtarmoq</span></li>
  <li><b>To vote</b><span>ovoz bermoq</span></li>
  <li><b>Twice as</b><span>ikki barobar</span></li>
  <li><b>As soon as possible</b><span>imkon qadar tezroq</span></li>
  <li><b>Shelf</b><span>tokcha</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>as + adjective + as</b> = equal. Negative: <b>not as … as</b>.</li>
    <li><b>too</b> = a problem · <b>very</b> = just a description.</li>
    <li><b>too much / too many</b> before nouns; plain <b>too</b> before adjectives.</li>
    <li><b>enough</b> goes <b>after</b> adjectives, <b>before</b> nouns.</li>
    <li>Both continue with <b>to + verb</b>: <em>too dark to read</em>, <em>old enough to
        drive</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-69: Quantifiers: some, any, much, many, a lot of",
        "category": "english",
        "order": 69,
        "summary": (
            "How much and how many — the words for amounts, which sentence types they belong to, "
            "and why 'Would you like some tea?' breaks the rule."
        ),
        "content": """
<h2>PE-69: Quantifiers: some, any, much, many, a lot of</h2>

<p>You met the countable / uncountable split back in PE-2. Now let's finish the job properly.
These small words — <b>some, any, much, many, a lot of</b> — appear in almost every sentence you
will ever say about amounts, and each one belongs to particular <mark>sentence types</mark>. Get
that map right and a whole class of mistakes disappears.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>some</b> and <b>any</b> — and the offer that breaks the rule</li>
    <li><b>much / many</b> — where they really belong</li>
    <li><b>a lot of, lots of, plenty of</b> — the safe options</li>
    <li><b>no</b> vs <b>not any</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The basic map</span>
  <span class="pe-chip pe-chip--v">some</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">positive</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">any</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">negative + question</span>
</div>

LEGEND_HERE

<h3>1. some and any</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">some — positive sentences</p>
    <ul>
      <li>There's <b>some</b> milk in the fridge.</li>
      <li>I bought <b>some</b> apples.</li>
      <li>I need <b>some</b> help.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">any — negatives and questions</p>
    <ul>
      <li>There isn't <b>any</b> milk.</li>
      <li>Did you buy <b>any</b> apples?</li>
      <li>I don't need <b>any</b> help.</li>
    </ul>
  </div>
</div>

<p>Both work with plural countable nouns and with uncountable nouns — that is why they are so
useful.</p>

<div class="pe-ex">
  <p class="pe-ex__en">We have <b>some</b> bread and <b>some</b> eggs, but we haven't got
     <b>any</b> sugar or <b>any</b> tomatoes.</p>
  <p class="pe-ex__uz">Bizda non va tuxum bor, lekin shakar ham, pomidor ham yoʻq.</p>
</div>

<h3>2. The exception: offers and requests</h3>

<p>In questions that <b>offer</b> or <b>ask for</b> something, English uses <b>some</b> — because
you already expect the answer to be yes.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Would you like <b>some</b> tea? — Could I have <b>some</b> water,
     please?</p>
  <p class="pe-ex__uz">Choy ichasizmi? — Bir oz suv olsam boʻladimi?</p>
  <p class="pe-ex__why">Compare a real question: <em>Is there <b>any</b> tea left?</em> — you
     genuinely don't know.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani shunday eslang: <b>taklif</b> yoki <b>iltimos</b> boʻlsa — <b>some</b>
  ("choy ichasizmi?", "bir oz suv bering"). <b>Haqiqiy savol</b> boʻlsa, yaʼni javobni
  bilmasangiz — <b>any</b> ("choy bormi?"). Oʻzbekchada ikkalasi ham "-mi" bilan
  tugaydi, shuning uchun bu farqni alohida eslab qolish kerak.
</div>

<h3>3. any = it doesn't matter which</h3>

<p><b>Any</b> has a second life in <b>positive</b> sentences, where it means "whichever one you
like".</p>

<div class="pe-ex">
  <p class="pe-ex__en">Take <b>any</b> seat you like. — <b>Any</b> student can join the club.
     — Come <b>any</b> time.</p>
  <p class="pe-ex__uz">Xohlagan joyingizga oʻtiring. — Har qanday oʻquvchi toʻgaramizga
     qoʻshilishi mumkin. — Xohlagan paytda keling.</p>
</div>

<h3>4. much and many — where they belong</h3>

<p>Both mean "a large amount", but they are mainly at home in <b>negatives</b> and
<b>questions</b>. In positive sentences they sound heavy and formal.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Sentence type</th><th>Countable</th><th>Uncountable</th></tr>
  <tr><td>Question</td><td>How <b>many</b> books?</td><td>How <b>much</b> water?</td></tr>
  <tr><td>Negative</td><td>not <b>many</b> people</td><td>not <b>much</b> time</td></tr>
  <tr><td>Positive (natural)</td><td><b>a lot of</b> books</td><td><b>a lot of</b> water</td></tr>
  <tr><td>Positive (formal)</td><td><b>many</b> books</td><td><b>much</b> water ✗ rare</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I don't have <b>much</b> time, and there weren't <b>many</b> students in
     the library. But I've got <b>a lot of</b> homework.</p>
  <p class="pe-ex__uz">Vaqtim koʻp emas va kutubxonada koʻp oʻquvchi yoʻq edi. Lekin uy
     vazifam koʻp.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <em>"I have much money"</em> sounds strange to a native ear. In positive sentences use
  <b>a lot of</b>. Keep <em>much</em> for negatives, questions, and after <em>too, so, very</em>
  — <em>too much sugar</em>, <em>so much noise</em>.
</div>

<h3>5. a lot of, lots of, plenty of</h3>

<p>These are the friendly ones: they work with <b>both</b> countable and uncountable nouns, in
<b>all</b> sentence types. When you are unsure, they are always safe.</p>

<div class="pe-ex">
  <p class="pe-ex__en">There are <b>a lot of</b> people here. — We have <b>plenty of</b> time.
     — She's got <b>lots of</b> friends.</p>
  <p class="pe-ex__uz">Bu yerda koʻp odam bor. — Vaqtimiz yetarlicha. — Uning doʻstlari koʻp.</p>
  <p class="pe-ex__why"><em>Lots of</em> is the most informal; <em>plenty of</em> adds "more
     than enough".</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>a lot of</b> va <b>a lot</b> ni farqlang: <b>a lot <u>of</u></b> — otdan oldin
  (<em>a lot <b>of</b> books</em> — "koʻp kitob"), <b>a lot</b> — feʼldan keyin, ravish
  sifatida (<em>I like it <b>a lot</b></em> — "juda yoqadi", <em>She studies <b>a
  lot</b></em> — "koʻp oʻqiydi"). Ot boʻlmasa, <em>of</em> ham qoʻyilmaydi.
</div>

<h3>6. no and not any</h3>

<p>Two ways to say zero. <b>No</b> + noun is a little stronger and more direct.</p>

<div class="pe-ex">
  <p class="pe-ex__en">There's <b>no</b> milk. = There isn't <b>any</b> milk. — I have
     <b>no</b> idea.</p>
  <p class="pe-ex__uz">Sut yoʻq. — Hech qanday tasavvurim yoʻq.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat: <b>no</b> va <b>not</b> ni birga ishlatib boʻlmaydi — bu ikkita inkor boʻladi
  (PE-11 ni eslang). <em>There is <b>no</b> milk</em> ✓ yoki <em>There <b>isn't any</b>
  milk</em> ✓, lekin <s>There isn't no milk</s> ✗. Oʻzbekchada "sut yoʻq" bitta inkor —
  ingliz tilida ham bitta boʻlishi kerak.
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have much friends in Tashkent.</s></p>
  <p class="pe-good">I have <b>a lot of</b> friends in Tashkent.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How much books did you read?</s></p>
  <p class="pe-good">How <b>many</b> books did you read?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>There isn't some bread left.</s></p>
  <p class="pe-good">There isn't <b>any</b> bread left.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Would you like any tea?</s></p>
  <p class="pe-good">Would you like <b>some</b> tea? <em>(an offer)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I don't have no money.</s></p>
  <p class="pe-good">I don't have <b>any</b> money. / I have <b>no</b> money.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     some or any: <em>I bought <span class="pe-blank">?</span> fruit, but I didn't buy
     <span class="pe-blank">?</span> vegetables.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>some … any.</strong> Positive → <em>some</em>; negative → <em>any</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     much or many: <em>How <span class="pe-blank">?</span> sugar do you take, and how
     <span class="pe-blank">?</span> cups do you drink?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>much … many.</strong> <em>Sugar</em> is uncountable, <em>cups</em> are
         countable.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Why <em>some</em> here? <em>Would you like some help with that?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because it is an offer, not a real question.</strong> You already expect the
         answer to be yes.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Improve it: <em>She has much homework tonight.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She has a lot of homework tonight.</strong></p>
      <p><em>Much</em> in a positive sentence sounds unnatural.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What does <em>any</em> mean here? <em>You can call me any time.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It doesn't matter which time — whenever you like.</strong> This is the
         positive use of <em>any</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Quantifier</b><span>miqdor soʻzi</span></li>
  <li><b>Amount</b><span>miqdor</span></li>
  <li><b>Countable</b><span>sanaladigan</span></li>
  <li><b>Uncountable</b><span>sanalmaydigan</span></li>
  <li><b>Plenty of</b><span>yetarlicha, mo'l</span></li>
  <li><b>Offer</b><span>taklif</span></li>
  <li><b>Left (remaining)</b><span>qolgan</span></li>
  <li><b>Seat</b><span>joy, oʻrindiq</span></li>
  <li><b>To join</b><span>qoʻshilmoq</span></li>
  <li><b>I have no idea</b><span>tasavvurim yoʻq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>some</b> → positive · <b>any</b> → negatives and questions.</li>
    <li>But <b>offers and requests take some</b>: <em>Would you like some tea?</em></li>
    <li><b>any</b> in a positive sentence = "it doesn't matter which".</li>
    <li><b>much / many</b> live in negatives and questions; use <b>a lot of</b> in positives.</li>
    <li><b>no</b> + noun = <b>not any</b> — never both together.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-70: few vs a few, little vs a little",
        "category": "english",
        "order": 70,
        "summary": (
            "One tiny article changes your whole attitude: 'a few friends' is cheerful, 'few "
            "friends' is sad. Learn the difference and the countable split."
        ),
        "content": """
<h2>PE-70: few vs a few, little vs a little</h2>

<p>Look at these two sentences:</p>

<p><em>"I have <b>a few</b> friends here."</em> — cheerful; I'm fine.<br>
<em>"I have <b>few</b> friends here."</em> — lonely; I wish I had more.</p>

<p>One three-letter word, and the whole mood of the sentence flips. This is a small piece of
grammar that carries a large amount of <mark>feeling</mark> — and exams love it.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>a few / a little</b> — positive: "some, and that's enough"</li>
    <li><b>few / little</b> — negative: "almost none, unfortunately"</li>
    <li>Which pair goes with countable and which with uncountable nouns</li>
    <li>The surprise of <b>quite a few</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two questions</span>
  <span class="pe-chip pe-chip--s">countable or uncountable?</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">positive or negative feeling?</span>
</div>

LEGEND_HERE

<h3>1. The four words in one grid</h3>

<div class="pe-table-wrap">
<table>
  <tr><th></th><th>Countable (books, friends)</th><th>Uncountable (time, water)</th></tr>
  <tr>
    <td><b>Positive</b><br>"some — enough"</td>
    <td><b>a few</b><br><em>I have a few friends.</em></td>
    <td><b>a little</b><br><em>I have a little time.</em></td>
  </tr>
  <tr>
    <td><b>Negative</b><br>"almost none"</td>
    <td><b>few</b><br><em>I have few friends.</em></td>
    <td><b>little</b><br><em>I have little time.</em></td>
  </tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">There's <b>a little</b> milk left — enough for tea. — There's
     <b>little</b> milk left — we need to buy some.</p>
  <p class="pe-ex__uz">Bir oz sut qolgan — choyga yetadi. — Sut juda kam qolgan — sotib olish
     kerak.</p>
  <p class="pe-ex__why">The same amount, two different attitudes.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni oʻzbekcha aniq koʻrsatadi: <b>a few / a little</b> = "<b>bir oz</b>" (bor,
  yetadi, xotirjam ohang). <b>few / little</b> = "<b>juda kam</b>" (deyarli yoʻq, afsus
  ohangi). Shuning uchun tarjima qilganda "bir oz" desangiz — <b>artikl bilan</b>,
  "juda kam" desangiz — <b>artiklsiz</b>.
</div>

<h3>2. The countable / uncountable half</h3>

<p>This half is mechanical — it is the same split you learned in PE-2. <b>Few</b> counts;
<b>little</b> measures.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">few / a few + plural countable</p>
    <ul>
      <li>a few books · a few people</li>
      <li>a few days · a few questions</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">little / a little + uncountable</p>
    <ul>
      <li>a little water · a little money</li>
      <li>a little time · a little help</li>
    </ul>
  </div>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>I have a little friends.</s></p>
  <p class="pe-good">I have <b>a few</b> friends.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We have a few time before the lesson.</s></p>
  <p class="pe-good">We have <b>a little</b> time before the lesson.</p>
</div>

<h3>3. Making the negative stronger</h3>

<p>Because the bare forms already sound negative, English strengthens them with <b>very</b>.
This is extremely common — in fact <em>very few</em> and <em>very little</em> are heard far more
often than <em>few</em> and <em>little</em> alone.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Very few</b> students passed the test. — She has <b>very little</b>
     experience.</p>
  <p class="pe-ex__uz">Juda kam oʻquvchi testdan oʻtdi. — Uning tajribasi juda kam.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In everyday speech, the bare <em>few</em> and <em>little</em> can sound quite formal. Natives
  often say <b>not many</b> and <b>not much</b> instead: <em>"Not many students passed"</em>,
  <em>"I haven't got much time"</em>. Learn all three ways and you always have an option.
</div>

<h3>4. The surprise: quite a few</h3>

<p>Logic would suggest that <em>quite a few</em> means "not many". It means the
<b>opposite</b> — quite a lot.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Quite a few</b> people came to the concert. <em>(= a good number,
     more than expected)</em></p>
  <p class="pe-ex__uz">Konsertga ancha koʻp odam keldi.</p>
  <p class="pe-ex__why">Compare: <em>a few people came</em> (some) · <em>few people came</em>
     (almost nobody).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>quite a few</b> ni soʻzma-soʻz tarjima qilmang! U "kamgina" degani <b>emas</b>,
  balki "<b>ancha koʻp</b>" degani. Shunga oʻxshash: <b>quite a lot</b> — "juda koʻp".
  Bu — tayyor ibora, shuning uchun butunligicha yodlang.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Imtihonda javobni <b>gapning ohangidan</b> toping. Yaqin atrofda
  <em>unfortunately</em>, <em>sadly</em>, <em>only</em> kabi soʻzlar boʻlsa — <b>artiklsiz</b>
  (<em>few / little</em>). <em>Don't worry</em>, <em>luckily</em>, <em>still</em> boʻlsa —
  <b>artikl bilan</b> (<em>a few / a little</em>). Yaʼni grammatika emas, <b>his-tuygʻu</b>
  hal qiladi.
</div>

<h3>5. a few / a little as answers</h3>

<p>Both can stand alone in short answers, which makes them very handy in conversation:</p>

<div class="pe-ex">
  <p class="pe-ex__en">— Do you speak Korean? — <b>A little.</b><br>
     — How many friends do you have there? — <b>A few.</b></p>
  <p class="pe-ex__uz">— Koreys tilida gapirasizmi? — Bir oz. — U yerda nechta doʻstingiz bor?
     — Bir nechta.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have little friends in this city.</s> <em>(if you mean "some")</em></p>
  <p class="pe-good">I have <b>a few</b> friends in this city.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Can I have a few water, please?</s></p>
  <p class="pe-good">Can I have <b>a little</b> water, please?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Quite a few people came, so the hall was almost empty.</s></p>
  <p class="pe-good"><b>Few</b> people came, so the hall was almost empty.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He has a little money, so he can't buy it.</s></p>
  <p class="pe-good">He has <b>little</b> money, so he can't buy it.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>There were a few informations in the article.</s></p>
  <p class="pe-good">There was <b>a little</b> information in the article.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>Don't worry, we still have <span class="pe-blank">?</span> time before the
     bus leaves.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a little</strong> — <em>time</em> is uncountable, and <em>Don't worry</em>
         shows the feeling is positive.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>Unfortunately, <span class="pe-blank">?</span> students came to the extra
     lesson.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>few</strong> (or <em>very few</em>) — <em>Unfortunately</em> tells you the
         feeling is negative, and <em>students</em> are countable.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) I have a little money. (b) I have little money.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) Some — enough for what I need.</strong>
         <strong>(b) Almost none — I'm short of money.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     True or false: <em>"Quite a few people liked it"</em> means very few people liked it.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>False.</strong> <em>Quite a few</em> means <b>quite a lot</b> — a surprising
         number liked it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Fill both gaps: <em>I've made <span class="pe-blank">?</span> mistakes, but I need
     <span class="pe-blank">?</span> more practice.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a few … a little.</strong> <em>Mistakes</em> are countable;
         <em>practice</em> is uncountable.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>A few</b><span>bir nechta</span></li>
  <li><b>Few</b><span>juda kam</span></li>
  <li><b>A little</b><span>bir oz</span></li>
  <li><b>Little</b><span>juda kam</span></li>
  <li><b>Quite a few</b><span>ancha koʻp</span></li>
  <li><b>Unfortunately</b><span>afsuski</span></li>
  <li><b>Attitude</b><span>munosabat</span></li>
  <li><b>Experience</b><span>tajriba</span></li>
  <li><b>Empty</b><span>boʻsh</span></li>
  <li><b>To be short of</b><span>yetishmaslik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>a few / a little</b> = some, and it's enough — positive feeling.</li>
    <li><b>few / little</b> = almost none — negative feeling.</li>
    <li><b>few</b> counts (friends) · <b>little</b> measures (time, water).</li>
    <li>Strengthen with <b>very few / very little</b>; in speech, <b>not many / not much</b>.</li>
    <li><b>quite a few</b> means <b>quite a lot</b> — not few at all.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
