# -*- coding: utf-8 -*-
"""Prime English — end of Block C (41) and start of Block D, modal verbs (42–45).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_41_45.py --author=prime
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
        "title": "PE-41: The 12 Tenses: The Complete Map",
        "category": "english",
        "order": 41,
        "summary": (
            "Every English tense on one page. Not twelve things to memorise — three times "
            "multiplied by four aspects, and one verb shown through all of them."
        ),
        "content": """
<h2>PE-41: The 12 Tenses: The Complete Map</h2>

<p>Stop for a moment and look at what you have done. Over the last twenty lessons you have
learned <b>every tense in the English language</b>. This lesson does not teach a new one — it
gives you the map, so that all twelve stop feeling like twelve separate problems and start
looking like what they really are: <mark>three times multiplied by four aspects</mark>. Keep
this lesson open whenever you write.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The 3 × 4 system behind all twelve tenses</li>
    <li>What each of the four <b>aspects</b> actually means</li>
    <li>One verb shown in all twelve forms</li>
    <li>Which five tenses do 90% of the work in real speech</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The whole system</span>
  <span class="pe-chip pe-chip--s">3 times</span>
  <span class="pe-op">×</span>
  <span class="pe-chip pe-chip--v">4 aspects</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--o">12 tenses</span>
</div>

<h3>1. The two questions behind every tense</h3>

<p>Every English verb form answers two questions at once. <b>When?</b> — past, present or
future. And <b>how do I see the action?</b> — that second question is called
<mark>aspect</mark>, and it is the part nobody explains at school.</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Simple — the plain fact</p>
    <p>It happened, it happens, it will happen. <em>I work.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Continuous — in the middle</p>
    <p>The action is in progress at that time. <em>I am working.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Perfect — before, with a result</p>
    <p>Finished earlier, and it matters. <em>I have worked.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Perfect Continuous — how long</p>
    <p>Duration up to that point. <em>I have been working.</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Muhim fikr: 12 ta zamonni <b>yodlash shart emas</b> — ularni <b>hisoblab chiqarish</b>
  mumkin. Avval vaqtni tanlang (oʻtgan / hozirgi / kelasi), keyin qarashni tanlang
  (oddiy / davomli / tugallangan / tugallangan davomli). Ikkisini qoʻshsangiz, kerakli
  shakl oʻzi chiqadi. Yaʼni bu — 12 ta alohida qoida emas, <b>bitta tizim</b>.
</div>

<h3>2. The complete map</h3>

<p>Here is every tense in the language, with the verb <em>work</em> and its formula. Read it
column by column and you will see the pattern repeating.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Aspect</th><th>PAST</th><th>PRESENT</th><th>FUTURE</th></tr>
  <tr>
    <td><b>Simple</b></td>
    <td>I <b>worked</b><br><em>V2</em></td>
    <td>I <b>work</b><br><em>V1 (+s)</em></td>
    <td>I <b>will work</b><br><em>will + V1</em></td>
  </tr>
  <tr>
    <td><b>Continuous</b></td>
    <td>I <b>was working</b><br><em>was/were + -ing</em></td>
    <td>I <b>am working</b><br><em>am/is/are + -ing</em></td>
    <td>I <b>will be working</b><br><em>will be + -ing</em></td>
  </tr>
  <tr>
    <td><b>Perfect</b></td>
    <td>I <b>had worked</b><br><em>had + V3</em></td>
    <td>I <b>have worked</b><br><em>have/has + V3</em></td>
    <td>I <b>will have worked</b><br><em>will have + V3</em></td>
  </tr>
  <tr>
    <td><b>Perfect Cont.</b></td>
    <td>I <b>had been working</b><br><em>had been + -ing</em></td>
    <td>I <b>have been working</b><br><em>have been + -ing</em></td>
    <td>I <b>will have been working</b><br><em>will have been + -ing</em></td>
  </tr>
</table>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Look down the columns, not across the rows. Every "Perfect" uses <b>V3</b>. Every
  "Continuous" uses <b>-ing</b>. Every "Perfect Continuous" uses <b>been + -ing</b>. Once you
  see that, you never have to memorise a single cell — you build it.
</div>

<h3>3. One story, all four aspects</h3>

<p>Watch how the same afternoon changes meaning as the aspect changes:</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>studied</b> yesterday. <em>(fact)</em><br>
     I <b>was studying</b> when you called. <em>(in the middle)</em><br>
     I <b>had studied</b> before the test began. <em>(earlier, finished)</em><br>
     I <b>had been studying</b> for hours when you called. <em>(how long)</em></p>
  <p class="pe-ex__uz">Kecha oʻqidim. — Sen qoʻngʻiroq qilganingda oʻqiyotgan edim. — Test
     boshlanishidan oldin oʻqib olgan edim. — Sen qoʻngʻiroq qilganingda bir necha soatdan
     beri oʻqiyotgan edim.</p>
  <p class="pe-ex__why">Same verb, same day, four different pictures of it.</p>
</div>

<p>And here is the same aspect moved through the three times — notice that only the helper
changes:</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>had been</b> working. → I <b>have been</b> working. →
     I <b>will have been</b> working.</p>
  <p class="pe-ex__uz">Ishlayotgan edim. → Ishlayotganimga ancha boʻldi. → Ishlayotgan
     boʻlaman.</p>
  <p class="pe-ex__why"><em>been + working</em> never moves. Only <b>had / have / will
     have</b> changes — that is the time.</p>
</div>

<h3>4. The decision questions</h3>

<ol class="pe-steps">
  <li><b>When?</b> Past, present or future — find the time word first
      (<em>yesterday, now, tomorrow, by Friday</em>).</li>
  <li><b>Is it in progress at that time?</b> → add <b>Continuous</b> (be + -ing).</li>
  <li><b>Is it finished before that time, with a result?</b> → add <b>Perfect</b>
      (have/had/will have + V3).</li>
  <li><b>Am I measuring how long it went on?</b> → add <b>Perfect Continuous</b>
      (been + -ing).</li>
