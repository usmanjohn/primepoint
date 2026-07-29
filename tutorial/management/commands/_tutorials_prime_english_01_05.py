# -*- coding: utf-8 -*-
"""Prime English — Block A, lessons 1–5 (Foundations).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_01_05.py --author=prime
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
        "title": "PE-1: What Is a Sentence? Subject + Verb",
        "category": "english",
        "order": 1,
        "summary": (
            "Build correct English sentences from day one: find the subject, find the verb, "
            "and put them in English word order — which is not Uzbek word order."
        ),
        "content": """
<h2>PE-1: What Is a Sentence? Subject + Verb</h2>

<p>You already know a lot of English words. But a pile of words is not a sentence —
<em>school · Afsona · to · goes</em> means nothing until you put those words in the right
places. English is strict about places. Learn that today, and every other lesson in Prime
English becomes easier.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What a subject and a verb are, and how to find them in any sentence</li>
    <li>The English word order that never changes: <b>S – V – O</b></li>
    <li>Why English always needs a subject, even when Uzbek does not</li>
    <li>How to spot a broken sentence and repair it</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The English sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">Verb</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">Object</span>
  <span class="pe-chip pe-chip--opt">(place)</span>
  <span class="pe-chip pe-chip--opt">(time)</span>
</div>

LEGEND_HERE

<h3>1. The subject — who or what does it?</h3>

<p>The <mark>subject</mark> is the person or thing the sentence is about — the one doing the
action. To find it, ask the verb: <em>Who? What?</em></p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Jasur</span>
     <span class="pe-hl pe-hl--v">plays</span>
     <span class="pe-hl pe-hl--o">football</span>.</p>
  <p class="pe-ex__uz">Jasur futbol oʻynaydi.</p>
  <p class="pe-ex__why">Who plays? → <b>Jasur</b>. That is the subject.</p>
</div>

<p>A subject can be one word or several words together: <em>Jasur</em>, <em>my little
sister</em>, <em>the boys in my class</em>, <em>learning English</em>. It can also be a
pronoun: <em>I, you, he, she, it, we, they</em>.</p>

<h3>2. The verb — what happens?</h3>

<p>The <mark>verb</mark> is the action or the state. It is the engine of the sentence: no
verb, no sentence. Some verbs are visible actions (<em>run, eat, write</em>), and some are
quiet states (<em>be, have, know, want</em>) — but grammatically they behave the same.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--v">knows</span>
     <span class="pe-hl pe-hl--o">the answer</span>.</p>
  <p class="pe-ex__uz">Afsona javobni biladi.</p>
  <p class="pe-ex__why"><em>Know</em> is not an action you can see — but it is still the verb.</p>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  Every English sentence needs <b>at least one subject and one verb</b>. If either one is
  missing, it is not a sentence yet — it is a fragment.
</div>

<h3>3. The object — who or what receives the action?</h3>

<p>Many verbs need something to receive the action. Ask the verb <em>What? Whom?</em> and the
answer is the object.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Sherbek</span>
     <span class="pe-hl pe-hl--v">is reading</span>
     <span class="pe-hl pe-hl--o">a book</span>.</p>
  <p class="pe-ex__uz">Sherbek kitob oʻqiyapti.</p>
</div>

<p>Not every sentence has an object. <em>The baby is sleeping.</em> — sleeping does not
travel to anything, so no object is needed. That sentence is complete with just S + V.</p>

<h3>4. The order matters — and it is not the Uzbek order</h3>

<p>This is the single most useful thing in this lesson. Uzbek puts the verb at the end.
English puts the verb <b>in the middle</b>, right after the subject.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">🇺🇿 Uzbek — S O V</p>
    <p>Men <b>ingliz tilini</b> <b>oʻrganaman</b>.</p>
    <p>subject → object → verb</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">🇬🇧 English — S V O</p>
    <p>I <b>study</b> <b>English</b>.</p>
    <p>subject → verb → object</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida feʼl gap oxirida keladi, ingliz tilida esa feʼl <b>egadan keyin darrov</b>
  keladi. Shuning uchun "I English study" notoʻgʻri — toʻgʻrisi <b>"I study English"</b>.
  Gap tuzayotganda avval <b>kim</b>, keyin <b>nima qiladi</b>, keyin <b>nimani</b> deb
  oʻylang.
</div>

<p>After the object, English adds extra information in a comfortable order: <b>place first,
time last</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">We</span>
     <span class="pe-hl pe-hl--v">learn</span>
     <span class="pe-hl pe-hl--o">English</span>
     <span class="pe-hl pe-hl--adv">at school</span>
     <span class="pe-hl pe-hl--adv">every day</span>.</p>
  <p class="pe-ex__uz">Biz har kuni maktabda ingliz tilini oʻrganamiz.</p>
</div>

<h3>5. English always needs a subject</h3>

<p>In Uzbek you can say <em>Yomgʻir yogʻyapti</em> or simply <em>Kelyapman</em> — the person
is hidden inside the verb. English cannot do this. Even when there is no real "doer",
English puts an empty subject <b>it</b> or <b>there</b> in the slot.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">It</span>
     <span class="pe-hl pe-hl--v">is raining</span>.</p>
  <p class="pe-ex__uz">Yomgʻir yogʻyapti.</p>
  <p class="pe-ex__why"><em>It</em> means nothing here — it is just holding the subject seat.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada ega tushib qolishi mumkin ("Kelyapman"), ingliz tilida esa <b>ega
  majburiy</b>. Har doim "kim?" degan savolga javob boʻlgan soʻzni yozing: <b>I</b> am
  coming. Ega yoʻq boʻlsa — <b>it</b> yoki <b>there</b> qoʻyiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada sifat bilan gap tuzilganda feʼl kerak emas: <em>Akam juda aqlli</em>. Ingliz
  tilida esa har bir gapda feʼl boʻlishi shart, shuning uchun <b>is/are</b> qoʻshiladi:
  <em>My brother <b>is</b> very clever</em>. Bu — eng koʻp uchraydigan xatolardan biri.
</div>

<h3>6. How to check any sentence in 3 steps</h3>

<ol class="pe-steps">
  <li><b>Find the verb.</b> What is happening? If you cannot find one, your sentence is broken.</li>
  <li><b>Ask "who or what?" before the verb.</b> That answer is your subject. No answer? Add <em>it</em> / <em>there</em> / a pronoun.</li>
  <li><b>Check the order.</b> Subject, then verb, then object — never verb at the end.</li>
