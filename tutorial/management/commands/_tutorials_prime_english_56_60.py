# -*- coding: utf-8 -*-
"""Prime English — Block E, lessons 56–60 (conditionals, wishes, relatives, passive).

Written per tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md
Lesson list: tutorial/management/commands/toc_prime_english.txt

    python manage.py import_tutorials \
        tutorial/management/commands/_tutorials_prime_english_56_60.py --author=prime
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
        "title": "PE-56: Mixed Conditionals",
        "category": "english",
        "order": 56,
        "summary": (
            "When the two halves live in different times: a past cause with a present result, "
            "or a present cause with a past result."
        ),
        "content": """
<h2>PE-56: Mixed Conditionals</h2>

<p>The second and third conditionals were tidy: both halves in the same time. But real life is
not tidy. <em>"If I <b>had studied</b> medicine, I <b>would be</b> a doctor now."</em> The
cause is in the past; the result is <b>today</b>. English simply mixes the two halves — and
once you see how, this becomes one of the most natural things you can say about your own
life.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>Past cause → present result</b> — the common mix</li>
    <li><b>Present cause → past result</b> — the rarer mix</li>
    <li>How to spot which mix a sentence needs</li>
    <li>Why you already know all the pieces</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Mix 1 — past cause, present result</span>
  <span class="pe-chip pe-chip--aux">If</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">had + V3</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">would + base verb</span>
</div>

LEGEND_HERE

<h3>1. You already know the pieces</h3>

<p>Nothing new has to be learned here. You take the <b>if-half of the third conditional</b> and
join it to the <b>result-half of the second</b> — or the other way round.</p>

<div class="pe-table-wrap">
<table>
  <tr><th>Conditional</th><th>If-half</th><th>Result</th></tr>
  <tr><td>Second</td><td>past simple</td><td>would + verb</td></tr>
  <tr><td>Third</td><td>had + V3</td><td>would have + V3</td></tr>
  <tr><td><b>Mix 1</b></td><td><b>had + V3</b> (past)</td><td><b>would + verb</b> (now)</td></tr>
  <tr><td><b>Mix 2</b></td><td><b>past simple</b> (now)</td><td><b>would have + V3</b> (past)</td></tr>
</table>
</div>

<h3>2. Mix 1: past cause, present result</h3>

