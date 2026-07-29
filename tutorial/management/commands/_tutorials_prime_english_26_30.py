# -*- coding: utf-8 -*-
"""Prime English — Block B, lessons 26–30 (the future).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_26_30.py --author=prime
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
        "title": "PE-26: Future with \"will\": Decisions, Promises, Predictions",
        "category": "english",
        "order": 26,
        "summary": (
            "One word for every person, no endings to remember — and five different jobs, from "
            "deciding on the spot to promising, predicting and offering help."
        ),
        "content": """
<h2>PE-26: Future with "will": Decisions, Promises, Predictions</h2>

<p>The phone rings. Nobody moves. You say: <em>"I'<b>ll</b> get it!"</em> — and in that second
you have used the most typically English future there is. <mark>Will</mark> is the tense of
the decision you make <b>while you are speaking</b>. It is also the easiest structure in this
whole course: one word, no endings, the same for every person.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>will + base verb</b> — and why it never changes</li>
    <li><b>Won't</b>, <b>'ll</b> and the question form</li>
    <li>Five jobs: instant decisions, promises, predictions, offers, future facts</li>
    <li>The one place where <b>will</b> is forbidden</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive — same for everybody</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">will</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
  <span class="pe-chip pe-chip--opt">(no to, no -s, no -ing)</span>
</div>

LEGEND_HERE

<h3>1. The picture and the form</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:30%"></span>
    <span class="pe-tl-dot" style="left:68%"></span>
    <span class="pe-tl-tag" style="left:68%">I'll call you</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">will</span>
     <span class="pe-hl pe-hl--v">help</span> you. —
     <span class="pe-hl pe-hl--s">She</span>
     <span class="pe-hl pe-hl--aux">will</span>
     <span class="pe-hl pe-hl--v">help</span> you.</p>
  <p class="pe-ex__uz">Men senga yordam beraman. — U senga yordam beradi.</p>
  <p class="pe-ex__why">No <b>-s</b> for "she", no <em>to</em> before the verb. Nothing
     changes.</p>
</div>

<ol class="pe-steps">
  <li><b>Short form:</b> <em>I'll, you'll, he'll, we'll, they'll</em> — this is what people
      actually say.</li>
  <li><b>Negative:</b> <em>will not = <b>won't</b></em> — <em>I <b>won't</b> forget.</em></li>
  <li><b>Question:</b> <em><b>Will</b> you help me?</em> — <b>will</b> jumps in front of the
      subject.</li>
  <li><b>Short answers:</b> <em>Yes, I will. / No, I won't.</em></li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Will</b> oʻzbekchadagi <b>-aman / -adi</b> kelasi zamon shakliga toʻgʻri keladi:
  <em>bora<b>man</b></em> = <em>I <b>will go</b></em>. Va bu yerda ingliz tili osonroq:
  oʻzbekchada shaxsga qarab qoʻshimcha oʻzgaradi ("boraman/borasan/boradi"), ingliz tilida
  esa <b>hamma uchun bitta soʻz</b> — <b>will</b>. Feʼlga <b>-s</b> ham, <b>to</b> ham
  qoʻshilmaydi.
</div>

<h3>2. The five jobs</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Deciding right now</p>
    <p><em>It's cold. I <b>'ll close</b> the window.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Promises</p>
    <p><em>I <b>won't tell</b> anybody, I promise.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Predictions &amp; opinions</p>
    <p><em>I think our team <b>will win</b>.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Offers &amp; requests</p>
    <p><em><b>I'll carry</b> your bag. — <b>Will you</b> open the door?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>Future facts</p>
    <p><em>Afsona <b>will be</b> sixteen next month.</em></p>
  </div>
</div>

<p>Job 3 travels with a small family of words that show you are giving an opinion, not a
certainty: <em>I think, I hope, I'm sure, I expect, probably, maybe, perhaps</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I think it <b>will rain</b> tomorrow. She <b>probably won't come</b>
     to the party.</p>
  <p class="pe-ex__uz">Menimcha, ertaga yomgʻir yogʻadi. U bazmga, ehtimol, kelmaydi.</p>
  <p class="pe-ex__why">Notice where <em>probably</em> sits: <b>before</b> <em>will</em>, but
     <b>after</b> <em>won't</em>.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Native speakers rarely say the full <em>will</em> in a positive sentence — they say
  <em>I'll</em>, <em>we'll</em>, and it is very fast. But in a <b>short answer</b> the full
  word comes back: <em>Yes, I <b>will</b></em>, never <s>Yes, I'll</s>. Same rule as
  <em>Yes, I am</em> in PE-6.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— This bag is so heavy. — <b>I'll take</b> it. And don't worry,
     <b>I won't drop</b> it!</p>
  <p class="pe-ex__uz">— Bu sumka juda ogʻir. — Men olaman. Xavotir olmang, tushirib
     yubormayman!</p>
  <p class="pe-ex__why">An offer and a promise in two short sentences — the natural home of
     <em>will</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Taklif qilishning yana bir yoʻli — <b>Shall I …?</b> va <b>Shall we …?</b>
  "Yordam beraymi?" = <em><b>Shall I</b> help you?</em>, "Boraylikmi?" =
  <em><b>Shall we</b> go?</em> Bu <em>will</em> ning muloyim shakli boʻlib, faqat
  <b>I</b> va <b>we</b> bilan ishlatiladi.
</div>

<h3>3. The place where "will" is forbidden</h3>