</ol>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I English study every day.</s></p>
  <p class="pe-good">I <b>study English</b> every day. <em>(verb before object)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Is very cold today.</s></p>
  <p class="pe-good"><b>It</b> is very cold today. <em>(the subject seat must be filled)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My brother very clever.</s></p>
  <p class="pe-good">My brother <b>is</b> very clever. <em>(no verb → not a sentence)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Because I was tired.</s></p>
  <p class="pe-good">I went home <b>because I was tired</b>. <em>(a half-thought needs its main sentence)</em></p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  When you write, read your sentence aloud and tap the table three times: <b>who — does —
  what</b>. If you cannot tap all three, something is missing.
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Find the subject and the verb: <em>The students in my class speak three languages.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p>Subject = <strong>The students in my class</strong> (ask: who speaks?).
         Verb = <strong>speak</strong>. Object = <em>three languages</em>.</p>
      <p><em>(Oʻzbekcha: ega bir necha soʻzdan iborat boʻlishi mumkin — "kim?" savoliga
         javob bergan butun guruh ega hisoblanadi.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Put the words in the correct order: <em>tea / drinks / every morning / my mother</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My mother drinks tea every morning.</strong></p>
      <p>Subject (my mother) → verb (drinks) → object (tea) → time (every morning). Time
         goes at the end, never between the verb and the object.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Repair it: <em>Is snowing in Tashkent.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It is snowing in Tashkent.</strong></p>
      <p>Weather sentences have no real doer, so English fills the subject seat with the
         empty <b>it</b>. <em>(Oʻzbekcha: ob-havo gaplarida ham ega boʻlishi shart.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Is this a complete sentence? <em>Afsona and her friends after the lesson.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>No — there is no verb.</strong> Add one: <em>Afsona and her friends
         <b>talked</b> after the lesson.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which sentence has no object, and why? <br>
     (a) <em>Sherbek opened the window.</em> &nbsp; (b) <em>Sherbek arrived late.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) has no object.</strong> "Arrive" does not pass the action to anything —
         you cannot arrive <em>something</em>. <em>Late</em> tells us how, not what.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Sentence</b><span>gap</span></li>
  <li><b>Subject</b><span>ega</span></li>
  <li><b>Verb</b><span>feʼl / kesim</span></li>
  <li><b>Object</b><span>toʻldiruvchi</span></li>
  <li><b>Word order</b><span>soʻz tartibi</span></li>
  <li><b>Fragment</b><span>tugallanmagan gap</span></li>
  <li><b>Action</b><span>harakat</span></li>
  <li><b>State</b><span>holat</span></li>
  <li><b>Pronoun</b><span>olmosh</span></li>
  <li><b>Complete</b><span>toʻliq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>A sentence = <b>subject + verb</b> (an object only if the verb needs one).</li>
    <li>English order is <b>S – V – O</b>: the verb comes second, never last.</li>
    <li>Extra information goes after: <b>place, then time</b>.</li>
    <li>The subject seat is never empty — use <b>it</b> or <b>there</b> if there is no doer.</li>
    <li>To check a sentence: find the verb → ask "who?" → check the order.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-2: Nouns: Countable and Uncountable",
        "category": "english",
        "order": 2,
        "summary": (
            "Why you can say 'three books' but never 'three breads' — how English splits nouns "
            "into countable and uncountable, and the words that go with each."
        ),
        "content": """
<h2>PE-2: Nouns: Countable and Uncountable</h2>

<p>In Uzbek you can happily say <em>ikkita non</em>. Say "two breads" in English and everyone
will smile — because English divides the world into things you can count one by one, and
things you can only measure. Get this split right and articles, plurals and quantity words
all fall into place.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The difference between countable and uncountable nouns</li>
    <li>Which quantity words go with each (<em>many / much, few / little</em>)</li>
    <li>How to count uncountable things using containers and measures</li>
    <li>The famous traps: <em>information, advice, news, money, furniture</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Countable</span>
  <span class="pe-chip pe-chip--s">a / an</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">singular noun</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">two, many, a few</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">plural noun</span>
</div>
<div class="pe-formula">
  <span class="pe-formula__label">Uncountable</span>
  <span class="pe-chip pe-chip--aux">some, much, a little</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">singular form only</span>
  <span class="pe-chip pe-chip--opt">(never a / an, never -s)</span>
</div>

<h3>1. Countable nouns — you can put a number in front</h3>

<p><mark>Countable nouns</mark> are separate objects. You can count them: <em>one book, two
books, twenty books</em>. They have a singular and a plural form, and singular ones need
<b>a</b> or <b>an</b> in front.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona bought <b>a pen</b> and <b>three notebooks</b>.</p>
  <p class="pe-ex__uz">Afsona bitta ruchka va uchta daftar sotib oldi.</p>
</div>

<h3>2. Uncountable nouns — you can only measure them</h3>

<p><mark>Uncountable nouns</mark> are seen as one mass, not as separate pieces. They have
<b>no plural</b> and take <b>no a/an</b>. The verb that follows them is always singular.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Water</b> <span class="pe-hl pe-hl--v">is</span> life. We need
     <b>some water</b>.</p>
  <p class="pe-ex__uz">Suv — hayot. Bizga bir oz suv kerak.</p>
  <p class="pe-ex__why">Not <s>waters</s>, not <s>a water</s>, and the verb is <em>is</em>, not <em>are</em>.</p>
</div>

<p>Uncountable nouns usually fall into a few families:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Liquids &amp; gases</p>
    <p><em>water, milk, tea, oil, air</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Materials &amp; powders</p>
    <p><em>bread, rice, sugar, salt, wood, paper, money</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Abstract ideas</p>
    <p><em>love, time, help, luck, advice, information, knowledge</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Collections</p>
    <p><em>furniture, luggage, equipment, homework, traffic</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida deyarli hamma narsani sanash mumkin: <em>ikkita maslahat, uchta yangilik</em>.
  Ingliz tilida esa <b>advice</b>, <b>news</b>, <b>information</b>, <b>furniture</b>,
  <b>homework</b> sanalmaydi — ularga <b>-s</b> ham, <b>a/an</b> ham qoʻshilmaydi. Bu roʻyxatni
  yod olib qoʻying, chunki bu eng koʻp uchraydigan xato.
</div>

<h3>3. How to count the uncountable</h3>

<p>You cannot count the substance, but you <em>can</em> count the container, the piece or the
measure it comes in. This is the trick that solves "two breads".</p>

<div class="pe-ex">
  <p class="pe-ex__en">Two <b>loaves of</b> bread, a <b>piece of</b> advice, three
     <b>bottles of</b> water, a <b>bowl of</b> rice.</p>
  <p class="pe-ex__uz">Ikkita non, bitta maslahat, uchta shisha suv, bir kosa guruch.</p>
</div>

<p>Useful partners: <em>a piece of</em> (advice, news, information, furniture, paper),
<em>a glass / cup / bottle of</em> (drinks), <em>a slice of</em> (bread, cheese, cake),
<em>a kilo of</em> (rice, meat), <em>a bit of</em> (anything, informal).</p>

<h3>4. Quantity words: the pairs you must not mix</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">With countable (plural)</p>
    <ul>
      <li><b>many</b> books</li>
      <li><b>a few</b> friends</li>
      <li><b>how many</b> apples?</li>
      <li><b>a number of</b> students</li>
      <li>too <b>many</b> mistakes</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">With uncountable</p>
    <ul>
      <li><b>much</b> time</li>
      <li><b>a little</b> sugar</li>
      <li><b>how much</b> money?</li>
      <li><b>an amount of</b> water</li>
      <li>too <b>much</b> noise</li>
    </ul>
  </div>
</div>

<p>Some words are friendly with both: <b>some, any, a lot of, lots of, plenty of, no</b>.
When you are unsure, <em>a lot of</em> is always safe: <em>a lot of books</em>, <em>a lot of
water</em>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida <em>koʻp</em> soʻzi hamma narsa uchun bir xil: <em>koʻp kitob</em>,
  <em>koʻp suv</em>. Ingliz tilida esa ikkiga boʻlinadi: sanaladiganlar uchun <b>many</b>,
  sanalmaydiganlar uchun <b>much</b>. Xuddi shunday: <em>oz</em> → <b>a few</b> (sanaladigan)
  va <b>a little</b> (sanalmaydigan).
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  <b>Much</b> and <b>many</b> sound heavy in positive sentences. Native speakers say
  <em>"I have a lot of homework"</em>, and save <em>much/many</em> for questions and
  negatives: <em>"Do you have much homework?" — "Not many people came."</em>
</div>

<h3>5. Some nouns live on both sides</h3>

<p>A few nouns change meaning when they change side. Uncountable = the substance or the idea;
countable = a type, a portion, or a single item.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I don't drink <b>coffee</b>. → Two <b>coffees</b>, please.</p>
  <p class="pe-ex__uz">Men qahva ichmayman. → Ikkita qahva bering.</p>
  <p class="pe-ex__why">The second one means <em>two cups of coffee</em> — portions can be counted.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">She hasn't got much <b>experience</b>. → I had a strange
     <b>experience</b> yesterday.</p>
  <p class="pe-ex__uz">Uning tajribasi kam. → Kecha gʻalati voqeani boshimdan kechirdim.</p>
  <p class="pe-ex__why">Uncountable = skill; countable = one event that happened to you.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Money</b> sanalmaydi, lekin <b>dollar / soʻm</b> sanaladi: <em>much money</em>, ammo
  <em>ten dollars</em>. Shuningdek <b>news</b> soʻzi <b>-s</b> bilan tugasa ham birlik:
  <em>The news <b>is</b> good</em>, <s>The news are good</s>.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I need some informations.</s></p>
  <p class="pe-good">I need <b>some information</b> / <b>two pieces of information</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He gave me a good advice.</s></p>
  <p class="pe-good">He gave me <b>good advice</b> / <b>a piece of good advice</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>How much apples do you want?</s></p>
  <p class="pe-good"><b>How many</b> apples do you want?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We bought new furnitures for the room.</s></p>
  <p class="pe-good">We bought <b>new furniture</b> for the room.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My homeworks are difficult.</s></p>
  <p class="pe-good">My <b>homework is</b> difficult.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>There isn't <span class="pe-blank">?</span> milk in the fridge.</em>
     (many / much)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>much</strong> — <em>milk</em> is a liquid, so it is uncountable, and
         <em>much</em> is the uncountable partner. <em>(Oʻzbekcha: suyuqliklar sanalmaydi.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct the sentence: <em>Jasur gave me three advices about the exam.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur gave me three pieces of advice about the exam.</strong></p>
      <p><em>Advice</em> never takes <b>-s</b>; to count it, count the pieces.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Is / Are: <em>The news about the match <span class="pe-blank">?</span> surprising.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — <em>news</em> looks plural because of the <b>-s</b>, but it is
         an uncountable noun and takes a singular verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which is correct, and what does it mean?
     (a) <em>Would you like a chicken?</em> &nbsp; (b) <em>Would you like some chicken?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Both are correct, but they mean different things.</strong> (a) offers you a
         whole live bird 🐔; (b) offers you chicken meat. Animals are countable; their meat is
         uncountable.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Sort these: <em>traffic · suggestion · luggage · idea · equipment · problem</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Uncountable:</strong> traffic, luggage, equipment.
         <strong>Countable:</strong> suggestion, idea, problem.</p>
      <p>Notice the trap: <em>advice</em> is uncountable but <em>suggestion</em> is countable —
         <em>He gave me two suggestions</em> ✓.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Noun</b><span>ot</span></li>
  <li><b>Countable</b><span>sanaladigan</span></li>
  <li><b>Uncountable</b><span>sanalmaydigan</span></li>
  <li><b>Singular</b><span>birlik</span></li>
  <li><b>Plural</b><span>koʻplik</span></li>
  <li><b>Quantity</b><span>miqdor</span></li>
  <li><b>A piece of</b><span>bir dona / bir parcha</span></li>
  <li><b>Substance</b><span>modda</span></li>
  <li><b>Advice</b><span>maslahat</span></li>
  <li><b>Luggage</b><span>yuk, chamadon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Countable = you can put a number in front; it has a plural and takes <b>a/an</b>.</li>
    <li>Uncountable = no plural, no <b>a/an</b>, always a <b>singular verb</b>.</li>
    <li>Count the container: <b>a piece of advice</b>, <b>two bottles of water</b>.</li>
    <li><b>many / a few</b> → countable · <b>much / a little</b> → uncountable ·
        <b>a lot of</b> → both.</li>
    <li>Learn the traps by heart: <b>information, advice, news, money, furniture,
        homework, traffic, luggage</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-3: Plural Nouns: Regular and Irregular",
        "category": "english",
        "order": 3,
        "summary": (
            "All the plural rules in one place — the -s and -es endings, y → ies, f → ves, "
            "the irregular family (child → children) and the nouns that never change."
        ),
        "content": """
<h2>PE-3: Plural Nouns: Regular and Irregular</h2>

<p>Uzbek has one plural ending and it never lets you down: <em>-lar</em>. Kitob → kitoblar,
bola → bolalar, oyoq → oyoqlar. English promises you the same simplicity with <b>-s</b> …
and then hands you <em>children</em>, <em>feet</em>, <em>mice</em> and <em>sheep</em>. This
lesson gives you every rule, in the order you actually need them.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>When to add <b>-s</b> and when to add <b>-es</b></li>
    <li>The spelling changes: <em>city → cities</em>, <em>knife → knives</em></li>
    <li>The irregular plurals every learner must memorise</li>
    <li>The three ways the <b>-s</b> ending is pronounced</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The default rule</span>
  <span class="pe-chip pe-chip--s">noun</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">-s</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">plural</span>
  <span class="pe-chip pe-chip--opt">book → books</span>
</div>

<h3>1. The default: just add -s</h3>

<p>Nine nouns out of ten do exactly this and nothing else.</p>

<div class="pe-ex">
  <p class="pe-ex__en">book → <b>books</b> · pen → <b>pens</b> · table → <b>tables</b> ·
     student → <b>students</b> · day → <b>days</b></p>
  <p class="pe-ex__uz">kitob → kitoblar · ruchka → ruchkalar · stol → stollar</p>
</div>

<h3>2. Add -es after a hissing sound</h3>

<p>If the word already ends in a hissing or buzzing sound, <b>-s</b> alone cannot be heard, so
English adds a whole extra syllable: <b>-es</b>. This happens after
<b>-s, -ss, -sh, -ch, -x, -z</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">bus → <b>buses</b> · class → <b>classes</b> · dish → <b>dishes</b> ·
     watch → <b>watches</b> · box → <b>boxes</b></p>
  <p class="pe-ex__uz">avtobus → avtobuslar · sinf → sinflar · tovoq → tovoqlar</p>
  <p class="pe-ex__why">Say them aloud: <em>bus-<b>iz</b></em>. You can hear the extra syllable.</p>
</div>

<p>Most nouns ending in <b>-o</b> also take <b>-es</b>: <em>potato → potatoes, tomato →
tomatoes, hero → heroes</em>. But modern and shortened words keep plain <b>-s</b>:
<em>photo → photos, piano → pianos, video → videos, kilo → kilos</em>.</p>

<h3>3. Consonant + y → -ies</h3>

<p>Look at the letter <b>before</b> the <b>y</b>. If it is a consonant, the y becomes
<b>-ies</b>. If it is a vowel, do nothing special — just add <b>-s</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">consonant + y → ies</p>
    <ul>
      <li>city → <b>cities</b></li>
      <li>country → <b>countries</b></li>
      <li>baby → <b>babies</b></li>
      <li>story → <b>stories</b></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">vowel + y → just s</p>
    <ul>
      <li>day → <b>days</b></li>
      <li>boy → <b>boys</b></li>
      <li>key → <b>keys</b></li>
      <li>toy → <b>toys</b></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>y</b> harfidan oldingi harfga qarang: undosh boʻlsa <em>-ies</em> (city → cit<b>ies</b>),
  unli boʻlsa oddiy <em>-s</em> (day → day<b>s</b>). Bu qoida keyinroq feʼllarda ham ishlaydi:
  <em>study → studies</em>, <em>play → plays</em>.
</div>

<h3>4. -f / -fe → -ves</h3>

<p>Many (not all) nouns ending in <b>-f</b> or <b>-fe</b> soften to <b>-ves</b>:</p>

<div class="pe-ex">
  <p class="pe-ex__en">knife → <b>knives</b> · wife → <b>wives</b> · leaf → <b>leaves</b> ·
     life → <b>lives</b> · half → <b>halves</b> · shelf → <b>shelves</b> · wolf → <b>wolves</b></p>
  <p class="pe-ex__uz">pichoq → pichoqlar · xotin → xotinlar · barg → barglar</p>
</div>

<p>Exceptions that keep the <b>f</b>: <em>roof → roofs, chief → chiefs, cliff → cliffs,
belief → beliefs, chef → chefs</em>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat: oʻzbek tilida sondan keyin ot <b>birlikda</b> qoladi — <em>beshta kitob</em>,
  <em>uchta bola</em>. Ingliz tilida esa sondan keyin ot <b>albatta koʻplikda</b> boʻladi:
  <b>five books</b>, <b>three children</b>. <s>five book</s> — notoʻgʻri.
</div>

<h3>5. The irregular family — learn these by heart</h3>

<p>These do not follow any rule. They are old words that English has kept unchanged for a
thousand years, and they are extremely common — so memorising them pays every day.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Singular</th><th>Plural</th><th>Oʻzbekcha</th></tr>
  <tr><td>man</td><td><b>men</b></td><td>erkak → erkaklar</td></tr>
  <tr><td>woman</td><td><b>women</b></td><td>ayol → ayollar</td></tr>
  <tr><td>child</td><td><b>children</b></td><td>bola → bolalar</td></tr>
  <tr><td>person</td><td><b>people</b></td><td>odam → odamlar</td></tr>
  <tr><td>foot</td><td><b>feet</b></td><td>oyoq → oyoqlar</td></tr>
  <tr><td>tooth</td><td><b>teeth</b></td><td>tish → tishlar</td></tr>
  <tr><td>mouse</td><td><b>mice</b></td><td>sichqon → sichqonlar</td></tr>
  <tr><td>goose</td><td><b>geese</b></td><td>gʻoz → gʻozlar</td></tr>
</table>
</div>

<p>And a small group never changes at all — the singular and the plural look identical:
<em>sheep, fish, deer, aircraft, series, species</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">One <b>sheep</b>, ten <b>sheep</b>. There <b>are</b> many
     <b>fish</b> in this river.</p>
  <p class="pe-ex__uz">Bitta qoʻy, oʻnta qoʻy. Bu daryoda koʻp baliq bor.</p>
  <p class="pe-ex__why">The noun does not change, but the <b>verb</b> shows you it is plural: <em>are</em>.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>People</b> is already the plural of <em>person</em>. Say <em>"Many people are
  here"</em> — never <s>peoples are</s>. (<em>Peoples</em> exists, but it means "nations",
  as in <em>the peoples of Central Asia</em>.)
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida koʻplik uchun bitta qoʻshimcha bor — <b>-lar</b>, va u hech qachon
  oʻzgarmaydi. Ingliz tilida esa <b>-s</b>, <b>-es</b>, <b>-ies</b>, <b>-ves</b> va
  qoidasiz shakllar bor. Shuning uchun yangi soʻz oʻrganganingizda uni <b>darrov koʻplik
  shakli bilan birga</b> yodlang: <em>child – children</em>, <em>leaf – leaves</em>.
