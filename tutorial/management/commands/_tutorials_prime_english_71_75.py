# -*- coding: utf-8 -*-
"""Prime English — Block F, lessons 71–75 (determiners, word order, tags, agreement).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_71_75.py --author=prime
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
        "title": "PE-71: Determiners: each, every, both, either, neither, all",
        "category": "english",
        "order": 71,
        "summary": (
            "Talking about groups with precision — one by one, two together, one of two, or "
            "none of them. Plus the singular verbs that surprise everybody."
        ),
        "stories": ['Both Brothers, Neither Answer'],
        "content": """
<h2>PE-71: Determiners: each, every, both, either, neither, all</h2>

<p>Uzbek handles groups with a small set of words: <em>har bir</em>, <em>ikkisi ham</em>,
<em>hech qaysi</em>. English has more of them, and — here is the part that catches learners —
several of them take a <mark>singular verb</mark> even though they clearly talk about many
people. <em>"<b>Everybody is</b> here."</em> Let's sort them all out.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>every</b> vs <b>each</b> — the group and the individual</li>
    <li><b>both / either / neither</b> — the words for exactly two</li>
    <li><b>all</b> and <b>none</b></li>
    <li>Which of them take a <b>singular</b> verb</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The surprise</span>
  <span class="pe-chip pe-chip--s">every / each / either / neither</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">singular noun + singular verb</span>
</div>

LEGEND_HERE

<h3>1. every and each</h3>

<p>Both mean "all of them, considered one at a time", and both take a <b>singular</b> noun and
verb. The difference is where your attention is.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">every — the whole group</p>
    <ul>
      <li><b>Every</b> student <b>has</b> a book.</li>
      <li>I go there <b>every</b> day.</li>
      <li>Used for 3 or more.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">each — one by one</p>
    <ul>
      <li><b>Each</b> student <b>has</b> a different book.</li>
      <li>She gave <b>each</b> child a sweet.</li>
      <li>Can be used for 2.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Every pupil</span>
     <span class="pe-hl pe-hl--v">was</span> present, and the teacher checked
     <b>each</b> notebook carefully.</p>
  <p class="pe-ex__uz">Har bir oʻquvchi hozir edi va oʻqituvchi har bir daftarni sinchkovlik
     bilan tekshirdi.</p>
  <p class="pe-ex__why">Singular nouns (<em>pupil, notebook</em>) and a singular verb
     (<em>was</em>) — even though many people are involved.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "<b>har bir</b>" dan keyin ot birlikda keladi — va ingliz tilida ham xuddi
  shunday: <em>every <b>student</b></em>, <s>every students</s> ✗. Feʼl ham birlikda:
  <em>every student <b>has</b></em>. Bu — eng koʻp uchraydigan xato, chunki maʼno jihatdan
  koʻplik tuyuladi.
</div>

<h3>2. The -body / -one / -thing words</h3>

<p><b>Everybody, everyone, somebody, nobody, anything</b> — all of them take a
<b>singular</b> verb.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Everybody is</b> ready. — <b>Nobody knows</b> the answer. —
     <b>Everything was</b> perfect.</p>
  <p class="pe-ex__uz">Hamma tayyor. — Hech kim javobni bilmaydi. — Hammasi mukammal edi.</p>
  <p class="pe-ex__why">In speech people say <em>everybody has <b>their</b> book</em> — the
     pronoun goes plural even though the verb stays singular.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qiziq holat: <b>everybody</b> feʼlni birlikda oladi, lekin olmoshi <b>koʻplikda</b>
  boʻladi — <em>Everybody <b>has</b> <b>their</b> own book</em>. Sababi: kimligi maʼlum
  emas, shuning uchun <em>his or her</em> oʻrniga qulay <em>their</em> ishlatiladi.
  Oʻzbekchada "har kim <b>oʻz</b> kitobiga ega" deganimizdek — bu ham betaraf shakl.
</div>

<h3>3. both, either, neither — the words for two</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>both — the two together</p>
    <p><b>Both</b> books <b>are</b> good. <em>(plural verb!)</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>either — one of the two</p>
    <p><b>Either</b> book <b>is</b> fine. <em>(singular)</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>neither — not one of them</p>
    <p><b>Neither</b> book <b>is</b> interesting. <em>(singular, already negative)</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>The pairs</p>
    <p><b>both … and</b> · <b>either … or</b> · <b>neither … nor</b></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Both</b> Afsona <b>and</b> Jasur passed. — We can go <b>either</b>
     today <b>or</b> tomorrow. — <b>Neither</b> Sherbek <b>nor</b> his brother was at home.</p>
  <p class="pe-ex__uz">Afsona ham, Jasur ham oʻtdi. — Yo bugun, yo ertaga borsak boʻladi. —
     Na Sherbek, na akasi uyda edi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>Neither</b> is already negative, so it never takes another negative:
  <s>Neither of them didn't come</s> ✗ → <b>Neither of them came</b> ✓. Same rule as
  <em>never</em> in PE-11.
</div>

<h3>4. With "of" — and the verb question</h3>

<p>Add <b>of</b> when you point at a specific group. The noun then becomes plural, but watch what
happens to the verb.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Structure</th><th>Verb</th><th>Example</th></tr>
  <tr><td>each / every one <b>of</b> + plural</td><td>singular</td><td><b>Each of</b> the boys <b>is</b> tall.</td></tr>
  <tr><td>either / neither <b>of</b> + plural</td><td>singular</td><td><b>Neither of</b> them <b>knows</b>.</td></tr>
  <tr><td>both <b>of</b> + plural</td><td>plural</td><td><b>Both of</b> them <b>are</b> here.</td></tr>
  <tr><td>all <b>of</b> + plural</td><td>plural</td><td><b>All of</b> the students <b>were</b> late.</td></tr>
  <tr><td>none <b>of</b> + plural</td><td>either</td><td><b>None of</b> them <b>was/were</b> ready.</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani mantiq bilan eslang: <b>each, every, either, neither</b> — bularning hammasi
  "<b>bittasi</b>" haqida gapiradi ("har bir<b>i</b>", "ikkisidan bir<b>i</b>"), shuning
  uchun feʼl <b>birlikda</b>. <b>Both, all</b> esa "<b>ikkisi ham</b>", "<b>hammasi</b>"
  degani — koʻplik, shuning uchun feʼl ham <b>koʻplikda</b>.
