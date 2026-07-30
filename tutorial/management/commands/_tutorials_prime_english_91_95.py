# -*- coding: utf-8 -*-
"""Prime English — end of Block G (91–92) and start of Block H, grammar at work (93–95).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_91_95.py --author=prime
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
        "title": "PE-91: Formal vs Informal English",
        "category": "english",
        "order": 91,
        "summary": (
            "The same message in two registers — how to sound right in an exam essay and right "
            "in a message to a friend."
        ),
        "content": """
<h2>PE-91: Formal vs Informal English</h2>

<p>Two sentences, one meaning:</p>

<p><em>"I'm really sorry, but I can't make it."</em> — perfect for a friend.<br>
<em>"I regret that I shall be unable to attend."</em> — perfect for an official letter.</p>

<p>Use the first in a formal letter and you sound careless; use the second with a friend and you
sound strange. Choosing the right <mark>register</mark> is a skill, and it costs marks in every
writing exam.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The four features that make English formal or informal</li>
    <li>Formal alternatives for everyday verbs</li>
    <li>What to avoid completely in formal writing</li>
    <li>How to judge which register a task needs</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Four dials</span>
  <span class="pe-chip pe-chip--s">contractions</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">phrasal verbs</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--o">passive</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--aux">vocabulary</span>
</div>

LEGEND_HERE

<h3>1. The four dials</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Feature</th><th>Informal</th><th>Formal</th></tr>
  <tr><td>contractions</td><td>I'm, don't, can't</td><td>I am, do not, cannot</td></tr>
  <tr><td>verbs</td><td>find out, put off, get</td><td>discover, postpone, receive</td></tr>
  <tr><td>voice</td><td>They cancelled the match.</td><td>The match <b>was cancelled</b>.</td></tr>
  <tr><td>words</td><td>kids, a lot of, stuff</td><td>children, a great deal of, items</td></tr>
  <tr><td>openers</td><td>Hi Jasur,</td><td>Dear Mr Karimov,</td></tr>
  <tr><td>closings</td><td>See you! Bye!</td><td>Yours sincerely,</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Informal: <em>Sorry, I can't come — I've got loads of homework.</em><br>
     Formal: <em>I am afraid I will be unable to attend, as I have a great deal of work to
     complete.</em></p>
  <p class="pe-ex__uz">Kechirasiz, kelolmayman — uy vazifam koʻp. — Afsuski, qatnasha
     olmayman, chunki bajarishim kerak boʻlgan ish juda koʻp.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbek tilida ham xuddi shunday farq bor: doʻstingizga "kelolmayman" deysiz, rasmiy
  xatda esa "qatnashish imkoniyatim yoʻqligini maʼlum qilaman" deb yozasiz. Yaʼni
  tushuncha tanish — faqat ingliz tilida bu farq <b>qisqartmalar</b> va <b>frazali
  feʼllar</b> orqali eng koʻp seziladi.
</div>

<h3>2. Formal alternatives worth knowing</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Informal</th><th>Formal</th><th>Informal</th><th>Formal</th></tr>
  <tr><td>get</td><td>receive / obtain</td><td>find out</td><td>discover</td></tr>
  <tr><td>put off</td><td>postpone</td><td>go up</td><td>increase</td></tr>
  <tr><td>go down</td><td>decrease</td><td>ask for</td><td>request</td></tr>
  <tr><td>help</td><td>assist</td><td>need</td><td>require</td></tr>
  <tr><td>show</td><td>demonstrate</td><td>tell</td><td>inform</td></tr>
  <tr><td>think about</td><td>consider</td><td>get better</td><td>improve</td></tr>
  <tr><td>a lot of</td><td>a great deal of / numerous</td><td>but</td><td>however</td></tr>
  <tr><td>so</td><td>therefore</td><td>also</td><td>in addition</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Informal: <em>We found out that prices went up a lot.</em><br>
     Formal: <em>We <b>discovered</b> that prices had <b>increased</b> <b>significantly</b>.</em></p>
  <p class="pe-ex__uz">Narxlar ancha oshganini bilib oldik. — Narxlar sezilarli darajada
     oshganini aniqladik.</p>
</div>

<h3>3. Avoid these in formal writing</h3>

<ol class="pe-steps">
  <li><b>Contractions:</b> write <em>do not</em>, <em>cannot</em>, <em>it is</em>.</li>
  <li><b>Slang and very casual words:</b> <em>kids, guys, stuff, cool, awesome</em>.</li>
  <li><b>Most phrasal verbs:</b> prefer the single-word alternative (PE-78).</li>
  <li><b>Exclamation marks</b> and emoji — never in an essay or official letter.</li>
  <li><b>Starting with And or But:</b> use <em>In addition</em> or <em>However</em>.</li>
</ol>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Formal does <b>not</b> mean complicated. A clear short sentence is always better than a long
  confusing one. The goal is <em>appropriate</em>, not <em>impressive</em> — examiners can tell
  the difference.
</div>

<h3>4. Which register does the task need?</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Formal</p>
    <ul>
      <li>essays and exam writing</li>
      <li>letters to a school, company or official</li>
      <li>reports and applications</li>
      <li>people you don't know</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Informal</p>
    <ul>
      <li>messages to friends and family</li>
      <li>personal emails</li>
      <li>social media</li>
      <li>speaking with people your own age</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">To a friend: <em>Hi Afsona! Fancy coming to the cinema on Friday?</em><br>
     To a teacher: <em>Dear Ms Ahmedova, I would like to ask whether the deadline could be
     extended.</em></p>
  <p class="pe-ex__uz">Salom Afsona! Juma kuni kinoga borasanmi? — Hurmatli Ahmedova opa,
     muddatni uzaytirish imkoni bormi, deb soʻramoqchi edim.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Muhim maslahat: <b>bir matn ichida ikkalasini aralashtirmang</b>. Rasmiy xatni
  "Dear Mr Karimov" bilan boshlab, keyin "I can't wait!" deb davom ettirsangiz, gʻalati
  chiqadi. Boshida qaysi uslub kerakligini hal qiling va <b>oxirigacha</b> shu uslubda
  yozing — bu imtihonda alohida baholanadi.
