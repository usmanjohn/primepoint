# -*- coding: utf-8 -*-
"""Prime English — end of Block F (81–82) and start of Block G, advanced style (83–85).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_81_85.py --author=prime
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
        "title": "PE-81: Punctuation: Comma, Apostrophe, Colon, Semicolon",
        "category": "english",
        "order": 81,
        "summary": (
            "The small marks that carry big meaning — where the comma goes, what a colon does, "
            "and the comma splice that spoils good writing."
        ),
        "content": """
<h2>PE-81: Punctuation: Comma, Apostrophe, Colon, Semicolon</h2>

<p>Read these two sentences aloud:</p>

<p><em>"Let's eat<b>,</b> Grandma!"</em> — a polite invitation to dinner.<br>
<em>"Let's eat Grandma!"</em> — something has gone very wrong.</p>

<p>One comma, an entirely different meaning. Punctuation is not decoration: it tells your reader
where to pause, what belongs together, and what your sentence actually means. And it is one of
the easiest places to gain marks in written work.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The five jobs of the <b>comma</b></li>
    <li>The <b>comma splice</b> — the most common punctuation error in essays</li>
    <li>What a <b>colon</b> and a <b>semicolon</b> actually do</li>
    <li>The apostrophe rules, gathered in one place</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Three levels of pause</span>
  <span class="pe-chip pe-chip--s">, comma</span>
  <span class="pe-op">&lt;</span>
  <span class="pe-chip pe-chip--v">; semicolon</span>
  <span class="pe-op">&lt;</span>
  <span class="pe-chip pe-chip--o">. full stop</span>
</div>

LEGEND_HERE

<h3>1. The five jobs of the comma</h3>

<ol class="pe-steps">
  <li><b>In lists:</b> <em>I bought bread, milk, eggs and cheese.</em> (British English usually
      has no comma before the final <em>and</em>.)</li>
  <li><b>After an introductory phrase or clause:</b> <em>After the lesson<b>,</b> we went home.</em>
      · <em>Although it rained<b>,</b> we walked.</em> (PE-52)</li>
  <li><b>Before <em>but</em>, <em>so</em>, <em>and</em></b> when they join two full sentences:
      <em>It was late<b>,</b> so we left.</em></li>
  <li><b>Around extra information:</b> <em>Afsona<b>,</b> who lives next door<b>,</b> is a
      nurse.</em> (PE-59)</li>
  <li><b>When speaking to somebody:</b> <em>Thank you<b>,</b> Jasur.</em> · <em>Sherbek<b>,</b>
      come here.</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en"><b>However,</b> the plan failed. — <b>First of all,</b> let me explain.
     — <b>In my opinion,</b> he was right.</p>
  <p class="pe-ex__uz">Biroq, reja amalga oshmadi. — Avvalo, tushuntirib beraman. — Menimcha,
     u haq edi.</p>
  <p class="pe-ex__why">Linking words at the start of a sentence always take a comma after
     them.</p>
</div>

<h3>2. The comma splice — the error to avoid</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  A comma <b>cannot</b> join two complete sentences on its own. You need a full stop, a
  semicolon, or a joining word.
</div>

<div class="pe-fix">
  <p class="pe-bad"><s>It was raining, we stayed at home.</s></p>
  <p class="pe-good">It was raining<b>.</b> We stayed at home.</p>
  <p class="pe-good">It was raining<b>, so</b> we stayed at home.</p>
  <p class="pe-good">It was raining<b>;</b> we stayed at home.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu xato oʻzbek tilidan kelib chiqadi: oʻzbekchada "Yomgʻir yogʻdi, biz uyda qoldik" —
  vergul bilan bogʻlash mumkin. Ingliz tilida esa <b>ikki toʻliq gapni faqat vergul bilan
  bogʻlab boʻlmaydi</b>. Yo nuqta qoʻying, yo bogʻlovchi (<em>so, and, but</em>) qoʻshing,
  yo nuqtali vergul ishlating. Bu — inshoda eng koʻp uchraydigan tinish belgisi xatosi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Insho yozganda eslab qoling: <b>bogʻlovchi soʻzlardan keyin vergul</b> qoʻyiladi —
  <em>However<b>,</b></em> · <em>Therefore<b>,</b></em> · <em>In addition<b>,</b></em> ·
  <em>For example<b>,</b></em> · <em>In my opinion<b>,</b></em>. Oʻzbekchada ham "Biroq,",
  "Shuning uchun," deb vergul qoʻyamiz — demak bu qoida sizga tanish. Bu — inshoda eng
  oson qoʻlga kiritiladigan ballardan biri.
</div>

<h3>3. The colon and the semicolon</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Colon : — "here it comes"</p>
    <ul>
      <li>Introduces a <b>list</b>: <em>I need three things: bread, milk and tea.</em></li>
      <li>Introduces an <b>explanation</b>: <em>He failed for one reason: he never
          studied.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Semicolon ; — a strong comma</p>
    <ul>
      <li>Joins two <b>related</b> sentences: <em>She studied hard; she passed easily.</em></li>
      <li>Before <em>however, therefore</em>: <em>It rained; however, we went.</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The recipe is simple<b>:</b> rice, meat, carrots and oil. Cook it
     slowly<b>;</b> that is the secret.</p>
  <p class="pe-ex__uz">Retsept oddiy: guruch, goʻsht, sabzi va yogʻ. Sekin pishiring — mana shu
     sir.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  If you are unsure about the semicolon, use a <b>full stop</b> instead. Two short correct
  sentences always score better than one long sentence with the punctuation guessed.
</div>

<h3>4. The apostrophe, gathered in one place</h3>

<p>Two jobs only (PE-75):</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Possession</p>
    <p><em>the boy's book · the boys' books · the children's toys</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Missing letters</p>
    <p><em>don't, it's, I'm, we'll, she'd</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Never for plurals</p>
    <p><s>two book's</s> ✗ → <em>two books</em> ✓</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Never on possessives</p>
    <p><s>it's tail, your's</s> ✗ → <em>its tail, yours</em> ✓</p>
  </div>
