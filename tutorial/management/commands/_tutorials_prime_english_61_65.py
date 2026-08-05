# -*- coding: utf-8 -*-
"""Prime English — Block E, lessons 61–65 (passive, reported speech, verb patterns).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_61_65.py --author=prime
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
        "title": "PE-61: Passive Voice in All Tenses, and the by-agent",
        "category": "english",
        "order": 61,
        "summary": (
            "One pattern, twelve tenses: change be, keep V3. Plus passives with modals, two "
            "objects, and when to keep the by-phrase."
        ),
        "stories": ['How a Book Is Made'],
        "content": """
<h2>PE-61: Passive Voice in All Tenses, and the by-agent</h2>

<p>In PE-60 you built the passive in two tenses. Here is the good news: <mark>you already know
all the rest</mark>. The passive is <b>be + V3</b>, and only the word <b>be</b> ever changes.
Put <em>be</em> into any tense you like — using the map from PE-41 — and the passive follows
automatically. This lesson turns that one idea into a complete tool.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The passive in every tense — by changing only <b>be</b></li>
    <li>Passives with modals: <em>can be done, must be done, should have been done</em></li>
    <li>What happens when a verb has <b>two</b> objects</li>
    <li>When to keep <b>by</b>, and when <b>with</b> is the right word</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The whole system</span>
  <span class="pe-chip pe-chip--aux">be (in any tense)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
  <span class="pe-chip pe-chip--opt">V3 never changes</span>
</div>

LEGEND_HERE

<h3>1. The complete table</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Tense</th><th>Active</th><th>Passive</th></tr>
  <tr><td>Present Simple</td><td>They clean it.</td><td>It <b>is cleaned</b>.</td></tr>
  <tr><td>Present Continuous</td><td>They are cleaning it.</td><td>It <b>is being cleaned</b>.</td></tr>
  <tr><td>Past Simple</td><td>They cleaned it.</td><td>It <b>was cleaned</b>.</td></tr>
  <tr><td>Past Continuous</td><td>They were cleaning it.</td><td>It <b>was being cleaned</b>.</td></tr>
  <tr><td>Present Perfect</td><td>They have cleaned it.</td><td>It <b>has been cleaned</b>.</td></tr>
  <tr><td>Past Perfect</td><td>They had cleaned it.</td><td>It <b>had been cleaned</b>.</td></tr>
  <tr><td>Future (will)</td><td>They will clean it.</td><td>It <b>will be cleaned</b>.</td></tr>
  <tr><td>going to</td><td>They are going to clean it.</td><td>It <b>is going to be cleaned</b>.</td></tr>
  <tr><td>Future Perfect</td><td>They will have cleaned it.</td><td>It <b>will have been cleaned</b>.</td></tr>
  <tr><td>Modals</td><td>They must clean it.</td><td>It <b>must be cleaned</b>.</td></tr>
</table>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Read the passive column downwards. Every single line ends in <b>cleaned</b> — the V3 never
  moves. All the work is done by <em>is, was, being, been, will be</em>. Learn <b>be</b> well
  and the passive costs you nothing.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The bridge <b>is being repaired</b> at the moment, and the road
     <b>has been closed</b> since Monday.</p>
  <p class="pe-ex__uz">Koʻprik hozir taʼmirlanyapti va yoʻl dushanbadan beri yopilgan.</p>
  <p class="pe-ex__why">Present Continuous passive, then Present Perfect passive — in one
     sentence.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sxemani yodda tuting: <b>zamonni be koʻrsatadi, maʼnoni V3 beradi</b>. Shuning uchun
  yangi zamonda majhul nisbat yasashda faqat bitta savol bering: <em>be</em> feʼli bu
  zamonda qanday boʻladi? <em>is → is being → has been → will be</em>. V3 esa hech qachon
  oʻzgarmaydi. Bu — 10 ta shaklni bitta qoida bilan yopadi.
</div>

<h3>2. Two tenses that avoid the passive</h3>

<p>Grammatically possible, but nobody says them: the <b>Present Perfect Continuous</b> and the
<b>Future Continuous</b> passives are too heavy (<em>has been being cleaned</em>). English
simply uses the active instead.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>The room has been being cleaned all morning.</s></p>
  <p class="pe-good">They <b>have been cleaning</b> the room all morning.</p>
</div>

<h3>3. Passives with modals</h3>

<p>The formula is <b>modal + be + V3</b>, and for the past, <b>modal + have been + V3</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">This form <b>must be signed</b> today. — The window <b>can't be
     opened</b>. — The letter <b>should have been sent</b> last week.</p>
  <p class="pe-ex__uz">Bu shakl bugun imzolanishi kerak. — Deraza ochilmaydi. — Xat oʻtgan
     hafta yuborilishi kerak edi.</p>
</div>

<h3>4. Verbs with two objects</h3>

<p>Some verbs give something to somebody: <em>give, send, tell, offer, show, teach, pay</em>.
They have two objects, so they make <b>two</b> possible passives — and English usually prefers
the one that starts with the <b>person</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Active: The school gave <u>Afsona</u> <u>a prize</u>.<br>
     ✓ Common: <b>Afsona was given a prize.</b><br>
     ✓ Also correct: <b>A prize was given to Afsona.</b></p>
  <p class="pe-ex__uz">Maktab Afsonaga sovrin berdi. → Afsonaga sovrin berildi.</p>
  <p class="pe-ex__why">Note the <em>to</em> in the second version — it is needed there.</p>
</div>

<h3>5. by or with?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">by — the doer</p>
    <ul>
      <li>The letter was written <b>by</b> my father.</li>
      <li>The window was broken <b>by</b> a ball.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">with — the tool</p>
    <ul>
      <li>The bread was cut <b>with</b> a knife.</li>
      <li>It was written <b>with</b> a pencil.</li>
    </ul>
  </div>
</div>

