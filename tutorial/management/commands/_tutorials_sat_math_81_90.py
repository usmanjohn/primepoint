# SAT Math tutorials 81–90 (Part 2: Math Tactics & Test Strategy)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_81_90.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 81 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-81: The \"Plugging In Numbers\" Tactic",
        "category": "math",
        "summary": "Turn abstract variable problems into easy arithmetic by choosing your own simple numbers.",
        "content": """
<h2>SAT-81: The "Plugging In Numbers" Tactic</h2>
<p><strong>Description:</strong> When a problem is full of variables and the answer choices are also in variables,
you can replace the letters with <mark>your own simple numbers</mark>, work out a real value, and then see which
choice matches. This turns scary algebra into easy arithmetic — and it is one of the most powerful SAT tactics.</p>

<h3>When to use it</h3>
<ul>
  <li>The question says "in terms of x" (or any variables) and the answer choices contain variables.</li>
  <li>The problem feels abstract and you're not sure how to start the algebra.</li>
  <li>There are percentages or fractions "of some number" with no actual number given.</li>
</ul>
<p><em>(Oʻzbekcha: javoblar ham harflar bilan berilgan boʻlsa, harflar oʻrniga oddiy sonlar qoʻyib hisoblang.)</em></p>

<h3>The steps</h3>
<ol>
  <li>Pick <strong>simple, easy numbers</strong> for the variables (avoid 0 and 1, which can hide differences).</li>
  <li>Work the problem with those numbers to get a single <mark>target number</mark>.</li>
  <li>Plug the same numbers into every answer choice.</li>
  <li>The choice that equals your target is the answer. (If two match, pick new numbers and re-test those two.)</li>
</ol>
<p><em>(Oʻzbekcha: 0 va 1 dan qoching — ular farqni yashirishi mumkin.)</em></p>

<h3>Worked Example 1 — answer in terms of x</h3>
<p>If a number is x, what is "3 more than twice the number"? Choices: (A) 2x + 3 (B) 3x + 2 (C) 2(x + 3) (D) 3x.</p>
<ul>
  <li>Let x = 4. "Twice the number" = 8; "3 more" = 11. Target = <strong>11</strong>.</li>
  <li>Test each with x = 4: (A) 2(4)+3 = 11 ✓; (B) 14; (C) 14; (D) 12. Only (A) hits 11 → <strong>(A)</strong>.</li>
</ul>

<h3>Worked Example 2 — percentages with no number</h3>
<p>A price is increased by 20%, then decreased by 50%. The final price is what percent of the original?</p>
<ul>
  <li>Let the original = 100 (the easiest number for percents).</li>
  <li>After +20%: 120. After −50%: 60. So the final is <strong>60%</strong> of the original.</li>
</ul>
<p><em>(Oʻzbekcha: foiz masalalarida boshlangʻich qiymatni 100 deb oling — eng qulayi.)</em></p>

<h3>Worked Example 3 — choosing safe numbers</h3>
<p>If y = 2x, which is larger, 3y or 5x? Try x = 3.</p>
<ul>
  <li>x = 3 → y = 6. Then 3y = 18 and 5x = 15. So <strong>3y is larger</strong>.</li>
  <li>(Here picking x = 0 would make both 0 and hide the answer — that's why we avoid 0.)</li>
</ul>
<blockquote>Tip: numbers like 2, 3, 4, 5, or 10 are usually best. For percent problems, 100 is king.
<em>(Oʻzbekcha: 2, 3, 4, 5 yoki 10 — eng qulay sonlar; foizlar uchun 100.)</em></blockquote>

<h3>Worked Example 4 — when a relationship is given</h3>
<p>If a + b = 10, what is the value of 2a + 2b + 5? Choices: (A) 15 (B) 20 (C) 25 (D) 30.</p>
<ul>
  <li>Pick numbers that fit the relationship: let a = 6 and b = 4 (they sum to 10).</li>
  <li>2(6) + 2(4) + 5 = 12 + 8 + 5 = 25 → <strong>(C)</strong>. (Any a, b summing to 10 gives the same result.)</li>
</ul>
<p><em>(Oʻzbekcha: shart berilgan boʻlsa (a + b = 10), shartga mos sonlarni tanlang.)</em></p>

<h3>The one safety check</h3>
<p>Plugging in can rarely produce a "false match" — a wrong choice that happens to equal your target for the specific
numbers you picked. That's why, if two choices both match, you re-test only those two with a <em>different</em> set of
numbers; the impostor will fail the second round. Choosing slightly unusual numbers (like 3 and 7 instead of 5 and 5)
also makes false matches less likely. <em>(Oʻzbekcha: ikki variant mos kelsa, ularni boshqa sonlar bilan qayta tekshiring — soxta moslik yoʻqoladi.)</em></p>

<h3>Practice 1</h3>
<p>The sum of three consecutive integers is, in terms of the smallest integer n, which expression?
(A) 3n (B) 3n + 3 (C) 3n + 1 (D) n + 3.</p>
<details>
  <summary>Show answer</summary>
  <p>Let n = 5: the integers are 5, 6, 7, sum = 18. Test: (B) 3(5)+3 = 18 ✓. Answer <strong>(B)</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>A shirt costs d dollars. It is marked up 25%. In terms of d, the new price is? (A) 1.25d (B) 0.25d (C) d + 25 (D) 1.025d.</p>
<details>
  <summary>Show answer</summary>
  <p>Let d = 40 → new price = 40 × 1.25 = 50. Test: (A) 1.25(40) = 50 ✓. Answer <strong>(A)</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Plug in</strong> — qiymat qoʻyish</li>
  <li><strong>Variable</strong> — oʻzgaruvchi</li>
  <li><strong>In terms of</strong> — ... orqali ifodalangan</li>
  <li><strong>Target number</strong> — maqsadli son</li>
  <li><strong>Answer choices</strong> — javob variantlari</li>
  <li><strong>Substitute</strong> — oʻrniga qoʻyish</li>
  <li><strong>Consecutive</strong> — ketma-ket</li>
  <li><strong>Simple number</strong> — oddiy son</li>
  <li><strong>Match</strong> — mos kelishi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Use when variables appear in both the question and the choices.</li>
  <li>Pick simple numbers (avoid 0 and 1), get a <mark>target number</mark>, test every choice.</li>
  <li>For percent problems, start the original at <strong>100</strong>.</li>
  <li>If two choices tie, re-test just those with new numbers.</li>
</ul>
""".strip(),
    },

    # ── 82 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-82: Backsolving (Working from the Options)",
        "category": "math",
        "summary": "Plug the answer choices back into the problem to find which one works — no algebra needed.",
        "content": """
<h2>SAT-82: Backsolving (Working from the Options)</h2>
<p><strong>Description:</strong> On a multiple-choice question, the correct number is already on the screen — it's one
of the four choices. <mark>Backsolving</mark> means testing those choices in the problem until one works. It's perfect
when solving forward looks messy.</p>

<h3>When to use it</h3>
<ul>
  <li>The answer choices are <strong>plain numbers</strong> (not variables).</li>
  <li>The question asks "what is x?" or "how many…?" and the algebra would be slow or error-prone.</li>
  <li>You're stuck on the setup but you <em>can</em> check whether a given value works.</li>
</ul>
<p><em>(Oʻzbekcha: javoblar oddiy sonlar boʻlsa, ularni masalaga qoʻyib tekshiring — toʻgʻri javobni topasiz.)</em></p>

<h3>The smart order: start in the middle</h3>
<p>Numerical choices are usually listed in order. Start with a <strong>middle value (B or C)</strong>. If it's too big,
you only need to test the smaller ones; if too small, test the larger ones. This often finds the answer in one or two
tries. <em>(Oʻzbekcha: oʻrtadagi variant (B yoki C) dan boshlang — bu sinovlar sonini kamaytiradi.)</em></p>

<h3>Worked Example 1 — a classic equation</h3>
<p>If 3x − 7 = 11, what is x? (A) 4 (B) 6 (C) 8 (D) 10.</p>
<ul>
  <li>Test (C) 8: 3(8) − 7 = 17 — too big. Try a smaller one.</li>
  <li>Test (B) 6: 3(6) − 7 = 11 ✓. Answer <strong>(B)</strong>.</li>
</ul>

<h3>Worked Example 2 — word problem</h3>
<p>A number plus its triple equals 24. What is the number? (A) 4 (B) 5 (C) 6 (D) 8.</p>
<ul>
  <li>Test (C) 6: 6 + 18 = 24 ✓. Answer <strong>(C)</strong> — no equation needed.</li>
</ul>
<p><em>(Oʻzbekcha: variantni masala shartiga qoʻyib, mos kelishini tekshiramiz.)</em></p>

<h3>Worked Example 3 — when forward algebra is ugly</h3>
<p>Which value of x satisfies √(x + 5) = x − 1? (A) 2 (B) 4 (C) 5 (D) 7.</p>
<ul>
  <li>Test (B) 4: √9 = 3 and 4 − 1 = 3 → 3 = 3 ✓. Answer <strong>(B)</strong>.</li>
  <li>This dodges squaring and the extraneous-solution check from SAT-39.</li>
</ul>
<blockquote>Tip: backsolving avoids algebra mistakes, because you only ever check arithmetic.
<em>(Oʻzbekcha: backsolving algebra xatolaridan saqlaydi — siz faqat arifmetikani tekshirasiz.)</em></blockquote>

<h3>Plugging-in vs backsolving — which one?</h3>
<p>Both use the answer choices, but for opposite situations: use <strong>plugging in</strong> (SAT-81) when the choices
contain <em>variables</em>; use <strong>backsolving</strong> when the choices are <em>plain numbers</em>.
<em>(Oʻzbekcha: javoblar harfli boʻlsa — plugging in; sonli boʻlsa — backsolving.)</em></p>

<h3>Worked Example 4 — read the wording carefully</h3>
<p>A test of backsolving's main risk: if the question asks for "x + 1" but the choices are values of that expression,
test each choice <em>as</em> x + 1, not as x. For 2(x) − 3 = 7 asking "what is x + 1?", with choices (A) 5 (B) 6 (C) 7:</p>
<ul>
  <li>Solve mentally or backsolve: 2x − 3 = 7 → x = 5, so x + 1 = 6.</li>
  <li>Answer <strong>(B) 6</strong> — don't grab 5, which is x itself (a classic trap, see SAT-89).</li>
</ul>
<p><em>(Oʻzbekcha: savol "x + 1" ni soʻrasa, variantlarni x emas, x + 1 sifatida tekshiring.)</em></p>

<h3>Why starting in the middle is mathematically smart</h3>
<p>With four ordered numeric choices, testing the middle one gives you the most information per test: a single check tells
you not just whether that choice is right, but whether the answer is bigger or smaller — instantly cutting the remaining
options roughly in half. This is the same "halving" logic computers use to search a sorted list, and it's why one or two
tests usually suffice. <em>(Oʻzbekcha: oʻrtadan boshlash har bir sinovda eng koʻp maʼlumot beradi — variantlar yarmiga kamayadi.)</em></p>

<h3>Practice 1</h3>
<p>If 2x + 5 = 17, what is x? (A) 4 (B) 6 (C) 7 (D) 8.</p>
<details>
  <summary>Show answer</summary>
  <p>Test (B) 6: 2(6) + 5 = 17 ✓. Answer <strong>(B)</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>The product of a number and 4 is 12 more than the number. What is the number? (A) 2 (B) 3 (C) 4 (D) 5.</p>
<details>
  <summary>Show answer</summary>
  <p>Test (C) 4: 4×4 = 16, and 4 + 12 = 16 ✓. Answer <strong>(C)</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Backsolving</strong> — javobdan teskari yechish</li>
  <li><strong>Answer choices</strong> — javob variantlari</li>
  <li><strong>Plug back in</strong> — qaytarib qoʻyish</li>
  <li><strong>Middle value</strong> — oʻrtadagi qiymat</li>
  <li><strong>Too big / too small</strong> — katta / kichik</li>
  <li><strong>Satisfy (an equation)</strong> — tenglamani qanoatlantirish</li>
  <li><strong>Check</strong> — tekshirish</li>
  <li><strong>Eliminate</strong> — chiqarib tashlash</li>
  <li><strong>Numerical</strong> — sonli</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Use when answer choices are <mark>plain numbers</mark>.</li>
  <li>Start with a middle choice (B or C) and use "too big / too small" to narrow down.</li>
  <li>You only ever check arithmetic, so it avoids algebra slips.</li>
  <li>Choices with variables → plug in instead (SAT-81).</li>
</ul>
""".strip(),
    },

    # ── 83 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-83: Mastering Desmos I — Graphing and Intersections",
        "category": "math",
        "summary": "Use the Desmos calculator to graph equations and read solutions as x-intercepts and intersection points.",
        "content": """
<h2>SAT-83: Mastering Desmos I — Graphing and Intersections</h2>
<p><strong>Description:</strong> The digital SAT gives you the <mark>Desmos graphing calculator</mark>. Many algebra
questions become one-click problems if you graph them. This lesson covers the core move: type equations, then read the
answer off the graph.</p>

<h3>The big idea: solutions are points on a graph</h3>
<ul>
  <li>The <strong>solution(s)</strong> of one equation = where the graph crosses the x-axis (the <mark>x-intercepts</mark>, also called roots or zeros).</li>
  <li>The <strong>solution of a system</strong> = where the two graphs <mark>intersect</mark>.</li>
</ul>
<p>So instead of solving by hand, you graph and click the special points; Desmos shows their coordinates.
<em>(Oʻzbekcha: tenglama yechimi — grafik x oʻqini kesgan nuqta; sistema yechimi — ikki grafik kesishgan nuqta.)</em></p>

<h3>How to do it</h3>
<ol>
  <li>Type each equation on its own line exactly as written (y = …, or the full equation).</li>
  <li>Click the curve where it crosses the x-axis, or where two curves meet; Desmos labels the point.</li>
  <li>Read the coordinate the question asks for (often just the x-value).</li>
</ol>
<p><em>(Oʻzbekcha: har bir tenglamani alohida qatorga yozing, soʻng kerakli nuqtani bosib koordinatani oʻqing.)</em></p>

<h3>Worked Example 1 — solve a quadratic</h3>
<p>Solve x<sup>2</sup> − 5x + 6 = 0 with Desmos.</p>
<ul>
  <li>Type y = x<sup>2</sup> − 5x + 6. The curve crosses the x-axis at x = 2 and x = 3.</li>
  <li>Solutions: <strong>x = 2 and x = 3</strong> — no factoring needed.</li>
</ul>

<h3>Worked Example 2 — a linear system</h3>
<p>Solve the system y = 2x + 1 and y = −x + 7.</p>
<ul>
  <li>Type both lines. They intersect at (2, 5).</li>
  <li>Solution: <strong>x = 2, y = 5</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: ikki chiziq (2, 5) nuqtada kesishadi — bu sistema yechimi.)</em></p>

<h3>Worked Example 3 — messy numbers</h3>
<p>How many real solutions does x<sup>2</sup> + 3x + 5 = 0 have?</p>
<ul>
  <li>Graph y = x<sup>2</sup> + 3x + 5. The curve never touches the x-axis.</li>
  <li>So there are <strong>0 real solutions</strong> (matches the negative discriminant from SAT-34).</li>
</ul>
<blockquote>Tip: enter equations as "y = …". If a question is given as "f(x) = …", graph "y = f(x)" or type the
expression directly. <em>(Oʻzbekcha: tenglamalarni "y = ..." koʻrinishida kiriting.)</em></blockquote>

<h3>Worked Example 4 — solve an equation by graphing both sides</h3>
<p>Solve 2x + 1 = x<sup>2</sup> − 2 using graphs.</p>
<ul>
  <li>Graph y = 2x + 1 and y = x<sup>2</sup> − 2 separately; their intersections give the solutions.</li>
  <li>They meet at x = −1 and x = 3, so the equation's solutions are <strong>x = −1 and x = 3</strong>.</li>
</ul>
<p>This "graph both sides" trick turns any equation into an intersection problem — very handy when one side is messy.
<em>(Oʻzbekcha: tenglamaning ikki tomonini alohida grafik qilib, kesishmalarni topamiz.)</em></p>

<h3>Common setup mistakes in Desmos</h3>
<p>A few errors waste time: forgetting to type the exponent with the caret (x^2, which Desmos renders as x²), writing
"2x" as "2 x" with a stray space, or leaving off "y =" so nothing graphs. Also remember to zoom out if a curve seems to
vanish — the interesting points may be off the default screen. A quick habit of checking that <em>something</em> actually
plotted prevents most of these. <em>(Oʻzbekcha: darajani ^ bilan yozing, "y =" ni unutmang, va grafik koʻrinmasa masshtabni kichraytiring.)</em></p>

<h3>Practice 1</h3>
<p>Use Desmos-style reasoning: the graph of y = x<sup>2</sup> − 9 crosses the x-axis where?</p>
<details>
  <summary>Show answer</summary>
  <p>At x<sup>2</sup> − 9 = 0 → x = −3 and x = 3. Those are the <strong>x-intercepts</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Lines y = 3x − 2 and y = x + 4 intersect at what point?</p>
<details>
  <summary>Show answer</summary>
  <p>Setting equal: 3x − 2 = x + 4 → 2x = 6 → x = 3, then y = 7. Intersection <strong>(3, 7)</strong> — exactly the point Desmos would show.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Graphing calculator</strong> — grafik kalkulyator</li>
  <li><strong>x-intercept</strong> — x oʻqini kesish nuqtasi</li>
  <li><strong>Root / Zero</strong> — ildiz / nol</li>
  <li><strong>Intersection</strong> — kesishish nuqtasi</li>
  <li><strong>System</strong> — sistema</li>
  <li><strong>Curve</strong> — egri chiziq</li>
  <li><strong>Coordinate</strong> — koordinata</li>
  <li><strong>Plot / Graph</strong> — chizish</li>
  <li><strong>Solution</strong> — yechim</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Solutions of one equation = <mark>x-intercepts</mark>; solution of a system = <mark>intersection point</mark>.</li>
  <li>Type each equation as y = …, then click the key points to read coordinates.</li>
  <li>Great for quadratics, systems, and "how many solutions" questions.</li>
</ul>
""".strip(),
    },

    # ── 84 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-84: Mastering Desmos II — Sliders for Unknown Constants",
        "category": "math",
        "summary": "Add a slider in Desmos to test unknown constants and instantly find the value that fits a condition.",
        "content": """
<h2>SAT-84: Mastering Desmos II — Sliders for Unknown Constants</h2>
<p><strong>Description:</strong> When a problem has an unknown constant (like k) and a condition (one solution, passes
through a point, etc.), Desmos lets you create a <mark>slider</mark> for that letter and drag it until the condition is
met. It turns "solve for k" into "watch the graph."</p>

<h3>What a slider is</h3>
<p>If you type an equation with a letter Desmos doesn't recognize as a variable (say k), it offers to <strong>add a
slider</strong>. The slider lets you change k smoothly and see the graph move in real time.
<em>(Oʻzbekcha: slayder — nomaʼlum doimiyni (masalan k) silliq oʻzgartirib, grafik qanday oʻzgarishini koʻrsatadi.)</em></p>

<h3>The method</h3>
<ol>
  <li>Type the equation using the unknown letter; tap "add slider" when prompted.</li>
  <li>Decide what the condition looks like on the graph (e.g. "touches the x-axis once" = one solution).</li>
  <li>Drag the slider until that picture appears; read the value.</li>
</ol>
<p><em>(Oʻzbekcha: shartni grafikda qanday koʻrinishini tasavvur qiling, soʻng slayderni shu holatga keltiring.)</em></p>

<h3>Worked Example 1 — pass through a point</h3>
<p>For what k does y = kx + 1 pass through (2, 7)?</p>
<ul>
  <li>Add a slider for k and drag until the line hits (2, 7). It lands at k = 3.</li>
  <li>Check: 3(2) + 1 = 7 ✓. So <strong>k = 3</strong>.</li>
</ul>

<h3>Worked Example 2 — exactly one solution</h3>
<p>For what positive k does x<sup>2</sup> + kx + 9 = 0 have exactly one solution?</p>
<ul>
  <li>Graph y = x<sup>2</sup> + kx + 9 with a slider. One solution means the curve just <em>touches</em> the x-axis.</li>
  <li>Slide k until it touches: that happens at k = 6. (Confirms the discriminant: k<sup>2</sup> − 36 = 0.)</li>
  <li>So <strong>k = 6</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: bitta yechim — parabola x oʻqiga tegib oʻtadi; slayderni shu holatga keltiramiz.)</em></p>

<h3>Worked Example 3 — match two graphs</h3>
<p>For what c do the lines y = 2x + c and y = −x + 9 intersect on the y-axis?</p>
<ul>
  <li>"On the y-axis" means at x = 0. The second line hits the y-axis at (0, 9).</li>
  <li>Slide c until y = 2x + c also passes (0, 9): that's c = 9. So <strong>c = 9</strong>.</li>
</ul>
<blockquote>Tip: sliders are fastest when the condition is visual — "tangent," "passes through," "same intercept."
<em>(Oʻzbekcha: shart koʻrinarli boʻlsa (urinma, nuqtadan oʻtadi), slayder eng tez yoʻl.)</em></blockquote>

<h3>Worked Example 4 — count solutions as k changes</h3>
<p>The equation x<sup>2</sup> − 4x + k = 0 can have 0, 1, or 2 solutions depending on k. Use a slider to explore.</p>
<ul>
  <li>Graph y = x<sup>2</sup> − 4x + k with a slider. As you raise k, the parabola lifts upward.</li>
  <li>It crosses the x-axis twice for small k, touches once at k = 4, and misses entirely for k &gt; 4.</li>
  <li>So the number of real solutions <strong>drops from 2 to 1 to 0</strong> as k passes 4 — you can literally watch it.</li>
</ul>
<p><em>(Oʻzbekcha: slayderni surganingizda parabola koʻtariladi va yechimlar soni 2 → 1 → 0 ga oʻzgaradi.)</em></p>

<h3>Set a sensible slider range</h3>
<p>By default a slider runs from −10 to 10 in small steps, which is fine for most SAT problems. If your target value seems
to sit at the very edge, widen the range by clicking the slider's endpoints and typing new limits. Narrowing the step size
also lets you land on exact values like 6 instead of 5.98. Tuning the slider takes seconds and makes the read-off precise.
<em>(Oʻzbekcha: slayder oraligʻini va qadamini sozlash aniq qiymatni topishga yordam beradi.)</em></p>

<h3>Practice 1</h3>
<p>For what k does the line y = kx pass through (4, 12)?</p>
<details>
  <summary>Show answer</summary>
  <p>Need 12 = k(4) → k = <strong>3</strong> (the slider would settle at 3).</p>
</details>

<h3>Practice 2</h3>
<p>For what value of b does y = x + b pass through the point (5, 2)?</p>
<details>
  <summary>Show answer</summary>
  <p>2 = 5 + b → b = <strong>−3</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Slider</strong> — slayder</li>
  <li><strong>Unknown constant</strong> — nomaʼlum doimiy</li>
  <li><strong>Condition</strong> — shart</li>
  <li><strong>Pass through</strong> — nuqtadan oʻtish</li>
  <li><strong>Tangent (touches once)</strong> — urinma (bir marta tegadi)</li>
  <li><strong>Drag</strong> — surish (tortish)</li>
  <li><strong>Real time</strong> — real vaqtda</li>
  <li><strong>y-axis</strong> — y oʻqi</li>
  <li><strong>Value</strong> — qiymat</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Type the unknown letter and <mark>add a slider</mark> to change it live.</li>
  <li>Translate the condition into a picture (touches once, passes through, same intercept).</li>
  <li>Drag until the picture appears, then read the value.</li>
</ul>
""".strip(),
    },

    # ── 85 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-85: Mastering Desmos III — Inequalities and Bounded Regions",
        "category": "math",
        "summary": "Graph systems of inequalities in Desmos to see the shaded solution region and test points.",
        "content": """
<h2>SAT-85: Mastering Desmos III — Inequalities and Bounded Regions</h2>
<p><strong>Description:</strong> Desmos shades inequalities automatically. For a <mark>system of inequalities</mark>, the
answer is the region where all the shadings <mark>overlap</mark>. This lesson shows how to read that region and test
whether a point is a solution.</p>

<h3>How Desmos shows inequalities</h3>
<p>Type an inequality (using &lt;, &gt;, ≤, ≥) and Desmos shades every point that makes it true. With several
inequalities, the <strong>overlap</strong> of all the shaded zones is the solution region — sometimes a closed
"bounded region." <em>(Oʻzbekcha: bir nechta tengsizlik boʻlsa, hamma soyalar kesishgan joy — yechim sohasi.)</em></p>

<h3>Reading the boundary lines</h3>
<ul>
  <li>≤ or ≥ → the boundary line is <strong>solid</strong> (points on the line count).</li>
  <li>&lt; or &gt; → the boundary line is <strong>dashed</strong> (points on the line do not count).</li>
</ul>
<p><em>(Oʻzbekcha: ≤ va ≥ — chegara chizigʻi qattiq; &lt; va &gt; — uzuq-uzuq.)</em></p>

<h3>The method</h3>
<ol>
  <li>Type each inequality on its own line.</li>
  <li>Find where all shadings overlap — that's the solution set.</li>
  <li>To test a point, plug it into each inequality, or see if it sits in the overlap.</li>
</ol>

<h3>Worked Example 1 — test a point</h3>
<p>Is (1, 1) a solution to the system y &gt; x and y &lt; 3?</p>
<ul>
  <li>y &gt; x: 1 &gt; 1 is false. The point fails the first inequality.</li>
  <li>So (1, 1) is <strong>not</strong> in the overlap → not a solution.</li>
</ul>

<h3>Worked Example 2 — find a point in the region</h3>
<p>Give a point that satisfies y ≥ 0, y ≤ x, and x ≤ 4.</p>
<ul>
  <li>Try (3, 1): y ≥ 0 ✓ (1 ≥ 0); y ≤ x ✓ (1 ≤ 3); x ≤ 4 ✓ (3 ≤ 4).</li>
  <li>So <strong>(3, 1)</strong> is in the bounded region.</li>
</ul>
<p><em>(Oʻzbekcha: nuqtani har bir tengsizlikka qoʻyib, hammasiga mos kelishini tekshiramiz.)</em></p>

<h3>Worked Example 3 — solid vs dashed</h3>
<p>For y ≤ 2x + 1, is the point (0, 1) on the boundary a solution?</p>
<ul>
  <li>(0, 1): 1 ≤ 2(0) + 1 → 1 ≤ 1 is true. Because the sign is ≤, the boundary line is solid.</li>
  <li>So (0, 1) <strong>is</strong> a solution (it lies on the included line).</li>
</ul>
<blockquote>Tip: the "maximum/minimum" of something in a bounded region usually occurs at a <strong>corner</strong> of the
region. Check the corners. <em>(Oʻzbekcha: chegaralangan sohada eng katta/kichik qiymat odatda burchaklarda boʻladi.)</em></blockquote>

<h3>Worked Example 4 — a real-world constraint problem</h3>
<p>A student has at most $12 to spend; pens cost $2 (x of them) and notebooks cost $3 (y of them), and they can't buy
negative amounts. Write the system and name one valid purchase.</p>
<ul>
  <li>Constraints: 2x + 3y ≤ 12, x ≥ 0, y ≥ 0. Graph these and the overlap is the bounded region of affordable combinations.</li>
  <li>One valid point: (3, 2) → cost 2(3) + 3(2) = 12 ≤ 12 ✓. So <strong>3 pens and 2 notebooks</strong> works.</li>
</ul>
<p><em>(Oʻzbekcha: real masalalarda tengsizliklar "cheklov" boʻladi; soyalar kesishgan joy — mumkin variantlar.)</em></p>

<h3>Why the answer is a whole region</h3>
<p>Unlike an equation, which usually has a few exact solutions, a system of inequalities is satisfied by <em>infinitely
many</em> points — the entire shaded overlap. That's why SAT questions ask things like "which point is a solution?" or
"what is the maximum of x + y in the region?" rather than "solve it." Keep that in mind: you're looking for points inside
a zone, not a single coordinate. <em>(Oʻzbekcha: tengsizliklar sistemasi cheksiz koʻp nuqtaga ega — butun soyalangan soha yechimdir.)</em></p>

<h3>Practice 1</h3>
<p>Is (2, 5) a solution to y &gt; 2x and y &lt; 10?</p>
<details>
  <summary>Show answer</summary>
  <p>y &gt; 2x: 5 &gt; 4 ✓. y &lt; 10: 5 &lt; 10 ✓. Both true → <strong>yes</strong>, it's a solution.</p>
</details>

<h3>Practice 2</h3>
<p>Does the point (4, 4) satisfy y ≤ x and y ≥ 1?</p>
<details>
  <summary>Show answer</summary>
  <p>y ≤ x: 4 ≤ 4 ✓ (solid boundary). y ≥ 1: 4 ≥ 1 ✓. Both hold → <strong>yes</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Inequality</strong> — tengsizlik</li>
  <li><strong>System of inequalities</strong> — tengsizliklar sistemasi</li>
  <li><strong>Shaded region</strong> — soyalangan soha</li>
  <li><strong>Overlap</strong> — kesishish (ustma-ust)</li>
  <li><strong>Bounded region</strong> — chegaralangan soha</li>
  <li><strong>Boundary line</strong> — chegara chizigʻi</li>
  <li><strong>Solid / Dashed</strong> — qattiq / uzuq-uzuq</li>
  <li><strong>Corner (vertex)</strong> — burchak</li>
  <li><strong>Satisfy</strong> — qanoatlantirish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>The solution of a system of inequalities is the <mark>overlap</mark> of all shaded regions.</li>
  <li>≤/≥ → solid (included) boundary; &lt;/&gt; → dashed (excluded).</li>
  <li>Test a point by checking it in every inequality.</li>
  <li>Max/min over a region usually sits at a <strong>corner</strong>.</li>
</ul>
""".strip(),
    },

    # ── 86 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-86: The \"Eyeballing\" Strategy for Geometry Diagrams",
        "category": "math",
        "summary": "Use the fact that SAT figures are drawn to scale to estimate lengths and angles and eliminate choices.",
        "content": """
<h2>SAT-86: The "Eyeballing" Strategy for Geometry Diagrams</h2>
<p><strong>Description:</strong> Unless a figure says "not drawn to scale," SAT geometry diagrams are drawn
<mark>roughly to scale</mark>. That means you can <em>estimate</em> a length or angle by eye and eliminate answers that
are clearly impossible. Eyeballing is a backup, not a substitute for math — but it saves many points.</p>

<h3>When it works (and when it doesn't)</h3>
<ul>
  <li><strong>Use it</strong> when the figure is shown and there's no "not to scale" warning.</li>
  <li><strong>Be careful</strong> when the label says "Note: figure not drawn to scale" — then ignore the look entirely.</li>
</ul>
<p><em>(Oʻzbekcha: "masshtabda chizilmagan" deyilmagan boʻlsa, rasm taxminan masshtabda — koʻz bilan baholash mumkin.)</em></p>

<h3>Two eyeball calibrations to memorize</h3>
<ul>
  <li>A <strong>right angle</strong> looks like a perfect corner (90°). Compare other angles to it: clearly smaller = acute, clearly wider = obtuse.</li>
  <li>Use a known side as a <strong>ruler</strong>: if one side is labeled 6 and another looks twice as long, it's about 12.</li>
</ul>
<p><em>(Oʻzbekcha: maʼlum tomonni "chizgʻich" sifatida ishlating; toʻgʻri burchakni esa etalon sifatida.)</em></p>

<h3>Worked Example 1 — estimate an angle</h3>
<p>An angle in a to-scale figure looks a bit less than a right angle. Choices: 30°, 50°, 85°, 140°. Which is reasonable?</p>
<ul>
  <li>"A bit less than 90°" rules out 30° (too small), and 140° (obtuse). 85° fits best; 50° is possible but looks too small.</li>
  <li>Eyeball answer: <strong>85°</strong> — and you'd confirm with the math.</li>
</ul>

<h3>Worked Example 2 — estimate a length</h3>
<p>In a to-scale triangle, one side is labeled 10 and the unknown side looks about half as long. Choices: 2, 5, 9, 14.</p>
<ul>
  <li>About half of 10 is ~5. That rules out 2 (too short), 9 and 14 (too long).</li>
  <li>Eyeball answer: <strong>5</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: nomaʼlum tomon maʼlum tomonning yarmiga oʻxshasa, taxminan 5.)</em></p>

<h3>Worked Example 3 — eliminate, don't finalize</h3>
<p>An angle clearly looks obtuse (wider than 90°). Choices: 45°, 60°, 88°, 120°. Narrow it down.</p>
<ul>
  <li>Obtuse means &gt; 90°, so only <strong>120°</strong> survives. The eyeball <em>eliminated</em> three answers instantly.</li>
</ul>
<blockquote>Rule: eyeballing is best for <strong>eliminating</strong> impossible choices, not for choosing between two close
ones. Use it to narrow, then compute. <em>(Oʻzbekcha: koʻz bilan baholash — notoʻgʻri variantlarni chiqarib tashlash uchun, ikki yaqin variantni tanlash uchun emas.)</em></blockquote>

<h3>Worked Example 4 — compare two sides without numbers</h3>
<p>In a to-scale triangle, the question asks which side is longest. You see one side clearly stretches across the figure
while the others are short.</p>
<ul>
  <li>The longest side sits opposite the largest angle — and you can confirm by eye which side simply looks longest.</li>
  <li>So you can answer "which is longest?" directly from the picture, then sanity-check with the angle sizes.</li>
</ul>
<p><em>(Oʻzbekcha: eng uzun tomon eng katta burchak qarshisida boʻladi — buni koʻz bilan ham tasdiqlash mumkin.)</em></p>

<h3>The danger zone: "not drawn to scale"</h3>
<p>When a figure carries the warning "not drawn to scale," the test-writers have <em>deliberately</em> drawn it
misleadingly — an angle that looks 90° might be far from it. In those cases, eyeballing is a trap, not a tool. Switch
entirely to the given measurements and the theorems from the geometry block (SAT-66 to SAT-72). Train yourself to glance
for that warning <em>before</em> trusting any picture. <em>(Oʻzbekcha: "masshtabda emas" deyilsa, rasmga ishonmang — faqat berilgan oʻlchovlardan foydalaning.)</em></p>

<h3>Practice 1</h3>
<p>A to-scale angle looks like a little more than a right angle. Which is most reasonable: 35°, 55°, 100°, 175°?</p>
<details>
  <summary>Show answer</summary>
  <p>Slightly more than 90° → <strong>100°</strong> (35° and 55° are acute; 175° is nearly a straight line).</p>
</details>

<h3>Practice 2</h3>
<p>A side looks roughly equal to a side labeled 8. Choices for its length: 3, 7, 15, 20. Best estimate?</p>
<details>
  <summary>Show answer</summary>
  <p>Roughly equal to 8 → <strong>7</strong> is closest (the others are far off).</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>To scale</strong> — masshtabda</li>
  <li><strong>Not to scale</strong> — masshtabda emas</li>
  <li><strong>Estimate</strong> — taxmin qilish</li>
  <li><strong>Eliminate</strong> — chiqarib tashlash</li>
  <li><strong>Right angle</strong> — toʻgʻri burchak</li>
  <li><strong>Acute / Obtuse</strong> — oʻtkir / oʻtmas</li>
  <li><strong>Diagram / Figure</strong> — chizma / shakl</li>
  <li><strong>Approximate</strong> — taxminiy</li>
  <li><strong>Reasonable</strong> — maʼqul (mantiqiy)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>SAT figures are <mark>to scale</mark> unless labeled otherwise — estimate angles and lengths by eye.</li>
  <li>Calibrate with a right angle and with any labeled side as a ruler.</li>
  <li>Use eyeballing to <strong>eliminate</strong> impossible choices, then confirm with math.</li>
</ul>
""".strip(),
    },

    # ── 87 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-87: The Art of Estimation",
        "category": "math",
        "summary": "Round numbers to estimate an answer quickly, then eliminate choices that are far from your estimate.",
        "content": """
<h2>SAT-87: The Art of Estimation</h2>
<p><strong>Description:</strong> You don't always need the exact answer to choose the right one. <mark>Estimation</mark> —
rounding numbers to friendly values and doing quick mental math — gets you close enough to eliminate wrong choices and
often pick the winner. It also catches silly mistakes on questions you do solve exactly.</p>

<h3>The core moves</h3>
<ul>
  <li><strong>Round</strong> ugly numbers to nearby friendly ones (98 → 100, 4.9 → 5, 1/3 → 0.33).</li>
  <li>Do the easy arithmetic with the rounded numbers.</li>
  <li>Pick the choice closest to your estimate; eliminate the far ones.</li>
</ul>
<p><em>(Oʻzbekcha: sonlarni qulay qiymatlarga yaxlitlang, soʻng oson hisoblab, eng yaqin variantni tanlang.)</em></p>

<h3>When estimation shines</h3>
<p>It's ideal when the answer choices are <strong>spread far apart</strong>, or when a question only asks "about how
many?" If two choices are very close together, estimate to narrow down, then compute exactly.
<em>(Oʻzbekcha: javoblar bir-biridan uzoq boʻlsa, baholash juda samarali.)</em></p>

<h3>Worked Example 1 — round and multiply</h3>
<p>Estimate 19.8 × 5.1. Choices: 25, 50, 100, 200.</p>
<ul>
  <li>Round: 20 × 5 = 100. The closest choice is <strong>100</strong>.</li>
</ul>

<h3>Worked Example 2 — percent estimate</h3>
<p>About what is 48% of 802? Choices: 200, 400, 600, 800.</p>
<ul>
  <li>48% ≈ 50% = half; 802 ≈ 800; half of 800 = 400. Answer ≈ <strong>400</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: 48% ni 50% (yarmi) deb, 802 ni 800 deb oling.)</em></p>

<h3>Worked Example 3 — sanity-check an exact answer</h3>
<p>You computed √215 and got 14.7. Is that reasonable?</p>
<ul>
  <li>14<sup>2</sup> = 196 and 15<sup>2</sup> = 225, so √215 must be between 14 and 15. 14.7 fits → <strong>reasonable</strong>.</li>
  <li>If you'd gotten 47 or 1.5, estimation would catch the error instantly.</li>
</ul>
<blockquote>Tip: even on "solve exactly" questions, a 5-second estimate before answering catches decimal-point and
sign mistakes. <em>(Oʻzbekcha: aniq yechgan javobni ham baholab tekshiring — xatolarni ushlaydi.)</em></blockquote>

<h3>Worked Example 4 — estimate a square root</h3>
<p>About how big is √50? Choices: 5, 7, 12, 25.</p>
<ul>
  <li>50 is just above 49 = 7<sup>2</sup>, so √50 is a little more than 7.</li>
  <li>Answer ≈ <strong>7</strong>. (The trap 25 is 50 ÷ 2, and 5 would be √25.)</li>
</ul>
<p><em>(Oʻzbekcha: 50 ≈ 49 = 7², shuning uchun √50 ≈ 7.)</em></p>

<h3>Estimating with fractions</h3>
<p>Fractions are easier to estimate if you turn them into rough decimals or compare them to ½. For instance, 5/9 is a bit
more than ½, and 2/7 is a bit less than ⅓. So "5/9 of 60" is a little more than 30, and you can eliminate any choice far
from that. Comparing a fraction to a familiar benchmark (½, ⅓, ¼) is often faster than exact division.
<em>(Oʻzbekcha: kasrlarni ½ yoki ⅓ kabi tanish qiymatlar bilan solishtirib baholang.)</em></p>

<h3>Why estimation also saves time</h3>
<p>Beyond catching errors, estimation can be the <em>whole</em> solution when choices are far apart — you never compute
the exact value at all. The skill is knowing when "close enough" is enough: if the four choices are 5, 50, 500, and 5000,
a rough estimate instantly picks the right power of ten. Save exact arithmetic for when two choices are genuinely close.
<em>(Oʻzbekcha: javoblar uzoq boʻlsa, baholashning oʻzi yetarli — aniq hisoblash shart emas.)</em></p>

<h3>Practice 1</h3>
<p>Estimate 31 × 9.8. Choices: 90, 150, 300, 600.</p>
<details>
  <summary>Show answer</summary>
  <p>≈ 30 × 10 = 300. Answer <strong>300</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>About what is 9.9% of 1,010? Choices: 1, 10, 100, 1000.</p>
<details>
  <summary>Show answer</summary>
  <p>≈ 10% of 1000 = 100. Answer <strong>100</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Estimate</strong> — taxminiy hisoblash</li>
  <li><strong>Round</strong> — yaxlitlash</li>
  <li><strong>Approximate</strong> — taxminiy</li>
  <li><strong>About / Roughly</strong> — taxminan</li>
  <li><strong>Sanity check</strong> — mantiqiy tekshiruv</li>
  <li><strong>Mental math</strong> — ogʻzaki hisob</li>
  <li><strong>Friendly number</strong> — qulay son</li>
  <li><strong>Eliminate</strong> — chiqarib tashlash</li>
  <li><strong>Reasonable</strong> — mantiqiy</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Round to <mark>friendly numbers</mark>, do quick mental math, pick the closest choice.</li>
  <li>Best when answer choices are far apart or the question says "about."</li>
  <li>Estimate even on exact problems to catch big mistakes.</li>
</ul>
""".strip(),
    },

    # ── 88 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-88: Strategic Guessing and Time Management",
        "category": "math",
        "summary": "Never leave a blank, spend time where it pays, and guess smartly when you must move on.",
        "content": """
<h2>SAT-88: Strategic Guessing and Time Management</h2>
<p><strong>Description:</strong> The SAT has <mark>no penalty for wrong answers</mark>, so you should answer every single
question. Combine that with smart pacing — spending your minutes where they earn the most points — and you protect your
score from the clock. </p>

<h3>Rule 1 — never leave a blank</h3>
<p>A blank is a guaranteed zero; a guess has a real chance. Before time runs out, make sure every question has an answer.
For grid-ins, write your best estimate. <em>(Oʻzbekcha: notoʻgʻri javob uchun jarima yoʻq — har bir savolga javob bering, hech qachon boʻsh qoldirmang.)</em></p>

<h3>Rule 2 — every question is worth the same</h3>
<p>A hard question and an easy question earn the same point. So don't burn five minutes on one monster while three easy
questions sit unanswered. <strong>Do the easy points first.</strong>
<em>(Oʻzbekcha: qiyin va oson savol bir xil ball beradi — avval oson ballarni yigʻing.)</em></p>

<h3>Rule 3 — the "skip and return" system</h3>
<ol>
  <li>First pass: answer everything you can do quickly; <strong>mark</strong> the slow ones.</li>
  <li>Second pass: return to the marked questions with your remaining time.</li>
  <li>Final 60 seconds: fill in a guess for anything still blank.</li>
</ol>
<p><em>(Oʻzbekcha: birinchi oʻtishda osonlarini yeching, qiyinlarini belgilang, soʻng qaytib keling.)</em></p>

<h3>Worked Example 1 — pacing math</h3>
<p>A module has 22 questions in 35 minutes. About how long per question on the first pass?</p>
<ul>
  <li>35 ÷ 22 ≈ 1.6 minutes each. So if a question eats 3+ minutes, mark it and move on.</li>
</ul>

<h3>Worked Example 2 — smart guessing after elimination</h3>
<p>You can't finish a problem but can eliminate two of four choices. Should you guess?</p>
<ul>
  <li>Yes. With two left, a guess is a 1-in-2 shot instead of 1-in-4. Eliminating first <strong>doubles</strong> your odds.</li>
</ul>
<p><em>(Oʻzbekcha: ikkita variantni chiqarib tashlasangiz, taxmin qilish ehtimoli 1/2 ga koʻtariladi.)</em></p>

<h3>Worked Example 3 — when to abandon</h3>
<p>You're 2.5 minutes into a question with no progress and 6 questions remain. What's the move?</p>
<ul>
  <li>Mark it, put a guess, and move on. Six unanswered easy points are worth far more than one stubborn hard one.</li>
</ul>
<blockquote>Tip: pick one "letter of the day" (say C) for pure blind guesses, so you never waste time deciding which
random letter. <em>(Oʻzbekcha: butunlay tasodifiy taxmin uchun bitta "kun harfi" tanlang — vaqt tejaysiz.)</em></blockquote>

<h3>Worked Example 4 — budgeting a review buffer</h3>
<p>You finish a 35-minute module's first pass in 28 minutes with 3 marked questions left. How should the last 7 minutes go?</p>
<ul>
  <li>Spend most of it on the 3 marked questions (about 2 minutes each = 6 minutes).</li>
  <li>Save the final ~1 minute to confirm no question is blank and to recheck any answer that felt rushed.</li>
</ul>
<p><em>(Oʻzbekcha: oxirgi daqiqalarni belgilangan savollarga va boʻsh qolmaganini tekshirishga ajrating.)</em></p>

<h3>The adaptive-test angle</h3>
<p>The digital SAT is <strong>adaptive</strong>: how well you do on the first module decides whether the second module is
the easier or harder version. That makes the first module especially worth your steady, careful effort — rushing it to
"save time" can lower the difficulty (and the score ceiling) of what comes next. Pace calmly, secure the points you know,
and don't sabotage module 1 by panicking. <em>(Oʻzbekcha: raqamli SAT moslashuvchan — birinchi modul keyingisining qiyinligini belgilaydi, shuning uchun uni shoshmasdan, puxta bajaring.)</em></p>

<h3>Practice 1</h3>
<p>You have 4 minutes left and 5 blank questions. What should you do first?</p>
<details>
  <summary>Show answer</summary>
  <p>Immediately put a guess on all 5 (no blanks!), then use the 4 minutes to actually solve as many as you can and fix
  the guesses. <strong>Never risk leaving a blank.</strong></p>
</details>

<h3>Practice 2</h3>
<p>On one question you've eliminated choices A and D. What are your odds if you guess between B and C, vs guessing among all four?</p>
<details>
  <summary>Show answer</summary>
  <p>Between B and C: <strong>1 in 2 (50%)</strong>. Among all four: 1 in 4 (25%). Eliminating doubled your chance.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Strategic guessing</strong> — strategik taxmin</li>
  <li><strong>No penalty</strong> — jarima yoʻq</li>
  <li><strong>Time management</strong> — vaqtni boshqarish</li>
  <li><strong>Pacing</strong> — sur'atni saqlash</li>
  <li><strong>Skip and return</strong> — tashlab keyin qaytish</li>
  <li><strong>Eliminate</strong> — chiqarib tashlash</li>
  <li><strong>Blank</strong> — boʻsh (javobsiz)</li>
  <li><strong>Odds</strong> — ehtimollik</li>
  <li><strong>Per question</strong> — har bir savolga</li>
</ul>

<h3>Summary</h3>
<ul>
  <li><mark>Never leave a blank</mark> — there's no penalty for wrong answers.</li>
  <li>Every question scores the same: <strong>grab easy points first</strong>, mark the slow ones.</li>
  <li>Eliminate before guessing to improve your odds.</li>
  <li>Watch your average time per question and abandon time-sinks.</li>
</ul>
""".strip(),
    },

    # ── 89 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-89: Avoiding the \"Trap Answers\"",
        "category": "math",
        "summary": "Recognize the predictable wrong answers test-writers plant and avoid the most common mistakes.",
        "content": """
<h2>SAT-89: Avoiding the "Trap Answers"</h2>
<p><strong>Description:</strong> Wrong answer choices aren't random — test-writers build <mark>trap answers</mark> from the
exact mistakes students tend to make. If you know the traps, you can spot and avoid them, and double-check the answers
that "feel" too easy.</p>

<h3>Common trap types</h3>
<ul>
  <li><strong>The "you stopped early" trap:</strong> the value of x when the question wanted x + 2, or the radius when it
  asked for the diameter.</li>
  <li><strong>The sign trap:</strong> the right number with the wrong sign (5 instead of −5).</li>
  <li><strong>The "wrong operation" trap:</strong> the result of adding when you should multiply, or vice versa.</li>
  <li><strong>The "right number, wrong units" trap:</strong> minutes vs hours, or a percent vs a decimal.</li>
</ul>
<p><em>(Oʻzbekcha: notoʻgʻri javoblar tasodifiy emas — ular talabalarning tipik xatolaridan tuziladi.)</em></p>

<h3>The best defense: answer the actual question</h3>
<p>Underline exactly what is asked ("the value of x + 2", "the diameter", "in hours"). After solving, re-read that
underlined phrase and make sure your answer matches it. Most traps die right there.
<em>(Oʻzbekcha: aynan nima soʻralganini tagiga chizing va javobingiz shunga mos kelishini tekshiring.)</em></p>

<h3>Worked Example 1 — the "stopped early" trap</h3>
<p>If 2x = 10, what is x + 3? Choices: (A) 5 (B) 8 (C) 13 (D) 2.</p>
<ul>
  <li>x = 5 — but the question wants x + 3 = 8. The trap (A) 5 is the value of x.</li>
  <li>Answer: <strong>(B) 8</strong>. Choice (A) punishes stopping early.</li>
</ul>

<h3>Worked Example 2 — the units trap</h3>
<p>A car travels 90 km in 1.5 hours. What is its speed in km per hour? Choices: 45, 60, 90, 135.</p>
<ul>
  <li>Speed = 90 ÷ 1.5 = 60 km/h. The trap 90 is the distance; 135 is 90 × 1.5 (wrong operation).</li>
  <li>Answer: <strong>60</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: 90 — bu masofa, tezlik emas; birliklar tuzogʻiga tushmang.)</em></p>

<h3>Worked Example 3 — the sign trap</h3>
<p>Solve x − 7 = −2. Choices: (A) 5 (B) −5 (C) 9 (D) −9.</p>
<ul>
  <li>x = −2 + 7 = 5. The trap (B) −5 flips the sign; (C) 9 adds instead of solving correctly.</li>
  <li>Answer: <strong>(A) 5</strong>.</li>
</ul>
<blockquote>Rule: if an answer comes <em>too</em> fast and easily on a hard question, pause — easy-looking choices on hard
questions are often traps. <em>(Oʻzbekcha: qiyin savolda javob juda oson kelsa — ehtiyot boʻling, bu tuzoq boʻlishi mumkin.)</em></blockquote>

<h3>Worked Example 4 — the percent-vs-decimal trap</h3>
<p>A quantity grows from 40 to 50. "By what factor did it grow?" Choices: (A) 0.25 (B) 1.25 (C) 10 (D) 25.</p>
<ul>
  <li>The factor is 50 ÷ 40 = 1.25. The trap (A) 0.25 is the percent <em>increase</em> as a decimal, and (D) 25 is the
  percent number. The question asked for the <strong>factor</strong>, so it's <strong>(B) 1.25</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: "koeffitsiyent" 1.25, "foiz oshish" esa 25% — savol nimani soʻraganiga eʼtibor bering.)</em></p>

<h3>How distractors are engineered</h3>
<p>It helps to think like the test-writer. For almost every question, they ask: "What will a student who makes the most
likely mistake get?" — and they put <em>that</em> number in as a choice. So when your answer exactly matches a choice, it
isn't automatic proof you're right; it might be the planted mistake. The real confirmation is re-reading the question and
checking units, signs, and whether you finished the final step. <em>(Oʻzbekcha: har bir notoʻgʻri variant — eng ehtimolli xatoning natijasi; javobingiz variantga mos kelishi hali toʻgʻriligini bildirmaydi.)</em></p>

<h3>Practice 1</h3>
<p>If 3x = 12, what is x − 1? Choices: (A) 4 (B) 3 (C) 11 (D) 5.</p>
<details>
  <summary>Show answer</summary>
  <p>x = 4, but the question wants x − 1 = 3. Trap (A) is x itself. Answer <strong>(B) 3</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>A circle has radius 6. What is its diameter? Choices: (A) 3 (B) 6 (C) 12 (D) 36.</p>
<details>
  <summary>Show answer</summary>
  <p>Diameter = 2 × radius = 12. Trap (B) 6 is the radius; (D) 36 looks like an area-style number. Answer <strong>(C) 12</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Trap answer</strong> — tuzoq javob</li>
  <li><strong>Distractor</strong> — chalgʻituvchi variant</li>
  <li><strong>Stopped early</strong> — yarim yoʻlda toʻxtash</li>
  <li><strong>Sign error</strong> — ishora xatosi</li>
  <li><strong>Units</strong> — oʻlchov birliklari</li>
  <li><strong>Diameter / Radius</strong> — diametr / radius</li>
  <li><strong>Underline</strong> — tagiga chizish</li>
  <li><strong>Double-check</strong> — qayta tekshirish</li>
  <li><strong>Operation</strong> — amal</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Trap answers are built from common mistakes: stopping early, sign slips, wrong operation, wrong units.</li>
  <li><mark>Underline what's asked</mark> and re-read it after solving.</li>
  <li>On hard questions, be suspicious of answers that come too easily.</li>
</ul>
""".strip(),
    },

    # ── 90 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-90: The Grid-In Blueprint (Student-Produced Responses)",
        "category": "math",
        "summary": "Enter grid-in answers correctly — fractions, decimals, negatives — and avoid format mistakes that cost points.",
        "content": """
<h2>SAT-90: The Grid-In Blueprint (Student-Produced Responses)</h2>
<p><strong>Description:</strong> Some SAT math questions have no choices — you type your own answer. These
<mark>grid-ins</mark> (student-produced responses) have strict format rules, and a correct value entered the wrong way
still scores zero. This lesson is your formatting checklist.</p>

<h3>The core format rules</h3>
<ul>
  <li>Answers can be <strong>positive, negative, fractions, or decimals</strong>.</li>
  <li>A fraction like 3/8 can be entered as a fraction or as its decimal 0.375 — both are accepted.</li>
  <li>Do <strong>not</strong> enter mixed numbers (like 1½): write 3/2 or 1.5 instead, or it's misread.</li>
  <li>Never grid a comma, a percent sign, or a dollar sign — just the number.</li>
</ul>
<p><em>(Oʻzbekcha: javob musbat, manfiy, kasr yoki oʻnli boʻlishi mumkin; aralash sonlarni yozmang — 3/2 yoki 1.5 deb yozing.)</em></p>

<h3>Decimals: don't round too early</h3>
<p>If a decimal doesn't fit the boxes, fill <em>all</em> available boxes (truncate or round to fill them) rather than
rounding to one digit. For 0.6666…, enter .666 or .667 — not 0.6. Giving too few digits can be marked wrong.
<em>(Oʻzbekcha: oʻnli kasrni erta yaxlitlamang — barcha kataklarni toʻldiring.)</em></p>

<h3>Worked Example 1 — a fraction answer</h3>
<p>Your answer is 6/4. How should you grid it?</p>
<ul>
  <li>Simplify to 3/2, or enter the decimal 1.5. Both are accepted. Do <strong>not</strong> write "1 1/2".</li>
</ul>

<h3>Worked Example 2 — a repeating decimal</h3>
<p>Your answer is 2/3. How should you grid it?</p>
<ul>
  <li>Enter the fraction 2/3 (cleanest), or fill the decimal as .666 or .667 across all boxes — not .6 or .67.</li>
</ul>
<p><em>(Oʻzbekcha: 2/3 ni kasr holida yozish eng qulayi; oʻnli yozsangiz .666 yoki .667 deb barcha kataklarni toʻldiring.)</em></p>

<h3>Worked Example 3 — a negative answer</h3>
<p>Your answer is −5. Can you grid it?</p>
<ul>
  <li>Yes — the digital grid-in accepts a negative sign. Enter <strong>−5</strong> directly.</li>
  <li>(On older paper bubble grids negatives weren't allowed, but the digital SAT accepts them.)</li>
</ul>
<blockquote>Tip: if your answer is a percent like 25%, grid the number <strong>25</strong> (or 0.25 if the question asks
for a decimal) — never the % sign. Read what form the question wants.
<em>(Oʻzbekcha: foizni % belgisisiz yozing — 25 yoki 0.25, savolga qarab.)</em></blockquote>

<h3>Worked Example 4 — when many answers are accepted</h3>
<p>A question says "give one possible value of x where 2 &lt; x &lt; 5." What can you grid?</p>
<ul>
  <li>Any value strictly between 2 and 5 is correct: 3, 4, 3.5, 7/2 all score.</li>
  <li>Pick the simplest — grid <strong>3</strong> or <strong>4</strong> and move on. Don't overthink "open ended" grid-ins.</li>
</ul>
<p><em>(Oʻzbekcha: "bitta mumkin qiymat" soʻralsa, eng oddiy mosini yozing — masalan 3 yoki 4.)</em></p>

<h3>Check the boundaries on "open" answers</h3>
<p>For range questions, watch whether the endpoints are included. "2 &lt; x &lt; 5" excludes 2 and 5, so gridding 2 or 5
would be wrong; but "2 ≤ x ≤ 5" would allow them. A safe habit is to pick a value comfortably in the <em>middle</em> of
the range, so you never get burned by a strict-versus-inclusive boundary. <em>(Oʻzbekcha: oraliqning chekkalari kiritilganmi tekshiring; xavfsizlik uchun oʻrtadagi qiymatni tanlang.)</em></p>

<h3>One more habit: re-read the requested form</h3>
<p>Before you lock in a grid-in, glance back at the question's last line. It often specifies the form: "to the nearest
tenth," "as a fraction," "in dollars." Matching that form is part of the answer — a perfectly correct number in the wrong
form can still be marked wrong. Two seconds of checking protects every grid-in point you earned.
<em>(Oʻzbekcha: javobni kiritishdan oldin soʻralgan koʻrinishni (kasr, oʻnli, yaxlitlangan) qayta oʻqing.)</em></p>

<h3>Practice 1</h3>
<p>Your computed answer is the mixed number 2¾. How do you grid it?</p>
<details>
  <summary>Show answer</summary>
  <p>Convert it: 2¾ = 11/4 or 2.75. Grid <strong>11/4</strong> or <strong>2.75</strong> — never "2 3/4".</p>
</details>

<h3>Practice 2</h3>
<p>Your answer is 1/7 ≈ 0.142857… If you grid the decimal, what should you enter?</p>
<details>
  <summary>Show answer</summary>
  <p>Fill all boxes: <strong>.142</strong> (or .143). Better yet, just grid the fraction <strong>1/7</strong>. Don't enter .1 or .14.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Grid-in</strong> — javobni oʻzi yozish (grid-in)</li>
  <li><strong>Student-produced response</strong> — talaba yozadigan javob</li>
  <li><strong>Fraction</strong> — kasr</li>
  <li><strong>Decimal</strong> — oʻnli kasr</li>
  <li><strong>Mixed number</strong> — aralash son</li>
  <li><strong>Negative</strong> — manfiy</li>
  <li><strong>Round / Truncate</strong> — yaxlitlash / kesish</li>
  <li><strong>Simplify</strong> — soddalashtirish</li>
  <li><strong>Format</strong> — koʻrinish (format)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Grid-ins accept positives, negatives, fractions, and decimals — but <mark>no mixed numbers</mark>.</li>
  <li>Convert a mixed number to an improper fraction or decimal.</li>
  <li>Fill all decimal boxes; don't round too early.</li>
  <li>Enter only the number — no %, $, or commas.</li>
</ul>
""".strip(),
    },
]
