# -*- coding: utf-8 -*-
"""Prime English — end of Block D (51) and start of Block E, building sentences (52–55).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_51_55.py --author=prime
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
        "title": "PE-51: Modal Verbs: The Full Strength Scale",
        "category": "english",
        "order": 51,
        "summary": (
            "Every modal on one page, arranged by strength — obligation, certainty and "
            "ability — plus how each one moves into the past."
        ),
        "content": """
<h2>PE-51: Modal Verbs: The Full Strength Scale</h2>

<p>You have met every modal verb English has. Now, just as PE-41 did for the tenses, this
lesson puts them all on one page. The secret is that modals are not a random list — they line
up on <mark>scales of strength</mark>, and choosing the right one is simply choosing how strong
you want to sound. Keep this lesson open when you write.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The three families: obligation, certainty, ability</li>
    <li>Every modal arranged from strongest to weakest</li>
    <li>How each one moves into the past</li>
    <li>The four rules that govern all of them</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three scales</span>
  <span class="pe-chip pe-chip--s">obligation</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">certainty</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">ability</span>
</div>

<h3>1. Scale one: obligation and advice</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Strength</th><th>Modal</th><th>Meaning</th><th>Example</th></tr>
  <tr><td>100%</td><td><b>must / have to</b></td><td>obligation</td><td>You <b>must</b> wear a helmet.</td></tr>
  <tr><td>80%</td><td><b>had better</b></td><td>advice + warning</td><td>You<b>'d better</b> hurry.</td></tr>
  <tr><td>70%</td><td><b>should / ought to</b></td><td>advice</td><td>You <b>should</b> rest.</td></tr>
  <tr><td>30%</td><td><b>could / might</b></td><td>suggestion</td><td>You <b>could</b> ask him.</td></tr>
  <tr><td>0%</td><td><b>don't have to</b></td><td>not necessary</td><td>You <b>don't have to</b> come.</td></tr>
  <tr><td>✗</td><td><b>mustn't / can't</b></td><td>forbidden</td><td>You <b>mustn't</b> smoke.</td></tr>
</table>
</div>

<p>Remember the crucial point from PE-45: the bottom two rows are <b>not</b> the same.
<em>Don't have to</em> frees you; <em>mustn't</em> forbids you.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <b>must</b> wear a seatbelt (the law). You<b>'d better</b> wear a
     coat (it's freezing). You <b>should</b> wear something smart (my opinion). You
     <b>don't have to</b> wear a tie (it's up to you).</p>
  <p class="pe-ex__uz">Xavfsizlik kamarini taqishingiz shart. Palto kiyganingiz maʼqul —
     juda sovuq. Chiroyliroq kiyinsangiz yaxshi boʻlardi. Galstuk taqishingiz esa shart
     emas.</p>
  <p class="pe-ex__why">One topic, four strengths — that is the whole scale in action.</p>
</div>

<h3>2. Scale two: certainty</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Certainty</th><th>Present</th><th>Past</th></tr>
  <tr><td>100% — I know</td><td>He <b>is</b> at home.</td><td>He <b>was</b> at home.</td></tr>
  <tr><td>95% — almost sure</td><td>He <b>must be</b> at home.</td><td>He <b>must have been</b> at home.</td></tr>
  <tr><td>70% — I expect</td><td>He <b>should be</b> at home.</td><td>He <b>should have been</b> at home.</td></tr>
  <tr><td>50% — perhaps</td><td>He <b>might / may / could be</b>.</td><td>He <b>might have been</b>.</td></tr>
  <tr><td>5% — almost sure not</td><td>He <b>can't be</b> at home.</td><td>He <b>can't have been</b> at home.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The light is on, so she <b>must be</b> in. Her car has gone, so she
     <b>can't be</b> here. She <b>might be</b> at her sister's.</p>
  <p class="pe-ex__uz">Chiroq yoniq, demak u uyda boʻlsa kerak. Mashinasi yoʻq, demak bu yerda
     boʻlishi mumkin emas. Opasinikida boʻlishi mumkin.</p>
</div>

<h3>3. Scale three: ability and permission</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Ability now</p>
    <p><b>can</b> — <em>I can swim.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Ability in the past</p>
    <p><b>could</b> (general) · <b>was able to</b> (one success)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Other times</p>
    <p><b>be able to</b> — <em>will be able to, have been able to</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Permission</p>
    <p><b>can → could → may</b> (increasingly polite)</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Modal feʼllarni alohida soʻzlar deb emas, <b>shkala</b> deb koʻring. Gapirishdan oldin
  bitta savol bering: <b>qanchalik kuchli aytmoqchiman?</b> Maslahatmi yoki majburiyat?
  Ishonchim komilmi yoki taxminmi? Javobni topsangiz, kerakli modal shkaladan oʻzi
  chiqadi — yodlash shart emas.
</div>

<h3>4. Moving into the past</h3>