<p>After the time words <b>when, as soon as, before, after, until, while</b> — and after
<b>if</b> — English does <b>not</b> use <em>will</em>, even though the meaning is clearly
future. It uses the Present Simple instead.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">✗ Wrong</p>
    <ul>
      <li><s>When I will arrive, I will call you.</s></li>
      <li><s>If it will rain, we will stay home.</s></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">✓ Right</p>
    <ul>
      <li>When I <b>arrive</b>, I <b>will call</b> you.</li>
      <li>If it <b>rains</b>, we <b>will stay</b> home.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qoida oʻzbek tilida yoʻq, shuning uchun uni alohida yodlash kerak: <b>when, if, as soon
  as, before, after, until</b> soʻzlaridan keyin <b>will ishlatilmaydi</b> — hozirgi zamon
  qoʻyiladi. "Uyga <b>borganimda</b> qoʻngʻiroq qilaman" → <em><b>When I get</b> home,
  I <b>will call</b> you</em>. Gapning faqat <b>bitta</b> yarmida <em>will</em> boʻladi.
</div>

<h3>4. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I will to help you.</s></p>
  <p class="pe-good">I <b>will help</b> you. <em>(no "to" after will)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He wills come tomorrow.</s></p>
  <p class="pe-good">He <b>will come</b> tomorrow. <em>(will never takes -s)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will going to the shop.</s></p>
  <p class="pe-good">I <b>will go</b> to the shop.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>When I will finish my homework, I will watch TV.</s></p>
  <p class="pe-good">When I <b>finish</b> my homework, I <b>will watch</b> TV.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>— Will you help me? — Yes, I'll.</s></p>
  <p class="pe-good">— Yes, <b>I will</b>.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Your friend's bag looks heavy. What do you say?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'll carry it for you.</strong></p>
      <p>An offer decided at this second — the classic job of <em>will</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>I think she will to pass the exam.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I think she will pass the exam.</strong></p>
      <p><em>Will</em> is followed by the bare verb — never by <em>to</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Fill in: <em>As soon as Jasur <span class="pe-blank">?</span> (arrive), we
     <span class="pe-blank">?</span> (start) the lesson.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>arrives … will start.</strong></p>
      <p>After <em>as soon as</em> comes the Present Simple; <em>will</em> stays in the other
         half of the sentence.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Make it negative: <em>I will forget your birthday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I won't forget your birthday.</strong></p>
      <p><em>Will not</em> shortens to <b>won't</b> — an old spelling that never became
         "willn't".</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which job of <em>will</em> is each? <em>(a) I'll never lie to you. (b) It'll be cold
     tonight. (c) I'll answer the door.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) a promise · (b) a prediction · (c) an instant decision.</strong></p>
      <p>Same word, three different reasons for using it.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Will</b><span>kelasi zamon yordamchisi</span></li>
  <li><b>Won't</b><span>...maydi (inkor)</span></li>
  <li><b>Prediction</b><span>bashorat</span></li>
  <li><b>Promise</b><span>vaʼda</span></li>
  <li><b>Offer</b><span>taklif</span></li>
  <li><b>Instant decision</b><span>shu zahoti qabul qilingan qaror</span></li>
  <li><b>Probably</b><span>ehtimol</span></li>
  <li><b>As soon as</b><span>...boʻlishi bilanoq</span></li>
  <li><b>To expect</b><span>kutmoq</span></li>
  <li><b>Time clause</b><span>payt ergash gapi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>will + base verb</b> — no <em>to</em>, no <b>-s</b>, no <b>-ing</b>, same for
        everyone.</li>
    <li><b>won't</b> = will not. Question: <b>Will you …?</b></li>
    <li>Five jobs: instant decisions, promises, predictions, offers, future facts.</li>
    <li>Opinion words travel with it: <em>I think, I'm sure, probably</em>.</li>
    <li>After <b>when, if, as soon as, until</b> → Present Simple, never <em>will</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-27: Future with \"be going to\": Plans and Evidence",
        "category": "english",
        "order": 27,
        "summary": (
            "The future you already decided on, and the future you can see coming. Learn "
            "be going to — the closest thing English has to Uzbek's -moqchiman."
        ),
        "content": """
<h2>PE-27: Future with "be going to": Plans and Evidence</h2>

<p>Yesterday you decided to study medicine. Today somebody asks about your future. You do not
say <em>"I'll study medicine"</em> — that would sound like you just thought of it this second.
You say <em>"I'<b>m going to</b> study medicine."</em> This structure carries one clear
message: <mark>the decision already exists</mark>. It is also what you use when you can
literally <b>see</b> the future coming.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>am / is / are + going to + base verb</b></li>
    <li>Its two jobs: prior plans, and predictions from present evidence</li>
    <li>How it differs from <b>will</b> in one sentence</li>
    <li>Why <em>going to go</em> is correct but rarely said</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">am / is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">going to</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
</div>

LEGEND_HERE

<h3>1. The picture: the decision is behind you</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:44%"></span>
    <span class="pe-tl-dot pe-tl-dot--x" style="left:18%"></span>
    <span class="pe-tl-dot" style="left:76%"></span>
    <span class="pe-tl-tag" style="left:18%">I decided</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>Red dot in the past: that is when you made up your mind. Blue dot in the future: that is
when it will happen. <b>Will</b> has no red dot at all — the decision is being made as you
speak.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">We</span>
     <span class="pe-hl pe-hl--aux">are going to</span>
     <span class="pe-hl pe-hl--v">visit</span> our grandparents this weekend. We bought the
     tickets last week.</p>
  <p class="pe-ex__uz">Bu hafta oxirida buvimlarnikiga bormoqchimiz. Chiptalarni oʻtgan hafta
     olganmiz.</p>
  <p class="pe-ex__why">The tickets prove the plan already existed — so <em>going to</em>,
     not <em>will</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu tuzilma oʻzbekchadagi <b>-moqchiman</b> shakliga juda aniq mos keladi:
  <em>bor<b>moqchiman</b></em> = <em>I <b>am going to</b> go</em>,
  <em>oʻqi<b>moqchiman</b></em> = <em>I <b>am going to</b> study</em>. Ikkalasida ham maʼno
  bir xil: <b>niyat allaqachon bor</b>. "Boraman" (<em>will</em>) esa shu zahoti aytilgan
  qaror.
</div>

<h3>2. Job one: plans and intentions</h3>

<p>Any decision you took <b>before</b> this conversation belongs here — from tonight's dinner
to your whole career.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek <b>is going to</b> buy a new bike. He <b>isn't going to</b>
     spend all his money, though.</p>
  <p class="pe-ex__uz">Sherbek yangi velosiped sotib olmoqchi. Lekin u butun pulini
     sarflamoqchi emas.</p>
</div>

<p>Negatives and questions follow <em>to be</em>, exactly as in PE-6 — there is no
<em>do/does</em> anywhere:</p>

<ol class="pe-steps">
  <li><b>Negative:</b> <em>I'<b>m not going to</b> argue. She <b>isn't going to</b> come.</em></li>
  <li><b>Question:</b> <em><b>Are</b> you <b>going to</b> tell him?</em></li>
  <li><b>Short answers:</b> <em>Yes, I am. / No, I'm not.</em></li>
  <li><b>Wh-:</b> <em><b>What are</b> you <b>going to</b> do after school?</em></li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Soʻroq va inkorda <b>do/does</b> ham, <b>will</b> ham ishlatilmaydi — bu tuzilma
  <b>to be</b> feʼliga tayanadi: <em><b>Are</b> you going to come?</em>,
  <em>I<b>'m not</b> going to come.</em> <s>Do you going to…</s> va
  <s>Will you going to…</s> — ikkalasi ham notoʻgʻri.
</div>

<h3>3. Job two: I can see it coming</h3>

<p>The second job is a prediction — but not an opinion like <em>will</em>. This one is based
on <b>evidence you can see right now</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Look at those black clouds! It <b>'s going to</b> rain.</p>
  <p class="pe-ex__uz">Anavi qora bulutlarga qara! Yomgʻir yogʻadi.</p>
  <p class="pe-ex__why">The clouds are the evidence. With <em>I think it will rain</em> you
     are only guessing.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">going to — evidence in front of you</p>
    <ul>
      <li>He's driving too fast — he <b>'s going to</b> crash!</li>
      <li>She <b>'s going to</b> have a baby. <em>(you can see)</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">will — opinion in your head</p>
    <ul>
      <li>I think he <b>'ll</b> drive more carefully next time.</li>
      <li>I'm sure they <b>'ll</b> be happy.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni shunday eslang: <b>going to</b> — "koʻrinib turibdi" (dalil bor, koʻzingiz bilan
  koʻryapsiz). <b>will</b> — "menimcha shunday boʻladi" (faqat fikr). Shuning uchun
  <em>Look!</em> yoki <em>Be careful!</em> soʻzlaridan keyin deyarli doim <b>going to</b>
  keladi.
</div>

<h3>4. going to go</h3>

<p>Grammatically <em>I am going to go to the cinema</em> is perfectly correct. But two "go"s in
a row sound heavy, so English usually drops the second one when a place is mentioned:</p>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'m going to</b> the cinema tonight. <em>(= I'm going to go
     there)</em></p>
  <p class="pe-ex__uz">Bugun kechqurun kinoga boraman.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In fast speech <em>going to</em> becomes <b>gonna</b>: <em>"I'm gonna call her."</em>
  Recognise it when you hear it in films and songs — but never write it in an exam, a letter
  or an essay.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>He going to buy a car.</s></p>
  <p class="pe-good">He <b>is going to</b> buy a car. <em>(the "be" is not optional)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I am going to studying medicine.</s></p>
  <p class="pe-good">I am going to <b>study</b> medicine. <em>(base verb after "to")</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you going to come with us?</s></p>
  <p class="pe-good"><b>Are you going to</b> come with us?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Look at the sky — I think it will rain in a minute.</s></p>
  <p class="pe-good">Look at the sky — it<b>'s going to</b> rain.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will visit my aunt tomorrow. I bought a present yesterday.</s></p>
  <p class="pe-good">I<b>'m going to</b> visit my aunt tomorrow. <em>(the present proves it was planned)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>Afsona <span class="pe-blank">?</span> (study) at the medical institute.
     She has already sent her documents.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is going to study</strong> — the documents show the decision was made
         earlier.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Which is better, and why? <em>Careful! You (a) will drop (b) are going to drop those
     plates.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) are going to drop.</strong> You can see it happening — the plates are
         already sliding. That is evidence, not opinion.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make it a question and a negative: <em>They are going to move to Tashkent.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Are they going to move to Tashkent? / They aren't going to move to
         Tashkent.</strong></p>
      <p>It behaves exactly like <em>to be</em> — no <em>do</em>, no <em>will</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Translate: <em>Men ertaga shifokorga bormoqchiman.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'm going to see the doctor tomorrow.</strong></p>
      <p><em>-moqchiman</em> = an intention that already exists → <b>going to</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write two sentences about your plans for next summer.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Next summer I<b>'m going to</b> take an English course,
         and my family <b>is going to</b> travel to Bukhara.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Be going to</b><span>...moqchi boʻlmoq</span></li>
  <li><b>Intention</b><span>niyat</span></li>
  <li><b>Plan</b><span>reja</span></li>
  <li><b>Evidence</b><span>dalil, koʻrinib turgan belgi</span></li>
  <li><b>Prediction</b><span>bashorat</span></li>
  <li><b>To decide</b><span>qaror qilmoq</span></li>
  <li><b>To argue</b><span>bahslashmoq</span></li>
  <li><b>To crash</b><span>toʻqnashmoq</span></li>
  <li><b>Careful!</b><span>Ehtiyot boʻling!</span></li>
  <li><b>Gonna (informal)</b><span>going to ning ogʻzaki shakli</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>am/is/are + going to + base verb</b> — the "be" part is never optional.</li>
    <li>Job 1: a plan you <b>already made</b> (= Uzbek <b>-moqchiman</b>).</li>
    <li>Job 2: a prediction from <b>evidence you can see</b> right now.</li>
    <li>Questions and negatives follow <b>to be</b>, never <em>do</em> or <em>will</em>.</li>
    <li><b>gonna</b> is speech only — never write it.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-28: Present Continuous for Future Arrangements",
        "category": "english",
        "order": 28,
        "summary": (
            "The tense you thought meant 'now' also talks about tomorrow — when the time and "
            "place are fixed and somebody else is expecting you."
        ),
        "content": """