</div>

<h3>6. How to pronounce the -s</h3>

<p>The spelling is one letter, but the sound is three different things. Your mouth chooses
automatically once you know the pattern.</p>

<ol class="pe-steps">
  <li><b>/ɪz/</b> — after a hissing sound (s, sh, ch, x, ge): <em>buses, watches, boxes,
      pages</em>. An extra syllable you can hear.</li>
  <li><b>/s/</b> — after a voiceless sound (p, t, k, f): <em>books, cats, maps, cups</em>.
      A soft snake sound.</li>
  <li><b>/z/</b> — after everything else, including vowels: <em>dogs, pens, boys, cars</em>.
      A buzzing sound.</li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Put your fingers on your throat and say <em>books</em>, then <em>dogs</em>. In
  <em>dogs</em> you feel a vibration — that is the /z/. You do not need to memorise this;
  you need to notice it once, and your mouth will do the rest.
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>There are five childs in the family.</s></p>
  <p class="pe-good">There are five <b>children</b> in the family.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Many peoples came to the concert.</s></p>
  <p class="pe-good">Many <b>people came</b> to the concert.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My foots hurt after the match.</s></p>
  <p class="pe-good">My <b>feet</b> hurt after the match.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She has two babys.</s></p>
  <p class="pe-good">She has two <b>babies</b>. <em>(consonant + y → ies)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We saw three sheeps on the hill.</s></p>
  <p class="pe-good">We saw three <b>sheep</b> on the hill.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Write the plurals: <em>watch · country · knife · photo · man</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>watches</strong> (hissing sound → -es), <strong>countries</strong>
         (consonant + y), <strong>knives</strong> (-fe → -ves), <strong>photos</strong>
         (shortened word keeps -s), <strong>men</strong> (irregular).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Why is it <em>days</em> but <em>cities</em>?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because of the letter before the y.</strong> In <em>day</em> it is the vowel
         <b>a</b> → just add -s. In <em>city</em> it is the consonant <b>t</b> → y becomes
         -ies.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>Sherbek brushes his tooths twice a day.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sherbek brushes his teeth twice a day.</strong></p>
      <p><em>Tooth → teeth</em> is irregular. Notice <em>brushes</em> also takes <b>-es</b> —
         the same hissing-sound rule works on verbs.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Is / Are: <em>The police <span class="pe-blank">?</span> looking for the driver.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>are</strong> — <em>police</em> has no <b>-s</b>, but English treats it as a
         plural group of officers, like <em>people</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which pronunciation of <b>-s</b>: <em>maps · pens · classes</em>?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>maps = /s/</strong> (after the voiceless <em>p</em>),
         <strong>pens = /z/</strong> (after the voiced <em>n</em>),
         <strong>classes = /ɪz/</strong> (after the hissing <em>ss</em>, an extra syllable).</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Plural</b><span>koʻplik</span></li>
  <li><b>Singular</b><span>birlik</span></li>
  <li><b>Regular</b><span>qoidali</span></li>
  <li><b>Irregular</b><span>qoidasiz</span></li>
  <li><b>Ending</b><span>qoʻshimcha</span></li>
  <li><b>Vowel</b><span>unli harf</span></li>
  <li><b>Consonant</b><span>undosh harf</span></li>
  <li><b>Syllable</b><span>boʻgʻin</span></li>
  <li><b>Spelling</b><span>imlo</span></li>
  <li><b>Pronunciation</b><span>talaffuz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Default: <b>+ s</b>. After a hissing sound (s, sh, ch, x, z) and most <b>-o</b>: <b>+ es</b>.</li>
    <li>Consonant + y → <b>-ies</b>; vowel + y → just <b>-s</b>.</li>
    <li>Many <b>-f / -fe</b> words become <b>-ves</b> (knife → knives).</li>
    <li>Memorise the irregulars: <b>men, women, children, people, feet, teeth, mice</b>.</li>
    <li><b>Sheep, fish, deer</b> never change — the verb shows the number.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-4: Articles: a, an, the and the Zero Article",
        "category": "english",
        "order": 4,
        "summary": (
            "The hardest small words in English, finally explained: a/an for new things, the "
            "for known things, and nothing at all when you speak in general."
        ),
        "content": """
<h2>PE-4: Articles: a, an, the and the Zero Article</h2>

<p>Uzbek has no articles at all, so these two tiny words — <b>a</b> and <b>the</b> — are the
number-one place where good Uzbek speakers of English are given away. The good news: there is
a logic behind them, and it fits in one idea. <mark>Use <b>a/an</b> when the listener does not
know which one yet; use <b>the</b> when they do.</mark></p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Why <em>a</em> and <em>an</em> depend on <b>sound</b>, not on spelling</li>
    <li>The "first mention → second mention" rule that decides almost everything</li>
    <li>When to use <b>no article at all</b> (this is half of English!)</li>
    <li>A 4-question ladder you can run in your head while you speak</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The core idea</span>
  <span class="pe-chip pe-chip--s">a / an</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">one of many — new to the listener</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">the</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">we both know which one</span>
</div>

<h3>1. a or an? Listen, don't look</h3>

<p>The choice depends on the <b>first sound</b> of the next word, not the first letter.
Consonant sound → <b>a</b>. Vowel sound → <b>an</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">a — consonant sound</p>
    <ul>
      <li><b>a</b> book, <b>a</b> car</li>
      <li><b>a</b> university <em>(yu-niversity)</em></li>
      <li><b>a</b> European country</li>
      <li><b>a</b> one-way street <em>(wan-way)</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">an — vowel sound</p>
    <ul>
      <li><b>an</b> apple, <b>an</b> egg</li>
      <li><b>an</b> hour <em>(the h is silent → auer)</em></li>
      <li><b>an</b> honest man</li>
      <li><b>an</b> MP3 player <em>(em-pee-three)</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Harfga emas, <b>tovushga</b> qarang. <em>University</em> "u" bilan yozilsa ham
  "<b>yu</b>niversity" deb oʻqiladi — shuning uchun <b>a</b> university. <em>Hour</em> esa "h"
  bilan yozilsa ham "<b>a</b>uer" deb oʻqiladi — shuning uchun <b>an</b> hour. Soʻzni ovoz
  chiqarib ayting, javob oʻzi keladi.
</div>

<h3>2. First mention → a/an. Second mention → the</h3>

<p>This is the heart of the system. The first time you introduce something, your listener does
not know which one you mean, so you say <b>a</b>. After that, you both know — so you switch to
<b>the</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Yesterday I bought <b>a</b> book and <b>a</b> pen. <b>The</b> book was
     expensive, but <b>the</b> pen was cheap.</p>
  <p class="pe-ex__uz">Kecha men kitob va ruchka sotib oldim. Kitob qimmat edi, ruchka esa arzon.</p>
  <p class="pe-ex__why">Sentence 1 introduces them; sentence 2 refers back to the same ones.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida artikl yoʻq, lekin xuddi shu maʼno bor: birinchi marta aytilganda
  <em>bir kitob</em> (= <b>a</b> book), keyin esa <em>oʻsha kitob</em> (= <b>the</b> book).
  Ingliz tilida bu farqni tushirib qoldirib boʻlmaydi — <b>a</b> yoki <b>the</b> deb
  aytishingiz shart.
</div>

<h3>3. Use "the" whenever the listener can point at it</h3>

<p><b>The</b> is not only for the second mention. Use it any time there is only one possible
thing you could mean:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Only one in the world</p>
    <p><em>the sun, the moon, the sky, the internet</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Only one here</p>
    <p><em>Close <b>the</b> door. Pass me <b>the</b> salt.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Made specific by extra words</p>
    <p><em><b>the</b> girl in the red coat, <b>the</b> capital of Uzbekistan</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Superlatives &amp; order</p>
    <p><em><b>the</b> best, <b>the</b> tallest, <b>the</b> first, <b>the</b> same</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona is <b>the</b> best student in <b>the</b> class.</p>
  <p class="pe-ex__uz">Afsona sinfdagi eng yaxshi oʻquvchi.</p>
  <p class="pe-ex__why">There can only be one "best" — so <b>the</b> is obligatory with superlatives.</p>
</div>

<h3>4. The zero article — when you say nothing</h3>

<p>Half of correct English uses <b>no article</b>. This happens when you talk about things
<b>in general</b>, not about particular ones.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Books</b> are expensive. I like <b>music</b>. <b>Water</b> boils at
     100°.</p>
  <p class="pe-ex__uz">Kitoblar qimmat. Men musiqani yaxshi koʻraman. Suv 100 darajada qaynaydi.</p>
  <p class="pe-ex__why">Plural or uncountable + general meaning = no article.</p>
</div>

<p>You also drop the article with:</p>

<ul>
  <li><b>Names</b> of people, cities, most countries: <em>Jasur, Tashkent, Uzbekistan</em></li>
  <li><b>Meals, languages, school subjects, sports, colours</b>: <em>after breakfast, speak
      English, study maths, play football, wear blue</em></li>
  <li><b>Transport with "by"</b>: <em>by bus, by car, by plane, on foot</em></li>
  <li><b>Places used for their purpose</b>: <em>go to school, at home, in bed, at work,
      in hospital</em></li>
</ul>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <em>Go to <b>school</b></em> = go there to study (the purpose).
  <em>Go to <b>the</b> school</em> = go to that building for another reason, e.g. your mother
  going to meet a teacher. The same pair works for <em>hospital, bed, church, prison</em>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kasb-hunar haqida gapirganda ingliz tilida <b>a/an</b> shart: <em>I am <b>a</b> student</em>,
  <em>She is <b>an</b> engineer</em>. Oʻzbekchada "Men oʻquvchiman" deymiz, artikl yoʻq —
  shuning uchun bu xato juda tez-tez uchraydi. Umumiy maʼnoda gapirganda esa aksincha,
  artikl <b>umuman qoʻyilmaydi</b>: <em>Life is short</em>, <s>The life is short</s>.
</div>

<h3>5. The decision ladder</h3>

<p>When you are speaking and you hesitate, run these four questions. It takes half a second
once you have practised it.</p>

<ol class="pe-steps">
  <li><b>Does my listener already know exactly which one?</b> → yes: <b>the</b>. Stop here.</li>
  <li><b>Am I speaking in general (all books, all water)?</b> → yes: <b>no article</b>. Stop.</li>
  <li><b>Is it singular and countable?</b> → yes: <b>a / an</b>.</li>
  <li><b>Is it plural or uncountable but specific?</b> → <b>the</b> (<em>the books I bought</em>).</li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  A singular countable noun almost never stands alone in English. If you write
  <em>student</em>, <em>car</em> or <em>problem</em> with nothing in front of it, something is
  usually missing: <b>a</b>, <b>the</b>, <b>my</b>, <b>this</b>… Check every bare singular noun
  in your writing.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I am student at school number 5.</s></p>
  <p class="pe-good">I am <b>a</b> student at school number 5.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The life is difficult sometimes.</s></p>
  <p class="pe-good"><b>Life</b> is difficult sometimes. <em>(life in general → no article)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I go to the school by the bus.</s></p>
  <p class="pe-good">I go to <b>school by bus</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She plays the football very well.</s></p>
  <p class="pe-good">She plays <b>football</b> very well. <em>(but: she plays <b>the</b> piano)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He waited for an hour and a half — it was a honest mistake.</s></p>
  <p class="pe-good">… it was <b>an</b> honest mistake. <em>(silent h → vowel sound)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     a / an: <span class="pe-blank">?</span> umbrella · <span class="pe-blank">?</span>
     university · <span class="pe-blank">?</span> hour · <span class="pe-blank">?</span> useful book</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>an</strong> umbrella, <strong>a</strong> university, <strong>an</strong> hour,
         <strong>a</strong> useful book.</p>
      <p><em>University</em> and <em>useful</em> begin with the sound "yu" (a consonant sound);
         <em>hour</em> begins with a vowel sound because the h is silent.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Fill the gaps: <em>I saw <span class="pe-blank">?</span> dog in the park.
     <span class="pe-blank">?</span> dog was very friendly.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a dog … The dog</strong> — first mention introduces it, second mention refers
         back to the same one. <em>(Oʻzbekcha: birinchi marta aytilganda "a", ikkinchi marta
         "the".)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which is right, and what is the difference?
     (a) <em>Jasur is in hospital.</em> &nbsp; (b) <em>Jasur is in the hospital.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Both are correct but different.</strong> (a) means he is ill and being
         treated. (b) means he is inside that building — maybe visiting someone or working
         there.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>The children like the chocolate more than the vegetables.</em>
     (general meaning)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Children like chocolate more than vegetables.</strong></p>
      <p>All three nouns are general — children everywhere, chocolate as a substance,
         vegetables as a class of food. General = no article.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Add articles where needed: <em>Sherbek plays __ guitar and studies __ English at __
     university.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sherbek plays the guitar and studies English at university.</strong></p>
      <p>Musical instruments take <b>the</b>; languages and "at university" (as an activity,
         British English) take no article.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Article</b><span>artikl</span></li>
  <li><b>Definite (the)</b><span>aniq</span></li>
  <li><b>Indefinite (a/an)</b><span>noaniq</span></li>
  <li><b>Zero article</b><span>artiklsiz</span></li>
  <li><b>First mention</b><span>birinchi bor tilga olish</span></li>
  <li><b>Specific</b><span>aniq bir</span></li>
  <li><b>In general</b><span>umumiy maʼnoda</span></li>
  <li><b>Vowel sound</b><span>unli tovush</span></li>
  <li><b>Silent letter</b><span>oʻqilmaydigan harf</span></li>
  <li><b>Superlative</b><span>orttirma daraja</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>a / an</b> = new to the listener, one of many. Choose by <b>sound</b>.</li>
    <li><b>the</b> = we both know which one: second mention, unique things, superlatives.</li>
    <li><b>No article</b> for general plurals and uncountables, names, languages, meals,
        sports, <em>by bus</em>, <em>at home</em>.</li>
    <li>A singular countable noun is almost never alone — it needs <b>a</b>, <b>the</b>,
        or a word like <b>my</b>.</li>
    <li>When stuck, run the ladder: known? → general? → singular countable?</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-5: Pronouns: Subject, Object and Possessive",
        "category": "english",
        "order": 5,
        "summary": (
            "I or me? My or mine? Its or it's? Master the small words that replace nouns and "
            "stop your sentences from repeating themselves."
        ),
        "content": """