<p>Modals have no past tense of their own. Each one solves the problem differently:</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Present</th><th>Past</th><th>Example</th></tr>
  <tr><td>can (ability)</td><td><b>could / was able to</b></td><td>I <b>could</b> swim at five.</td></tr>
  <tr><td>must (obligation)</td><td><b>had to</b></td><td>I <b>had to</b> leave early.</td></tr>
  <tr><td>mustn't (forbidden)</td><td><b>wasn't allowed to</b></td><td>We <b>weren't allowed to</b> talk.</td></tr>
  <tr><td>must be (deduction)</td><td><b>must have + V3</b></td><td>She <b>must have</b> forgotten.</td></tr>
  <tr><td>should (advice)</td><td><b>should have + V3</b></td><td>You <b>should have</b> told me.</td></tr>
  <tr><td>will</td><td><b>would</b></td><td>He said he <b>would</b> come.</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat: <b>must</b>, <b>can</b>, <b>should</b> — bularning hech birida <b>-ed</b> yoʻq.
  Oʻtgan zamonda ular <b>butunlay boshqa soʻzga</b> aylanadi: <em>must → had to</em>,
  <em>can → could</em>, yoki <b>have + V3</b> qoʻshiladi: <em>should → should have + V3</em>.
  <s>musted</s>, <s>shoulded</s>, <s>canned</s> degan shakllar yoʻq.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>can</b> swim now. I <b>couldn't</b> swim as a child. Last summer
     I <b>was able to</b> swim across the lake. Next year I<b>'ll be able to</b> teach my
     little brother.</p>
  <p class="pe-ex__uz">Hozir suza olaman. Bolaligimda suza olmasdim. Oʻtgan yozda koʻlni suzib
     oʻta oldim. Kelasi yil ukamga oʻrgata olaman.</p>
  <p class="pe-ex__why">One ability, four times — and only <em>be able to</em> can reach the
     future.</p>
</div>

<h3>5. The four rules, one last time</h3>