</div>

<h3>5. Direct speech</h3>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona said<b>, "</b>I'll be late<b>."</b> — <b>"</b>Where are you
     going<b>?"</b> he asked.</p>
  <p class="pe-ex__uz">Afsona: "Kechikaman," dedi. — "Qayerga ketyapsan?" — deb soʻradi u.</p>
  <p class="pe-ex__why">The comma comes <b>before</b> the quotation marks open, and the final
     punctuation goes <b>inside</b> them.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Koʻchirma gapda farq bor: oʻzbekchada tire (—) va "dedi" ishlatiladi, ingliz tilida esa
  <b>qoʻshtirnoq</b> va vergul: <em>She said<b>,</b> <b>"</b>I'm tired.<b>"</b></em>
  Eʼtibor bering — nuqta <b>qoʻshtirnoq ichida</b> qoladi, tashqarisida emas.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I like tea he likes coffee.</s></p>
  <p class="pe-good">I like tea<b>, but</b> he likes coffee.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>However the weather was bad.</s></p>
  <p class="pe-good"><b>However,</b> the weather was bad.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My mother who is a doctor works here.</s></p>
  <p class="pe-good">My mother<b>,</b> who is a doctor<b>,</b> works here.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We need: bread and milk.</s></p>
  <p class="pe-good">We need <b>bread and milk.</b> / We need three things<b>:</b> bread, milk
     and tea.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She asked "are you ready"?</s></p>
  <p class="pe-good">She asked<b>, "</b>Are you ready<b>?"</b></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Punctuate: <em>after the lesson we went to the library and borrowed three books</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>After the lesson, we went to the library and borrowed three books.</strong></p>
      <p>Comma after the introductory phrase; no comma before <em>and</em> here because it
         joins two verbs, not two sentences.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Fix the comma splice: <em>I was tired, I went to bed early.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I was tired, so I went to bed early.</strong> (or a full stop, or a
         semicolon)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Colon or semicolon? <em>He gave one excuse ___ he had overslept.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>A colon</strong> — the second part explains the first. A semicolon would work
         too, but the colon points forward more clearly.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Add commas: <em>Bukhara which is an ancient city attracts many tourists.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Bukhara, which is an ancient city, attracts many tourists.</strong></p>
      <p>Extra information about a unique name → commas (PE-59).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What is wrong? <em>The teacher's are waiting in the staff room.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The teachers are waiting…</strong> An apostrophe never makes a plural.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Punctuation</b><span>tinish belgilari</span></li>
  <li><b>Comma</b><span>vergul</span></li>
  <li><b>Full stop</b><span>nuqta</span></li>
  <li><b>Semicolon</b><span>nuqtali vergul</span></li>
  <li><b>Colon</b><span>ikki nuqta</span></li>
  <li><b>Apostrophe</b><span>apostrof</span></li>
  <li><b>Quotation marks</b><span>qoʻshtirnoq</span></li>
  <li><b>Comma splice</b><span>vergul xatosi</span></li>
  <li><b>To pause</b><span>toʻxtalmoq</span></li>
  <li><b>To oversleep</b><span>uxlab qolmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Comma: lists · after an opening phrase · before <b>but/so</b> joining sentences ·
        around extra information · before a name.</li>
    <li><b>Never join two sentences with only a comma.</b></li>
    <li><b>Colon</b> introduces; <b>semicolon</b> joins two related sentences.</li>
    <li>Apostrophe = possession or missing letters — <b>never</b> a plural.</li>
    <li>In direct speech, the final punctuation goes <b>inside</b> the quotation marks.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-82: Capital Letters and Spelling Rules",
        "category": "english",
        "order": 82,
        "summary": (
            "Where English uses capitals that Uzbek doesn't, the spelling rules worth knowing, "
            "and the twenty words learners misspell most."
        ),
        "content": """
<h2>PE-82: Capital Letters and Spelling Rules</h2>

<p>English capitalises far more than Uzbek does. In Uzbek you write <em>ingliz tili</em> with a
small letter; in English it is <b>English</b> — always. And there is one word that takes a
capital everywhere it appears, in the middle of a sentence or anywhere else: the pronoun
<b>I</b>. These details are small, but they are exactly what a reader notices first.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Everything English capitalises — and the things it doesn't</li>
    <li>The spelling rules you have met, gathered in one place</li>
    <li>Twenty words that learners misspell most often</li>
    <li>British vs American spelling</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The unbreakable one</span>
  <span class="pe-chip pe-chip--s">I</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">always a capital letter</span>
</div>

LEGEND_HERE

<h3>1. What takes a capital letter</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Category</th><th>Examples</th></tr>
  <tr><td>the pronoun <b>I</b></td><td>Yesterday <b>I</b> saw him.</td></tr>
  <tr><td>names of people</td><td>Afsona, Jasur Karimov</td></tr>
  <tr><td>places</td><td>Tashkent, Uzbekistan, Navoi Street</td></tr>
  <tr><td><b>nationalities &amp; languages</b></td><td><b>U</b>zbek, <b>E</b>nglish, <b>K</b>orean</td></tr>
  <tr><td>days &amp; months</td><td><b>M</b>onday, <b>S</b>eptember</td></tr>
  <tr><td>holidays</td><td><b>N</b>avruz, <b>N</b>ew <b>Y</b>ear</td></tr>
  <tr><td>titles before names</td><td><b>M</b>r Karimov, <b>D</b>r Ahmedova</td></tr>
  <tr><td>book &amp; film titles</td><td><b>T</b>he <b>L</b>ittle <b>P</b>rince</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">On <b>Monday</b> <b>I</b> have an <b>English</b> lesson, and in
     <b>March</b> we celebrate <b>Navruz</b>.</p>
  <p class="pe-ex__uz">Dushanba kuni ingliz tili darsim bor, martda esa Navruzni
     nishonlaymiz.</p>
  <p class="pe-ex__why">Compare the Uzbek line — <em>dushanba</em>, <em>ingliz</em>,
     <em>mart</em> are all lower case there.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu asosiy farq: oʻzbek tilida <b>millat, til, oy va hafta kunlari kichik harf</b>
  bilan yoziladi — <em>ingliz tili</em>, <em>dushanba</em>, <em>mart</em>. Ingliz tilida esa
  ularning hammasi <b>bosh harf</b> bilan: <em>English</em>, <em>Monday</em>,
  <em>March</em>. Va <b>I</b> — har doim bosh harf, gap oʻrtasida ham.
</div>

<h3>2. What does NOT take a capital</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✗ Lower case in English</p>
    <ul>
      <li>seasons: <em>summer, winter</em></li>
      <li>school subjects: <em>maths, history, biology</em></li>
      <li>directions: <em>north, south-east</em></li>
      <li>family words alone: <em>my mother, his uncle</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✓ But capital when…</p>
    <ul>
      <li>the subject is a language: <em>English, Russian</em></li>
      <li>a direction is a region: <em>the Middle East</em></li>
      <li>a family word replaces a name: <em>Thanks, Mum!</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">In <b>winter</b> I study <b>maths</b> and <b>English</b>; my
     <b>mother</b> teaches <b>history</b> in the <b>north</b> of the country.</p>
  <p class="pe-ex__uz">Qishda matematika va ingliz tilini oʻqiyman; onam mamlakatning
     shimolida tarixdan dars beradi.</p>
  <p class="pe-ex__why">Only <em>English</em> takes a capital — it is a language. Season,
     subjects, family words and directions stay lower case.</p>
</div>

<h3>3. The spelling rules, gathered</h3>

<ol class="pe-steps">
  <li><b>Doubling:</b> short verb, one vowel + one consonant → double it before <b>-ing</b> or
      <b>-ed</b>: <em>stop → stopped, sit → sitting, plan → planned</em>. (PE-12, PE-20)</li>
  <li><b>Consonant + y → i:</b> <em>study → studies/studied, happy → happier, easy →
      easily</em>. Vowel + y keeps the y: <em>play → played</em>. (PE-3, PE-9)</li>
  <li><b>Drop the silent e</b> before a vowel ending: <em>make → making, nice → nicer, use →
      using</em>. Keep it before a consonant ending: <em>nice → nicely</em>.</li>
  <li><b>-ful and -fully:</b> the adjective has <b>one</b> l (<em>careful</em>), the adverb has
      <b>two</b> (<em>carefully</em>).</li>
  <li><b>i before e</b> after most letters (<em>believe, friend, piece</em>) but <b>e before
      i</b> after c (<em>receive, ceiling</em>).</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">He <b>studied</b> <b>carefully</b>, <b>believed</b> in himself and
     <b>received</b> the best mark.</p>
  <p class="pe-ex__uz">U sinchkovlik bilan oʻqidi, oʻziga ishondi va eng yaxshi bahoni oldi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikki qoida bir-biriga qarama-qarshi tuyuladi, shuning uchun ularni yonma-yon eslang:
  <em>write → writ<b>ing</b></em> (oxiridagi <b>e</b> tushadi, <b>t</b> ikkilanmaydi),
  lekin <em>sit → si<b>tt</b>ing</em> (<b>t</b> ikkilanadi, chunki qisqa unli bor).
  Farq: <em>write</em> da uzun unli va oxirida <b>e</b> bor, <em>sit</em> da esa yoʻq.
</div>

<h3>4. The twenty words learners misspell most</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>✓ Correct</th><th>✗ Common error</th><th>✓ Correct</th><th>✗ Common error</th></tr>
  <tr><td>because</td><td>becouse</td><td>beautiful</td><td>beatiful</td></tr>
  <tr><td>necessary</td><td>neccessary</td><td>definitely</td><td>definately</td></tr>
  <tr><td>receive</td><td>recieve</td><td>believe</td><td>beleive</td></tr>
  <tr><td>tomorrow</td><td>tommorow</td><td>which</td><td>wich</td></tr>
  <tr><td>friend</td><td>freind</td><td>government</td><td>goverment</td></tr>
  <tr><td>business</td><td>bussiness</td><td>restaurant</td><td>restourant</td></tr>
  <tr><td>interesting</td><td>intresting</td><td>different</td><td>diffrent</td></tr>
  <tr><td>a lot</td><td>alot</td><td>usually</td><td>usualy</td></tr>
  <tr><td>writing</td><td>writting</td><td>foreign</td><td>foriegn</td></tr>
  <tr><td>surprise</td><td>suprise</td><td>Wednesday</td><td>Wenesday</td></tr>
</table>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Keep a personal list of <b>your own</b> five worst spellings and revise only those. A general
  list of a hundred words is useless; five words you actually get wrong will fix themselves in
  a week.
</div>

<h3>5. British or American?</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>British</th><th>American</th></tr>
  <tr><td>colour, favourite, neighbour</td><td>color, favorite, neighbor</td></tr>
  <tr><td>centre, theatre, metre</td><td>center, theater, meter</td></tr>
  <tr><td>organise, realise</td><td>organize, realize</td></tr>
  <tr><td>travelled, cancelled</td><td>traveled, canceled</td></tr>
  <tr><td>practise (verb)</td><td>practice (both)</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkalasi ham <b>toʻgʻri</b> — faqat izchil boʻlish kerak. Bitta insho ichida
  <em>colour</em> va <em>color</em> ni aralashtirmang. Oʻzbekistonda maktab va imtihonlarda
  odatda <b>Britaniya</b> varianti oʻrgatiladi (IELTS ham ikkalasini qabul qiladi),
  shuning uchun <em>colour, centre, organise</em> ni tanlang va oxirigacha shu tizimda
  qoling.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>i study english on mondays.</s></p>
  <p class="pe-good"><b>I</b> study <b>E</b>nglish on <b>M</b>ondays.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>In Summer we go to the village.</s></p>
  <p class="pe-good">In <b>summer</b> we go to the village. <em>(seasons are lower case)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She is an Uzbek and speaks uzbek and Russian.</s></p>
  <p class="pe-good">She is <b>Uzbek</b> and speaks <b>Uzbek</b> and <b>Russian</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I have alot of homework.</s></p>
  <p class="pe-good">I have <b>a lot of</b> homework. <em>(two words)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He is writting a letter.</s></p>
  <p class="pe-good">He is <b>writing</b> a letter. <em>(drop the e, don't double the t)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Add capitals: <em>next tuesday i have a maths test and an english test.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Next Tuesday I have a maths test and an English test.</strong></p>
      <p><em>Maths</em> stays lower case, but <em>English</em> is a language — capital.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Spell correctly: <em>becouse · beatiful · definately · recieve</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>because · beautiful · definitely · receive.</strong></p>
      <p><em>Receive</em> follows the "e before i after c" rule.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Add the ending: <em>stop + ing · study + ed · make + ing · care + fully</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>stopping · studied · making · carefully.</strong></p>
      <p>Double, y → i, drop the e, and two l's in the adverb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which is British? <em>colour / color · center / centre</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>colour and centre are British</strong>; <em>color</em> and <em>center</em> are
         American. Both are correct — just be consistent.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>my Mother speaks three Languages and loves History.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My mother speaks three languages and loves history.</strong></p>
      <p>Only the first word takes a capital — <em>mother</em>, <em>languages</em> and
         <em>history</em> are ordinary nouns.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Capital letter</b><span>bosh harf</span></li>
  <li><b>Lower case</b><span>kichik harf</span></li>
  <li><b>Spelling</b><span>imlo</span></li>
  <li><b>Nationality</b><span>millat</span></li>
  <li><b>Title (Mr, Dr)</b><span>murojaat shakli</span></li>
  <li><b>Season</b><span>fasl</span></li>
  <li><b>Consistent</b><span>izchil</span></li>
  <li><b>To misspell</b><span>xato yozmoq</span></li>
  <li><b>To celebrate</b><span>nishonlamoq</span></li>
  <li><b>Foreign</b><span>chet, xorijiy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>I</b> is always a capital letter, anywhere in a sentence.</li>
    <li>Capitals for <b>nationalities, languages, days, months</b> — unlike Uzbek.</li>
    <li><b>No</b> capitals for seasons, school subjects (except languages), or directions.</li>
    <li>Spelling: double the consonant · y → i · drop the silent e · <b>-fully</b> has two l's.</li>
    <li>British or American — either is fine, but be <b>consistent</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-83: Emphasis with do, does, did",
        "category": "english",
        "order": 83,
        "summary": (
            "I DID tell you! How English uses its helper verb in a positive sentence to insist, "
            "contradict and add warmth."
        ),
        "content": """