<h2>PE-5: Pronouns: Subject, Object and Possessive</h2>

<p>Read this: <em>Afsona took Afsona's book because Afsona needed Afsona's book for
Afsona's lesson.</em> Painful, isn't it? Pronouns exist to fix exactly this:
<em>Afsona took <b>her</b> book because <b>she</b> needed <b>it</b> for <b>her</b>
lesson.</em> Same meaning, half the words.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The full pronoun family in one table you can picture in your head</li>
    <li>When to say <b>I</b> and when to say <b>me</b></li>
    <li>The difference between <b>my</b> and <b>mine</b></li>
    <li>The <b>its / it's</b> trap that even native speakers fall into</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Where each form lives</span>
  <span class="pe-chip pe-chip--s">I (subject)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">me (object)</span>
</div>

LEGEND_HERE

<h3>1. The whole family in one table</h3>

<p>Learn this table across, one row at a time — <em>I, me, my, mine, myself</em> — like a
little song. Every row works the same way.</p>

<div class="pe-table-wrap">
<table>
  <tr>
    <th>Subject</th><th>Object</th><th>Possessive adjective</th>
    <th>Possessive pronoun</th><th>Reflexive</th>
  </tr>
  <tr><td><b>I</b></td><td>me</td><td>my</td><td>mine</td><td>myself</td></tr>
  <tr><td><b>you</b></td><td>you</td><td>your</td><td>yours</td><td>yourself</td></tr>
  <tr><td><b>he</b></td><td>him</td><td>his</td><td>his</td><td>himself</td></tr>
  <tr><td><b>she</b></td><td>her</td><td>her</td><td>hers</td><td>herself</td></tr>
  <tr><td><b>it</b></td><td>it</td><td>its</td><td>—</td><td>itself</td></tr>
  <tr><td><b>we</b></td><td>us</td><td>our</td><td>ours</td><td>ourselves</td></tr>
  <tr><td><b>they</b></td><td>them</td><td>their</td><td>theirs</td><td>themselves</td></tr>