<ol class="pe-steps">
  <li><b>No -s:</b> <em>she must</em>, <em>he can</em>, <em>it should</em>.</li>
  <li><b>No "to"</b> after them — except <b>ought to</b> and <b>have to</b>.</li>
  <li><b>Questions by inversion:</b> <em>Can you…? Should I…? Must we…?</em></li>
  <li><b>Negatives with "not":</b> <em>can't, mustn't, shouldn't, won't</em> — never
      <em>don't</em>.</li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  If you only master five modals, make them <b>can</b>, <b>should</b>, <b>have to</b>,
  <b>might</b> and <b>would</b>. Between them they cover ability, advice, obligation,
  possibility and politeness — which is nearly everything you need in daily conversation.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchadagi <b>"kerak"</b> soʻzi ingliz tilida kamida <b>toʻrtta</b> turli soʻzga
  aylanadi: <em>must</em> / <em>have to</em> (majburiyat), <em>should</em> (maslahat),
  <em>need to</em> (zarurat), <em>must be</em> (taxmin — "boʻlsa kerak"). Shuning uchun
  "kerak" ni koʻrganda avtomatik <em>must</em> deb tarjima qilmang — avval maʼnosini
  aniqlang.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>You don't have to smoke here — it's forbidden.</s></p>
  <p class="pe-good">You <b>mustn't</b> smoke here.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He mustn't be at home — his car is gone.</s></p>
  <p class="pe-good">He <b>can't be</b> at home.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I must go to the doctor.</s></p>
  <p class="pe-good">Yesterday I <b>had to</b> go to the doctor.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I should of called you.</s></p>
  <p class="pe-good">I <b>should have</b> called you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Next year I will can drive.</s></p>
  <p class="pe-good">Next year I <b>will be able to</b> drive.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>You <span class="pe-blank">?</span> touch that wire — it's live!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>mustn't</strong> (or <em>can't</em>) — this is prohibition, not free choice.
         <s>don't have to</s> would mean it's optional.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Put into the past: <em>She must be very tired.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She must have been very tired.</strong></p>
      <p>Deduction moves into the past with <b>have + V3</b>, not with <em>had to</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Order by strength: <em>should · could · must · had better</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>must → had better → should → could.</strong> From obligation down to a gentle
         suggestion.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which meaning of <em>must</em>? <em>(a) You must be Afsona's brother. (b) You must
     finish by six.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) deduction</strong> — I'm guessing who you are.
         <strong>(b) obligation</strong> — I'm telling you what to do.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Fill in with any suitable modal: <em>I ___ swim when I was six, but I ___ dive — I was
     too afraid.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>could … couldn't.</strong> General past ability, positive and negative.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Modal verb</b><span>modal feʼl</span></li>
  <li><b>Strength</b><span>kuch darajasi</span></li>
  <li><b>Obligation</b><span>majburiyat</span></li>
  <li><b>Certainty</b><span>ishonchlilik</span></li>
  <li><b>Deduction</b><span>taxmin, xulosa</span></li>
  <li><b>Prohibition</b><span>taqiq</span></li>
  <li><b>Permission</b><span>ruxsat</span></li>
  <li><b>Helmet</b><span>dubulgʻa</span></li>
  <li><b>Wire</b><span>sim</span></li>
  <li><b>To dive</b><span>sho'ngʻimoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Modals are <b>scales</b>, not lists — choose by how strong you want to sound.</li>
    <li>Obligation: <b>must → had better → should → could → don't have to</b>.</li>
    <li>Certainty: <b>must be → should be → might be → can't be</b>.</li>
    <li>In the past they change word: <b>had to, could, must have + V3, should have +
        V3</b>.</li>
    <li>The four rules: no <b>-s</b>, no <b>to</b>, invert for questions, <b>not</b> for
        negatives.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-52: Conjunctions: and, but, or, so, because",
        "category": "english",
        "order": 52,
        "summary": (
            "The words that join ideas into real sentences — and the although/but mistake that "
            "comes straight from Uzbek."
        ),
        "content": """
<h2>PE-52: Conjunctions: and, but, or, so, because</h2>

<p><em>"I was tired. I went home. I slept."</em> Every sentence is correct — and it reads like
a five-year-old wrote it. Real English joins ideas together: <em>"I was tired, <b>so</b> I went
home <b>and</b> slept."</em> The words that do this joining are called
<mark>conjunctions</mark>, and they are the first tool of Block E: building bigger
sentences.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The five everyday joiners: <b>and, but, or, so, because</b></li>
    <li>Why <b>so</b> and <b>because</b> point in opposite directions</li>
    <li><b>although</b> — and why you must never add <em>but</em> after it</li>
    <li>Where the comma goes</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Joining two ideas</span>
  <span class="pe-chip pe-chip--s">idea 1</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">conjunction</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">idea 2</span>
</div>

LEGEND_HERE

<h3>1. The five you need every day</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>and — adding</p>
    <p><em>I bought bread <b>and</b> milk.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>but — contrast</p>
    <p><em>It's cheap <b>but</b> good.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>or — choice</p>
    <p><em>Tea <b>or</b> coffee?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>so — result</p>
    <p><em>It was late, <b>so</b> I left.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>because — reason</p>
    <p><em>I left <b>because</b> it was late.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">6</span>although — contrast</p>
    <p><em><b>Although</b> it rained, we went.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona studies hard <span class="pe-hl pe-hl--adv">and</span> she
     helps at home, <span class="pe-hl pe-hl--adv">but</span> she never complains.</p>
  <p class="pe-ex__uz">Afsona qattiq oʻqiydi va uyda yordam beradi, lekin hech qachon
     shikoyat qilmaydi.</p>
</div>

<h3>2. so and because — the same idea, opposite order</h3>

<p>This pair confuses many learners, but the logic is simple. <b>Because</b> introduces the
<b>reason</b>. <b>So</b> introduces the <b>result</b>. The same two facts can be joined either
way — you just swap their order.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">because + reason</p>
    <p>I went home <b>because</b> I was tired.</p>
    <p>result ← reason</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">so + result</p>
    <p>I was tired, <b>so</b> I went home.</p>
    <p>reason → result</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Use one or the other, never both in the same sentence:
  <s>Because I was tired, so I went home.</s> ✗ Choose either <b>because</b> or <b>so</b> —
  the sentence needs only one joiner.
</div>

<p>Also note <b>because</b> + a full clause vs <b>because of</b> + a noun:</p>

<div class="pe-ex">
  <p class="pe-ex__en">We stayed at home <b>because it rained</b>. = We stayed at home
     <b>because of the rain</b>.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻgani uchun uyda qoldik. = Yomgʻir tufayli uyda qoldik.</p>
  <p class="pe-ex__why"><em>because</em> needs a subject and a verb; <em>because of</em> needs
     only a noun.</p>
</div>

<h3>3. although — and the mistake that comes from Uzbek</h3>

<p>In Uzbek, a contrast sentence takes <b>two</b> markers: <em><b>Garchi</b> charchagan
boʻlsam ham, <b>lekin</b> ishladim.</em> English uses only <b>one</b>. Writing both is one of
the most recognisable Uzbek-speaker errors in written English.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>Although it was raining, but we went out.</s></p>
  <p class="pe-good"><b>Although</b> it was raining, we went out.</p>
  <p class="pe-good">It was raining, <b>but</b> we went out.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu — oʻzbek tilidan kelib chiqadigan eng koʻzga tashlanadigan xato. Oʻzbekchada
  "<b>garchi</b> ... <b>lekin</b>" juftlik boʻlib keladi, ingliz tilida esa
  <b>faqat bittasi</b> ishlatiladi: yo <b>although</b>, yo <b>but</b> — ikkalasi
  birga emas. Xuddi shu qoida <em>because ... so</em> juftligiga ham tegishli.
</div>

<p><b>Though</b> means the same as <em>although</em> and is more common in speech;
<b>even though</b> is stronger. All three follow the same one-joiner rule.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tuzilishdagi katta farqni sezing: oʻzbek tilida gaplar <b>feʼl qoʻshimchalari</b> bilan
  bogʻlanadi — <em>charchagan<b>im uchun</b></em>, <em>tugat<b>gach</b></em>,
  <em>yogʻ<b>sa</b></em>. Ingliz tilida esa <b>alohida soʻz</b> qoʻyiladi va u odatda
  gap boʻlagining <b>boshida</b> turadi: <em><b>because</b> I was tired</em>,
  <em><b>after</b> I finished</em>, <em><b>if</b> it rains</em>. Shuning uchun tarjima
  qilganda bogʻlovchini <b>oldinga</b> olib chiqing.
</div>

<h3>4. Where the comma goes</h3>

<ol class="pe-steps">
  <li><b>Before <em>but</em> and <em>so</em></b> when they join two full sentences:
      <em>It was cold, <b>so</b> we stayed in.</em></li>
  <li><b>No comma before <em>because</em></b> in a short sentence:
      <em>I stayed in because it was cold.</em></li>
  <li><b>Comma when the joined part comes first:</b>
      <em><b>Although</b> it was cold<b>,</b> we went out.</em></li>
  <li><b>No comma</b> when joining two short words or phrases: <em>bread and milk</em>.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en"><b>When</b> the lesson finished<b>,</b> we went home. — We went home
     <b>when</b> the lesson finished.</p>
  <p class="pe-ex__uz">Dars tugagach, uyga ketdik. — Dars tugagach uyga ketdik.</p>
  <p class="pe-ex__why">The comma appears only in the first version, where the clause comes
     first.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Vergul qoidasini oson eslash yoʻli: agar gap <b>bogʻlovchi bilan boshlansa</b>
  (<em>Although…, When…, Because…</em>), oʻrtada vergul boʻladi. Agar bogʻlovchi
  <b>oʻrtada</b> boʻlsa, vergul kerak emas. Oʻzbekchadagi "gach, -sa" dan keyingi
  vergulga oʻxshaydi.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Because I was ill, so I didn't come.</s></p>
  <p class="pe-good"><b>Because</b> I was ill, I didn't come. / I was ill, <b>so</b> I didn't come.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We stayed home because of it rained.</s></p>
  <p class="pe-good">We stayed home <b>because it rained</b> / <b>because of the rain</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Although he is rich, but he isn't happy.</s></p>
  <p class="pe-good"><b>Although</b> he is rich, he isn't happy.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I like tea and I don't like coffee.</s></p>
  <p class="pe-good">I like tea <b>but</b> I don't like coffee. <em>(contrast, not addition)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He was tired so much that he slept.</s></p>
  <p class="pe-good">He was <b>so tired that</b> he slept.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Join with <em>so</em> and then with <em>because</em>: <em>It was very hot. We stayed
     inside.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It was very hot, so we stayed inside.</strong><br>
         <strong>We stayed inside because it was very hot.</strong></p>
      <p>Same meaning — the order of reason and result simply swaps.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>Although Jasur studied hard, but he failed the test.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Although Jasur studied hard, he failed the test.</strong></p>
      <p>One joiner only. <em>(Oʻzbekcha: "garchi...lekin" ingliz tilida ikkitasi
         boʻlmaydi.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     because or because of: <em>The match was cancelled ___ the bad weather.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>because of</strong> — <em>the bad weather</em> is a noun phrase, with no
         verb. With a verb you would say <em>because the weather was bad</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Where does the comma go? <em>When I got home my mother was cooking.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>When I got home, my mother was cooking.</strong></p>
      <p>The clause comes first, so a comma separates the two halves.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Join these three short sentences into one: <em>I was hungry. There was no bread. I made
     eggs.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I was hungry, <b>but</b> there was no bread, <b>so</b>
         I made eggs.</em></p>
      <p>Three ideas, one sentence, two different joiners — that is adult English.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Conjunction</b><span>bogʻlovchi</span></li>
  <li><b>To join</b><span>bogʻlamoq</span></li>
  <li><b>Reason</b><span>sabab</span></li>
  <li><b>Result</b><span>natija</span></li>
  <li><b>Contrast</b><span>qarama-qarshilik</span></li>
  <li><b>Although / though</b><span>garchi, boʻlsa ham</span></li>
  <li><b>Because of</b><span>tufayli</span></li>
  <li><b>Comma</b><span>vergul</span></li>
  <li><b>Clause</b><span>gap boʻlagi</span></li>
  <li><b>To complain</b><span>shikoyat qilmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>and</b> adds · <b>but</b> contrasts · <b>or</b> chooses · <b>so</b> gives the
        result · <b>because</b> gives the reason.</li>
    <li><b>because</b> + reason · <b>so</b> + result — never both in one sentence.</li>
    <li><b>because</b> + subject + verb · <b>because of</b> + noun.</li>
    <li><b>Although</b> … <s>but</s> — English uses <b>one</b> joiner, not two.</li>
    <li>Comma when the joined clause comes <b>first</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-53: Zero and First Conditional",
        "category": "english",
        "order": 53,
        "summary": (
            "If sentences that are real: what always happens, and what will happen if — plus "
            "the golden rule that there is never a 'will' after 'if'."
        ),
        "content": """
