# -*- coding: utf-8 -*-
"""Prime English — Block A, lessons 6–10 (Foundations).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_06_10.py --author=prime
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
        "title": "PE-6: The Verb \"to be\": am / is / are",
        "category": "english",
        "order": 6,
        "summary": (
            "The most used verb in English. Learn am/is/are, their short forms, negatives, "
            "questions — and why Uzbek speakers keep forgetting to say it at all."
        ),
        "content": """
<h2>PE-6: The Verb "to be": am / is / are</h2>

<p>If you counted every verb spoken in English today, <b>to be</b> would win by a huge
distance. It tells people who you are, how you feel, where you are and what things are like.
And it is exactly the verb Uzbek speakers forget most often — because in Uzbek you simply do
not need it: <em>Men oʻquvchiman</em> has no separate "am" inside it.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Which form goes with which subject: <b>am, is, are</b></li>
    <li>The short forms native speakers actually use (<em>I'm, he's, they're</em>)</li>
    <li>How to make negatives and questions with <b>to be</b> — without any helper verb</li>
    <li>The jobs <b>to be</b> does: identity, age, feelings, place, weather</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">am / is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">the rest</span>
</div>

LEGEND_HERE

<h3>1. The three forms</h3>

<p>Only three forms cover every subject in English. Learn them as one small rhyme:
<em>I am, he is, they are.</em></p>

<div class="pe-table-wrap">
<table>
  <tr><th>Subject</th><th>Full form</th><th>Short form</th><th>Negative short form</th></tr>
  <tr><td>I</td><td>I am</td><td>I'm</td><td>I'm not</td></tr>
  <tr><td>he / she / it</td><td>he is</td><td>he's</td><td>he isn't</td></tr>
  <tr><td>you / we / they</td><td>you are</td><td>you're</td><td>you aren't</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">am</span> a student.
     <span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--v">is</span> my classmate.
     <span class="pe-hl pe-hl--s">We</span>
     <span class="pe-hl pe-hl--v">are</span> in the same group.</p>
  <p class="pe-ex__uz">Men oʻquvchiman. Afsona mening sinfdoshim. Biz bir guruhdamiz.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida "men oʻquvchi<b>man</b>", "u oʻquvchi" deymiz — alohida feʼl yoʻq. Ingliz
  tilida esa har bir gapda feʼl boʻlishi shart, shuning uchun <b>am / is / are</b> tushib
  qolmasligi kerak: <em>I <b>am</b> a student</em>, <em>She <b>is</b> a student</em>.
</div>

<h3>2. What "to be" is used for</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Who / what you are</p>
    <p>She <em>is</em> a doctor. This <em>is</em> my book.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Age</p>
    <p>Jasur <em>is</em> fifteen. I <em>am</em> sixteen years old.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Feelings &amp; qualities</p>
    <p>We <em>are</em> tired. The film <em>is</em> boring.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Place &amp; weather</p>
    <p>They <em>are</em> at home. It <em>is</em> cold today.</p>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Age uses <b>to be</b>, not <em>have</em>: <em>I <b>am</b> 15</em> ✓ — <s>I have 15
  years</s> ✗. The same for feelings: <em>I <b>am</b> hungry / cold / afraid</em>, not
  <s>I have hunger</s>.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Teskari xato ham bor: baʼzi soʻzlar oʻzbekchada sifatga oʻxshaydi, ingliz tilida esa
  <b>feʼl</b>. <em>Roziman</em> → <b>I agree</b>, <s>I am agree</s> emas. Xuddi shunday:
  <em>I remember</em>, <em>I understand</em>, <em>I need</em> — bularning oldiga
  <b>am/is/are</b> qoʻyilmaydi, chunki ular allaqachon feʼl.
</div>

<h3>3. Negatives — just add "not"</h3>

<p><b>To be</b> is special: it needs no helper. You simply put <b>not</b> straight after it.
(Every other verb will need <em>do/does</em> — you meet that in PE-10.)</p>

<div class="pe-formula">
  <span class="pe-formula__label">Negative</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">am / is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">not</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek <span class="pe-hl pe-hl--v">is</span>
     <span class="pe-hl pe-hl--neg">not</span> at school today. He
     <span class="pe-hl pe-hl--v">isn't</span> well.</p>
  <p class="pe-ex__uz">Sherbek bugun maktabda emas. U oʻzini yaxshi his qilmayapti.</p>
  <p class="pe-ex__why">Short forms: <em>is not → isn't</em>, <em>are not → aren't</em>.
     <em>Am not</em> has no short form — say <b>I'm not</b>.</p>
</div>

<h3>4. Questions — swap the first two words</h3>

<p>To ask a question, move <b>am / is / are</b> in front of the subject. Nothing else changes.
This is called <mark>inversion</mark>.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Question</span>
  <span class="pe-chip pe-chip--v">Am / Is / Are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">the rest</span>
  <span class="pe-op">?</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">You are ready. → <span class="pe-hl pe-hl--v">Are</span>
     <span class="pe-hl pe-hl--s">you</span> ready?</p>
  <p class="pe-ex__uz">Sen tayyorsan. → Sen tayyormisan?</p>
</div>

<p>Short answers follow a fixed pattern — and there is one trap in them:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Positive short answer — no contraction</p>
    <ul>
      <li>Are you tired? — <b>Yes, I am.</b> <s>Yes, I'm.</s></li>
      <li>Is she here? — <b>Yes, she is.</b></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Negative short answer — contraction is fine</p>
    <ul>
      <li>Are you tired? — <b>No, I'm not.</b></li>
      <li>Is she here? — <b>No, she isn't.</b></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  A short form can never end a sentence in English. That is why <em>Yes, I'm</em> sounds
  broken to a native ear — the word <b>am</b> needs to be heard fully at the end.
</div>

<h3>5. "It" and "there" — the two empty subjects</h3>

<p>Remember from PE-1 that English always fills the subject seat. With <b>to be</b> you will
constantly use <b>it</b> for weather, time and distance:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>It is</b> Monday. <b>It is</b> five o'clock. <b>It is</b> hot in
     Bukhara in July.</p>
  <p class="pe-ex__uz">Bugun dushanba. Soat besh. Iyulda Buxoroda issiq.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  "Soat besh", "Bugun issiq" kabi gaplarda oʻzbekchada ega yoʻq. Ingliz tilida esa
  <b>it</b> qoʻyiladi va u tarjima qilinmaydi: <em><b>It is</b> five o'clock</em>. Buni
  yodda tutsangiz, ob-havo va vaqt haqidagi barcha gaplaringiz toʻgʻri boʻladi.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I student at school 25.</s></p>
  <p class="pe-good">I <b>am</b> a student at school 25.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She have 14 years old.</s></p>
  <p class="pe-good">She <b>is</b> 14 <b>years old</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I am agree with you.</s></p>
  <p class="pe-good">I <b>agree</b> with you. <em>(agree is already a verb — no "am")</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yes, I'm. / He no is here.</s></p>
  <p class="pe-good"><b>Yes, I am.</b> / He <b>isn't</b> here.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You are ready? (in writing)</s></p>
  <p class="pe-good"><b>Are you</b> ready? <em>(a written question needs inversion)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Fill in am / is / are: <em>My parents <span class="pe-blank">?</span> teachers, and I
     <span class="pe-blank">?</span> in the ninth grade.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>are … am.</strong> <em>My parents</em> is plural → <b>are</b>; <em>I</em>
         always takes <b>am</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it a question: <em>Afsona is your sister.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Is Afsona your sister?</strong> Move <em>is</em> in front of the subject —
         no helper verb is needed with <b>to be</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is wrong here? <em>— Are you hungry? — Yes, I'm.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Yes, I am.</strong> A short form (<em>I'm, he's, they're</em>) can never end
         a sentence. Negative answers are different: <em>No, I'm not</em> ✓.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>Jasur have 16 years and he very tall.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur is 16 (years old) and he is very tall.</strong></p>
      <p>Two classic errors in one sentence: age takes <b>is</b>, not <em>have</em>; and an
         adjective (<em>tall</em>) still needs <b>is</b> in front of it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which sentences need <b>it</b>? <em>___ is raining. ___ is my bag. ___ is half past
     seven.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>All three: It is raining. It is my bag. It is half past seven.</strong></p>
      <p>In the second one <em>it</em> really points at the bag; in the other two it is just
         filling the subject seat.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Verb "to be"</b><span>boʻlmoq feʼli</span></li>
  <li><b>Short form</b><span>qisqa shakl</span></li>
  <li><b>Contraction</b><span>qisqartma (I'm)</span></li>
  <li><b>Negative</b><span>inkor</span></li>
  <li><b>Question</b><span>soʻroq gap</span></li>
  <li><b>Inversion</b><span>soʻz tartibini almashtirish</span></li>
  <li><b>Short answer</b><span>qisqa javob</span></li>
  <li><b>Age</b><span>yosh</span></li>
  <li><b>Adjective</b><span>sifat</span></li>
  <li><b>Empty subject</b><span>rasmiy ega (it)</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>I am · he/she/it is · you/we/they are</b> — three forms, no exceptions.</li>
    <li>Negative = <b>+ not</b>. Question = <b>swap</b> the subject and am/is/are. No helper verb.</li>
    <li>Never drop it: an adjective or a noun still needs <b>is/are</b> in front.</li>
    <li>Age and feelings use <b>be</b>, not <em>have</em>: <b>I am 15</b>, <b>I am hungry</b>.</li>
    <li><b>Yes, I am</b> — never <s>Yes, I'm</s>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-7: There is / There are",
        "category": "english",
        "order": 7,
        "summary": (
            "How to say that something exists — the English answer to 'bor' and 'yoʻq', with "
            "the agreement rule, negatives, questions and the there/it difference."
        ),
        "content": """
<h2>PE-7: There is / There are</h2>

<p>You want to describe your room. In Uzbek it is easy: <em>Xonamda stol bor.</em> Word by
word into English that becomes <s>In my room a table is</s> — and no English speaker says
that. English opens the sentence with a special phrase instead: <b>There is a table in my
room.</b> This one structure will serve you for the rest of your life.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>When to use <b>there is</b> and when to use <b>there are</b></li>
    <li>The list rule: which noun the verb agrees with</li>
    <li>Negatives and questions: <em>there isn't any / Are there any…?</em></li>
    <li>The difference between <b>there is</b> and <b>it is</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Something exists</span>
  <span class="pe-chip pe-chip--s">There</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">noun</span>
  <span class="pe-chip pe-chip--opt">(place)</span>
</div>

LEGEND_HERE

<h3>1. is or are? Look at the noun that follows</h3>

<p><b>There</b> is not the real subject here — it is a placeholder, exactly like the empty
<em>it</em> you met in PE-6. The verb agrees with the noun that comes <b>after</b> it.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">There</span>
     <span class="pe-hl pe-hl--v">is</span>
     <span class="pe-hl pe-hl--o">a big park</span> near our school.</p>
  <p class="pe-ex__uz">Maktabimiz yonida katta bogʻ bor.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">There</span>
     <span class="pe-hl pe-hl--v">are</span>
     <span class="pe-hl pe-hl--o">thirty pupils</span> in our class.</p>
  <p class="pe-ex__uz">Sinfimizda oʻttizta oʻquvchi bor.</p>
  <p class="pe-ex__why">Plural noun → <b>are</b>. Singular or uncountable → <b>is</b>.</p>
</div>

<p>Uncountable nouns (PE-2!) always take <b>is</b>: <em>There <b>is</b> some water in the
bottle. There <b>is</b> a lot of traffic today.</em></p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>There is / There are</b> — bu oʻzbekchadagi <b>bor</b> soʻzining ingliz tilidagi
  ifodasi, <b>there isn't / aren't</b> esa <b>yoʻq</b>. Eng muhimi: <em>there</em> soʻzi
  "u yerda" deb tarjima qilinmaydi — u shunchaki gapni boshlab beradi.
</div>

<h3>2. The list rule</h3>

<p>When you list several things, English is lazy: the verb agrees only with the <b>first</b>
noun in the list, because that is the one the speaker reaches first.</p>

<div class="pe-ex">
  <p class="pe-ex__en">There <b>is</b> a table and four chairs in the kitchen.</p>
  <p class="pe-ex__uz">Oshxonada stol va toʻrtta stul bor.</p>
  <p class="pe-ex__why">First noun = <em>a table</em> (singular) → <b>is</b>, even though
     chairs follow.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">There <b>are</b> four chairs and a table in the kitchen.</p>
  <p class="pe-ex__uz">Oshxonada toʻrtta stul va stol bor.</p>
  <p class="pe-ex__why">Reverse the order and the verb changes too. Both sentences are correct.</p>
</div>

<h3>3. Negatives and questions</h3>

<ol class="pe-steps">
  <li><b>Negative:</b> add <em>not</em> to the verb, and use <b>any</b> with plurals and
      uncountables — <em>There <b>isn't</b> a shop here. There <b>aren't any</b> tickets
      left.</em></li>
  <li><b>Question:</b> swap <em>there</em> and the verb — <em><b>Is there</b> a bank near
      here? <b>Are there any</b> questions?</em></li>
  <li><b>Short answers:</b> <em>Yes, there is. / No, there isn't. / Yes, there are. /
      No, there aren't.</em></li>
</ol>

<p>Two more useful negatives mean the same thing: <em>There <b>isn't any</b> milk</em> =
<em>There <b>is no</b> milk.</em> The second sounds a little stronger.</p>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In speech you will hear <em>there's</em> everywhere — even before plurals
  (<em>there's two people outside</em>). Understand it, but do not copy it in writing or in
  an exam: write <b>there are</b>.
</div>

<h3>4. "There is" vs "It is" — a pair worth 10 marks</h3>

<p>Use <b>there is</b> to say that something <em>exists</em>, for the first time. Use
<b>it is</b> to say something <em>about</em> a thing you have already introduced.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">There is — introduces</p>
    <p><b>There is</b> a new café in our street.</p>
    <p><b>There is</b> a problem.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">It is — describes</p>
    <p><b>It is</b> very cheap and quiet.</p>
    <p><b>It is</b> not serious.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>There is</b> a letter on your desk. <b>It is</b> from your school.</p>
  <p class="pe-ex__uz">Stolingizda xat bor. U maktabingizdan kelgan.</p>
  <p class="pe-ex__why">Sentence 1 announces the letter; sentence 2 talks about that same letter.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoida oddiy: birinchi marta "bor" deyayotgan boʻlsangiz — <b>there is/are</b>. Oʻsha
  narsa haqida keyin gapirsangiz — <b>it is</b> yoki <b>they are</b>. Bu PE-4 dagi
  <em>a → the</em> qoidasiga juda oʻxshaydi.
</div>

<h3>5. Where does the place go?</h3>

<p>The place phrase normally comes at the end. Putting it first is possible but sounds
literary, and the verb order still cannot be Uzbek order.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>In my room is a big window.</s></p>
  <p class="pe-good"><b>There is</b> a big window in my room.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada joy birinchi keladi: <em><b>Xonamda</b> stol bor</em>. Ingliz tilida esa
  gap <b>there</b> bilan boshlanadi va joy oxirida keladi: <em><b>There is</b> a table
  <b>in my room</b></em>. Soʻzma-soʻz tarjima qilmang — shablonni butunligicha yodlang.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>There are a lot of furnitures in the room.</s></p>
  <p class="pe-good">There <b>is</b> a lot of <b>furniture</b> in the room. <em>(uncountable)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Have many people in the bazaar.</s></p>
  <p class="pe-good"><b>There are</b> many people in the bazaar.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>There is five days in a school week.</s></p>
  <p class="pe-good">There <b>are</b> five days in a school week.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Is there some milk? / There aren't some eggs.</s></p>
  <p class="pe-good"><b>Is there any</b> milk? / There aren't <b>any</b> eggs.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>It is a mistake in your homework.</s></p>
  <p class="pe-good"><b>There is</b> a mistake in your homework.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     is / are: <em>There <span class="pe-blank">?</span> a sofa, two armchairs and a carpet
     in the living room.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is</strong> — the list rule: the verb agrees with the first noun,
         <em>a sofa</em>, which is singular.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it negative: <em>There is some sugar in the tea.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>There isn't any sugar in the tea.</strong> (or <em>There is no sugar…</em>)</p>
      <p><b>Some</b> becomes <b>any</b> in negatives and questions.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     There is or It is? <em>___ a good film on TV tonight. ___ about a young doctor.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>There is … It is.</strong> The first sentence announces that the film
         exists; the second describes that same film.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Translate: <em>Bizning maktabimizda kutubxona yoʻq.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>There isn't a library in our school.</strong>
         (also correct: <em>There is no library in our school</em>.)</p>
      <p><em>Yoʻq</em> = <b>there isn't / there aren't</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Ask a question and answer it: <em>… any milk in the fridge? (no)</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Is there any milk in the fridge? — No, there isn't.</strong></p>
      <p><em>Milk</em> is uncountable → <b>is</b>, and the short answer repeats
         <em>there + verb</em>, never the noun.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>There is / are</b><span>bor</span></li>
  <li><b>There isn't</b><span>yoʻq</span></li>
  <li><b>To exist</b><span>mavjud boʻlmoq</span></li>
  <li><b>Placeholder</b><span>oʻrinbosar soʻz</span></li>
  <li><b>To agree (verb)</b><span>moslashmoq</span></li>
  <li><b>Any</b><span>hech qanday / biror</span></li>
  <li><b>To introduce</b><span>tanishtirmoq, kiritmoq</span></li>
  <li><b>Furniture</b><span>mebel</span></li>
  <li><b>Fridge</b><span>muzlatgich</span></li>
  <li><b>Left (remaining)</b><span>qolgan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>There is</b> + singular / uncountable · <b>There are</b> + plural.</li>
    <li>In a list, the verb agrees with the <b>first</b> noun.</li>
    <li>Negative: <b>isn't/aren't any</b> (= <b>is no</b>). Question: <b>Is/Are there…?</b></li>
    <li><b>There is</b> introduces something new; <b>it is</b> describes it afterwards.</li>
    <li>Never start with the place: <s>In my room is…</s> → <b>There is … in my room.</b></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-8: This, That, These, Those",
        "category": "english",
        "order": 8,
        "summary": (
            "Four little words that point: near or far, one or many — plus how English uses "
            "them on the phone, in time expressions and when introducing people."
        ),
        "content": """
<h2>PE-8: This, That, These, Those</h2>

<p>Point at something on your desk, then at something across the classroom. English gives you
four words for that finger: <b>this, that, these, those</b>. They are easy — there are only
two questions to answer — but they hide a few surprises, like the fact that English people
answer the phone with <em>"This is Afsona"</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The 2×2 system: <b>near / far</b> × <b>one / many</b></li>
    <li>The difference between <em>this book</em> and <em>This is my book</em></li>
    <li>How English uses these words for <b>time</b>, not only for distance</li>
    <li>Phone and introduction phrases every learner needs</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two questions, one answer</span>
  <span class="pe-chip pe-chip--s">near or far?</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">one or many?</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">this / that / these / those</span>
</div>

<h3>1. The whole system in one picture</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">👉 Near me (here)</p>
    <ul>
      <li><b>this</b> + one thing — <em>this pen</em></li>
      <li><b>these</b> + many things — <em>these pens</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">👈 Far from me (there)</p>
    <ul>
      <li><b>that</b> + one thing — <em>that building</em></li>
      <li><b>those</b> + many things — <em>those buildings</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>This</b> is my pen and <b>that</b> is yours.
     <b>These</b> books are new, but <b>those</b> books over there are old.</p>
  <p class="pe-ex__uz">Bu mening ruchkam, u esa seniki. Bu kitoblar yangi, ammo anavi
     kitoblar eski.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Hear the spelling in the sound: <b>th<u>i</u>s / th<u>e</u>se</b> — the plural has the long
  "ee" sound, like <em>bees</em>. <b>Th<u>a</u>t / th<u>o</u>se</b> — the plural has the "o"
  sound, like <em>nose</em>.
</div>

<h3>2. Two jobs: with a noun, or standing alone</h3>

<p>These four words can sit in front of a noun (like <em>my</em> or <em>the</em>), or replace
the noun completely and stand alone.</p>

<div class="pe-ex">
  <p class="pe-ex__en">With a noun: <b>This shirt</b> is expensive. — Alone:
     <b>This</b> is expensive.</p>
  <p class="pe-ex__uz">Bu koʻylak qimmat. — Bu qimmat.</p>
</div>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  The number must match on both sides: <b>this / that</b> go with a singular noun and a
  singular verb; <b>these / those</b> go with a plural noun and a plural verb.
  <em>This is…</em> / <em>These are…</em>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda asosiy xato shu: oʻzbekchada <em>bu kitob</em> va <em>bu kitoblar</em> — "bu"
  soʻzi oʻzgarmaydi. Ingliz tilida esa <b>soʻzning oʻzi oʻzgaradi</b>: <em>this book</em> →
  <em><b>these</b> books</em>, <em>that shoe</em> → <em><b>those</b> shoes</em>. Otni
  koʻplikka qoʻysangiz, koʻrsatish olmoshini ham koʻplikka qoʻying.
</div>

<h3>3. Careful with the ones that are always plural</h3>

<p>A few everyday things are plural in English even though they are one object:
<em>trousers, jeans, glasses, scissors, shorts</em>. They always take <b>these/those</b> and
a plural verb.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>These jeans are</b> too big, but <b>those glasses are</b> perfect.</p>
  <p class="pe-ex__uz">Bu jinsi shim juda katta, lekin anavi koʻzoynak juda mos.</p>
  <p class="pe-ex__why">To count them, use <em>a pair of</em>: <b>a pair of</b> jeans,
     <b>two pairs of</b> scissors.</p>
</div>

<h3>4. Not only distance — English also points in time</h3>

<p>This is the part learners rarely get taught. <b>This/these</b> = near <em>now</em>;
<b>that/those</b> = away in the past.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Now / soon</p>
    <p><em>this week, this morning, these days</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Then / the past</p>
    <p><em>that year, in those days, at that time</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>On the phone</p>
    <p><em>Hello, <b>this is</b> Jasur. Who's <b>that</b>?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Introducing people</p>
    <p><em><b>This is</b> my friend Sherbek.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>These days</b> everyone has a phone. In <b>those days</b> we wrote
     letters.</p>
  <p class="pe-ex__uz">Hozirgi kunlarda hammada telefon bor. Oʻsha paytlarda biz xat
     yozardik.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Odamni tanishtirganda oʻzbekchada "Bu — mening doʻstim" deymiz va ingliz tilida ham xuddi
  shunday: <b>This is my friend</b> — <s>He is my friend</s> emas (birinchi marta
  tanishtirayotganda). Telefonda esa <b>This is Jasur</b> ("Men Jasurman") va
  <b>Who's that?</b> ("Siz kimsiz?") deyiladi — bu ingliz tilining oʻz odati.
</div>

<h3>5. "That" has a second life</h3>

<p>You will also meet <b>that</b> as a connecting word, with no pointing meaning at all:
<em>I think <b>that</b> you are right.</em> Do not confuse the two — you will study this
<em>that</em> properly in the relative-clause lessons (PE-58).</p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkita <b>that</b> bor: birinchisi — koʻrsatish olmoshi ("anavi"), ikkinchisi — gaplarni
  bogʻlovchi ("...ligini"). <em>I know <b>that</b> boy</em> = anavi bola. <em>I know
  <b>that</b> he is late</em> = kechikkanini bilaman. Maʼnodan farqlang.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>This books are interesting.</s></p>
  <p class="pe-good"><b>These</b> books are interesting.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>These is my brother.</s></p>
  <p class="pe-good"><b>This is</b> my brother.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>That are my shoes.</s></p>
  <p class="pe-good"><b>Those are</b> my shoes.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Hello, I am Jasur. (on the phone)</s></p>
  <p class="pe-good">Hello, <b>this is</b> Jasur.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This trousers are new.</s></p>
  <p class="pe-good"><b>These</b> trousers are new. <em>(trousers is always plural)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em><span class="pe-blank">?</span> apples in my hand are sweet, but
     <span class="pe-blank">?</span> apples on the tree are sour.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>These … those.</strong> In my hand = near → <em>these</em>; on the tree =
         far → <em>those</em>. Both nouns are plural.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>This are my new shoes.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>These are my new shoes.</strong> The noun is plural, so both the pointing
         word and the verb must be plural.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     You are introducing your sister to your teacher. What do you say?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>This is my sister, Afsona.</strong></p>
      <p>English introduces people with <b>this is</b>, not with <em>she is</em>. Use
         <em>she is</em> only after she has been introduced.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     this / that: <em>I am very busy <span class="pe-blank">?</span> week. I wasn't busy
     <span class="pe-blank">?</span> week.</em> (last week)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>this … that.</strong> Time works like distance: the week I am in is near
         (<em>this</em>), the finished week is far (<em>that</em>).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     What does <b>that</b> mean in each sentence?
     (a) <em>Give me that book.</em> (b) <em>She said that she was tired.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) points</strong> — "anavi kitobni". <strong>(b) connects</strong> two
         parts of a sentence and is not translated as "anavi" at all.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Demonstrative</b><span>koʻrsatish olmoshi</span></li>
  <li><b>To point at</b><span>koʻrsatmoq</span></li>
  <li><b>Near / far</b><span>yaqin / uzoq</span></li>
  <li><b>Over there</b><span>anavi yerda</span></li>
  <li><b>To introduce</b><span>tanishtirmoq</span></li>
  <li><b>These days</b><span>hozirgi kunlarda</span></li>
  <li><b>In those days</b><span>oʻsha paytlarda</span></li>
  <li><b>To replace</b><span>oʻrnini bosmoq</span></li>
  <li><b>Trousers</b><span>shim (doim koʻplik)</span></li>
  <li><b>Sour</b><span>nordon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Near → <b>this</b> (one) / <b>these</b> (many). Far → <b>that</b> / <b>those</b>.</li>
    <li>Match the number everywhere: <b>This is</b> … / <b>These are</b> …</li>
    <li>They point in time too: <b>this week</b> (now) vs <b>in those days</b> (past).</li>
    <li>Phone and introductions: <b>This is Jasur. Who's that?</b></li>
    <li><b>That</b> also works as a connector — a different word with the same spelling.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-9: Present Simple: Habits, Facts and Timetables",
        "category": "english",
        "order": 9,
        "summary": (
            "The tense of your everyday life. Learn when to use the Present Simple and master "
            "the one letter that causes more mistakes than any other: the third-person -s."
        ),
        "content": """
<h2>PE-9: Present Simple: Habits, Facts and Timetables</h2>

<p>What time do you get up? What does your father do? Where does your best friend live?
Every answer to those questions uses the <mark>Present Simple</mark> — the tense of routine,
of facts, of who you are. It is the first tense every learner meets, and it contains one tiny
letter that trips up learners for years: the <b>-s</b> on <em>he, she, it</em>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The four jobs of the Present Simple</li>
    <li>The third-person <b>-s</b> and its spelling rules</li>
    <li>Which time words go with this tense</li>
    <li>Why <em>The train leaves at 7</em> is about the future — and still Present Simple</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">I / you / we / they</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">he / she / it</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + s</span>
</div>

LEGEND_HERE

<h3>1. What this tense really means</h3>

<p>The Present Simple does not mean "now". It means <b>always, again and again, in general</b>.
Picture your action repeating along the whole timeline — before now, and after now too:</p>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:55%"></span>
    <span class="pe-tl-dot" style="left:12%"></span>
    <span class="pe-tl-dot" style="left:32%"></span>
    <span class="pe-tl-dot" style="left:55%"></span>
    <span class="pe-tl-dot" style="left:76%"></span>
    <span class="pe-tl-tag" style="left:32%">I go to school every day</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Habits &amp; routines</p>
    <p>I <em>get up</em> at seven. We <em>play</em> football on Sundays.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Permanent situations</p>
    <p>Afsona <em>lives</em> in Samarkand. He <em>works</em> in a bank.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>General truths</p>
    <p>Water <em>boils</em> at 100°. The sun <em>rises</em> in the east.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Timetables</p>
    <p>The train <em>leaves</em> at 6:40. The lesson <em>starts</em> at nine.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Present Simple oʻzbekchadagi <b>-adi / -ydi</b> shakliga toʻgʻri keladi: <em>Men har kuni
  maktabga bora<b>man</b></em> → <em>I <b>go</b> to school every day</em>. Diqqat: bu
  zamon "hozir shu daqiqada" degani emas — u <b>doim takrorlanadigan</b> ish uchun.
</div>

<h3>2. The third-person -s</h3>

<p>Here is the whole difficulty of this tense in one line: with <b>he, she, it</b> (or any
single person or thing — <em>Jasur, my sister, the dog, the school</em>), the verb takes
<b>-s</b>. Everywhere else the verb stays bare.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--v">work</span> hard. →
     <span class="pe-hl pe-hl--s">Sherbek</span>
     <span class="pe-hl pe-hl--v">works</span> hard.</p>
  <p class="pe-ex__uz">Men qattiq ishlayman. → Sherbek qattiq ishlaydi.</p>
</div>

<p>The spelling rules are the same ones you learned for plural nouns in PE-3 — one set of
rules, two uses:</p>

<ol class="pe-steps">
  <li><b>Most verbs: + s</b> — <em>read → reads, live → lives, play → plays</em></li>
  <li><b>After a hissing sound (s, sh, ch, x) and after o: + es</b> —
      <em>watch → watches, wash → washes, go → goes, do → does</em></li>
  <li><b>Consonant + y → ies</b> — <em>study → studies, fly → flies</em>
      (but <em>play → plays</em>, because <em>a</em> is a vowel)</li>
  <li><b>Two irregulars to memorise:</b> <em>have → <b>has</b></em> and
      <em>be → <b>is</b></em></li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu <b>-s</b> — ingliz tilini oʻrganayotganlarning eng koʻp xato qiladigan joyi, chunki
  oʻzbekchada uchinchi shaxs uchun alohida qoʻshimcha yoʻq: "men boraman", "u boradi" —
  ikkalasida ham feʼl bir xil oʻzgaradi. Ingliz tilida esa faqat <b>he/she/it</b> uchun
  <b>-s</b> qoʻshiladi, qolgan hamma shaxslarda feʼl yalangʻoch qoladi.
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  When you check your writing, do one pass looking <b>only</b> at he/she/it sentences. Ask:
  "one person? present? — then where is my <b>-s</b>?" Ten seconds of checking removes the
  most visible mistake in your English.
</div>

<h3>3. Time words that live with this tense</h3>

<p>These signal words almost always mean Present Simple: <em>always, usually, often,
sometimes, never, every day / week / year, on Mondays, twice a month, in the morning</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">My mother <b>cooks</b> plov <b>every Sunday</b>, and we
     <b>eat</b> together.</p>
  <p class="pe-ex__uz">Onam har yakshanba palov pishiradi va biz birga ovqatlanamiz.</p>
</div>

<p>Short adverbs like <em>always, usually, never</em> go <b>before</b> the main verb, but
<b>after</b> <em>am/is/are</em>. (Full lesson: PE-11.)</p>

<div class="pe-ex">
  <p class="pe-ex__en">She <b>always</b> helps me. — She <b>is always</b> late.</p>
  <p class="pe-ex__uz">U doim menga yordam beradi. — U doim kechikadi.</p>
</div>

<h3>4. The timetable future</h3>

<p>English uses the Present Simple for events on a fixed schedule, even when they happen
tomorrow. If a timetable, a programme or a calendar decides it, use Present Simple.</p>

<div class="pe-ex">
  <p class="pe-ex__en">The bus <b>leaves</b> at 6:40 tomorrow. Our exam <b>starts</b> on
     Monday.</p>
  <p class="pe-ex__uz">Ertaga avtobus 6:40 da joʻnaydi. Imtihonimiz dushanba kuni boshlanadi.</p>
  <p class="pe-ex__why">Nobody's decision — the schedule is fixed. That is why it is not "will".</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qoida siz uchun tanish: oʻzbekchada ham jadval haqida gapirganda hozirgi zamon
  ishlatiladi — <em>Ertaga poyezd oltida <b>joʻnaydi</b></em>, "joʻnaydi boʻladi" emas.
  Ingliz tili ham xuddi shunday yoʻl tutadi, shuning uchun bu joyda oʻzbekcha
  mantiqingizga ishoning.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>My father work in a hospital.</s></p>
  <p class="pe-good">My father <b>works</b> in a hospital.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She haves two brothers.</s></p>
  <p class="pe-good">She <b>has</b> two brothers.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He studys English and gos to college.</s></p>
  <p class="pe-good">He <b>studies</b> English and <b>goes</b> to college.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>They lives in Andijan.</s></p>
  <p class="pe-good">They <b>live</b> in Andijan. <em>(-s only for he/she/it)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I am go to school every day.</s></p>
  <p class="pe-good">I <b>go</b> to school every day. <em>(never two verbs together)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Put the verb in the right form: <em>Afsona <span class="pe-blank">?</span> (study) at
     school number 12 and <span class="pe-blank">?</span> (want) to be a doctor.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>studies … wants.</strong> Afsona = she → both verbs need <b>-s</b>.
         <em>Study</em> ends in consonant + y, so it becomes <b>studies</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Which is correct and why? <em>(a) Water boils at 100°. (b) Water is boiling at 100°.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a)</strong> — a general truth that is always true, so Present Simple.
         Sentence (b) would mean water is boiling at this exact moment.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Add the -s where it is missing: <em>My brother go to the gym, play football and watch
     films.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My brother goes to the gym, plays football and watches films.</strong></p>
      <p>All three verbs belong to the same subject, so all three take the ending —
         <em>go<b>es</b></em>, <em>play<b>s</b></em>, <em>watch<b>es</b></em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Why is this Present Simple? <em>Our plane lands at 3 p.m. tomorrow.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Because it is a timetable.</strong> The airline's schedule decides it, not
         the speaker — so English uses the Present Simple even for tomorrow.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Where does <em>usually</em> go? <em>(a) Jasur ___ gets up ___ at six.
     (b) Jasur ___ is ___ tired in the evening.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) Jasur usually gets up at six — before the main verb.
         (b) Jasur is usually tired — after "is".</strong></p>
      <p>Rule: <em>before the verb, but after <b>am/is/are</b></em>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Present Simple</b><span>hozirgi oddiy zamon</span></li>
  <li><b>Habit</b><span>odat</span></li>
  <li><b>Routine</b><span>kundalik tartib</span></li>
  <li><b>Fact</b><span>haqiqat, dalil</span></li>
  <li><b>Third person</b><span>uchinchi shaxs</span></li>
  <li><b>Ending</b><span>qoʻshimcha</span></li>
  <li><b>Timetable</b><span>jadval</span></li>
  <li><b>Signal word</b><span>ishora soʻz</span></li>
  <li><b>Permanent</b><span>doimiy</span></li>
  <li><b>To boil</b><span>qaynamoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Present Simple = habits, permanent facts, general truths, timetables — <b>not</b> "now".</li>
    <li><b>he / she / it → verb + s.</b> Everyone else takes the bare verb.</li>
    <li>Spelling: <b>+es</b> after hissing sounds and <em>o</em>; consonant + y → <b>-ies</b>;
        <em>have → has</em>.</li>
    <li>Signal words: <b>always, usually, never, every day, on Mondays</b>.</li>
    <li>Fixed schedules use this tense even for the future: <em>The train leaves at 7.</em></li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-10: Present Simple: Negatives and Questions",
        "category": "english",
        "order": 10,
        "summary": (
            "Meet do and does — the helper verbs that build every Present Simple negative and "
            "question, and the golden rule that stops 'she doesn't works'."
        ),
        "content": """