<h2>PE-83: Emphasis with do, does, did</h2>

<p>Somebody says you never told them about the exam. You reply: <em>"I <b>did</b> tell you!"</em>
That extra word is not a mistake and not a question — it is <mark>emphasis</mark>. English uses
its helper verb in a <b>positive</b> sentence to insist, to contradict, and even to sound warmer
when inviting somebody. It is one of the simplest ways to make your English sound
sophisticated.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>do / does / did + base verb</b> in positive sentences</li>
    <li>Four situations where you need it</li>
    <li>How to use it with imperatives to sound warm</li>
    <li>Other tools for emphasis: <b>really, actually, so, such</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Emphatic positive</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">do / does / did</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
</div>

LEGEND_HERE

<h3>1. The form is one you already know</h3>

<p>It is exactly the helper from PE-10 and PE-22 — but now in a positive sentence, and stressed
in speech. Notice that the main verb stays <b>bare</b>, following the same "one marker" rule.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Normal: <em>I told you.</em> — Emphatic: <em>I
     <span class="pe-hl pe-hl--aux">did</span>
     <span class="pe-hl pe-hl--v">tell</span> you!</em></p>
  <p class="pe-ex__uz">Senga aytdim. — Senga aytdim-ku!</p>
  <p class="pe-ex__why"><em>Did tell</em>, not <s>did told</s> — the past appears once only.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qurilma oʻzbekchadagi <b>-ku</b> yuklamasiga va "<b>-ku, aytdim!</b>",
  "<b>haqiqatan ham</b>", "<b>albatta</b>" kabi kuchaytiruvchi soʻzlarga toʻgʻri keladi:
  <em>I <b>did</b> tell you</em> = "Aytdim<b>-ku</b>!". Yaʼni ingliz tilida bu maʼno
  alohida soʻz bilan emas, <b>yordamchi feʼl</b> bilan beriladi.