</div>

<h3>5. The middle register</h3>

<p>Most real English sits between the two extremes — polite but not stiff. This is the safest
style for an email to a teacher, a colleague or a shop.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><em>Dear Mr Karimov, I am writing to ask about the course. Could you tell
     me when it starts? Thank you for your help. Best regards, Sherbek.</em></p>
  <p class="pe-ex__uz">Hurmatli Karimov aka, kurs haqida soʻramoqchi edim. Qachon boshlanishini
     ayta olasizmi? Yordamingiz uchun rahmat. Hurmat bilan, Sherbek.</p>
  <p class="pe-ex__why">No contractions, no slang, but not heavy either. This is the register you
     will use most in real life.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Amalda eng koʻp kerak boʻladigan uslub — <b>oʻrta daraja</b>: qisqartma va jargon yoʻq,
  lekin ogʻir soʻzlar ham yoʻq. Oʻqituvchiga, ish beruvchiga yoki doʻkonga yozgan
  xatingiz shu darajada boʻlishi kerak. Qoida: <em>Dear…</em> bilan boshlang,
  <em>Could you…</em> bilan soʻrang, <em>Best regards</em> bilan tugating.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Dear Sir, I wanna ask about the job.</s></p>
  <p class="pe-good">Dear Sir, I <b>would like to</b> ask about the position.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>In conclusion, the film was awesome!</s></p>
  <p class="pe-good">In conclusion, the film was <b>excellent</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Hi Mr Karimov, Yours sincerely, Jasur</s></p>
  <p class="pe-good"><b>Dear</b> Mr Karimov, … <b>Yours sincerely</b>, Jasur</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The government didn't do nothing about it.</s></p>
  <p class="pe-good">The government <b>did not take any action</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>But there are also many good things.</s> <em>(essay)</em></p>
  <p class="pe-good"><b>However,</b> there are also many advantages.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make it formal: <em>We found out that a lot of students didn't come.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>We discovered that numerous students did not attend.</strong></p>
      <p>Three changes: phrasal verb → single verb, <em>a lot of</em> → <em>numerous</em>, and
         no contraction.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it informal: <em>I regret that I am unable to assist you.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Sorry, I can't help you.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which is wrong for an essay? <em>(a) However, (b) But, (c) In addition,</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b) But</strong> at the start of a sentence is too informal for an essay —
         use <em>However,</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Formal alternatives for: <em>put off · ask for · get better</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>postpone · request · improve.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which register for a message to your classmate about homework?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Informal.</strong> <em>Hi! What's the maths homework for tomorrow?</em>
         Writing <em>Dear Sir/Madam</em> to a classmate would be strange.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Register</b><span>uslub, nutq darajasi</span></li>
  <li><b>Formal</b><span>rasmiy</span></li>
  <li><b>Informal</b><span>norasmiy</span></li>
  <li><b>Contraction</b><span>qisqartma</span></li>
  <li><b>Slang</b><span>jargon</span></li>
  <li><b>To postpone</b><span>keyinga qoldirmoq</span></li>
  <li><b>To request</b><span>soʻramoq</span></li>
  <li><b>To attend</b><span>qatnashmoq</span></li>
  <li><b>Appropriate</b><span>mos, oʻrinli</span></li>
  <li><b>Deadline</b><span>oxirgi muddat</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Four dials: <b>contractions, phrasal verbs, passive voice, vocabulary</b>.</li>
    <li>Formal: <b>discover, postpone, request, however, therefore</b>.</li>
    <li>Avoid in formal writing: contractions, slang, exclamation marks, opening
        <em>But</em>.</li>
    <li>Formal ≠ complicated. Clear and appropriate beats impressive.</li>
    <li><b>Never mix registers</b> inside one text.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-92: The 20 Mistakes Uzbek Speakers Make Most",
        "category": "english",
        "order": 92,
        "summary": (
            "The complete checklist — every error that comes from Uzbek, gathered in one place "
            "with the reason behind it and the fix."
        ),
        "content": """
<h2>PE-92: The 20 Mistakes Uzbek Speakers Make Most</h2>

<p>Throughout this course, one idea has come back again and again: most mistakes are not random.
They are <mark>your first language quietly translating itself</mark>. Uzbek puts the verb last,
marks case on the noun, has no articles and no Present Perfect. Every one of those facts produces
a predictable English error — which means every one of them can be fixed on purpose. Here is the
complete list.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The 20 most frequent Uzbek-speaker errors, with the reason for each</li>
    <li>A quick self-check you can run over any piece of writing</li>
    <li>Which five to fix first for the biggest improvement</li>
    <li>Where in this course each one is explained in full</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Why mistakes happen</span>
  <span class="pe-chip pe-chip--s">Uzbek structure</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--neg">word-for-word</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">predictable error</span>
</div>

LEGEND_HERE

<h3>1. Word order and sentence building</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>✗ Mistake</th><th>✓ Correct</th><th>Why · Lesson</th></tr>
  <tr><td>I English study.</td><td>I <b>study English</b>.</td><td>Uzbek is SOV · PE-1, PE-72</td></tr>
  <tr><td>I like very much tea.</td><td>I like <b>tea very much</b>.</td><td>nothing between verb and object · PE-72</td></tr>
  <tr><td>Is raining today.</td><td><b>It</b> is raining today.</td><td>Uzbek drops the subject · PE-1</td></tr>
  <tr><td>My brother very clever.</td><td>My brother <b>is</b> very clever.</td><td>Uzbek needs no "to be" · PE-6</td></tr>
  <tr><td>Where you live?</td><td>Where <b>do you live</b>?</td><td>no helper verb in Uzbek · PE-18</td></tr>
</table>
</div>

<h3>2. Articles and nouns</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>✗ Mistake</th><th>✓ Correct</th><th>Why · Lesson</th></tr>
  <tr><td>I am student.</td><td>I am <b>a</b> student.</td><td>no articles in Uzbek · PE-4</td></tr>
  <tr><td>The life is hard.</td><td><b>Life</b> is hard.</td><td>general → no article · PE-4</td></tr>
  <tr><td>five book</td><td>five <b>books</b></td><td>Uzbek keeps singular after numbers · PE-3</td></tr>
  <tr><td>many informations</td><td>much <b>information</b></td><td>uncountable in English · PE-2</td></tr>
  <tr><td>ingliz tili → english</td><td><b>E</b>nglish</td><td>languages take capitals · PE-82</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Artikllar — roʻyxatdagi eng koʻp uchraydigan xato, chunki oʻzbek tilida ular
  <b>umuman yoʻq</b>. Shuning uchun yozganingizdan keyin <b>maxsus bitta oʻqish</b>
  qiling: har bir birlik sanaladigan otga qarab, oldida <em>a</em>, <em>the</em> yoki
  <em>my</em> bormi, deb tekshiring. Faqat shu bitta tekshiruv koʻp xatoni yoʻqotadi.
</div>

<h3>3. Verbs and tenses</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>✗ Mistake</th><th>✓ Correct</th><th>Why · Lesson</th></tr>
  <tr><td>She go to school.</td><td>She <b>goes</b> to school.</td><td>no 3rd-person ending in Uzbek · PE-9</td></tr>
  <tr><td>I live here for ten years.</td><td>I <b>have lived</b> here for ten years.</td><td>Uzbek uses the present · PE-33</td></tr>
  <tr><td>Did you went?</td><td>Did you <b>go</b>?</td><td>one past marker only · PE-22</td></tr>
  <tr><td>I am knowing the answer.</td><td>I <b>know</b> the answer.</td><td>stative verbs · PE-13</td></tr>
  <tr><td>When I will arrive, I will call.</td><td>When I <b>arrive</b>, I will call.</td><td>no <em>will</em> after <em>when</em> · PE-26</td></tr>
</table>
</div>

<h3>4. Prepositions and negatives</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>✗ Mistake</th><th>✓ Correct</th><th>Why · Lesson</th></tr>
  <tr><td>We discussed about it.</td><td>We <b>discussed it</b>.</td><td>Uzbek case ending · PE-76</td></tr>
  <tr><td>I'm listening music.</td><td>I'm <b>listening to</b> music.</td><td>fixed partner · PE-76</td></tr>
  <tr><td>I never don't smoke.</td><td>I <b>never smoke</b>.</td><td>Uzbek needs two negatives · PE-11</td></tr>
  <tr><td>Although…, but…</td><td><b>Although</b> …, …</td><td>Uzbek "garchi…lekin" · PE-52</td></tr>
  <tr><td>I did a mistake.</td><td>I <b>made</b> a mistake.</td><td>"qilmoq" covers both · PE-90</td></tr>
</table>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eʼtibor bering: bu 20 xatoning <b>hech biri</b> "eʼtiborsizlik" emas. Har birining
  aniq sababi bor — oʻzbek tilining tuzilishi. Sababni bilsangiz, xato <b>tasodifiy</b>
  boʻlmay qoladi: uni oldindan kutib, ataylab tekshirish mumkin. Aynan shu — tez
  oʻsishning kaliti.
</div>

<h3>5. Three sentences, rebuilt</h3>

<p>Here is what the checklist looks like in action. Each of these has three or four errors, all
from the list above.</p>

<div class="pe-ex">
  <p class="pe-ex__en">✗ <s>My father work in hospital and he very busy.</s><br>
     ✓ My father <b>works</b> in <b>a</b> hospital and he <b>is</b> very busy.</p>
  <p class="pe-ex__uz">Otam kasalxonada ishlaydi va u juda band.</p>
  <p class="pe-ex__why">Missing <b>-s</b> · missing article · missing <em>is</em> — the three
     commonest of all.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">✗ <s>I study English since five years and I like very much it.</s><br>
     ✓ I <b>have studied</b> English <b>for</b> five years and I like <b>it very much</b>.</p>
  <p class="pe-ex__uz">Besh yildan beri ingliz tilini oʻrganaman va u menga juda yoqadi.</p>
  <p class="pe-ex__why">Present Perfect · <em>for</em> not <em>since</em> · word order.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">✗ <s>Although I was tired, but I didn't never stop.</s><br>
     ✓ <b>Although</b> I was tired, I <b>never stopped</b>.</p>
  <p class="pe-ex__uz">Charchagan boʻlsam ham, hech qachon toʻxtamadim.</p>
  <p class="pe-ex__why">One contrast word · one negative.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Xatolarni <b>uyat</b> deb bilmang — ular oʻrganish jarayonining tabiiy qismi. Muhimi:
  <b>bir xil xatoni takrorlamaslik</b>. Shuning uchun oʻzingizning eng koʻp uchraydigan
  <b>uchta</b> xatosini daftaringizning birinchi sahifasiga yozib qoʻying va har safar
  yozganingizdan keyin faqat shu uchtasini tekshiring.
</div>

<h3>6. The five to fix first</h3>

<p>If you only work on five, choose these — they appear most often and are noticed most
quickly:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Articles</p>
    <p><em>a / the / nothing</em> — check every singular noun. (PE-4)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Third-person -s</p>
    <p><em>she go<b>es</b></em> — one pass through he/she/it. (PE-9)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Word order</p>
    <p>Verb second, nothing between verb and object. (PE-72)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>for / since + Perfect</p>
    <p><em>I <b>have lived</b> here for…</em> (PE-33)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>One negative only</p>
    <p><em>I <b>never</b> smoke</em> · <em>Although…</em> (PE-11, PE-52)</p>
  </div>
</div>

<h3>7. Your self-check routine</h3>

<ol class="pe-steps">
  <li><b>Read for articles only.</b> Every singular countable noun — does it have
      <em>a</em>, <em>the</em>, or a word like <em>my</em>?</li>
  <li><b>Read for he/she/it only.</b> Present tense? Then the verb needs <b>-s</b>.</li>
  <li><b>Read for word order.</b> Is anything sitting between a verb and its object?</li>
  <li><b>Read for double negatives</b> and <em>although…but</em>.</li>
  <li><b>Read it aloud.</b> Your ear catches what your eye misses — especially missing
      <em>is</em> and <em>are</em>.</li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Do <b>one pass per problem</b>, not one pass for everything. Looking for a single type of
  error at a time finds far more than a general re-read, and it takes less than a minute per
  pass.
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Find three mistakes: <em>My sister is student and she go to university since two
     years.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My sister is a student and she has gone / has been going to university for two
         years.</strong></p>
      <p>Missing article · missing <b>-s</b> (fixed by the Perfect) · <em>since</em> →
         <em>for</em>, and the tense must be Present Perfect.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Fix it: <em>Although he was tired, but he didn't never complain.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Although he was tired, he never complained.</strong></p>
      <p>Two Uzbek habits at once: <em>garchi…lekin</em> and the double negative.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Fix it: <em>Yesterday we discussed about the plan and I like very much it.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Yesterday we discussed the plan and I liked it very much.</strong></p>
      <p>No preposition after <em>discuss</em>; nothing between verb and object; and the tense
         should match <em>yesterday</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Fix it: <em>When I will finish school, I want study medicine.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>When I finish school, I want to study medicine.</strong></p>
      <p>No <em>will</em> after <em>when</em>; <em>want</em> takes <b>to + verb</b>
         (PE-64).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Which two of your own mistakes will you check first from now on?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>There is no single right answer</strong> — but write them down. Two errors you
         actively watch for will disappear within a month; twenty you only read about will
         not.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Mistake / error</b><span>xato</span></li>
  <li><b>Interference</b><span>ona tili taʼsiri</span></li>
  <li><b>Word-for-word</b><span>soʻzma-soʻz</span></li>
  <li><b>Predictable</b><span>oldindan aytish mumkin</span></li>
  <li><b>Self-check</b><span>oʻz-oʻzini tekshirish</span></li>
  <li><b>Routine</b><span>tartib, odat</span></li>
  <li><b>To proofread</b><span>qayta oʻqib tekshirmoq</span></li>
  <li><b>Case ending</b><span>kelishik qoʻshimchasi</span></li>
  <li><b>Double negative</b><span>qoʻsh inkor</span></li>
  <li><b>Improvement</b><span>yaxshilanish</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Almost every mistake has a <b>reason</b> in Uzbek — so it can be predicted and
        checked.</li>
    <li>The big five: <b>articles · third-person -s · word order · for/since + Perfect · one
        negative</b>.</li>
    <li>Check with <b>one pass per problem</b>, not one general re-read.</li>
    <li>Read your work <b>aloud</b> — the ear catches missing <em>is</em> and <em>are</em>.</li>
    <li>Two errors you actively watch for beat twenty you only read about.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-93: Writing an Email: Grammar That Sounds Polite",
        "category": "english",
        "order": 93,
        "summary": (
            "The email that gets a helpful reply — openings, closings, and the grammar of "
            "polite requests, all in one template you can reuse."
        ),
        "content": """