<p>And remember from PE-60: most passive sentences have <b>no</b> agent at all. Keep <em>by</em>
only when the doer is genuinely interesting.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>by</b> — bajaruvchi ("<b>tomonidan</b>"), <b>with</b> — vosita ("<b>bilan</b>"):
  <em>pichoq <b>bilan</b> kesildi</em> → <em>cut <b>with</b> a knife</em>, <em>otam
  <b>tomonidan</b> yozilgan</em> → <em>written <b>by</b> my father</em>. Oʻzbekchada ikkita
  turli qoʻshimcha borligi kabi, ingliz tilida ham ikkita turli predlog bor.
</div>

<h3>6. It is said that… — the impersonal passive</h3>

<p>Formal English and news reports use this to say "people say" without naming anybody:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>It is said that</b> the bridge is 500 years old. = The bridge
     <b>is said to be</b> 500 years old.</p>
  <p class="pe-ex__uz">Aytishlaricha, koʻprik 500 yillik. — Koʻprik 500 yillik deb
     hisoblanadi.</p>
  <p class="pe-ex__why">Common verbs here: <em>say, believe, think, know, expect,
     report</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>It is said that…</b> oʻzbekchadagi "<b>aytishlaricha</b>", "<b>deb hisoblanadi</b>"
  iboralariga toʻgʻri keladi. Bu qurilma yangiliklar va ilmiy matnlarda juda koʻp
  uchraydi, chunki manbani aytmasdan maʼlumot berish imkonini beradi. Inshoda ishlatsangiz,
  yozganingiz ancha rasmiy eshitiladi.
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>The car is repairing now.</s></p>
  <p class="pe-good">The car <b>is being repaired</b> now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The work has finished by the students.</s></p>
  <p class="pe-good">The work <b>has been finished</b> by the students.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This must to be done today.</s></p>
  <p class="pe-good">This <b>must be done</b> today.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The letter was written by a pen.</s></p>
  <p class="pe-good">The letter was written <b>with</b> a pen.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The homework should have been did yesterday.</s></p>
  <p class="pe-good">The homework <b>should have been done</b> yesterday.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make it passive: <em>Somebody is painting the classroom.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The classroom is being painted.</strong></p>
      <p>Present Continuous → <em>is being</em> + V3.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it passive: <em>They have already sold all the tickets.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>All the tickets have already been sold.</strong></p>
      <p>Present Perfect → <em>have been</em> + V3, with <em>already</em> in its usual middle
         position.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make it passive: <em>You must wash these plates before dinner.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>These plates must be washed before dinner.</strong></p>
      <p>Modal + <b>be</b> + V3 — never <em>must to be</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     by or with: <em>The soup was made ___ my mother, ___ fresh vegetables.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>by my mother, with fresh vegetables.</strong> The doer takes <em>by</em>; the
         materials take <em>with</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Two passives from: <em>The teacher showed us a video.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>We were shown a video.</strong> (more natural)<br>
         <strong>A video was shown to us.</strong> (also correct)</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Agent</b><span>bajaruvchi</span></li>
  <li><b>Instrument</b><span>vosita</span></li>
  <li><b>To repair</b><span>taʼmirlamoq</span></li>
  <li><b>To sign</b><span>imzolamoq</span></li>
  <li><b>To announce</b><span>eʼlon qilmoq</span></li>
  <li><b>Impersonal</b><span>shaxssiz</span></li>
  <li><b>It is said that</b><span>aytishlaricha</span></li>
  <li><b>Prize</b><span>sovrin</span></li>
  <li><b>Form (document)</b><span>shakl, blanka</span></li>
  <li><b>Formal</b><span>rasmiy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>be</b> carries the tense; <b>V3</b> never changes.</li>
    <li>Modals: <b>modal + be + V3</b> · past: <b>modal + have been + V3</b>.</li>
    <li>Two-object verbs give two passives — the <b>person</b> version is more natural.</li>
    <li><b>by</b> = the doer · <b>with</b> = the tool.</li>
    <li><b>It is said that…</b> is the formal way to report without naming a source.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-62: Reported Speech: Statements and Backshift",
        "category": "english",
        "order": 62,
        "summary": (
            "How to tell somebody what somebody else said — the backshift rule that moves every "
            "verb one step into the past."
        ),
        "stories": ['What He Actually Said'],
        "content": """
<h2>PE-62: Reported Speech: Statements and Backshift</h2>

<p>Afsona says: <em>"I <b>am</b> tired."</em> An hour later you tell me about it. In Uzbek you
can simply repeat her words: <em>"Charchadim, dedi."</em> English does something different —
it pulls the whole sentence one step into the past: <em>"She said she <b>was</b> tired."</em>
That move is called <mark>backshift</mark>, and it is the heart of reported speech.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>say</b> and <b>tell</b> — which one takes a person</li>
    <li>The backshift table: every tense moves one step back</li>
    <li>What happens to pronouns, times and places</li>
    <li>When you do <b>not</b> need to backshift</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Reporting a statement</span>
  <span class="pe-chip pe-chip--s">He said</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--opt">(that)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">sentence, one step back</span>
</div>

LEGEND_HERE

<h3>1. say or tell?</h3>

<p>They are not interchangeable, and the rule is mechanical: <b>tell</b> needs a person
straight after it; <b>say</b> does not.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">tell + person</p>
    <ul>
      <li>He <b>told me</b> he was busy. ✓</li>
      <li>She <b>told us</b> the truth. ✓</li>
      <li><s>He told he was busy.</s> ✗</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">say (no person)</p>
    <ul>
      <li>He <b>said</b> he was busy. ✓</li>
      <li>He <b>said to me</b> that… ✓</li>
      <li><s>He said me he was busy.</s> ✗</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "menga aytdi" bitta shakl, ingliz tilida esa ikkita: <b>told me</b>
  (odam bilan) yoki <b>said to me</b> (predlog bilan). Eng koʻp uchraydigan xato —
  <s>said me</s>. Qoidani shunday eslang: <b>tell</b> soʻzi doim "<b>kimga</b>" ni
  talab qiladi, <b>say</b> esa yoʻq.
</div>

<h3>2. The backshift table</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Direct speech</th><th>Reported speech</th></tr>
  <tr><td>Present Simple — <em>"I <b>work</b>"</em></td><td>Past Simple — he <b>worked</b></td></tr>
  <tr><td>Present Cont. — <em>"I <b>am working</b>"</em></td><td>Past Cont. — he <b>was working</b></td></tr>
  <tr><td>Past Simple — <em>"I <b>worked</b>"</em></td><td>Past Perfect — he <b>had worked</b></td></tr>
  <tr><td>Present Perfect — <em>"I <b>have worked</b>"</em></td><td>Past Perfect — he <b>had worked</b></td></tr>
  <tr><td>will — <em>"I <b>will</b> come"</em></td><td><b>would</b> come</td></tr>
  <tr><td>can — <em>"I <b>can</b> swim"</em></td><td><b>could</b> swim</td></tr>
  <tr><td>must — <em>"I <b>must</b> go"</em></td><td><b>had to</b> go</td></tr>
  <tr><td>may — <em>"I <b>may</b> be late"</em></td><td><b>might</b> be late</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">"I <b>am</b> learning Korean." → She said she
     <span class="pe-hl pe-hl--v">was</span> learning Korean.</p>
  <p class="pe-ex__uz">"Koreys tilini oʻrganyapman." → U koreys tilini oʻrganayotganini
     aytdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">"I <b>will</b> help you." → He said he <b>would</b> help me.</p>
  <p class="pe-ex__uz">"Senga yordam beraman." → U menga yordam berishini aytdi.</p>
</div>

<p>Note that <b>would, could, should, might</b> and the Past Perfect cannot go back any
further — they stay as they are.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu — oʻzbek va ingliz tili orasidagi katta farq. Oʻzbekchada odamning soʻzlarini
  <b>oʻzgartirmasdan</b> keltirish odatiy: <em>"Boraman", dedi</em>. Ingliz tilida esa
  <b>hamma feʼl bir qadam orqaga suriladi</b>: <em>He said he <b>would</b> go</em>.
  Shuning uchun tarjima qilganda "dedi" dan keyingi qismni ham oʻzgartirishni yodda
  tuting.
</div>

<h3>3. Pronouns, times and places also move</h3>

<p>Reported speech is spoken from a different position, so the words that point at people,
times and places must be adjusted too.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Pronouns</p>
    <p><em>I → he/she · my → his/her · we → they</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Time</p>
    <p><em>now → then · today → that day · tomorrow → the next day · yesterday → the day
       before</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Place</p>
    <p><em>here → there · this → that · these → those</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>that</p>
    <p>Optional: <em>He said (that) he was busy.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">"<b>I</b> saw <b>your</b> brother <b>here yesterday</b>." → She said
     <b>she</b> had seen <b>my</b> brother <b>there the day before</b>.</p>
  <p class="pe-ex__uz">"Akangni kecha shu yerda koʻrdim." → U akamni bir kun oldin oʻsha yerda
     koʻrganini aytdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Vaqt va joy soʻzlari ham oʻzgarishini eslab qoling — bu mantiqan tushunarli: siz
  <b>boshqa joyda va boshqa paytda</b> gapiryapsiz. Afsona "<b>bugun</b>" degan boʻlsa,
  siz ertaga "<b>oʻsha kuni</b>" deysiz; u "<b>bu yerda</b>" degan boʻlsa, siz "<b>oʻsha
  yerda</b>" deysiz. Oʻzbekchada ham xuddi shunday qilamiz — faqat ingliz tilida bu
  qatʼiy qoida.
</div>

<h3>4. When you do NOT backshift</h3>

<ol class="pe-steps">
  <li><b>The reporting verb is in the present:</b> <em>He <b>says</b> he <b>is</b> tired.</em></li>
  <li><b>The statement is still true:</b> <em>She said she <b>lives</b> in Nukus.</em>
      (she still does — <em>lived</em> is also fine)</li>
  <li><b>It is a permanent fact:</b> <em>The teacher said water <b>boils</b> at 100°.</em></li>
  <li><b>You are repeating something just said:</b> <em>Sorry, what did you say? — I said
      I<b>'m</b> hungry.</em></li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In an exam, always backshift — it is never marked wrong. In real conversation, native
  speakers often skip it when the information is still true. So learn the rule properly, then
  relax about it when you speak.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He said me that he was tired.</s></p>
  <p class="pe-good">He <b>told me</b> that he was tired. / He <b>said</b> that he was tired.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She said she will call me later.</s></p>
  <p class="pe-good">She said she <b>would</b> call me later.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He said he is a doctor. (reporting later)</s></p>
  <p class="pe-good">He said he <b>was</b> a doctor.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She told that she had finished.</s></p>
  <p class="pe-good">She <b>told me</b> that she had finished.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He said he must to leave early.</s></p>
  <p class="pe-good">He said he <b>had to</b> leave early.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Report it: <em>Jasur: "I am waiting for my sister."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur said (that) he was waiting for his sister.</strong></p>
      <p>Present Continuous → Past Continuous, and <em>my</em> → <em>his</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Report it: <em>Afsona: "I have finished my homework."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona said she had finished her homework.</strong></p>
      <p>Present Perfect → Past Perfect.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     say or tell: <em>He ___ me the news, but he didn't ___ anything about the exam.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>told … say.</strong> <em>Told</em> because a person (<em>me</em>) follows;
         <em>say</em> because nothing but the object follows.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Report it: <em>Sherbek: "I will see you here tomorrow."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sherbek said he would see me there the next day.</strong></p>
      <p>Four changes: <em>will → would</em>, <em>you → me</em>, <em>here → there</em>,
         <em>tomorrow → the next day</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Does this need backshift? <em>The teacher said: "The Earth goes round the Sun."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>No.</strong> It is a permanent fact, so <em>The teacher said the Earth
         <b>goes</b> round the Sun</em> is correct (though <em>went</em> is also
         accepted).</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Reported speech</b><span>oʻzlashtirilgan gap</span></li>
  <li><b>Direct speech</b><span>koʻchirma gap</span></li>
  <li><b>Backshift</b><span>zamonni orqaga surish</span></li>
  <li><b>To report</b><span>yetkazmoq, xabar bermoq</span></li>
  <li><b>Statement</b><span>darak gap</span></li>
  <li><b>The next day</b><span>ertasi kuni</span></li>
  <li><b>The day before</b><span>bir kun oldin</span></li>
  <li><b>Permanent fact</b><span>doimiy haqiqat</span></li>
  <li><b>To adjust</b><span>moslashtirmoq</span></li>
  <li><b>Truth</b><span>haqiqat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>tell + person</b> · <b>say</b> without a person — never <s>said me</s>.</li>
    <li>Backshift: every tense moves <b>one step back</b>; <em>will → would</em>,
        <em>can → could</em>, <em>must → had to</em>.</li>
    <li>Pronouns, times and places shift too: <em>here → there</em>,
        <em>tomorrow → the next day</em>.</li>
    <li><b>that</b> is optional.</li>
    <li>No backshift needed for permanent facts or things still true.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-63: Reported Speech: Questions, Commands and Reporting Verbs",
        "category": "english",
        "order": 63,
        "summary": (
            "A reported question is not a question any more — no inversion, no question mark. "
            "Plus how to report orders, requests and a dozen useful reporting verbs."
        ),
        "stories": ['He Asked Where I Had Been'],
        "content": """
