# -*- coding: utf-8 -*-
"""Prime English — Block A, lessons 11–15 (Foundations).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_11_15.py --author=prime
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
        "title": "PE-11: Adverbs of Frequency: always, usually, never",
        "category": "english",
        "order": 11,
        "summary": (
            "How often do you do it? Learn the frequency scale from always to never, and the "
            "one position rule that decides where these words go in a sentence."
        ),
        "stories": ["He Never Says No"],
        "content": """
<h2>PE-11: Adverbs of Frequency: always, usually, never</h2>

<p>"I go to school" tells me what you do. <em>"I <b>always</b> go to school"</em>,
<em>"I <b>sometimes</b> go to school"</em>, <em>"I <b>never</b> go to school"</em> — three
very different lives, and only one small word changed. These words are called
<mark>adverbs of frequency</mark>, and they are the fastest way to make your Present Simple
sentences sound real.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The frequency scale from <b>100% always</b> down to <b>0% never</b></li>
    <li>The position rule: before the verb, but <b>after</b> am/is/are</li>
    <li>Why <em>never</em> already means "not" — and must not be doubled</li>
    <li>How to ask and answer <b>How often …?</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The position rule</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">adverb</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">main verb</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">am / is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">adverb</span>
</div>

LEGEND_HERE

<h3>1. The scale</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">100</span>always</p>
    <p>doim — <em>I always brush my teeth.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">90</span>usually</p>
    <p>odatda — <em>She usually walks to school.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">70</span>often</p>
    <p>tez-tez — <em>We often play chess.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">50</span>sometimes</p>
    <p>baʼzan — <em>He sometimes helps me.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">20</span>rarely / seldom</p>
    <p>kamdan-kam — <em>They rarely watch TV.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">0</span>never</p>
    <p>hech qachon — <em>I never drink coffee.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--adv">usually</span>
     <span class="pe-hl pe-hl--v">does</span> her homework in the evening, but she
     <span class="pe-hl pe-hl--adv">sometimes</span>
     <span class="pe-hl pe-hl--v">finishes</span> it at school.</p>
  <p class="pe-ex__uz">Afsona odatda uy vazifasini kechqurun qiladi, lekin baʼzan uni
     maktabda tugatadi.</p>
</div>

<h3>2. The position rule — one rule, two halves</h3>

<p>This is the only thing you really have to remember, and it has a neat logic: the adverb
sits <b>before</b> an ordinary verb, but <b>after</b> <em>am / is / are</em>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Ordinary verb → adverb goes BEFORE</p>
    <ul>
      <li>I <b>never</b> eat fast food.</li>
      <li>He <b>often</b> plays football.</li>
      <li>We <b>always</b> help her.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">am / is / are → adverb goes AFTER</p>
    <ul>
      <li>I <b>am never</b> late.</li>
      <li>He <b>is often</b> tired.</li>
      <li>They <b>are always</b> busy.</li>
    </ul>
  </div>
</div>

<p>When there is a helper verb, the adverb slides in <b>between</b> the helper and the main
verb — which is really the same rule, since the adverb still comes just before the meaning
verb.</p>

<div class="pe-ex">
  <p class="pe-ex__en">She <span class="pe-hl pe-hl--aux">doesn't</span>
     <span class="pe-hl pe-hl--adv">usually</span>
     <span class="pe-hl pe-hl--v">work</span> on Sundays.</p>
  <p class="pe-ex__uz">U odatda yakshanba kunlari ishlamaydi.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  One picture for the whole rule: the adverb wants to stand as close to the meaning verb as
  possible, on its left. Only <b>be</b> is strong enough to push it to the right.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida bu soʻzlarning oʻrni erkin: "Men <b>doim</b> maktabga boraman" ham,
  "<b>Doim</b> men maktabga boraman" ham toʻgʻri eshitiladi. Ingliz tilida esa oʻrni
  <b>qatʼiy belgilangan</b> — feʼldan oldin. Shuning uchun oʻzbekcha jumlani soʻzma-soʻz
  koʻchirsangiz, <s>I go always</s> degan xato chiqadi.
</div>

<h3>3. "Never" is already negative</h3>

<p><b>Never</b> contains the "not" inside it. Adding <em>don't</em> as well makes a double
negative, which is wrong in standard English.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>I don't never smoke.</s></p>
  <p class="pe-good">I <b>never</b> smoke. / I <b>don't</b> smoke.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu joy juda muhim! Oʻzbek tilida <b>ikkita</b> inkor kerak: "Men <b>hech qachon</b>
  kofe <b>ichmayman</b>" — "hech qachon" ham, "-ma-" ham inkor. Ingliz tilida esa faqat
  <b>bittasi</b> boʻladi: <em>I <b>never drink</b> coffee</em> — feʼl <b>ijobiy</b> shaklda
  qoladi. <s>I never don't drink</s> — notoʻgʻri.
</div>

<h3>4. Longer expressions go at the end</h3>

<p>Short one-word adverbs sit in the middle. Longer frequency phrases go to the end of the
sentence (or, for emphasis, to the very beginning).</p>

<div class="pe-ex">
  <p class="pe-ex__en">We have English <b>three times a week</b>. Jasur visits his grandmother
     <b>every Sunday</b>.</p>
  <p class="pe-ex__uz">Bizda haftada uch marta ingliz tili bor. Jasur har yakshanba buvisini
     yoʻqlaydi.</p>
  <p class="pe-ex__why">Useful phrases: <em>once a day, twice a week, three times a month,
     every year, from time to time</em>.</p>
</div>

<p>Three of the middle adverbs — <b>usually, often, sometimes</b> — may also open a sentence.
<b>Always</b> and <b>never</b> cannot.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>Never I eat meat.</s></p>
  <p class="pe-good"><b>Sometimes I</b> walk to school. / I <b>never</b> eat meat.</p>