<h2>PE-93: Writing an Email: Grammar That Sounds Polite</h2>

<p>Welcome to the last block of Prime English: <b>grammar at work</b>. From here on, every lesson
takes what you have learned and puts it into a real task. And the most useful task of all is the
one you will do hundreds of times in your life — <mark>writing an email that gets a helpful
reply</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The five parts of every email</li>
    <li>Which opening and closing go together</li>
    <li>The grammar of a polite request — modals doing real work</li>
    <li>A complete template you can reuse</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The five parts</span>
  <span class="pe-chip pe-chip--s">greeting</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">reason</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--o">details</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--adv">request</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">closing</span>
</div>

LEGEND_HERE

<h3>1. Greeting and closing must match</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Situation</th><th>Opening</th><th>Closing</th></tr>
  <tr><td>You know the name</td><td>Dear Mr Karimov,</td><td>Yours sincerely,</td></tr>
  <tr><td>You don't know the name</td><td>Dear Sir or Madam,</td><td>Yours faithfully,</td></tr>
  <tr><td>Teacher, colleague</td><td>Dear Ms Ahmedova,</td><td>Best regards, / Kind regards,</td></tr>
  <tr><td>Friend</td><td>Hi Afsona, / Hello!</td><td>See you soon! / Best wishes,</td></tr>