</div>

<h3>5. all — and where it sits</h3>

<p><b>All</b> works with plural and uncountable nouns. Note that <em>all</em> alone needs no
<em>of</em>; with <em>the</em> or a pronoun, <em>of</em> appears.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>All</b> children love stories. — <b>All of the</b> children were
     tired. — <b>All</b> the milk has gone.</p>
  <p class="pe-ex__uz">Barcha bolalar ertakni yaxshi koʻradi. — Bolalarning hammasi charchagan
     edi. — Sut butunlay tugagan.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Every students must bring a pen.</s></p>
  <p class="pe-good"><b>Every student</b> must bring a pen.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Both of them is my friends.</s></p>
  <p class="pe-good"><b>Both of them are</b> my friends.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Neither of the answers aren't correct.</s></p>
  <p class="pe-good"><b>Neither of</b> the answers <b>is</b> correct.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Everybody are waiting outside.</s></p>
  <p class="pe-good"><b>Everybody is</b> waiting outside.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>All of student passed the exam.</s></p>
  <p class="pe-good"><b>All of the students</b> passed the exam.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>Every child in the class <span class="pe-blank">?</span> (have) a
     dictionary.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>has</strong> — <em>every</em> takes a singular noun and a singular verb, even
         though many children are meant.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     both, either or neither: <em>___ of my parents speaks English — only my sister does.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Neither</strong> — it means "not one of the two", and it carries the negative
         by itself.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>Both of my brother are students.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Both of my brothers are students.</strong></p>
      <p>After <em>both of</em> the noun must be <b>plural</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What is the difference? <em>(a) Every answer is wrong. (b) Each answer is wrong.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) looks at the group as a whole</strong> — all of them, generally.
         <strong>(b) looks at them one by one</strong> — I checked them individually.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Join with <em>either … or</em>: <em>We can take the bus. We can take a taxi.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>We can take either the bus or a taxi.</strong></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Determiner</b><span>aniqlovchi soʻz</span></li>
  <li><b>Every</b><span>har bir</span></li>
  <li><b>Each</b><span>har biri (alohida)</span></li>
  <li><b>Both</b><span>ikkisi ham</span></li>
  <li><b>Either</b><span>ikkisidan biri</span></li>
  <li><b>Neither</b><span>hech qaysi biri</span></li>
  <li><b>All</b><span>hammasi</span></li>
  <li><b>None</b><span>hech biri</span></li>
  <li><b>Individual</b><span>alohida, yakka</span></li>
  <li><b>Present (there)</b><span>hozir, mavjud</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>every / each</b> + singular noun + singular verb.</li>
    <li><b>everybody, nobody, everything</b> → singular verb.</li>
    <li>For two: <b>both</b> (plural verb) · <b>either / neither</b> (singular verb).</li>
    <li><b>neither</b> is already negative — one negative per sentence.</li>
    <li>Pairs: <b>both … and</b>, <b>either … or</b>, <b>neither … nor</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-72: Word Order in English: SVOMPT",
        "category": "english",
        "order": 72,
        "summary": (
            "The master rule of English sentence building: subject, verb, object, then manner, "
            "place and time — in that order, every time."
        ),
        "stories": ['The Sentence That Sounded Wrong'],
        "content": """
<h2>PE-72: Word Order in English: SVOMPT</h2>

<p>In PE-1 you learned that English puts the verb second, not last. Now here is the full chain
that governs every longer sentence you will ever write:
<mark>S – V – O – Manner – Place – Time</mark>. English is unusually strict about this. Learn the
chain once and your sentences will simply come out in the right order.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The <b>SVOMPT</b> chain, with an example for each link</li>
    <li>The one place you must <b>never</b> put anything</li>
    <li>Where adverbs of frequency and time may move</li>
    <li>The two patterns for <em>give somebody something</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The master chain</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">Verb</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">Object</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">Manner</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">Place</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">Time</span>
</div>

LEGEND_HERE

<h3>1. The chain in one sentence</h3>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--v">sang</span>
     <span class="pe-hl pe-hl--o">a song</span>
     <span class="pe-hl pe-hl--adv">beautifully</span>
     <span class="pe-hl pe-hl--adv">at the concert</span>
     <span class="pe-hl pe-hl--adv">last night</span>.</p>
  <p class="pe-ex__uz">Afsona kecha kechqurun konsertda qoʻshiqni ajoyib kuyladi.</p>
  <p class="pe-ex__why">Six links, and every one in its place: who, did, what, how, where,
     when.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekcha tarjimani solishtiring — tartib deyarli <b>teskari</b>: oʻzbekchada avval
  vaqt ("kecha kechqurun"), keyin joy ("konsertda"), keyin tarz ("ajoyib"), oxirida feʼl
  ("kuyladi"). Ingliz tilida esa aynan aksincha: <b>feʼl oldinda, vaqt oxirida</b>.
  Shuning uchun soʻzma-soʻz tarjima qilmang — zanjirni yodda tuting.
</div>

<h3>2. The forbidden place</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  <b>Never put anything between the verb and its object.</b> They belong together.
  <s>I like very much English</s> ✗ → <b>I like English very much</b> ✓.
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>She speaks fluently English.</s></p>
  <p class="pe-good">She speaks <b>English fluently</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I finished quickly my homework.</s></p>
  <p class="pe-good">I finished <b>my homework quickly</b>.</p>
</div>

<h3>3. Which links can move?</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Time can go first</p>
    <p><em><b>Yesterday</b> we went to the bazaar.</em> — for emphasis.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Frequency goes mid</p>
    <p><em>I <b>always</b> get up early.</em> (PE-11)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Manner is flexible</p>
    <p><em>She <b>quickly</b> opened it.</em> = <em>She opened it <b>quickly</b></em>.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Place stays put</p>
    <p>Almost always after the object, before time.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">We study English <b>at school every day</b>. — <b>Every day</b> we study
     English at school.</p>
  <p class="pe-ex__uz">Biz har kuni maktabda ingliz tilini oʻrganamiz.</p>
  <p class="pe-ex__why">Both correct. What you cannot do is put <em>every day</em> between
     <em>study</em> and <em>English</em>.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>usually</b> do my homework <b>quietly in my room after dinner</b>.</p>
  <p class="pe-ex__uz">Men odatda kechki ovqatdan keyin xonamda jimgina uy vazifamni
     bajaraman.</p>
  <p class="pe-ex__why">Frequency (<em>usually</em>) in the middle, then the full chain:
     manner → place → time.</p>
</div>

<h3>4. Two objects: give somebody something</h3>

<p>Verbs like <em>give, send, show, tell, buy, lend</em> can take two objects. There are two
correct patterns, and the word <b>to</b> decides the order.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">person first — no "to"</p>
    <ul>
      <li>She gave <b>me a present</b>.</li>
      <li>He sent <b>his mother flowers</b>.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">thing first — with "to"</p>
    <ul>
      <li>She gave <b>a present to me</b>.</li>
      <li>He sent <b>flowers to his mother</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>She gave to me a present.</s></p>
  <p class="pe-good">She gave <b>me</b> a present. / She gave a present <b>to me</b>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "menga sovgʻa berdi" — bitta tartib. Ingliz tilida ikkita yoʻl bor va
  <b>to</b> soʻzi tartibni belgilaydi: odam oldinda boʻlsa — <b>to yoʻq</b>
  (<em>gave <b>me</b> a present</em>), narsa oldinda boʻlsa — <b>to bor</b>
  (<em>gave a present <b>to me</b></em>). Ikkalasini aralashtirib <s>gave to me a
  present</s> deb yozib qoʻymang.
</div>

<h3>5. A quick checklist for your writing</h3>

<ol class="pe-steps">
  <li><b>Is the verb right after the subject?</b> Not at the end (that is Uzbek order).</li>
  <li><b>Is anything sitting between the verb and the object?</b> Move it to the end.</li>
  <li><b>Are manner, place and time in that order?</b> How → where → when.</li>
  <li><b>Is the adjective before its noun?</b> (PE-15) And frequency adverbs before the verb?
      (PE-11)</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yozganingizdan keyin shu tartibni <b>ovoz chiqarib</b> tekshirib chiqing:
  "<b>kim — nima qildi — nimani — qanday — qayerda — qachon</b>". Agar biror boʻlak
  oʻz oʻrnida boʻlmasa, quloqqa gʻalati eshitiladi. Bu — inshoda eng koʻp ball
  yoʻqotadigan joy, shuning uchun har safar tekshirish arziydi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I like very much this film.</s></p>
  <p class="pe-good">I like <b>this film very much</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She yesterday went to Samarkand.</s></p>
  <p class="pe-good">She went to Samarkand <b>yesterday</b>. / <b>Yesterday</b> she went to
     Samarkand.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We every Sunday play football in the park.</s></p>
  <p class="pe-good">We play football in the park <b>every Sunday</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He read yesterday in the library a book.</s></p>
  <p class="pe-good">He read <b>a book in the library yesterday</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I go always to school on foot.</s></p>
  <p class="pe-good">I <b>always go</b> to school on foot.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Put in order: <em>in the garden / played / the children / happily / all morning</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The children played happily in the garden all morning.</strong></p>
      <p>S – V – Manner – Place – Time.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>I speak very well English.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I speak English very well.</strong></p>
      <p>Nothing may stand between <em>speak</em> and <em>English</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Two ways: <em>Jasur / a letter / his cousin / sent</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur sent his cousin a letter.</strong> /
         <strong>Jasur sent a letter to his cousin.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Put in order: <em>quietly / the door / she / closed</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She closed the door quietly.</strong> (also acceptable: <em>She quietly
         closed the door</em>.)</p>
      <p>What you cannot write is <s>She closed quietly the door</s>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one sentence with all six links (S-V-O-M-P-T).</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Sherbek finished his homework carefully in his room
         yesterday evening.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Word order</b><span>soʻz tartibi</span></li>
  <li><b>Manner</b><span>tarz, qanday</span></li>
  <li><b>Place</b><span>joy</span></li>
  <li><b>Time</b><span>payt</span></li>
  <li><b>Adverb</b><span>ravish</span></li>
  <li><b>Direct object</b><span>vositasiz toʻldiruvchi</span></li>
  <li><b>Indirect object</b><span>vositali toʻldiruvchi</span></li>
  <li><b>Fluently</b><span>ravon</span></li>
  <li><b>Quietly</b><span>sekin, jimgina</span></li>
  <li><b>Emphasis</b><span>taʼkid</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>S – V – O – Manner – Place – Time.</b> How, then where, then when.</li>
    <li><b>Never</b> put anything between the verb and its object.</li>
    <li>Time may move to the front for emphasis; place almost never moves.</li>
    <li>Frequency adverbs go <b>before</b> the main verb, after <em>am/is/are</em>.</li>
    <li><b>gave me a present</b> = <b>gave a present to me</b> — never <s>gave to me a
        present</s>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-73: Question Tags",
        "category": "english",
        "order": 73,
        "summary": (
            "It's useful, isn't it? The little question at the end of a sentence — how to build "
            "it, and why Uzbek's single tag becomes dozens in English."
        ),
        "stories": ["You're Coming, Aren't You?"],
        "content": """