<h2>PE-53: Zero and First Conditional</h2>

<p>Conditionals are how English talks about consequences: <em>if this, then that</em>. There
are four of them, and the good news is that they are a system, not a list. The first two are
about the <b>real</b> world — what is always true, and what will probably happen. And they
share one golden rule that you already met in PE-26:
<mark>never put <em>will</em> after <em>if</em></mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>Zero conditional</b> — things that are always true</li>
    <li><b>First conditional</b> — a real possibility in the future</li>
    <li>The no-<em>will</em>-after-<em>if</em> rule</li>
    <li><b>unless</b>, and the other time words that behave like <em>if</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Zero — always true</span>
  <span class="pe-chip pe-chip--aux">If</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">present simple</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">present simple</span>
</div>
<div class="pe-formula">
  <span class="pe-formula__label">First — real future possibility</span>
  <span class="pe-chip pe-chip--aux">If</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">present simple</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">will + base verb</span>
</div>

LEGEND_HERE

<h3>1. Zero conditional — the law of nature</h3>

<p>Use it for things that are <b>always</b> true: science, rules, habits. Both halves are in
the Present Simple, and <em>if</em> here means almost the same as <em>when</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> you <b>heat</b> water to 100°, it <b>boils</b>.
     <b>If</b> I <b>drink</b> coffee at night, I <b>don't sleep</b>.</p>
  <p class="pe-ex__uz">Agar suvni 100 darajagacha qizdirsangiz, u qaynaydi. Agar kechqurun
     qahva ichsam, uxlay olmayman.</p>
  <p class="pe-ex__why">Not one particular occasion — this is what happens <b>every</b>
     time.</p>
</div>

<h3>2. First conditional — a real future</h3>

<p>Use it when something is genuinely possible: it may well happen, and here is the
consequence. The <em>if</em>-half stays in the Present Simple; the result half takes
<b>will</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> it <span class="pe-hl pe-hl--v">rains</span> tomorrow, we
     <span class="pe-hl pe-hl--aux">will stay</span> at home.</p>
  <p class="pe-ex__uz">Agar ertaga yomgʻir yogʻsa, uyda qolamiz.</p>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  <b>Never put <em>will</em> in the <em>if</em>-half.</b> Both halves are about the future,
  but only one of them shows it: <em>If it <b>rains</b>, I <b>will</b> stay</em> ✓ ·
  <s>If it will rain</s> ✗.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qoidani oʻzbekcha orqali eslash oson: siz ham "Agar yomgʻir yogʻ<b>sa</b>" deysiz,
  "yogʻ<b>adi bo'lsa</b>" demaysiz. Yaʼni oʻzbekchada ham shart qismida kelasi zamon
  ishlatilmaydi. Ingliz tilida ham xuddi shunday — <em>if</em> dan keyin <b>hozirgi
  zamon</b>, <em>will</em> esa faqat ikkinchi yarmida.
</div>

