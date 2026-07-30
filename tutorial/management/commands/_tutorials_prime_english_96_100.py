# -*- coding: utf-8 -*-
"""Prime English — Block H, lessons 96–100. THE FINAL BATCH.

PE-100 is the course capstone: a one-page review of the entire 100 lessons.

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_96_100.py --author=prime
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
        "title": "PE-96: Describing People, Places and Things",
        "category": "english",
        "order": 96,
        "summary": (
            "The most common speaking task there is — how to describe someone's appearance and "
            "character, a place you love, and an object, using the grammar you already have."
        ),
        "content": """
<h2>PE-96: Describing People, Places and Things</h2>

<p>Ask any examiner what candidates are asked to do most often and the answer is the same:
<em>"Describe a person you admire."</em> <em>"Describe your home town."</em> <em>"Describe
something important to you."</em> Nothing new is needed here — you already have the grammar. This
lesson shows you how to <mark>assemble</mark> it into a fluent description.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>be</b> and <b>have got</b> for appearance</li>
    <li>The difference between <b>look like</b> and <b>be like</b></li>
    <li>How to describe a place with <b>there is/are</b> and prepositions</li>
    <li>Structures that make a description sound thought-out</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two tools for people</span>
  <span class="pe-chip pe-chip--s">be</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">adjective</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">have got</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">noun</span>
</div>

LEGEND_HERE

<h3>1. Appearance: be or have got?</h3>

<p>The rule is mechanical. <b>Be</b> takes an adjective; <b>have got</b> takes a noun.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">be + adjective</p>
    <ul>
      <li>She <b>is</b> tall / short / slim.</li>
      <li>He <b>is</b> in his twenties.</li>
      <li>They <b>are</b> good-looking.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">have got + noun</p>
    <ul>
      <li>She <b>has got</b> long dark hair.</li>
      <li>He <b>has got</b> brown eyes.</li>
      <li>She <b>has got</b> a friendly face.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--v">is</span> quite tall and she
     <span class="pe-hl pe-hl--v">has got</span> long dark hair and a very warm smile.</p>
  <p class="pe-ex__uz">Afsona ancha baland boʻyli, uzun qora sochli va juda iliq tabassumli.</p>
  <p class="pe-ex__why">Adjective after <em>is</em>, nouns after <em>has got</em> — never
     <s>she is long hair</s>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "u uzun sochli" — bitta tuzilma bilan aytiladi. Ingliz tilida esa
  <b>ikkiga boʻlinadi</b>: sifat boʻlsa <b>is</b> (<em>she <b>is</b> tall</em>), ot boʻlsa
  <b>has got</b> (<em>she <b>has got</b> long hair</em>). Shuning uchun gapni tuzishdan
  oldin oʻzingizga savol bering: bu <b>sifat</b>mi yoki <b>ot</b>mi?
</div>

<h3>2. look like vs be like</h3>

<p>Two questions that sound similar and mean completely different things:</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Question</th><th>Asks about</th><th>Answer</th></tr>
  <tr><td>What does she <b>look like</b>?</td><td>appearance</td><td>She's tall with dark hair.</td></tr>
  <tr><td>What <b>is</b> she <b>like</b>?</td><td>character</td><td>She's kind and very funny.</td></tr>
  <tr><td>What does she <b>like</b>?</td><td>preferences</td><td>She likes reading and music.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">My brother <b>looks like</b> my father, but he <b>is like</b> my mother —
     calm and patient.</p>
  <p class="pe-ex__uz">Akam otamga oʻxshaydi, lekin xarakteri onamga tortgan — bosiq va sabrli.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  These three are a classic exam trap. <b>look like</b> = face and body · <b>be like</b> =
  personality · <b>like</b> = what they enjoy. Missing one small word changes the whole
  question.
</div>

<h3>3. Personality — and how to make it interesting</h3>

<p>A list of adjectives is dull. Add a reason or an example and the description comes alive.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Weak: <em>He is kind and helpful.</em><br>
     Better: <em>He<b>'s the kind of person who</b> always notices when you're upset. Last week,
     for example, he stayed late to help me with my homework.</em></p>
  <p class="pe-ex__uz">U mehribon va yordamchi. — U shunday odam: sen xafa boʻlsang, darrov
     sezadi. Masalan, oʻtgan hafta uy vazifamga yordam berish uchun kech qolib ketdi.</p>
  <p class="pe-ex__why">Useful openers: <em>He's the kind of person who…</em>,
     <em>What I like about her is…</em> (PE-85), <em>She's one of the most … people I know</em>
     (PE-67).</p>
</div>

<h3>4. Describing a place</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>What's there</p>
    <p><b>There is / There are</b> … (PE-7)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Where exactly</p>
    <p><b>in, on, at, next to, opposite</b> (PE-16)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>What it's like</p>
    <p><b>It's</b> quiet / crowded / famous for…</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Feelings</p>
    <p><b>It's the sort of place where</b> you can relax.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">My village is <b>in</b> the mountains, about fifty kilometres <b>from</b>
     the city. <b>There's</b> a small river <b>next to</b> our house, and <b>there are</b>
     apricot trees everywhere. <b>It's the sort of place where</b> nothing ever hurries.</p>
  <p class="pe-ex__uz">Qishlogʻim togʻlarda, shahardan ellik chaqirim uzoqda. Uyimiz yonida
     kichik daryo bor va hamma yerda oʻrik daraxtlari. Bu — hech narsa shoshmaydigan joy.</p>
</div>

<h3>5. Describing a thing</h3>

<p>Use the adjective order from PE-15 — <b>opinion → size → age → colour → origin → material</b> —
and finish with what it means to you.</p>