</div>

<h3>2. The four situations</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Contradicting</p>
    <p>— You didn't lock the door.<br>— I <b>did</b> lock it!</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Insisting</p>
    <p><em>I <b>do</b> like her — I just don't agree with her.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Surprise / concession</p>
    <p><em>She <b>does</b> speak Korean well, doesn't she!</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Warm invitations</p>
    <p><em><b>Do</b> come in! <b>Do</b> sit down.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— Why didn't you study? — I <b>did</b> study! I studied for three hours.</p>
  <p class="pe-ex__uz">— Nega oʻqimadingiz? — Oʻqidim-ku! Uch soat oʻqidim.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek isn't very tall, but he <b>does</b> play basketball very well.</p>
  <p class="pe-ex__uz">Sherbek unchalik baland boʻyli emas, lekin basketbolni haqiqatan ham
     yaxshi oʻynaydi.</p>
  <p class="pe-ex__why">Here it admits one thing while insisting on another — very common in
     good writing.</p>
</div>

<h3>3. Do + imperative = warmth, not force</h3>

<p>A bare imperative can sound like an order. Adding <b>do</b> turns it into a friendly, almost
hospitable invitation — you will hear it constantly from a host.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Plain — could sound blunt</p>
    <ul>
      <li><em>Come in.</em></li>
      <li><em>Sit down.</em></li>
      <li><em>Have some tea.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">With do — warm and welcoming</p>
    <ul>
      <li><em><b>Do</b> come in!</em></li>
      <li><em><b>Do</b> sit down.</em></li>
      <li><em><b>Do</b> have some tea.</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Do come in!</b> — bu "kir!" degan buyruq emas, balki "<b>marhamat, kiring!</b>",
  "<b>qani, kiravering</b>" degan iliq taklif. Oʻzbek mehmondoʻstligidagi "qani-qani,
  oʻtiring" ohangiga juda oʻxshaydi. Mehmon kutayotganda bu ibora juda mos tushadi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda ham "<b>bitta belgi</b>" qoidasi ishlaydi (PE-22 ni eslang): oʻtganlikni
  <b>did</b> koʻrsatgani uchun asosiy feʼl asl shaklda qoladi — <em>did <b>tell</b></em>,
  <s>did told</s> emas. Xuddi shunday hozirgi zamonda: <em>does <b>like</b></em>,
  <s>does likes</s> emas. Yaʼni yordamchi feʼl bor joyda asosiy feʼl yalangʻoch.