</table>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  Never mix them (PE-91). <s>Hi Mr Karimov, … Yours faithfully</s> ✗. And note the comma after
  the greeting, with the message starting on a new line.
</div>

<h3>2. Say why you are writing — in the first line</h3>

<p>English emails get to the point quickly. One sentence, using a fixed phrase:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>I am writing to</b> ask about the summer course. — <b>I am writing to
     apply for</b> the position. — <b>I am writing regarding</b> my exam results.</p>
  <p class="pe-ex__uz">Yozgi kurs haqida soʻramoqchi edim. — Ish oʻrniga daʼvogarlik qilmoqchi
     edim. — Imtihon natijalarim haqida yozyapman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Muhim madaniy farq: oʻzbekcha xatlarda odatda uzun salomlashish va hol-ahvol soʻrash
  boʻladi. Ingliz tilidagi <b>rasmiy</b> xatda esa <b>birinchi jumlada maqsadni</b>
  aytish kutiladi — <em>I am writing to…</em>. Bu qoʻpollik emas, balki hurmat belgisi:
  oʻqiyotgan odamning vaqtini tejaydi.
</div>

<h3>3. The grammar of a polite request</h3>

<p>This is where PE-49 earns its keep. The longer the structure, the more polite it sounds.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Too direct in writing</p>
    <ul>
      <li><s>Send me the form.</s></li>
      <li><s>I want more information.</s></li>
      <li><s>Tell me when it starts.</s></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Polite and normal</p>
    <ul>
      <li><b>Could you</b> send me the form?</li>
      <li><b>I would like to</b> request more information.</li>
      <li><b>I would be grateful if you could</b> tell me when it starts.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>I would be grateful if you could</b> confirm the date. —
     <b>I would appreciate it if you could</b> reply by Friday.</p>
  <p class="pe-ex__uz">Sanani tasdiqlab bersangiz, minnatdor boʻlardim. — Juma kunigacha javob
     bersangiz, juda yaxshi boʻlardi.</p>
  <p class="pe-ex__why">Notice the second conditional (PE-54) doing the politeness work:
     <em>would … if you could</em>.</p>