<div class="pe-ex">
  <p class="pe-ex__en">It's a <b>beautiful old wooden</b> box that my grandfather made. It's
     <b>about</b> twenty centimetres long, and it's <b>the most precious thing</b> I own.</p>
  <p class="pe-ex__uz">Bu — bobom yasagan chiroyli, eski, yogʻoch quti. Uzunligi taxminan yigirma
     santimetr va bu men uchun eng qadrli narsa.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Imtihonda tavsiflashning oltin qoidasi: <b>faktdan keyin sabab yoki hikoya</b> qoʻshing.
  "Bu quti chiroyli" — bir jumla. "Bu qutini bobom yasagan va u men uchun eng qadrli
  narsa" — bu allaqachon <b>javob</b>. Har bir faktga "nega?" yoki "masalan?" qoʻshsangiz,
  javobingiz ikki barobar uzun va qiziqarli boʻladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Joyni tavsiflashda uchta qurilma yetarli: <b>There is / There are</b> (nima bor),
  <b>predloglar</b> (qayerda), <b>It's…</b> (qanday). Shu uchtasini birlashtirsangiz, har
  qanday joy haqida bir necha jumla ayta olasiz — imtihonda ham, suhbatda ham.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>She is long hair.</s></p>
  <p class="pe-good">She <b>has got</b> long hair. / She <b>is</b> tall.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>What does she like? — She is tall and slim.</s></p>
  <p class="pe-good"><b>What does she look like?</b> — She is tall and slim.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He is looking like his father.</s></p>
  <p class="pe-good">He <b>looks like</b> his father. <em>(stative — PE-13)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>In my village is a river.</s></p>
  <p class="pe-good"><b>There is</b> a river in my village.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It's a box wooden old beautiful.</s></p>
  <p class="pe-good">It's a <b>beautiful old wooden</b> box.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     be or have got: <em>She ___ green eyes and she ___ quite short.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>has got green eyes … is quite short.</strong> Noun → <em>has got</em>;
         adjective → <em>is</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Which question? <em>— …? — He's very generous and patient.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>What is he like?</strong> The answer describes character, not appearance.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Improve it: <em>My city is big. It is nice. There are many people.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>My city is big and lively. There are wide streets full of
         cafés, and it's the sort of place where you always meet somebody you know.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Order the adjectives: <em>silk / a / beautiful / Uzbek / scarf</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a beautiful Uzbek silk scarf</strong> — opinion, origin, material (PE-15).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Describe a person you admire in three sentences.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>My grandmother is small and she has got very kind eyes.
         She's the kind of person who never complains, even when she's tired. What I admire
         most about her is her patience.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Appearance</b><span>tashqi koʻrinish</span></li>
  <li><b>Personality</b><span>xarakter</span></li>
  <li><b>To look like</b><span>oʻxshamoq (tashqi)</span></li>
  <li><b>To be like</b><span>qanday odam boʻlmoq</span></li>
  <li><b>Slim</b><span>nozik, ozgʻin</span></li>
  <li><b>Generous</b><span>saxiy</span></li>
  <li><b>Patient</b><span>sabrli</span></li>
  <li><b>Crowded</b><span>gavjum</span></li>
  <li><b>Precious</b><span>qadrli</span></li>
  <li><b>To admire</b><span>hayratlanmoq, qadrlamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>be</b> + adjective · <b>have got</b> + noun.</li>
    <li><b>look like</b> = appearance · <b>be like</b> = character · <b>like</b> =
        preferences.</li>
    <li>Places: <b>there is/are</b> + prepositions + <em>It's the sort of place where…</em></li>
    <li>Things: adjective order from PE-15, then why it matters to you.</li>
    <li>Always add a <b>reason or an example</b> — that is what turns a list into a
        description.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-97: Describing Charts, Trends and Numbers",
        "category": "english",
        "order": 97,
        "summary": (
            "The language of data — rise, fall, peak, remain stable — plus the prepositions that "
            "decide whether something increased BY or TO a number."
        ),
        "content": """
<h2>PE-97: Describing Charts, Trends and Numbers</h2>

<p>Every serious English exam contains a chart, and every serious subject — economics, geography,
biology — needs you to describe numbers. The good news is that this is one of the most
<mark>learnable</mark> topics in the language: a fixed set of verbs, a fixed set of adverbs, and
three prepositions that do all the work.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The verbs of change: <b>rise, fall, peak, remain stable</b></li>
    <li>The adverbs of degree: <b>sharply, slightly, gradually</b></li>
    <li>The three prepositions: <b>from … to, by, of</b></li>
    <li>How to structure a description: overview first, detail second</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The core sentence</span>
  <span class="pe-chip pe-chip--s">Sales</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">rose</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">sharply</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">from 20 to 50</span>
</div>

LEGEND_HERE

<h3>1. The verbs</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Direction</th><th>Verbs</th><th>Noun form</th></tr>
  <tr><td><b>up</b></td><td>increase, rise, grow, go up, climb</td><td>an increase, a rise, growth</td></tr>
  <tr><td><b>down</b></td><td>decrease, fall, drop, decline, go down</td><td>a decrease, a fall, a drop, a decline</td></tr>
  <tr><td><b>no change</b></td><td>remain stable, stay the same, level off</td><td>—</td></tr>
  <tr><td><b>up and down</b></td><td>fluctuate</td><td>a fluctuation</td></tr>
  <tr><td><b>highest point</b></td><td>peak, reach a peak</td><td>a peak</td></tr>
  <tr><td><b>lowest point</b></td><td>hit a low, bottom out</td><td>a low</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The number of tourists <span class="pe-hl pe-hl--v">rose</span> steadily
     until 2019, when it <span class="pe-hl pe-hl--v">peaked</span> at four million. It then
     <span class="pe-hl pe-hl--v">fell</span> sharply.</p>
  <p class="pe-ex__uz">Turistlar soni 2019-yilgacha barqaror oshdi va toʻrt million bilan eng
     yuqori choʻqqiga chiqdi. Keyin keskin tushdi.</p>
  <p class="pe-ex__why">Note <b>peak at</b> a number — that preposition is fixed.</p>
</div>

<h3>2. The adverbs — how much and how fast</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">A lot</p>
    <ul>
      <li>sharply · dramatically</li>
      <li>significantly · considerably</li>
      <li>rapidly · steeply</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">A little / slowly</p>
    <ul>
      <li>slightly · marginally</li>
      <li>gradually · steadily</li>
      <li>slowly</li>
    </ul>
  </div>
</div>

<p>You can also use the <b>adjective + noun</b> version, which is very common in writing:</p>

<div class="pe-ex">
  <p class="pe-ex__en">Prices rose <b>sharply</b>. = There was <b>a sharp rise</b> in prices.<br>
     Sales fell <b>slightly</b>. = There was <b>a slight fall</b> in sales.</p>
  <p class="pe-ex__uz">Narxlar keskin oshdi. = Narxlarda keskin oʻsish boʻldi.</p>
  <p class="pe-ex__why">Alternating between the two versions makes your writing less
     repetitive.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkita variantni bilib qoʻyish juda foydali: <b>feʼl + ravish</b> (<em>rose
  sharply</em>) va <b>sifat + ot</b> (<em>a sharp rise</em>). Inshoda ikkalasini
  navbatlashtirsangiz, matn takrorlanmaydi va ancha puxta koʻrinadi. Oʻzbekchada ham
  "keskin oshdi" va "keskin oʻsish" deb ikki xil aytish mumkin.
</div>

<h3>3. The three prepositions</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  <b>from … to</b> = the two end points · <b>by</b> = the size of the change ·
  <b>of</b> = after a noun. <em>Sales rose <b>from</b> 20 <b>to</b> 50 — an increase
  <b>of</b> 30. They rose <b>by</b> 30.</em>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Production increased <b>from</b> 10,000 <b>to</b> 15,000 tonnes —
     an increase <b>of</b> 50%. It grew <b>by</b> 5,000 tonnes.</p>
  <p class="pe-ex__uz">Ishlab chiqarish 10 000 dan 15 000 tonnaga oshdi — 50 foizga oʻsish.
     U 5 000 tonnaga koʻpaydi.</p>
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>Sales increased of 20%.</s> · <s>It rose from 20 until 50.</s></p>
  <p class="pe-good">Sales increased <b>by</b> 20%. · It rose <b>from</b> 20 <b>to</b> 50.</p>
</div>

<h3>4. Time and approximation</h3>

<ul>
  <li><b>in</b> 2020 · <b>between</b> 2010 <b>and</b> 2020 · <b>from</b> 2010 <b>to</b> 2020 ·
      <b>over</b> the last decade</li>
  <li><b>about, around, roughly, approximately</b> · <b>just over / just under</b> ·
      <b>nearly, almost</b></li>
  <li><b>a quarter, a third, half, two thirds</b> · <b>twice as many as</b></li>
</ul>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Between</b> 2015 <b>and</b> 2020, the figure remained
     <b>at around</b> 30% — <b>just under</b> a third of the total.</p>
  <p class="pe-ex__uz">2015 va 2020 yillar orasida koʻrsatkich 30 foiz atrofida qoldi — bu
     umumiy miqdorning uchdan biridan bir oz kamrogʻi.</p>
</div>

<h3>5. How to structure it</h3>

<ol class="pe-steps">
  <li><b>Say what the chart shows</b> (one sentence, your own words):
      <em>The graph shows the number of visitors to three museums between 2010 and 2020.</em></li>
  <li><b>Give the overview</b> — the biggest pattern, no numbers yet:
      <em>Overall, visitor numbers increased at all three museums.</em></li>
  <li><b>Give the details</b> with numbers, comparing where useful.</li>
  <li><b>Do not give your opinion</b> — a chart description reports, it does not argue.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Muhim: grafik tavsifida <b>oʻz fikringizni bildirmang</b>. "Menimcha, bu yaxshi
  tendensiya" degan jumla ball qoʻshmaydi — bu vazifa <b>faktlarni bayon qilish</b>.
  Tuzilma: nima koʻrsatilgan → umumiy manzara → raqamlar bilan tafsilot. Xulosa
  yozmaysiz.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>number</b> va <b>amount</b> ni adashtirmang (PE-2): sanaladigan narsalar uchun
  <em>the <b>number</b> of students</em>, sanalmaydiganlar uchun <em>the <b>amount</b> of
  water</em>. Grafik tavsifida bu juda tez-tez kerak boʻladi, chunki deyarli har bir
  jumla "...ning soni" yoki "...ning miqdori" bilan boshlanadi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>The number of students was increased.</s></p>
  <p class="pe-good">The number of students <b>increased</b>. <em>(not passive)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Prices raised sharply.</s></p>
  <p class="pe-good">Prices <b>rose</b> sharply. <em>(rise = go up by itself; raise = lift
     something)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>There was a sharply increase.</s></p>
  <p class="pe-good">There was a <b>sharp</b> increase. <em>(adjective before a noun)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It increased with 20%.</s></p>
  <p class="pe-good">It increased <b>by</b> 20%.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The amount of tourists grew.</s></p>
  <p class="pe-good">The <b>number</b> of tourists grew. <em>(countable → number)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Fill in: <em>Sales rose <span class="pe-blank">?</span> 100 <span class="pe-blank">?</span>
     150, an increase <span class="pe-blank">?</span> 50%.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>from 100 to 150, an increase of 50%.</strong> And you could also say
         <em>rose <b>by</b> 50</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Rewrite with a noun: <em>Prices fell slightly in June.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>There was a slight fall in prices in June.</strong></p>
      <p>Adverb → adjective, verb → noun, and <em>in</em> before the thing that changed.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     rise or raise: <em>The government ___ taxes, so prices ___ .</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>raised taxes … prices rose.</strong> <em>Raise</em> needs an object;
         <em>rise</em> happens by itself.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Write the overview: <em>All three cities grew, but Tashkent grew fastest.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Overall, the population increased in all three cities,
         with the sharpest growth in Tashkent.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     number or amount: <em>the ___ of students · the ___ of water</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>the number of students</strong> (countable) · <strong>the amount of
         water</strong> (uncountable) — PE-2 again.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>To increase / rise</b><span>oshmoq</span></li>
  <li><b>To decrease / fall</b><span>kamaymoq</span></li>
  <li><b>To peak</b><span>eng yuqori choʻqqiga chiqmoq</span></li>
  <li><b>To remain stable</b><span>barqaror qolmoq</span></li>
  <li><b>To fluctuate</b><span>oʻzgarib turmoq</span></li>
  <li><b>Sharply</b><span>keskin</span></li>
  <li><b>Gradually</b><span>asta-sekin</span></li>
  <li><b>Slightly</b><span>bir oz</span></li>
  <li><b>Overview</b><span>umumiy manzara</span></li>
  <li><b>Figure</b><span>koʻrsatkich, raqam</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Verbs: <b>rise / fall / peak / remain stable / fluctuate</b>.</li>
    <li>Two versions: <b>rose sharply</b> = <b>a sharp rise</b>. Alternate them.</li>
    <li><b>from … to</b> = end points · <b>by</b> = size of change · <b>of</b> = after a
        noun.</li>
    <li><b>rise</b> happens by itself; <b>raise</b> needs an object.</li>
    <li>Structure: what it shows → overview → details. <b>No opinions.</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-98: Making Excuses, Apologising and Explaining",
        "category": "english",
        "order": 98,
        "summary": (
            "Sorry for being late — the grammar of apologies, the tenses that make an excuse "
            "believable, and how to accept an apology graciously."
        ),
        "content": """