</div>

<h3>4. Say it with your voice</h3>

<p>In speech, the emphasis lives in the <b>stress</b>. The helper is said loudly and slowly:
<em>"I <b>DID</b> tell you."</em> Without that stress the sentence sounds odd, so practise saying
it aloud, not just writing it.</p>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Use it sparingly. One emphatic <em>do</em> in a paragraph is powerful; four of them sound like
  an argument. And never use it in a sentence that already has another auxiliary:
  <s>I do have finished</s> ✗ → <b>I have finished</b> ✓.
</div>

<h3>5. Other ways to add emphasis</h3>

<ul>
  <li><b>really / actually:</b> <em>I <b>really</b> like it.</em> · <em>He <b>actually</b>
      apologised!</em></li>
  <li><b>so + adjective / such a + noun:</b> <em>It was <b>so</b> cold!</em> · <em>It was
      <b>such a</b> good film!</em></li>
  <li><b>at all</b> in negatives: <em>I don't like it <b>at all</b>.</em></li>
  <li><b>indeed</b> (formal): <em>That is <b>indeed</b> a problem.</em></li>
</ul>

<div class="pe-ex">
  <p class="pe-ex__en">It was <b>such a</b> long journey, and we were <b>so</b> tired that we
     <b>did</b> sleep for twelve hours.</p>
  <p class="pe-ex__uz">Shunday uzoq safar boʻldi va shunchalik charchadikki, oʻn ikki soat
     uxlab qoldik.</p>
  <p class="pe-ex__why">Remember: <b>so</b> + adjective, but <b>such a</b> + (adjective +)
     noun.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I do told you about it!</s></p>
  <p class="pe-good">I <b>did tell</b> you about it!</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She does likes him.</s></p>
  <p class="pe-good">She <b>does like</b> him.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I do am tired.</s></p>
  <p class="pe-good">I <b>am</b> tired. / I<b>'m really</b> tired.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It was so a good film.</s></p>
  <p class="pe-good">It was <b>such a</b> good film. / It was <b>so</b> good.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I did went there yesterday.</s></p>
  <p class="pe-good">I <b>did go</b> there yesterday.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Contradict this: <em>"You never help at home."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I do help at home!</strong> The helper carries the stress and the
         contradiction.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>She did finished her homework, I saw it.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She did finish her homework, I saw it.</strong></p>
      <p>After <em>did</em>, the verb returns to its base form — the same rule as in
         PE-22.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What does the <em>do</em> add here? <em>Do have another piece of cake!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Warmth and hospitality</strong> — it is an encouraging invitation, not an
         order.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     so or such: <em>It was ___ hot that we stayed inside. It was ___ a hot day.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>so hot … such a hot day.</strong> <em>So</em> goes with an adjective alone;
         <em>such a</em> goes with a noun phrase.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Add emphasis: <em>Afsona speaks Korean well.</em> (you are surprised)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona does speak Korean well!</strong> (or <em>Afsona really does speak
         Korean well!</em>)</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Emphasis</b><span>taʼkid, kuchaytirish</span></li>
  <li><b>To emphasise</b><span>taʼkidlamoq</span></li>
  <li><b>To contradict</b><span>rad etmoq, aksini aytmoq</span></li>
  <li><b>To insist</b><span>qatʼiy turmoq</span></li>
  <li><b>Stress (in speech)</b><span>urgʻu</span></li>
  <li><b>Concession</b><span>tan olish, yon berish</span></li>
  <li><b>Hospitable</b><span>mehmondoʻst</span></li>
  <li><b>Actually</b><span>aslida, haqiqatan</span></li>
  <li><b>Indeed</b><span>darhaqiqat</span></li>
  <li><b>At all</b><span>umuman</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>do / does / did + base verb</b> in a positive sentence = emphasis.</li>
    <li>The main verb stays <b>bare</b>: <em>did tell</em>, not <s>did told</s>.</li>
    <li>Four uses: contradicting, insisting, expressing surprise, warm invitations.</li>
    <li><b>Do come in!</b> = "marhamat, kiring" — hospitality, not an order.</li>
    <li>Also: <b>really, actually, so</b> + adjective, <b>such a</b> + noun.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-84: Inversion: Never have I seen ...",
        "category": "english",
        "order": 84,
        "summary": (
            "Putting the helper before the subject for dramatic effect — the structure that "
            "makes writing sound literary, and the exam favourite 'Had I known'."
        ),
        "content": """
<h2>PE-84: Inversion: Never have I seen ...</h2>

<p>Normal English: <em>"I have never seen such a beautiful city."</em> Dramatic English:
<em>"<b>Never have I seen</b> such a beautiful city."</em> The subject and the helper swap places
— just as they do in a question — and the sentence suddenly sounds literary and powerful. This is
<mark>inversion</mark>, and it is the mark of an advanced writer.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The rule: negative adverb first, then question word order</li>
    <li>The words that trigger it: <b>never, rarely, hardly, not only, no sooner</b></li>
    <li>Conditional inversion: <b>Had I known…</b></li>
    <li>When <b>not</b> to use it</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Inversion</span>
  <span class="pe-chip pe-chip--neg">negative adverb</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">helper</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
</div>

LEGEND_HERE

<h3>1. The rule in one move</h3>

<p>Take a negative or limiting adverb, move it to the <b>front</b> of the sentence, and then use
<b>question word order</b> for the rest.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I have <b>never</b> been so happy. →
     <span class="pe-hl pe-hl--neg">Never</span>
     <span class="pe-hl pe-hl--aux">have</span>
     <span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">been</span> so happy.</p>
  <p class="pe-ex__uz">Hech qachon bunchalik baxtli boʻlmaganman.</p>
  <p class="pe-ex__why">The word order is exactly that of a question — but it is a statement,
     so no question mark.</p>
</div>

<p>If there is no helper verb, one appears — <b>do / does / did</b>, exactly as in questions:</p>

<div class="pe-ex">
  <p class="pe-ex__en">She <b>rarely</b> speaks in class. → <b>Rarely does she speak</b> in
     class.</p>
  <p class="pe-ex__uz">U darsda kamdan-kam gapiradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida taʼkid uchun soʻz tartibini oʻzgartirish tabiiy: "<b>Hech qachon</b>
  bunchalik chiroyli shaharni koʻrmaganman". Ingliz tilida ham shunday, lekin bitta
  qoʻshimcha shart bor: inkor soʻz oldinga chiqqanda <b>yordamchi feʼl ham egadan oldin
  keladi</b> — yaʼni gap savol tartibiga oʻtadi.
</div>

<h3>2. The trigger words</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Trigger</th><th>Example</th></tr>
  <tr><td><b>Never</b></td><td><b>Never</b> have I heard such nonsense.</td></tr>
  <tr><td><b>Rarely / Seldom</b></td><td><b>Seldom</b> do we see such talent.</td></tr>
  <tr><td><b>Hardly ever</b></td><td><b>Hardly ever</b> does he complain.</td></tr>
  <tr><td><b>Little</b></td><td><b>Little</b> did I know what would happen.</td></tr>
  <tr><td><b>Not only … but also</b></td><td><b>Not only did she</b> pass, but she also came first.</td></tr>
  <tr><td><b>No sooner … than</b></td><td><b>No sooner had</b> we arrived <b>than</b> it rained.</td></tr>
  <tr><td><b>Hardly … when</b></td><td><b>Hardly had</b> I sat down <b>when</b> the phone rang.</td></tr>
  <tr><td><b>Under no circumstances</b></td><td><b>Under no circumstances should you</b> open it.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Not only did</b> Afsona win the olympiad, <b>but she also</b> got the
     highest mark in the school.</p>
  <p class="pe-ex__uz">Afsona nafaqat olimpiadada gʻolib boʻldi, balki maktabda eng yuqori
     bahoni ham oldi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Note the pairs carefully: <b>no sooner … than</b> (not <em>when</em>) and
  <b>hardly … when</b> (not <em>than</em>). Exams test exactly this.
</div>

<h3>3. Conditional inversion — the exam favourite</h3>

<p>Here is the most useful one for writing. You can drop the <em>if</em> from a conditional and
invert instead. It sounds more formal and slightly more elegant.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">With if</p>
    <ul>
      <li><b>If I had known</b>, I would have come.</li>
      <li><b>If you should need</b> help, call me.</li>
      <li><b>If I were</b> you, I'd wait.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Inverted — no if</p>
    <ul>
      <li><b>Had I known</b>, I would have come.</li>
      <li><b>Should you need</b> help, call me.</li>
      <li><b>Were I</b> you, I'd wait.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Had I studied</b> harder, I would have passed. — <b>Should you have</b>
     any questions, please ask.</p>
  <p class="pe-ex__uz">Qattiqroq oʻqiganimda, imtihondan oʻtgan boʻlardim. — Savollaringiz
     boʻlsa, soʻrashingiz mumkin.</p>
  <p class="pe-ex__why">Only <b>had, should</b> and <b>were</b> can do this — and the
     <em>if</em> disappears completely.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Had I known…</b> — bu <em>If I had known…</em> ning rasmiy shakli va maʼnosi
  bir xil: "Bilganimda edi...". Rasmiy xat va inshoda juda chiroyli eshitiladi, ammo
  <b>if</b> ni ham qoʻshib yubormang: <s>If had I known</s> ✗ — faqat bittasi boʻladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uslub haqida ogohlantirish: inversiya — <b>rasmiy va adabiy</b> shakl. Insho, rasmiy xat
  yoki hikoyada bir marta ishlatilsa, juda chiroyli chiqadi. Ammo doʻstingizga
  <em>"Never have I eaten such good plov"</em> desangiz, teatrdagidek gʻalati eshitiladi.
  Oddiy suhbatda <em>"I've never eaten such good plov"</em> deng.
</div>

<h3>4. Two friendly inversions</h3>

<p>Not all inversion is formal. These two are everyday spoken English, and here the
<b>full verb</b> moves, not a helper:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Here comes</b> the bus! — <b>There goes</b> my brother. — On the
     wall <b>hung</b> an old photograph.</p>
  <p class="pe-ex__uz">Mana avtobus keldi! — Anavi akam ketyapti. — Devorda eski surat osilgan
     edi.</p>
  <p class="pe-ex__why">But with a pronoun there is no inversion: <em>Here <b>it</b> comes!</em>,
     not <s>Here comes it</s>.</p>
</div>

<h3>5. When not to use it</h3>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Inversion is a <b>spice, not a meal</b>. One inverted sentence in an essay is impressive;
  four is exhausting to read. Keep it for your strongest point, and never use it in casual
  conversation — <em>"Never have I eaten such good plov"</em> to a friend sounds theatrical.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Never I have seen such a thing.</s></p>
  <p class="pe-good"><b>Never have I seen</b> such a thing.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Rarely she goes out.</s></p>
  <p class="pe-good"><b>Rarely does she go</b> out.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Not only she sang, but she danced.</s></p>
  <p class="pe-good"><b>Not only did she sing</b>, but she <b>also</b> danced.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If had I known, I would have called.</s></p>
  <p class="pe-good"><b>Had I known</b>, I would have called.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>No sooner we arrived when it started raining.</s></p>
  <p class="pe-good"><b>No sooner had we arrived than</b> it started raining.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Invert: <em>I have never eaten such delicious plov.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Never have I eaten such delicious plov.</strong></p>
      <p><em>Never</em> first, then helper + subject + verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Invert: <em>She seldom asks for help.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Seldom does she ask for help.</strong></p>
      <p>No helper in the original, so <em>does</em> appears — and the verb goes bare.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Remove the <em>if</em>: <em>If I had left earlier, I wouldn't have missed the bus.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Had I left earlier, I wouldn't have missed the bus.</strong></p>
      <p><em>Had</em> moves to the front and <em>if</em> disappears entirely.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     than or when: <em>No sooner had we sat down ___ the film started.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>than</strong> — <em>no sooner</em> always pairs with <em>than</em>;
         <em>hardly</em> pairs with <em>when</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>Here comes it!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Here it comes!</strong> With a pronoun subject there is no inversion after
         <em>here</em> or <em>there</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Inversion</b><span>soʻz tartibini almashtirish</span></li>
  <li><b>Dramatic</b><span>taʼsirchan</span></li>
  <li><b>Literary</b><span>adabiy</span></li>
  <li><b>Seldom / rarely</b><span>kamdan-kam</span></li>
  <li><b>Hardly</b><span>deyarli emas</span></li>
  <li><b>No sooner … than</b><span>...zahoti</span></li>
  <li><b>Not only … but also</b><span>nafaqat ... balki</span></li>
  <li><b>Under no circumstances</b><span>hech qanday holatda</span></li>
  <li><b>Nonsense</b><span>bemaʼnilik</span></li>
  <li><b>Formal register</b><span>rasmiy uslub</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Negative adverb first → then <b>question word order</b> (but no question mark).</li>
    <li>If there is no helper, <b>do / does / did</b> appears and the verb goes bare.</li>
    <li>Triggers: <b>never, seldom, rarely, hardly, little, not only, no sooner</b>.</li>
    <li><b>Had I known / Should you need / Were I you</b> — conditionals without <em>if</em>.</li>
    <li>Use it <b>sparingly</b> — one per essay, never in casual speech.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-85: Cleft Sentences: It was ... / What I need is ...",
        "category": "english",
        "order": 85,
        "summary": (
            "How to put a spotlight on exactly the word you mean — splitting one sentence into "
            "two to correct, contrast or emphasise."
        ),
        "content": """