</div>

<h3>4. The whole template</h3>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Dear Ms Ahmedova,</b><br><br>
     <b>I am writing to</b> ask about the English summer course.<br><br>
     I am a Year 10 student at School 25, and I <b>have been studying</b> English for six years.
     I <b>am particularly interested in</b> improving my speaking.<br><br>
     <b>Could you</b> tell me when the course starts and how much it costs? <b>I would also be
     grateful if you could</b> send me the application form.<br><br>
     <b>Thank you for your help.</b> <b>I look forward to hearing from you.</b><br><br>
     <b>Best regards,</b><br>Sherbek Tursunov</p>
  <p class="pe-ex__uz">Hurmatli Ahmedova opa, yozgi ingliz tili kursi haqida soʻramoqchi edim…
     Yordamingiz uchun rahmat. Javobingizni kutaman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu shablonni <b>yod olib qoʻying</b> — u umr boʻyi kerak boʻladi. Ichidagi grammatika
  butun kursdan yigʻilgan: <em>have been studying</em> (PE-36), <em>interested in
  improving</em> (PE-76 + PE-64), <em>Could you…</em> (PE-49), <em>I would be grateful if
  you could…</em> (PE-54). Yaʼni bu — grammatikaning <b>ish paytidagi</b> koʻrinishi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Xat yozishda vaqt tejash uchun <b>tayyor iboralarni</b> yod oling — ularni har safar
  oʻylab topish shart emas: <em>I am writing to…</em> (maqsad), <em>Could you…?</em>
  (iltimos), <em>Thank you for your help</em> (minnatdorchilik), <em>I look forward to
  hearing from you</em> (yakun). Toʻrtta ibora — butun xat tayyor.
</div>

<h3>5. Two phrases that always help</h3>

<ul>
  <li><b>I look forward to hearing from you.</b> — note the <b>-ing</b> after <em>to</em>
      (PE-64): <s>look forward to hear</s> ✗</li>
  <li><b>Please do not hesitate to contact me</b> if you need more information. — a standard,
      very useful closing line.</li>
  <li><b>Thank you in advance for your help.</b> — polite and short.</li>
  <li><b>I apologise for the late reply.</b> — better than <em>Sorry for late</em>.</li>