<h2>PE-28: Present Continuous for Future Arrangements</h2>

<p>Open your diary. <em>"I<b>'m meeting</b> Afsona at four."</em> That sentence uses the
Present Continuous — the tense you learned in PE-12 for things happening <b>right now</b> —
and yet it clearly means tomorrow. English does this whenever an arrangement is
<mark>fixed with another person</mark>: the time is agreed, the place is agreed, somebody is
waiting for you.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>What an <b>arrangement</b> is, and why it needs this tense</li>
    <li>How to tell the "now" meaning from the "future" meaning</li>
    <li>Which verbs appear in this structure most often</li>
    <li>How it differs from the timetable future of PE-9</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">A fixed arrangement</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">am / is / are</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--adv">future time</span>
</div>

LEGEND_HERE

<h3>1. What makes it an "arrangement"</h3>

<p>An arrangement is more than a wish and more than a plan in your head. Three things are
already settled: <b>when</b>, <b>where</b>, and usually <b>with whom</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">'m meeting</span> the dentist
     <span class="pe-hl pe-hl--adv">at 3 o'clock tomorrow</span>.</p>
  <p class="pe-ex__uz">Ertaga soat uchda tish shifokoriga boraman.</p>
  <p class="pe-ex__why">The appointment is written in a book. Somebody expects you.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">We<b>'re having</b> a party on Saturday. Sherbek <b>is coming</b> too.</p>
  <p class="pe-ex__uz">Shanba kuni bazm qilamiz. Sherbek ham keladi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxshi xabar: oʻzbek tilida ham xuddi shunday qilinadi! "Ertaga Afsona bilan
  uchrash<b>yapman</b>" — hozirgi zamon shakli, lekin maʼnosi kelasi zamon. Ingliz tilida ham
  aynan shu mantiq ishlaydi: <em>I<b>'m meeting</b> Afsona tomorrow</em>. Demak bu tuzilma
  siz uchun tabiiy — faqat unga ishonish kerak.