<h2>PE-73: Question Tags</h2>

<p>Uzbek checks agreement with one small word: <em>"Havo sovuq, <b>shundaymi</b>?"</em> or
simply <em>"…-a?"</em> — and it never changes. English builds a fresh little question every
single time: <em>"It's cold, <b>isn't it</b>?"</em>, <em>"You went, <b>didn't you</b>?"</em>,
<em>"She can swim, <b>can't she</b>?"</em> These are <mark>question tags</mark>, and they are
everywhere in spoken English.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The two-part rule: opposite sign, same helper</li>
    <li>What to do when the sentence has no helper verb</li>
    <li>The special cases: <em>I am</em>, <em>Let's</em>, imperatives, <em>there is</em></li>
    <li>How intonation changes the meaning</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Building a tag</span>
  <span class="pe-chip pe-chip--s">positive sentence</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--neg">negative tag</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">negative sentence</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">positive tag</span>
</div>

LEGEND_HERE

<h3>1. The two-part rule</h3>

<p>Every tag does two things: it <b>flips the sign</b> (positive ↔ negative) and it <b>repeats
the helper verb</b> with a pronoun.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <span class="pe-hl pe-hl--aux">are</span> tired,
     <span class="pe-hl pe-hl--aux">aren't</span> you? — She <b>hasn't</b> finished,
     <b>has</b> she?</p>
  <p class="pe-ex__uz">Charchadingiz, shundaymi? — U tugatmadi, shundaymi?</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Positive → negative tag</p>
    <ul>
      <li>He <b>is</b> a doctor, <b>isn't he</b>?</li>
      <li>They <b>have</b> arrived, <b>haven't they</b>?</li>
      <li>You <b>can</b> drive, <b>can't you</b>?</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Negative → positive tag</p>
    <ul>
      <li>He <b>isn't</b> a doctor, <b>is he</b>?</li>
      <li>They <b>haven't</b> arrived, <b>have they</b>?</li>
      <li>You <b>can't</b> drive, <b>can you</b>?</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu asosiy farq: oʻzbekchada <b>bitta</b> shakl hammasiga yetadi —
  "<b>shundaymi?</b>", "<b>-a?</b>", "<b>toʻgʻrimi?</b>" — va u oʻzgarmaydi. Ingliz tilida
  esa har safar <b>yangi</b> savolcha yasaladi va u gapdagi yordamchi feʼlga bogʻliq.
  Shuning uchun hamma joyda <s>isn't it?</s> deb qoʻyish — eng koʻp uchraydigan xato.