</ol>

<h3>5. The five that really matter</h3>

<p>Here is the honest truth that no textbook tells you: in everyday speech, about
<b>five tenses</b> carry almost all the meaning. Master these first and you can hold any
conversation.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Use these every day</p>
    <ul>
      <li>Present Simple — <em>I work</em></li>
      <li>Present Continuous — <em>I'm working</em></li>
      <li>Past Simple — <em>I worked</em></li>
      <li>Present Perfect — <em>I've worked</em></li>
      <li>will / going to — <em>I'll work</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Rarer — but needed in exams</p>
    <ul>
      <li>Past Continuous, Past Perfect</li>
      <li>Present Perfect Continuous</li>
      <li>Future Continuous, Future Perfect</li>
      <li>Past Perfect Continuous</li>
      <li>Future Perfect Continuous <em>(very rare)</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Xotirjam boʻling: 12 tasini bir vaqtda mukammal bilish shart emas. Kundalik nutqda
  yuqoridagi <b>beshtasi</b> deyarli hamma narsani qoplaydi. Qolganlari — imtihon va yozma
  ish uchun. Shuning uchun avval shu beshtasini <b>avtomatik</b> darajaga yetkazing,
  keyin qolganlarini asta-sekin qoʻshing.
</div>

<div class="pe-ex">
  <p class="pe-ex__en">A whole day with just five tenses: <em>I <b>get up</b> at seven. Right
     now I<b>'m writing</b> this. Yesterday I <b>played</b> football. I<b>'ve finished</b> my
     homework, so tonight I<b>'ll watch</b> a film.</em></p>
  <p class="pe-ex__uz">Soat yettida turaman. Hozir shuni yozyapman. Kecha futbol oʻynadim.
     Uy vazifamni tugatdim, shuning uchun bugun kechqurun kino koʻraman.</p>
  <p class="pe-ex__why">Four sentences, five tenses, and a complete day described.</p>
</div>