<h2>PE-85: Cleft Sentences: It was ... / What I need is ...</h2>

<p>In Uzbek you can emphasise a word by moving it, or by adding <em>aynan</em>. English word order
is too strict for that (PE-72), so it does something clever instead: it <b>splits the sentence
in two</b> and puts a spotlight on one part. <em>"Jasur broke the window"</em> becomes
<em>"<b>It was Jasur who</b> broke the window."</em> These are <mark>cleft sentences</mark> —
"cleft" simply means split.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>It is / It was … who / that …</b> — spotlighting a person or thing</li>
    <li><b>What … is …</b> — spotlighting an action or a need</li>
    <li>Other openers: <em>All I want…</em>, <em>The reason why…</em></li>
    <li>How clefts are used to <b>correct</b> somebody politely</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The it-cleft</span>
  <span class="pe-chip pe-chip--s">It is / was</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">the spotlight</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">who / that</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">the rest</span>
</div>

LEGEND_HERE

<h3>1. The it-cleft: spotlighting a person or thing</h3>

<p>Start with <b>It is</b> or <b>It was</b>, put the important word next, then continue with
<b>who</b> (people) or <b>that</b> (things).</p>

<div class="pe-ex">
  <p class="pe-ex__en">Plain: <em>Afsona won the prize.</em><br>
     Spotlight on her: <em><b>It was Afsona who</b> won the prize.</em><br>
     Spotlight on the prize: <em><b>It was the prize that</b> Afsona won.</em></p>
  <p class="pe-ex__uz">Sovrinni Afsona oldi. — Sovrinni <b>aynan Afsona</b> oldi. — Afsona
     <b>aynan sovrinni</b> oldi.</p>
  <p class="pe-ex__why">One fact, three versions — each one points at something different.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada taʼkidni <b>"aynan"</b> soʻzi yoki soʻz tartibi bilan beramiz: "Derazani
  <b>aynan Jasur</b> sindirdi". Ingliz tilida soʻz tartibi qatʼiy boʻlgani uchun boshqa
  yoʻl tanlanadi — gap <b>ikkiga boʻlinadi</b>: <em>It was Jasur who broke it</em>.
  Yaʼni "aynan" ning ingliz tilidagi ekvivalenti — mana shu qurilma.
