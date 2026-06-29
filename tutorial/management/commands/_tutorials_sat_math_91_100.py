# SAT Math tutorials 91–100 (Part 2 finale: the rest of Math Tactics & Test Strategy)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_91_100.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 91 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-91: Translating English into Math (Key Terms Dictionary)",
        "category": "math",
        "summary": "Turn word problems into equations by translating key English phrases into math symbols.",
        "content": """
<h2>SAT-91: Translating English into Math (Key Terms Dictionary)</h2>
<p><strong>Description:</strong> Word problems are just equations hidden inside sentences. Once you know which English
words become which math symbols, you can <mark>translate</mark> almost any sentence into an equation you can solve. This
lesson is your dictionary.</p>

<h3>The key terms dictionary</h3>
<ul>
  <li>"is", "was", "equals", "will be" → <strong>=</strong></li>
  <li>"sum", "more than", "increased by", "total" → <strong>+</strong></li>
  <li>"difference", "less than", "decreased by", "fewer" → <strong>−</strong></li>
  <li>"product", "of", "times", "twice", "triple" → <strong>×</strong></li>
  <li>"quotient", "per", "ratio", "divided by" → <strong>÷</strong></li>
  <li>"a number", "what", "some value" → a <strong>variable</strong> (x)</li>
</ul>
<p><em>(Oʻzbekcha: "is" = teng, "of" = koʻpaytirish, "per" = boʻlish — soʻzlarni belgilarga aylantiramiz.)</em></p>

<h3>The two famous order traps</h3>
<p>"<strong>Less than</strong>" and "<strong>more than</strong>" flip the order: "5 less than x" is <strong>x − 5</strong>,
not 5 − x. And "the quotient of a and b" is a ÷ b, in that order. Read carefully.
<em>(Oʻzbekcha: "less than" tartibni teskari qiladi: "x dan 5 kam" = x − 5.)</em></p>

<h3>Worked Example 1 — a basic sentence</h3>
<p>"Three more than twice a number is 11." Translate and solve.</p>
<ul>
  <li>Twice a number = 2x; three more = 2x + 3; "is 11" = = 11.</li>
  <li>2x + 3 = 11 → 2x = 8 → <strong>x = 4</strong>.</li>
</ul>

<h3>Worked Example 2 — the "less than" trap</h3>
<p>"Seven less than a number equals 12." Translate and solve.</p>
<ul>
  <li>"Seven less than a number" = x − 7 (not 7 − x); "equals 12" = = 12.</li>
  <li>x − 7 = 12 → <strong>x = 19</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: "seven less than" = x − 7, tartibga eʼtibor bering.)</em></p>

<h3>Worked Example 3 — "of" means multiply</h3>
<p>"Half of a number, increased by 4, is 9." Translate and solve.</p>
<ul>
  <li>Half of a number = x/2; increased by 4 = + 4; is 9 = = 9.</li>
  <li>x/2 + 4 = 9 → x/2 = 5 → <strong>x = 10</strong>.</li>
</ul>

<h3>Worked Example 4 — two quantities</h3>
<p>"A pen costs 3 dollars more than a pencil. Together they cost 9 dollars." Find the pencil's price.</p>
<ul>
  <li>Let pencil = p. Pen = p + 3. Together: p + (p + 3) = 9.</li>
  <li>2p + 3 = 9 → 2p = 6 → <strong>p = 3</strong> (pencil $3, pen $6).</li>
</ul>
<blockquote>Strategy: translate the sentence piece by piece, left to right, replacing each phrase with its symbol.
<em>(Oʻzbekcha: gapni qism-qismga boʻlib, har birini belgiga aylantiring.)</em></blockquote>

<h3>The two phrases that flip order — in detail</h3>
<p>It's worth slowing down on the order-flippers because they cause more errors than any other translation. "5 less than x"
means you start with x and take 5 away: x − 5. "5 fewer than x" works the same way. The same logic applies to subtraction
words generally — the thing being subtracted comes <em>after</em> the phrase. Compare "the difference of x and 5" (x − 5) with
"5 less than x" (also x − 5) — both land in the same order, but the wording feels reversed, which is exactly the trap.
<em>(Oʻzbekcha: "less than" va "fewer than" tartibni teskari qiladi — ayiriladigan son keyin keladi.)</em></p>

<h3>Naming the unknown clearly</h3>
<p>Always write "let x = …" in words before translating, so you don't lose track of what the variable stands for. In a problem
about ages, "let x = Ben's age in years" is far safer than a bare x, especially when the question later asks for a different
quantity (like Anna's age). Clear labels turn multi-step word problems into routine algebra.
<em>(Oʻzbekcha: tarjimadan oldin "x = ..." deb soʻz bilan yozing — oʻzgaruvchi nimani bildirishini unutmaysiz.)</em></p>

<h3>Practice 1</h3>
<p>"Five more than three times a number is 20." Find the number.</p>
<details>
  <summary>Show answer</summary>
  <p>3x + 5 = 20 → 3x = 15 → <strong>x = 5</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>"Four less than half of a number is 6." Find the number.</p>
<details>
  <summary>Show answer</summary>
  <p>x/2 − 4 = 6 → x/2 = 10 → <strong>x = 20</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Translate</strong> — tarjima qilish (oʻgirish)</li>
  <li><strong>Sum</strong> — yigʻindi</li>
  <li><strong>Difference</strong> — ayirma</li>
  <li><strong>Product</strong> — koʻpaytma</li>
  <li><strong>Quotient</strong> — boʻlinma</li>
  <li><strong>Less than / More than</strong> — kam / koʻp</li>
  <li><strong>Of</strong> (= multiply) — "ning" (koʻpaytirish)</li>
  <li><strong>Per</strong> — har biriga (boʻlish)</li>
  <li><strong>Variable</strong> — oʻzgaruvchi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>"Is" → =, "of" → ×, "per" → ÷, "more/less than" → +/−.</li>
  <li><mark>"Less than" flips the order</mark>: "5 less than x" = x − 5.</li>
  <li>Translate left to right, phrase by phrase, then solve the equation.</li>
</ul>
""".strip(),
    },

    # ── 92 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-92: Recognizing Structure (Treating a Group as One Variable)",
        "category": "math",
        "summary": "Spot a repeated expression and treat the whole group as a single variable to simplify hard problems.",
        "content": """
<h2>SAT-92: Recognizing Structure (Treating a Group as One Variable)</h2>
<p><strong>Description:</strong> Some problems look terrifying until you notice a <mark>repeated chunk</mark>. If the same
expression appears more than once, you can treat that whole group as a <strong>single variable</strong> and the problem
collapses into something simple. This is "seeing the structure."</p>

<h3>The core move</h3>
<p>If you see the same expression twice (say x + y, or √x, or x<sup>2</sup>), give it a temporary name like u. Solve for
u, then translate back. The SAT rewards students who manipulate the <em>whole structure</em> instead of expanding
everything. <em>(Oʻzbekcha: takrorlanayotgan ifodani bitta harf (u) deb belgilang, soʻng yeching va orqaga qaytaring.)</em></p>

<h3>Worked Example 1 — a repeated binomial</h3>
<p>If 3(x + y) = 21, what is x + y?</p>
<ul>
  <li>Don't distribute. Treat (x + y) as one block: 3·(block) = 21 → block = 7.</li>
  <li>So <strong>x + y = 7</strong> — no need to know x or y separately.</li>
</ul>

<h3>Worked Example 2 — substitution into structure</h3>
<p>If a + b = 5, what is 2(a + b) + 9?</p>
<ul>
  <li>Replace the whole (a + b) with 5: 2(5) + 9 = <strong>19</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: (a + b) butun bloki oʻrniga 5 ni qoʻyamiz.)</em></p>

<h3>Worked Example 3 — a hidden quadratic</h3>
<p>Solve (x + 1)<sup>2</sup> − 5(x + 1) + 6 = 0.</p>
<ul>
  <li>Let u = x + 1. Then u<sup>2</sup> − 5u + 6 = 0 → (u − 2)(u − 3) = 0 → u = 2 or u = 3.</li>
  <li>Translate back: x + 1 = 2 → x = 1; or x + 1 = 3 → x = 2. So <strong>x = 1 or 2</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: u = x + 1 deb olsak, oddiy kvadrat tenglama hosil boʻladi.)</em></p>

<h3>Worked Example 4 — recognizing a known form</h3>
<p>If x<sup>2</sup> − y<sup>2</sup> = 20 and x + y = 5, find x − y.</p>
<ul>
  <li>Structure: x<sup>2</sup> − y<sup>2</sup> = (x + y)(x − y) (difference of squares, SAT-31).</li>
  <li>So 20 = 5·(x − y) → <strong>x − y = 4</strong>, without solving for x and y individually.</li>
</ul>
<blockquote>Rule: before grinding through algebra, ask "does a chunk repeat, or is this a known form?" Structure beats
brute force. <em>(Oʻzbekcha: algebra bilan urinishdan oldin "takrorlanayotgan boʻlak bormi?" deb soʻrang.)</em></blockquote>

<h3>Why the SAT loves structure questions</h3>
<p>These problems test whether you understand that algebra is about <em>relationships</em>, not just isolated letters. A
student who panics will try to find x and y individually — often impossible from the given information — while a student who
sees the structure realizes the question never needed the individual values at all. That's why structure questions frequently
give you "not enough" information to solve for each variable separately: it's a deliberate signal that you're meant to work
with the whole group. When you can't isolate the variables, that's your cue to look for a repeated chunk or a known form.
<em>(Oʻzbekcha: alohida oʻzgaruvchini topib boʻlmasa — bu butun boʻlak bilan ishlash kerakligining belgisi.)</em></p>

<h3>Practice 1</h3>
<p>If 5(a − b) = 35, what is a − b?</p>
<details>
  <summary>Show answer</summary>
  <p>Treat (a − b) as one block: block = 35 ÷ 5 = <strong>7</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>If m + n = 8, what is 3(m + n) − 4?</p>
<details>
  <summary>Show answer</summary>
  <p>3(8) − 4 = 24 − 4 = <strong>20</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Structure</strong> — tuzilish</li>
  <li><strong>Repeated expression</strong> — takrorlangan ifoda</li>
  <li><strong>Substitution</strong> — oʻrniga qoʻyish</li>
  <li><strong>Block / Chunk</strong> — yaxlit boʻlak</li>
  <li><strong>Binomial</strong> — ikkihad</li>
  <li><strong>Difference of squares</strong> — kvadratlar ayirmasi</li>
  <li><strong>Distribute</strong> — qavsni ochish</li>
  <li><strong>Treat as one variable</strong> — bitta oʻzgaruvchidek qarash</li>
  <li><strong>Translate back</strong> — orqaga qaytarish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>If an expression repeats, <mark>name the whole group</mark> as one variable.</li>
  <li>Solve the simpler equation, then substitute back to the original variable.</li>
  <li>Watch for known forms like (x + y)(x − y) — structure beats brute force.</li>
</ul>
""".strip(),
    },

    # ── 93 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-93: The Extreme Plug-In Technique (0, 1, Negatives)",
        "category": "math",
        "summary": "Test strategic extreme values — 0, 1, and negatives — to eliminate answer choices fast.",
        "content": """
<h2>SAT-93: The Extreme Plug-In Technique (0, 1, Negatives)</h2>
<p><strong>Description:</strong> Plugging in (SAT-81) gets even more powerful when you choose <mark>extreme values</mark> on
purpose — 0, 1, and negatives. These special numbers behave in unusual ways and quickly expose which answer choices are
wrong, especially on "which expression is always true?" questions.</p>

<h3>Why extremes are powerful</h3>
<ul>
  <li><strong>0</strong> makes many terms vanish, simplifying instantly.</li>
  <li><strong>1</strong> is the multiplicative identity, so it isolates the structure.</li>
  <li><strong>Negatives</strong> reveal sign mistakes that positive numbers hide.</li>
</ul>
<p><em>(Oʻzbekcha: 0, 1 va manfiy sonlar koʻp hadlarni soddalashtiradi va ishora xatolarini ochib beradi.)</em></p>

<h3>The caution</h3>
<p>Use extremes for <em>eliminating</em>, but be aware: 0 and 1 can occasionally make two choices look equal. If that
happens, switch to a different extreme (like −2) to break the tie. <em>(Oʻzbekcha: 0 va 1 baʼzan ikki variantni teng koʻrsatadi — bunday holatda −2 kabi boshqa qiymatni sinang.)</em></p>

<h3>Worked Example 1 — eliminate with 0</h3>
<p>Which equals 0 when x = 0? (A) x + 1 (B) x<sup>2</sup> (C) 2x − 3 (D) (x − 1).</p>
<ul>
  <li>Plug x = 0: (A) 1, (B) 0, (C) −3, (D) −1. Only (B) gives 0 → <strong>(B)</strong>.</li>
</ul>

<h3>Worked Example 2 — "always true" question</h3>
<p>Which is always equal to 2(x + 3)? (A) 2x + 3 (B) 2x + 6 (C) x + 6 (D) 2x + 5.</p>
<ul>
  <li>Test x = 0: target 2(3) = 6. Choices give (A) 3, (B) 6, (C) 6, (D) 5. (B) and (C) tie.</li>
  <li>Break the tie with x = 1: target 2(4) = 8. (B) 2+6 = 8 ✓; (C) 1+6 = 7 ✗. Answer <strong>(B)</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: ikki variant teng chiqsa, x = 1 bilan farqlang.)</em></p>

<h3>Worked Example 3 — catch a sign error with a negative</h3>
<p>Is |x| = x always true? Test x = −3.</p>
<ul>
  <li>|−3| = 3 but x = −3, so 3 ≠ −3. The statement is <strong>false</strong> — the negative exposed it instantly.</li>
  <li>(A positive test value like x = 3 would have wrongly suggested it's true.)</li>
</ul>

<h3>Worked Example 4 — fractions with 1</h3>
<p>Which equals 1 when x = 1? (A) x/2 (B) 2x (C) x<sup>2</sup> (D) x + 1.</p>
<ul>
  <li>Plug x = 1: (A) 0.5, (B) 2, (C) 1, (D) 2. Only (C) gives 1 → <strong>(C)</strong>.</li>
</ul>
<blockquote>Tip: when a question says "for all x" or "always," extreme plug-ins are the fastest way to kill wrong
choices. <em>(Oʻzbekcha: "barcha x uchun" deyilsa, ekstremal qiymatlar eng tez yoʻl.)</em></blockquote>

<h3>Which extreme to reach for first</h3>
<p>A quick decision guide: try <strong>0</strong> first on most "always equal" questions, since it instantly zeroes out many
terms and is the fastest to compute. If 0 leaves two choices tied, jump to <strong>1</strong>, which separates expressions that
differ by a coefficient. Save a <strong>negative</strong> for any question involving absolute value, squaring, or inequalities,
where sign behavior is the whole point. Cycling through 0, then 1, then a negative will resolve almost every elimination
question without algebra. <em>(Oʻzbekcha: avval 0 ni, keyin 1 ni, soʻng manfiyni sinang — shu tartibda koʻp savol hal boʻladi.)</em></p>

<h3>Practice 1</h3>
<p>Which expression equals 0 when x = 0? (A) x − 2 (B) 3x (C) x + 5 (D) x<sup>2</sup> + 1.</p>
<details>
  <summary>Show answer</summary>
  <p>Plug x = 0: (A) −2, (B) 0, (C) 5, (D) 1. Answer <strong>(B)</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Test whether (x + 2)<sup>2</sup> = x<sup>2</sup> + 4 for all x by trying x = 1.</p>
<details>
  <summary>Show answer</summary>
  <p>Left: (3)<sup>2</sup> = 9. Right: 1 + 4 = 5. 9 ≠ 5, so it is <strong>not</strong> always true (the middle term 4x is missing).</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Extreme value</strong> — ekstremal qiymat</li>
  <li><strong>Zero</strong> — nol</li>
  <li><strong>Identity (1)</strong> — birlik (1)</li>
  <li><strong>Negative</strong> — manfiy</li>
  <li><strong>Always true</strong> — har doim toʻgʻri</li>
  <li><strong>Eliminate</strong> — chiqarib tashlash</li>
  <li><strong>Absolute value</strong> — modul (absolyut qiymat)</li>
  <li><strong>Break the tie</strong> — tenglikni buzish</li>
  <li><strong>Sign error</strong> — ishora xatosi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Test <mark>0, 1, and negatives</mark> to expose wrong choices quickly.</li>
  <li>0 simplifies, 1 isolates structure, negatives catch sign errors.</li>
  <li>If two choices tie, switch to another extreme to break it.</li>
</ul>
""".strip(),
    },

    # ── 94 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-94: The Direct Translation Method for Word Problems",
        "category": "math",
        "summary": "Define variables, translate each sentence to an equation, then solve — a reliable system for word problems.",
        "content": """
<h2>SAT-94: The Direct Translation Method for Word Problems</h2>
<p><strong>Description:</strong> SAT-91 gave you the dictionary; this lesson gives you the <mark>system</mark>. The Direct
Translation Method is a repeatable four-step routine that turns any word problem into equations you can solve — even the
multi-sentence ones.</p>

<h3>The four steps</h3>
<ol>
  <li><strong>Define variables:</strong> write "let x = …" for each unknown.</li>
  <li><strong>Translate each sentence</strong> into an equation (using the SAT-91 dictionary).</li>
  <li><strong>Solve</strong> the equation(s).</li>
  <li><strong>Answer the question asked</strong> (check what it actually wants).</li>
</ol>
<p><em>(Oʻzbekcha: oʻzgaruvchini belgilang, har bir gapni tenglamaga aylantiring, yeching, soʻng aynan soʻralganini toping.)</em></p>

<h3>Worked Example 1 — one unknown</h3>
<p>"A number tripled, then decreased by 4, equals 17. Find the number."</p>
<ul>
  <li>Let x = the number. Translate: 3x − 4 = 17.</li>
  <li>Solve: 3x = 21 → <strong>x = 7</strong>.</li>
</ul>

<h3>Worked Example 2 — two unknowns, one relationship</h3>
<p>"Anna is 5 years older than Ben. The sum of their ages is 27. How old is Ben?"</p>
<ul>
  <li>Let Ben = b. Then Anna = b + 5. Translate the sum: b + (b + 5) = 27.</li>
  <li>2b + 5 = 27 → 2b = 22 → <strong>b = 11</strong>. (Ben is 11; the question asked for Ben, so stop here.)</li>
</ul>
<p><em>(Oʻzbekcha: soʻralgani Ben boʻlgani uchun b ni topib toʻxtaymiz.)</em></p>

<h3>Worked Example 3 — a rate problem</h3>
<p>"A taxi charges $3 plus $2 per mile. A ride cost $19. How many miles?"</p>
<ul>
  <li>Let m = miles. Translate: 3 + 2m = 19.</li>
  <li>2m = 16 → <strong>m = 8 miles</strong>.</li>
</ul>

<h3>Worked Example 4 — answer the right quantity</h3>
<p>"The width of a rectangle is x. The length is twice the width. The perimeter is 30. Find the length."</p>
<ul>
  <li>Width = x, length = 2x. Perimeter: 2(x) + 2(2x) = 30 → 6x = 30 → x = 5.</li>
  <li>But the question wants the <strong>length</strong> = 2x = <strong>10</strong> (don't stop at x = 5 — that's the trap).</li>
</ul>
<blockquote>Rule: the last step is the most missed one. After solving, re-read and make sure you reported the exact
quantity asked. <em>(Oʻzbekcha: oxirgi qadam — aynan soʻralgan miqdorni berish; uni unutmang.)</em></blockquote>

<h3>Choosing which unknown to call the variable</h3>
<p>When a problem has two related quantities, define your variable as the <em>smaller or simpler</em> one, then express the
other in terms of it. In the ages example, calling Ben's age b (and Anna's b + 5) is cleaner than the reverse, because it
avoids subtraction. A good choice of variable keeps the equation simple and reduces sign errors. If your first choice leads
to ugly fractions, it's fine to restart with the other quantity as the variable.
<em>(Oʻzbekcha: ikki bogʻliq miqdor boʻlsa, oddiyrogʻini oʻzgaruvchi deb oling — tenglama soddaroq boʻladi.)</em></p>

<h3>When to use two equations</h3>
<p>If a problem gives two genuinely separate facts about two unknowns, you can set up <strong>two equations</strong> and solve
the system (review the linear-systems lessons). But many SAT word problems only need <em>one</em> variable if you express the
second quantity in terms of the first — fewer variables means fewer chances to slip. Reach for a full system only when the two
quantities can't be linked in a single expression. <em>(Oʻzbekcha: ikkita alohida fakt berilsa, ikkita tenglama tuzing; aks holda bitta oʻzgaruvchi yetarli.)</em></p>

<h3>Practice 1</h3>
<p>"A number doubled, then increased by 6, equals 20. Find the number."</p>
<details>
  <summary>Show answer</summary>
  <p>2x + 6 = 20 → 2x = 14 → <strong>x = 7</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>"Maria has twice as many books as Sam. Together they have 18. How many does Sam have?"</p>
<details>
  <summary>Show answer</summary>
  <p>Let Sam = s, Maria = 2s. s + 2s = 18 → 3s = 18 → <strong>s = 6</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Define a variable</strong> — oʻzgaruvchini belgilash</li>
  <li><strong>Translate</strong> — tarjima qilish</li>
  <li><strong>Equation</strong> — tenglama</li>
  <li><strong>Unknown</strong> — nomaʼlum</li>
  <li><strong>Relationship</strong> — bogʻlanish (munosabat)</li>
  <li><strong>Rate</strong> — tezlik (narx sur'ati)</li>
  <li><strong>Perimeter</strong> — perimetr</li>
  <li><strong>Sum of ages</strong> — yoshlar yigʻindisi</li>
  <li><strong>Solve</strong> — yechish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Four steps: <mark>define → translate → solve → answer the question</mark>.</li>
  <li>Name each unknown clearly before translating.</li>
  <li>The most common error is stopping at x instead of the quantity actually asked.</li>
</ul>
""".strip(),
    },

    # ── 95 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-95: Using the Scratchpad Effectively",
        "category": "math",
        "summary": "Organize your scratch work so it speeds you up and prevents careless mistakes instead of causing them.",
        "content": """
<h2>SAT-95: Using the Scratchpad Effectively</h2>
<p><strong>Description:</strong> Messy scratch work creates careless errors; organized scratch work prevents them. Whether
you use the digital SAT's built-in notepad or scratch paper, a few habits turn your <mark>scratchpad</mark> into a tool
that earns points instead of losing them.</p>

<h3>Habit 1 — label each problem</h3>
<p>Write the question number next to your work so you never mix up calculations or lose track when you return to a marked
question. <em>(Oʻzbekcha: har bir ishni savol raqami bilan belgilang — chalkashmaslik uchun.)</em></p>

<h3>Habit 2 — write the equation before you compute</h3>
<p>Jotting the equation (or the formula) first forces a correct setup and gives you something to check against. Most
arithmetic errors come from doing steps in your head; writing them down makes them catchable.
<em>(Oʻzbekcha: hisoblashdan oldin tenglamani yozing — bu toʻgʻri tuzilishni taʼminlaydi.)</em></p>

<h3>Habit 3 — keep steps vertical and spaced</h3>
<p>Stacking one step under the next (instead of cramming sideways) makes it easy to spot where a sign or number went
wrong. Leave space; you're not saving paper. <em>(Oʻzbekcha: qadamlarni tik va keng joylashtiring — xatoni topish oson boʻladi.)</em></p>

<h3>Worked Example 1 — setup before numbers</h3>
<p>Problem: "20% of what number is 30?" Good scratch work writes the equation first.</p>
<ul>
  <li>Write: 0.20 × n = 30. Then solve: n = 30 ÷ 0.20 = <strong>150</strong>.</li>
  <li>Because the equation is on the page, you can re-check the setup if the answer seems off.</li>
</ul>

<h3>Worked Example 2 — sketch the figure</h3>
<p>A geometry problem describes a right triangle with legs 6 and 8 but shows no picture.</p>
<ul>
  <li>Quickly sketch the triangle and label 6 and 8 on the legs. Seeing it, you apply 6<sup>2</sup> + 8<sup>2</sup> = c<sup>2</sup> → c = <strong>10</strong>.</li>
  <li>A 10-second sketch prevents mislabeling which sides are the legs.</li>
</ul>
<p><em>(Oʻzbekcha: rasm berilmagan boʻlsa, oʻzingiz chizib, tomonlarni belgilang.)</em></p>

<h3>Worked Example 3 — track what you've eliminated</h3>
<p>On a multiple-choice question you rule out A and D.</p>
<ul>
  <li>Cross them off on the scratchpad. Now if you guess, you instantly see only B and C remain (a 50% shot — see SAT-88).</li>
</ul>

<h3>Worked Example 4 — record the units</h3>
<p>A problem gives a speed in km/h but asks for meters per second.</p>
<ul>
  <li>Write the units beside each number as you convert (km/h → m/s). Tracking units on paper stops the classic
  unit-trap (SAT-50, SAT-89) from sneaking in.</li>
</ul>
<blockquote>Tip: a tidy scratchpad isn't about neatness for its own sake — it's about making your own mistakes visible
before they cost points. <em>(Oʻzbekcha: tartibli qoralama — xatolarni ball yoʻqotishdan oldin koʻrinadigan qiladi.)</em></blockquote>

<h3>Digital vs paper — same principles</h3>
<p>On the digital SAT you get an on-screen notepad, and many test centers also allow scratch paper — use whichever you find
faster, but apply the same habits to both. Typing is slower for math symbols, so a quick handwritten sketch of a figure or a
stacked calculation often beats the notepad for geometry. Whatever you use, the goal is identical: externalize your thinking so
errors become visible. The worst scratchpad is the one in your head, where mistakes hide until they cost points.
<em>(Oʻzbekcha: raqamli yoki qogʻoz — qaysi tezroq boʻlsa, ishlating; muhimi fikrni tashqariga chiqarish.)</em></p>

<h3>Practice 1</h3>
<p>Why write the equation "0.25 × n = 15" before solving, instead of computing in your head?</p>
<details>
  <summary>Show answer</summary>
  <p>Writing it forces a correct setup and leaves a record to re-check; mental-only steps hide errors. (Here n = 15 ÷ 0.25 = <strong>60</strong>.)</p>
</details>

<h3>Practice 2</h3>
<p>You've eliminated two of four choices but must move on. What should your scratchpad show?</p>
<details>
  <summary>Show answer</summary>
  <p>The two eliminated choices <strong>crossed off</strong>, so a later guess is between the remaining two (50%) — not a blind 1-in-4.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Scratchpad</strong> — qoralama (chernovik)</li>
  <li><strong>Label</strong> — belgilash (nomlash)</li>
  <li><strong>Setup</strong> — tuzilish (tayyorlash)</li>
  <li><strong>Sketch</strong> — chizma (eskiz)</li>
  <li><strong>Step</strong> — qadam</li>
  <li><strong>Cross off</strong> — chizib tashlash</li>
  <li><strong>Units</strong> — oʻlchov birliklari</li>
  <li><strong>Organized</strong> — tartibli</li>
  <li><strong>Re-check</strong> — qayta tekshirish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Label each problem, and write the <mark>equation/formula before computing</mark>.</li>
  <li>Keep steps vertical and spaced so errors are easy to spot.</li>
  <li>Sketch missing figures, track units, and cross off eliminated choices.</li>
</ul>
""".strip(),
    },

    # ── 96 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-96: The \"Testing the Boundaries\" Tactic (Domain and Range)",
        "category": "math",
        "summary": "Check edge cases and boundary values to handle domain, range, and inequality questions confidently.",
        "content": """
<h2>SAT-96: The "Testing the Boundaries" Tactic (Domain and Range)</h2>
<p><strong>Description:</strong> Many SAT questions hinge on <mark>edge cases</mark> — the smallest or largest allowed value,
or the point where something is undefined. Deliberately <strong>testing the boundaries</strong> reveals the answer for
domain, range, and inequality problems.</p>

<h3>What "boundaries" means</h3>
<ul>
  <li>For a <strong>domain</strong>: the x-values where the function breaks (division by zero, square root of a negative).</li>
  <li>For a <strong>range</strong>: the smallest or largest output the function can reach.</li>
  <li>For an <strong>inequality</strong>: the endpoint value where it switches from true to false.</li>
</ul>
<p><em>(Oʻzbekcha: chegara — funksiya buziladigan yoki eng kichik/katta qiymatga yetadigan nuqta.)</em></p>

<h3>Worked Example 1 — domain boundary</h3>
<p>What value must be excluded from the domain of f(x) = 1/(x − 4)?</p>
<ul>
  <li>The boundary is where the denominator is 0: x − 4 = 0 → x = 4.</li>
  <li>So x = 4 is excluded; the domain is <strong>all real numbers except 4</strong>.</li>
</ul>

<h3>Worked Example 2 — range boundary</h3>
<p>What is the smallest value in the range of f(x) = x<sup>2</sup> + 3?</p>
<ul>
  <li>x<sup>2</sup> is smallest at x = 0 (its boundary), where x<sup>2</sup> = 0.</li>
  <li>So the minimum output is 0 + 3 = <strong>3</strong>; the range is y ≥ 3.</li>
</ul>
<p><em>(Oʻzbekcha: x² eng kichik qiymati x = 0 da, shuning uchun eng kichik chiqish 3.)</em></p>

<h3>Worked Example 3 — square-root domain</h3>
<p>What is the domain of f(x) = √(x − 2)?</p>
<ul>
  <li>The inside cannot be negative: x − 2 ≥ 0 → x ≥ 2. The boundary is x = 2 (allowed, since √0 = 0).</li>
  <li>Domain: <strong>x ≥ 2</strong>.</li>
</ul>

<h3>Worked Example 4 — inequality endpoint</h3>
<p>For which integers is 2x + 1 &lt; 9 true? Test the boundary.</p>
<ul>
  <li>Solve the boundary: 2x + 1 = 9 → x = 4. So the switch happens at x = 4.</li>
  <li>Since it's "&lt;", x = 4 is not included; integers <strong>x ≤ 3</strong> make it true (test x = 3: 7 &lt; 9 ✓; x = 4: 9 &lt; 9 ✗).</li>
</ul>
<blockquote>Tip: always test a value just inside and just outside the boundary to confirm which side is the solution.
<em>(Oʻzbekcha: chegaraning ikki tomonidagi qiymatlarni sinab, qaysi tomon yechim ekanini aniqlang.)</em></blockquote>

<h3>Open vs closed boundaries</h3>
<p>Whether the boundary value itself counts depends on the symbol. With ≤ or ≥ (and "at most"/"at least"), the endpoint
<strong>is</strong> included — that's a <em>closed</em> boundary. With &lt; or &gt; (and "less than"/"more than"), the endpoint
is <strong>excluded</strong> — an <em>open</em> boundary. Square-root domains are usually closed (√0 is fine), while
denominators are always open at the forbidden value (you can never divide by zero). Reading the exact symbol decides whether
your answer includes the edge. <em>(Oʻzbekcha: ≤/≥ — chegara kiritiladi (yopiq); &lt;/&gt; — kiritilmaydi (ochiq).)</em></p>

<h3>A quick way to find a range</h3>
<p>For range questions, think about the function's shape: a parabola opening up has a <em>minimum</em> at its vertex and rises
forever, so its range is "y ≥ (vertex y)." A parabola opening down has a <em>maximum</em>. A square root only outputs values
≥ 0 (shifted by any constant). Identifying the shape tells you which boundary — top or bottom — to compute, instead of testing
random points. <em>(Oʻzbekcha: funksiya shaklini aniqlang — parabola eng kichik yoki eng katta qiymatga ega, shu chegarani hisoblang.)</em></p>

<h3>Practice 1</h3>
<p>What value is excluded from the domain of f(x) = 5/(x + 2)?</p>
<details>
  <summary>Show answer</summary>
  <p>Denominator 0 at x + 2 = 0 → x = −2. Exclude <strong>x = −2</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>What is the minimum value of f(x) = (x − 1)<sup>2</sup> + 4?</p>
<details>
  <summary>Show answer</summary>
  <p>(x − 1)<sup>2</sup> is smallest (0) at x = 1, so the minimum is 0 + 4 = <strong>4</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Boundary</strong> — chegara</li>
  <li><strong>Edge case</strong> — chekka holat</li>
  <li><strong>Domain</strong> — aniqlanish sohasi</li>
  <li><strong>Range</strong> — qiymatlar sohasi</li>
  <li><strong>Excluded value</strong> — chiqarib tashlangan qiymat</li>
  <li><strong>Undefined</strong> — aniqlanmagan</li>
  <li><strong>Minimum / Maximum</strong> — eng kichik / eng katta</li>
  <li><strong>Endpoint</strong> — chetki nuqta</li>
  <li><strong>Inequality</strong> — tengsizlik</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>For domain: find where the function <mark>breaks</mark> (zero denominator, negative under a root).</li>
  <li>For range: the min/max usually sits at a boundary (like x = 0 for x<sup>2</sup>).</li>
  <li>For inequalities: solve the endpoint, then test just inside and outside it.</li>
</ul>
""".strip(),
    },

    # ── 97 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-97: Data Table Extraction",
        "category": "math",
        "summary": "Pull exactly the right numbers from dense tables, combining rows and columns without misreading.",
        "content": """
<h2>SAT-97: Data Table Extraction</h2>
<p><strong>Description:</strong> Dense tables hold more numbers than any one question needs. The skill is <mark>extracting
exactly the right values</mark> — the correct row and column — and combining them, without drowning in the rest. This
builds on SAT-53 with a focus on precision under time pressure.</p>

<h3>The extraction routine</h3>
<ol>
  <li>Read the question first and underline <strong>which</strong> value(s) it needs.</li>
  <li>Find the matching <strong>row</strong> and <strong>column</strong>; trace to where they meet.</li>
  <li>Combine only the needed cells (add a row/column, or take a difference).</li>
  <li>Re-check the units and any "Total" row before finalizing.</li>
</ol>
<p><em>(Oʻzbekcha: avval savolni oʻqing, kerakli qator va ustunni toping, faqat keraklilarini birlashtiring.)</em></p>

<h3>Our example table</h3>
<p>Students by grade and lunch choice:</p>
<ul>
  <li>Grade 9: Pizza 30, Salad 10 (row total 40).</li>
  <li>Grade 10: Pizza 25, Salad 35 (row total 60).</li>
  <li>Column totals: Pizza 55, Salad 45; grand total 100.</li>
</ul>

<h3>Worked Example 1 — single cell</h3>
<p>How many Grade 10 students chose Salad?</p>
<ul>
  <li>Grade 10 row × Salad column = <strong>35</strong>. One cell, nothing else needed.</li>
</ul>

<h3>Worked Example 2 — combine a column</h3>
<p>How many students total chose Pizza?</p>
<ul>
  <li>Add the Pizza column: 30 + 25 = <strong>55</strong> (matches the column total).</li>
</ul>
<p><em>(Oʻzbekcha: "jami pitsa" uchun pitsa ustunini qoʻshamiz.)</em></p>

<h3>Worked Example 3 — a percentage from the table</h3>
<p>What percent of Grade 9 students chose Pizza?</p>
<ul>
  <li>Grade 9 Pizza = 30; Grade 9 total = 40. Percent = 30/40 × 100% = <strong>75%</strong>.</li>
  <li>Note the denominator is the Grade 9 row total (40), not the grand total (100) — read the question's "of."</li>
</ul>

<h3>Worked Example 4 — a difference question</h3>
<p>How many more students chose Pizza than Salad overall?</p>
<ul>
  <li>Pizza total 55, Salad total 45. Difference = 55 − 45 = <strong>10</strong>.</li>
</ul>
<blockquote>Trap: using the grand total when the question restricts to one group (like "of Grade 9"). The word "of"
tells you the correct denominator (review SAT-59). <em>(Oʻzbekcha: "of" soʻzi toʻgʻri maxrajni koʻrsatadi — butun jamimi yoki bitta guruhmi.)</em></blockquote>

<h3>Why reading the question first saves time</h3>
<p>A dense table is designed to overwhelm — it deliberately includes numbers you don't need. If you study the whole table
before reading the question, you waste time absorbing irrelevant data and you're more likely to grab the wrong cell. By
reading the question <em>first</em>, you walk into the table already knowing exactly which row, column, or total you're
hunting for, and everything else becomes background noise you can ignore. This single ordering habit is the difference
between a slow, error-prone table question and a five-second lookup. <em>(Oʻzbekcha: avval savolni oʻqisangiz, jadvaldan aynan kerakli katakni qidirasiz va keraksiz sonlar chalgʻitmaydi.)</em></p>

<h3>Watch for footnotes and units in the header</h3>
<p>Tables often hide a crucial detail in the title or a footnote: "values in thousands," "percentages, not counts," or "data
for 2019 only." A number read correctly but interpreted in the wrong units is still wrong. Before you finalize, glance at the
table's header and any small print so you know what each number actually represents.
<em>(Oʻzbekcha: jadval sarlavhasi yoki izohida "minglarda", "foizlarda" kabi muhim maʼlumot boʻlishi mumkin — eʼtibor bering.)</em></p>

<h3>Practice 1</h3>
<p>How many Grade 9 students are there in total?</p>
<details>
  <summary>Show answer</summary>
  <p>Grade 9 row: 30 + 10 = <strong>40</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>What percent of all 100 students chose Salad?</p>
<details>
  <summary>Show answer</summary>
  <p>Salad total = 45 of 100 → <strong>45%</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Extract</strong> — ajratib olish</li>
  <li><strong>Row / Column</strong> — qator / ustun</li>
  <li><strong>Cell</strong> — katak</li>
  <li><strong>Total</strong> — jami</li>
  <li><strong>Grand total</strong> — umumiy jami</li>
  <li><strong>Difference</strong> — ayirma</li>
  <li><strong>Percent of</strong> — ... ning foizi</li>
  <li><strong>Denominator</strong> — maxraj</li>
  <li><strong>Units</strong> — oʻlchov birliklari</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Read the question first; underline exactly which values you need.</li>
  <li>Find the right <mark>row × column</mark>, then combine only those cells.</li>
  <li>The word "of" sets the denominator — group total vs grand total.</li>
</ul>
""".strip(),
    },

    # ── 98 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-98: The Formula Sheet Hack",
        "category": "math",
        "summary": "Use the provided reference formulas wisely — know what's given, what isn't, and how to apply it fast.",
        "content": """
<h2>SAT-98: The Formula Sheet Hack</h2>
<p><strong>Description:</strong> Every SAT math section gives you a <mark>reference sheet</mark> of formulas. Knowing exactly
what's on it (so you don't memorize those) — and, more importantly, what's <em>not</em> on it (so you do) — is a quiet but
real advantage.</p>

<h3>What the reference sheet gives you</h3>
<ul>
  <li>Area of a circle: A = πr<sup>2</sup>; circumference: C = 2πr.</li>
  <li>Area of a rectangle and triangle; the Pythagorean theorem.</li>
  <li>Volumes: rectangular box, cylinder, sphere, cone, pyramid.</li>
  <li>Special right triangles (the 30-60-90 and 45-45-90 ratios).</li>
  <li>The fact that a circle has 360°, and a triangle's angles sum to 180°.</li>
</ul>
<p><em>(Oʻzbekcha: maʼlumotnomada doira yuzasi, hajmlar, Pifagor teoremasi va maxsus uchburchaklar bor.)</em></p>

<h3>What is NOT on the sheet (you must know these)</h3>
<ul>
  <li>The <strong>slope formula</strong> and slope-intercept form y = mx + b.</li>
  <li>The <strong>quadratic formula</strong> and the discriminant.</li>
  <li>The <strong>distance</strong> and <strong>midpoint</strong> formulas.</li>
  <li>Percent change, exponential growth (a·b<sup>x</sup>), and SOH-CAH-TOA.</li>
</ul>
<p>Memorize <em>these</em>, because the sheet won't help you. <em>(Oʻzbekcha: nishab, kvadrat formula, masofa formulasi — bular varaqda yoʻq, ularni yodlang.)</em></p>

<h3>Worked Example 1 — use a given volume formula</h3>
<p>A cylinder has radius 3 and height 10. Find its volume (V = πr<sup>2</sup>h is on the sheet).</p>
<ul>
  <li>V = π(3)<sup>2</sup>(10) = π·9·10 = <strong>90π</strong>. You just look up the formula and plug in.</li>
</ul>

<h3>Worked Example 2 — recall a NOT-given formula</h3>
<p>Find the slope between (1, 2) and (5, 10). (The slope formula is NOT on the sheet.)</p>
<ul>
  <li>slope = (10 − 2)/(5 − 1) = 8/4 = <strong>2</strong>. You must know this from memory.</li>
</ul>
<p><em>(Oʻzbekcha: nishab formulasi varaqda yoʻq — yoddan bilishingiz kerak.)</em></p>

<h3>Worked Example 3 — combine sheet + memory</h3>
<p>A sphere has volume 36π. Find its radius (V = (4/3)πr<sup>3</sup> is on the sheet).</p>
<ul>
  <li>36π = (4/3)πr<sup>3</sup> → 36 = (4/3)r<sup>3</sup> → r<sup>3</sup> = 27 → r = <strong>3</strong>.</li>
</ul>

<h3>Worked Example 4 — don't waste time re-deriving</h3>
<p>You need the area of a circle with radius 5. Should you derive it?</p>
<ul>
  <li>No — A = πr<sup>2</sup> is on the sheet. Just use it: A = π(25) = <strong>25π</strong>. Save your time for the
  formulas you had to memorize.</li>
</ul>
<blockquote>Strategy: at the start, glance at the reference sheet so you know what's there. Spend memorization energy on
the formulas that are NOT provided. <em>(Oʻzbekcha: varaqda nima borligini bilib oling — yodlashni varaqda yoʻq formulalarga sarflang.)</em></blockquote>

<h3>The hidden cost of relying only on the sheet</h3>
<p>Even for provided formulas, the sheet helps only if you know <em>which</em> one applies and what each letter means. It
won't tell you that a "can" is a cylinder, or that you need the cone formula rather than the cylinder one. So the real skill is
matching the situation to the right formula and identifying r, h, and so on from the problem. Treat the sheet as a memory aid
for the equation's form, not a substitute for understanding the shape. <em>(Oʻzbekcha: varaq formulani beradi, lekin qaysi shaklga mosligini va harflar maʼnosini oʻzingiz aniqlashingiz kerak.)</em></p>

<h3>Practice 1</h3>
<p>A cylinder has radius 2 and height 7. Find its volume (use the sheet's V = πr<sup>2</sup>h).</p>
<details>
  <summary>Show answer</summary>
  <p>V = π(2)<sup>2</sup>(7) = π·4·7 = <strong>28π</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Which of these must you memorize because it's NOT on the reference sheet: area of a circle, or the quadratic formula?</p>
<details>
  <summary>Show answer</summary>
  <p>The <strong>quadratic formula</strong> — area of a circle is provided, but the quadratic formula is not.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Reference sheet</strong> — maʼlumotnoma varagʻi</li>
  <li><strong>Formula</strong> — formula</li>
  <li><strong>Provided / Given</strong> — berilgan</li>
  <li><strong>Memorize</strong> — yodlash</li>
  <li><strong>Volume</strong> — hajm</li>
  <li><strong>Slope</strong> — nishab</li>
  <li><strong>Quadratic formula</strong> — kvadrat tenglama formulasi</li>
  <li><strong>Distance formula</strong> — masofa formulasi</li>
  <li><strong>Cylinder / Sphere</strong> — silindr / shar</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>The sheet gives areas, volumes, the Pythagorean theorem, and special-triangle ratios — don't memorize those.</li>
  <li><mark>Memorize what's missing</mark>: slope, quadratic formula, distance/midpoint, SOH-CAH-TOA, percent change.</li>
  <li>Glance at the sheet early; use it instead of re-deriving provided formulas.</li>
</ul>
""".strip(),
    },

    # ── 99 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-99: Pacing for Module 2 (The Adaptive Test)",
        "category": "math",
        "summary": "Understand how the adaptive digital SAT works and how to pace Module 2 based on its difficulty.",
        "content": """
<h2>SAT-99: Pacing for Module 2 (The Adaptive Test)</h2>
<p><strong>Description:</strong> The digital SAT math section is <mark>adaptive</mark>: your performance on Module 1 decides
whether Module 2 is the easier or harder version. Understanding this changes how you pace each module — and protects your
score.</p>

<h3>How the adaptive format works</h3>
<p>You take Module 1 (a mix of easy, medium, and hard). Based on how well you do, Module 2 is delivered as either a
<strong>lower</strong> or <strong>higher</strong> difficulty version. The harder version unlocks access to the top of the
score range. <em>(Oʻzbekcha: 1-modul natijasi 2-modulning oson yoki qiyin boʻlishini belgilaydi.)</em></p>

<h3>Why Module 1 deserves steady, careful effort</h3>
<p>Because Module 1 sets your path, rushing it to "save time" can drop you into the easier Module 2 and cap your score.
Treat every Module 1 question with care — accuracy here matters more than raw speed.
<em>(Oʻzbekcha: 1-modulni shoshmasdan, aniqlik bilan ishlang — u keyingisini belgilaydi.)</em></p>

<h3>Pacing inside a module</h3>
<ul>
  <li>Do a <strong>first pass</strong> answering all the quick ones; mark the slow ones.</li>
  <li>Budget your time: roughly total minutes ÷ number of questions per question (review SAT-88).</li>
  <li>Leave a buffer at the end for the marked questions and a no-blanks check.</li>
</ul>

<h3>Worked Example 1 — pacing arithmetic</h3>
<p>A module has 22 questions in 35 minutes. What's a healthy first-pass pace?</p>
<ul>
  <li>35 ÷ 22 ≈ 1.6 min each. Aim faster on easy ones to bank time for hard ones.</li>
</ul>

<h3>Worked Example 2 — reading the difficulty signal</h3>
<p>Module 2 feels noticeably harder than Module 1 did. What does that likely mean?</p>
<ul>
  <li>You probably did well on Module 1 and unlocked the <strong>harder</strong> Module 2 — a good sign. Stay calm; these
  questions are worth more for your score ceiling.</li>
</ul>
<p><em>(Oʻzbekcha: 2-modul qiyinroq tuyulsa — bu yaxshi belgi, qiyin versiyani ochgansiz.)</em></p>

<h3>Worked Example 3 — don't panic on a hard run</h3>
<p>You hit three hard questions in a row in Module 2. What's the move?</p>
<ul>
  <li>Mark the ones that stall you, secure the ones you can, and keep moving — a hard stretch is expected in the harder
  module. Points still count equally (SAT-88).</li>
</ul>

<h3>Worked Example 4 — protecting the buffer</h3>
<p>You're halfway through Module 2's time but only a third through the questions. Adjust?</p>
<ul>
  <li>Speed up the first pass: answer quick ones, mark the rest, and guess on anything you can't reach — never leave
  blanks. Better to attempt all than to perfect a few.</li>
</ul>
<blockquote>Mindset: pace calmly in Module 1 to earn the harder Module 2; then in Module 2, protect easy points and
guess smartly on the rest. <em>(Oʻzbekcha: 1-modulda xotirjam ishlang, 2-modulda oson ballarni saqlang va aqlli taxmin qiling.)</em></blockquote>

<h3>Practice 1</h3>
<p>Why is it risky to rush carelessly through Module 1?</p>
<details>
  <summary>Show answer</summary>
  <p>Module 1 determines Module 2's difficulty. Careless errors can route you to the <strong>easier</strong> Module 2 and
  cap your top possible score.</p>
</details>

<h3>Practice 2</h3>
<p>A module gives 35 minutes for 22 questions. About how much time per question on average?</p>
<details>
  <summary>Show answer</summary>
  <p>35 ÷ 22 ≈ <strong>1.6 minutes</strong> each — go faster on easy ones to save time for hard ones.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Adaptive test</strong> — moslashuvchan test</li>
  <li><strong>Module</strong> — modul</li>
  <li><strong>Difficulty</strong> — qiyinlik darajasi</li>
  <li><strong>First pass</strong> — birinchi oʻtish</li>
  <li><strong>Pace</strong> — sur'at</li>
  <li><strong>Buffer (time)</strong> — zaxira vaqt</li>
  <li><strong>Score ceiling</strong> — ball shifti (eng yuqori chegara)</li>
  <li><strong>Accuracy</strong> — aniqlik</li>
  <li><strong>Mark and return</strong> — belgilab keyin qaytish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>The SAT is <mark>adaptive</mark>: Module 1 sets Module 2's difficulty.</li>
  <li>Work Module 1 calmly and accurately to unlock the higher score range.</li>
  <li>In any module: first pass for quick points, mark the slow ones, keep a buffer, never leave blanks.</li>
</ul>
""".strip(),
    },

    # ── 100 ───────────────────────────────────────────────────────────────────
    {
        "title": "SAT-100: The Final Review Protocol (30-Second Double-Check)",
        "category": "math",
        "summary": "Run a fast, systematic final check on every answer to catch the careless mistakes that cost easy points.",
        "content": """
<h2>SAT-100: The Final Review Protocol (30-Second Double-Check)</h2>
<p><strong>Description:</strong> The last lesson of the course is about keeping the points you already earned. Most lost
points on the SAT aren't from hard math — they're from <mark>careless slips</mark>. A quick, systematic
<strong>double-check</strong> catches them. Congratulations on reaching the finish line!</p>

<h3>The 30-second checklist (per flagged answer)</h3>
<ol>
  <li><strong>Did I answer the question asked?</strong> (x vs x + 2, radius vs diameter — see SAT-89, SAT-94.)</li>
  <li><strong>Right units and form?</strong> (hours vs minutes, fraction vs decimal — see SAT-50, SAT-90.)</li>
  <li><strong>Does the answer make sense?</strong> (a quick estimate sanity-check — see SAT-87.)</li>
  <li><strong>Any blanks?</strong> (Fill every one — see SAT-88.)</li>
</ol>
<p><em>(Oʻzbekcha: aynan soʻralganini, birlik/koʻrinishni, mantiqiyligini va boʻsh qolmaganini tekshiring.)</em></p>

<h3>How to spend your final minutes</h3>
<p>First, make sure <strong>nothing is blank</strong> — a guess beats a zero. Then revisit questions you <em>marked</em> as
uncertain, applying the checklist. Don't re-solve everything; trust your work and target the risky ones.
<em>(Oʻzbekcha: avval boʻsh savol yoʻqligini taʼminlang, soʻng belgilangan savollarni qayta koʻring.)</em></p>

<h3>Worked Example 1 — the "answered the question?" check</h3>
<p>You solved 2x = 14 and wrote 7, but the question asked for x + 1.</p>
<ul>
  <li>x = 7, but x + 1 = <strong>8</strong>. The 30-second check catches that you reported x, not x + 1.</li>
</ul>

<h3>Worked Example 2 — the units check</h3>
<p>You found a time of 90 minutes, but the answer choices are in hours.</p>
<ul>
  <li>90 minutes = 90 ÷ 60 = <strong>1.5 hours</strong>. The check converts before you submit.</li>
</ul>
<p><em>(Oʻzbekcha: javob soatlarda soʻralgan boʻlsa, daqiqani soatga aylantiring.)</em></p>

<h3>Worked Example 3 — the sanity-check</h3>
<p>A probability problem gives you an answer of 1.4. Reasonable?</p>
<ul>
  <li>No — a probability must be between 0 and 1, so 1.4 is impossible. The check flags it and you re-solve.</li>
</ul>

<h3>Worked Example 4 — the no-blanks sweep</h3>
<p>With one minute left you notice question 18 is blank.</p>
<ul>
  <li>Put your best guess (after eliminating any choices). A 1-in-4 (or better) shot beats a guaranteed zero — never leave it empty.</li>
</ul>
<blockquote>Final word: the double-check is the cheapest points on the test. Thirty seconds per flagged answer routinely
saves multiple points. You've learned the math and the tactics — now finish strong.
<em>(Oʻzbekcha: qayta tekshirish — eng arzon ballar; 30 soniya bir nechta ballni saqlaydi. Kuchli yakunlang!)</em></blockquote>

<h3>Don't over-review — trust your work</h3>
<p>Reviewing has a limit. If you re-check <em>every</em> answer, you'll run out of time and may "correct" right answers into
wrong ones out of second-guessing. The smart approach is targeted: only revisit questions you flagged as uncertain, plus any
where the checklist raises a flag. Answers you solved confidently the first time are usually correct — leave them alone. Spend
your scarce final minutes where doubt actually lives. <em>(Oʻzbekcha: hamma javobni qayta koʻrmang — faqat shubhali belgilanganlarini tekshiring, ishonchli javoblarga tegmang.)</em></p>

<h3>How this course fits together</h3>
<p>You've now covered the full arc: the core content (algebra, advanced math, data, geometry, trig) and the tactics that turn
that knowledge into points (plugging in, backsolving, Desmos, estimation, pacing, and this final check). On test day the
content gets you to an answer; the tactics protect it and save time; and this protocol catches the slips. Used together, they
are how a prepared student earns every point they're capable of. <em>(Oʻzbekcha: bu kurs mazmun va taktikani birlashtiradi — bilim javob beradi, taktika uni himoya qiladi, tekshiruv esa xatolarni ushlaydi.)</em></p>

<h3>Practice 1</h3>
<p>You solved 3x = 12 and wrote 4, but the question asked for 2x. What's the correct answer?</p>
<details>
  <summary>Show answer</summary>
  <p>x = 4, but 2x = <strong>8</strong>. The check catches that you stopped at x.</p>
</details>

<h3>Practice 2</h3>
<p>Your answer to "what fraction of students passed?" is 1.25. Why must you re-check?</p>
<details>
  <summary>Show answer</summary>
  <p>A fraction (or probability) of a whole can't exceed 1, so <strong>1.25 is impossible</strong> — re-solve; you likely
  inverted a ratio or mis-divided.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Double-check</strong> — qayta tekshirish</li>
  <li><strong>Review</strong> — koʻrib chiqish</li>
  <li><strong>Careless mistake</strong> — eʼtiborsizlik xatosi</li>
  <li><strong>Checklist</strong> — tekshiruv roʻyxati</li>
  <li><strong>Units / Form</strong> — birlik / koʻrinish</li>
  <li><strong>Sanity check</strong> — mantiqiy tekshiruv</li>
  <li><strong>Blank</strong> — boʻsh (javobsiz)</li>
  <li><strong>Flagged / Marked</strong> — belgilangan</li>
  <li><strong>Reasonable</strong> — mantiqiy</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Run a 30-second check on each flagged answer: <mark>question asked, units/form, sanity, no blanks</mark>.</li>
  <li>Spend final minutes filling blanks first, then reviewing marked questions.</li>
  <li>The double-check is the cheapest, most reliable way to protect your score. You made it — finish strong! 🎉</li>
</ul>
""".strip(),
    },
]