<h3>6. The three rules that cross all tenses</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Stative verbs</p>
    <p><em>know, like, want, have (own)</em> take <b>no Continuous</b>, in any tense.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Time clauses</p>
    <p>After <em>when, if, as soon as, by the time</em> → <b>no will</b>.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>One marker only</p>
    <p>If the helper carries the tense, the main verb is <b>bare</b>: <em>didn't go</em>.</p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu uchta qoida <b>hamma zamonlarda</b> ishlaydi va koʻpchilik xatolar aynan shu
  yerdan chiqadi. Yozganingizdan keyin gapni shu uchtasi boʻyicha tekshiring: holat feʼli
  <b>-ing</b> olmagandir? <em>when/if</em> dan keyin <em>will</em> qoʻyilmagandir?
  Yordamchi feʼl bor joyda asosiy feʼl yalangʻoch turibdimi?
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Name the tense: <em>She had been waiting for two hours.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Past Perfect Continuous.</strong> <em>had</em> = past + perfect,
         <em>been + -ing</em> = continuous.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Build it: <b>future</b> + <b>perfect</b>, verb <em>finish</em>, subject <em>they</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>They will have finished.</strong> Future → <em>will</em>; Perfect →
         <em>have + V3</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Put <em>read</em> into all four present-time aspects.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I read · I am reading · I have read · I have been reading.</strong></p>
      <p>Fact, in progress, finished with a result, and how long.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which of the three cross-tense rules is broken? <em>When I will arrive, I will call
     you.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Rule 2 — the time clause.</strong> After <em>when</em> use the Present
         Simple: <em>When I <b>arrive</b>, I will call you.</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Choose the tense and explain: <em>Look! The children ___ (play) in the snow.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>are playing</strong> — Present Continuous. <em>Look!</em> opens a window on
         this exact moment, so the time is <b>present</b> and the aspect is
         <b>in progress</b>.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Tense</b><span>zamon</span></li>
  <li><b>Aspect</b><span>koʻrinish, tur</span></li>
  <li><b>Simple</b><span>oddiy</span></li>
  <li><b>Continuous</b><span>davomli</span></li>
  <li><b>Perfect</b><span>tugallangan</span></li>
  <li><b>Duration</b><span>davomiylik</span></li>
  <li><b>System</b><span>tizim</span></li>
  <li><b>Formula</b><span>qolip, formula</span></li>
  <li><b>To build (a form)</b><span>shakl yasamoq</span></li>
  <li><b>Everyday speech</b><span>kundalik nutq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>3 times × 4 aspects = 12 tenses.</b> Build them, don't memorise them.</li>
    <li>Perfect → <b>V3</b> · Continuous → <b>-ing</b> · Perfect Continuous → <b>been +
        -ing</b>.</li>
    <li>Ask two questions: <b>when?</b> and <b>how do I see the action?</b></li>
    <li>Five tenses carry everyday speech — master those first.</li>
    <li>Three rules cross all tenses: stative verbs, time clauses, one tense marker.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-42: can, could, be able to: Ability",
        "category": "english",
        "order": 42,
        "summary": (
            "Your first modal verbs — and the rules that govern all of them. Plus the "
            "difference between 'I could swim' and 'I was able to escape'."
        ),
        "content": """
<h2>PE-42: can, could, be able to: Ability</h2>

<p>Welcome to the <mark>modal verbs</mark> — a small family of helper words that add an
attitude to a sentence: ability, permission, obligation, certainty. They are wonderfully easy
to use, because they refuse to change their shape. No <b>-s</b>, no <b>-ed</b>, no <b>to</b>.
We start with the most useful one of all: <b>can</b>.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The four rules that govern <b>every</b> modal verb</li>
    <li><b>can</b> for ability, permission and requests</li>
    <li><b>could</b> for past ability and polite questions</li>
    <li><b>be able to</b> — and when you are forced to use it instead</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Every modal verb</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">modal</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
  <span class="pe-chip pe-chip--opt">(no to, no -s, no -ing)</span>
</div>

LEGEND_HERE

<h3>1. The four rules of all modals</h3>

<ol class="pe-steps">
  <li><b>No -s for he/she/it.</b> <em>She can swim</em>, never <s>she cans</s>.</li>
  <li><b>No "to" after them.</b> <em>I can swim</em>, never <s>I can to swim</s>.</li>
  <li><b>Questions by inversion</b> — no <em>do/does</em>: <em><b>Can</b> you swim?</em></li>
  <li><b>Negatives with "not"</b>: <em>can<b>not</b> → can't</em>. No <em>don't</em>.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Afsona</span>
     <span class="pe-hl pe-hl--aux">can</span>
     <span class="pe-hl pe-hl--v">speak</span> three languages, but she
     <span class="pe-hl pe-hl--aux">can't</span>
     <span class="pe-hl pe-hl--v">drive</span>.</p>
  <p class="pe-ex__uz">Afsona uchta tilda gapira oladi, lekin mashina hayday olmaydi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Can</b> oʻzbekchadagi "<b>-a olmoq</b>" qoʻshimchasiga toʻgʻri keladi:
  <em>bora <b>olaman</b></em> → <em>I <b>can go</b></em>, <em>qila <b>olmayman</b></em> →
  <em>I <b>can't do</b></em>. Va eng muhimi: oʻzbekchada "olmoq" feʼl boʻlgani uchun
  qoʻshimcha oladi, ingliz tilida esa <b>can</b> hech qachon oʻzgarmaydi — <s>cans</s>,
  <s>canned</s>, <s>to can</s> yoʻq.
</div>

<h3>2. What can does</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>Ability</p>
    <p><em>I <b>can</b> swim 500 metres.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>Permission</p>
    <p><em>You <b>can</b> use my pen.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>Requests</p>
    <p><em><b>Can</b> you help me, please?</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>General possibility</p>
    <p><em>It <b>can</b> get very cold here in January.</em></p>
  </div>
</div>

<h3>3. could — the past and the polite</h3>

<p><b>Could</b> has two quite different jobs. First, it is the past of <em>can</em> for
<b>general</b> abilities — things you were able to do over a long period.</p>

<div class="pe-ex">
  <p class="pe-ex__en">When I was five, I <b>could</b> already read. My grandmother
     <b>couldn't</b> write.</p>
  <p class="pe-ex__uz">Besh yoshimda men allaqachon oʻqiy olardim. Buvim yoza olmasdi.</p>
</div>

<p>Second, it makes a request softer and more polite than <em>can</em> — and here it has no
past meaning at all.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>Could</b> you open the window, please? — <b>Could</b> I borrow your
     book?</p>
  <p class="pe-ex__uz">Derazani ochib yubora olasizmi? — Kitobingizni olib turishim
     mumkinmi?</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Iltimos qilishning muloyimlik darajasi: <b>Can you…?</b> — oddiy, doʻstona
  ("...ib bera olasanmi?"). <b>Could you…?</b> — muloyimroq ("...ib bera olasizmi?").
  <b>Would you mind…?</b> — eng rasmiy. Oʻzbekchada ham "ochib yubor" / "ochib yuboring" /
  "ochib yuborsangiz maylimi" farqi borligidek. Notanish odam bilan <b>could</b> ni
  tanlang.
</div>

<h3>4. could or was able to?</h3>

<p>Here is the difference that exams love. For a <b>general</b> past ability, use
<b>could</b>. But for <b>one particular occasion</b> where somebody actually succeeded, English
prefers <b>was/were able to</b> or <b>managed to</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">could — general ability</p>
    <ul>
      <li>He <b>could</b> run very fast as a boy.</li>
      <li>She <b>could</b> play the piano at six.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">was able to — one success</p>
    <ul>
      <li>The fire started, but everyone <b>was able to</b> escape.</li>
      <li>The exam was hard, but I <b>was able to</b> pass.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  In the <b>negative</b> this difference disappears — <em>couldn't</em> is fine for both:
  <em>I <b>couldn't</b> open the door</em> ✓ (one occasion) and <em>I <b>couldn't</b> swim
  as a child</em> ✓ (general).
</div>

<h3>5. be able to — filling the gaps</h3>

<p>Modals have no infinitive, no <b>-ing</b> form and no future of their own. So when you need
<em>can</em> in a place where a modal cannot go, <b>be able to</b> steps in.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Future: I <b>will be able to</b> drive next year. <s>I will can</s><br>
     Perfect: I <b>haven't been able to</b> sleep. <s>I haven't could</s><br>
     After another verb: I want <b>to be able to</b> speak Korean.</p>
  <p class="pe-ex__uz">Kelasi yil mashina hayday olaman. — Uxlay olmadim. — Koreys tilida
     gapira olishni xohlayman.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoida oddiy: ikkita modal feʼl <b>yonma-yon kelmaydi</b>. Shuning uchun
  <s>will can</s>, <s>must can</s>, <s>to can</s> deyilmaydi — bunday joylarda
  <b>be able to</b> ishlatiladi: <em>will <b>be able to</b></em>. Oʻzbekchada
  "boraman + ola olaman" deb ikki marta aytmaganingizdek.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I can to speak English.</s></p>
  <p class="pe-good">I <b>can speak</b> English.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She cans play the guitar.</s></p>
  <p class="pe-good">She <b>can play</b> the guitar.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you can help me?</s></p>
  <p class="pe-good"><b>Can you</b> help me?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Next year I will can drive.</s></p>
  <p class="pe-good">Next year I <b>will be able to</b> drive.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The test was difficult, but I could finish it.</s></p>
  <p class="pe-good">… but I <b>was able to</b> finish it. <em>(one occasion, success)</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Correct it: <em>My brother can to swims very well.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My brother can swim very well.</strong></p>
      <p>Two rules broken at once: no <em>to</em> after a modal, and no <b>-s</b> on the main
         verb.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     could or was able to: <em>The room was dark, but Jasur <span class="pe-blank">?</span>
     find the switch.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>was able to</strong> — one particular occasion, and he succeeded. (You could
         also say <em>managed to</em>.)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Put into the future: <em>I can speak a little Korean.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I will be able to speak a little Korean.</strong></p>
      <p>Two modals cannot stand together, so <em>can</em> becomes <b>be able to</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Make the request more polite: <em>Can you pass me the salt?</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Could you pass me the salt, please?</strong></p>
      <p>Here <em>could</em> has nothing to do with the past — it simply sounds gentler.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write two sentences about yourself with <em>can</em> and <em>can't</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I <b>can</b> ride a bike and cook plov, but I
         <b>can't</b> swim yet.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Modal verb</b><span>modal feʼl</span></li>
  <li><b>Ability</b><span>qobiliyat, imkoniyat</span></li>
  <li><b>Permission</b><span>ruxsat</span></li>
  <li><b>Request</b><span>iltimos</span></li>
  <li><b>Be able to</b><span>...a olmoq</span></li>
  <li><b>To manage to</b><span>uddasidan chiqmoq</span></li>
  <li><b>To succeed</b><span>muvaffaqiyat qozonmoq</span></li>
  <li><b>To escape</b><span>qochib qutulmoq</span></li>
  <li><b>To borrow</b><span>olib turmoq</span></li>
  <li><b>Polite</b><span>xushmuomala</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>Modals take a <b>bare verb</b>: no <em>to</em>, no <b>-s</b>, no <b>-ing</b>.</li>
    <li>Questions by <b>inversion</b>, negatives with <b>not</b> — never <em>do/does</em>.</li>
    <li><b>can</b> = ability, permission, request · <b>could</b> = past ability or politeness.</li>
    <li>One past success → <b>was able to</b> / <b>managed to</b>, not <em>could</em>.</li>
    <li>Two modals never meet: use <b>will be able to</b>, <b>to be able to</b>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-43: may, might, could: Possibility",
        "category": "english",
        "order": 43,
        "summary": (
            "How sure are you? The modals that sit at 50% — plus the maybe / may be trap that "
            "catches almost every learner."
        ),
        "content": """