</div>

<h3>2. How do I know it is the future?</h3>

<p>The form is identical to the "happening now" meaning. The <b>time expression</b> is what
tells your listener which one you mean — and if there is no time expression, they assume
"now".</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Now</p>
    <ul>
      <li>Be quiet — I<b>'m working</b>.</li>
      <li>She<b>'s talking</b> to her mother.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Future arrangement</p>
    <ul>
      <li>I<b>'m working</b> <em>on Sunday</em>.</li>
      <li>She<b>'s talking</b> to the director <em>on Monday</em>.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Without a future time word, <em>"I'm going to Samarkand"</em> means you are on the road
  right now. Add the time and it becomes an arrangement: <em>"I'm going to Samarkand
  <b>next week</b>."</em> Never leave the time out.
</div>

<h3>3. The verbs that live here</h3>

<p>Not every verb suits an arrangement — the ones that do are verbs of meeting, moving and
social life.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Meeting people</p>
    <p><em>meet, see, visit</em> — <em>I'm seeing the doctor at five.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Movement</p>
    <p><em>go, come, leave, arrive, fly, travel</em> — <em>We're leaving at dawn.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Events</p>
    <p><em>have (a party), play, start, finish</em> — <em>They're playing on Friday.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Never here</p>
    <p>Stative verbs (<em>know, want, like</em>) and predictions — those take <em>will</em>.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— <b>What are you doing</b> on Friday? — I<b>'m not doing</b>
     anything. Why?</p>
  <p class="pe-ex__uz">— Juma kuni nima qilyapsan? — Hech narsa qilmayapman. Nega?</p>
  <p class="pe-ex__why">This is <em>the</em> standard English way to ask a friend about their
     plans.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Doʻstingizdan reja soʻraganda ingliz tilida deyarli doim shu shakl ishlatiladi:
  <em>What <b>are</b> you <b>doing</b> tonight?</em> Oʻzbekchada ham xuddi shunday aytamiz —
  "Bugun kechqurun nima <b>qilyapsan</b>?" — garchi gap kelajak haqida boʻlsa ham.
  <s>What will you do tonight?</s> soʻrasangiz, bu "nima qilarding?" degandek biroz
  gʻalati eshitiladi.