<h2>PE-63: Reported Speech: Questions, Commands and Reporting Verbs</h2>

<p>People do not only make statements — they ask, order, promise and refuse. Reporting those
needs one extra idea, and it is the one learners find strangest:
<mark>a reported question stops behaving like a question</mark>. No inversion, no
<em>do/does</em>, no question mark. Once you accept that, this lesson is easy.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Reporting yes/no questions with <b>if / whether</b></li>
    <li>Reporting wh- questions in normal word order</li>
    <li>Reporting orders and requests with <b>tell / ask + to</b></li>
    <li>A dozen reporting verbs and their patterns</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Reported question</span>
  <span class="pe-chip pe-chip--s">He asked</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">if / wh-word</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
</div>

LEGEND_HERE

<h3>1. Yes/no questions → if or whether</h3>

<div class="pe-ex">
  <p class="pe-ex__en">"<b>Are</b> you tired?" → He asked <b>if I was</b> tired.</p>
  <p class="pe-ex__uz">"Charchadingmi?" → U charchaganimni soʻradi.</p>
  <p class="pe-ex__why">The question order (<em>are you</em>) becomes statement order
     (<em>I was</em>).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">"<b>Do</b> you like plov?" → She asked <b>if I liked</b> plov.</p>
  <p class="pe-ex__uz">"Palovni yoqtirasanmi?" → U palovni yoqtirishimni soʻradi.</p>
  <p class="pe-ex__why"><em>Do</em> disappears completely — it only exists to build a real
     question.</p>