<h2>PE-43: may, might, could: Possibility</h2>

<p>English does not only say <em>what</em> happens — it says <b>how sure you are</b> that it
will. <em>"It will rain"</em> is a promise from the sky. <em>"It <b>might</b> rain"</em> is an
honest maybe. These three modals — <b>may</b>, <b>might</b> and <b>could</b> — are how you
speak carefully, which is exactly what educated English sounds like.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The certainty scale from 100% down to 0%</li>
    <li><b>may / might / could</b> + base verb for possible futures</li>
    <li>The negatives, and why <em>couldn't</em> is different</li>
    <li>The <b>maybe</b> vs <b>may be</b> trap</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Possibility</span>
  <span class="pe-chip pe-chip--s">Subject</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">may / might / could</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">base verb</span>
</div>

LEGEND_HERE

<h3>1. The certainty scale</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">100</span>will</p>
    <p><em>It <b>will</b> rain tomorrow.</em> — I'm certain.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">70</span>should</p>
    <p><em>It <b>should</b> arrive today.</em> — I expect it.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">50</span>may / might / could</p>
    <p><em>It <b>might</b> rain.</em> — Perhaps yes, perhaps no.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">0</span>won't</p>
    <p><em>It <b>won't</b> rain.</em> — I'm certain it will not.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">Sherbek</span>
     <span class="pe-hl pe-hl--aux">may</span>
     <span class="pe-hl pe-hl--v">come</span> to the party — he hasn't decided yet.</p>
  <p class="pe-ex__uz">Sherbek bazmga kelishi mumkin — u hali qaror qilmagan.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu uchtasi oʻzbekchadagi "<b>...ishi mumkin</b>" va "<b>balki ...ar</b>" shakllariga
  toʻgʻri keladi: <em>Balki yomgʻir yogʻ<b>ar</b></em> → <em>It <b>might</b> rain</em>,
  <em>Kelishi <b>mumkin</b></em> → <em>He <b>may</b> come</em>. Uchalasi ham taxminan
  bir xil ishonch darajasini bildiradi — 50 foiz atrofida.
</div>

<h3>2. Is there any difference between them?</h3>

<p>Honestly, very little. In modern English they are almost interchangeable for possibility.
The small shades are these:</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">may</p>
    <ul>
      <li>Slightly more formal, slightly more likely.</li>
      <li>Also used for <b>permission</b>: <em>May I come in?</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">might / could</p>
    <ul>
      <li>Slightly less certain, more everyday.</li>
      <li><em>Could</em> also suggests an <b>option</b>: <em>We could go by taxi.</em></li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">— What shall we do tonight? — We <b>could</b> watch a film, or we
     <b>might</b> just go for a walk.</p>
  <p class="pe-ex__uz">— Bugun kechqurun nima qilamiz? — Kino koʻrsak ham boʻladi, yoki
     shunchaki sayr qilarmiz.</p>
  <p class="pe-ex__why"><em>Could</em> here offers a suggestion, not a doubt.</p>
</div>

<h3>3. Negatives — and one that behaves differently</h3>

