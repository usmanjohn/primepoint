# SAT Math tutorials 32–36 (Block B: Advanced Math — Quadratics)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_32_36.py --author=prime

TUTORIALS = [
    # ── 32 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-32: Factoring Advanced Quadratics (ax² + bx + c)",
        "category": "math",
        "summary": "Factor quadratics where a ≠ 1 using the reliable AC (split-the-middle) method.",
        "content": """
<h2>SAT-32: Factoring Advanced Quadratics (ax² + bx + c)</h2>
<p><strong>Description:</strong> In SAT-31 you factored quadratics where the leading number was 1.
Now the front coefficient <em>a</em> is not 1 (for example 2x<sup>2</sup> + 7x + 3). This lesson
teaches the <mark>AC method</mark> — a step-by-step trick that always works.</p>

<h3>The AC Method (split the middle)</h3>
<p><em>(Oʻzbekcha: AC usuli — bosh koeffitsiyent 1 ga teng boʻlmagan kvadrat ifodalarni koʻpaytuvchilarga ajratishning ishonchli yoʻli.)</em></p>
<p>For a quadratic <strong>ax<sup>2</sup> + bx + c</strong>:</p>
<ol>
  <li>Multiply <strong>a × c</strong>.</li>
  <li>Find two numbers that <mark>multiply to a·c</mark> and <mark>add to b</mark>.</li>
  <li>Split the middle term bx into those two numbers.</li>
  <li>Factor by grouping (see SAT-29).</li>
</ol>

<blockquote>Rule: a·c gives you what to multiply to, and b gives you what to add to.
<em>(Oʻzbekcha: ikkita son a·c ga koʻpaytirilib, b ga qoʻshilishi kerak.)</em></blockquote>

<h3>Worked Example</h3>
<p>Factor <strong>2x<sup>2</sup> + 7x + 3</strong>.</p>
<ul>
  <li>a·c = 2 × 3 = 6. We need two numbers that multiply to 6 and add to 7 → <strong>6 and 1</strong>.</li>
  <li>Split: 2x<sup>2</sup> + 6x + 1x + 3</li>
  <li>Group: 2x(x + 3) + 1(x + 3)</li>
  <li>Factor out (x + 3): <strong>(2x + 1)(x + 3)</strong></li>
</ul>
<p>Check by FOIL: (2x + 1)(x + 3) = 2x<sup>2</sup> + 7x + 3. ✓</p>
<p><em>(Oʻzbekcha: oʻrta hadni (7x) ikkita hadga ajratamiz, soʻng guruhlab umumiy koʻpaytuvchini chiqaramiz.)</em></p>

<h3>Watch the signs</h3>
<p>If c is negative, the two numbers have <em>opposite</em> signs. If b is negative but c is
positive, both numbers are negative.</p>
<p><em>(Oʻzbekcha: agar c manfiy boʻlsa, sonlar har xil ishorada boʻladi; ishoralarga juda eʼtibor bering.)</em></p>

<h3>Practice</h3>
<p>Factor 3x<sup>2</sup> − 10x + 8.</p>
<details>
  <summary>Show answer</summary>
  <p>a·c = 3 × 8 = 24. Need product 24, sum −10 → −6 and −4.</p>
  <p>3x<sup>2</sup> − 6x − 4x + 8 = 3x(x − 2) − 4(x − 2) = <strong>(3x − 4)(x − 2)</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Factor</strong> — koʻpaytuvchilarga ajratish</li>
  <li><strong>Quadratic</strong> — kvadrat ifoda / tenglama</li>
  <li><strong>Coefficient</strong> — koeffitsiyent</li>
  <li><strong>Leading coefficient</strong> — bosh koeffitsiyent</li>
  <li><strong>Term</strong> — had</li>
  <li><strong>Middle term</strong> — oʻrta had</li>
  <li><strong>Grouping</strong> — guruhlash</li>
  <li><strong>Product</strong> — koʻpaytma</li>
  <li><strong>Sum</strong> — yigʻindi</li>
  <li><strong>Sign</strong> — ishora</li>
</ul>

<h3>Summary</h3>
<ul>
  <li><mark>AC method</mark>: find two numbers that multiply to a·c and add to b.</li>
  <li>Split the middle term, then factor by grouping.</li>
  <li>Always check by multiplying back (FOIL).</li>
  <li>Signs: negative c → opposite signs; positive c with negative b → both negative.</li>
</ul>
""".strip(),
    },

    # ── 33 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-33: The Quadratic Formula and the Discriminant",
        "category": "math",
        "summary": "Solve any quadratic with the quadratic formula, and meet the discriminant b² − 4ac.",
        "content": """
<h2>SAT-33: The Quadratic Formula and the Discriminant</h2>
<p><strong>Description:</strong> Some quadratics do not factor nicely. The <mark>quadratic formula</mark>
solves <strong>every</strong> quadratic, even the ugly ones. It is one of the most important tools
on the SAT.</p>

<h3>The Formula</h3>
<blockquote>For ax<sup>2</sup> + bx + c = 0:<br>
<strong>x = ( −b ± √(b<sup>2</sup> − 4ac) ) / (2a)</strong></blockquote>
<p>The <em>±</em> means you usually get <strong>two answers</strong>: one with + and one with −.
<em>(Oʻzbekcha: ± belgisi odatda ikkita javob beradi.)</em></p>

<h3>The Discriminant</h3>
<p>The part under the square root, <strong>b<sup>2</sup> − 4ac</strong>, is called the
<mark>discriminant</mark>. You will use it constantly in SAT-34.</p>
<p><em>(Oʻzbekcha: ildiz ostidagi qism — b<sup>2</sup> − 4ac — diskriminant deyiladi.)</em></p>

<h3>Worked Example</h3>
<p>Solve 2x<sup>2</sup> + 3x − 5 = 0. Here a = 2, b = 3, c = −5.</p>
<p><em>(Oʻzbekcha: avval a, b, c larni ishoralari bilan toʻgʻri yozib oling, keyin formulaga qoʻying.)</em></p>
<ul>
  <li>Discriminant: b<sup>2</sup> − 4ac = 3<sup>2</sup> − 4(2)(−5) = 9 + 40 = 49.</li>
  <li>x = ( −3 ± √49 ) / (2·2) = ( −3 ± 7 ) / 4</li>
  <li>x = 4/4 = <strong>1</strong>  or  x = −10/4 = <strong>−5/2</strong></li>
</ul>

<blockquote>Tip: write down a, b, c carefully <em>with their signs</em> before plugging in.
A wrong sign is the most common mistake here.</blockquote>

<h3>Practice</h3>
<p>Solve x<sup>2</sup> − 4x + 1 = 0 (it does not factor).</p>
<details>
  <summary>Show answer</summary>
  <p>a = 1, b = −4, c = 1. Discriminant = 16 − 4 = 12.</p>
  <p>x = (4 ± √12) / 2 = (4 ± 2√3) / 2 = <strong>2 ± √3</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Quadratic formula</strong> — kvadrat tenglama formulasi</li>
  <li><strong>Discriminant</strong> — diskriminant</li>
  <li><strong>Root / Solution</strong> — ildiz / yechim</li>
  <li><strong>Square root</strong> — kvadrat ildiz</li>
  <li><strong>Coefficient</strong> — koeffitsiyent</li>
  <li><strong>Plus-minus (±)</strong> — qoʻshish-ayirish belgisi</li>
  <li><strong>Substitute / Plug in</strong> — (formulaga) qoʻyish</li>
  <li><strong>Real number</strong> — haqiqiy son</li>
  <li><strong>Factor</strong> — koʻpaytuvchilarga ajratish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Quadratic formula: <strong>x = (−b ± √(b<sup>2</sup> − 4ac)) / (2a)</strong> — works for any quadratic.</li>
  <li>The discriminant is <mark>b<sup>2</sup> − 4ac</mark> (under the root).</li>
  <li>Identify a, b, c with correct signs first.</li>
  <li>The ± normally gives two solutions.</li>
</ul>
""".strip(),
    },

    # ── 34 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-34: Determining Number and Type of Roots using the Discriminant",
        "category": "math",
        "summary": "Use b² − 4ac to tell how many real solutions a quadratic has — without solving it.",
        "content": """
<h2>SAT-34: Determining Number and Type of Roots using the Discriminant</h2>
<p><strong>Description:</strong> The SAT often asks <em>how many</em> solutions an equation has,
not what they are. The <mark>discriminant</mark> (b<sup>2</sup> − 4ac) answers this instantly, so
you do not waste time solving.</p>

<h3>The Three Cases</h3>
<p><em>(Oʻzbekcha: diskriminantning ishorasi tenglama nechta haqiqiy yechimga ega ekanini koʻrsatadi.)</em></p>
<ul>
  <li><strong>b<sup>2</sup> − 4ac &gt; 0</strong> → <mark>two</mark> different real solutions
      (graph crosses the x-axis twice).</li>
  <li><strong>b<sup>2</sup> − 4ac = 0</strong> → <mark>exactly one</mark> real solution
      (graph just touches the x-axis).</li>
  <li><strong>b<sup>2</sup> − 4ac &lt; 0</strong> → <mark>no</mark> real solutions
      (graph never touches the x-axis).</li>
</ul>

<blockquote>Memory hook: Positive = two, Zero = one, Negative = none.
<em>(Oʻzbekcha: musbat → ikkita, nol → bitta, manfiy → yechim yoʻq.)</em></blockquote>

<h3>Worked Example</h3>
<p>How many real solutions does x<sup>2</sup> + 6x + 9 = 0 have?</p>
<ul>
  <li>a = 1, b = 6, c = 9. Discriminant = 6<sup>2</sup> − 4(1)(9) = 36 − 36 = 0.</li>
  <li>Discriminant = 0 → <strong>exactly one</strong> real solution.</li>
</ul>

<h3>Harder SAT version (solve for a constant)</h3>
<p>For what value of k does x<sup>2</sup> + kx + 16 = 0 have exactly one solution?</p>
<ul>
  <li>One solution means discriminant = 0: k<sup>2</sup> − 4(1)(16) = 0.</li>
  <li>k<sup>2</sup> = 64 → k = <strong>±8</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: "aniq bitta yechim" deganda diskriminantni 0 ga tenglab, nomaʼlumni topamiz.)</em></p>

<h3>Practice</h3>
<p>Does 2x<sup>2</sup> − 3x + 5 = 0 have real solutions?</p>
<details>
  <summary>Show answer</summary>
  <p>Discriminant = (−3)<sup>2</sup> − 4(2)(5) = 9 − 40 = −31 &lt; 0 → <strong>no real solutions</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Discriminant</strong> — diskriminant</li>
  <li><strong>Real solution</strong> — haqiqiy yechim</li>
  <li><strong>Root</strong> — ildiz</li>
  <li><strong>x-axis</strong> — x oʻqi</li>
  <li><strong>Graph</strong> — grafik</li>
  <li><strong>Parabola</strong> — parabola</li>
  <li><strong>Touch (the axis)</strong> — (oʻqqa) tegish</li>
  <li><strong>Cross (the axis)</strong> — (oʻqni) kesib oʻtish</li>
  <li><strong>Constant</strong> — oʻzgarmas (konstanta)</li>
  <li><strong>Exactly one</strong> — aniq bitta</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Discriminant = <mark>b<sup>2</sup> − 4ac</mark> tells the number of real roots without solving.</li>
  <li>Positive → two, Zero → one, Negative → none.</li>
  <li>"Exactly one solution" → set the discriminant equal to 0 and solve for the unknown.</li>
</ul>
""".strip(),
    },

    # ── 35 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-35: Vertex Form of a Quadratic",
        "category": "math",
        "summary": "Read the turning point of a parabola straight from vertex form y = a(x − h)² + k.",
        "content": """
<h2>SAT-35: Vertex Form of a Quadratic</h2>
<p><strong>Description:</strong> A parabola has a turning point called the <mark>vertex</mark>.
<strong>Vertex form</strong> lets you read that point directly, with no calculation. The SAT loves this.</p>

<h3>The Form</h3>
<blockquote><strong>y = a(x − h)<sup>2</sup> + k</strong>, where the vertex is the point <strong>(h, k)</strong>.</blockquote>
<p><em>(Oʻzbekcha: uch koʻrinishida parabolaning uchi (choʻqqisi) (h, k) nuqtasi boʻladi.)</em></p>
<p><strong>Watch the sign of h carefully.</strong> The form has (x − h), so:</p>
<ul>
  <li>y = (x − 3)<sup>2</sup> + 2 → h = 3, k = 2 → vertex <strong>(3, 2)</strong>.</li>
  <li>y = (x + 4)<sup>2</sup> − 1 → this is (x − (−4))<sup>2</sup> − 1 → vertex <strong>(−4, −1)</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: x + 4 aslida x − (−4), shuning uchun h = −4.)</em></p>

<h3>What "a" tells you</h3>
<ul>
  <li>a &gt; 0 → parabola opens <strong>up</strong> → vertex is the <mark>lowest</mark> point (minimum).</li>
  <li>a &lt; 0 → parabola opens <strong>down</strong> → vertex is the <mark>highest</mark> point (maximum).</li>
</ul>
<p><em>(Oʻzbekcha: a &gt; 0 boʻlsa parabola yuqoriga ochiladi (eng kichik nuqta), a &lt; 0 boʻlsa pastga ochiladi (eng katta nuqta).)</em></p>

<h3>Vertex form vs standard form</h3>
<ul>
  <li><strong>Standard:</strong> y = ax<sup>2</sup> + bx + c — easy to see the y-intercept (c).</li>
  <li><strong>Vertex:</strong> y = a(x − h)<sup>2</sup> + k — easy to see the vertex (h, k).</li>
</ul>

<h3>Practice</h3>
<p>What is the vertex of y = −2(x − 5)<sup>2</sup> + 7, and is it a max or min?</p>
<details>
  <summary>Show answer</summary>
  <p>Vertex = <strong>(5, 7)</strong>. Since a = −2 &lt; 0, the parabola opens down, so (5, 7) is a
  <strong>maximum</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Vertex</strong> — uch (choʻqqi)</li>
  <li><strong>Vertex form</strong> — uch koʻrinishi</li>
  <li><strong>Parabola</strong> — parabola</li>
  <li><strong>Turning point</strong> — burilish nuqtasi</li>
  <li><strong>Minimum</strong> — eng kichik qiymat</li>
  <li><strong>Maximum</strong> — eng katta qiymat</li>
  <li><strong>Opens up</strong> — yuqoriga ochiladi</li>
  <li><strong>Opens down</strong> — pastga ochiladi</li>
  <li><strong>Standard form</strong> — standart koʻrinish</li>
  <li><strong>y-intercept</strong> — y oʻqini kesish nuqtasi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Vertex form: <strong>y = a(x − h)<sup>2</sup> + k</strong>, vertex = <mark>(h, k)</mark>.</li>
  <li>Sign trick: (x + 4) means h = −4.</li>
  <li>a &gt; 0 opens up (minimum); a &lt; 0 opens down (maximum).</li>
</ul>
""".strip(),
    },

    # ── 36 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-36: Finding Maximum and Minimum Values of a Quadratic",
        "category": "math",
        "summary": "Find the highest or lowest value of a quadratic using the vertex (h, k) and x = −b/2a.",
        "content": """
<h2>SAT-36: Finding Maximum and Minimum Values of a Quadratic</h2>
<p><strong>Description:</strong> Many SAT word problems ask for a <em>maximum profit</em>,
<em>maximum height</em>, or <em>minimum cost</em>. All of these are the <mark>vertex</mark> of a
parabola. This lesson shows how to find it from any form.</p>

<h3>The key idea</h3>
<blockquote>The max or min value of a quadratic happens at the <strong>vertex</strong>.
The vertex's <strong>x = h</strong> tells you <em>where</em>; the <strong>y = k</strong> tells you the
max/min <em>value</em> itself.</blockquote>
<p><em>(Oʻzbekcha: kvadrat funksiyaning eng katta yoki eng kichik qiymati doim uchida (vertex) boʻladi.)</em></p>

<h3>Method 1 — from vertex form</h3>
<p>If y = a(x − h)<sup>2</sup> + k, the max/min value is simply <strong>k</strong> (review SAT-35).</p>

<h3>Method 2 — from standard form</h3>
<p>For y = ax<sup>2</sup> + bx + c, the vertex's x-coordinate is:</p>
<blockquote><strong>x = −b / (2a)</strong></blockquote>
<p>Plug that x back in to get the max/min value (the y).
<em>(Oʻzbekcha: avval x = −b/2a ni top, keyin uni qoʻyib y ni hisobla.)</em></p>

<h3>Worked Example</h3>
<p>A ball's height is h(t) = −16t<sup>2</sup> + 64t. What is its maximum height?</p>
<ul>
  <li>a = −16, b = 64. Time of max: t = −b/(2a) = −64 / (2·−16) = −64 / −32 = <strong>2 seconds</strong>.</li>
  <li>Max height: h(2) = −16(2)<sup>2</sup> + 64(2) = −64 + 128 = <strong>64</strong>.</li>
</ul>
<blockquote>Tip: a &lt; 0 means it opens down, so the vertex is a <strong>maximum</strong> — exactly what a
"maximum height" problem needs.</blockquote>
<p><em>(Oʻzbekcha: "maksimal balandlik" masalalarida a manfiy boʻlganligi uchun uch eng katta qiymatni beradi.)</em></p>

<h3>Practice</h3>
<p>Find the minimum value of y = x<sup>2</sup> − 6x + 5.</p>
<details>
  <summary>Show answer</summary>
  <p>x = −b/(2a) = −(−6)/(2·1) = 3. Then y = 3<sup>2</sup> − 6(3) + 5 = 9 − 18 + 5 = <strong>−4</strong>.</p>
  <p>So the minimum value is −4 (at x = 3).</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Maximum</strong> — eng katta qiymat</li>
  <li><strong>Minimum</strong> — eng kichik qiymat</li>
  <li><strong>Vertex</strong> — uch (choʻqqi)</li>
  <li><strong>Profit</strong> — foyda</li>
  <li><strong>Cost</strong> — xarajat</li>
  <li><strong>Height</strong> — balandlik</li>
  <li><strong>Standard form</strong> — standart koʻrinish</li>
  <li><strong>Substitute / Plug in</strong> — (qiymatni) qoʻyish</li>
  <li><strong>Coordinate</strong> — koordinata</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Max/min of a quadratic = the <mark>vertex</mark>.</li>
  <li>Vertex form: the value is <strong>k</strong> directly.</li>
  <li>Standard form: find <strong>x = −b/(2a)</strong>, then plug in to get the value.</li>
  <li>a &gt; 0 → minimum; a &lt; 0 → maximum.</li>
</ul>
""".strip(),
    },
]