<h2>PE-10: Present Simple: Negatives and Questions</h2>

<p>In PE-6 you saw that <b>to be</b> makes questions by itself: <em>Are you ready?</em> Every
other verb refuses to do that. You cannot say <s>Like you tea?</s> — English sends in a
helper: <b>do</b> and <b>does</b>. Learn how that helper behaves and you can ask about
anything in the present.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>How to build negatives with <b>don't / doesn't</b></li>
    <li>How to build questions with <b>Do / Does</b> and answer them shortly</li>
    <li>The golden rule: only <b>one</b> verb in a sentence carries the <b>-s</b></li>
    <li>Wh- questions, and the special case where <em>do</em> disappears</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Negative</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">do / does</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--neg">not</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb (no -s!)</span>
</div>
<div class="pe-formula">
  <span class="pe-formula__label">Question</span>
  <span class="pe-chip pe-chip--aux">Do / Does</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb (no -s!)</span>
  <span class="pe-op">?</span>
</div>

LEGEND_HERE

<h3>1. Choosing do or does</h3>

<p>The choice copies the rule you already know: <b>he, she, it</b> take <b>does</b>; everybody
else takes <b>do</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">don't</span>
     <span class="pe-hl pe-hl--v">like</span> coffee. —
     <span class="pe-hl pe-hl--s">She</span>
     <span class="pe-hl pe-hl--aux">doesn't</span>
     <span class="pe-hl pe-hl--v">like</span> coffee.</p>
  <p class="pe-ex__uz">Men qahvani yoqtirmayman. — U qahvani yoqtirmaydi.</p>