<p><b>may not</b> and <b>might not</b> mean "perhaps not". They are still 50% — just pointing
the other way.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona <b>might not</b> come — she has a lot of homework.</p>
  <p class="pe-ex__uz">Afsona kelmasligi mumkin — uning uy vazifasi koʻp.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>couldn't</b> does <b>not</b> mean "perhaps not". It means "impossible" or "was unable
  to". Compare: <em>She <b>might not</b> be at home</em> (perhaps she isn't) with
  <em>She <b>couldn't</b> be at home — I saw her at school</em> (it's impossible).
</div>

<h3>4. Talking about right now</h3>

<p>Add <b>be + -ing</b> to guess about what is happening at this moment:</p>

<div class="pe-ex">
  <p class="pe-ex__en">Jasur isn't answering. He <b>might be sleeping</b>, or he
     <b>may be studying</b>.</p>
  <p class="pe-ex__uz">Jasur javob bermayapti. U uxlayotgan boʻlishi mumkin yoki
     oʻqiyotgandir.</p>
</div>

<h3>5. may for permission</h3>

<p><b>May</b> has a second life as the most formal way to ask for or give permission. You will
hear it from officials, in announcements, and in polite company.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>May I</b> come in? — <b>May I</b> ask you a question? —
     Students <b>may</b> use the library until six.</p>
  <p class="pe-ex__uz">Kirsam maylimi? — Bir savol bersam maylimi? — Talabalar kutubxonadan
     soat oltigacha foydalanishlari mumkin.</p>
  <p class="pe-ex__why"><em>Can I…?</em> is the everyday version; <em>May I…?</em> is the
     respectful one.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>May I…?</b> — bu "<b>...sam maylimi? / ...sam boʻladimi?</b>" degani va u eng
  hurmatli shakl. Oʻqituvchingiz yoki katta yoshli odam bilan gaplashganda
  <em>May I…?</em> yoki <em>Could I…?</em> ishlating; tengdoshingiz bilan
  <em>Can I…?</em> yetarli.
</div>

<h3>6. maybe or may be?</h3>