</div>

<h3>4. Arrangement or timetable?</h3>

<p>Remember from PE-9 that fixed schedules use the <b>Present Simple</b>. The difference is
who decided: a company and its timetable, or you and another person.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Present Simple — a public timetable</p>
    <ul>
      <li>The train <b>leaves</b> at 6:40.</li>
      <li>The film <b>starts</b> at eight.</li>
      <li>Term <b>ends</b> on 25 May.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Present Continuous — your personal diary</p>
    <ul>
      <li>I<b>'m catching</b> the 6:40 train.</li>
      <li>We<b>'re watching</b> that film tonight.</li>
      <li>I<b>'m taking</b> my exam on 25 May.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farq — <b>kim qaror qilgan</b>: agar jadval (poyezd, kino, dars jadvali) qaror qilgan
  boʻlsa — Present Simple. Agar <b>siz</b> boshqa odam bilan kelishib olgan boʻlsangiz —
  Present Continuous. Shuning uchun bitta voqea haqida ikki xil gapirish mumkin: poyezd
  <em>leaves</em>, siz esa uni <em>are catching</em>.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I meet my friend tomorrow evening.</s></p>
  <p class="pe-good">I<b>'m meeting</b> my friend tomorrow evening.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'm going to Khiva. (meaning: next month)</s></p>
  <p class="pe-good">I'm going to Khiva <b>next month</b>. <em>(the time makes it future)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She is knowing the answer tomorrow.</s></p>
  <p class="pe-good">She <b>will know</b> the answer tomorrow. <em>(stative verb)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I'm thinking it's raining tomorrow.</s></p>
  <p class="pe-good">I <b>think</b> it <b>will rain</b> tomorrow. <em>(a prediction, not an arrangement)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The bus is leaving at 7 every morning.</s></p>
  <p class="pe-good">The bus <b>leaves</b> at 7 every morning. <em>(a timetable)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Now or future? <em>(a) Jasur is playing football. (b) Jasur is playing football on
     Sunday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) now · (b) future arrangement.</strong> The only difference is the time
         expression — the verb form is identical.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Correct it: <em>I see the dentist at ten tomorrow.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I'm seeing the dentist at ten tomorrow.</strong></p>
      <p>An appointment is an arrangement with another person → Present Continuous.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which tense? <em>Our English lesson ___ (start) at 8:30 every day.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>starts</strong> — a school timetable decides it, and <em>every day</em>
         makes it a routine. Present Simple.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Answer about yourself: <em>What are you doing this weekend?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I<b>'m visiting</b> my grandparents on Saturday, and on
         Sunday I<b>'m playing</b> football with my friends.</em></p>
      <p>Notice the question itself uses this tense — it is the normal way to ask about
         plans.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Why is one of these strange? <em>(a) I'm having dinner with Afsona tonight.
     (b) I'm wanting a new phone next month.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) is wrong.</strong> <em>Want</em> is stative — it can never take
         <b>-ing</b>. Say: <em>I<b>'m going to</b> buy a new phone next month.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Arrangement</b><span>kelishilgan reja</span></li>
  <li><b>Appointment</b><span>uchrashuv, navbat</span></li>
  <li><b>Diary</b><span>kundalik daftar</span></li>
  <li><b>To arrange</b><span>kelishib olmoq</span></li>
  <li><b>To expect somebody</b><span>kimnidir kutmoq</span></li>
  <li><b>Timetable</b><span>jadval</span></li>
  <li><b>Term</b><span>oʻquv chorak / semestr</span></li>
  <li><b>At dawn</b><span>tong saharda</span></li>
  <li><b>To catch a train</b><span>poyezdga ulgurmoq</span></li>
  <li><b>Personal</b><span>shaxsiy</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>am/is/are + -ing + future time</b> = an arrangement already fixed with somebody.</li>
    <li>The <b>time expression</b> is what turns "now" into "future" — never omit it.</li>
    <li>Verbs of meeting, moving and events; <b>never</b> stative verbs.</li>
    <li>Public timetable → <b>Present Simple</b>; your own diary → <b>Present
        Continuous</b>.</li>
    <li><em>What are you doing tonight?</em> is the normal way to ask about plans.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-29: will vs going to vs Present Continuous",
        "category": "english",
        "order": 29,
        "summary": (
            "Three futures, one decision. A four-question ladder that picks the right one every "
            "time — plus the rule that bans will after when and if."
        ),
        "content": """
<h2>PE-29: will vs going to vs Present Continuous</h2>

<p>You now own three ways to talk about the future, and a natural question follows: which one
do I actually say? The honest answer is that English speakers choose by <b>how fixed the
future is</b> — from "just arranged in my diary" all the way down to "I've only just thought
of it". Here is that scale, and a ladder you can run in your head in one second.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The "how fixed is it?" scale behind all three forms</li>
    <li>A four-question ladder that always gives you an answer</li>
    <li>The restaurant test — the clearest example of <em>will</em> vs <em>going to</em></li>
    <li>The time-clause rule that applies to all three</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">From most fixed to least fixed</span>
  <span class="pe-chip pe-chip--s">I'm meeting him</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">I'm going to meet him</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">I'll meet him</span>
</div>

<h3>1. The scale</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Present Continuous</p>
    <p><em>Arranged with somebody.</em> Time and place already agreed.
       <em>I'm seeing the doctor at five.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>be going to</p>
    <p><em>Decided, but not arranged.</em> Or evidence you can see.
       <em>I'm going to learn Korean.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>will</p>
    <p><em>Nothing decided until now.</em> Opinions, promises, offers, instant decisions.
       <em>I'll help you.</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'m flying</b> to Seoul on Tuesday. I<b>'m going to</b> look for a
     job there. I think I<b>'ll like</b> it.</p>
  <p class="pe-ex__uz">Seshanba kuni Seulga uchaman. U yerda ish qidirmoqchiman. Menimcha,
     menga yoqadi.</p>
  <p class="pe-ex__why">Ticket bought → Continuous. Intention → going to. Opinion → will.
     Three sentences, three futures, all correct.</p>
</div>

<h3>2. The decision ladder</h3>

<ol class="pe-steps">
  <li><b>Is it arranged with another person — time and place fixed?</b> →
      <b>Present Continuous</b>. Stop.</li>
  <li><b>Did I decide before now, or can I see the evidence?</b> → <b>be going to</b>. Stop.</li>
  <li><b>Am I deciding at this second, offering, or promising?</b> → <b>will</b>.</li>
  <li><b>Am I giving an opinion or a prediction from my head?</b> → <b>will</b>
      (with <em>I think, I'm sure, probably</em>).</li>
</ol>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Uchta shakl — uchta oʻzbekcha maʼno: <b>Present Continuous</b> = "ertaga uchrash<b>yapman</b>"
  (kelishilgan), <b>going to</b> = "bor<b>moqchiman</b>" (niyat bor), <b>will</b> =
  "bora<b>man</b>" (hozir qaror qildim yoki shunchaki fikrim). Gapirishdan oldin oʻzingizga
  bitta savol bering: <b>bu ish qanchalik aniq belgilangan?</b>
</div>

<h3>3. The restaurant test</h3>

<p>This tiny scene shows the <em>will</em> / <em>going to</em> difference better than any
rule. Two people sit down with a menu.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Reading the menu now</p>
    <p>— What would you like?<br>
       — Hmm… I<b>'ll have</b> the lagman.</p>
    <p>Decided at this second → <b>will</b>.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Talking on the way there</p>
    <p>— I<b>'m going to have</b> the lagman.</p>
    <p>Decided before arriving → <b>going to</b>.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  In a restaurant, a shop or a ticket office, the polite English is almost always
  <em>"I'll have…"</em> / <em>"I'll take…"</em>. Using <em>going to</em> there sounds as if
  you have been planning your lunch for a week.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Restoran misolini yodda tutsangiz, farqni hech qachon adashtirmaysiz. Menyuni oʻqib
  turib tanlasangiz — <b>will</b> ("Men lagʻmon <b>olaman</b>" — hozir qaror qildim).
  Yoʻlda kelayotib gaplashgan boʻlsangiz — <b>going to</b> ("Lagʻmon
  <b>yemoqchiman</b>" — oldindan hal qilganman).
</div>

<h3>4. Where they overlap — and it doesn't matter</h3>

<p>Sometimes two forms are both fine and the difference is tiny. Do not freeze while speaking.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'m going to</b> visit my aunt on Sunday. = I<b>'m visiting</b> my
     aunt on Sunday.</p>
  <p class="pe-ex__uz">Yakshanba kuni xolamnikiga boraman.</p>
  <p class="pe-ex__why">Both correct. The second just sounds slightly more definite.</p>
</div>

<p>What is <b>not</b> interchangeable: never use the Present Continuous for a prediction
(<s>It's raining tomorrow, I think</s>), and never use <em>will</em> for a plan you have
clearly already made.</p>

<h3>5. The rule that covers all three</h3>

<p>After <b>when, if, as soon as, before, after, until, while</b>, English uses the
<b>Present Simple</b> — no <em>will</em>, no <em>going to</em>. The future lives in the other
half of the sentence.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>When</b> I <b>finish</b> school, I<b>'m going to</b> study
     engineering. <b>If</b> it <b>rains</b>, we<b>'ll stay</b> at home.</p>
  <p class="pe-ex__uz">Maktabni tugatganimdan keyin muhandislikni oʻqimoqchiman. Agar yomgʻir
     yogʻsa, uyda qolamiz.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada ikkala yarmida ham kelasi zamon boʻlishi mumkin: "Maktabni <b>tugatsam</b>,
  institutga <b>kiraman</b>". Ingliz tilida esa <b>when / if</b> dan keyingi qism
  <b>hozirgi zamonda</b> qoladi. Bu — imtihonlarda eng koʻp tekshiriladigan qoidalardan
  biri, shuning uchun uni mashq qilib mustahkamlang.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>— The phone is ringing! — I'm going to answer it.</s></p>
  <p class="pe-good">— <b>I'll answer</b> it. <em>(decided this second)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will meet Sherbek at six — we agreed yesterday.</s></p>
  <p class="pe-good">I<b>'m meeting</b> Sherbek at six.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Look at those clouds — it will rain.</s></p>
  <p class="pe-good">Look at those clouds — it<b>'s going to</b> rain.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I think I'm going to like this book. (just an opinion)</s></p>
  <p class="pe-good">I think I<b>'ll like</b> this book.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>When I will see her, I will tell her.</s></p>
  <p class="pe-good">When I <b>see</b> her, I<b>'ll tell</b> her.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>— Why are you carrying that big bag? — I <span class="pe-blank">?</span>
     (play) tennis with Jasur at four. We arranged it yesterday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>'m playing</strong> — arranged with another person, time fixed → Present
         Continuous.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>— I can't open this jar. — Give it to me, I <span class="pe-blank">?</span>
     (do) it.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>'ll do</strong> — an offer made at this exact moment.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Choose: <em>She has bought paint and brushes. She <span class="pe-blank">?</span>
     (paint) her room.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>is going to paint</strong> — the paint and brushes are the evidence that the
         decision already exists.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Fix it: <em>As soon as I will get my salary, I will buy a laptop.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>As soon as I get my salary, I'll buy a laptop.</strong></p>
      <p>One <em>will</em> only, and never in the <em>as soon as</em> half.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Explain the difference: <em>(a) I'll see the doctor. (b) I'm seeing the doctor.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I have just decided</strong> — perhaps I feel ill right now.
         <strong>(b) I have an appointment</strong> — it is already in the diary.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Arrangement</b><span>kelishilgan reja</span></li>
  <li><b>Intention</b><span>niyat</span></li>
  <li><b>Instant decision</b><span>shu ondagi qaror</span></li>
  <li><b>Evidence</b><span>dalil</span></li>
  <li><b>To agree</b><span>kelishmoq</span></li>
  <li><b>Definite</b><span>aniq, qatʼiy</span></li>
  <li><b>To overlap</b><span>bir-biriga mos kelmoq</span></li>
  <li><b>Salary</b><span>oylik maosh</span></li>
  <li><b>Jar</b><span>banka</span></li>
  <li><b>Time clause</b><span>payt ergash gapi</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Arranged with somebody → <b>Present Continuous</b>.</li>
    <li>Decided earlier, or evidence you can see → <b>be going to</b>.</li>
    <li>Deciding now, offering, promising, predicting → <b>will</b>.</li>
    <li>Restaurant test: <em>"I'll have the lagman"</em> — you decided while reading the
        menu.</li>
    <li>After <b>when, if, as soon as, until</b> → <b>Present Simple</b>, whichever future
        you use.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-30: Future Continuous: What You Will Be Doing",
        "category": "english",
        "order": 30,
        "summary": (
            "This time tomorrow, what will you be doing? The tense for an action in progress at "
            "a future moment — and the politest way to ask about someone's plans."
        ),
        "content": """