</div>

<h3>2. Wh- questions → keep the question word, drop the inversion</h3>

<div class="pe-ex">
  <p class="pe-ex__en">"<b>Where do</b> you live?" → He asked <b>where I lived</b>.</p>
  <p class="pe-ex__uz">"Qayerda yashaysan?" → U qayerda yashashimni soʻradi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✗ Still a question</p>
    <ul>
      <li><s>He asked where do I live.</s></li>
      <li><s>He asked where did I live.</s></li>
      <li><s>He asked me where I live?</s></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✓ Now a statement</p>
    <ul>
      <li>He asked <b>where I lived</b>.</li>
      <li>She wondered <b>what time it was</b>.</li>
      <li>I don't know <b>who he is</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu joyda oʻzbek tili sizga yordam beradi! Oʻzbekchada ham "Qayerda yashaysan?" degan
  savol oʻzlashtirilganda <b>savol shaklini yoʻqotadi</b>: "qayerda yashashi<b>mni</b>
  soʻradi". Ingliz tilida ham xuddi shunday — <b>do/does/did</b> yoʻqoladi, soʻz tartibi
  oddiy gapdek boʻladi va <b>savol belgisi qoʻyilmaydi</b>.
</div>

<h3>3. Orders and requests</h3>

<p>Commands and requests do not use <em>that</em> at all. They use <b>to + verb</b>, and the
negative is <b>not to + verb</b>.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Order → tell sb to</p>
    <p>"Sit down!" → He <b>told me to</b> sit down.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Request → ask sb to</p>
    <p>"Please wait." → She <b>asked me to</b> wait.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Negative → not to</p>
    <p>"Don't be late!" → He <b>told me not to</b> be late.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Advice → advise sb to</p>
    <p>"You should rest." → She <b>advised me to</b> rest.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The teacher <b>told us to open</b> our books and <b>not to talk</b>.</p>
  <p class="pe-ex__uz">Oʻqituvchi kitoblarimizni ochishimizni va gaplashmasligimizni aytdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>if</b> va <b>whether</b> deyarli bir xil, lekin farqi bor: <b>whether</b> tanlov
  boʻlganda va rasmiy matnda ishlatiladi — <em>He asked <b>whether</b> I wanted tea
  <b>or</b> coffee</em>. Shuningdek predlogdan keyin faqat <b>whether</b> keladi:
  <em>We talked about <b>whether</b> to go</em>. Oddiy suhbatda esa <b>if</b> yetarli.