</div>

<h3>5. Asking about frequency</h3>

<div class="pe-formula">
  <span class="pe-formula__label">Question</span>
  <span class="pe-chip pe-chip--adv">How often</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">do / does</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
  <span class="pe-op">?</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>How often do</b> you go to the gym? — <b>Twice a week.</b></p>
  <p class="pe-ex__uz">— Sport zaliga qanchalik tez-tez borasan? — Haftada ikki marta.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  "Haftada ikki marta" degan tuzilma ingliz tilida teskari yoziladi: avval <b>necha marta</b>,
  keyin <b>qancha vaqtda</b> — <em><b>twice a week</b></em>, <em><b>three times a
  month</b></em>. Eʼtibor bering, "bir marta" va "ikki marta" uchun alohida soʻzlar bor:
  <b>once</b> va <b>twice</b> (<s>one time</s>, <s>two times</s> deyilmaydi).
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I go always to school by bus.</s></p>
  <p class="pe-good">I <b>always go</b> to school by bus.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She never is late.</s></p>
  <p class="pe-good">She <b>is never</b> late. <em>(after "is")</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He usually don't eat breakfast.</s></p>
  <p class="pe-good">He <b>doesn't usually</b> eat breakfast.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>We play football two times a week.</s></p>
  <p class="pe-good">We play football <b>twice</b> a week.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Always I help my mother.</s></p>
  <p class="pe-good">I <b>always</b> help my mother.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Put <em>often</em> in the right place: <em>Sherbek is late for the first lesson.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sherbek is often late for the first lesson.</strong></p>
      <p>The verb is <em>is</em>, so the adverb goes <b>after</b> it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Put <em>never</em> in the right place: <em>My father drinks cola.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My father never drinks cola.</strong></p>
      <p>An ordinary verb → the adverb goes before it. And the verb keeps its <b>-s</b>,
         because <em>never</em> is not a helper verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>I don't never forget my homework.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I never forget my homework.</strong></p>
      <p>English uses one negative only. <em>(Oʻzbekcha: ingliz tilida ikkita inkor
         ishlatilmaydi.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Answer about yourself: <em>How often do you speak English?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model answers:</strong> <em>Every day.</em> / <em>Three times a week.</em> /
         <em>I usually speak English at school, and I sometimes speak it with my friends.</em></p>
      <p>Notice <em>usually</em> before the verb, and the long phrase at the end.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Two mistakes — find them: <em>Afsona always is busy, and she goes rarely out.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona is always busy, and she rarely goes out.</strong></p>
      <p>(1) After <em>is</em> the adverb goes second. (2) Before an ordinary verb it goes
         first. The two halves of the same rule.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Adverb of frequency</b><span>takror ravishi</span></li>
  <li><b>Always</b><span>doim</span></li>
  <li><b>Usually</b><span>odatda</span></li>
  <li><b>Often</b><span>tez-tez</span></li>
  <li><b>Sometimes</b><span>baʼzan</span></li>
  <li><b>Rarely / seldom</b><span>kamdan-kam</span></li>
  <li><b>Never</b><span>hech qachon</span></li>
  <li><b>Once / twice</b><span>bir marta / ikki marta</span></li>
  <li><b>How often?</b><span>qanchalik tez-tez?</span></li>
  <li><b>Double negative</b><span>qoʻsh inkor</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>The scale: <b>always → usually → often → sometimes → rarely → never</b>.</li>
    <li><b>Before</b> an ordinary verb, <b>after</b> am/is/are, <b>between</b> helper and verb.</li>
    <li><b>Never</b> is already negative — one negative per sentence.</li>
    <li>Long phrases (<b>twice a week, every day</b>) go at the end.</li>
    <li><b>once</b> and <b>twice</b>, not <s>one time</s> / <s>two times</s>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-12: Present Continuous: Happening Right Now",
        "category": "english",
        "order": 12,
        "summary": (
            "The tense for this exact moment: am/is/are + verb-ing. Includes the -ing spelling "
            "rules and the three other jobs this tense quietly does."
        ),
        "stories": ["The Rain Is Starting"],
        "content": """
<h2>PE-12: Present Continuous: Happening Right Now</h2>

<p>Look around you. Somebody <b>is talking</b>, a phone <b>is ringing</b>, you
<b>are reading</b> this sentence. For actions in progress at this very moment English uses a
different tense from the one you learned in PE-9 — the <mark>Present Continuous</mark>. It is
built from two pieces you already know: the verb <em>to be</em>, plus <b>-ing</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The formula <b>am / is / are + verb-ing</b> and how to negate and question it</li>
    <li>The spelling rules for <b>-ing</b> (make → making, sit → sitting)</li>
    <li>Four jobs this tense does, not just "now"</li>
    <li>The signal words that tell you to use it</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">am / is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
</div>

LEGEND_HERE

<h3>1. The picture: an action in progress</h3>

<p>Present Simple was a row of repeated dots. Present Continuous is a <b>band around NOW</b> —
the action started before this moment and has not finished yet.</p>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:50%"></span>
    <span class="pe-tl-band" style="left:28%;width:44%"></span>
    <span class="pe-tl-tag" style="left:50%">I am reading</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--aux">is</span>
     <span class="pe-hl pe-hl--v">cooking</span> dinner, and the children
     <span class="pe-hl pe-hl--aux">are</span>
     <span class="pe-hl pe-hl--v">playing</span> in the garden.</p>
  <p class="pe-ex__uz">Afsona kechki ovqat pishiryapti, bolalar esa bogʻda oʻynashyapti.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Present Continuous oʻzbekchadagi <b>-yapti / -moqda</b> shakliga toʻgʻri keladi:
  <em>oʻqi<b>yapman</b></em> → <em>I <b>am reading</b></em>. Eng muhim farq: oʻzbekchada bitta
  soʻz yetarli, ingliz tilida esa <b>ikkita</b> boʻlak kerak — <b>am/is/are</b> <u>va</u>
  <b>-ing</b>. Biri tushib qolsa, gap notoʻgʻri boʻladi.
</div>

<h3>2. Negatives and questions — the same as "to be"</h3>

<p>Because the first word is <em>am/is/are</em>, you already know how to do this from PE-6:
add <b>not</b>, or swap the first two words.</p>

<div class="pe-ex">
  <p class="pe-ex__en">He <b>isn't listening</b> to me. — <b>Are</b> you <b>waiting</b> for
     the bus? — Yes, I am.</p>
  <p class="pe-ex__uz">U meni eshitmayapti. — Avtobus kutyapsizmi? — Ha.</p>
  <p class="pe-ex__why">No <em>do/does</em> here — that helper belongs to the Present Simple only.</p>
</div>

<h3>3. Spelling the -ing form</h3>

<ol class="pe-steps">
  <li><b>Most verbs: just add -ing</b> — <em>play → playing, read → reading, study → studying</em>
      (yes, <em>y</em> stays!)</li>
  <li><b>Verb ends in silent -e: drop the e</b> — <em>make → making, write → writing,
      come → coming</em> (but <em>see → seeing</em>, the e is not silent)</li>
  <li><b>Short verb, one vowel + one consonant: double the consonant</b> —
      <em>sit → sitting, run → running, swim → swimming, get → getting</em></li>
  <li><b>-ie → -y</b> — <em>lie → lying, die → dying</em></li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Rule 3 exists to protect the sound. <em>Sit + ing</em> without doubling would look like
  <em>siting</em>, which an English reader pronounces "sy-ting". The double letter keeps the
  vowel short.
</div>

<h3>4. Four jobs, not one</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>At this moment</p>
    <p><em>Be quiet — the baby <b>is sleeping</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Around now (temporary)</p>
    <p><em>I <b>am reading</b> a great book these days.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Changing situations</p>
    <p><em>The weather <b>is getting</b> warmer.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Annoying habits</p>
    <p><em>He <b>is always losing</b> his keys!</em></p>
  </div>
</div>

<p>Job 2 is worth a second look. <em>I am reading a great book</em> does not mean the book is
open in your hands right now — it means "in this period of my life". The action is
<b>temporary</b>, and that is the real heart of this tense.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Jasur <b>is living</b> with his uncle <b>this year</b>.</p>
  <p class="pe-ex__uz">Jasur bu yil amakisinikida yashayapti.</p>
  <p class="pe-ex__why">Compare: <em>Jasur <b>lives</b> in Namangan</em> — that is permanent,
     so Present Simple.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  4-vazifaga eʼtibor bering: <b>always + -ing</b> "doim" degani emas, balki <b>norozilik</b>
  bildiradi — <em>He is always losing his keys</em> = "Kalitini doim yoʻqotadi-ya!" degan
  achchiqlanish maʼnosi. Oddiy odat uchun esa Present Simple ishlatiladi:
  <em>He always loses…</em> emas, <em>He always <b>takes</b> the bus</em>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ehtiyot boʻling: oʻzbekchada odat haqida ham "-yapman" deb aytish mumkin — "Men shu kunlarda
  har kuni oʻqi<b>yapman</b>". Ingliz tilida esa <b>har kuni takrorlanadigan odat</b> uchun
  Present Continuous ishlatilmaydi: <em>I <b>study</b> every day</em>, <s>I am studying every
  day</s> emas. Odat — Present Simple, ayni damdagi ish — Present Continuous.
</div>

<h3>5. Signal words</h3>

<p>These words point straight at this tense: <em>now, right now, at the moment, at present,
today, this week, these days, still</em>, and the two little words that open a window on the
present — <em>Look!</em> and <em>Listen!</em></p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Look!</b> Sherbek <b>is running</b> to catch the bus.</p>
  <p class="pe-ex__uz">Qara! Sherbek avtobusga yetib olish uchun yuguryapti.</p>
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I am go to the shop now.</s></p>
  <p class="pe-good">I <b>am going</b> to the shop now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She reading a book.</s></p>
  <p class="pe-good">She <b>is</b> reading a book. <em>(the "be" part is not optional)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>They are writeing / He is siting.</s></p>
  <p class="pe-good">They are <b>writing</b> / He is <b>sitting</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you playing football now?</s></p>
  <p class="pe-good"><b>Are</b> you <b>playing</b> football now?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I am studying English every day.</s></p>
  <p class="pe-good">I <b>study</b> English every day. <em>(a habit → Present Simple)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Write the -ing forms: <em>make · run · study · lie · take</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>making</strong> (drop the e), <strong>running</strong> (double the n),
         <strong>studying</strong> (y stays!), <strong>lying</strong> (ie → y),
         <strong>taking</strong> (drop the e).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Complete: <em>Be quiet! The baby <span class="pe-blank">?</span> (sleep).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is sleeping</strong> — happening right now, and <em>Be quiet!</em> is the
         signal.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make a question and a negative: <em>They are watching the match.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Are they watching the match? / They aren't watching the match.</strong></p>
      <p>Only the <em>be</em> part moves or takes <em>not</em> — the <b>-ing</b> word never
         changes.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What does the speaker feel? <em>My little brother is always taking my things!</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Annoyance.</strong> <em>Always</em> + Present Continuous is a complaint, not
         a neutral statement of frequency. In Uzbek: "Ukam narsalarimni doim olib ketadi-ya!"</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which sentence is about a temporary situation? <br>
     (a) <em>Afsona works in a pharmacy.</em> (b) <em>Afsona is working in a pharmacy this
     summer.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b).</strong> The Continuous plus <em>this summer</em> says it is only for
         now; (a) is her permanent job.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Present Continuous</b><span>hozirgi davomli zamon</span></li>
  <li><b>In progress</b><span>davom etayotgan</span></li>
  <li><b>At the moment</b><span>ayni paytda</span></li>
  <li><b>Temporary</b><span>vaqtinchalik</span></li>
  <li><b>Permanent</b><span>doimiy</span></li>
  <li><b>To double (a letter)</b><span>harfni takrorlamoq</span></li>
  <li><b>Silent e</b><span>oʻqilmaydigan e</span></li>
  <li><b>Annoying</b><span>jahlni chiqaradigan</span></li>
  <li><b>These days</b><span>shu kunlarda</span></li>
  <li><b>Still</b><span>hali ham</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>am / is / are + verb-ing</b> — both parts, always.</li>
    <li>Negatives and questions work like <b>to be</b>: no <em>do/does</em> anywhere.</li>
    <li>Spelling: drop silent <b>-e</b>, double the consonant in short verbs, <b>-ie → -y</b>.</li>
    <li>It means <b>now</b> or <b>temporarily</b> — not a habit.</li>
    <li><b>always + -ing</b> = a complaint, not a frequency.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-13: Present Simple vs Present Continuous",
        "category": "english",
        "order": 13,
        "summary": (
            "The decision that separates confident speakers from hesitant ones — plus the "
            "stative verbs that refuse to take -ing at all."
        ),
        "stories": ["Usually She Walks, Today She Runs"],
        "content": """
<h2>PE-13: Present Simple vs Present Continuous</h2>

<p>You now know both present tenses. This lesson is about the moment of choice — the half
second before you speak, when you must decide between <em>I work</em> and <em>I am
working</em>. There is a clean test for it, and there is a group of verbs that quietly break
the rules. Both are here.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The one question that decides between the two tenses</li>
    <li>Which signal words belong to which tense</li>
    <li><b>Stative verbs</b> — the verbs that never take <b>-ing</b></li>
    <li>Verbs that change meaning in the Continuous (<em>have, think, see</em>)</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The test question</span>
  <span class="pe-chip pe-chip--s">Always / in general?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">Present Simple</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">Now / temporarily?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">Present Continuous</span>
</div>

<h3>1. Two pictures side by side</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:50%"></span>
    <span class="pe-tl-dot" style="left:12%"></span>
    <span class="pe-tl-dot" style="left:31%"></span>
    <span class="pe-tl-dot" style="left:69%"></span>
    <span class="pe-tl-dot" style="left:88%"></span>
    <span class="pe-tl-band" style="left:40%;width:20%"></span>
    <span class="pe-tl-tag" style="left:26%">band = right now</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>The dots are Present Simple — the same thing again and again. The band around NOW is
Present Continuous — one action, happening in this window of time.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Present Simple — always / in general</p>
    <ul>
      <li>Sherbek <b>plays</b> football every Sunday.</li>
      <li>Water <b>boils</b> at 100°.</li>
      <li>She <b>lives</b> in Fergana.</li>
      <li>Signals: <em>always, usually, every day, on Mondays, never</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Present Continuous — now / temporarily</p>
    <ul>
      <li>Sherbek <b>is playing</b> football right now.</li>
      <li>The water <b>is boiling</b> — turn it off!</li>
      <li>She <b>is living</b> with us this month.</li>
      <li>Signals: <em>now, at the moment, today, this week, Look!</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">My mother <b>works</b> in a school, but this week she
     <b>is working</b> from home.</p>
  <p class="pe-ex__uz">Onam maktabda ishlaydi, lekin bu hafta uyda ishlayapti.</p>
  <p class="pe-ex__why">One sentence, both tenses: the permanent fact, then the temporary
     exception.</p>
</div>

<h3>2. Stative verbs — the ones that never take -ing</h3>

<p>Some verbs do not describe an <b>action</b> at all. They describe a state: something inside
your head or heart that you cannot start and stop. English refuses to put these in the
Continuous, no matter how "now" the situation is.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Thinking</p>
    <p><em>know, understand, remember, forget, believe, mean</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Feelings</p>
    <p><em>like, love, hate, want, need, prefer</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Senses</p>
    <p><em>see, hear, smell, taste, sound, seem</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Belonging</p>
    <p><em>have (own), belong, own, cost, contain</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>know</b> the answer. She <b>wants</b> a new phone. This
     <b>belongs</b> to Jasur.</p>
  <p class="pe-ex__uz">Men javobni bilaman. U yangi telefon xohlaydi. Bu Jasurniki.</p>
  <p class="pe-ex__why">All of them are true <em>right now</em> — and all of them still use
     the Simple.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxshi xabar: bu yerda oʻzbekcha mantiqingiz sizga yordam beradi. Siz ham "bil<b>yapman</b>",
  "xohla<b>yapman</b>", "sev<b>yapman</b>" demaysiz — <em>bilaman</em>, <em>xohlayman</em>,
  <em>sevaman</em> deysiz. Ingliz tilida ham xuddi shunday: <b>I know</b>, <b>I want</b>,
  <b>I love</b> — <s>I am knowing</s> emas.
</div>

<h3>3. Verbs with two lives</h3>

<p>A few verbs are stative in one meaning and active in another. When the meaning changes to a
real action, the Continuous becomes possible — and the sentence means something completely
different.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">State → Simple</p>
    <ul>
      <li>I <b>have</b> two brothers. <em>(own)</em></li>
      <li>I <b>think</b> he is right. <em>(opinion)</em></li>
      <li>The soup <b>tastes</b> salty.</li>
      <li>She <b>is</b> very kind. <em>(character)</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Action → Continuous</p>
    <ul>
      <li>I <b>am having</b> lunch. <em>(eating)</em></li>
      <li>I <b>am thinking</b> about you. <em>(mental activity)</em></li>
      <li>She <b>is tasting</b> the soup. <em>(trying it)</em></li>
      <li>He <b>is being</b> rude today. <em>(behaving so now)</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <em>I <b>am having</b> a car</em> is wrong, but <em>I <b>am having</b> a shower / lunch /
  a party / a good time</em> is perfect. The test: is <em>have</em> about owning, or about
  doing something?
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>see</b> a bird in that tree. — I <b>am looking</b> at the photos.</p>
  <p class="pe-ex__uz">Anavi daraxtda qushni koʻryapman. — Men suratlarni koʻryapman.</p>
  <p class="pe-ex__why"><em>See</em> and <em>hear</em> just happen to you (states);
     <em>look at</em> and <em>listen to</em> are things you choose to do (actions).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Mana bu tuzoq juda tez-tez uchraydi: oʻzbekchada "koʻr<b>yapman</b>", "eshit<b>yapman</b>"
  deymiz, shuning uchun <s>I am seeing</s>, <s>I am hearing</s> deb yozib qoʻyish oson.
  Toʻgʻrisi — <b>I see</b>, <b>I hear</b>. Agar ataylab qarayotgan yoki tinglayotgan
  boʻlsangiz, boshqa feʼl olinadi: <b>I am looking at…</b>, <b>I am listening to…</b>
</div>

<h3>4. The decision in three steps</h3>

<ol class="pe-steps">
  <li><b>Is the verb stative?</b> (know, like, want, have=own…) → Present Simple. Stop here.</li>
  <li><b>Is it happening now, or only for a short period?</b> → Present Continuous.</li>
  <li><b>Is it a habit, a fact, or a schedule?</b> → Present Simple.</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Imtihonlarda savol koʻpincha ishora soʻzlar orqali beriladi. Gapda <em>every day, usually,
  always</em> boʻlsa — Present Simple. <em>now, at the moment, Look!, this week</em> boʻlsa —
  Present Continuous. Ishora soʻzni topish — javobni topishning eng tez yoʻli.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I am knowing the answer.</s></p>
  <p class="pe-good">I <b>know</b> the answer.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She is wanting a cup of tea.</s></p>
  <p class="pe-good">She <b>wants</b> a cup of tea.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Look! He plays the guitar.</s></p>
  <p class="pe-good">Look! He <b>is playing</b> the guitar.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I am having a bike.</s></p>
  <p class="pe-good">I <b>have</b> a bike. <em>(but: I am having breakfast ✓)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Every morning I am going to school.</s></p>
  <p class="pe-good">Every morning I <b>go</b> to school.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>Afsona <span class="pe-blank">?</span> (wear) a beautiful dress today.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is wearing</strong> — <em>today</em> makes it temporary. Compare:
         <em>She usually <b>wears</b> jeans.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>I <span class="pe-blank">?</span> (not understand) this question.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>don't understand</strong> — <em>understand</em> is stative, so it never
         takes <b>-ing</b>, even though the problem is happening right now.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) I think it's a good idea. (b) I'm thinking about your
     idea.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) is my opinion</strong> ("menimcha") — a state.
         <strong>(b) is a mental activity happening now</strong> ("oʻylab koʻryapman").</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Fill both gaps: <em>Jasur normally <span class="pe-blank">?</span> (take) the bus, but
     today he <span class="pe-blank">?</span> (walk).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>takes … is walking.</strong> <em>Normally</em> → the habit; <em>today</em> →
         the exception happening now. This contrast is a favourite exam question.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Find the mistake: <em>Listen! Somebody knocks at the door.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Listen! Somebody is knocking at the door.</strong></p>
      <p><em>Listen!</em> opens a window on this exact moment, so the action must be in the
         Continuous.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Stative verb</b><span>holat feʼli</span></li>
  <li><b>Action verb</b><span>harakat feʼli</span></li>
  <li><b>State</b><span>holat</span></li>
  <li><b>Signal word</b><span>ishora soʻz</span></li>
  <li><b>Temporary</b><span>vaqtinchalik</span></li>
  <li><b>To own</b><span>egalik qilmoq</span></li>
  <li><b>To belong to</b><span>tegishli boʻlmoq</span></li>
  <li><b>Opinion</b><span>fikr</span></li>
  <li><b>To behave</b><span>oʻzini tutmoq</span></li>
  <li><b>Exception</b><span>istisno</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>General or repeated → <b>Simple</b>. Now or temporary → <b>Continuous</b>.</li>
    <li>Stative verbs (<b>know, like, want, need, see, have=own</b>) never take <b>-ing</b>.</li>
    <li>Uzbek helps you here: you don't say "bilyapman" either.</li>
    <li>Some verbs change meaning: <b>have</b> a car (own) vs <b>having</b> lunch (eating).</li>
    <li>Find the signal word first — it usually gives you the answer.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-14: have / have got: Talking About Possession",
        "category": "english",
        "order": 14,
        "summary": (
            "Two ways to say what you own, and when each one sounds natural — plus the have "
            "that means 'do', as in have breakfast and have a shower."
        ),
        "stories": ["The Boy Who Has Everything"],
        "content": """
<h2>PE-14: have / have got: Talking About Possession</h2>

<p>In Uzbek, owning something is easy: <em>Menda velosiped <b>bor</b>.</em> English does not
use "there is" for this — it uses a verb. And it gives you two of them:
<em>I <b>have</b> a bike</em> and <em>I've <b>got</b> a bike</em>. Both are correct. This
lesson shows you when each one sounds natural, and why <em>have</em> is secretly two
different verbs.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The two forms — <b>have</b> and <b>have got</b> — and their negatives and questions</li>
    <li>Which one to use in speaking, in writing, and in an exam</li>
    <li>The other <b>have</b>: <em>have breakfast, have a shower, have a good time</em></li>
    <li>Why <em>he's</em> can mean two completely different things</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two ways, one meaning</span>
  <span class="pe-chip pe-chip--s">I / you / we / they</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">have (got)</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">he / she / it</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">has (got)</span>
</div>

LEGEND_HERE

<h3>1. The two forms</h3>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">have</span> two sisters. =
     <span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">'ve got</span> two sisters.</p>
  <p class="pe-ex__uz">Mening ikkita opam bor.</p>
</div>

<p>Notice that <b>have got</b> is almost always shortened in speech: <em>I've got, you've got,
he's got, we've got, they've got</em>. Saying the full "I have got" sounds heavy.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada egalik <b>"-da ... bor"</b> orqali beriladi: "Men<b>da</b> mashina <b>bor</b>".
  Ingliz tilida esa bu <b>feʼl</b> bilan ifodalanadi va ega — buyum egasi:
  <em><b>I have</b> a car</em>. <s>By me is a car</s> yoki <s>There is a car by me</s>
  deyilmaydi.
</div>

<h3>2. Negatives and questions — the two systems</h3>

<p>This is where the two forms really separate. <b>Have</b> behaves like an ordinary verb and
needs <em>do/does</em>. <b>Have got</b> behaves like a helper and inverts by itself.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">have → needs do / does</p>
    <ul>
      <li><b>Do</b> you <b>have</b> a pen?</li>
      <li><b>Does</b> she <b>have</b> a car?</li>
      <li>I <b>don't have</b> time.</li>
      <li>Short answer: <em>Yes, I do.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">have got → inverts by itself</p>
    <ul>
      <li><b>Have</b> you <b>got</b> a pen?</li>
      <li><b>Has</b> she <b>got</b> a car?</li>
      <li>I <b>haven't got</b> time.</li>
      <li>Short answer: <em>Yes, I have.</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Never mix the two systems. <s>Do you have got a pen?</s> and <s>Have you a pen?</s> are both
  wrong (the second one was correct 100 years ago — you may meet it in old books).
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>don't have</b> any money. = I <b>haven't got</b> any money.</p>
  <p class="pe-ex__uz">Mening pulim yoʻq.</p>
  <p class="pe-ex__why">Two systems, one meaning — but never <s>I don't have got</s>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  "Menda pul <b>yoʻq</b>" ni ikki xil aytish mumkin: <b>I don't have</b> money (yordamchi feʼl
  bilan) yoki <b>I haven't got</b> money (<em>have</em> ning oʻzi yordamchi vazifasini
  bajaradi). Ikkalasini <b>aralashtirmang</b> — bittasini tanlang va oxirigacha shu tizimda
  qoling.
</div>

<h3>3. Which one should you use?</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Speaking, British</p>
    <p><em>have got</em> — <em>I've got a headache.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Writing &amp; exams</p>
    <p><em>have</em> — safer and more formal.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>American English</p>
    <p><em>have</em> — <em>Do you have a minute?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Past or future</p>
    <p><b>only <em>have</em></b> — <em>I had a bike.</em> <s>I had got</s></p>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  <b>Have got</b> lives in the present only. The moment you move into the past or the future,
  it disappears and plain <em>have</em> takes over: <em>I <b>had</b> long hair when I was
  ten. I <b>will have</b> more time next week.</em> If you are unsure, use <b>have</b> — it
  is never wrong.
</div>

<h3>4. The other "have" — actions, not possession</h3>

<p>English also uses <b>have</b> to mean "do" or "experience", in dozens of everyday phrases.
In this meaning you can <b>never</b> add <em>got</em>, and it <b>can</b> take <b>-ing</b>
(remember PE-13).</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>have breakfast</b> at seven, then I <b>have a shower</b>. Right
     now Sherbek <b>is having</b> a English lesson.</p>
  <p class="pe-ex__uz">Men soat yettida nonushta qilaman, keyin dush qabul qilaman. Hozir
     Sherbek ingliz tili darsida.</p>
</div>

<p>Common ones worth learning as whole phrases: <em>have breakfast / lunch / dinner, have a
shower, have a rest, have a look, have a good time, have a party, have a problem, have
fun</em>.</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu iboralarda <b>have</b> "ega boʻlmoq" degani emas, "qilmoq" degani:
  <em>have breakfast</em> = nonushta <b>qilmoq</b>, <em>have a shower</em> = dush
  <b>qabul qilmoq</b>, <em>have a rest</em> = <b>dam olmoq</b>. Shuning uchun ularga
  <em>got</em> qoʻshilmaydi: <s>I've got breakfast at 7</s> — notoʻgʻri.
</div>

<h3>5. The "he's" trap</h3>

<p>The short form <b>'s</b> hides two different words. Look at what comes after it:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">'s = is</p>
    <p><em>He<b>'s</b> a doctor.</em> (He is)</p>
    <p><em>She<b>'s</b> reading.</em> (She is)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">'s = has</p>
    <p><em>He<b>'s got</b> a car.</em> (He has)</p>
    <p><em>She<b>'s got</b> blue eyes.</em> (She has)</p>
  </div>
</div>

<p>The rule is simple: if the word after <b>'s</b> is <em>got</em>, then <b>'s = has</b>.</p>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have got 15 years.</s></p>
  <p class="pe-good">I <b>am</b> 15 (years old). <em>(age uses "be" — see PE-6)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you have got a brother?</s></p>
  <p class="pe-good"><b>Have you got</b> a brother? / <b>Do you have</b> a brother?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She don't have a phone.</s></p>
  <p class="pe-good">She <b>doesn't have</b> a phone. / She <b>hasn't got</b> a phone.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I've got a shower every morning.</s></p>
  <p class="pe-good">I <b>have</b> a shower every morning.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Last year I had got a bicycle.</s></p>
  <p class="pe-good">Last year I <b>had</b> a bicycle.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Say it both ways: <em>Afsona owns a laptop.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona has a laptop. = Afsona has got (Afsona's got) a laptop.</strong></p>
      <p>She → <b>has</b>, not <em>have</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make two questions from: <em>You have a dictionary.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Do you have a dictionary? / Have you got a dictionary?</strong></p>
      <p>Two systems, never mixed. <s>Do you have got…</s> ✗</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Does <b>'s</b> mean <em>is</em> or <em>has</em>?
     <em>(a) Jasur's got two dogs. (b) Jasur's at home.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) has</strong> (because <em>got</em> follows), <strong>(b) is</strong>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>I've got lunch at school every day.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I have lunch at school every day.</strong></p>
      <p>Here <em>have</em> means "eat", not "own", so <b>got</b> is impossible.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which is wrong, and why? <em>(a) When I was small, I had a red bike. (b) When I was
     small, I had got a red bike.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) is wrong.</strong> <em>Have got</em> exists only in the present. In the
         past, use plain <b>had</b>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Possession</b><span>egalik</span></li>
  <li><b>To own</b><span>ega boʻlmoq</span></li>
  <li><b>Have got</b><span>bor (soʻzlashuvda)</span></li>
  <li><b>Short form</b><span>qisqa shakl</span></li>
  <li><b>Formal</b><span>rasmiy</span></li>
  <li><b>Informal</b><span>norasmiy</span></li>
  <li><b>Have a shower</b><span>dush qabul qilmoq</span></li>
  <li><b>Have a rest</b><span>dam olmoq</span></li>
  <li><b>Have a look</b><span>koʻrib chiqmoq</span></li>
  <li><b>Have a good time</b><span>yaxshi vaqt oʻtkazmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>I have</b> = <b>I've got</b>. Same meaning; <em>got</em> is more spoken/British.</li>
    <li><b>have</b> → questions with <em>do/does</em>. <b>have got</b> → inverts by itself.</li>
    <li><b>have got</b> is present only — the past is always <b>had</b>.</li>
    <li>Action <em>have</em> (<b>have breakfast, have a shower</b>) never takes <em>got</em>.</li>
    <li>If <b>'s</b> is followed by <em>got</em>, it means <b>has</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-15: Adjectives: Meaning, Position and Order",
        "category": "english",
        "order": 15,
        "summary": (
            "Where adjectives go, why they never take -s, the native order of 'a beautiful old "
            "Uzbek silk carpet', and the bored/boring difference that changes what you say."
        ),
        "stories": ["A Small Old Blue Bicycle"],
        "content": """