<h2>PE-30: Future Continuous: What You Will Be Doing</h2>

<p><em>"This time tomorrow I<b>'ll be flying</b> to Seoul."</em> Not <em>I will fly</em> —
that is just the fact. <b>I'll be flying</b> puts you inside the moment: the plane is in the
air, you are in your seat, the action is in the middle of happening. This is the fourth and
last future you need, and it completes the whole picture.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The form <b>will be + verb-ing</b></li>
    <li>Three jobs: a future moment, an expected event, a polite question</li>
    <li>Why <em>Will you be using the car?</em> is more polite than <em>Will you use it?</em></li>
    <li>Which verbs still refuse the <b>-ing</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Positive sentence</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">will be</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">verb + ing</span>
</div>

LEGEND_HERE

<h3>1. The picture: a band around a future moment</h3>

<div class="pe-timeline">
  <div class="pe-tl-track">
    <span class="pe-tl-now" style="left:24%"></span>
    <span class="pe-tl-band" style="left:52%;width:32%"></span>
    <span class="pe-tl-tag" style="left:68%">8 p.m. — I'll be studying</span>
  </div>
  <div class="pe-tl-foot"><span>Past</span><span>Now</span><span>Future</span></div>
</div>

<p>Same shape as the Past Continuous in PE-23, only moved to the right of NOW. The action
starts before the future moment and is still going afterwards.</p>