</div>

<h3>2. No helper verb? Use do / does / did</h3>

<p>If the sentence has no auxiliary — just an ordinary verb in the Present or Past Simple —
the tag borrows <b>do, does</b> or <b>did</b>, exactly as questions do (PE-10, PE-22).</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <b>like</b> plov, <b>don't you</b>? — She <b>works</b> here,
     <b>doesn't she</b>? — They <b>went</b> home, <b>didn't they</b>?</p>
  <p class="pe-ex__uz">Palovni yoqtirasiz, shundaymi? — U shu yerda ishlaydi-a? — Ular uyga
     ketdi, shundaymi?</p>
</div>

<h3>3. The special cases</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Sentence</th><th>Tag</th><th>Note</th></tr>
  <tr><td>I <b>am</b> late,</td><td><b>aren't I?</b></td><td>not <s>amn't I</s></td></tr>
  <tr><td><b>Let's</b> go,</td><td><b>shall we?</b></td><td>suggestions</td></tr>
  <tr><td><b>Open</b> the window,</td><td><b>will you?</b></td><td>imperatives</td></tr>
  <tr><td><b>Don't</b> be late,</td><td><b>will you?</b></td><td>negative imperative</td></tr>
  <tr><td><b>There is</b> a problem,</td><td><b>isn't there?</b></td><td><em>there</em> acts as the subject</td></tr>
  <tr><td><b>Nobody</b> came,</td><td><b>did they?</b></td><td><em>nobody</em> is already negative</td></tr>
  <tr><td>This <b>is</b> Afsona's,</td><td><b>isn't it?</b></td><td>a thing → <em>it</em></td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Let's</b> take a taxi, <b>shall we</b>? — <b>Nobody</b> phoned,
     <b>did they</b>?</p>
  <p class="pe-ex__uz">Taksi olaylikmi? — Hech kim qoʻngʻiroq qilmadi-a?</p>
  <p class="pe-ex__why">Words like <em>nobody, nothing, never</em> already make the sentence
     negative, so the tag is <b>positive</b>.</p>
</div>

<h3>4. Intonation changes the meaning</h3>

<p>The same tag can do two different jobs, depending on your voice.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Falling voice — I expect you to agree</p>
    <p><em>"Beautiful day, isn't it?" ↘</em></p>
    <p>= I'm not really asking; just making conversation.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Rising voice — a real question</p>
    <p><em>"You've finished, haven't you?" ↗</em></p>
    <p>= I'm genuinely not sure. Please tell me.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ohang muhim: <b>pastga</b> tushsa — bu haqiqiy savol emas, shunchaki suhbat boshlash
  yoki tasdiq kutish ("Havo yaxshi-a?"). <b>Yuqoriga</b> koʻtarilsa — bu <b>rostdan</b>
  savol ("Tugatdingizmi, ha?"). Oʻzbekchadagi "-a?" ohangi ham xuddi shunday ishlaydi.