<h2>PE-98: Making Excuses, Apologising and Explaining</h2>

<p>You will need this lesson more often than you would like. Being late, forgetting something,
missing a deadline — every language has a script for it, and English has a very specific one. The
grammar matters: <em>"Sorry <b>for being</b> late"</em> and <em>"Sorry <b>to hear</b> that"</em>
use different structures, and mixing them up is one of the commonest errors at this level.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The three <b>sorry</b> structures: <em>for + -ing</em>, <em>about + noun</em>,
        <em>to + verb</em></li>
    <li>Apologies from casual to formal</li>
    <li>The tenses that make an excuse sound real</li>
    <li>How to accept an apology, and how to promise better</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three structures</span>
  <span class="pe-chip pe-chip--v">sorry for + -ing</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">sorry about + noun</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">sorry to + verb</span>
</div>

LEGEND_HERE

<h3>1. The three sorry structures</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Structure</th><th>Used for</th><th>Example</th></tr>
  <tr>
    <td><b>sorry for + -ing</b></td><td>something you did</td>
    <td>Sorry <b>for being</b> late.</td>
  </tr>
  <tr>
    <td><b>sorry about + noun</b></td><td>a thing or situation</td>
    <td>Sorry <b>about the noise</b>.</td>
  </tr>
  <tr>
    <td><b>sorry to + verb</b></td><td>reacting to news, or interrupting</td>
    <td>Sorry <b>to hear</b> that. · Sorry <b>to bother</b> you.</td>
  </tr>
  <tr>
    <td><b>sorry (that) + clause</b></td><td>a full explanation</td>
    <td>I'm sorry <b>I forgot</b> your birthday.</td>
  </tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I'm sorry <b>for being</b> late and sorry <b>about the mess</b> — and I'm
     sorry <b>to bother</b> you again.</p>
  <p class="pe-ex__uz">Kechikkanim uchun kechirasiz, tartibsizlik uchun ham uzr — va yana
     bezovta qilganim uchun kechirasiz.</p>
  <p class="pe-ex__why">Never <s>sorry for be late</s> or <s>sorry to being late</s> — the
     structures do not mix.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada bitta shakl hammasiga yetadi: "kechikkanim <b>uchun</b> kechirasiz",
  "shovqin <b>uchun</b> kechirasiz". Ingliz tilida esa <b>keyingi soʻzga</b> qarab
  tanlanadi: feʼl boʻlsa — <b>for + -ing</b>, ot boʻlsa — <b>about</b>, xabarga javob
  boʻlsa — <b>to + feʼl</b>. Uchtasini juftlik bilan yodlab qoʻyish kifoya.