</ul>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Dear teacher, how are you? How is your family? I want ask something.</s></p>
  <p class="pe-good">Dear Ms Ahmedova, <b>I am writing to ask</b> about…</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I look forward to hear from you.</s></p>
  <p class="pe-good">I look forward <b>to hearing</b> from you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Please send me the form immediately.</s></p>
  <p class="pe-good"><b>Could you</b> send me the form, please?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Dear Sir, … Best wishes, Jasur</s></p>
  <p class="pe-good">Dear Sir or Madam, … <b>Yours faithfully</b>, Jasur Karimov</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I wanna know about the course.</s></p>
  <p class="pe-good">I <b>would like to</b> know about the course.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Which closing goes with <em>Dear Sir or Madam</em>?</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Yours faithfully.</strong> Use <em>Yours sincerely</em> only when you know the
         person's name.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it polite: <em>Send me the timetable.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Could you send me the timetable, please?</strong> or
         <strong>I would be grateful if you could send me the timetable.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>I look forward to meet you next week.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I look forward to meeting you next week.</strong></p>
      <p>That <em>to</em> is a preposition, so the verb takes <b>-ing</b> (PE-64).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Write the first line: <em>You want to ask your teacher about a missed lesson.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I am writing to ask about the lesson I missed on Monday.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a short email (4 lines) asking a school for information about a course.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Dear Sir or Madam,<br>I am writing to ask about your
         evening English course. Could you tell me when it starts and how much it costs?<br>
         Thank you for your help. I look forward to hearing from you.<br>
         Yours faithfully, Afsona Yusupova</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Greeting</b><span>salomlashish</span></li>
  <li><b>Closing</b><span>xayrlashuv qismi</span></li>
  <li><b>Yours sincerely</b><span>hurmat bilan (ism maʼlum)</span></li>
  <li><b>Yours faithfully</b><span>hurmat bilan (ism nomaʼlum)</span></li>
  <li><b>To apply for</b><span>daʼvogarlik qilmoq</span></li>
  <li><b>Grateful</b><span>minnatdor</span></li>
  <li><b>To confirm</b><span>tasdiqlamoq</span></li>
  <li><b>Application form</b><span>ariza blankasi</span></li>
  <li><b>To hesitate</b><span>tortinmoq</span></li>
  <li><b>In advance</b><span>oldindan</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Five parts: <b>greeting → reason → details → request → closing</b>.</li>
    <li><b>Dear + name → Yours sincerely</b> · <b>Dear Sir or Madam → Yours faithfully</b>.</li>
    <li>State your purpose in the <b>first line</b>: <em>I am writing to…</em></li>
    <li>Requests: <b>Could you…?</b> · <b>I would be grateful if you could…</b></li>
    <li><b>I look forward to hearing</b> from you — <b>-ing</b>, never <em>hear</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-94: Telling a Story: Narrative Tenses in Action",
        "category": "english",
        "order": 94,
        "summary": (
            "How the four past tenses work together to build a story — background, events, "
            "earlier causes and the words that carry a reader along."
        ),
        "content": """
<h2>PE-94: Telling a Story: Narrative Tenses in Action</h2>

<p>You learned the past tenses one at a time. A story uses them <b>together</b>, each doing a
different job: one paints the scene, one moves the action forward, one reaches back to explain.
Get that combination right and your writing stops being a list of events and becomes a
<mark>story somebody wants to finish</mark>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Which tense does which job in a narrative</li>
    <li>The classic four-part story shape</li>
    <li>The time words that carry a reader forward</li>
    <li>How to open and close a story well</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The three jobs</span>
  <span class="pe-chip pe-chip--aux">was -ing</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">scene</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">V2</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">events</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">had + V3</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">earlier</span>
</div>

LEGEND_HERE

<h3>1. Each tense has a job</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Tense</th><th>Job in the story</th><th>Example</th></tr>
  <tr>
    <td><b>Past Continuous</b></td><td>paints the background scene</td>
    <td>The sun <b>was setting</b> and birds <b>were singing</b>.</td>
  </tr>
  <tr>
    <td><b>Past Simple</b></td><td>moves the action forward</td>
    <td>Suddenly, somebody <b>knocked</b> at the door.</td>
  </tr>
  <tr>
    <td><b>Past Perfect</b></td><td>explains something earlier</td>
    <td>I <b>had forgotten</b> to lock it.</td>
  </tr>
  <tr>
    <td><b>Past Perfect Cont.</b></td><td>how long it had been going on</td>
    <td>He <b>had been waiting</b> for an hour.</td>
  </tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">It <span class="pe-hl pe-hl--aux">was raining</span> heavily and I
     <span class="pe-hl pe-hl--aux">was walking</span> home alone. Suddenly a car
     <span class="pe-hl pe-hl--v">stopped</span> beside me. I <span class="pe-hl pe-hl--v">
     looked</span> up — it was my uncle, who <b>had been looking</b> for me for an hour.</p>
  <p class="pe-ex__uz">Kuchli yomgʻir yogʻayotgan va men uyga yolgʻiz ketayotgan edim. Toʻsatdan
     yonimda mashina toʻxtadi. Yuqoriga qaradim — bu amakim edi, u bir soatdan beri meni
     qidirayotgan edi.</p>
  <p class="pe-ex__why">Scene (Continuous) → event (Simple) → earlier cause (Perfect
     Continuous).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekcha hikoyada ham xuddi shu tuzilma bor: "<b>yogʻayotgan edi</b>" (fon),
  "<b>toʻxtadi</b>" (voqea), "<b>qidirayotgan edi</b>" (undan oldingi sabab). Yaʼni
  hikoya qurish mantigʻi bir xil — faqat ingliz tilidagi shakllarni toʻgʻri qoʻyish
  kerak: <em>was -ing</em> · <em>V2</em> · <em>had been -ing</em>.
</div>

<h3>2. The four-part shape</h3>

<ol class="pe-steps">
  <li><b>Set the scene</b> — Past Continuous, plus where and when.
      <em>Last summer I was staying with my grandparents in the village.</em></li>
  <li><b>Start the action</b> — Past Simple with a time word.
      <em>One morning, I decided to walk to the river.</em></li>
  <li><b>Build the problem</b> — Past Simple events, Past Perfect for causes.
      <em>When I got there, I realised I had left my shoes at home.</em></li>
  <li><b>Finish</b> — resolution plus a feeling.
      <em>In the end, I walked back barefoot — and I have never forgotten it.</em></li>
</ol>

<h3>3. The words that carry a reader forward</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Starting</p>
    <p><em>One day, One morning, Last summer, It all began when…</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Moving on</p>
    <p><em>Then, After that, A few minutes later, Meanwhile</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Surprise</p>
    <p><em>Suddenly, All of a sudden, Without warning, To my surprise</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Ending</p>
    <p><em>In the end, Finally, Luckily, Since then</em></p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>One morning</b> we set off early. <b>A few hours later</b> we reached
     the mountains. <b>Suddenly</b>, the weather changed. <b>In the end</b>, we had to turn
     back.</p>
  <p class="pe-ex__uz">Bir kuni ertalab erta yoʻlga chiqdik. Bir necha soatdan keyin togʻlarga
     yetib bordik. Toʻsatdan havo oʻzgardi. Oxir-oqibat, ortga qaytishga toʻgʻri keldi.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  <b>Suddenly</b> is powerful — and weak if you use it three times. One surprise per story.
  Vary with <em>To my surprise</em>, <em>Without warning</em>, or simply a short sentence:
  <em>Then the lights went out.</em>
</div>

<h3>4. Two things that lift a story</h3>

<p><b>Vary your sentence length.</b> A long descriptive sentence followed by a very short one
creates drama:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><em>We had been walking for hours through the hot, dusty valley, talking
     about nothing in particular, when Jasur stopped. He pointed. A wolf.</em></p>
  <p class="pe-ex__uz">Issiq, changli vodiyda soatlab yurgan, aytarli hech narsa haqida
     gaplashmagan edik — shu payt Jasur toʻxtadi. U barmoq bilan koʻrsatdi. Boʻri.</p>
</div>

<p>And <b>use participle clauses</b> (PE-86) to keep the pace up:</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Hearing</b> the noise, Afsona ran to the window. <b>Seeing</b> nothing,
     she went back to bed.</p>
  <p class="pe-ex__uz">Shovqinni eshitib, Afsona derazaga yugurdi. Hech narsa koʻrmagach,
     yana yotdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Hikoya yozganda eng koʻp uchraydigan xato — <b>hamma gapni bir xil uzunlikda</b> yozish.
  Uzun jumladan keyin <b>juda qisqa</b> jumla qoʻysangiz, taʼsir kuchayadi: "...gaplashib
  ketayotgan edik. Jasur toʻxtadi. Boʻri." Oʻzbek hikoyalarida ham shu usul ishlatiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Hikoyani <b>yaxshi boshlash va yaxshi tugatish</b> — ballning yarmi. Boshida joy va
  vaqtni ayting (<em>Last summer, in my grandparents' village…</em>), oxirida esa
  <b>his-tuygʻu</b> qoʻshing (<em>I have never forgotten that day</em> — "Oʻsha kunni
  hech qachon unutmayman"). Quruq "The end" deb tugatmang.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I was going to school and I was seeing an accident.</s></p>
  <p class="pe-good">Yesterday I <b>was going</b> to school when I <b>saw</b> an accident.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>When I arrived, the film already started.</s></p>
  <p class="pe-good">When I arrived, the film <b>had already started</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I had woken up, I had eaten breakfast and I had gone out.</s></p>
  <p class="pe-good">I <b>woke up</b>, <b>ate</b> breakfast and <b>went</b> out. <em>(a simple
     sequence — PE-38)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Suddenly it was raining and suddenly we ran and suddenly we arrived.</s></p>
  <p class="pe-good">It <b>started to rain</b>, so we <b>ran</b>. <b>Finally</b> we
     <b>arrived</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Walking home, my bag was stolen.</s></p>
  <p class="pe-good">Walking home, <b>I had my bag stolen</b>. <em>(PE-66, PE-86)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose the tenses: <em>I ___ (watch) TV when the lights ___ (go) out.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>was watching … went.</strong> Long background action + short interrupting
         event (PE-24).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>When we got to the station, the train ___ (leave).</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>had left</strong> — it happened before we arrived, so Past Perfect.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Set a scene in one sentence (Past Continuous).</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>It was late evening, the streets were emptying and a cold
         wind was blowing from the mountains.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Improve it: <em>I went out. I saw a dog. I was afraid. I ran home.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>As I was going out, I saw a large dog in the yard.
         <b>Feeling</b> afraid, I ran straight back home.</em></p>
      <p>Same events — but with a background tense, a participle clause and varied length.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a four-sentence story using all three narrative tenses.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Last winter I <b>was travelling</b> to Samarkand by train.
         I <b>fell</b> asleep and <b>woke up</b> at the wrong station. I <b>had forgotten</b>
         to set an alarm. <b>Luckily</b>, a kind woman <b>helped</b> me find the next
         train.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Narrative</b><span>hikoya, bayon</span></li>
  <li><b>To set the scene</b><span>fonni tasvirlamoq</span></li>
  <li><b>Background</b><span>orqa fon</span></li>
  <li><b>Suddenly</b><span>toʻsatdan</span></li>
  <li><b>Meanwhile</b><span>shu orada</span></li>
  <li><b>To my surprise</b><span>hayratimga qarshi</span></li>
  <li><b>In the end</b><span>oxir-oqibat</span></li>
  <li><b>Barefoot</b><span>yalangʻoyoq</span></li>
  <li><b>Valley</b><span>vodiy</span></li>
  <li><b>Resolution</b><span>yechim</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Past Continuous</b> = the scene · <b>Past Simple</b> = the events · <b>Past
        Perfect</b> = earlier causes.</li>
    <li>Four parts: set the scene → start the action → build the problem → finish.</li>
    <li>Time words move the reader: <b>One morning · Then · Suddenly · In the end</b>.</li>
    <li>Use <b>suddenly</b> once, not three times.</li>
    <li><b>Vary sentence length</b>, and use participle clauses to keep the pace.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-95: Giving Your Opinion and Disagreeing Politely",
        "category": "english",
        "order": 95,
        "summary": (
            "How to say what you think and say 'no' without offence — the phrases for opinions, "
            "agreement, partial agreement and polite disagreement."
        ),
        "content": """