</div>

<h3>5. Why tags matter so much</h3>

<p>Tags are not decoration — they are how English speakers stay friendly. A bare statement can
sound flat or even rude; a tag invites the other person into the conversation.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Flat</p>
    <ul>
      <li><em>The exam was difficult.</em></li>
      <li><em>You're new here.</em></li>
      <li><em>It's very hot.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Friendly — with a tag</p>
    <ul>
      <li><em>The exam was difficult, <b>wasn't it</b>?</em></li>
      <li><em>You're new here, <b>aren't you</b>?</em></li>
      <li><em>It's very hot, <b>isn't it</b>?</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— Lovely weather, <b>isn't it</b>? — Yes, beautiful. — You're waiting for
     the bus, <b>aren't you</b>? — That's right.</p>
  <p class="pe-ex__uz">— Havo ajoyib-a? — Ha, juda yaxshi. — Avtobus kutyapsizmi? — Ha,
     shunday.</p>
  <p class="pe-ex__why">This is how a conversation with a stranger begins in English.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ingliz tilida savol qoʻshimchasi — <b>muloqot vositasi</b>. Quruq gap ("Havo issiq")
  biroz sovuq eshitiladi; qoʻshimcha esa suhbatdoshni gapga tortadi ("Havo issiq-a?").
  Oʻzbekchadagi "<b>-a?</b>" ham aynan shu vazifani bajaradi. Notanish odam bilan
  suhbat boshlashning eng tabiiy yoʻli.
</div>

<h3>6. Answering a tag question</h3>

<p>Answer the <b>fact</b>, not the tag. This can feel strange after a negative sentence:</p>