</div>

<h3>2. From casual to formal</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Spoken, everyday</p>
    <ul>
      <li>Sorry! · Sorry about that.</li>
      <li>I'm really sorry.</li>
      <li>I'm so sorry — it was my fault.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Written, formal</p>
    <ul>
      <li>I apologise for the delay.</li>
      <li>I do apologise. <em>(emphatic — PE-83)</em></li>
      <li>Please accept my apologies for any inconvenience caused.</li>
    </ul>
  </div>
</div>

<h3>3. The grammar of a believable excuse</h3>

<p>Here is where the past tenses earn their keep. A good excuse usually needs the <b>Past
Continuous</b> (what you were in the middle of) or the <b>Past Perfect</b> (what had already gone
wrong).</p>

<div class="pe-ex">
  <p class="pe-ex__en">I'm sorry I'm late. I <b>was waiting</b> for the bus for half an hour,
     and when it finally came it <b>had already</b> broken down once.</p>
  <p class="pe-ex__uz">Kechikkanim uchun kechirasiz. Yarim soat avtobus kutdim va u nihoyat
     kelganda, allaqachon bir marta buzilgan edi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I couldn't finish the homework <b>because</b> the electricity
     <b>went off</b>. — The lesson was cancelled <b>due to</b> the weather.</p>
  <p class="pe-ex__uz">Uy vazifasini tugatolmadim, chunki chiroq oʻchdi. — Dars ob-havo tufayli
     bekor qilindi.</p>
  <p class="pe-ex__why"><b>because</b> + clause · <b>due to / owing to</b> + noun (PE-52,
     PE-88).</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  In English, a good apology has three parts: <b>apologise → explain briefly → offer to
  fix it</b>. A long explanation with no apology sounds like an excuse; an apology with no
  explanation sounds careless.
</div>

<h3>4. Promising to do better</h3>

<div class="pe-ex">
  <p class="pe-ex__en">It <b>won't happen</b> again. — I<b>'ll make sure</b> I'm on time
     tomorrow. — <b>Let me</b> fix it. — <b>I should have</b> told you earlier.</p>
  <p class="pe-ex__uz">Bu qaytarilmaydi. — Ertaga oʻz vaqtida kelishimga ishonch hosil
     qilaman. — Tuzatib beraman. — Sizga oldinroq aytishim kerak edi.</p>
  <p class="pe-ex__why">Notice <em>should have</em> (PE-48) doing the work of admitting a
     mistake.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Sababni ikki xil aytish mumkin: <b>because</b> dan keyin <b>toʻliq gap</b>
  (<em>because the bus <b>was</b> late</em>), <b>because of / due to</b> dan keyin esa
  faqat <b>ot</b> (<em>because of the <b>traffic</b></em>). Rasmiy xatda <b>due to</b> yoki
  <b>owing to</b> chiroyliroq eshitiladi (PE-88).
</div>