<p>This trips up almost every learner, and the difference is simple once you see it.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">maybe — one word, an adverb</p>
    <p>Means "perhaps". Usually at the <b>start</b> of the sentence.</p>
    <p><em><b>Maybe</b> she is at home.</em></p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">may be — two words, modal + verb</p>
    <p><em>may</em> is the modal, <em>be</em> is the verb.</p>
    <p><em>She <b>may be</b> at home.</em></p>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkalasi ham "balki uydadir" deb tarjima qilinadi, lekin tuzilishi boshqacha.
  <b>Maybe</b> — bitta soʻz, gap boshida turadi va undan keyin <b>toʻliq gap</b> keladi:
  <em>Maybe she <b>is</b> at home</em>. <b>May be</b> — ikkita soʻz, egadan keyin keladi
  va <em>is</em> qoʻshilmaydi: <em>She <b>may be</b> at home</em>.
  <s>Maybe she may be at home</s> — takror boʻladi.
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>It may to rain tomorrow.</s></p>
  <p class="pe-good">It <b>may rain</b> tomorrow.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He mights come later.</s></p>
  <p class="pe-good">He <b>might come</b> later.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Maybe she is at home. — She maybe at home.</s></p>
  <p class="pe-good">She <b>may be</b> at home. / <b>Maybe</b> she <b>is</b> at home.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you may help me?</s></p>
  <p class="pe-good"><b>May I</b> help you? / <b>Could you</b> help me?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She couldn't be at home — I'm not sure.</s></p>
  <p class="pe-good">She <b>might not</b> be at home — I'm not sure.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Correct it: <em>Maybe he will comes tomorrow, or he may to come on Friday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Maybe he will come tomorrow, or he may come on Friday.</strong></p>
      <p>No <b>-s</b> and no <em>to</em> after a modal.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Rewrite with <em>may be</em>: <em>Maybe Afsona is ill.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Afsona may be ill.</strong></p>
      <p>The <em>is</em> disappears, because <b>be</b> now follows the modal.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     might not or couldn't: <em>He ___ be in Tashkent — I spoke to him here an hour
     ago.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>couldn't</strong> — you have proof, so it is impossible, not merely
         doubtful.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Guess about now: <em>The lights are on in their house.</em> (have dinner)</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>They might be having dinner.</strong></p>
      <p>Modal + <b>be + -ing</b> guesses about this exact moment.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Make the sentence less certain: <em>It will snow tonight.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It might snow tonight.</strong> (or <em>may / could snow</em>)</p>
      <p>You have moved from 100% down to about 50%.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Possibility</b><span>ehtimollik</span></li>
  <li><b>Certainty</b><span>ishonchlilik</span></li>
  <li><b>Perhaps / maybe</b><span>balki</span></li>
  <li><b>Likely</b><span>ehtimoli bor</span></li>
  <li><b>Impossible</b><span>mumkin emas</span></li>
  <li><b>To doubt</b><span>shubhalanmoq</span></li>
  <li><b>Suggestion</b><span>taklif</span></li>
  <li><b>Option</b><span>variant</span></li>
  <li><b>Formal</b><span>rasmiy</span></li>
  <li><b>To decide</b><span>qaror qilmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>may / might / could + base verb</b> ≈ 50% certain.</li>
    <li>They are almost interchangeable; <b>may</b> is a little more formal.</li>
    <li><b>may not / might not</b> = perhaps not · <b>couldn't</b> = impossible.</li>
    <li>Add <b>be + -ing</b> to guess about right now.</li>
    <li><b>Maybe</b> + full sentence · subject + <b>may be</b> + rest.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-44: must, have to, need to: Obligation",
        "category": "english",
        "order": 44,
        "summary": (
            "Who says you have to? The difference between the rule inside your head and the "
            "rule on the wall — and why must has no past tense."
        ),
        "content": """
<h2>PE-44: must, have to, need to: Obligation</h2>

<p><em>"I <b>must</b> study tonight"</em> and <em>"I <b>have to</b> study tonight"</em> both
describe a necessity — but they come from different places. The first is <b>your own</b>
decision; the second comes from outside you: a teacher, an exam, a rule. English keeps that
difference alive, and once you hear it, your sentences carry much more meaning.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>must</b> — obligation from inside, or from the speaker</li>
    <li><b>have to</b> — obligation from outside: rules and circumstances</li>
    <li>Why <b>must</b> has no past and no future of its own</li>
    <li><b>need to</b>, and how questions are formed for each</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Two sources of obligation</span>
  <span class="pe-chip pe-chip--s">I decide</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--aux">must + base verb</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--s">Someone else decides</span>
  <span class="pe-op">→</span>
  <span class="pe-chip pe-chip--v">have to + base verb</span>
</div>

LEGEND_HERE

<h3>1. must — from inside</h3>

<p>Use <b>must</b> when the necessity comes from the speaker: your own feeling, your own
decision, or an order you are giving.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">I</span>
     <span class="pe-hl pe-hl--aux">must</span>
     <span class="pe-hl pe-hl--v">call</span> my grandmother today — I promised her.</p>
  <p class="pe-ex__uz">Bugun buvimga qoʻngʻiroq qilishim kerak — unga vaʼda berganman.</p>
</div>

<p>It is also the language of written rules and strong advice, because the writer is the
authority: <em>Passengers <b>must</b> wear a seatbelt.</em></p>

<h3>2. have to — from outside</h3>

<p>Use <b>have to</b> when somebody or something else creates the obligation: a law, a
timetable, a boss, a situation.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>have to</b> wear a uniform at school. We <b>have to</b> be there
     at eight.</p>
  <p class="pe-ex__uz">Maktabda forma kiyishim kerak. Soat sakkizda u yerda boʻlishimiz
     kerak.</p>
  <p class="pe-ex__why">Nobody asked my opinion — the school decided.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Oʻzbekchada ikkalasi ham "<b>kerak</b>" yoki "<b>shart</b>" deb tarjima qilinadi, shuning
  uchun farqni <b>manbaga</b> qarab tanlang: qaror <b>oʻzimniki</b> boʻlsa — <b>must</b>
  ("Bugun oʻqishim kerak, oʻzim shunday qaror qildim"). Qoida <b>tashqaridan</b> boʻlsa —
  <b>have to</b> ("Maktab qoidasi shunday"). Shubhalansangiz, <b>have to</b> deyavering —
  u deyarli har doim toʻgʻri keladi.
</div>

<h3>3. The big practical difference: must has no other forms</h3>

<p><b>Must</b> is a modal, so it never changes (PE-42). That means it has <b>no past</b>, no
future, no infinitive. Whenever you leave the present, <b>have to</b> takes over.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Time</th><th>Form</th><th>Example</th></tr>
  <tr><td>Present</td><td>must / have to</td><td>I <b>must</b> go. / I <b>have to</b> go.</td></tr>
  <tr><td>Past</td><td><b>had to</b></td><td>I <b>had to</b> go. <s>I musted</s></td></tr>
  <tr><td>Future</td><td><b>will have to</b></td><td>I <b>will have to</b> go. <s>I will must</s></td></tr>
  <tr><td>Perfect</td><td><b>have had to</b></td><td>I <b>have had to</b> work late.</td></tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Yesterday I <b>had to</b> stay at home, and tomorrow I <b>will have
     to</b> work all day.</p>
  <p class="pe-ex__uz">Kecha uyda qolishimga toʻgʻri keldi, ertaga esa kun boʻyi ishlashimga
     toʻgʻri keladi.</p>
</div>

<h3>4. Questions and negatives — two different systems</h3>

<p><b>Must</b> behaves like a modal: inversion, no helper. <b>Have to</b> behaves like an
ordinary verb: it needs <em>do / does / did</em>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">must — modal rules</p>
    <ul>
      <li><b>Must</b> I come? <em>(rather formal)</em></li>
      <li>You <b>mustn't</b> smoke here.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">have to — ordinary verb rules</p>
    <ul>
      <li><b>Do</b> I <b>have to</b> come?</li>
      <li><b>Did</b> you <b>have to</b> pay?</li>
      <li>You <b>don't have to</b> pay.</li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  In everyday speech, <em>Must I…?</em> sounds old-fashioned or annoyed. The normal question
  is <b>Do I have to…?</b> Save <em>must</em> for statements and written rules.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>Must</b> ning yana bir maʼnosi bor — <b>kuchli tavsiya</b>, majburiyat emas:
  <em>You <b>must</b> see this film!</em> = "Bu kinoni albatta koʻring!" Bu yerda hech kim
  sizni majbur qilmayapti, shunchaki juda qattiq tavsiya qilinyapti. Oʻzbekchadagi
  "<b>albatta ...ing</b>" shakliga toʻgʻri keladi.
</div>

<h3>5. need to — the gentler necessity</h3>

<p><b>Need to</b> means the same as <em>have to</em> but sounds softer and more practical —
it is about what is <em>necessary</em>, not what is <em>ordered</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">You <b>need to</b> practise every day if you want to speak fluently.
     — I <b>don't need to</b> get up early tomorrow.</p>
  <p class="pe-ex__uz">Ravon gapirishni xohlasangiz, har kuni mashq qilishingiz kerak. —
     Ertaga erta turishim shart emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Eng koʻp uchraydigan xato — <b>must</b> ni oʻtgan zamonga qoʻyishga urinish. Ingliz
  tilida <s>musted</s> degan soʻz <b>umuman yoʻq</b>. Oʻtgan zamonda faqat <b>had to</b>
  ishlatiladi: "borishimga toʻgʻri keldi" → <em>I <b>had to</b> go</em>. Kelasi zamonda —
  <b>will have to</b>.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I must to go home now.</s></p>
  <p class="pe-good">I <b>must go</b> home now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She musts finish her homework.</s></p>
  <p class="pe-good">She <b>must finish</b> her homework.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday I must work late.</s></p>
  <p class="pe-good">Yesterday I <b>had to</b> work late.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you must wear a uniform?</s></p>
  <p class="pe-good"><b>Do you have to</b> wear a uniform?</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Next week I will must travel to Nukus.</s></p>
  <p class="pe-good">Next week I <b>will have to</b> travel to Nukus.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     must or have to: <em>Students <span class="pe-blank">?</span> show their ID card at the
     entrance.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>have to</strong> — it is the university's rule, not the speaker's wish.
         (<em>must</em> is also possible if the sign itself is speaking.)</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Put into the past: <em>I must take a taxi.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I had to take a taxi.</strong></p>
      <p><em>Must</em> has no past form at all — <b>had to</b> replaces it.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Make a question: <em>You have to work on Saturday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Do you have to work on Saturday?</strong></p>
      <p><em>Have to</em> is an ordinary verb, so it needs the helper <b>do</b>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Which sounds more personal? <em>(a) I must lose some weight. (b) I have to lose some
     weight.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a)</strong> — <em>must</em> shows it is my own decision.
         <strong>(b)</strong> suggests someone else said so, perhaps a doctor.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Put into the future: <em>She has to take an exam.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>She will have to take an exam.</strong></p>
      <p>Never <s>will must</s> — two modals cannot stand together.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Obligation</b><span>majburiyat</span></li>
  <li><b>Necessity</b><span>zarurat</span></li>
  <li><b>Rule</b><span>qoida</span></li>
  <li><b>Law</b><span>qonun</span></li>
  <li><b>Authority</b><span>vakolat, hokimiyat</span></li>
  <li><b>Uniform</b><span>forma</span></li>
  <li><b>Seatbelt</b><span>xavfsizlik kamari</span></li>
  <li><b>Entrance</b><span>kirish joyi</span></li>
  <li><b>To practise</b><span>mashq qilmoq</span></li>
  <li><b>Fluently</b><span>ravon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>must</b> = the obligation comes from <b>me</b> or from a written rule.</li>
    <li><b>have to</b> = the obligation comes from <b>outside</b>.</li>
    <li><b>must</b> has no past or future: use <b>had to</b> and <b>will have to</b>.</li>
    <li>Questions: <b>Do you have to…?</b> — not <em>Must you…?</em> in everyday speech.</li>
    <li><b>need to</b> is the softer, practical version.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-45: mustn't vs don't have to: The Dangerous Pair",
        "category": "english",
        "order": 45,
        "summary": (
            "Two negatives that look like a pair but mean opposite things — one forbids, the "
            "other frees you. In Uzbek: 'mumkin emas' and 'shart emas'."
        ),
        "content": """