<h2>PE-15: Adjectives: Meaning, Position and Order</h2>

<p>Say <em>a beautiful old Uzbek silk carpet</em> to a native speaker and it sounds perfect.
Say <em>a silk Uzbek old beautiful carpet</em> and it sounds broken — even though every word
is correct. English has a hidden order for adjectives that natives never learn at school; they
just feel it. In fifteen minutes you can know it consciously, which is better.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The two places an adjective can stand</li>
    <li>Why English adjectives never take <b>-s</b></li>
    <li>The native order: <b>opinion → size → age → shape → colour → origin → material</b></li>
    <li>The difference between <b>bored</b> and <b>boring</b> — and why it matters</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two positions</span>
  <span class="pe-chip pe-chip--o">adjective</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">noun</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">noun</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">be / seem / look</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">adjective</span>
</div>

LEGEND_HERE

<h3>1. Where adjectives live</h3>

<p>An adjective describes a noun, and it can do that from two places: right <b>in front of</b>
the noun, or <b>after</b> a linking verb such as <em>be, seem, look, feel, sound, taste,
become, get</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Before the noun: This is a <span class="pe-hl pe-hl--o">difficult</span>
     question. — After a linking verb: This question
     <span class="pe-hl pe-hl--v">is</span> <span class="pe-hl pe-hl--o">difficult</span>.</p>
  <p class="pe-ex__uz">Bu qiyin savol. — Bu savol qiyin.</p>