<h3>5. Accepting an apology</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Warm</p>
    <p><em>That's all right. · Don't worry about it.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Casual</p>
    <p><em>No problem. · It's fine. · Never mind.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Formal</p>
    <p><em>That's quite all right. · Thank you for letting me know.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Reassuring</p>
    <p><em>It happens to everybody. · These things happen.</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kechirim qabul qilish ham muhim: ingliz tilida jim turish <b>xafa boʻlgandek</b>
  tuyuladi. Shuning uchun qisqa javob bering: <em>That's all right</em> ("hechqisi yoʻq"),
  <em>Don't worry</em> ("xavotir olmang"), <em>These things happen</em> ("boʻlib turadi").
  Oʻzbekchadagi "zarari yoʻq" ohangi bilan bir xil.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Sorry for be late.</s></p>
  <p class="pe-good">Sorry <b>for being</b> late.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Sorry for hear about your problem.</s></p>
  <p class="pe-good">Sorry <b>to hear</b> about your problem.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I apologise about the delay.</s></p>
  <p class="pe-good">I apologise <b>for</b> the delay.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It was because of the traffic was bad.</s></p>
  <p class="pe-good">It was <b>because</b> the traffic was bad. / <b>because of</b> the heavy
     traffic.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Excuse me for the mistake I did.</s></p>
  <p class="pe-good">I'm sorry <b>for the mistake I made</b>. <em>(PE-90)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     for, about or to: <em>Sorry ___ forgetting your book. Sorry ___ the noise. Sorry ___
     interrupt you.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>for forgetting · about the noise · to interrupt.</strong></p>
      <p>Verb → <em>for + -ing</em>; noun → <em>about</em>; interrupting → <em>to +
         verb</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make a full apology: <em>You missed your friend's birthday party.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I'm so sorry for missing your party. My little sister was
         ill and I had to stay at home. Let me take you out at the weekend to make up for
         it.</em></p>
      <p>Apologise → explain → offer to fix.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make it formal: <em>Sorry I'm late with the report.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I apologise for the delay in submitting the report.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Accept this apology: <em>"I'm really sorry — I forgot to bring your book."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>That's all right, don't worry about it.</strong> Saying nothing would seem
         cold in English.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which tense makes this excuse work? <em>I couldn't call you — my phone ___ (die).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>had died</strong> (or <em>died</em>) — the Past Perfect shows it happened
         <b>before</b> the moment you couldn't call.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>To apologise</b><span>kechirim soʻramoq</span></li>
  <li><b>Apology</b><span>uzr, kechirim</span></li>
  <li><b>Excuse</b><span>bahona</span></li>
  <li><b>Fault</b><span>ayb</span></li>
  <li><b>Delay</b><span>kechikish</span></li>
  <li><b>Inconvenience</b><span>noqulaylik</span></li>
  <li><b>To interrupt</b><span>gapini boʻlmoq</span></li>
  <li><b>To bother</b><span>bezovta qilmoq</span></li>
  <li><b>To make up for</b><span>oʻrnini qoplamoq</span></li>
  <li><b>Never mind</b><span>hechqisi yoʻq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>sorry for + -ing</b> (what you did) · <b>sorry about + noun</b> · <b>sorry to +
        verb</b> (reacting).</li>
    <li>Formal: <b>I apologise for…</b> · <b>Please accept my apologies.</b></li>
    <li>A good apology has three parts: <b>apologise → explain → offer to fix</b>.</li>
    <li>Excuses use the <b>Past Continuous</b> and <b>Past Perfect</b>.</li>
    <li>Always <b>accept</b> an apology out loud — silence seems cold in English.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-99: Small Talk and Everyday Conversation Grammar",
        "category": "english",
        "order": 99,
        "summary": (
            "The grammar of being friendly — openers, echo questions, so do I / neither do I, "
            "and how to leave a conversation politely."
        ),
        "content": """
<h2>PE-99: Small Talk and Everyday Conversation Grammar</h2>

<p>Small talk is not empty. It is how English speakers open a door before walking through it — and
it has real grammar behind it: question tags, short answers, echo questions, and the beautiful
little structures <em>so do I</em> and <em>neither do I</em>. Learn these and you stop
<mark>translating</mark> and start <b>chatting</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Openers and the expected replies</li>
    <li><b>Echo questions</b> — how to show you are listening</li>
    <li><b>So do I / Neither do I</b> for agreeing</li>
    <li>How to keep a conversation going, and how to end it politely</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Agreeing in two words</span>
  <span class="pe-chip pe-chip--v">So do I</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--neg">Neither do I</span>
</div>

LEGEND_HERE

<h3>1. Openers — and the reply they expect</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Opener</th><th>Expected reply</th></tr>
  <tr><td>How are you?</td><td>Fine, thanks. And you?</td></tr>
  <tr><td>How's it going?</td><td>Not bad, thanks. You?</td></tr>
  <tr><td>How have you been?</td><td>Pretty good, thanks.</td></tr>
  <tr><td>What have you been up to?</td><td>Not much, really. Just studying.</td></tr>
  <tr><td>Lovely day, isn't it?</td><td>Yes, beautiful!</td></tr>
  <tr><td>Long time no see!</td><td>I know! How are things?</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— Hi Afsona! <b>How have you been</b>? — Pretty good, thanks. <b>What
     about you</b>? — Not bad. I<b>'ve been studying</b> for my exams.</p>
  <p class="pe-ex__uz">— Salom Afsona! Ahvollar qalay? — Yaxshi, rahmat. Sen-chi? — Yomon emas.
     Imtihonlarga tayyorlanyapman.</p>
  <p class="pe-ex__why">Notice the Present Perfect Continuous (PE-36) — it is the natural tense
     for "what have you been doing lately".</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Madaniy nozik nuqta: <em>How are you?</em> ingliz tilida <b>haqiqiy savol emas</b> — bu
  salomlashishning bir qismi. Uzoq javob berish ("Ahvolim yaxshi emas, chunki...") kutilmaydi.
  Qisqa javob bering va <b>savolni qaytaring</b>: <em>Fine, thanks. And you?</em> Oʻzbekchadagi
  "Yaxshi, rahmat. Oʻzingiz-chi?" bilan bir xil.
</div>

<h3>2. Echo questions — showing you are listening</h3>

<p>This is the trick that makes you sound like a real speaker. You repeat the auxiliary as a tiny
question, meaning "really? tell me more".</p>

<div class="pe-ex">
  <p class="pe-ex__en">— I went to Samarkand last week. — <b>Oh, did you?</b><br>
     — I'm learning Korean. — <b>Are you?</b> That's interesting!<br>
     — I've never eaten sushi. — <b>Haven't you?</b></p>
  <p class="pe-ex__uz">— Oʻtgan hafta Samarqandga bordim. — Rostdanmi? — Koreys tilini
     oʻrganyapman. — Shundaymi? Qiziq!</p>
  <p class="pe-ex__why">Same auxiliary as the speaker used — exactly like a question tag
     (PE-73), but standing alone.</p>
</div>

<h3>3. So do I / Neither do I</h3>

<p>Two very short ways to say "me too" and "me neither" — and they need the <b>same auxiliary</b>
plus <b>inversion</b> (PE-84).</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Positive → So + aux + I</p>
    <ul>
      <li>— I like plov. — <b>So do I.</b></li>
      <li>— I'm tired. — <b>So am I.</b></li>
      <li>— I've been there. — <b>So have I.</b></li>
      <li>— I can swim. — <b>So can I.</b></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Negative → Neither + aux + I</p>
    <ul>
      <li>— I don't smoke. — <b>Neither do I.</b></li>
      <li>— I'm not hungry. — <b>Neither am I.</b></li>
      <li>— I haven't seen it. — <b>Neither have I.</b></li>
      <li>— I can't drive. — <b>Neither can I.</b></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  The word order is inverted: <b>So do I</b>, not <s>So I do</s>. And <em>neither</em> already
  carries the negative — <s>Neither don't I</s> ✗. Informally you will also hear
  <em>Me too</em> and <em>Me neither</em>, which are always safe.
</div>

<h3>4. Keeping it going</h3>

<ol class="pe-steps">
  <li><b>React:</b> <em>Really? · That's interesting. · That sounds great. · Oh no!</em></li>
  <li><b>Ask back:</b> <em>What about you? · And how about your family?</em></li>
  <li><b>Ask a follow-up:</b> <em>How long have you been doing that? · What was it like?</em></li>
  <li><b>Use fillers</b> while you think: <em>Well… · Actually… · You know… · I mean…</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">— I've just started playing the guitar. — <b>Have you? That's great!</b>
     <b>How long have you been</b> learning? — <b>Well</b>, only about a month.</p>
  <p class="pe-ex__uz">— Yaqinda gitara chalishni boshladim. — Shundaymi? Zoʻr! Qancha vaqtdan
     beri oʻrganyapsan? — Xoʻsh, taxminan bir oydan beri.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Fillerlar ("<em>Well…</em>", "<em>Actually…</em>", "<em>You know…</em>") — vaqt yutish
  vositasi, xuddi oʻzbekchadagi "<b>xoʻsh</b>", "<b>aslida</b>", "<b>bilasizmi</b>" kabi.
  Ular <b>xato emas</b> — aksincha, jim qolishdan koʻra ancha tabiiy eshitiladi. Ogʻzaki
  imtihonda ham foydali: oʻylash uchun vaqt beradi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Takroriy savollar (<em>Oh, did you? · Are you? · Have you?</em>) — ingliz suhbatining
  <b>eng tabiiy belgisi</b>. Ular "eshitib turibman, davom eting" degan maʼnoni beradi,
  xuddi oʻzbekchadagi "<b>shundaymi?</b>", "<b>rostdanmi?</b>", "<b>ha-a?</b>" kabi.
  Suhbatda jim turmang — kichik javoblar bering, shunda gap uzilmaydi.
</div>

<h3>5. Ending politely</h3>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Anyway,</b> I'd better go — I've got a lesson at two. <b>It was nice
     talking to you.</b> <b>See you soon!</b></p>
  <p class="pe-ex__uz">Xoʻp, men ketaman — soat ikkida darsim bor. Suhbatdan xursandman.
     Yana koʻrishguncha!</p>
  <p class="pe-ex__why"><em>Anyway</em> is the standard signal that you are about to leave, and
     <em>I'd better go</em> (PE-46) softens it.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>— I like tea. — So I do.</s></p>
  <p class="pe-good">— <b>So do I.</b> <em>(inversion)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>— I don't like coffee. — Neither don't I.</s></p>
  <p class="pe-good">— <b>Neither do I.</b></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>— How are you? — I am not very well because my head hurts and…</s></p>
  <p class="pe-good">— <b>Fine, thanks. And you?</b> <em>(save the details for a real
     question)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>— I went to London. — Oh, do you?</s></p>
  <p class="pe-good">— Oh, <b>did you?</b> <em>(match the tense)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>What are you doing these days? — I am study.</s></p>
  <p class="pe-good">— I<b>'ve been studying</b> a lot lately.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Reply with <em>So</em> or <em>Neither</em>: <em>— I'm really tired. — ___</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>So am I.</strong> Positive sentence, verb <em>am</em> — so <em>So am I</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Reply: <em>— I've never been abroad. — ___</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Neither have I.</strong> Negative + <em>have</em> → <em>Neither have I</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Add an echo question: <em>— I passed my driving test! — ___</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Did you? Congratulations!</strong> Match the tense of the speaker.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     End a conversation politely — write two sentences.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Anyway, I'd better get going — I'm meeting my sister at
         five. It was lovely to see you!</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a five-line small-talk exchange with a classmate.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong><br>
         — Hi Jasur! How's it going?<br>
         — Not bad, thanks. What about you?<br>
         — Fine. I've been revising all weekend.<br>
         — Have you? So have I. Anyway, see you in class!<br>
         — See you!</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Small talk</b><span>oddiy suhbat</span></li>
  <li><b>Echo question</b><span>takroriy savol</span></li>
  <li><b>Filler</b><span>toʻldiruvchi soʻz</span></li>
  <li><b>So do I</b><span>men ham</span></li>
  <li><b>Neither do I</b><span>men ham yoʻq</span></li>
  <li><b>Not bad</b><span>yomon emas</span></li>
  <li><b>Long time no see</b><span>koʻrishmaganimizga ancha boʻldi</span></li>
  <li><b>Anyway</b><span>xoʻp, har holda</span></li>
  <li><b>To get going</b><span>ketmoq, joʻnamoq</span></li>
  <li><b>Follow-up question</b><span>qoʻshimcha savol</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><em>How are you?</em> is a greeting, not a real question — reply short and ask back.</li>
    <li><b>Echo questions</b> repeat the auxiliary: <em>Oh, did you? Are you?</em></li>
    <li><b>So do I</b> / <b>Neither do I</b> — same auxiliary, inverted order.</li>
    <li>Keep it going: react → ask back → follow-up. Use <b>fillers</b> to think.</li>
    <li>End with <b>Anyway, I'd better go…</b> plus something warm.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-100: Your Grammar Toolkit: The One-Page Review of Everything",
        "category": "english",
        "order": 100,
        "summary": (
            "The whole course on one page — every tense, every modal, every conditional, the ten "
            "golden rules, and what to do next. The finish line."
        ),
        "content": """