<h3>3. Zero or First? One question</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Zero — every time, always</p>
    <ul>
      <li>If you press this button, the light <b>comes</b> on.</li>
      <li>If Afsona <b>is</b> tired, she <b>goes</b> to bed early.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">First — one particular future occasion</p>
    <ul>
      <li>If you press this button, the light <b>will come</b> on.</li>
      <li>If Afsona <b>is</b> tired tonight, she <b>will go</b> to bed early.</li>
    </ul>
  </div>
</div>

<h3>4. unless = if not</h3>

<p><b>Unless</b> is a useful short-cut. It already contains the negative, so the verb after it
stays positive.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <b>won't pass unless</b> you <b>study</b>. = You won't pass
     <b>if</b> you <b>don't study</b>.</p>
  <p class="pe-ex__uz">Oʻqimasangiz, imtihondan oʻtolmaysiz.</p>
  <p class="pe-ex__why">Never <s>unless you don't study</s> — that would be a double
     negative.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Unless</b> bilan ehtiyot boʻling: oʻzbekchada "<b>-masa</b>" inkor qoʻshimchasi
  feʼlga qoʻshiladi ("oʻqi<b>masa</b>ng"), ingliz tilida esa inkor <b>unless</b> ning
  <b>ichida</b> yashiringan. Shuning uchun undan keyingi feʼl <b>ijobiy</b> qoladi:
  <em>unless you <b>study</b></em> ✓, <s>unless you don't study</s> ✗ — aks holda
  ikkita inkor boʻlib qoladi.
</div>

<h3>5. Other words that follow the same rule</h3>

<p>The no-<em>will</em> rule is not only for <em>if</em>. These joiners behave identically:
<b>when, as soon as, before, after, until, while, by the time</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>As soon as</b> I <b>get</b> home, I<b>'ll call</b> you.
     I won't leave <b>until</b> you <b>arrive</b>.</p>
  <p class="pe-ex__uz">Uyga yetib borishim bilanoq senga qoʻngʻiroq qilaman. Sen kelmaguningcha
     ketmayman.</p>
</div>