</div>

<h3>2. The golden rule</h3>

<div class="pe-call pe-rule">
  <span class="pe-call__t">Rule</span>
  Once <b>does</b> takes the <b>-s</b>, the main verb gives it up. Two verbs in one sentence
  never both carry the ending: <em>She <b>does</b>n't <b>like</b></em> ✓ —
  <s>She doesn't likes</s> ✗.
</div>

<p>Think of the <b>-s</b> as a single ball that only one player can hold. In a positive
sentence the main verb holds it (<em>she like<b>s</b></em>). As soon as the helper arrives,
the helper takes the ball (<em>doe<b>s</b> she like?</em>) and the main verb goes bare.</p>

<div class="pe-ex">
  <p class="pe-ex__en">He <b>works</b> here. → He <b>doesn't work</b> here. →
     <b>Does</b> he <b>work</b> here?</p>
  <p class="pe-ex__uz">U shu yerda ishlaydi. → U bu yerda ishlamaydi. → U shu yerda
     ishlaydimi?</p>
  <p class="pe-ex__why">Follow the <b>-s</b>: it moves from <em>works</em> onto
     <em>does</em>, and never appears twice.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida inkor va soʻroq feʼlning oʻzida yasaladi: ishla<b>ydi</b> → ishla<b>maydi</b>
  → ishlaydi<b>mi?</b> Ingliz tilida esa buning uchun <b>alohida yordamchi feʼl</b> kerak:
  <b>do / does</b>. Shuning uchun "She not like tea" yoki "Like she tea?" degan gaplar
  notoʻgʻri — yordamchi feʼlsiz gap qurilmaydi.