<h2>PE-45: mustn't vs don't have to: The Dangerous Pair</h2>

<p>In the last lesson, <em>must</em> and <em>have to</em> were near-twins. Put <b>not</b> on
them, however, and they fly apart completely. <em>"You <b>mustn't</b> tell him"</em> means
<b>it is forbidden</b>. <em>"You <b>don't have to</b> tell him"</em> means <b>it is up to
you</b>. Getting these the wrong way round can cause real misunderstandings — which is why
they get a lesson of their own.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>mustn't</b> = prohibition — do not do it</li>
    <li><b>don't have to</b> = no obligation — do it if you like</li>
    <li>How to say each one in the past</li>
    <li>The other ways English forbids things: <em>can't, may not, not allowed to</em></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Opposite meanings</span>
  <span class="pe-chip pe-chip--neg">mustn't</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">forbidden</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">don't have to</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">optional</span>
</div>

LEGEND_HERE

<h3>1. The two meanings side by side</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">mustn't — it is forbidden</p>
    <ul>
      <li>You <b>mustn't</b> smoke here.</li>
      <li>You <b>mustn't</b> use your phone in the exam.</li>
      <li>Children <b>mustn't</b> play with matches.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">don't have to — it is your choice</p>
    <ul>
      <li>You <b>don't have to</b> come if you're tired.</li>
      <li>You <b>don't have to</b> pay — it's free.</li>
      <li>We <b>don't have to</b> wear a uniform on Fridays.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">You <span class="pe-hl pe-hl--neg">mustn't</span> take photos in the
     museum. — You <span class="pe-hl pe-hl--aux">don't have to</span> take photos; you can
     just enjoy the paintings.</p>
  <p class="pe-ex__uz">Muzeyda surat olish mumkin emas. — Surat olishingiz shart emas;
     shunchaki rasmlardan zavqlansangiz ham boʻladi.</p>
  <p class="pe-ex__why">Sentence 1 forbids. Sentence 2 sets you free.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu yerda oʻzbek tili sizga <b>mukammal kalit</b> beradi, chunki bizda ham ikkita alohida
  ibora bor: <b>mustn't</b> = "<b>mumkin emas</b>" (taqiqlangan),
  <b>don't have to</b> = "<b>shart emas</b>" (majbur emassiz, xohlasangiz qilasiz).
  Tarjima qilishdan oldin oʻzbekchada qaysi biri toʻgʻri kelishini oʻylang — javob oʻzi
  chiqadi.
</div>

<h3>2. Why they differ — where the "not" lands</h3>

<p>There is a logic behind it. Look at what the <em>not</em> is actually negating:</p>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>mustn't</p>
    <p>= "It is necessary <b>not</b> to do it." The <em>not</em> attaches to the action.</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>don't have to</p>
    <p>= "It is <b>not</b> necessary to do it." The <em>not</em> attaches to the necessity.</p>
  </div>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Say it to yourself in full: <em>mustn't</em> → "it's necessary NOT to". <em>don't have
  to</em> → "it's NOT necessary to". One sentence of self-talk and you will never mix them
  again.