<p>This is by far the more common one. Something happened (or didn't) in the past, and you can
still feel the effect today.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> I <span class="pe-hl pe-hl--aux">had learned</span> to drive,
     I <span class="pe-hl pe-hl--aux">wouldn't need</span> a taxi every day.</p>
  <p class="pe-ex__uz">Agar haydashni oʻrganganimda, har kuni taksiga muhtoj boʻlmasdim.</p>
  <p class="pe-ex__why">Real facts: I didn't learn (past), and I do need a taxi (now).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> Sherbek <b>hadn't missed</b> the train, he <b>would be</b>
     here with us now.</p>
  <p class="pe-ex__uz">Agar Sherbek poyezdni oʻtkazib yubormaganida, hozir biz bilan birga
     boʻlardi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qolip oʻzbekchada ham bor va juda tabiiy eshitiladi: "Agar tibbiyotni
  <b>oʻqiganimda</b>, hozir shifokor <b>boʻlardim</b>". Eʼtibor bering — birinchi yarmi
  oʻtmish ("oʻqiganimda"), ikkinchi yarmi hozirgi holat ("hozir ... boʻlardim"). Ingliz
  tilida ham xuddi shu: <b>had + V3</b> ... <b>would + feʼl</b>.
</div>

<h3>3. Mix 2: present cause, past result</h3>

<p>The rarer direction: something that is <b>always</b> true about you or the world explains
something that happened once in the past.</p>

<div class="pe-formula">
  <span class="pe-formula__label">Mix 2 — present cause, past result</span>
  <span class="pe-chip pe-chip--aux">If</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--s">past simple</span>
  <span class="pe-op">,</span>
  <span class="pe-chip pe-chip--v">would have + V3</span>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> I <b>weren't</b> so shy, I <b>would have spoken</b> to her at
     the party.</p>
  <p class="pe-ex__uz">Agar bunchalik uyatchan boʻlmaganimda, bazmda u bilan gaplashgan
     boʻlardim.</p>
  <p class="pe-ex__why">I <b>am</b> shy — that is permanent — and because of it I said nothing
     that evening.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If</b> Afsona <b>didn't like</b> children, she <b>wouldn't have
     become</b> a teacher.</p>
  <p class="pe-ex__uz">Agar Afsona bolalarni yoqtirmaganida, oʻqituvchi boʻlmagan boʻlardi.</p>
</div>

<h3>4. How to choose</h3>

<ol class="pe-steps">
  <li><b>Look at the result half first.</b> Is the effect happening <b>now</b>, or did it
      happen <b>then</b>?</li>
  <li><b>Result now</b> (<em>now, today, still, at the moment</em>) → <b>would + base
      verb</b>.</li>
  <li><b>Result in the past</b> (<em>yesterday, at the party, last year</em>) →
      <b>would have + V3</b>.</li>
  <li><b>Then set the if-half</b> to match its own time: past event → <em>had + V3</em>;
      permanent truth → <em>past simple</em>.</li>
</ol>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Time words are your friends here. Words like <b>now, today, still</b> in the result half are
  a signal that you need <em>would + base verb</em>, even though the <em>if</em>-half is
  clearly about the past.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Qoidani sodda qilib ayting: <b>har bir yarim oʻz vaqtiga qarab yoziladi</b>. Sabab
  oʻtmishda boʻlsa — <em>had + V3</em>. Natija hozir boʻlsa — <em>would + feʼl</em>.
  Ikkalasi bir xil boʻlishi shart emas — aynan shuning uchun bu "aralash" shart gap
  deyiladi.
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Aralash shart gaplar aslida <b>hayot haqida gapirishning eng tabiiy yoʻli</b> — odamlar
  oʻz tanlovlari haqida aynan shunday gapiradi: "Agar oʻsha ishni <b>olganimda</b>, hozir
  Toshkentda <b>yashayotgan boʻlardim</b>". Oʻzbekchada ham birinchi yarim oʻtmish,
  ikkinchi yarim hozir. Demak bu qurilma sizga begona emas — faqat ingliz tilidagi
  shakllarini qoʻyish kerak.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>If I had studied medicine, I would have been a doctor now.</s></p>
  <p class="pe-good">If I had studied medicine, I <b>would be</b> a doctor now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I would have taken the job, I would be richer now.</s></p>
  <p class="pe-good"><b>If I had taken</b> the job, I would be richer now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If she wasn't so busy, she would have come yesterday.</s></p>
  <p class="pe-good">If she <b>weren't</b> so busy, she would have come yesterday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If I had slept well, I wouldn't be tired now — I would have felt fresh.</s></p>
  <p class="pe-good">If I had slept well, I <b>wouldn't be</b> tired now.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If he had left earlier, he will be here now.</s></p>
  <p class="pe-good">If he had left earlier, he <b>would be</b> here now.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Complete: <em>If I <span class="pe-blank">?</span> (not eat) so much last night, I
     <span class="pe-blank">?</span> (feel) better now.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>hadn't eaten … would feel.</strong> Past cause, present result — Mix 1. The
         word <em>now</em> tells you the result half stays in the present.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What are the real facts? <em>If Jasur had saved his money, he would have a car now.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>He didn't save his money, and he doesn't have a car now.</strong></p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Which mix? <em>If I spoke Russian, I would have understood that film.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Mix 2</strong> — present cause (I don't speak Russian, generally), past
         result (I didn't understand that particular film).</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>If we had bought the tickets last week, we wouldn't have been worried
     now.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>… we wouldn't be worried now.</strong></p>
      <p><em>Now</em> means the result is in the present, so no <em>have</em> in the result
         half.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one mixed conditional about your own life.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>If I <b>hadn't started</b> learning English three years
         ago, I <b>wouldn't understand</b> this lesson today.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Mixed conditional</b><span>aralash shart gap</span></li>
  <li><b>Cause</b><span>sabab</span></li>
  <li><b>Result</b><span>natija</span></li>
  <li><b>Permanent truth</b><span>doimiy haqiqat</span></li>
  <li><b>To save (money)</b><span>pul yigʻmoq</span></li>
  <li><b>Shy</b><span>uyatchan</span></li>
  <li><b>To miss (a train)</b><span>oʻtkazib yubormoq</span></li>
  <li><b>Worried</b><span>xavotirda</span></li>
  <li><b>Effect</b><span>taʼsir</span></li>
  <li><b>To match</b><span>mos kelmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>Mix 1:</b> If + had + V3 → <b>would + base verb</b> (past cause, present result).</li>
    <li><b>Mix 2:</b> If + past simple → <b>would have + V3</b> (present cause, past result).</li>
    <li>Write each half <b>in its own time</b> — they do not have to match.</li>
    <li>Words like <b>now, today, still</b> point to <em>would + base verb</em>.</li>
    <li>Still no <b>would</b> in the <em>if</em>-half.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-57: wish and if only",
        "category": "english",
        "order": 57,
        "summary": (
            "How English says 'koshki edi' — wishing for a different present, a different past, "
            "or for somebody to stop doing something annoying."
        ),
        "content": """
<h2>PE-57: wish and if only</h2>

<p>There is a sentence every language needs: <em>I wish things were different.</em> In Uzbek
you say <em>koshki edi</em>. English builds it with <b>wish</b> — and, exactly like the
conditionals in PE-54, it signals "this is not real" by pushing the verb <mark>one step into
the past</mark>. Learn that one idea and all three uses fall into place.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>wish + past simple</b> — a different present</li>
    <li><b>wish + past perfect</b> — a different past</li>
    <li><b>wish + would</b> — complaining about somebody's behaviour</li>
    <li>The difference between <b>wish</b> and <b>hope</b></li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Wishing about now</span>
  <span class="pe-chip pe-chip--s">I wish</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">past simple</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">but it isn't true now</span>
</div>

LEGEND_HERE

<h3>1. wish + past simple — a different present</h3>

<div class="pe-ex">
  <p class="pe-ex__en">I <span class="pe-hl pe-hl--aux">wish</span> I
     <span class="pe-hl pe-hl--v">had</span> a car.</p>
  <p class="pe-ex__uz">Koshki mashinam boʻlsa edi.</p>
  <p class="pe-ex__why">Real fact: I <b>don't</b> have a car. Past form, present meaning.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">She <b>wishes</b> she <b>lived</b> nearer to school. — I <b>wish</b> I
     <b>knew</b> the answer.</p>
  <p class="pe-ex__uz">U maktabga yaqinroq yashasa edi, deb orzu qiladi. — Koshki javobni
     bilsam edi.</p>
</div>

<p>As in the second conditional, <b>were</b> is used for every person after <em>wish</em>:
<em>I wish I <b>were</b> taller.</em></p>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>wish + oʻtgan zamon</b> oʻzbekchadagi "<b>koshki ... boʻlsa edi</b>" qolipiga toʻgʻri
  keladi: <em>I wish I had a car</em> = "Koshki mashinam boʻlsa edi". Ikkala tilda ham
  <b>oʻtgan zamon shakli</b> ishlatiladi, lekin maʼno <b>hozir</b> haqida. Bu — PE-54 dagi
  bilan bir xil mantiq.
</div>

<h3>2. wish + past perfect — a different past</h3>

<p>To regret something that already happened, push one more step back: <b>had + V3</b>.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>wish</b> I <b>had studied</b> harder for the exam.</p>
  <p class="pe-ex__uz">Koshki imtihonga qattiqroq tayyorlanganimda edi.</p>
  <p class="pe-ex__why">Real fact: I didn't study hard, and it is too late now.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek <b>wishes</b> he <b>hadn't said</b> those words.</p>
  <p class="pe-ex__uz">Sherbek oʻsha soʻzlarni aytmagan boʻlsam edi, deb afsuslanadi.</p>
</div>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">wish + past simple → now</p>
    <ul>
      <li><em>I wish I <b>had</b> more money.</em> (today)</li>
      <li><em>I wish I <b>spoke</b> Korean.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">wish + past perfect → then</p>
    <ul>
      <li><em>I wish I <b>had had</b> more money last year.</em></li>
      <li><em>I wish I <b>had learned</b> Korean at school.</em></li>
    </ul>
  </div>
</div>

<h3>3. wish + would — the complaint</h3>

<p>This third pattern is different and very useful: it complains about somebody else's
<b>behaviour</b>, and quietly asks them to change it.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>wish</b> you <b>would stop</b> interrupting me. — I <b>wish</b>
     it <b>would stop</b> raining.</p>
  <p class="pe-ex__uz">Meni boʻlishni bas qilsang edi. — Yomgʻir toʻxtasa edi.</p>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  You cannot use <b>wish + would</b> about yourself, because you can change your own
  behaviour: <s>I wish I would study more</s> ✗ → <b>I wish I studied more</b> ✓.
</div>

<h3>4. if only — the stronger version</h3>

<p><b>If only</b> works with exactly the same three structures, but it sounds more emotional —
closer to Uzbek <em>koshki</em>.</p>

<div class="pe-ex">
  <p class="pe-ex__en"><b>If only</b> I <b>knew</b> his number! — <b>If only</b> I
     <b>hadn't lost</b> my keys!</p>
  <p class="pe-ex__uz">Koshki uning raqamini bilsam edi! — Koshki kalitlarimni yoʻqotmagan
     boʻlsam edi!</p>
</div>

<h3>5. wish or hope?</h3>

<p>These two are not interchangeable, and the difference is simple. <b>Wish</b> is for things
that are <b>not true or impossible</b>. <b>Hope</b> is for things that are still
<b>possible</b>.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">wish — unreal</p>
    <ul>
      <li><em>I wish I <b>were</b> taller.</em> (I'm not)</li>
      <li><em>I wish it <b>weren't</b> raining.</em> (it is)</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">hope — still possible</p>
    <ul>
      <li><em>I hope you <b>pass</b> the exam.</em></li>
      <li><em>I hope it <b>doesn't rain</b> tomorrow.</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni tez aniqlang: <b>wish</b> = "koshki ... boʻlsa edi" (imkonsiz yoki haqiqat emas),
  <b>hope</b> = "umid qilaman" (hali boʻlishi mumkin). Shuning uchun imtihon oldidan
  doʻstingizga <em>I <b>hope</b> you pass</em> deysiz, <s>I wish you pass</s> emas.
  (Faqat <em>I wish you good luck</em> kabi tayyor iboralarda <b>wish</b> boshqacha
  ishlatiladi.)
</div>

<h3>6. The other "wish" — good wishes</h3>

<p>One more use, and it has nothing to do with regret. <b>Wish somebody something</b> means to
express a kind hope for them — and here the grammar is completely ordinary.</p>

<div class="pe-ex">
  <p class="pe-ex__en">I <b>wish you</b> good luck. — We <b>wish you</b> a happy birthday. —
     <b>Best wishes</b>, Afsona.</p>
  <p class="pe-ex__uz">Sizga omad tilayman. — Tugʻilgan kuningiz bilan tabriklaymiz. —
     Eng ezgu tilaklar bilan, Afsona.</p>
  <p class="pe-ex__why">Two objects, no past tense, no unreality — a completely different
     pattern.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Ikkalasini adashtirmang: <b>wish + gap</b> = "koshki ... boʻlsa edi" (haqiqat emas),
  <b>wish + kimga + nimani</b> = "<b>tilamoq</b>" (<em>I wish you success</em> — "sizga
  muvaffaqiyat tilayman"). Xat oxirida yoziladigan <b>Best wishes</b> ham shu ikkinchi
  maʼnoda.
</div>

<h3>7. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I wish I have more free time.</s></p>
  <p class="pe-good">I wish I <b>had</b> more free time.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I wish I would be taller.</s></p>
  <p class="pe-good">I wish I <b>were</b> taller.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I wish you will come to my party.</s></p>
  <p class="pe-good">I <b>hope</b> you<b>'ll come</b> to my party.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>I wish I studied medicine when I was young.</s></p>
  <p class="pe-good">I wish I <b>had studied</b> medicine when I was young.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>If only I would know the answer!</s></p>
  <p class="pe-good"><b>If only I knew</b> the answer!</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Rewrite with <em>wish</em>: <em>I don't have a bicycle.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I wish I had a bicycle.</strong> Present situation → past simple after
         <em>wish</em>.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Rewrite with <em>wish</em>: <em>I ate too much at lunch.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I wish I hadn't eaten so much at lunch.</strong> A past regret → past
         perfect.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     wish or hope: <em>I ___ you feel better soon.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>hope</strong> — getting better is still possible, so this is not an
         impossible wish.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     What does this really mean? <em>I wish my neighbours would turn the music down.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>They are playing loud music now, and I want them to stop.</strong>
         <em>Wish + would</em> is a complaint about somebody's behaviour.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Write one <em>wish</em> about now and one about the past.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>I wish I <b>lived</b> closer to my school. I wish I
         <b>had joined</b> the English club last year.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>To wish</b><span>orzu qilmoq</span></li>
  <li><b>If only</b><span>koshki edi</span></li>
  <li><b>To hope</b><span>umid qilmoq</span></li>
  <li><b>Regret</b><span>afsus</span></li>
  <li><b>To complain</b><span>shikoyat qilmoq</span></li>
  <li><b>Behaviour</b><span>xatti-harakat</span></li>
  <li><b>To interrupt</b><span>gapini boʻlmoq</span></li>
  <li><b>Neighbour</b><span>qoʻshni</span></li>
  <li><b>To turn down</b><span>ovozini pasaytirmoq</span></li>
  <li><b>Impossible</b><span>imkonsiz</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>wish + past simple</b> = I want a different <b>present</b>.</li>
    <li><b>wish + past perfect</b> = I regret a different <b>past</b>.</li>
    <li><b>wish + would</b> = I want <b>somebody else</b> to change their behaviour.</li>
    <li><b>if only</b> = the same, but stronger — Uzbek <em>koshki</em>.</li>
    <li><b>wish</b> = not real · <b>hope</b> = still possible.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-58: Relative Clauses: who, which, that",
        "category": "english",
        "order": 58,
        "summary": (
            "How to add information about a noun without starting a new sentence — and why "
            "English puts the description AFTER the noun, unlike Uzbek."
        ),
        "content": """
<h2>PE-58: Relative Clauses: who, which, that</h2>

<p>Compare these: <em>"I have a friend. He lives in Khiva. He is a doctor."</em> versus
<em>"I have a friend <b>who lives in Khiva</b> and <b>who is a doctor</b>."</em> The second
sounds like an adult speaking. The tool is a <mark>relative clause</mark> — a small piece of
information attached to a noun. And it involves one big structural difference from Uzbek that
is worth understanding properly.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>who, which, that, whose, where, when</b> — and which noun each one follows</li>
    <li>Why English puts the description <b>after</b> the noun</li>
    <li>When you can leave the relative pronoun out</li>
    <li>The "double object" mistake</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">Word order</span>
  <span class="pe-chip pe-chip--s">noun</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">who / which / that</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">the information</span>
</div>

LEGEND_HERE

<h3>1. The structural difference from Uzbek</h3>

<p>Uzbek puts the description <b>before</b> the noun: <em><u>men oʻqigan</u> kitob</em>.
English puts it <b>after</b>: <em>the book <u>that I read</u></em>. This single fact explains
a large share of the mistakes learners make with these clauses.</p>

<div class="pe-ex">
  <p class="pe-ex__en">the man <b>who lives next door</b> · the book <b>that I bought</b> ·
     the school <b>where I study</b></p>
  <p class="pe-ex__uz">qoʻshnimizda yashaydigan odam · men sotib olgan kitob · men oʻqiydigan
     maktab</p>
  <p class="pe-ex__why">In Uzbek the description comes first; in English it always follows the
     noun.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu — eng muhim tuzilmaviy farq. Oʻzbekchada aniqlovchi <b>otdan oldin</b> keladi:
  "<u>men oʻqigan</u> kitob". Ingliz tilida esa <b>otdan keyin</b>: "the book <u>that I
  read</u>". Shuning uchun gap tuzayotganda avval <b>otni</b> ayting, keyin uni
  <b>who / which / that</b> bilan davom ettiring — teskarisi emas.
</div>

<h3>2. Which word for which noun</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>who — people</p>
    <p><em>the girl <b>who</b> won the prize</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>which — things</p>
    <p><em>the film <b>which</b> we watched</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>that — both</p>
    <p><em>the man <b>that</b> called · the book <b>that</b> I read</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>whose — possession</p>
    <p><em>the boy <b>whose</b> bike was stolen</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">5</span>where — places</p>
    <p><em>the town <b>where</b> I was born</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">6</span>when — times</p>
    <p><em>the day <b>when</b> we met</em></p>
  </div>
</div>

<p><b>That</b> is the friendly all-rounder — it can replace <em>who</em> or <em>which</em> in
everyday English. (There is one situation where it cannot, and that is PE-59.)</p>

<h3>3. When can you leave it out?</h3>

<p>Here is a rule that instantly makes your English sound more natural. If the relative pronoun
is the <b>object</b> of its clause — if another subject follows it — you may simply drop it.</p>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Subject → must keep it</p>
    <ul>
      <li>the man <b>who</b> <u>lives</u> next door</li>
      <li>the bus <b>which</b> <u>goes</u> to the centre</li>
    </ul>
    <p>A verb follows directly.</p>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Object → can drop it</p>
    <ul>
      <li>the book (<b>that</b>) <u>I</u> bought</li>
      <li>the girl (<b>who</b>) <u>you</u> met</li>
    </ul>
    <p>A new subject follows.</p>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">The film <b>we saw</b> yesterday was excellent. — The man
     <b>who helped</b> us was very kind.</p>
  <p class="pe-ex__uz">Kecha koʻrgan filmimiz ajoyib edi. — Bizga yordam bergan odam juda
     mehribon edi.</p>
  <p class="pe-ex__why">Sentence 1 drops <em>that</em> (object); sentence 2 must keep
     <em>who</em> (subject).</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">That's the boy <b>whose father</b> teaches us maths, and this is the
     house <b>where he lives</b>.</p>
  <p class="pe-ex__uz">Anavi — otasi bizga matematikadan dars beradigan bola, bu esa u
     yashaydigan uy.</p>
  <p class="pe-ex__why"><em>Whose</em> replaces <em>his</em>; <em>where</em> replaces
     <em>in which</em>.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tushirib qoldirish qoidasini oson tekshiring: <b>who / that</b> dan keyin darrov
  <b>feʼl</b> kelsa — uni <b>tushirib boʻlmaydi</b> (<em>the man who <u>lives</u></em>).
  Agar undan keyin <b>yangi ega</b> kelsa (I, you, he...) — <b>tushirsa boʻladi</b>
  (<em>the book (that) <u>I</u> read</em>). Jonli nutqda ingliz tilida uni koʻpincha
  tushirib qoldirishadi.
</div>

<h3>4. The double-object mistake</h3>

<p>Because Uzbek builds these phrases differently, learners often repeat the object at the end.
The relative pronoun <b>is</b> the object — nothing else is needed.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>The book that I read it was interesting.</s></p>
  <p class="pe-good">The book <b>that I read</b> was interesting.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The city where I live in is beautiful.</s></p>
  <p class="pe-good">The city <b>where I live</b> is beautiful. / The city <b>which I live
     in</b> is beautiful.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>that</b> soʻzining oʻzi allaqachon "kitobni" degan maʼnoni oʻz ichiga oladi, shuning
  uchun oxirida yana <em>it</em> qoʻshilmaydi: <s>the book that I read <b>it</b></s> ✗.
  Xuddi shunday, <b>where</b> ichida "da" bor: <s>the city where I live <b>in</b></s> ✗.
  Bitta gapda bitta toʻldiruvchi yetarli.
</div>

<h3>5. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>I have a friend which lives in Nukus.</s></p>
  <p class="pe-good">I have a friend <b>who</b> lives in Nukus.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The man who's car was stolen called the police.</s></p>
  <p class="pe-good">The man <b>whose</b> car was stolen called the police.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>This is the house where I was born in it.</s></p>
  <p class="pe-good">This is the house <b>where I was born</b>.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The lives next door man is a doctor.</s></p>
  <p class="pe-good">The man <b>who lives next door</b> is a doctor.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Do you know the girl who she won the competition?</s></p>
  <p class="pe-good">Do you know the girl <b>who won</b> the competition?</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Join: <em>I met a woman. She teaches Korean.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>I met a woman who teaches Korean.</strong></p>
      <p><em>Who</em> is the subject of <em>teaches</em>, so it cannot be dropped.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Join, then drop the pronoun if possible: <em>This is the phone. I bought it
     yesterday.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>This is the phone (that) I bought yesterday.</strong></p>
      <p>A new subject (<em>I</em>) follows, so <em>that</em> is optional — and notice
         <em>it</em> disappears.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Choose: <em>The teacher <span class="pe-blank">?</span> daughter is in my class is very
     strict.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>whose</strong> — it shows possession: the daughter belongs to the teacher.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Correct it: <em>The restaurant where we ate in it was cheap.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The restaurant where we ate was cheap.</strong></p>
      <p><em>Where</em> already contains "in which", so both <em>in</em> and <em>it</em>
         must go.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Describe your best friend in one sentence using a relative clause.</p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Model:</strong> <em>Afsona is the friend <b>who always helps me</b> when I
         have a problem.</em></p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Relative clause</b><span>aniqlovchi ergash gap</span></li>
  <li><b>Relative pronoun</b><span>nisbiy olmosh</span></li>
  <li><b>To describe</b><span>taʼriflamoq</span></li>
  <li><b>Whose</b><span>kimning</span></li>
  <li><b>To omit / drop</b><span>tushirib qoldirmoq</span></li>
  <li><b>Competition</b><span>musobaqa</span></li>
  <li><b>To steal</b><span>oʻgʻirlamoq</span></li>
  <li><b>Strict</b><span>talabchan</span></li>
  <li><b>Next door</b><span>qoʻshnida</span></li>
  <li><b>Excellent</b><span>ajoyib</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li>English puts the description <b>after</b> the noun — Uzbek puts it before.</li>
    <li><b>who</b> people · <b>which</b> things · <b>that</b> both · <b>whose</b> possession ·
        <b>where</b> places.</li>
    <li>Drop the pronoun when a <b>new subject</b> follows it: <em>the book I read</em>.</li>
    <li>Never repeat the object: <s>the book that I read it</s>.</li>
    <li><b>where</b> already means "in which" — don't add a preposition.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-59: Defining vs Non-Defining Relative Clauses",
        "category": "english",
        "order": 59,
        "summary": (
            "Two commas that change what a sentence means — how English separates essential "
            "information from extra information."
        ),
        "content": """
<h2>PE-59: Defining vs Non-Defining Relative Clauses</h2>

<p>Read these two sentences slowly:</p>

<p><em>"My brother <b>who lives in Tashkent</b> is a doctor."</em><br>
<em>"My brother<b>,</b> who lives in Tashkent<b>,</b> is a doctor."</em></p>

<p>The first says I have <b>several brothers</b>, and I'm telling you which one. The second
says I have <b>one brother</b>, and I'm adding a fact about him. Two commas changed the size of
my family — and that is the whole lesson.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li><b>Defining</b> clauses — essential, no commas</li>
    <li><b>Non-defining</b> clauses — extra, commas required</li>
    <li>The three rules that change with the commas</li>
    <li><b>which</b> referring to a whole idea</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The difference</span>
  <span class="pe-chip pe-chip--s">no commas</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">which one — essential</span>
  <span class="pe-op">·</span>
  <span class="pe-chip pe-chip--v">commas</span>
  <span class="pe-op">=</span>
  <span class="pe-chip pe-chip--opt">extra information</span>
</div>

LEGEND_HERE

<h3>1. Defining — it tells you which one</h3>

<p>A <b>defining</b> clause is essential. Remove it and the sentence no longer identifies
anybody. No commas are used.</p>

<div class="pe-ex">
  <p class="pe-ex__en">The student <b>who sits next to me</b> is from Nukus.</p>
  <p class="pe-ex__uz">Yonimda oʻtiradigan oʻquvchi Nukusdan.</p>
  <p class="pe-ex__why">Take the clause away and you get <em>"The student is from Nukus"</em> —
     which student?</p>
</div>

<h3>2. Non-defining — it just adds a fact</h3>

<p>A <b>non-defining</b> clause is extra. We already know exactly who or what is meant; the
clause simply adds information. It always sits between commas.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona<b>,</b> <b>who sits next to me</b><b>,</b> is from Nukus.</p>
  <p class="pe-ex__uz">Afsona, yonimda oʻtiradigan qiz, Nukusdan.</p>
  <p class="pe-ex__why">We know who Afsona is. Remove the clause and the sentence still works
     perfectly.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Farqni ikki savol bilan aniqlang: <b>"Qaysi biri?"</b> degan savolga javob berayotgan
  boʻlsa — bu <b>defining</b>, vergul <b>qoʻyilmaydi</b>. Agar allaqachon kim ekani maʼlum
  boʻlsa va siz shunchaki <b>qoʻshimcha maʼlumot</b> berayotgan boʻlsangiz — bu
  <b>non-defining</b>, ikki tomondan <b>vergul qoʻyiladi</b>. Ism (Afsona, Toshkent) bilan
  deyarli doim ikkinchisi boʻladi.
</div>

<h3>3. Three rules change with the commas</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Defining (no commas)</p>
    <ul>
      <li><b>that</b> is allowed ✓</li>
      <li>you <b>can drop</b> the object pronoun ✓</li>
      <li>no commas ✓</li>
      <li><em>The book (that) I read was good.</em></li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Non-defining (commas)</p>
    <ul>
      <li><b>that</b> is forbidden ✗</li>
      <li>you <b>cannot drop</b> the pronoun ✗</li>
      <li>commas required ✓</li>
      <li><em>This book, which I read last year, was good.</em></li>
    </ul>
  </div>
</div>

<div class="pe-call pe-warn">
  <span class="pe-call__t">Careful</span>
  <b>That</b> can never follow a comma. <s>Afsona, that lives next door, is my friend</s> ✗ →
  <b>Afsona, who lives next door, is my friend</b> ✓.
</div>

<h3>4. When do you need commas?</h3>

<ol class="pe-steps">
  <li><b>Is the noun already unique?</b> A name (<em>Afsona, Bukhara</em>), <em>my mother</em>,
      <em>this book</em> → commas.</li>
  <li><b>Could the sentence lose the clause and still make sense?</b> → commas.</li>
  <li><b>Does the clause answer "which one?"</b> → no commas.</li>
  <li><b>When in doubt in speech</b>, listen for a small pause — a pause means a comma.</li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">Students <b>who work hard</b> pass the exam. <em>(only those
     students)</em><br>
     My best friend<b>,</b> who works very hard<b>,</b> passed the exam. <em>(one person,
     extra fact)</em></p>
  <p class="pe-ex__uz">Qattiq ishlaydigan oʻquvchilar imtihondan oʻtadi. — Eng yaqin
     doʻstim, u juda tirishqoq, imtihondan oʻtdi.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Gapirganda vergul <b>eshitiladi</b>: non-defining gapdan oldin va keyin kichik
  <b>pauza</b> boʻladi — "Afsona, <i>(pauza)</i> yonimda oʻtiradigan qiz, <i>(pauza)</i>
  Nukusdan". Defining gapda esa pauza yoʻq, hammasi bir nafasda aytiladi. Shuning uchun
  yozayotganda gapni ovoz chiqarib oʻqing: pauza boʻlsa — vergul qoʻying.
</div>

<h3>5. which for a whole idea</h3>

<p>In non-defining clauses only, <b>which</b> can refer back to the <b>entire sentence</b>, not
just one noun. This is very common in good writing.</p>

<div class="pe-ex">
  <p class="pe-ex__en">Sherbek arrived two hours late<b>, which</b> annoyed everybody.</p>
  <p class="pe-ex__uz">Sherbek ikki soat kechikib keldi, bu esa hammani jahlini chiqardi.</p>
  <p class="pe-ex__why"><em>Which</em> = "the fact that he arrived late", not any single
     noun.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Bu qurilma oʻzbekchadagi "<b>bu esa</b>" bogʻlovchisiga toʻgʻri keladi: <em>U kechikdi,
  <b>bu esa</b> hammaga yoqmadi</em> → <em>He was late, <b>which</b> annoyed everyone</em>.
  Diqqat: bu holatda <b>what</b> emas, <b>which</b> ishlatiladi — <s>He was late, what
  annoyed everyone</s> notoʻgʻri.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>My mother who is a teacher works at school 12.</s></p>
  <p class="pe-good">My mother<b>,</b> who is a teacher<b>,</b> works at school 12.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>Bukhara, that is an ancient city, is beautiful.</s></p>
  <p class="pe-good">Bukhara<b>, which</b> is an ancient city, is beautiful.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The car, I bought last year, broke down.</s></p>
  <p class="pe-good">The car <b>(that) I bought</b> last year broke down. <em>(defining — no commas)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He failed the exam, what surprised us all.</s></p>
  <p class="pe-good">He failed the exam<b>, which</b> surprised us all.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My friend, lives in Khiva, is coming tomorrow.</s></p>
  <p class="pe-good">My friend<b>, who</b> lives in Khiva, is coming tomorrow.</p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Commas or not? <em>Samarkand which is famous for its mosques attracts many tourists.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Samarkand, which is famous for its mosques, attracts many tourists.</strong></p>
      <p>There is only one Samarkand, so the clause can only be extra information.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     What do these two mean? <em>(a) My sister who lives in Tashkent is a nurse.
     (b) My sister, who lives in Tashkent, is a nurse.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) I have more than one sister</strong> — this is the Tashkent one.
         <strong>(b) I have one sister</strong>, and by the way she lives in Tashkent.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>Jasur, that won the competition, is my cousin.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Jasur, who won the competition, is my cousin.</strong></p>
      <p><em>That</em> can never appear in a non-defining clause.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Add a comment with <em>which</em>: <em>It rained all weekend.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>It rained all weekend, which ruined our plans.</strong></p>
      <p><em>Which</em> refers to the whole first half of the sentence.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Can you drop the pronoun? <em>(a) The film that we saw was long.
     (b) That film, which we saw last week, was long.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>(a) Yes</strong> — <em>The film we saw was long.</em>
         <strong>(b) No</strong> — a non-defining clause always keeps its pronoun.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Defining</b><span>aniqlovchi (zarur)</span></li>
  <li><b>Non-defining</b><span>qoʻshimcha maʼlumot beruvchi</span></li>
  <li><b>Essential</b><span>zarur</span></li>
  <li><b>Extra information</b><span>qoʻshimcha maʼlumot</span></li>
  <li><b>Comma</b><span>vergul</span></li>
  <li><b>Unique</b><span>yagona</span></li>
  <li><b>To identify</b><span>aniqlamoq</span></li>
  <li><b>To annoy</b><span>jahlini chiqarmoq</span></li>
  <li><b>Ancient</b><span>qadimiy</span></li>
  <li><b>To ruin</b><span>barbod qilmoq</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>No commas</b> = essential, tells you <b>which one</b>.</li>
    <li><b>Commas</b> = extra information you could remove.</li>
    <li>With commas: <b>no <em>that</em></b>, and the pronoun <b>cannot</b> be dropped.</li>
    <li>Names and unique things almost always take <b>commas</b>.</li>
    <li><b>, which</b> can comment on the whole sentence — never <em>what</em>.</li>
  </ul>
</div>
""",
    },

    # ══════════════════════════════════════════════════════════════════
    {
        "title": "PE-60: Passive Voice: Present and Past",
        "category": "english",
        "order": 60,
        "summary": (
            "When the doer doesn't matter: be + V3. The structure behind almost all academic "
            "and news English."
        ),
        "content": """
<h2>PE-60: Passive Voice: Present and Past</h2>

<p><em>"Somebody built this house in 1890."</em> Who? Nobody knows, and nobody cares — the
house is what matters. So English says: <em>"This house <b>was built</b> in 1890."</em> That is
the <mark>passive voice</mark>, and it is everywhere in news, science and formal writing.
Fortunately, Uzbek has a passive too, so the idea is already familiar.</p>

<div class="pe-goal">
  <p class="pe-goal__title">In this lesson you will learn</p>
  <ul>
    <li>The formula <b>be + V3</b> in the present and the past</li>
    <li>The four reasons English chooses the passive</li>
    <li>How to turn an active sentence into a passive one</li>
    <li>When to add <b>by</b> — and when to leave it out</li>
  </ul>
</div>

<div class="pe-formula">
  <span class="pe-formula__label">The passive</span>
  <span class="pe-chip pe-chip--s">Subject (receiver)</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--aux">am / is / are / was / were</span>
  <span class="pe-op">+</span>
  <span class="pe-chip pe-chip--v">V3</span>
</div>

LEGEND_HERE

<h3>1. Active and passive — the same event, a different focus</h3>

<div class="pe-vs">
  <div class="pe-vs__card">
    <p class="pe-vs__h">Active — the doer is the subject</p>
    <ul>
      <li>Millions of people <b>speak</b> English.</li>
      <li>Amir Temur <b>built</b> this mosque.</li>
      <li>Somebody <b>stole</b> my bike.</li>
    </ul>
  </div>
  <div class="pe-vs__card pe-vs__card--alt">
    <p class="pe-vs__h">Passive — the receiver is the subject</p>
    <ul>
      <li>English <b>is spoken</b> by millions.</li>
      <li>This mosque <b>was built</b> by Amir Temur.</li>
      <li>My bike <b>was stolen</b>.</li>
    </ul>
  </div>
</div>

<div class="pe-ex">
  <p class="pe-ex__en"><span class="pe-hl pe-hl--s">The letters</span>
     <span class="pe-hl pe-hl--aux">are</span>
     <span class="pe-hl pe-hl--v">delivered</span> every morning.</p>
  <p class="pe-ex__uz">Xatlar har kuni ertalab yetkaziladi.</p>
  <p class="pe-ex__why">Who delivers them? The postman, obviously — so we don't bother saying
     it.</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Yaxshi xabar: oʻzbek tilida ham majhul nisbat bor va u <b>-il / -in</b> qoʻshimchalari
  bilan yasaladi: <em>yoz<b>il</b>di</em>, <em>qur<b>il</b>gan</em>, <em>ayt<b>il</b>adi</em>.
  Ingliz tilida esa qoʻshimcha emas, <b>ikkita soʻz</b> ishlatiladi: <b>be</b> + <b>V3</b>.
  Yaʼni maʼno tanish, faqat shakli boshqacha.
</div>

<h3>2. The two tenses</h3>

<div class="pe-table-wrap">
<table>
  <tr><th>Tense</th><th>Active</th><th>Passive</th></tr>
  <tr>
    <td>Present Simple</td>
    <td>They <b>clean</b> the room.</td>
    <td>The room <b>is cleaned</b>.</td>
  </tr>
  <tr>
    <td>Present Simple (plural)</td>
    <td>They <b>clean</b> the rooms.</td>
    <td>The rooms <b>are cleaned</b>.</td>
  </tr>
  <tr>
    <td>Past Simple</td>
    <td>They <b>cleaned</b> the room.</td>
    <td>The room <b>was cleaned</b>.</td>
  </tr>
  <tr>
    <td>Past Simple (plural)</td>
    <td>They <b>cleaned</b> the rooms.</td>
    <td>The rooms <b>were cleaned</b>.</td>
  </tr>
</table>
</div>

<p>Notice what carries the tense: the verb <b>be</b>. The V3 never changes at all.</p>

<h3>3. Why choose the passive?</h3>

<div class="pe-grid">
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">1</span>The doer is unknown</p>
    <p><em>My phone <b>was stolen</b> yesterday.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">2</span>The doer is obvious</p>
    <p><em>He <b>was arrested</b>.</em> (by the police, of course)</p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">3</span>The doer doesn't matter</p>
    <p><em>Rice <b>is grown</b> in Khorezm.</em></p>
  </div>
  <div class="pe-card">
    <p class="pe-card__h"><span class="pe-card__n">4</span>Formal / scientific writing</p>
    <p><em>The water <b>was heated</b> to 80°.</em></p>
  </div>
</div>

<h3>4. How to change active into passive</h3>

<ol class="pe-steps">
  <li><b>Find the object</b> of the active sentence — it becomes the new subject.
      <em>Ali wrote <u>the letter</u>.</em></li>
  <li><b>Put <em>be</em> in the same tense</b> as the original verb.
      <em>wrote</em> (past) → <em>was</em>.</li>
  <li><b>Add the V3</b> of the main verb. → <em>The letter <b>was written</b>.</em></li>
  <li><b>Add <em>by</em> + the doer</b> only if it is useful information.
      <em>… by Ali.</em></li>
</ol>

<div class="pe-ex">
  <p class="pe-ex__en">Afsona painted this picture. → This picture <b>was painted by
     Afsona</b>.</p>
  <p class="pe-ex__uz">Bu rasmni Afsona chizgan. → Bu rasm Afsona tomonidan chizilgan.</p>
  <p class="pe-ex__why">Keep <em>by</em> here — the artist is exactly the interesting part.</p>
</div>

<div class="pe-call pe-tip">
  <span class="pe-call__t">Teacher's tip</span>
  Most passive sentences have <b>no</b> <em>by</em>-phrase at all. Add it only when the doer
  genuinely adds information. Writing <em>"My bike was stolen by somebody"</em> is worse than
  simply <em>"My bike was stolen."</em>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  <b>by</b> oʻzbekchadagi "<b>tomonidan</b>" ga toʻgʻri keladi va xuddi shunday —
  u ham koʻpincha <b>tushirib qoldiriladi</b>. "Uy 1890-yilda qurilgan" deymiz, "kim
  tomonidan" demaymiz. Ingliz tilida ham shunday: <em>The house was built in 1890</em>
  yetarli.
</div>

<h3>5. Not every verb can be passive</h3>

<p>Here is a rule that saves you from strange sentences. A verb can only go into the passive if
it has an <b>object</b> — something that receives the action. Verbs like <em>sleep, arrive,
happen, come, go, fall, die, live</em> have no object, so they have <b>no passive form at
all</b>.</p>

<div class="pe-fix">
  <p class="pe-bad"><s>The accident was happened yesterday.</s></p>
  <p class="pe-good">The accident <b>happened</b> yesterday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>He was arrived at six o'clock.</s></p>
  <p class="pe-good">He <b>arrived</b> at six o'clock.</p>
</div>

<div class="pe-ex">
  <p class="pe-ex__en">✓ They <b>built</b> the bridge. → The bridge <b>was built</b>.
     <em>(built what? → has an object)</em><br>
     ✗ The bridge <b>fell</b>. → <s>The bridge was fallen.</s> <em>(fell what? → no
     object)</em></p>
  <p class="pe-ex__uz">Koʻprikni qurishdi → Koʻprik qurildi. — Koʻprik qulab tushdi
     (majhul shakli yoʻq).</p>
</div>

<div class="pe-call pe-uz">
  <span class="pe-call__t">Oʻzbekcha</span>
  Tekshiruv savoli oddiy: feʼldan keyin <b>"nimani? kimni?"</b> deb soʻrash mumkinmi?
  Mumkin boʻlsa — majhul nisbat yasaladi (<em>yozmoq → yozildi</em>). Mumkin boʻlmasa
  (<em>kelmoq, uxlamoq, sodir boʻlmoq</em>) — majhul shakli <b>yoʻq</b>. Shuning uchun
  <s>was happened</s>, <s>was arrived</s> kabi gaplar notoʻgʻri.
</div>

<h3>6. Common mistakes</h3>

<div class="pe-fix">
  <p class="pe-bad"><s>English is speak in many countries.</s></p>
  <p class="pe-good">English <b>is spoken</b> in many countries. <em>(V3, not V1)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The house built in 1890.</s></p>
  <p class="pe-good">The house <b>was built</b> in 1890. <em>(the "be" is missing)</em></p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>My bag was stole yesterday.</s></p>
  <p class="pe-good">My bag <b>was stolen</b> yesterday.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The letters was sent last week.</s></p>
  <p class="pe-good">The letters <b>were</b> sent last week.</p>
</div>
<div class="pe-fix">
  <p class="pe-bad"><s>The window was broken by somebody.</s></p>
  <p class="pe-good">The window <b>was broken</b>. <em>(drop the useless "by somebody")</em></p>
</div>

<h3>Practice</h3>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">1</span>
     Make it passive: <em>They sell fresh bread here every morning.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Fresh bread is sold here every morning.</strong></p>
      <p>Present tense, singular subject → <em>is</em> + V3.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">2</span>
     Make it passive: <em>Somebody stole my wallet on the bus.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>My wallet was stolen on the bus.</strong></p>
      <p>Drop <em>somebody</em> — that is exactly why the passive exists here.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">3</span>
     Correct it: <em>These carpets are make in Bukhara.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>These carpets are made in Bukhara.</strong></p>
      <p>After <em>be</em> always comes the <b>third form</b>, never the base form.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">4</span>
     Should you keep the <em>by</em>-phrase? <em>The Registan was designed by Ulugh Beg's
     architects.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>Yes</strong> — the architects are interesting, important information. Compare
         <em>"The floor was cleaned by a cleaner"</em>, where the phrase adds nothing.</p>
    </div>
  </details>
</div>

<div class="pe-quiz">
  <p class="pe-quiz__q"><span class="pe-quiz__n">5</span>
     Make it active: <em>The exam results are announced in July.</em></p>
  <details class="pe-reveal"><summary>Show answer</summary>
    <div class="pe-reveal__a">
      <p><strong>The school announces the exam results in July.</strong></p>
      <p>You have to invent a doer — which shows why the passive was convenient in the first
         place.</p>
    </div>
  </details>
</div>

<h3>Key words — Kalit soʻzlar</h3>
<ul class="pe-gloss">
  <li><b>Passive voice</b><span>majhul nisbat</span></li>
  <li><b>Active voice</b><span>aniq nisbat</span></li>
  <li><b>The doer / agent</b><span>bajaruvchi</span></li>
  <li><b>Receiver</b><span>qabul qiluvchi</span></li>
  <li><b>To deliver</b><span>yetkazib bermoq</span></li>
  <li><b>To announce</b><span>eʼlon qilmoq</span></li>
  <li><b>To arrest</b><span>hibsga olmoq</span></li>
  <li><b>To grow (crops)</b><span>yetishtirmoq</span></li>
  <li><b>To design</b><span>loyihalashtirmoq</span></li>
  <li><b>Wallet</b><span>hamyon</span></li>
</ul>

<div class="pe-recap">
  <p class="pe-recap__t">🎯 Remember this</p>
  <ul>
    <li><b>be + V3</b> — and <b>be</b> carries the tense, not the V3.</li>
    <li>Present: <b>am/is/are</b> + V3 · Past: <b>was/were</b> + V3.</li>
    <li>Use it when the doer is unknown, obvious, unimportant, or in formal writing.</li>
    <li>The object of the active sentence becomes the <b>subject</b> of the passive one.</li>
    <li>Add <b>by</b> only when the doer is worth mentioning.</li>
  </ul>
</div>
""",
    },
]

# The colour legend is written once and dropped into the lessons that use colour-coded
# examples, so the palette explanation never drifts between lessons.
for _t in TUTORIALS:
    _t["content"] = _t["content"].replace("LEGEND_HERE", LEGEND).strip()