</div>

<h3>3. Short answers</h3>

<p>English almost never answers with a bare <em>Yes</em> or <em>No</em> — it repeats the
helper. This sounds polite and natural.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Positive</p>
    <ul>
      <li>Do you play chess? — <b>Yes, I do.</b></li>
      <li>Does he live here? — <b>Yes, he does.</b></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Negative</p>
    <ul>
      <li>Do they know? — <b>No, they don't.</b></li>
      <li>Does she smoke? — <b>No, she doesn't.</b></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Never repeat the main verb in a short answer: <s>Yes, I play.</s> Use the helper —
  <b>Yes, I do.</b> And never mix the two systems: <s>Do you are a student?</s> With
  <em>to be</em> there is no <em>do</em> at all — <b>Are you a student?</b>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qisqa javobda oʻzbekcha feʼlni takrorlaydi: "— Choy ichasanmi? — Ha, <b>ichaman</b>."
  Ingliz tilida esa <b>asosiy feʼl emas, yordamchi feʼl</b> takrorlanadi:
  "— Do you drink tea? — Yes, I <b>do</b>." Shu bitta odatni oʻzgartirsangiz,
  gaplaringiz darrov tabiiy eshitiladi.
</div>

<h3>4. Wh- questions</h3>

<p>Put the question word at the front; everything else keeps the same order.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Wh- question</span>
  <span class="pe-chip pe-chip--adv">Where / What / When</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">do / does</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb</span>
  <span class="pe-op">?</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Where do</b> you live? <b>What does</b> your father <b>do</b>?
     <b>When do</b> the lessons <b>start</b>?</p>
  <p class="pe-ex__uz">Qayerda yashaysan? Otangiz nima ish qiladi? Darslar qachon boshlanadi?</p>
  <p class="pe-ex__why">In <em>What does your father do?</em> the first <b>does</b> is the
     helper and the second <b>do</b> is the real verb ("to do a job").</p>