<div class="pe-ex">
  <p class="pe-ex__en">At eight o'clock tonight <span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">will be</span>
     <span class="pe-hl pe-hl--v">doing</span> my homework.</p>
  <p class="pe-ex__uz">Bugun kechqurun soat sakkizda men uy vazifamni qilayotgan boʻlaman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Future Continuous oʻzbekchadagi <b>-ayotgan boʻlaman</b> shakliga toʻgʻri keladi:
  <em>oʻqi<b>yotgan boʻlaman</b></em> = <em>I <b>will be studying</b></em>. Eʼtibor bering,
  oʻzbekchada ham uchta boʻlak bor ("oʻqiyotgan" + "boʻl" + "-aman"), ingliz tilida ham
  uchta: <b>will</b> + <b>be</b> + <b>-ing</b>. Hech biri tushib qolmasin.
</div>

<h3>2. Job one: in the middle of a future moment</h3>

<p>This is the job you will use most. It answers the question <em>"What will you be doing
at …?"</em></p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">will + verb — the whole action</p>
    <ul>
      <li>I <b>'ll write</b> the report tomorrow.<br><em>(from start to finish)</em></li>
      <li>She <b>'ll cook</b> dinner.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">will be + -ing — the middle of it</p>
    <ul>
      <li>At ten I <b>'ll be writing</b> the report.<br><em>(already in progress)</em></li>
      <li>When you arrive, she <b>'ll be cooking</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Don't call me at seven — I<b>'ll be having</b> dinner with my family.</p>
  <p class="pe-ex__uz">Soat yettida menga qoʻngʻiroq qilma — oilam bilan ovqatlanayotgan
     boʻlaman.</p>
  <p class="pe-ex__why">Signal words: <em>at 7 o'clock, this time tomorrow, when you
     arrive, all day</em>.</p>
</div>