<h2>PE-100: Your Grammar Toolkit: The One-Page Review of Everything</h2>

<p>You have reached the last lesson. Stop for a moment and look at what that means: you started at
<em>"What Is a Sentence?"</em> and you have worked through <b>every tense in English</b>, every
modal verb, every conditional, the passive, reported speech, relative clauses and the whole
apparatus of academic style. <mark>There is no major area of English grammar left that you have
not met.</mark></p>

<p>This lesson gives you no new grammar. It gives you the <b>map</b> — everything in one place, so
you can find any rule in seconds. Keep it open when you write.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will find</p>
  <ul>
    <li>All 12 tenses in one table</li>
    <li>The modal scales and the four conditionals</li>
    <li>The <b>ten golden rules</b> that cross the whole language</li>
    <li>What to do next, now that the course is finished</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Where you started · where you are</span>
  <span class="pe-chip pe-chip--s">Subject + Verb</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">the whole grammar of English</span>
</div>

LEGEND_HERE

<h3>1. The 12 tenses</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Aspect</th><th>PAST</th><th>PRESENT</th><th>FUTURE</th></tr>
  <tr>
    <td><b>Simple</b></td><td>I worked</td><td>I work</td><td>I will work</td>
  </tr>
  <tr>
    <td><b>Continuous</b></td><td>I was working</td><td>I am working</td><td>I will be working</td>
  </tr>
  <tr>
    <td><b>Perfect</b></td><td>I had worked</td><td>I have worked</td><td>I will have worked</td>
  </tr>
  <tr>
    <td><b>Perfect Cont.</b></td><td>I had been working</td><td>I have been working</td><td>I will have been working</td>
  </tr>