</div>

<h3>5. The one question that needs no helper</h3>

<p>When your question word <b>is</b> the subject — when you are asking <em>who</em> or
<em>what</em> does the action — there is nothing to invert, so <em>do/does</em> disappears
and the verb keeps its <b>-s</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Asking about the object — helper needed</p>
    <p><b>Who does</b> Afsona <b>help</b>?</p>
    <p>(Afsona helps somebody — who?)</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Asking about the subject — no helper</p>
    <p><b>Who helps</b> Afsona?</p>
    <p>(Somebody helps Afsona — who?)</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Agar <b>who / what</b> gapning <b>egasi</b> boʻlsa, <em>do/does</em> ishlatilmaydi va feʼl
  <b>-s</b> ni saqlab qoladi: <em>Who <b>lives</b> here?</em> ("Bu yerda kim yashaydi?"),
  <s>Who does live here?</s> emas. Bu qoidani bilsangiz, imtihonlarda bir nechta ballni
  yutasiz.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>She doesn't likes vegetables.</s></p>
  <p class="pe-good">She <b>doesn't like</b> vegetables.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do she speak English?</s></p>
  <p class="pe-good"><b>Does</b> she speak English?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Where you live? / Where do you live in?</s></p>
  <p class="pe-good"><b>Where do you live?</b></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I not know his name.</s></p>
  <p class="pe-good">I <b>don't know</b> his name.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Who does want tea?</s></p>
  <p class="pe-good"><b>Who wants</b> tea? <em>(who is the subject)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make it negative: <em>Sherbek watches TV in the evening.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sherbek doesn't watch TV in the evening.</strong></p>
      <p>The <b>-s</b> moves onto the helper (<em>does</em>), so <em>watches</em> becomes the
         bare <b>watch</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make a question: <em>Your parents speak Russian.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Do your parents speak Russian?</strong> <em>Parents</em> is plural →
         <b>do</b>, and the verb stays bare.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Answer shortly: <em>Does Afsona play the piano? (yes)</em> —
     <em>Do you like maths? (no)</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Yes, she does. — No, I don't.</strong></p>
      <p>Repeat the helper, never the main verb. <s>Yes, she plays.</s> is not a short answer.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which is right? <em>(a) Who does teach you English? (b) Who teaches you English?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) Who teaches you English?</strong> <em>Who</em> is the subject of the
         sentence, so no helper is used and the verb keeps its <b>-s</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Find and fix two mistakes: <em>Does your brother works in Tashkent? — No, he don't.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Does your brother work in Tashkent? — No, he doesn't.</strong></p>
      <p>(1) The main verb loses the <b>-s</b> after <em>does</em>. (2) The short answer must
         match the helper: <em>he</em> → <b>doesn't</b>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Helper (auxiliary) verb</b><span>yordamchi feʼl</span></li>
  <li><b>Negative</b><span>inkor gap</span></li>
  <li><b>Question form</b><span>soʻroq shakli</span></li>
  <li><b>Short answer</b><span>qisqa javob</span></li>
  <li><b>Wh- question</b><span>soʻroq soʻzli savol</span></li>
  <li><b>Bare verb</b><span>qoʻshimchasiz feʼl</span></li>
  <li><b>Subject question</b><span>egaga savol</span></li>
  <li><b>Word order</b><span>soʻz tartibi</span></li>
  <li><b>To invert</b><span>oʻrnini almashtirmoq</span></li>
  <li><b>Politely</b><span>xushmuomalalik bilan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Negative: <b>don't / doesn't + bare verb.</b> Question: <b>Do / Does + subject +
        bare verb?</b></li>
    <li>The <b>-s</b> is one ball: if <em>does</em> holds it, the main verb cannot.</li>
    <li>Short answers repeat the helper: <b>Yes, he does. No, they don't.</b></li>
    <li>Wh- word first, then the same order: <b>Where do you live?</b></li>
    <li>If <b>who/what</b> is the subject, use no helper: <b>Who wants tea?</b></li>
    <li><b>To be</b> never uses <em>do</em>: <b>Are you ready?</b>, not <s>Do you are…</s></li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