</div>

<h3>2. Correcting somebody politely</h3>

<p>This is where clefts earn their keep in real conversation. They let you correct a mistake
without sounding rude.</p>

<div class="pe-ex">
  <p class="pe-ex__en">— You broke the window! — <b>It wasn't me who</b> broke it — <b>it was
     the wind that</b> did it.</p>
  <p class="pe-ex__uz">— Derazani sen sindirdingmi! — Uni men sindirganim yoʻq — aynan shamol
     sindirdi.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>It was in 2019 that</b> we moved here, not 2018.</p>
  <p class="pe-ex__uz">Biz bu yerga 2018-yilda emas, aynan 2019-yilda koʻchib kelganmiz.</p>
  <p class="pe-ex__why">The spotlight can also fall on a <b>time</b> or a <b>place</b>.</p>
</div>

<h3>3. The what-cleft: spotlighting an action or a need</h3>

<p>Begin with <b>What</b> and finish with <b>is</b> or <b>was</b>. This one is extremely common in
speech, and it makes your point sound considered.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Plain: <em>I need a holiday.</em> → <em><b>What I need is</b> a
     holiday.</em><br>
     Plain: <em>She said something strange.</em> → <em><b>What she said was</b> strange.</em></p>
  <p class="pe-ex__uz">Menga dam olish kerak. → Menga <b>aynan</b> dam olish kerak. — U
     gʻalati narsa aytdi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Common what-openers</p>
    <ul>
      <li><b>What I want is</b> …</li>
      <li><b>What happened was</b> …</li>
      <li><b>What I don't understand is</b> …</li>
      <li><b>What she did was</b> (to) call the police.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Other useful openers</p>
    <ul>
      <li><b>All I want is</b> a quiet evening.</li>
      <li><b>The reason why</b> I came is …</li>
      <li><b>The person who</b> helped me was …</li>
      <li><b>The place where</b> we met was …</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>All I want is</b> to pass this exam. <b>The reason why</b> I study at
     night <b>is that</b> the house is quiet.</p>
  <p class="pe-ex__uz">Men xohlagan yagona narsa — bu imtihondan oʻtish. Kechasi oʻqishimning
     sababi — uyning jimjitligi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>What I need is…</b> qurilmasi oʻzbekchadagi "<b>Menga kerak boʻlgan narsa — bu ...</b>"
  yoki "<b>Men xohlaganim — ...</b>" tuzilmasiga toʻgʻri keladi. Suhbatda bu ibora
  fikringizni <b>tartibli va ishonchli</b> qilib koʻrsatadi, shuning uchun ogʻzaki
  imtihonlarda juda foydali.