</table>
</div>

<h3>2. Subject pronouns — before the verb</h3>

<p>The subject pronoun does the action. It stands in the subject seat you met in PE-1, right
before the verb.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">She</span>
     <span class="pe-hl pe-hl--v">speaks</span> three languages.</p>
  <p class="pe-ex__uz">U uchta tilda gapiradi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada "u" ham erkak, ham ayol uchun ishlatiladi. Ingliz tilida esa farq bor:
  <b>he</b> (erkak), <b>she</b> (ayol), <b>it</b> (narsa yoki hayvon). Odam haqida
  <b>it</b> deyish qoʻpol eshitiladi — hech qachon ishlatmang.
</div>

<h3>3. Object pronouns — after the verb or a preposition</h3>

<p>The object pronoun receives the action. It comes after the verb, or after a preposition
(<em>to, for, with, about, at</em>).</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Jasur</span>
     <span class="pe-hl pe-hl--v">called</span>
     <span class="pe-hl pe-hl--o">me</span> and waited for
     <span class="pe-hl pe-hl--o">us</span>.</p>
  <p class="pe-ex__uz">Jasur menga qoʻngʻiroq qildi va bizni kutdi.</p>
  <p class="pe-ex__why">After the verb <em>called</em> and after the preposition <em>for</em> — object form.</p>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  Before the verb → <b>I, he, she, we, they</b>. After the verb or a preposition →
  <b>me, him, her, us, them</b>. <em>You</em> and <em>it</em> are lazy: they never change.