</div>

<p>What English will <b>not</b> do is put the adjective after the noun the way many languages
can: <s>a car red</s>, <s>a girl beautiful</s>. The adjective goes in front, always.</p>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  Adjectives in English <b>never change</b> — no plural, no gender: <em>a tall boy</em>,
  <em>two <b>tall</b> boys</em>, <em>a <b>tall</b> girl</em>. Writing <s>talls boys</s> is one
  of the most visible learner mistakes.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda oʻzbek tili sizga yordam beradi: oʻzbekchada ham sifat oʻzgarmaydi —
  <em>baland boʻyli bola</em>, <em>baland boʻyli bola<b>lar</b></em>: "balandlar" deyilmaydi.
  Ingliz tilida ham xuddi shunday. Ammo bir farq bor: oʻzbekchada sifat otdan <b>oldin</b>
  keladi va bu ingliz tiliga mos tushadi — shuning uchun <s>a car red</s> xatosidan
  qoʻrqmang.
</div>

<h3>2. The order of adjectives</h3>

<p>When you use two or more adjectives before a noun, English puts them in this sequence.
Learn it by the shape of the idea: the more <b>personal and changeable</b> the adjective, the
earlier it goes; the more it is a <b>permanent fact</b>, the closer it sits to the noun.</p>

<ol class="pe-steps">
  <li><b>Opinion</b> — what I think: <em>beautiful, nice, terrible, delicious</em></li>
  <li><b>Size</b> — <em>big, small, tall, short</em></li>
  <li><b>Age</b> — <em>new, old, young, ancient</em></li>
  <li><b>Shape &amp; colour</b> — <em>round, square · red, blue, white</em></li>
  <li><b>Origin</b> — where it is from: <em>Uzbek, Korean, Italian</em></li>
  <li><b>Material</b> — what it is made of: <em>silk, wooden, plastic, gold</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">a <b>beautiful</b> <b>old</b> <b>Uzbek</b> <b>silk</b> carpet —
     opinion, age, origin, material</p>
  <p class="pe-ex__uz">chiroyli, eski, oʻzbek ipak gilami</p>
  <p class="pe-ex__why">Try moving any word and read it aloud — you will hear that it breaks.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In real life you will rarely use more than <b>two or three</b> adjectives at once. The
  practical version of the rule is short: <b>opinion before fact</b>, and <b>colour before
  origin before material</b>. That covers 95% of sentences.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yana bir yaxshi xabar: oʻzbekchada ham sifatlar deyarli shu tartibda keladi —
  <em>chiroyli eski oʻzbek ipak gilami</em>. Yaʼni "fikr → yosh → kelib chiqishi → material".
  Demak bu qoidani noldan yodlashingiz shart emas: oʻzbekcha jumlani xayolan tuzing va shu
  tartibni ingliz tiliga koʻchiring.