<h2>PE-95: Giving Your Opinion and Disagreeing Politely</h2>

<p>In an exam, a discussion or a job interview, two things get you marks: saying what you think
<b>clearly</b>, and disagreeing <b>without causing offence</b>. English has a whole set of ready
phrases for both — and the crucial discovery for most learners is that a flat
<em>"No, you are wrong"</em> is much harsher in English than its Uzbek equivalent.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>Phrases for giving an opinion, from casual to formal</li>
    <li>How to agree, and how to <b>partly</b> agree</li>
    <li>The polite disagreement formula</li>
    <li>How to build a balanced argument in writing</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The polite disagreement formula</span>
  <span class="pe-chip pe-chip--s">soften</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">acknowledge</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--o">your view</span>
</div>

LEGEND_HERE

<h3>1. Giving your opinion</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Level</th><th>Phrases</th></tr>
  <tr><td>Casual</td><td>I think… · I reckon… · If you ask me…</td></tr>
  <tr><td>Neutral</td><td>In my opinion… · I believe… · It seems to me that…</td></tr>
  <tr><td>Formal / essay</td><td>In my view… · From my point of view… · It could be argued that…</td></tr>
  <tr><td>Strong</td><td>I am convinced that… · I strongly believe that…</td></tr>
  <tr><td>Careful</td><td>I tend to think… · As far as I know… · I may be wrong, but…</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>In my opinion</b>, learning a language should start early.
     <b>It seems to me that</b> children learn faster than adults.</p>
  <p class="pe-ex__uz">Menimcha, tilni erta oʻrganish kerak. Menga shunday tuyuladi: bolalar
     kattalardan tezroq oʻzlashtiradi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <s>To my opinion</s> ✗ and <s>By my opinion</s> ✗ are very common errors. The correct
  preposition is <b>in</b>: <b>in my opinion</b>. And in an essay, use it once — not in every
  paragraph.
</div>

<h3>2. Agreeing</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Full agreement</p>
    <ul>
      <li>I agree. / I completely agree.</li>
      <li>Exactly. / That's true.</li>
      <li>You're absolutely right.</li>
      <li>I couldn't agree more.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Partial agreement</p>
    <ul>
      <li>I agree up to a point.</li>
      <li>That's true, but…</li>
      <li>I see your point, however…</li>
      <li>There is some truth in that, although…</li>
    </ul>
  </div>
</div>

<p>Note the grammar: <b>I agree</b> — not <s>I am agree</s> (PE-6). <em>Agree</em> is already a
verb.</p>