<div class="pe-ex">
  <p class="pe-ex__en">— You don't like coffee, do you? — <b>No, I don't.</b> <em>(correct — I
     don't like it)</em> / <b>Yes, I do.</b> <em>(= actually I do like it)</em></p>
  <p class="pe-ex__uz">— Qahvani yoqtirmaysiz-a? — Yoʻq, yoqtirmayman. / Ha, yoqtiraman.</p>
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>You are coming, isn't it?</s></p>
  <p class="pe-good">You are coming, <b>aren't you</b>?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She likes music, doesn't she likes?</s></p>
  <p class="pe-good">She likes music, <b>doesn't she</b>?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You don't know him, don't you?</s></p>
  <p class="pe-good">You don't know him, <b>do you</b>?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'm right, amn't I?</s></p>
  <p class="pe-good">I'm right, <b>aren't I</b>?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Let's go, will we?</s></p>
  <p class="pe-good">Let's go, <b>shall we</b>?</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Add the tag: <em>Afsona speaks Korean, ___ ?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>doesn't she?</strong> No helper in the sentence, so the tag borrows
         <em>does</em>, and the sign flips to negative.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Add the tag: <em>They haven't arrived yet, ___ ?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>have they?</strong> The sentence is negative, so the tag is positive, using
         the same helper <em>have</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Add the tag: <em>Nothing happened, ___ ?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>did it?</strong> <em>Nothing</em> already makes the sentence negative, so the
         tag is positive — and <em>nothing</em> is referred to as <em>it</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Add the tag: <em>Let's watch a film, ___ ?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>shall we?</strong> <em>Let's</em> always takes this tag — it is a
         suggestion, not a statement.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>Your brother can drive, isn't he?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Your brother can drive, can't he?</strong></p>
      <p>The tag must repeat the helper in the sentence — here that is <em>can</em>, not
         <em>is</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Question tag</b><span>soʻroq qoʻshimchasi</span></li>
  <li><b>Auxiliary</b><span>yordamchi feʼl</span></li>
  <li><b>To flip / reverse</b><span>teskari qilmoq</span></li>
  <li><b>Intonation</b><span>ohang</span></li>
  <li><b>To agree</b><span>qoʻshilmoq, tasdiqlamoq</span></li>
  <li><b>Suggestion</b><span>taklif</span></li>
  <li><b>Imperative</b><span>buyruq shakli</span></li>
  <li><b>Small talk</b><span>oddiy suhbat</span></li>
  <li><b>Genuinely</b><span>chin dildan, rostdan</span></li>
  <li><b>To confirm</b><span>tasdiqlamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Positive sentence → <b>negative tag</b>; negative sentence → <b>positive tag</b>.</li>
    <li>Repeat the <b>same helper</b>; if there isn't one, use <b>do / does / did</b>.</li>
    <li>Specials: <b>I am → aren't I</b>, <b>Let's → shall we</b>, imperative → <b>will
        you</b>.</li>
    <li><b>Nobody / nothing / never</b> already make it negative → positive tag.</li>
    <li>Falling voice = expecting agreement · rising voice = a real question.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-74: Subject–Verb Agreement",
        "category": "english",
        "order": 74,
        "summary": (
            "Finding the real subject when a long phrase gets in the way — plus the nouns that "
            "look plural but aren't, and the ones that look singular but are."
        ),
        "stories": ['The News Is Not Good'],
        "content": """
<h2>PE-74: Subject–Verb Agreement</h2>

<p>The basic rule is easy and you learned it in PE-9: singular subject, singular verb. The
difficulty is that English loves to put <b>long phrases</b> between the subject and its verb, and
your ear starts agreeing with the wrong word. <em>"The box of old books <b>is</b> heavy"</em> —
not <em>are</em>, even though <em>books</em> is the last thing you heard.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>How to find the <b>real</b> subject in a long sentence</li>
    <li>What <em>and</em>, <em>with</em> and <em>as well as</em> do to the verb</li>
    <li>Nouns that look plural but take a singular verb — and the reverse</li>
    <li>Money, time and distance amounts</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The method</span>
  <span class="pe-chip pe-chip--s">find the head noun</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--opt">ignore everything between</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">match the verb</span>
</div>

LEGEND_HERE

<h3>1. Ignore what comes between</h3>

<p>Find the <b>head</b> of the subject — the one word the sentence is really about — and match
the verb to that. Cross out everything in between.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">The book</span> on the shelf near the
     windows <span class="pe-hl pe-hl--v">is</span> mine.</p>
  <p class="pe-ex__uz">Derazalar yonidagi tokchadagi kitob mening.</p>
  <p class="pe-ex__why">The head is <em>the book</em> — singular. <em>Shelf</em> and
     <em>windows</em> are just decoration.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>One of my friends is</b> a doctor. — <b>A number of students are</b>
     absent.</p>
  <p class="pe-ex__uz">Doʻstlarimdan biri shifokor. — Bir qancha oʻquvchi yoʻq.</p>
  <p class="pe-ex__why"><em>One of…</em> → singular. But <em>a number of…</em> → plural, because
     the meaning is "several".</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida feʼl egaga qarab kam oʻzgaradi, shuning uchun bu qoida <b>yangi
  odat</b> talab qiladi. Usul oddiy: gapni oʻqib, oʻzingizga "<b>bu gap nima haqida?</b>"
  deb savol bering. Javob bitta soʻz boʻladi — feʼlni <b>oʻsha soʻzga</b> moslashtiring,
  yonidagi soʻzlarga emas.
</div>

<h3>2. and makes plural — but with doesn't</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">and → plural verb</p>
    <ul>
      <li>Jasur <b>and</b> Afsona <b>are</b> here.</li>
      <li>Bread and butter <b>are</b> on the table.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">with / as well as → unchanged</p>
    <ul>
      <li>Jasur, <b>with</b> his friends, <b>is</b> here.</li>
      <li>The teacher, <b>as well as</b> the pupils, <b>was</b> late.</li>
    </ul>
  </div>
</div>

<p>The logic: <em>and</em> genuinely adds a second subject. <em>With</em>, <em>as well as</em>,
<em>together with</em> and <em>including</em> only add extra information, so the verb keeps
agreeing with the original subject.</p>

<h3>3. The tricky nouns</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Look plural, are singular</p>
    <p><em>news, mathematics, physics, politics</em> — <b>The news is</b> good.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Look singular, are plural</p>
    <p><em>people, police, children</em> — <b>The police are</b> here.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Uncountables</p>
    <p><em>information, advice, furniture, money</em> — <b>Advice is</b> useful. (PE-2)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Always plural</p>
    <p><em>trousers, glasses, scissors</em> — <b>My glasses are</b> broken.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>The news was</b> surprising, and <b>the people were</b> shocked.
     <b>Physics is</b> my favourite subject.</p>
  <p class="pe-ex__uz">Yangilik hayratlanarli edi va odamlar hayron boʻlishdi. Fizika mening
     sevimli fanim.</p>
</div>

<h3>4. Amounts of money, time and distance</h3>

<p>When a plural amount is treated as <b>one quantity</b>, the verb is singular.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Ten dollars is</b> not enough. — <b>Two hours is</b> a long time. —
     <b>Five kilometres is</b> quite far.</p>
  <p class="pe-ex__uz">Oʻn dollar yetarli emas. — Ikki soat — uzoq vaqt. — Besh kilometr
     ancha uzoq.</p>
  <p class="pe-ex__why">We are thinking of <em>one</em> amount, not ten separate dollars.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Jamlovchi otlar (<em>team, family, class, government</em>) ikki xil qaralishi mumkin:
  <b>bir butun</b> sifatida — feʼl birlikda (<em>The team <b>is</b> strong</em> — "jamoa
  kuchli"), yoki <b>alohida odamlar</b> sifatida — feʼl koʻplikda (<em>The team <b>are</b>
  arguing</em> — "jamoa aʼzolari bahslashyapti"). Ikkalasi ham toʻgʻri; maʼnoga qarab
  tanlanadi.
</div>

<h3>5. there is / there are, and either/or</h3>

<ol class="pe-steps">
  <li><b>there is / there are</b> agrees with the noun that <b>follows</b> it (PE-7):
      <em>There <b>is</b> a book and two pens.</em></li>
  <li><b>either … or / neither … nor</b> — the verb matches the <b>nearer</b> subject:
      <em>Neither Jasur nor his brothers <b>are</b> here.</em></li>
  <li><b>each / every / everybody</b> → always singular (PE-71).</li>
  <li><b>Collective nouns</b> (<em>team, family, government</em>) can take either, depending on
      whether you mean the unit or the members: <em>The team <b>is</b> strong</em> /
      <em>The team <b>are</b> arguing</em>.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Pul, vaqt va masofa haqidagi qoidani mantiq bilan eslang: "oʻn dollar" — bu
  <b>bitta summa</b>, shuning uchun <em>is</em>. "Ikki soat" — bitta muddat, shuning uchun
  yana <em>is</em>. Oʻzbekchada ham "Oʻn dollar yetarli <b>emas</b>" deymiz — bitta
  butun narsa haqida gapirayotgandek.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>The list of students are on the wall.</s></p>
  <p class="pe-good">The <b>list</b> of students <b>is</b> on the wall.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>One of my friends live in Nukus.</s></p>
  <p class="pe-good"><b>One</b> of my friends <b>lives</b> in Nukus.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The news are very good today.</s></p>
  <p class="pe-good">The news <b>is</b> very good today.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The police is looking for him.</s></p>
  <p class="pe-good">The police <b>are</b> looking for him.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Twenty thousand som are not much.</s></p>
  <p class="pe-good">Twenty thousand som <b>is</b> not much.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>The box of chocolates on the table <span class="pe-blank">?</span> (be) for
     you.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — the head of the subject is <em>the box</em>, not
         <em>chocolates</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>Afsona, together with her sisters, <span class="pe-blank">?</span> (be)
     coming.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — <em>together with</em> adds information but does not add a
         subject. (With <em>and</em> it would be <em>are</em>.)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>Mathematics are difficult for many students.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Mathematics is difficult for many students.</strong></p>
      <p>It ends in <b>-s</b> but names one subject of study.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Choose: <em>Three years <span class="pe-blank">?</span> (be) a long time to wait.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — one period of time, treated as a single quantity.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Choose and explain: <em>Neither the teacher nor the students
     <span class="pe-blank">?</span> (know) the answer.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>know</strong> — with <em>neither … nor</em> the verb agrees with the
         <b>nearer</b> subject, and <em>the students</em> is plural.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Agreement</b><span>moslashuv</span></li>
  <li><b>Head noun</b><span>asosiy ot</span></li>
  <li><b>Phrase</b><span>soʻz birikmasi</span></li>
  <li><b>Collective noun</b><span>jamlovchi ot</span></li>
  <li><b>Amount</b><span>miqdor</span></li>
  <li><b>Distance</b><span>masofa</span></li>
  <li><b>Absent</b><span>yoʻq, kelmagan</span></li>
  <li><b>As well as</b><span>...bilan bir qatorda</span></li>
  <li><b>Shocked</b><span>hayratda qolgan</span></li>
  <li><b>Government</b><span>hukumat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Find the <b>head</b> of the subject and ignore the words in between.</li>
    <li><b>and</b> → plural · <b>with / as well as / together with</b> → verb unchanged.</li>
    <li><b>news, physics, information</b> → singular · <b>people, police, glasses</b> →
        plural.</li>
    <li>Amounts of money, time and distance take a <b>singular</b> verb.</li>
    <li><b>neither … nor</b> → agree with the <b>nearer</b> subject.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-75: Possession: 's, s' and of",
        "category": "english",
        "order": 75,
        "summary": (
            "Where the apostrophe goes, when to use 'of' instead, and the one place you must "
            "never put an apostrophe at all."
        ),
        "stories": ["The Teacher's Desk and the Teachers' Room"],
        "content": """
<h2>PE-75: Possession: 's, s' and of</h2>

<p>Uzbek marks possession with one clean suffix: <em>Ali<b>ning</b> kitobi</em>. English gives
you two competing tools — <b>'s</b> and <b>of</b> — plus an apostrophe that moves depending on
whether the owner is singular or plural. And it hides one trap that even native speakers fall
into daily.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Where the apostrophe goes: <b>'s</b> or <b>s'</b></li>
    <li>When to use <b>of</b> instead</li>
    <li>The shop and home shortcut: <em>at the doctor's</em></li>
    <li>The trap: <b>never</b> use an apostrophe to make a plural</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two tools</span>
  <span class="pe-chip pe-chip--s">people &amp; animals</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">'s</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">things</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">of</span>
</div>

LEGEND_HERE

<h3>1. Where the apostrophe goes</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Owner</th><th>Form</th><th>Example</th></tr>
  <tr><td>singular</td><td><b>'s</b></td><td>the boy<b>'s</b> book (one boy)</td></tr>
  <tr><td>plural ending in -s</td><td><b>s'</b></td><td>the boy<b>s'</b> books (several boys)</td></tr>
  <tr><td>irregular plural</td><td><b>'s</b></td><td>the children<b>'s</b> toys</td></tr>
  <tr><td>name ending in -s</td><td><b>'s</b> or <b>'</b></td><td>James<b>'s</b> car / James<b>'</b> car</td></tr>
  <tr><td>two owners together</td><td>last one only</td><td>Jasur and Afsona<b>'s</b> house</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">My <b>sister's</b> room is small, but my <b>sisters'</b> rooms are both
     big.</p>
  <p class="pe-ex__uz">Opamning xonasi kichkina, lekin opalarimning xonalari ikkalasi ham
     katta.</p>
  <p class="pe-ex__why">One sister vs several sisters — the apostrophe's position is the only
     clue.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada <b>-ning</b> egasiga qoʻshiladi va sonidan qatʼi nazar oʻzgarmaydi:
  <em>opamning</em>, <em>opalarimning</em>. Ingliz tilida esa <b>apostrofning oʻrni</b>
  sonni koʻrsatadi: <em>sister<b>'s</b></em> (bitta), <em>sisters<b>'</b></em> (bir necha).
  Yozganda bu farqni eʼtiborsiz qoldirmang — maʼno oʻzgaradi.
</div>

<h3>2. 's or of?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Use 's for…</p>
    <ul>
      <li>people: <em>my father's car</em></li>
      <li>animals: <em>the dog's tail</em></li>
      <li>time: <em>today's lesson, a week's holiday</em></li>
      <li>places &amp; groups: <em>Uzbekistan's history</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Use of for…</p>
    <ul>
      <li>things: <em>the door of the car</em></li>
      <li>parts: <em>the end of the film</em></li>
      <li>long phrases: <em>the name of the girl I met</em></li>
      <li>abstract: <em>the beginning of the year</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Afsona's</b> notebook was on the table at the <b>end of</b> the
     lesson.</p>
  <p class="pe-ex__uz">Dars oxirida Afsonaning daftari stolda edi.</p>
</div>

<p>With things, English often prefers a <b>compound noun</b> — two nouns side by side — over
<em>of</em>: <em>the car door</em>, <em>the kitchen window</em>, <em>a school bag</em>. Remember
from PE-15 that the first noun stays singular.</p>

<h3>3. The shop and home shortcut</h3>

<p>A lovely English habit: <b>'s</b> alone can mean somebody's shop, office or home. The noun
disappears because everybody knows it.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I'm going to the <b>doctor's</b>. — We had dinner at my
     <b>aunt's</b>. — She works at the <b>baker's</b>.</p>
  <p class="pe-ex__uz">Shifokorga boryapman. — Xolamnikida ovqatlandik. — U nonvoyxonada
     ishlaydi.</p>
  <p class="pe-ex__why"><em>the doctor's</em> = the doctor's surgery; <em>my aunt's</em> = my
     aunt's house.</p>
</div>

<h3>4. The double possessive: a friend of mine</h3>

<p>English has one more pattern that looks strange but is completely normal — possession marked
<b>twice</b>, once with <em>of</em> and once with <em>'s</em> or a possessive pronoun.</p>

<div class="pe-ex">
  <p class="pe-ex__en">She's <b>a friend of mine</b>. — He's <b>a cousin of Afsona's</b>. —
     That old car of <b>my father's</b> still works.</p>
  <p class="pe-ex__uz">U mening doʻstim. — U Afsonaning amakivachchasi. — Otamning oʻsha eski
     mashinasi hamon yuradi.</p>
  <p class="pe-ex__why">Use it when you mean "one of several": <em>a friend of mine</em> = one of
     my friends.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>She's a friend of me.</s></p>
  <p class="pe-good">She's a friend <b>of mine</b>. / She's <b>my friend</b>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>a friend of mine</b> — bu "doʻstlarimdan biri" degani, yaʼni bir nechta doʻstim bor
  va bu ulardan biri. Shuning uchun <em>of</em> dan keyin <b>me</b> emas, <b>mine</b>
  qoʻyiladi: <em>of mine, of yours, of his, of ours</em>. Odam ismi bilan esa apostrof
  qoʻshiladi: <em>a cousin of <b>Afsona's</b></em>.
</div>

<h3>5. The trap: never an apostrophe for plurals</h3>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  An apostrophe shows <b>possession</b> or a <b>missing letter</b> — never a plural.
  <s>I bought two book's</s> ✗ → <b>two books</b> ✓. This mistake is so common on shop signs
  in England that it has a nickname: the greengrocer's apostrophe.
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>The teacher's are in the staff room.</s></p>
  <p class="pe-good">The <b>teachers</b> are in the staff room.</p>
</div>

<p>And the pair you met back in PE-5, which follows the same logic:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>its</b> = belonging to it <em>(the dog wagged its tail)</em> ·
     <b>it's</b> = it is / it has <em>(it's raining)</em></p>
  <p class="pe-ex__uz">its — uning (narsa) · it's — bu ... dir</p>
  <p class="pe-ex__why">Possessive pronouns never take an apostrophe: <em>its, yours, hers,
     ours, theirs</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Apostrof <b>faqat ikkita</b> vazifada ishlatiladi: (1) egalik — <em>Ali<b>'s</b></em>,
  (2) tushib qolgan harf — <em>it<b>'s</b></em> = it is, <em>don<b>'</b>t</em> = do not.
  <b>Koʻplik uchun hech qachon</b> qoʻyilmaydi: <em>kitoblar</em> → <em>books</em>,
  <s>book's</s> emas. Shu bitta qoida yozma ishlarda koʻp xatoni oldini oladi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>This is my brothers car.</s> <em>(one brother)</em></p>
  <p class="pe-good">This is my <b>brother's</b> car.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The childrens' toys are everywhere.</s></p>
  <p class="pe-good">The <b>children's</b> toys are everywhere.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The leg of the table's is broken.</s></p>
  <p class="pe-good">The <b>table leg</b> is broken. / The <b>leg of the table</b> is broken.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The dog wagged it's tail.</s></p>
  <p class="pe-good">The dog wagged <b>its</b> tail.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We stayed at my grandmother house.</s></p>
  <p class="pe-good">We stayed at my <b>grandmother's</b> house.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Add the apostrophe: <em>the students books</em> (many students)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>the students' books.</strong> A plural already ending in <b>-s</b> takes the
         apostrophe <b>after</b> the s.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     's or of: <em>the roof ___ the house · my ___ friend bike</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>the roof of the house</strong> (a thing) · <strong>my friend's bike</strong>
         (a person).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What does this mean? <em>I'm going to the dentist's.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>To the dentist's surgery / clinic.</strong> The noun is left out because
         everyone knows what it is.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>We sell fresh apple's and orange's.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>We sell fresh apples and oranges.</strong></p>
      <p>Plurals never take an apostrophe.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What is the difference? <em>(a) my sister's friends (b) my sisters' friends</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I have one sister.</strong> <strong>(b) I have two or more
         sisters.</strong> One apostrophe, a whole family difference.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Possession</b><span>egalik</span></li>
  <li><b>Apostrophe</b><span>apostrof (')</span></li>
  <li><b>Owner</b><span>ega, egasi</span></li>
  <li><b>Compound noun</b><span>qoʻshma ot</span></li>
  <li><b>Roof</b><span>tom</span></li>
  <li><b>Tail</b><span>dum</span></li>
  <li><b>To wag</b><span>likillatmoq</span></li>
  <li><b>Staff room</b><span>oʻqituvchilar xonasi</span></li>
  <li><b>Surgery (doctor's)</b><span>qabulxona</span></li>
  <li><b>Baker's</b><span>nonvoyxona</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Singular owner → <b>'s</b> · plural owner ending in s → <b>s'</b> · children →
        <b>children's</b>.</li>
    <li><b>'s</b> for people, animals, time and places · <b>of</b> for things and parts.</li>
    <li><b>the doctor's</b>, <b>my aunt's</b> = their place — the noun is left out.</li>
    <li><b>Never</b> an apostrophe for a plural: <em>two books</em>, not <s>two book's</s>.</li>
    <li>Possessive pronouns take no apostrophe: <b>its, yours, hers, theirs</b>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