</div>

<h3>4. Reporting verbs beyond say and tell</h3>

<p>Good English uses precise reporting verbs. Each has its own pattern — learn the verb together
with what follows it.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Verb</th><th>Pattern</th><th>Example</th></tr>
  <tr><td>offer</td><td>+ to + verb</td><td>He <b>offered to</b> help.</td></tr>
  <tr><td>promise</td><td>+ to + verb</td><td>She <b>promised to</b> call.</td></tr>
  <tr><td>refuse</td><td>+ to + verb</td><td>He <b>refused to</b> answer.</td></tr>
  <tr><td>agree</td><td>+ to + verb</td><td>They <b>agreed to</b> wait.</td></tr>
  <tr><td>advise / warn</td><td>+ sb + to</td><td>She <b>warned me not to</b> go.</td></tr>
  <tr><td>remind</td><td>+ sb + to</td><td>He <b>reminded me to</b> lock the door.</td></tr>
  <tr><td>suggest</td><td>+ -ing / that</td><td>He <b>suggested going</b> by bus.</td></tr>
  <tr><td>admit</td><td>+ -ing / that</td><td>She <b>admitted breaking</b> it.</td></tr>
  <tr><td>explain</td><td>+ that</td><td>He <b>explained that</b> he was late.</td></tr>