</div>

<h3>3. -ed or -ing? The pair that changes your meaning</h3>

<p>Many adjectives come in two versions, and mixing them up can say something you did not
mean at all.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">-ed → how a PERSON feels</p>
    <ul>
      <li>I am <b>bored</b>. (zerikdim)</li>
      <li>She was <b>interested</b>.</li>
      <li>We are <b>tired</b>.</li>
      <li>He looked <b>surprised</b>.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">-ing → what the THING is like</p>
    <ul>
      <li>The lesson is <b>boring</b>. (zerikarli)</li>
      <li>The book was <b>interesting</b>.</li>
      <li>The journey is <b>tiring</b>.</li>
      <li>The news was <b>surprising</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <em>I am <b>boring</b></em> does not mean "I'm bored" — it means <b>"I am a boring
  person"</b>, and everyone around you will smile. Feelings take <b>-ed</b>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oddiy tekshiruv: <b>-ed</b> = "men shunday <b>his qilyapman</b>" (zerikkanman, charchaganman),
  <b>-ing</b> = "u narsa shunday <b>tabiatga ega</b>" (zerikarli, charchatadigan). Oʻzbekchada
  ham shu farq bor: <em>qiziq<b>qan</b></em> (odam) va <em>qiziq<b>arli</b></em> (kitob) —
  shu mantiqni ingliz tiliga koʻchiring.