</div>

<h3>3. In the past</h3>

<p><b>Mustn't</b> has no past form (remember PE-44 — <em>must</em> has no past at all). To
forbid something in the past, English uses <b>wasn't/weren't allowed to</b> or
<b>couldn't</b>.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Meaning</th><th>Present</th><th>Past</th></tr>
  <tr>
    <td>Forbidden</td>
    <td>you <b>mustn't</b> / <b>can't</b></td>
    <td>you <b>weren't allowed to</b> / <b>couldn't</b></td>
  </tr>
  <tr>
    <td>Not necessary</td>
    <td>you <b>don't have to</b></td>
    <td>you <b>didn't have to</b></td>
  </tr>
</table>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">We <b>weren't allowed to</b> leave the classroom. — Luckily, we
     <b>didn't have to</b> write the whole test.</p>
  <p class="pe-ex__uz">Sinfdan chiqishimiz mumkin emas edi. — Yaxshiyamki, butun testni
     yozishimiz shart emas edi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Diqqat: <b>mustn't</b> ning oʻtgan zamon shakli <b>yoʻq</b> (PE-44 ni eslang — <em>must</em>
  umuman oʻzgarmaydi). Oʻtmishda taqiqni aytish uchun <b>wasn't / weren't allowed to</b>
  yoki <b>couldn't</b> ishlatiladi: "chiqishimiz mumkin emas edi" →
  <em>we <b>weren't allowed to</b> leave</em>. Ammo <b>didn't have to</b> ("shart emas edi")
  bemalol ishlatilaveradi.
</div>

<h3>4. Other ways to forbid</h3>

<ul>
  <li><b>can't</b> — the everyday spoken choice: <em>You <b>can't</b> park here.</em></li>
  <li><b>may not</b> — formal, in written rules: <em>Visitors <b>may not</b> enter this
      area.</em></li>
  <li><b>be not allowed to</b> — neutral and very common: <em>We're <b>not allowed to</b>
      use phones.</em></li>
  <li><b>Don't …</b> — a direct order: <em><b>Don't</b> touch that!</em></li>
</ul>

<div class="pe-ex">
  <p class="pe-ex__en">Signs often say it shortly: <b>No smoking. No parking. Do not
     enter.</b></p>
  <p class="pe-ex__uz">Belgilarda qisqa yoziladi: chekish mumkin emas, toʻxtash taqiqlanadi,
     kirish mumkin emas.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Kundalik nutqda ingliz tilida <b>mustn't</b> dan koʻra <b>can't</b> yoki <b>not allowed
  to</b> koʻproq ishlatiladi, chunki <em>mustn't</em> ancha qatʼiy va rasmiy eshitiladi.
  Doʻstingizga "bu yerda chekma" demoqchi boʻlsangiz — <em>You <b>can't</b> smoke here</em>
  tabiiyroq.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>You mustn't pay — the entrance is free.</s></p>
  <p class="pe-good">You <b>don't have to</b> pay — the entrance is free.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You don't have to touch the wires — it's dangerous!</s></p>
  <p class="pe-good">You <b>mustn't</b> touch the wires — it's dangerous!</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Yesterday we mustn't use our phones.</s></p>
  <p class="pe-good">Yesterday we <b>weren't allowed to</b> use our phones.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>She hasn't to come tomorrow.</s></p>
  <p class="pe-good">She <b>doesn't have to</b> come tomorrow.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>You mustn't to be late.</s></p>
  <p class="pe-good">You <b>mustn't be</b> late.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Choose: <em>It's Sunday, so you <span class="pe-blank">?</span> get up early.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>don't have to</strong> — nothing is forbidden; you are simply free to sleep
         in. <em>(Oʻzbekcha: erta turish shart emas.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Choose: <em>You <span class="pe-blank">?</span> drive without a licence.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>mustn't</strong> (or <em>can't</em>) — it is against the law, so it is
         forbidden. <em>(Oʻzbekcha: guvohnomasiz haydash mumkin emas.)</em></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     What is the difference? <em>(a) You mustn't tell Afsona. (b) You don't have to tell
     Afsona.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) Keep it secret — telling her is forbidden.</strong>
         <strong>(b) Tell her if you want — it isn't necessary.</strong></p>
      <p>Opposite advice from one small change.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Put into the past: <em>You mustn't leave the room.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>You weren't allowed to leave the room.</strong> (or <em>couldn't
         leave</em>)</p>
      <p><em>Mustn't</em> has no past form.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one rule for your classroom with <em>mustn't</em> and one with <em>don't have
     to</em>.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>We <b>mustn't</b> use our phones during the lesson, but
         we <b>don't have to</b> stand up when the teacher comes in.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Prohibition</b><span>taqiq</span></li>
  <li><b>Forbidden</b><span>taqiqlangan</span></li>
  <li><b>Mustn't</b><span>mumkin emas</span></li>
  <li><b>Don't have to</b><span>shart emas</span></li>
  <li><b>Optional</b><span>ixtiyoriy</span></li>
  <li><b>Allowed</b><span>ruxsat etilgan</span></li>
  <li><b>Licence</b><span>guvohnoma</span></li>
  <li><b>Dangerous</b><span>xavfli</span></li>
  <li><b>Free (no cost)</b><span>bepul</span></li>
  <li><b>Secret</b><span>sir</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>mustn't</b> = <b>mumkin emas</b> — it is forbidden, do not do it.</li>
    <li><b>don't have to</b> = <b>shart emas</b> — you may, but you need not.</li>
    <li>Say it in full: "necessary NOT to" vs "NOT necessary to".</li>
    <li>Past: <b>weren't allowed to</b> (forbidden) · <b>didn't have to</b> (not
        necessary).</li>
    <li>In speech, <b>can't</b> and <b>not allowed to</b> are more common than
        <em>mustn't</em>.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