</div>

<h3>4. The verb agreement detail</h3>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  In a <em>what</em>-cleft, the verb after <em>What…</em> is <b>singular</b>, because the whole
  clause counts as one idea: <em>What I need <b>is</b> two more days</em> ✓ — even though
  <em>two days</em> is plural.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bitta koʻp uchraydigan xatoni yodda tuting: <b>all</b> dan keyin <b>what</b>
  qoʻyilmaydi. Oʻzbekchada "men xohlagan <b>hamma narsa</b>" deymiz, shuning uchun
  <s>All what I want</s> deb yozib qoʻyish oson. Toʻgʻrisi — <b>All I want is…</b>
  (<em>what</em> siz). Faqat <em>What I want is…</em> shaklida <b>what</b> boshida keladi.
</div>

<h3>5. Don't overdo it</h3>

<p>Like inversion (PE-84), clefts are for the sentence that matters. Used once, a cleft makes
your reader stop and notice. Used in every paragraph, it becomes a habit that slows the writing
down.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Plain and good: <em>We must protect the Aral Sea.</em><br>
     Emphatic, for your key point: <em><b>What we must do is</b> protect the Aral Sea.</em></p>
  <p class="pe-ex__uz">Orol dengizini asrashimiz kerak. — Biz qilishimiz kerak boʻlgan narsa —
     Orol dengizini asrash.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>It was Jasur which broke the window.</s></p>
  <p class="pe-good">It was Jasur <b>who</b> broke the window.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>What I need are two more days.</s></p>
  <p class="pe-good">What I need <b>is</b> two more days.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Was Afsona who called you.</s></p>
  <p class="pe-good"><b>It was</b> Afsona who called you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The reason why I'm late is because of the traffic was bad.</s></p>
  <p class="pe-good">The reason why I'm late <b>is that</b> the traffic was bad.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>All what I want is a cup of tea.</s></p>
  <p class="pe-good"><b>All I want is</b> a cup of tea.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Spotlight <em>Sherbek</em>: <em>Sherbek found the keys.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It was Sherbek who found the keys.</strong></p>
      <p><em>Who</em> because the spotlight is on a person.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Rewrite with <em>What</em>: <em>I want a new bicycle.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>What I want is a new bicycle.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct somebody politely: <em>"You told the teacher!"</em> (it was your brother)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It wasn't me who told the teacher — it was my brother.</strong></p>
      <p>A cleft lets you deny and correct in the same breath, without sounding aggressive.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     is or are: <em>What we need <span class="pe-blank">?</span> more chairs.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — the subject is the whole clause <em>What we need</em>, which
         counts as one singular idea.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Correct it: <em>All what I want is to sleep.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>All I want is to sleep.</strong> After <em>all</em> there is no
         <em>what</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Cleft sentence</b><span>boʻlingan gap</span></li>
  <li><b>To split</b><span>boʻlmoq, ajratmoq</span></li>
  <li><b>Spotlight</b><span>diqqat markazi</span></li>
  <li><b>To emphasise</b><span>taʼkidlamoq</span></li>
  <li><b>To correct</b><span>toʻgʻrilamoq</span></li>
  <li><b>The reason why</b><span>...ning sababi</span></li>
  <li><b>All I want</b><span>men xohlagan yagona narsa</span></li>
  <li><b>To deny</b><span>rad etmoq</span></li>
  <li><b>To protect</b><span>asramoq</span></li>
  <li><b>Considered</b><span>oʻylangan, puxta</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>It is / was + spotlight + who / that + rest</b> — for people, things, times, places.</li>
    <li><b>What … is / was …</b> — for actions and needs.</li>
    <li>Also: <b>All I want is…</b>, <b>The reason why … is that…</b></li>
    <li>The verb after <b>What…</b> is <b>singular</b>.</li>
    <li>Clefts are perfect for <b>correcting politely</b> — and best used sparingly.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