</div>

<h3>4. Two useful extras</h3>

<p><b>Nouns can work as adjectives.</b> When a noun describes another noun, it comes first and
stays singular: <em>a <b>school</b> bag</em>, <em>a <b>football</b> match</em>, <em>a
<b>three-year</b> course</em> (not <s>three-years</s>).</p>

<p><b>Very and really go before the adjective:</b> <em>a <b>very</b> difficult exam</em>,
<em>She is <b>really</b> kind.</em></p>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek has a <b>very</b> nice <b>new leather</b> school bag.</p>
  <p class="pe-ex__uz">Sherbekning juda chiroyli, yangi, charmdan tikilgan maktab sumkasi bor.</p>
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have two beautifuls sisters.</s></p>
  <p class="pe-good">I have two <b>beautiful</b> sisters.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She bought a car red.</s></p>
  <p class="pe-good">She bought a <b>red car</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>a red big old car</s></p>
  <p class="pe-good">a <b>big old red</b> car <em>(size → age → colour)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The film was bored.</s></p>
  <p class="pe-good">The film was <b>boring</b>. / I was <b>bored</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It is a shoes shop.</s></p>
  <p class="pe-good">It is a <b>shoe shop</b>. <em>(a noun used as an adjective stays singular)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Put in order: <em>Korean / a / small / lovely / car</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>a lovely small Korean car</strong> — opinion (lovely) → size (small) →
         origin (Korean).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>The three-hour lesson was very <span class="pe-blank">?</span>, so all the
     pupils were <span class="pe-blank">?</span>.</em> (tiring / tired)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>tiring … tired.</strong> The lesson has the quality (-ing); the people feel
         it (-ed).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>Afsona has two smalls dogs and a cat white.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona has two small dogs and a white cat.</strong></p>
      <p>Adjectives never take <b>-s</b>, and they stand before the noun.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What is the difference? <em>(a) I am interested. (b) I am interesting.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) = I want to know more</strong> (qiziqyapman).
         <strong>(b) = I am an interesting person</strong> (men qiziqarli odamman) — true,
         perhaps, but rarely what you meant to say!</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Describe your classroom in one sentence, using at least two adjectives.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Our classroom is a big bright room with new wooden
         desks.</em></p>
      <p>Order check: <em>big</em> (size) → <em>bright</em> (quality), and <em>new</em> (age)
         → <em>wooden</em> (material).</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Adjective</b><span>sifat</span></li>
  <li><b>To describe</b><span>tasvirlamoq</span></li>
  <li><b>Linking verb</b><span>bogʻlovchi feʼl</span></li>
  <li><b>Opinion</b><span>fikr, baho</span></li>
  <li><b>Size</b><span>oʻlcham</span></li>
  <li><b>Origin</b><span>kelib chiqishi</span></li>
  <li><b>Material</b><span>material, xomashyo</span></li>
  <li><b>Bored / boring</b><span>zerikkan / zerikarli</span></li>
  <li><b>Leather</b><span>charm</span></li>
  <li><b>Wooden</b><span>yogʻochdan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Adjective goes <b>before the noun</b>, or after <b>be / seem / look</b>.</li>
    <li>Adjectives <b>never</b> take <b>-s</b>: <em>two small dogs</em>.</li>
    <li>Order: <b>opinion → size → age → shape/colour → origin → material</b>.</li>
    <li><b>-ed</b> = how a person feels · <b>-ing</b> = what the thing is like.</li>
    <li>A noun describing a noun stays singular: <b>a shoe shop</b>, <b>a football match</b>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