</table>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>Suggest</b> never takes <em>to + verb</em>. <s>He suggested to go</s> ✗ →
  <b>He suggested going</b> ✓ or <b>He suggested that we go</b> ✓. This is one of the most
  frequently tested patterns in exams.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Feʼlni <b>qolipi bilan birga</b> yodlang, alohida emas: <em>offer <b>to</b> do</em>,
  <em>suggest <b>doing</b></em>, <em>remind somebody <b>to</b> do</em>. Oʻzbekchada
  hammasi "taklif qildi, eslatdi" boʻlib bir xil tuzilishga ega, ingliz tilida esa har
  bir feʼlning <b>oʻz qolipi</b> bor — shuning uchun butun boʻlakni birga oʻrganish
  kerak.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He asked me where do I live.</s></p>
  <p class="pe-good">He asked me <b>where I lived</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She asked me that if I was ready.</s></p>
  <p class="pe-good">She asked me <b>if I was</b> ready. <em>(no "that" with if)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He told me don't be late.</s></p>
  <p class="pe-good">He told me <b>not to be</b> late.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She suggested to visit the museum.</s></p>
  <p class="pe-good">She <b>suggested visiting</b> the museum.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I asked him what time is it?</s></p>
  <p class="pe-good">I asked him <b>what time it was</b>.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Report it: <em>"Do you speak Korean?" she asked.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She asked if I spoke Korean.</strong></p>
      <p><em>Do</em> disappears, the order becomes normal, and no question mark is used.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Report it: <em>"Why are you laughing?" he asked.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He asked why I was laughing.</strong></p>
      <p>Keep <em>why</em>, then subject + verb — never <s>why was I laughing</s>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Report it: <em>"Don't touch the wires!" the teacher said.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The teacher told us not to touch the wires.</strong></p>
      <p>Commands use <b>tell + person + (not) to + verb</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Choose the best reporting verb: <em>"I'll definitely pay you back tomorrow," he said.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He promised to pay me back the next day.</strong></p>
      <p><em>Promised</em> carries far more meaning than <em>said</em> — that is why precise
         reporting verbs matter.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>My friend suggested to go to the cinema, but I refused going.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My friend suggested going to the cinema, but I refused to go.</strong></p>
      <p><em>Suggest</em> takes <b>-ing</b>; <em>refuse</em> takes <b>to + verb</b>. The two
         patterns are opposite.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Reported question</b><span>oʻzlashtirilgan soʻroq gap</span></li>
  <li><b>Command / order</b><span>buyruq</span></li>
  <li><b>Request</b><span>iltimos</span></li>
  <li><b>Whether</b><span>...mi (yoki yoʻqmi)</span></li>
  <li><b>To wonder</b><span>qiziqmoq, oʻylanmoq</span></li>
  <li><b>To offer</b><span>taklif qilmoq</span></li>
  <li><b>To refuse</b><span>rad etmoq</span></li>
  <li><b>To remind</b><span>eslatmoq</span></li>
  <li><b>To admit</b><span>tan olmoq</span></li>
  <li><b>To warn</b><span>ogohlantirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Yes/no questions → <b>ask if / whether</b> + normal word order.</li>
    <li>Wh- questions → keep the wh-word, then <b>subject + verb</b>. No <em>do/does</em>, no
        question mark.</li>
    <li>Orders and requests → <b>tell / ask + person + (not) to + verb</b>.</li>
    <li>Learn each reporting verb with its pattern: <b>offer to</b>, <b>suggest doing</b>,
        <b>remind sb to</b>.</li>
    <li><b>suggest</b> never takes <em>to + verb</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-64: Gerunds and Infinitives: The Basics",
        "category": "english",
        "order": 64,
        "summary": (
            "When to say 'I enjoy reading' and when to say 'I want to read' — the two ways a "
            "verb follows another verb, and the preposition rule that never fails."
        ),
        "stories": ['I Enjoy Cooking, I Want to Cook'],
        "content": """
<h2>PE-64: Gerunds and Infinitives: The Basics</h2>

<p>Two verbs meet in one sentence, and English must decide what to do with the second one.
<em>"I enjoy <b>reading</b>."</em> <em>"I want <b>to read</b>."</em> Both are correct; swap them
and both become wrong. This is the <mark>gerund / infinitive</mark> choice — and while part of
it must be memorised, one big part of it follows a rule that never fails.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What a <b>gerund</b> (-ing) and an <b>infinitive</b> (to + verb) are</li>
    <li>The rule that always works: <b>after a preposition, always -ing</b></li>
    <li>Which verbs take which — the two lists worth memorising</li>
    <li>The pattern <b>verb + person + to</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two possibilities</span>
  <span class="pe-chip pe-chip--v">verb + -ing</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">gerund</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">to + verb</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">infinitive</span>
</div>

LEGEND_HERE

<h3>1. The gerund is a verb acting as a noun</h3>

<p>Add <b>-ing</b> and a verb can do everything a noun does — be the subject, be the object,
follow a preposition.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Swimming</b> is good for you. — I love <b>swimming</b>. — He's afraid
     of <b>swimming</b>.</p>
  <p class="pe-ex__uz">Suzish foydali. — Suzishni yaxshi koʻraman. — U suzishdan qoʻrqadi.</p>
  <p class="pe-ex__why">Subject, object, and after a preposition — all with the same
     <b>-ing</b> form.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Gerund oʻzbekchadagi <b>-ish / -moq</b> shakliga toʻgʻri keladi: <em>suz<b>ish</b></em> →
  <em>swimming</em>, <em>oʻqi<b>sh</b></em> → <em>reading</em>. Infinitiv esa "<b>...moqni
  xohlamoq</b>" kabi qurilmalarda: <em>bor<b>moqchiman</b></em> → <em>I want <b>to
  go</b></em>. Oʻzbekchada bitta shakl ikkisini ham qoplaydi — shuning uchun ingliz tilida
  qaysi feʼl qaysi shaklni olishini <b>alohida</b> yodlash kerak.
</div>

<h3>2. The rule that never fails: after a preposition, -ing</h3>

<p>If a verb comes straight after <em>in, on, at, of, for, about, after, before, without,
by</em> — it takes <b>-ing</b>. No exceptions.</p>

<div class="pe-ex">
  <p class="pe-ex__en">She's good <b>at drawing</b>. — Thank you <b>for helping</b> me. —
     He left <b>without saying</b> goodbye. — <b>Before going</b> out, close the window.</p>
  <p class="pe-ex__uz">U rasm chizishda zoʻr. — Yordam berganingiz uchun rahmat. — U xayrlashmasdan
     ketdi. — Chiqishdan oldin derazani yoping.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Watch out for phrases where <b>to</b> is a preposition, not part of an infinitive:
  <em>look forward <b>to</b></em>, <em>be used <b>to</b></em>, <em>instead <b>of</b></em>.
  <s>I look forward to see you</s> ✗ → <b>I look forward to seeing you</b> ✓.
</div>

<h3>3. Verbs that take -ing</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Feelings about activities</p>
    <p><em>enjoy, like, love, hate, don't mind, can't stand</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Starting and stopping</p>
    <p><em>start, begin, finish, stop, keep, give up, carry on</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Avoiding and suggesting</p>
    <p><em>avoid, suggest, imagine, practise, consider</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Also</p>
    <p><em>spend time, waste time, it's worth, it's no use</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>enjoy cooking</b>, but I <b>avoid washing</b> up. Afsona
     <b>practises speaking</b> English every day.</p>
  <p class="pe-ex__uz">Ovqat pishirishni yoqtiraman, lekin idish yuvishdan qochaman. Afsona
     har kuni ingliz tilida gapirishni mashq qiladi.</p>
</div>

<h3>4. Verbs that take to + verb</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">verb + to + verb</p>
    <ul>
      <li><em>want, need, hope, plan, decide</em></li>
      <li><em>promise, agree, refuse, offer</em></li>
      <li><em>learn, try, manage, forget, seem</em></li>
      <li><em>would like, would love</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">verb + person + to + verb</p>
    <ul>
      <li><em>tell, ask, want, allow</em></li>
      <li><em>advise, remind, warn, teach</em></li>
      <li>He <b>asked me to</b> wait.</li>
      <li>She <b>taught us to</b> swim.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>decided to study</b> harder, and my teacher <b>advised me to
     start</b> with grammar.</p>
  <p class="pe-ex__uz">Qattiqroq oʻqishga qaror qildim va oʻqituvchim grammatikadan boshlashimni
     maslahat berdi.</p>
</div>

<p>And remember from PE-42: after a <b>modal</b>, the verb takes <b>no <em>to</em></b> at all —
<em>I can swim</em>, <em>you should go</em>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Roʻyxatni yodlashning eng qulay yoʻli — <b>juftlik bilan</b>: <em>enjoy reading</em>,
  <em>want to read</em>, <em>finish eating</em>, <em>decide to eat</em>. Har bir feʼlni
  <b>keyingi soʻzi bilan birga</b> ayting va shu holda yodlang. Alohida yodlangan feʼl
  gapda xato shakl bilan chiqadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Gap <b>boshida</b> feʼl kelsa, deyarli doim <b>-ing</b> shakli ishlatiladi:
  <em><b>Smoking</b> is bad for you</em>, <em><b>Learning</b> languages takes time</em>.
  Oʻzbekchada ham xuddi shunday — "<b>Chekish</b> zararli", "<b>Til oʻrganish</b> vaqt
  talab qiladi" — harakat nomi ega boʻlib keladi. <s>To smoke is bad</s> grammatik
  jihatdan mumkin, lekin juda rasmiy va gʻalati eshitiladi.
</div>

<h3>5. Both possible, no real difference</h3>

<p>With <b>start, begin, continue</b> and the feeling verbs <b>like, love, hate</b>, both forms
are correct and mean the same thing:</p>

<div class="pe-ex">
  <p class="pe-ex__en">It <b>started raining</b>. = It <b>started to rain</b>. — I <b>like
     swimming</b>. = I <b>like to swim</b>.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻa boshladi. — Suzishni yoqtiraman.</p>
  <p class="pe-ex__why">Do not lose marks worrying about these — either answer is accepted.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I enjoy to read books.</s></p>
  <p class="pe-good">I <b>enjoy reading</b> books.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I want going home.</s></p>
  <p class="pe-good">I <b>want to go</b> home.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She's good at to cook.</s></p>
  <p class="pe-good">She's good <b>at cooking</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I look forward to meet you.</s></p>
  <p class="pe-good">I look forward <b>to meeting</b> you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He suggested to take a taxi.</s></p>
  <p class="pe-good">He <b>suggested taking</b> a taxi.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>I've finished <span class="pe-blank">?</span> (write) my essay, so I've
     decided <span class="pe-blank">?</span> (watch) a film.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>writing … to watch.</strong> <em>Finish</em> takes <b>-ing</b>;
         <em>decide</em> takes <b>to + verb</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>Thank you for <span class="pe-blank">?</span> (invite) me.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>inviting</strong> — <em>for</em> is a preposition, and after a preposition it
         is always <b>-ing</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>My mother told me to don't be late.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My mother told me not to be late.</strong></p>
      <p>The negative of <em>to + verb</em> is <b>not to + verb</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Why is <em>"I'm looking forward to see you"</em> wrong?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because that "to" is a preposition, not an infinitive marker.</strong>
         So: <em>looking forward <b>to seeing</b> you</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write two sentences about yourself: one with <em>enjoy</em>, one with <em>want</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I <b>enjoy playing</b> football with my friends, and I
         <b>want to learn</b> Korean next year.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Gerund</b><span>-ing shakli (harakat nomi)</span></li>
  <li><b>Infinitive</b><span>infinitiv (to + feʼl)</span></li>
  <li><b>Preposition</b><span>predlog</span></li>
  <li><b>To avoid</b><span>qochmoq</span></li>
  <li><b>To practise</b><span>mashq qilmoq</span></li>
  <li><b>To give up</b><span>tashlab qoʻymoq</span></li>
  <li><b>Can't stand</b><span>toqat qilolmaslik</span></li>
  <li><b>To look forward to</b><span>intiqlik bilan kutmoq</span></li>
  <li><b>To allow</b><span>ruxsat bermoq</span></li>
  <li><b>It's worth</b><span>arziydi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>After a preposition, always -ing</b> — the one rule with no exceptions.</li>
    <li><b>-ing verbs:</b> enjoy, finish, avoid, suggest, keep, practise, don't mind.</li>
    <li><b>to + verb:</b> want, need, hope, decide, promise, learn, refuse.</li>
    <li><b>verb + person + to:</b> tell, ask, advise, remind, allow.</li>
    <li>Learn each verb <b>with its pattern</b>, never alone.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-65: Verbs That Change Meaning: stop doing vs stop to do",
        "category": "english",
        "order": 65,
        "summary": (
            "Six verbs where -ing and to + verb mean completely different things — the "
            "difference between stopping smoking and stopping to smoke."
        ),
        "stories": ['He Stopped to Help'],
        "content": """