<p>And the result half does not have to use <em>will</em>. It can take an <b>imperative</b> or
another <b>modal</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__en">If you <b>see</b> Sherbek, <b>tell</b> him to call me. — If you
     <b>finish</b> early, you <b>can</b> go home.</p>
  <p class="pe-ex__uz">Agar Sherbekni koʻrsang, menga qoʻngʻiroq qilishini ayt. — Agar erta
     tugatsangiz, uyga ketishingiz mumkin.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Vergul qoidasi PE-52 dagidek: agar gap <b>if</b> bilan boshlansa, oʻrtada vergul boʻladi —
  <em><b>If</b> it rains<b>,</b> I'll stay home</em>. Agar <b>if</b> oʻrtada boʻlsa, vergul
  qoʻyilmaydi — <em>I'll stay home <b>if</b> it rains</em>. Maʼno ikkalasida ham bir xil.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>If it will rain, we will stay home.</s></p>
  <p class="pe-good"><b>If it rains</b>, we will stay home.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I will see him, I will tell him.</s></p>
  <p class="pe-good"><b>If I see</b> him, I will tell him.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Unless you don't hurry, you'll be late.</s></p>
  <p class="pe-good"><b>Unless you hurry</b>, you'll be late.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>When I will finish, I will call you.</s></p>
  <p class="pe-good"><b>When I finish</b>, I will call you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If you heat ice, it will melts.</s></p>
  <p class="pe-good">If you heat ice, it <b>melts</b>. <em>(always true → zero conditional)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>If you <span class="pe-blank">?</span> (mix) blue and yellow, you
     <span class="pe-blank">?</span> (get) green.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>mix … get.</strong> Zero conditional — this is always true, so both halves
         are Present Simple.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>If Jasur <span class="pe-blank">?</span> (not hurry), he
     <span class="pe-blank">?</span> (miss) the bus.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>doesn't hurry … will miss.</strong> One particular occasion in the future →
         First conditional.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Rewrite with <em>unless</em>: <em>If you don't water the plants, they will die.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Unless you water the plants, they will die.</strong></p>
      <p><em>Unless</em> carries the "not", so the verb becomes positive.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Find the mistake: <em>As soon as the film will finish, we will go home.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>As soon as the film finishes, we will go home.</strong></p>
      <p><em>As soon as</em> follows the same rule as <em>if</em> — no <em>will</em> in that
         half.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Zero or First? <em>If I eat too much plov, I feel sleepy.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Zero conditional</strong> — it describes what always happens to me, not one
         future occasion.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Conditional</b><span>shart gap</span></li>
  <li><b>Condition</b><span>shart</span></li>
  <li><b>Consequence</b><span>oqibat, natija</span></li>
  <li><b>Unless</b><span>...masa</span></li>
  <li><b>To melt</b><span>erimoq</span></li>
  <li><b>To boil</b><span>qaynamoq</span></li>
  <li><b>To press</b><span>bosmoq</span></li>
  <li><b>To water (plants)</b><span>sugʻormoq</span></li>
  <li><b>Always true</b><span>doim toʻgʻri</span></li>
  <li><b>Possibility</b><span>ehtimollik</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Zero:</b> if + present, present — always true (science, rules, habits).</li>
    <li><b>First:</b> if + present, will + base verb — a real future possibility.</li>
    <li><b>Never <em>will</em> after <em>if</em></b> — nor after when, as soon as, until.</li>
    <li><b>unless</b> = if not; the verb after it stays positive.</li>
    <li>The result half can also use an imperative or a modal.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-54: Second Conditional: The Imaginary Present",
        "category": "english",
        "order": 54,
        "summary": (
            "If I had a million dollars… The conditional for dreams and impossible situations "
            "— and the famous phrase 'If I were you'."
        ),
        "content": """
<h2>PE-54: Second Conditional: The Imaginary Present</h2>

<p>The first conditional was about the real world: <em>if it rains, I'll stay home</em> — and
it might well rain. The second conditional steps into <mark>imagination</mark>:
<em>"If I <b>had</b> a million dollars, I <b>would</b> travel the world."</em> I do not have a
million dollars. I am dreaming — and English marks that dream by moving the verb one step into
the past.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>If + past simple, would + base verb</b></li>
    <li>Why an unreal present uses a past tense</li>
    <li><b>If I were you</b> — the most useful advice phrase in English</li>
    <li>How it differs from the first conditional</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Imaginary present</span>
  <span class="pe-chip pe-chip--aux">If</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">past simple</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">would + base verb</span>
</div>

LEGEND_HERE

<h3>1. The past form that isn't about the past</h3>

<p>This is the idea that surprises everyone: the verb after <em>if</em> is in the
<b>Past Simple</b>, but the meaning is <b>now</b>. English uses that past form as a signal
meaning "this is not real".</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> I <span class="pe-hl pe-hl--v">knew</span> her number, I
     <span class="pe-hl pe-hl--aux">would call</span> her.</p>
  <p class="pe-ex__uz">Agar uning raqamini bilsam edi, qoʻngʻiroq qilardim.</p>
  <p class="pe-ex__why">Meaning: I <b>don't</b> know it, so I <b>can't</b> call. Present time,
     past form.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxshi xabar: oʻzbek tilida ham xuddi shunday qilinadi! "Agar pulim <b>boʻlsa edi</b>,
  sayohat qil<b>ardim</b>" — bu yerda ham oʻtgan zamon shakllari ishlatiladi, lekin gap
  <b>hozirgi</b> xayoliy holat haqida. Yaʼni ingliz tilining bu mantigʻi siz uchun
  begona emas — <em>if + oʻtgan zamon</em> = "boʻlsa edi".
</div>

<h3>2. What it is used for</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Impossible situations</p>
    <p><em>If I <b>were</b> a bird, I <b>would</b> fly.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Untrue right now</p>
    <p><em>If I <b>had</b> more time, I <b>would</b> help you.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Unlikely futures</p>
    <p><em>If I <b>won</b> the lottery, I <b>would</b> buy a house.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Giving advice</p>
    <p><em>If I <b>were</b> you, I <b>would</b> apologise.</em></p>
  </div>
</div>

<h3>3. If I were you — learn it as one phrase</h3>

<p>In the second conditional, English traditionally uses <b>were</b> for <b>every</b> person —
including <em>I, he, she, it</em>. This old form survives most strongly in the advice phrase
you will use constantly.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If I were you</b>, I<b>'d</b> talk to the teacher. —
     <b>If I were</b> rich, I<b>'d</b> build a school.</p>
  <p class="pe-ex__uz">Sening oʻrningda boʻlsam, oʻqituvchi bilan gaplashardim. — Boy boʻlsam,
     maktab qurardim.</p>
  <p class="pe-ex__why"><em>If I was</em> is heard in casual speech, but <b>were</b> is the
     correct form in writing and exams.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  <b>If I were you, I'd…</b> is the warmest way to give advice in English — much gentler than
  <em>you should</em>, because you are putting yourself in their place. Learn it as a single
  block and use it whenever a friend asks you what to do.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkinchi shart gapida <b>be</b> feʼli hamma shaxs uchun <b>were</b> boʻladi — hatto
  <em>I</em>, <em>he</em>, <em>she</em> bilan ham: <em>If I <b>were</b>…</em>,
  <em>If he <b>were</b>…</em> Bu eski shakl boʻlib, aynan xayoliylikni bildiradi.
  Ogʻzaki nutqda <em>If I was</em> ham eshitiladi, lekin <b>yozma ish va imtihonda</b>
  doim <b>were</b> yozing.
</div>

<h3>4. First or second? Real or imaginary?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">First — it might really happen</p>
    <ul>
      <li>If it <b>rains</b>, I<b>'ll take</b> an umbrella.</li>
      <li>If I <b>pass</b> the exam, I<b>'ll celebrate</b>.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Second — imagination or unlikely</p>
    <ul>
      <li>If it <b>snowed</b> in July, I<b>'d be</b> amazed.</li>
      <li>If I <b>were</b> the president, I<b>'d change</b> the schools.</li>
    </ul>
  </div>
</div>

<p>Sometimes both are possible, and the choice shows your attitude. <em>If I <b>get</b> a
job…</em> means I expect to. <em>If I <b>got</b> a job…</em> means I doubt it.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni tanlash — bu <b>grammatika emas, munosabat</b>. <em>If I <b>win</b>…</em> — "yutsam"
  (yutishim mumkin deb oʻylayman). <em>If I <b>won</b>…</em> — "yutib qolsam edi"
  (deyarli imkonsiz, xayol). Shuning uchun bir xil vaziyat haqida ikki xil gapirish
  mumkin — hammasi sizning ishonchingizga bogʻliq.
</div>

<h3>5. could and might in the result</h3>

<p>The result half does not have to use <em>would</em>. Swap in <b>could</b> ("would be able
to") or <b>might</b> ("perhaps would") to soften it:</p>

<div class="pe-ex">
  <p class="pe-ex__en">If I had a car, I <b>could</b> drive you home. — If we left now, we
     <b>might</b> catch the train.</p>
  <p class="pe-ex__uz">Mashinam boʻlsa, seni uyingga olib borardim. — Hozir chiqsak, poyezdga
     ulgurishimiz mumkin edi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Never put <b>would</b> in the <em>if</em>-half. Just as <em>will</em> is banned from the
  first conditional's <em>if</em>-half, <em>would</em> is banned here:
  <s>If I would have money…</s> ✗ → <b>If I had money…</b> ✓
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>If I would have time, I would help you.</s></p>
  <p class="pe-good"><b>If I had</b> time, I would help you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I will be you, I would say sorry.</s></p>
  <p class="pe-good"><b>If I were you</b>, I<b>'d</b> say sorry.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If she had more money, she will buy a car.</s></p>
  <p class="pe-good">If she had more money, she <b>would</b> buy a car.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I was a bird, I would flew.</s></p>
  <p class="pe-good">If I <b>were</b> a bird, I would <b>fly</b>. <em>(base verb after would)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>What would you do if you would win the lottery?</s></p>
  <p class="pe-good">What would you do if you <b>won</b> the lottery?</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>If I <span class="pe-blank">?</span> (speak) Korean, I
     <span class="pe-blank">?</span> (work) in Seoul.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>spoke … would work.</strong> I don't speak Korean, so this is imagination —
         past form after <em>if</em>, <em>would</em> in the result.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Give advice: <em>Your friend argued with his brother.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>If I were you, I'd apologise to him.</strong></p>
      <p>Warmer than <em>You should apologise</em>, because you are standing in his place.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     First or second? <em>(a) If I see Afsona, I'll tell her. (b) If I saw a ghost, I'd
     scream.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) First</strong> — I probably will see her. <strong>(b) Second</strong> —
         ghosts are imaginary.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>If I would be taller, I would play basketball.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>If I were taller, I would play basketball.</strong></p>
      <p><em>Would</em> never appears in the <em>if</em>-half.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Answer about yourself: <em>What would you do if you had a free week?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>If I had a free week, I<b>'d</b> visit my grandparents
         in the village and I<b>'d</b> read three books.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Imaginary</b><span>xayoliy</span></li>
  <li><b>Unreal</b><span>haqiqiy emas</span></li>
  <li><b>Unlikely</b><span>ehtimoldan yiroq</span></li>
  <li><b>To imagine</b><span>tasavvur qilmoq</span></li>
  <li><b>Lottery</b><span>lotereya</span></li>
  <li><b>To celebrate</b><span>nishonlamoq</span></li>
  <li><b>Amazed</b><span>hayratda qolgan</span></li>
  <li><b>To argue</b><span>janjallashmoq</span></li>
  <li><b>Ghost</b><span>arvoh</span></li>
  <li><b>To scream</b><span>qichqirmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>If + past simple, would + base verb</b> — past form, present meaning.</li>
    <li>It means the situation is <b>not real</b> or very unlikely.</li>
    <li><b>If I were you, I'd…</b> — the warmest advice phrase in English.</li>
    <li><b>could</b> and <b>might</b> can replace <em>would</em> in the result.</li>
    <li>Never <b>would</b> after <b>if</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-55: Third Conditional: Regretting the Past",
        "category": "english",
        "order": 55,
        "summary": (
            "The conditional for what never happened — if I had studied, I would have passed. "
            "How English rewrites a past it cannot change."
        ),
        "content": """