</table>
</div>

<p><b>Two questions build any tense</b> (PE-41): <em>When?</em> — past, present, future.
<em>How do I see it?</em> — a fact (Simple), in progress (Continuous), finished with a result
(Perfect), or measured in length (Perfect Continuous).</p>

<h3>2. Modals: three scales</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Obligation</p>
    <p>must / have to → had better → should → could → don't have to · <b>mustn't</b> =
       forbidden</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Certainty</p>
    <p>must be (95%) → should be (70%) → might be (50%) → <b>can't be</b> (5%)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Ability</p>
    <p>can → could / was able to → will be able to</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>In the past</p>
    <p>modal + <b>have + V3</b>: <em>must have gone, should have told</em></p>
  </div>
</div>

<h3>3. The four conditionals</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Type</th><th>If-half</th><th>Result</th><th>Meaning</th></tr>
  <tr><td>Zero</td><td>present</td><td>present</td><td>always true</td></tr>
  <tr><td>First</td><td>present</td><td>will + verb</td><td>real future</td></tr>
  <tr><td>Second</td><td>past</td><td>would + verb</td><td>imaginary present</td></tr>
  <tr><td>Third</td><td>had + V3</td><td>would have + V3</td><td>imaginary past</td></tr>
</table>
</div>

<p>Each step into imagination moves the verb one step <b>back</b> — and there is
<b>never a <em>will</em> or <em>would</em> after <em>if</em></b>.</p>

<h3>4. Look how far you have come</h3>

<p>Here are three sentences: what a beginner writes, and what you can write now. The ideas are
the same. The difference is a hundred lessons.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Then: <em>I live here 10 year. I like very much.</em><br>
     Now: <em>I<b>'ve been living</b> here <b>for</b> ten years, and I like it <b>very
     much</b>.</em></p>
  <p class="pe-ex__uz">Bu yerda oʻn yildan beri yashayman va menga bu juda yoqadi.</p>
  <p class="pe-ex__why">Present Perfect Continuous · <em>for</em> · word order — PE-36, PE-33,
     PE-72.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Then: <em>If I will have money, I will buy car.</em><br>
     Now: <em><b>If I had</b> more money, I <b>would buy a</b> car — but <b>if I save</b>
     enough this year, I <b>will</b> definitely get one.</em></p>
  <p class="pe-ex__uz">Agar koʻproq pulim boʻlsa, mashina olardim — lekin bu yil yetarlicha
     yigʻsam, albatta olaman.</p>
  <p class="pe-ex__why">Second and first conditionals in one sentence — PE-53, PE-54.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Then: <em>Yesterday I go school. Teacher say me homework.</em><br>
     Now: <em>Yesterday, <b>while I was walking</b> to school, I <b>realised</b> that I
     <b>had forgotten</b> the homework <b>my teacher had told me to do</b>.</em></p>
  <p class="pe-ex__uz">Kecha maktabga ketayotib, oʻqituvchim aytgan uy vazifasini esdan
     chiqarganimni angladim.</p>
  <p class="pe-ex__why">Past Continuous · Past Perfect · reported command · relative clause —
     PE-23, PE-38, PE-63, PE-58.</p>
</div>

<h3>5. The ten golden rules</h3>