</div>

<p>The classic difficulty is a double subject. To test it, cover the other person:
<em>Sherbek and (I / me) went home</em> → you would never say <s>Me went home</s>, so it is
<b>Sherbek and I went home</b>. Now: <em>He invited Sherbek and (I / me)</em> → you would say
<em>He invited me</em>, so it is <b>Sherbek and me</b>.</p>

<h3>4. Possessive adjectives vs possessive pronouns</h3>

<p>Both show ownership, but they sit in different places. A possessive <b>adjective</b> needs
a noun after it. A possessive <b>pronoun</b> stands alone and replaces the whole phrase.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">my / your / his / her / our / their + noun</p>
    <ul>
      <li>This is <b>my</b> book.</li>
      <li><b>Their</b> house is big.</li>
      <li>Is this <b>your</b> pen?</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">mine / yours / his / hers / ours / theirs — alone</p>
    <ul>
      <li>This book is <b>mine</b>.</li>
      <li>The big house is <b>theirs</b>.</li>
      <li>Is this pen <b>yours</b>?</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida egalik ikki marta koʻrsatiladi: <em>mening kitob<b>im</b></em> — ham
  "mening", ham "-im". Ingliz tilida faqat <b>bir marta</b>: <b>my book</b>.
  <s>my my book</s> emas. Va <b>mine</b> — bu "meniki", undan keyin ot kelmaydi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Juda muhim: <b>his</b> yoki <b>her</b> — bu <b>egasining</b> jinsiga qarab tanlanadi,
  narsaning jinsiga emas. <em>Afsona and <b>her</b> brother</em> (Afsona ayol → her),
  <em>Jasur and <b>his</b> sister</em> (Jasur erkak → his). Oʻzbekchada "uning" hamma uchun
  bir xil boʻlgani uchun bu joyda tez-tez adashiladi.