<h2>PE-55: Third Conditional: Regretting the Past</h2>

<p>Some sentences exist purely to say "it could have been different". <em>"If I <b>had
studied</b> harder, I <b>would have passed</b>."</em> I did not study. I did not pass. Nothing
can change that now — and the third conditional is how English talks about exactly that kind of
imaginary past. It is the language of regret, of relief, and of understanding what went
wrong.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>If + had + V3, would have + V3</b></li>
    <li>How to read the real meaning behind every third conditional</li>
    <li><b>could have</b> and <b>might have</b> in the result</li>
    <li>How the three conditionals line up as one system</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Imaginary past</span>
  <span class="pe-chip pe-chip--aux">If</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">had + V3</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">would have + V3</span>
</div>

LEGEND_HERE

<h3>1. Reading the meaning</h3>

<p>Every third conditional tells you two facts about the real past — and both are the
<b>opposite</b> of what the sentence says.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> I <span class="pe-hl pe-hl--aux">had left</span> earlier, I
     <span class="pe-hl pe-hl--aux">would have caught</span> the bus.</p>
  <p class="pe-ex__uz">Agar erta chiqqanimda, avtobusga ulgurgan boʻlardim.</p>
  <p class="pe-ex__why">Real facts: I did <b>not</b> leave early, and I did <b>not</b> catch
     the bus.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">If Afsona <b>hadn't helped</b> me, I <b>wouldn't have finished</b> the
     project.</p>
  <p class="pe-ex__uz">Agar Afsona menga yordam bermaganida, loyihani tugatmagan boʻlardim.</p>
  <p class="pe-ex__why">Real facts: she <b>did</b> help me, and I <b>did</b> finish. This one
     is relief, not regret.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu tuzilma oʻzbekchadagi "<b>agar ...ganimda, ...gan boʻlardim</b>" qolipiga toʻliq mos
  keladi: <em>Agar oʻqiganimda, imtihondan oʻtgan boʻlardim</em> →
  <em>If I <b>had studied</b>, I <b>would have passed</b></em>. Ikkala tilda ham maʼno
  bir xil: <b>bunday boʻlmagan, va endi oʻzgartirib boʻlmaydi</b>.
</div>

<h3>2. Building it, step by step</h3>

<ol class="pe-steps">
  <li><b>Take the real past:</b> <em>I didn't study. I failed.</em></li>
  <li><b>Turn each half around:</b> didn't study → <em>had studied</em>; failed →
      <em>wouldn't have failed</em>.</li>
  <li><b>Put them together:</b> <em>If I <b>had studied</b>, I <b>wouldn't have
      failed</b>.</em></li>
  <li><b>Check:</b> the <em>if</em>-half always has <b>had + V3</b>; the result always has
      <b>would have + V3</b>.</li>