<h3>3. The polite disagreement formula</h3>

<p>English almost never disagrees in one blunt move. The pattern is: <b>soften</b>, then
<b>acknowledge</b> what the other person said, then <b>give your view</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>I'm afraid I don't quite agree.</b> <b>I can see why you think that,
     but</b> in my experience the opposite is true.</p>
  <p class="pe-ex__uz">Afsuski, men bunga toʻliq qoʻshilmayman. Nega bunday deb oʻylayotganingizni
     tushunaman, lekin mening tajribamda buning aksi.</p>
  <p class="pe-ex__why">Three steps — and not one rude word.</p>
</div>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Softeners</p>
    <p><em>I'm afraid… · Actually… · To be honest… · With respect…</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Acknowledging</p>
    <p><em>I see your point… · That's a fair point, but… · I understand, however…</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Soft disagreement</p>
    <p><em>I don't quite agree · I'm not sure about that · I see it differently</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Avoid</p>
    <p><s>You are wrong.</s> <s>That's nonsense.</s> — very rude in English</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Madaniy farqni sezing: oʻzbekchada "Yoʻq, unday emas" deyish odatiy va qoʻpol emas.
  Ingliz tilida esa <em>"No, you're wrong"</em> juda qattiq eshitiladi. Shuning uchun
  <b>yumshatuvchi ibora</b> shart: <em>I'm afraid…</em>, <em>I don't quite agree…</em>,
  <em>I see your point, but…</em>. Bu — zaiflik emas, <b>madaniy norma</b>.
</div>

<h3>4. Balanced argument in writing</h3>

<p>In an essay you must show <b>both sides</b> before your conclusion. This structure scores
well because it proves you have thought about it.</p>

<ol class="pe-steps">
  <li><b>Introduce:</b> <em>People have different views on whether…</em></li>
  <li><b>One side:</b> <em>On the one hand, some people believe that… For example…</em></li>
  <li><b>The other side:</b> <em>On the other hand, others argue that…</em></li>
  <li><b>Your conclusion:</b> <em>In my view, … because …</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en"><b>On the one hand</b>, homework helps students revise. <b>On the other
     hand</b>, too much of it causes stress. <b>In my view</b>, a reasonable amount is
     best.</p>
  <p class="pe-ex__uz">Bir tomondan, uy vazifasi takrorlashga yordam beradi. Boshqa tomondan,
     uning koʻpligi stressga olib keladi. Menimcha, meʼyoridagi miqdor eng yaxshisi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu tuzilma ogʻzaki imtihonlarda ham juda yaxshi ishlaydi:
  <b>On the one hand… On the other hand… In my view…</b> Uchta ibora bilan javobingiz
  <b>tartibli va puxta</b> koʻrinadi. Yod olib qoʻysangiz, har qanday savolga shu qolip
  bilan javob bera olasiz.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng foydali toʻrtta yumshatuvchi ibora — ularni yod oling va suhbatda ishlatavering:
  <b>I'm afraid…</b> ("afsuski"), <b>Actually…</b> ("aslida"), <b>To be honest…</b>
  ("rostini aytsam"), <b>I see your point, but…</b> ("fikringizni tushunaman, lekin").
  Shu toʻrttasi bilan har qanday e'tirozni muloyim qilib aytish mumkin.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I am agree with you.</s></p>
  <p class="pe-good">I <b>agree</b> with you.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>To my opinion, it is wrong.</s></p>
  <p class="pe-good"><b>In my opinion</b>, it is wrong.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>No, you are wrong.</s></p>
  <p class="pe-good"><b>I'm afraid I don't quite agree.</b></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I agree with your opinion about that this is good.</s></p>
  <p class="pe-good">I agree <b>that</b> this is good.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>From one hand… from other hand…</s></p>
  <p class="pe-good"><b>On the one hand</b>… <b>on the other hand</b>…</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Correct it: <em>I am agree with you, but to my opinion it is difficult.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I agree with you, but in my opinion it is difficult.</strong></p>
      <p>Two classic errors: <em>am agree</em> and <em>to my opinion</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Disagree politely: <em>"Students shouldn't have any homework at all."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I see your point, but I'm afraid I don't quite agree.
         A little homework helps us remember the lesson.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Agree only partly: <em>"Learning grammar is boring."</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I agree up to a point — some exercises are dull. However,
         grammar makes everything else easier.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which is too direct for a discussion? <em>(a) I'm not sure about that. (b) That's
     nonsense. (c) I see it differently.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(b)</strong> — it would sound aggressive in English, even if the same words
         feel normal in Uzbek.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write a balanced answer (3 sentences): <em>Should schools ban mobile phones?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>On the one hand, phones distract students during lessons.
         On the other hand, they are useful for looking up information. In my view, phones
         should be allowed at break time but not in class.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Opinion</b><span>fikr</span></li>
  <li><b>To agree</b><span>qoʻshilmoq</span></li>
  <li><b>To disagree</b><span>qoʻshilmaslik</span></li>
  <li><b>Partial agreement</b><span>qismiy rozilik</span></li>
  <li><b>Softener</b><span>yumshatuvchi ibora</span></li>
  <li><b>To acknowledge</b><span>tan olmoq</span></li>
  <li><b>Balanced</b><span>muvozanatli</span></li>
  <li><b>On the one hand</b><span>bir tomondan</span></li>
  <li><b>To distract</b><span>chalgʻitmoq</span></li>
  <li><b>Offence</b><span>xafa qilish</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>In my opinion</b> — never <s>to my opinion</s>. And <b>I agree</b>, never <s>I am
        agree</s>.</li>
    <li>Disagree in three steps: <b>soften + acknowledge + your view</b>.</li>
    <li>Partial agreement is very useful: <b>I agree up to a point, but…</b></li>
    <li>Avoid <b>"You're wrong"</b> — far harsher in English than in Uzbek.</li>
    <li>For essays and speaking: <b>On the one hand … On the other hand … In my view …</b></li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