</div>

<h3>5. The its / it's trap</h3>

<p>These two look almost the same and mean completely different things. This is the most
common spelling mistake in English — worldwide, not only for learners.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">its = of it (possessive)</p>
    <p>The cat washed <b>its</b> paws.</p>
    <p>The city is famous for <b>its</b> bazaars.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">it's = it is / it has</p>
    <p><b>It's</b> raining. (it is)</p>
    <p><b>It's</b> been a long day. (it has)</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Test it in one second: say <em>"it is"</em> out loud in place of the word. If the sentence
  still makes sense, write <b>it's</b> with the apostrophe. If it sounds crazy, write
  <b>its</b>.
</div>

<h3>6. A quick look at reflexives</h3>

<p>Use <b>-self / -selves</b> when the subject and the object are the same person.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona taught <b>herself</b> to play the guitar. Be careful — don't cut
     <b>yourself</b>!</p>
  <p class="pe-ex__uz">Afsona gitara chalishni oʻzi oʻrgandi. Ehtiyot boʻling — oʻzingizni kesib
     olmang!</p>
</div>

<p>They also add emphasis: <em>I painted the room <b>myself</b></em> (= nobody helped me).</p>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Me and my brother play football.</s></p>
  <p class="pe-good"><b>My brother and I</b> play football. <em>(subject seat → I; and put the other person first)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This book is my.</s></p>
  <p class="pe-good">This book is <b>mine</b>. / This is <b>my</b> book.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The dog broke it's leg.</s></p>
  <p class="pe-good">The dog broke <b>its</b> leg. <em>(possessive → no apostrophe)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She gave the money to I.</s></p>
  <p class="pe-good">She gave the money to <b>me</b>. <em>(after a preposition → object form)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Every student must bring their own pen — he must be blue.</s></p>
  <p class="pe-good">… <b>it</b> must be blue. <em>(a pen is a thing → it)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     I or me: <em>Sherbek and <span class="pe-blank">?</span> are in the same class. The
     teacher praised Sherbek and <span class="pe-blank">?</span>.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I … me.</strong> Cover the other name: <em>I am in the same class</em> ✓ and
         <em>The teacher praised me</em> ✓.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     my or mine: <em>That's not <span class="pe-blank">?</span> bag. <span class="pe-blank">?</span>
     is black.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>my … Mine.</strong> Before a noun (<em>bag</em>) use <b>my</b>; standing alone
         as the subject, use <b>mine</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     its or it's: <em>The company changed <span class="pe-blank">?</span> name because
     <span class="pe-blank">?</span> too long.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>its … it's.</strong> Test with "it is": <s>changed it is name</s> ✗ → <b>its</b>;
         <em>because it is too long</em> ✓ → <b>it's</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Replace the repeated nouns: <em>Jasur lost Jasur's keys, so Jasur asked Jasur's sister
     to help Jasur.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur lost his keys, so he asked his sister to help him.</strong></p>
      <p>Keep the name once at the start; after that, pronouns do all the work —
         <em>his</em> (possessive), <em>he</em> (subject), <em>him</em> (object).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Fill in: <em>We couldn't find our tickets, so the guard checked
     <span class="pe-blank">?</span> and let <span class="pe-blank">?</span> in.</em>
     (theirs/them/us)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>them … us.</strong> <em>Them</em> = the tickets (object of <em>checked</em>);
         <em>us</em> = we, in object form after <em>let</em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Pronoun</b><span>olmosh</span></li>
  <li><b>Subject pronoun</b><span>ega olmoshi</span></li>
  <li><b>Object pronoun</b><span>toʻldiruvchi olmoshi</span></li>
  <li><b>Possessive</b><span>egalik</span></li>
  <li><b>Reflexive</b><span>oʻzlik olmoshi</span></li>
  <li><b>Preposition</b><span>predlog</span></li>
  <li><b>Apostrophe</b><span>apostrof (')</span></li>
  <li><b>To replace</b><span>almashtirmoq</span></li>
  <li><b>To own</b><span>egalik qilmoq</span></li>
  <li><b>Emphasis</b><span>taʼkid</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Before the verb → <b>I, he, she, we, they</b>. After a verb or preposition →
        <b>me, him, her, us, them</b>.</li>
    <li>Test a double subject by covering the other person: <em>(Sherbek and) I went</em>.</li>
    <li><b>my + noun</b>, but <b>mine</b> alone. English marks possession only once.</li>
    <li><b>its</b> = belonging to it · <b>it's</b> = it is / it has. Say "it is" to check.</li>
    <li>Use <b>-self</b> when the doer and the receiver are the same person.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