<h3>3. Job two: things that will happen anyway</h3>

<p>Use it for events that are simply part of the normal course of things — nobody decided them
specially, they are just going to happen.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I<b>'ll be seeing</b> Afsona at school tomorrow, so I can give her
     your book.</p>
  <p class="pe-ex__uz">Ertaga maktabda Afsonani koʻraman, shuning uchun kitobingizni unga
     bera olaman.</p>
  <p class="pe-ex__why">Not a plan or a promise — it is simply going to happen because we
     both go to school.</p>
</div>

<h3>4. Job three: the polite question</h3>

<p>Here is a subtle and very useful piece of English. <em>"Will you use the car tonight?"</em>
sounds like a request or even pressure. <em>"<b>Will you be using</b> the car tonight?"</em>
is neutral — it only asks about the facts, with no hidden request attached.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Sounds like a request</p>
    <ul>
      <li><em>Will you come to the meeting?</em><br>(= please come)</li>
      <li><em>Will you help us?</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Just asking — polite and neutral</p>
    <ul>
      <li><em>Will you be coming to the meeting?</em><br>(= I'm only asking)</li>
      <li><em>Will you be staying long?</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu — ingliz tilining muloyimlik nozikligi. <em>Will you come?</em> — bu deyarli
  "keling, iltimos" degan maʼnoni beradi. <em>Will you <b>be coming</b>?</em> esa faqat
  "kelasizmi, bilib qoʻysam boʻladimi?" degan xolis savol — hech qanday bosim yoʻq.
  Kattalar bilan va rasmiy vaziyatlarda ikkinchisi ancha xushmuomala eshitiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>will</b> va <b>will be + -ing</b> farqini oʻzbekchada aniq koʻrish mumkin:
  <em>Ertaga xat <b>yozaman</b></em> = <em>I <b>will write</b></em> (ishning oʻzi),
  <em>Soat oʻnda xat <b>yozayotgan boʻlaman</b></em> = <em>I <b>will be writing</b></em>
  (oʻsha paytda jarayon davom etadi). Birinchisi — butun ish, ikkinchisi — uning
  oʻrtasi.
</div>

<h3>5. Stative verbs, one more time</h3>

<p>The rule from PE-13 holds in every tense, including this one. Verbs of knowing, wanting and
belonging never take <b>-ing</b>.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>Tomorrow I will be knowing my results.</s></p>
  <p class="pe-good">Tomorrow I <b>will know</b> my results.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Negatives and questions are easy here, because only the first word moves:
  <em>I <b>won't be</b> working</em> · <em><b>Will</b> you <b>be</b> working?</em> The
  <b>be</b> and the <b>-ing</b> never change position.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>At six I will studying.</s></p>
  <p class="pe-good">At six I <b>will be studying</b>. <em>(the "be" is missing)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I will be go to school tomorrow.</s></p>
  <p class="pe-good">I <b>will go</b> to school tomorrow. / I <b>will be going</b> …</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Will you be to come tonight?</s></p>
  <p class="pe-good"><b>Will you be coming</b> tonight?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This time tomorrow I will fly to Seoul.</s></p>
  <p class="pe-good">This time tomorrow I<b>'ll be flying</b> to Seoul.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She will be wanting a new phone.</s></p>
  <p class="pe-good">She <b>will want</b> a new phone. <em>(stative)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>This time next week we <span class="pe-blank">?</span> (sit) on the beach
     in Termez.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>will be sitting</strong> — <em>this time next week</em> names a future
         moment, and we will be in the middle of sitting there.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What is the difference? <em>(a) I'll cook dinner when you arrive. (b) I'll be cooking
     dinner when you arrive.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I will start cooking after you arrive.</strong>
         <strong>(b) I will already be cooking when you walk in.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make it polite and neutral: <em>Will you stay for dinner?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Will you be staying for dinner?</strong></p>
      <p>The Continuous removes the feeling of a request and just asks about the plan.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>Don't phone at nine — I will have a shower.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Don't phone at nine — I'll be having a shower.</strong></p>
      <p>You need the "in the middle of it" meaning; <em>will have</em> only states the
         fact.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one sentence about what you will be doing at 9 p.m. tonight.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>At nine o'clock tonight I<b>'ll be reading</b> in my
         room, because I always read before I sleep.</em></p>
      <p>Check all three parts: <b>will</b> + <b>be</b> + <b>-ing</b>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Future Continuous</b><span>kelasi davomli zamon</span></li>
  <li><b>This time tomorrow</b><span>ertaga shu paytda</span></li>
  <li><b>In progress</b><span>davom etayotgan</span></li>
  <li><b>Neutral</b><span>xolis, betaraf</span></li>
  <li><b>Polite</b><span>xushmuomala</span></li>
  <li><b>Request</b><span>iltimos</span></li>
  <li><b>Anyway</b><span>baribir, har holda</span></li>
  <li><b>Results</b><span>natijalar</span></li>
  <li><b>To stay long</b><span>uzoq qolmoq</span></li>
  <li><b>Beach</b><span>plyaj, qirgʻoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>will be + verb-ing</b> — all three parts, every time.</li>
    <li>It means "in the <b>middle</b> of it" at a future moment, not the whole action.</li>
    <li>Also for things that will happen <b>anyway</b>: <em>I'll be seeing her at school.</em></li>
    <li><b>Will you be …?</b> is the polite, neutral way to ask about someone's plans.</li>
    <li>Stative verbs still refuse <b>-ing</b>: <em>I will know</em>, not <s>will be
        knowing</s>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
