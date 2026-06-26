# SAT Math tutorials 37–41 (Block B: Advanced Math — Parabolas, Systems & Rational/Radical)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_37_41.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 37 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-37: Graphing Parabolas — Intercepts, Vertex, and Symmetry",
        "category": "math",
        "summary": "Graph any parabola fast by finding its intercepts, vertex, and axis of symmetry.",
        "content": """
<h2>SAT-37: Graphing Parabolas — Intercepts, Vertex, and Symmetry</h2>
<p><strong>Description:</strong> A quadratic always graphs as a U-shaped curve called a
<mark>parabola</mark>. If you can find a few special points — the intercepts and the vertex — you
can sketch it perfectly. The SAT tests these points constantly.</p>

<h3>The four things to find</h3>
<ul>
  <li><strong>y-intercept</strong>: set x = 0. For y = ax<sup>2</sup> + bx + c this is just <strong>c</strong>.</li>
  <li><strong>x-intercepts</strong> (the <mark>roots</mark>): set y = 0 and solve the quadratic (factor or formula).</li>
  <li><strong>Axis of symmetry</strong>: the vertical line <strong>x = −b/(2a)</strong>.</li>
  <li><strong>Vertex</strong>: sits on the axis of symmetry; its x is −b/(2a), then plug in for y.</li>
</ul>
<p><em>(Oʻzbekcha: parabolani chizish uchun toʻrt narsa kerak: y-kesishma, x-kesishmalar (ildizlar), simmetriya oʻqi va uch.)</em></p>

<h3>Why symmetry helps</h3>
<p>A parabola is a <mark>mirror image</mark> across its axis of symmetry. So the two x-intercepts are
always the <strong>same distance</strong> from the axis, and the vertex's x is exactly halfway between them.</p>
<blockquote>Shortcut: if the x-intercepts are p and q, the axis (and vertex x) is the average <strong>(p + q) / 2</strong>.
<em>(Oʻzbekcha: ikkita x-kesishma oʻrtasi — simmetriya oʻqi.)</em></blockquote>

<h3>Worked Example</h3>
<p>Graph y = x<sup>2</sup> − 4x + 3.</p>
<ul>
  <li>y-intercept: c = 3 → point <strong>(0, 3)</strong>.</li>
  <li>x-intercepts: x<sup>2</sup> − 4x + 3 = (x − 1)(x − 3) = 0 → x = 1 and x = 3 → points <strong>(1, 0)</strong> and <strong>(3, 0)</strong>.</li>
  <li>Axis of symmetry: x = −(−4)/(2·1) = <strong>2</strong> (also the average of 1 and 3).</li>
  <li>Vertex: x = 2 → y = 2<sup>2</sup> − 4(2) + 3 = −1 → vertex <strong>(2, −1)</strong>.</li>
</ul>
<p>Since a = 1 &gt; 0 the parabola opens up, so (2, −1) is the lowest point.
<em>(Oʻzbekcha: a &gt; 0 boʻlgani uchun parabola yuqoriga ochiladi, uch eng past nuqta boʻladi.)</em></p>

<h3>Practice</h3>
<p>Find the vertex and axis of symmetry of y = x<sup>2</sup> + 6x + 5.</p>
<details>
  <summary>Show answer</summary>
  <p>Axis: x = −6/(2·1) = −3. Vertex: y = (−3)<sup>2</sup> + 6(−3) + 5 = 9 − 18 + 5 = −4 → <strong>(−3, −4)</strong>.</p>
  <p>(Check: x-intercepts are (x + 1)(x + 5) = 0 → x = −1 and −5, whose average is −3. ✓)</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Parabola</strong> — parabola</li>
  <li><strong>Intercept</strong> — kesishma nuqta</li>
  <li><strong>x-intercept / Root</strong> — x-kesishma / ildiz</li>
  <li><strong>y-intercept</strong> — y-kesishma</li>
  <li><strong>Vertex</strong> — uch (choʻqqi)</li>
  <li><strong>Axis of symmetry</strong> — simmetriya oʻqi</li>
  <li><strong>Mirror image</strong> — koʻzgu aksi</li>
  <li><strong>Opens up / down</strong> — yuqoriga / pastga ochiladi</li>
  <li><strong>Average (midpoint)</strong> — oʻrtacha (oʻrta nuqta)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>y-intercept = c; x-intercepts come from solving y = 0.</li>
  <li>Axis of symmetry and vertex x are both <mark>−b/(2a)</mark>.</li>
  <li>The vertex x is the <strong>average</strong> of the two x-intercepts.</li>
  <li>a &gt; 0 opens up (vertex = minimum); a &lt; 0 opens down (vertex = maximum).</li>
</ul>
""".strip(),
    },

    # ── 38 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-38: Systems of Non-Linear Equations (Linear–Quadratic)",
        "category": "math",
        "summary": "Solve a line-and-parabola system by substitution, and use the discriminant to count intersections.",
        "content": """
<h2>SAT-38: Systems of Non-Linear Equations (Linear–Quadratic)</h2>
<p><strong>Description:</strong> Sometimes the SAT gives a line and a parabola together and asks
where they meet. The solutions are the <mark>intersection points</mark>. The reliable method is
<strong>substitution</strong>.</p>

<h3>The method (substitution)</h3>
<ol>
  <li>Solve the <strong>linear</strong> equation for y (or x).</li>
  <li>Substitute that into the <strong>quadratic</strong> equation.</li>
  <li>You now have one quadratic in a single variable — set it to 0 and solve.</li>
  <li>Plug each x back into the line to get its y.</li>
</ol>
<p><em>(Oʻzbekcha: chiziqli tenglamani y uchun yeching, soʻngra uni kvadrat tenglamaga qoʻying.)</em></p>

<h3>Worked Example</h3>
<p>Solve the system: y = x + 1 and y = x<sup>2</sup> − 1.</p>
<ul>
  <li>Substitute: x + 1 = x<sup>2</sup> − 1.</li>
  <li>Rearrange to 0: x<sup>2</sup> − x − 2 = 0 → (x − 2)(x + 1) = 0 → x = 2 or x = −1.</li>
  <li>Back into the line y = x + 1: x = 2 → y = 3; x = −1 → y = 0.</li>
  <li>Intersection points: <strong>(2, 3)</strong> and <strong>(−1, 0)</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: ikkita yechim — chiziq parabolani ikki nuqtada kesib oʻtadi.)</em></p>

<h3>How many intersections? (use the discriminant)</h3>
<p>After substituting you get a quadratic. Its <mark>discriminant</mark> (b<sup>2</sup> − 4ac, from SAT-34) tells you how many times the graphs meet:</p>
<ul>
  <li>discriminant &gt; 0 → <strong>two</strong> intersection points,</li>
  <li>discriminant = 0 → <strong>one</strong> point (the line is tangent / just touches),</li>
  <li>discriminant &lt; 0 → <strong>no</strong> intersection (they never meet).</li>
</ul>
<blockquote>Tip: "for what value of k is the line tangent to the parabola?" means set the
discriminant equal to 0. <em>(Oʻzbekcha: "urinma" deganda diskriminant = 0 qilinadi.)</em></blockquote>

<h3>Practice</h3>
<p>How many times does y = 2x − 3 meet y = x<sup>2</sup>?</p>
<details>
  <summary>Show answer</summary>
  <p>x<sup>2</sup> = 2x − 3 → x<sup>2</sup> − 2x + 3 = 0. Discriminant = (−2)<sup>2</sup> − 4(1)(3) = 4 − 12 = −8 &lt; 0.</p>
  <p>So they meet <strong>0 times</strong> (no real intersection).</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>System of equations</strong> — tenglamalar sistemasi</li>
  <li><strong>Non-linear</strong> — chiziqli boʻlmagan</li>
  <li><strong>Substitution</strong> — oʻrniga qoʻyish</li>
  <li><strong>Intersection point</strong> — kesishish nuqtasi</li>
  <li><strong>Linear equation</strong> — chiziqli tenglama</li>
  <li><strong>Quadratic equation</strong> — kvadrat tenglama</li>
  <li><strong>Discriminant</strong> — diskriminant</li>
  <li><strong>Tangent</strong> — urinma</li>
  <li><strong>Rearrange</strong> — qayta tartiblash</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Solve the line for y, <mark>substitute</mark> into the quadratic, solve the resulting quadratic.</li>
  <li>Each x-solution gives an intersection point (find y from the line).</li>
  <li>The discriminant counts intersections: positive → 2, zero → 1 (tangent), negative → 0.</li>
</ul>
""".strip(),
    },

    # ── 39 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-39: Radical Equations and Extraneous Solutions",
        "category": "math",
        "summary": "Solve square-root equations by isolating and squaring — then check for extraneous (fake) solutions.",
        "content": """
<h2>SAT-39: Radical Equations and Extraneous Solutions</h2>
<p><strong>Description:</strong> A <mark>radical equation</mark> has the variable under a square root,
like √(x + 2) = 3. The trick is to undo the root by squaring — but squaring can create fake
answers called <strong>extraneous solutions</strong>, so checking is required.</p>

<h3>The method</h3>
<ol>
  <li><strong>Isolate</strong> the radical on one side (get √… alone).</li>
  <li><strong>Square</strong> both sides to remove the root.</li>
  <li>Solve the equation that remains.</li>
  <li><mark>Check every answer</mark> in the original equation — discard any that don't work.</li>
</ol>
<p><em>(Oʻzbekcha: avval ildizni bir tomonda yolgʻiz qoldiring, keyin ikkala tomonni kvadratga koʻtaring.)</em></p>

<h3>Why checking matters</h3>
<p>Squaring turns both +n and −n into the same number, so it can introduce a solution the
original equation never had. A square root gives a non-negative result, so any answer that makes
the two sides have opposite signs is <strong>extraneous</strong>.</p>
<blockquote>Rule: never trust a radical-equation answer until you plug it back in.
<em>(Oʻzbekcha: kvadratga koʻtarish soxta yechim keltirib chiqarishi mumkin — shuning uchun har bir javobni tekshiring.)</em></blockquote>

<h3>Worked Example</h3>
<p>Solve √(x + 2) = x.</p>
<ul>
  <li>Radical is already isolated. Square both sides: x + 2 = x<sup>2</sup>.</li>
  <li>Rearrange: x<sup>2</sup> − x − 2 = 0 → (x − 2)(x + 1) = 0 → x = 2 or x = −1.</li>
  <li>Check x = 2: √4 = 2 ✓. Check x = −1: √1 = 1, but right side is −1 → 1 ≠ −1 ✗.</li>
  <li>So x = −1 is <strong>extraneous</strong>. The only solution is <strong>x = 2</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: x = −1 soxta yechim, chunki ildiz manfiy boʻla olmaydi.)</em></p>

<h3>Practice</h3>
<p>Solve √(2x + 3) = x.</p>
<details>
  <summary>Show answer</summary>
  <p>Square: 2x + 3 = x<sup>2</sup> → x<sup>2</sup> − 2x − 3 = 0 → (x − 3)(x + 1) = 0 → x = 3 or x = −1.</p>
  <p>Check: x = 3 → √9 = 3 ✓. x = −1 → √1 = 1 ≠ −1 ✗. So <strong>x = 3</strong> only.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Radical equation</strong> — ildizli tenglama</li>
  <li><strong>Square root</strong> — kvadrat ildiz</li>
  <li><strong>Radical sign (√)</strong> — ildiz belgisi</li>
  <li><strong>Isolate</strong> — yolgʻiz qoldirish (ajratish)</li>
  <li><strong>Square both sides</strong> — ikkala tomonni kvadratga koʻtarish</li>
  <li><strong>Extraneous solution</strong> — soxta (begona) yechim</li>
  <li><strong>Check / Verify</strong> — tekshirish</li>
  <li><strong>Non-negative</strong> — manfiy boʻlmagan</li>
  <li><strong>Rearrange</strong> — qayta tartiblash</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Isolate the radical, then <mark>square both sides</mark> to remove it.</li>
  <li>Solve the resulting equation (often a quadratic).</li>
  <li>Always <strong>check</strong> answers; throw out extraneous ones that fail the original.</li>
</ul>
""".strip(),
    },

    # ── 40 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-40: Rational Equations and Domain Restrictions",
        "category": "math",
        "summary": "Solve equations with variables in the denominator, and exclude values that make a denominator zero.",
        "content": """
<h2>SAT-40: Rational Equations and Domain Restrictions</h2>
<p><strong>Description:</strong> A <mark>rational equation</mark> has a variable in the denominator,
like 1/x + 1/2 = 3/x. To solve, you clear the fractions — but you must watch for values that make
a denominator zero, since those are forbidden (<strong>domain restrictions</strong>).</p>

<h3>The method</h3>
<ol>
  <li>Note the <mark>restricted values</mark>: any x that makes a denominator 0 is not allowed.</li>
  <li>Multiply every term by the <strong>LCD</strong> (least common denominator) to clear fractions.</li>
  <li>Solve the resulting equation.</li>
  <li>Reject any solution that equals a restricted value.</li>
</ol>
<p><em>(Oʻzbekcha: maxrajni 0 qiladigan x qiymatlari taqiqlangan — ularni javobdan chiqarib tashlang.)</em></p>

<h3>Why restrictions exist</h3>
<p>Division by zero is undefined, so x can never make any denominator 0. Even if your algebra
produces such a value, it is <strong>not</strong> a valid solution.</p>
<blockquote>Rule: list the forbidden x-values <em>before</em> you solve, then cross-check at the end.
<em>(Oʻzbekcha: 0 ga boʻlish aniqlanmagan, shuning uchun bunday qiymatlar yechim boʻla olmaydi.)</em></blockquote>

<h3>Worked Example</h3>
<p>Solve 1/x + 1/2 = 3/x.</p>
<ul>
  <li>Restriction: x ≠ 0 (denominator can't be zero).</li>
  <li>LCD = 2x. Multiply each term: 2x·(1/x) + 2x·(1/2) = 2x·(3/x) → 2 + x = 6.</li>
  <li>Solve: x = 4. Since 4 ≠ 0, it is allowed → <strong>x = 4</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: x = 4 ruxsat etilgan, chunki u maxrajni nolga aylantirmaydi.)</em></p>

<h3>Practice</h3>
<p>Solve (x)/(x − 2) = 4/(x − 2).</p>
<details>
  <summary>Show answer</summary>
  <p>Restriction: x ≠ 2. Multiply both sides by (x − 2): x = 4.</p>
  <p>x = 4 is allowed (4 ≠ 2), so <strong>x = 4</strong>. (If it had given x = 2, we'd reject it.)</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Rational equation</strong> — ratsional (kasrli) tenglama</li>
  <li><strong>Denominator</strong> — maxraj</li>
  <li><strong>Numerator</strong> — surat</li>
  <li><strong>Domain</strong> — aniqlanish sohasi</li>
  <li><strong>Restriction</strong> — cheklov (taqiq)</li>
  <li><strong>LCD (least common denominator)</strong> — eng kichik umumiy maxraj</li>
  <li><strong>Clear the fractions</strong> — kasrlardan qutulish</li>
  <li><strong>Undefined</strong> — aniqlanmagan</li>
  <li><strong>Reject a solution</strong> — yechimni rad etish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>List <mark>restricted values</mark> (denominator = 0) first — they can never be solutions.</li>
  <li>Multiply through by the <strong>LCD</strong> to clear fractions, then solve.</li>
  <li>Reject any answer that hits a restricted value.</li>
</ul>
""".strip(),
    },

    # ── 41 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-41: Simplifying Rational Expressions & Polynomial Division",
        "category": "math",
        "summary": "Simplify fractions of polynomials by factoring and cancelling, and divide polynomials by long division.",
        "content": """
<h2>SAT-41: Simplifying Rational Expressions &amp; Polynomial Division</h2>
<p><strong>Description:</strong> A <mark>rational expression</mark> is a fraction whose top and bottom
are polynomials. You simplify it the same way you simplify number fractions: <strong>factor, then
cancel</strong> common factors. When it won't cancel cleanly, use <strong>polynomial long division</strong>.</p>

<h3>Method 1 — Factor and cancel</h3>
<ol>
  <li>Factor the numerator and denominator fully (review SAT-31, SAT-32).</li>
  <li>Cancel any factor that appears on both top and bottom.</li>
  <li>Note the restricted values (where the original denominator was 0).</li>
</ol>
<p><em>(Oʻzbekcha: suratni va maxrajni koʻpaytuvchilarga ajrating, soʻng umumiy koʻpaytuvchilarni qisqartiring.)</em></p>

<h3>Worked Example (factor and cancel)</h3>
<p>Simplify (x<sup>2</sup> − 9) / (x<sup>2</sup> + 5x + 6).</p>
<ul>
  <li>Factor top: x<sup>2</sup> − 9 = (x − 3)(x + 3) (difference of squares).</li>
  <li>Factor bottom: x<sup>2</sup> + 5x + 6 = (x + 2)(x + 3).</li>
  <li>Cancel (x + 3): result = <strong>(x − 3) / (x + 2)</strong>, with x ≠ −2, −3.</li>
</ul>
<p><em>(Oʻzbekcha: faqat koʻpaytuvchilarni qisqartiring — hadlarni emas.)</em></p>

<h3>Method 2 — Polynomial long division</h3>
<p>When factoring/cancelling isn't possible, divide like you divide numbers.</p>
<p>Divide (x<sup>2</sup> + 5x + 6) ÷ (x + 2):</p>
<ul>
  <li>x<sup>2</sup> ÷ x = x. Multiply: x(x + 2) = x<sup>2</sup> + 2x. Subtract → 3x + 6.</li>
  <li>3x ÷ x = 3. Multiply: 3(x + 2) = 3x + 6. Subtract → 0.</li>
  <li>Quotient: <strong>x + 3</strong>, remainder 0.</li>
</ul>
<blockquote>Tip: a remainder of 0 means the divisor is a <mark>factor</mark> of the polynomial — this idea
leads into the Factor Theorem (SAT-42). <em>(Oʻzbekcha: qoldiq 0 boʻlsa, boʻluvchi — koʻpaytuvchi.)</em></blockquote>

<h3>Practice</h3>
<p>Simplify (x<sup>2</sup> − 4) / (x − 2).</p>
<details>
  <summary>Show answer</summary>
  <p>Top factors as (x − 2)(x + 2). Cancel (x − 2): result = <strong>x + 2</strong>, with x ≠ 2.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Rational expression</strong> — ratsional ifoda</li>
  <li><strong>Polynomial</strong> — koʻphad</li>
  <li><strong>Numerator</strong> — surat</li>
  <li><strong>Denominator</strong> — maxraj</li>
  <li><strong>Factor</strong> — koʻpaytuvchi / koʻpaytuvchilarga ajratish</li>
  <li><strong>Cancel</strong> — qisqartirish</li>
  <li><strong>Difference of squares</strong> — kvadratlar ayirmasi</li>
  <li><strong>Long division</strong> — burchak (uzun) boʻlish</li>
  <li><strong>Quotient</strong> — boʻlinma</li>
  <li><strong>Remainder</strong> — qoldiq</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Simplify a rational expression by <mark>factoring</mark> top and bottom, then cancelling common factors.</li>
  <li>Only cancel <strong>factors</strong>, never individual terms.</li>
  <li>When it won't cancel, use <strong>polynomial long division</strong> (quotient + remainder).</li>
  <li>A remainder of 0 means the divisor is a factor.</li>
</ul>
""".strip(),
    },
]