<h2>PE-65: Verbs That Change Meaning: stop doing vs stop to do</h2>

<p>In PE-64 most verbs took one form or the other. Now meet the small group that takes
<b>both</b> — and changes meaning completely when it does. <em>"He stopped <b>smoking</b>"</em>
means he gave up cigarettes. <em>"He stopped <b>to smoke</b>"</em> means he paused what he was
doing in order to have one. Same verb, opposite lives.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>stop, remember, forget, try, go on</b> — the meaning-changing verbs</li>
    <li>The logic behind the change: <b>-ing</b> looks back, <b>to</b> looks forward</li>
    <li><b>like doing</b> vs <b>like to do</b></li>
    <li>The passive-meaning pattern <b>need washing</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The underlying logic</span>
  <span class="pe-chip pe-chip--v">-ing</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">the activity itself / earlier</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">to + verb</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">the purpose / later</span>
</div>

LEGEND_HERE

<h3>1. stop</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">stop + -ing = end the activity</p>
    <p><em>He <b>stopped smoking</b> last year.</em></p>
    <p>= he gave it up (chekishni tashladi)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">stop + to = pause in order to</p>
    <p><em>He <b>stopped to smoke</b>.</em></p>
    <p>= he paused so that he could smoke</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">We were driving for hours, so we <b>stopped to have</b> lunch. Then my
     brother <b>stopped complaining</b> about being hungry.</p>
  <p class="pe-ex__uz">Bir necha soat yoʻl yurdik, shuning uchun tushlik qilish uchun
     toʻxtadik. Keyin akam qorni ochligi haqida shikoyat qilishni bas qildi.</p>
</div>

<h3>2. remember and forget</h3>