</ol>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  The banned word again: <b>never put <em>would</em> in the <em>if</em>-half</b>.
  <s>If I would have known…</s> ✗ → <b>If I had known…</b> ✓. This is the single most common
  mistake in the third conditional, and native speakers make it too.
</div>

<h3>3. could have and might have</h3>

<p>As in PE-54, the result half can soften. <b>Could have</b> = "would have been able to";
<b>might have</b> = "perhaps would have".</p>

<div class="pe-ex">
  <p class="pe-ex__en">If you <b>had told</b> me, I <b>could have helped</b> you. — If we
     <b>had left</b> earlier, we <b>might have arrived</b> on time.</p>
  <p class="pe-ex__uz">Agar menga aytganingda, yordam bera olardim. — Agar erta chiqqanimizda,
     oʻz vaqtida yetib borgan boʻlarmidik.</p>
</div>

<h3>4. The three conditionals as one system</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Type</th><th>If-half</th><th>Result</th><th>Meaning</th></tr>
  <tr>
    <td><b>Zero</b></td><td>present simple</td><td>present simple</td>
    <td>always true</td>
  </tr>
  <tr>
    <td><b>First</b></td><td>present simple</td><td>will + verb</td>
    <td>real future possibility</td>
  </tr>
  <tr>
    <td><b>Second</b></td><td>past simple</td><td>would + verb</td>
    <td>imaginary present</td>
  </tr>
  <tr>
    <td><b>Third</b></td><td>had + V3</td><td>would have + V3</td>
    <td>imaginary past</td>
  </tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tizimni koʻring: har safar xayolga bir qadam yaqinlashganda, feʼl bir qadam
  <b>orqaga</b> suriladi. Haqiqiy kelajak — hozirgi zamon (<em>if it rains</em>). Xayoliy
  hozir — oʻtgan zamon (<em>if it rained</em>). Xayoliy oʻtmish — Past Perfect
  (<em>if it had rained</em>). Yaʼni "orqaga surish" — bu ingliz tilining
  <b>xayolot belgisi</b>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Imtihon uchun tez usul: shart gapining <b>turini faqat birinchi yarmiga qarab</b>
  aniqlash mumkin. <em>if + hozirgi zamon</em> → birinchi (yoki nol) tur, javobda
  <b>will</b>. <em>if + oʻtgan zamon</em> → ikkinchi tur, javobda <b>would</b>.
  <em>if + had + V3</em> → uchinchi tur, javobda <b>would have + V3</b>. Birinchi yarmini
  koʻrsangiz, ikkinchisini xatosiz yozasiz.
</div>

<h3>5. It connects to should have</h3>

<p>You already met the language of regret in PE-48. The two work beautifully together:</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>should have</b> revised more. If I <b>had revised</b> more, I
     <b>would have got</b> a better mark.</p>
  <p class="pe-ex__uz">Koʻproq takrorlashim kerak edi. Agar koʻproq takrorlaganimda, yaxshiroq
     baho olgan boʻlardim.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>If I would have known, I would have come.</s></p>
  <p class="pe-good"><b>If I had known</b>, I would have come.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I had knew about the test, I would have studied.</s></p>
  <p class="pe-good">If I <b>had known</b> about the test… <em>(V3, not V2)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If she had come, I would be happy.</s></p>
  <p class="pe-good">If she had come, I <b>would have been</b> happy.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If you had asked me, I would of helped.</s></p>
  <p class="pe-good">… I <b>would have</b> helped.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I didn't miss the bus, I wouldn't have been late.</s></p>
  <p class="pe-good">If I <b>hadn't missed</b> the bus, I wouldn't have been late.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     What really happened? <em>If Sherbek had trained harder, he would have won.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He didn't train hard enough, and he didn't win.</strong> Both halves are the
         opposite of reality.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make a third conditional: <em>I didn't take my umbrella. I got wet.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>If I had taken my umbrella, I wouldn't have got wet.</strong></p>
      <p>Turn each half around: didn't take → <em>had taken</em>; got wet → <em>wouldn't have
         got wet</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>If I would have seen you, I would have said hello.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>If I had seen you, I would have said hello.</strong></p>
      <p><em>Would</em> belongs only in the result half — never after <em>if</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Second or third? <em>If I had a bike, I would cycle to school.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Second</strong> — <em>had</em> alone (not <em>had had</em>), and
         <em>would cycle</em> without <em>have</em>. It means: I don't have a bike now.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one true third conditional about your own past.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>If I <b>hadn't started</b> learning English, I
         <b>wouldn't have met</b> so many interesting people.</em></p>
      <p>Notice this one expresses relief rather than regret — both are possible.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Regret</b><span>afsus</span></li>
  <li><b>Relief</b><span>yengillik</span></li>
  <li><b>Imaginary past</b><span>xayoliy oʻtmish</span></li>
  <li><b>To change</b><span>oʻzgartirmoq</span></li>
  <li><b>To train</b><span>mashq qilmoq</span></li>
  <li><b>To revise</b><span>takrorlamoq</span></li>
  <li><b>Mark / grade</b><span>baho</span></li>
  <li><b>On time</b><span>oʻz vaqtida</span></li>
  <li><b>To cycle</b><span>velosipedda yurmoq</span></li>
  <li><b>Opposite</b><span>teskari</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>If + had + V3, would have + V3</b> — an imaginary past.</li>
    <li>Both halves mean the <b>opposite</b> of what really happened.</li>
    <li><b>could have / might have</b> can replace <em>would have</em>.</li>
    <li>Never <b>would</b> after <b>if</b>; and it is <b>would have</b>, not <s>would
        of</s>.</li>
    <li>The system: each step into imagination moves the verb one step <b>back</b>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