<ol class="pe-steps">
  <li><b>One tense marker per verb phrase.</b> <em>didn't go</em>, not <s>didn't went</s>.</li>
  <li><b>English word order is S–V–O–Manner–Place–Time</b> — and nothing comes between the verb
      and its object.</li>
  <li><b>Every sentence needs a subject.</b> <em>It is raining.</em> <em>There is a problem.</em></li>
  <li><b>he / she / it takes -s</b> in the present simple. Nothing else does.</li>
  <li><b>A singular countable noun needs a word in front:</b> <em>a, the, my, this…</em></li>
  <li><b>One negative per sentence.</b> <em>I never smoke.</em> <em>Although…</em> (not
      <em>…but</em>).</li>
  <li><b>Stative verbs take no -ing:</b> know, want, like, need, have (own).</li>
  <li><b>No <em>will</em> after when, if, as soon as, until, by the time.</b></li>
  <li><b>After a preposition, a verb takes -ing.</b> <em>good at swimming</em>.</li>
  <li><b>Learn words with their partners:</b> <em>good at</em>, <em>depend on</em>, <em>make a
      decision</em>.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana shu <b>oʻn qoida</b> — butun kursning eng qisqa xulosasi. Ularni bir varaqqa
  koʻchirib, stolingiz ustiga qoʻyib qoʻying. Yozgan har bir matnni shu roʻyxat boʻyicha
  tekshirsangiz, xatolaringizning taxminan <b>80 foizi</b> shu yerda tutiladi. Qolgan 20
  foizi — soʻz boyligi va mashq masalasi.
</div>

<h3>6. The five Uzbek-interference fixes</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Watch for these</p>
    <ul>
      <li>Articles — Uzbek has none (PE-4)</li>
      <li>Third-person <b>-s</b> (PE-9)</li>
      <li>Word order — Uzbek is SOV (PE-72)</li>
      <li><em>for / since</em> + Present Perfect (PE-33)</li>
      <li>Double negatives · <em>although…but</em> (PE-11, PE-52)</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Where Uzbek helps you</p>
    <ul>
      <li><b>-moqchiman</b> = going to (PE-27)</li>
      <li><b>-gan ekan</b> = has been -ing (PE-36)</li>
      <li><b>-tirdim</b> = have it done (PE-66)</li>
      <li><b>-ib / -ayotib</b> = participle clause (PE-86)</li>
      <li><b>mumkin emas / shart emas</b> = mustn't / don't have to (PE-45)</li>
    </ul>
  </div>
</div>

<h3>7. What to do next</h3>

<p>Grammar is now the part of English you know best. From here, progress comes from
<b>use</b>, not study.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Read every day</p>
    <p>Fifteen minutes. Copy any phrase you like into a notebook — <b>whole phrases</b>, not
       single words (PE-90).</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Write something weekly</p>
    <p>An email, a diary entry, a short story. Then check it with the ten golden rules.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Speak, imperfectly</p>
    <p>Fluency comes from talking with mistakes, not from waiting until you are perfect.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Keep three errors in view</p>
    <p>Your own top three, on the first page of your notebook (PE-92).</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Come back to this lesson often. It is not a farewell page — it is a <b>reference desk</b>.
  When you are unsure of a rule, find it here first, then open the lesson number beside it.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Va oxirgi soʻz: siz <b>100 dars</b> davomida ingliz tili grammatikasining <b>butun
  tizimini</b> koʻrib chiqdingiz — 12 zamon, modal feʼllar, shart gaplar, majhul nisbat,
  koʻchirma gap. Bu kichik ish emas. Endi grammatika sizning <b>tayanchingiz</b>, va
  bundan keyingi oʻsish <b>mashq</b> orqali keladi: oʻqing, yozing, gapiring. Xato
  qilishdan qoʻrqmang — xato qilgan odam oʻrganadi, jim turgan odam esa yoʻq.
  <b>Omad, va oʻrganishni davom ettiring!</b>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yuqoridagi "Then / Now" misollariga yana bir marta qarang. Birinchi variantlarni koʻp
  oʻquvchi yozadi — va bu <b>uyat emas</b>, bu boshlanish. Ikkinchi variantlarni esa
  <b>siz</b> yozasiz, chunki endi Present Perfect, shart gaplar, Past Perfect va
  aniqlovchi ergash gaplarni bilasiz. Farq — isteʼdodda emas, <b>mehnatda</b>.
</div>

<h3>Practice — a little of everything</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Name the tense and fix the error: <em>I am living here since 2018.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I have lived / have been living here since 2018.</strong></p>
      <p>Started in the past and still true → Present Perfect (PE-33), not the present.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Which conditional, and complete it: <em>If I ___ (know) his number, I ___ (call)
     him.</em> (I don't know it)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Second conditional: If I knew his number, I would call him.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Find three errors: <em>She go to the school every day and she is very good in maths.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She goes to school every day and she is very good at maths.</strong></p>
      <p>Missing <b>-s</b> (PE-9) · <em>the</em> before <em>school</em> (PE-4) ·
         <em>good at</em>, not <em>in</em> (PE-76).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Make it passive, then report it: <em>Somebody stole my bike. "My bike was stolen," he
     said.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My bike was stolen.</strong> (PE-60) →
         <strong>He said (that) his bike had been stolen.</strong> (PE-62)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write three sentences about what you will do with your English next.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I<b>'m going to</b> read one English article every day.
         <b>If I keep</b> doing that, my vocabulary <b>will grow</b> quickly. By this time next
         year, I <b>will have finished</b> my first English novel.</em></p>
      <p>Going to (PE-27) · first conditional (PE-53) · future perfect (PE-40). You built
         that.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Toolkit</b><span>asboblar toʻplami</span></li>
  <li><b>Reference</b><span>maʼlumotnoma</span></li>
  <li><b>Aspect</b><span>zamon koʻrinishi</span></li>
  <li><b>Golden rule</b><span>oltin qoida</span></li>
  <li><b>Interference</b><span>ona tili taʼsiri</span></li>
  <li><b>Fluency</b><span>ravonlik</span></li>
  <li><b>Accuracy</b><span>aniqlik</span></li>
  <li><b>To revise</b><span>takrorlamoq</span></li>
  <li><b>Progress</b><span>oʻsish, natija</span></li>
  <li><b>To keep going</b><span>davom ettirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 The whole course in five lines</p>
  <ul>
    <li><b>3 times × 4 aspects = 12 tenses.</b> Build them, don't memorise them.</li>
    <li><b>Modals are scales</b> — choose how strong you want to sound.</li>
    <li><b>Each step into imagination moves the verb one step back.</b></li>
    <li><b>The ten golden rules</b> catch most of your remaining errors.</li>
    <li><b>Grammar is finished; now use it.</b> Read, write, speak — and keep going. 🎓</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