<p>Here the difference is <b>time order</b>. With <b>-ing</b>, the action happened <b>first</b>
and you remember it afterwards. With <b>to</b>, the remembering comes first and the action
follows.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">-ing = a memory of the past</p>
    <ul>
      <li>I <b>remember locking</b> the door. <em>(I did it, and I recall it)</em></li>
      <li>I'll never <b>forget meeting</b> her.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">to = a duty, before the action</p>
    <ul>
      <li>Please <b>remember to lock</b> the door. <em>(don't forget!)</em></li>
      <li>I <b>forgot to lock</b> it. <em>(so it's open)</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni oʻzbekcha orqali koʻring: <b>remember + -ing</b> = "qilganimni <b>eslayman</b>"
  (ish allaqachon boʻlgan). <b>remember + to</b> = "qilishni <b>esdan chiqarmang</b>"
  (ish hali boʻlmagan). <b>forgot to lock</b> = "qulflashni esdan chiqardim" — yaʼni
  eshik ochiq qoldi. Vaqt tartibi hal qiladi.
</div>

<h3>3. try</h3>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>tried to open</b> the window, but it was stuck. <em>(I attempted
     it)</em><br>
     <b>Try opening</b> the other window. <em>(experiment — maybe that will work)</em></p>
  <p class="pe-ex__uz">Derazani ochishga harakat qildim, lekin qotib qolgan edi. — Boshqa
     derazani ochib koʻring-chi.</p>
</div>

<p>So <b>try to</b> = make an effort (it may fail); <b>try -ing</b> = test a method as a
possible solution.</p>

<h3>4. go on</h3>

<div class="pe-ex">
  <p class="pe-ex__en">She <b>went on talking</b> for an hour. <em>(continued the same
     thing)</em><br>
     She finished her introduction and <b>went on to explain</b> the results. <em>(moved to the
     next thing)</em></p>
  <p class="pe-ex__uz">U bir soat gapirishda davom etdi. — Kirish qismini tugatib, natijalarni
     tushuntirishga oʻtdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Hammasini bitta mantiq bilan eslab qolish mumkin: <b>-ing</b> — ishning <b>oʻzi</b>
  yoki <b>allaqachon boʻlgani</b> ("chekishni tashladi", "qulflaganimni eslayman").
  <b>to + feʼl</b> — <b>maqsad</b> yoki <b>keyin boʻladigan ish</b> ("chekish uchun
  toʻxtadi", "qulflashni esdan chiqarmang"). Shubhaga borsangiz shu savolni bering:
  <b>ish allaqachon boʻldimi yoki hali boʻladimi?</b>
</div>

<h3>5. like, love, hate — a small difference</h3>

<p>These usually mean the same with either form (PE-64), but there is a fine shade:
<b>-ing</b> = I enjoy the activity; <b>to</b> = I think it is a good idea, a habit or a
choice.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>like swimming</b>. <em>(I enjoy it)</em> — I <b>like to check</b>
     my homework twice. <em>(it's my habit; I think it's wise)</em></p>
  <p class="pe-ex__uz">Suzishni yaxshi koʻraman. — Uy vazifamni ikki marta tekshirishni
     odat qilganman.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>would like</b> is different from <b>like</b>. It always takes <b>to + verb</b> and means
  "want": <em>I'<b>d like to go</b></em> ✓, not <s>I'd like going</s>.
</div>

<h3>6. need + -ing — a passive meaning</h3>

<p>One last useful pattern. When the <b>subject is a thing</b>, <em>need + -ing</em> has a
passive meaning: something has to be done <b>to</b> it.</p>

<div class="pe-ex">
  <p class="pe-ex__en">The car <b>needs washing</b>. = The car <b>needs to be washed</b>. —
     My shoes <b>need repairing</b>.</p>
  <p class="pe-ex__uz">Mashinani yuvish kerak. — Tuflilarimni taʼmirlash kerak.</p>
  <p class="pe-ex__why">But with a person: <em>I <b>need to wash</b> the car</em> — active,
     normal infinitive.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>need + -ing</b> qurilmasi oʻzbekchadagi "<b>...ish kerak</b>" ga toʻgʻri keladi va
  majhul maʼno beradi: <em>The car needs washing</em> = "Mashinani yuvish kerak" (kim
  yuvishi aytilmaydi). Agar bajaruvchini aytmoqchi boʻlsangiz, oddiy infinitiv oling:
  <em>I need to wash the car</em> — "Men mashinani yuvishim kerak".
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He stopped to smoke ten years ago and is much healthier now.</s></p>
  <p class="pe-good">He <b>stopped smoking</b> ten years ago.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Remember locking the door before you leave!</s></p>
  <p class="pe-good"><b>Remember to lock</b> the door before you leave!</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I forgot turning off the lights, so they were on all night.</s></p>
  <p class="pe-good">I <b>forgot to turn off</b> the lights.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'd like going to the cinema tonight.</s></p>
  <p class="pe-good">I'<b>d like to go</b> to the cinema tonight.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My bike needs to repairing.</s></p>
  <p class="pe-good">My bike <b>needs repairing</b> / <b>needs to be repaired</b>.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     What is the difference? <em>(a) He stopped reading. (b) He stopped to read.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) He was reading and he ended it.</strong>
         <strong>(b) He was doing something else and paused in order to read.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>Did you remember <span class="pe-blank">?</span> (post) my letter?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>to post</strong> — you are asking whether the duty was carried out.
         <em>Remember posting</em> would ask whether he recalls doing it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Choose: <em>The computer isn't working. <span class="pe-blank">?</span> (try / restart)
     it.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Try restarting it.</strong> You are suggesting a method that might solve the
         problem — not describing an effort.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Rewrite: <em>Somebody needs to clean these windows.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>These windows need cleaning.</strong> (or <em>need to be cleaned</em>)</p>
      <p>The thing becomes the subject and the meaning turns passive.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Explain: <em>I'll never forget visiting Samarkand.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I visited Samarkand, and the memory will stay with me for ever.</strong></p>
      <p><em>Forget to visit</em> would mean failing to go at all.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>To give up</b><span>tashlamoq, voz kechmoq</span></li>
  <li><b>To pause</b><span>toʻxtab turmoq</span></li>
  <li><b>Purpose</b><span>maqsad</span></li>
  <li><b>Memory</b><span>xotira</span></li>
  <li><b>Duty</b><span>vazifa, majburiyat</span></li>
  <li><b>To attempt</b><span>harakat qilmoq</span></li>
  <li><b>To be stuck</b><span>qotib qolmoq</span></li>
  <li><b>To restart</b><span>qayta ishga tushirmoq</span></li>
  <li><b>To post (a letter)</b><span>xat joʻnatmoq</span></li>
  <li><b>Habit</b><span>odat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>stop -ing</b> = end it · <b>stop to</b> = pause in order to do it.</li>
    <li><b>remember/forget -ing</b> = a memory · <b>+ to</b> = a duty before the action.</li>
    <li><b>try to</b> = make an effort · <b>try -ing</b> = test a method.</li>
    <li><b>go on -ing</b> = continue · <b>go on to</b> = move to the next thing.</li>
    <li><b>need + -ing</b> has a passive meaning: <em>the car needs washing</em>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
