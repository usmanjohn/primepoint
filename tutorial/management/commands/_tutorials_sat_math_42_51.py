# SAT Math tutorials 42–51 (Polynomials, Exponentials, Functions, Problem-Solving start)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_42_51.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 42 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-42: The Remainder Theorem and the Factor Theorem",
        "category": "math",
        "summary": "Use P(a) to find the remainder when dividing by (x − a), and to test whether (x − a) is a factor.",
        "content": """
<h2>SAT-42: The Remainder Theorem and the Factor Theorem</h2>
<p><strong>Description:</strong> In SAT-41 you divided polynomials the long way. These two theorems
let you get the same information by just <mark>plugging in a number</mark> — no long division needed.</p>

<h3>The Remainder Theorem</h3>
<blockquote>If you divide a polynomial P(x) by (x − a), the remainder is exactly <strong>P(a)</strong>.</blockquote>
<p>So to find a remainder, you don't divide — you evaluate.
<em>(Oʻzbekcha: P(x) ni (x − a) ga boʻlgandagi qoldiq — bu P(a) qiymati.)</em></p>

<h3>The Factor Theorem</h3>
<blockquote>(x − a) is a <mark>factor</mark> of P(x) if and only if <strong>P(a) = 0</strong>.</blockquote>
<p>This is just the special case where the remainder is 0: no remainder means it divides evenly.
<em>(Oʻzbekcha: agar P(a) = 0 boʻlsa, (x − a) — P(x) ning koʻpaytuvchisi.)</em></p>

<h3>Worked Example (remainder)</h3>
<p>Find the remainder when P(x) = x<sup>3</sup> − 2x<sup>2</sup> + 5 is divided by (x − 2).</p>
<ul>
  <li>Here a = 2. Compute P(2) = 2<sup>3</sup> − 2(2)<sup>2</sup> + 5 = 8 − 8 + 5 = <strong>5</strong>.</li>
  <li>The remainder is 5 (no division required).</li>
</ul>

<h3>Worked Example (factor)</h3>
<p>Is (x − 1) a factor of P(x) = x<sup>3</sup> + 2x − 3?</p>
<ul>
  <li>Compute P(1) = 1 + 2 − 3 = 0. Since P(1) = 0, <strong>yes</strong>, (x − 1) is a factor.</li>
</ul>
<p><em>(Oʻzbekcha: P(1) = 0 boʻlgani uchun (x − 1) koʻpaytuvchi ekan.)</em></p>

<h3>Practice</h3>
<p>What is the remainder when P(x) = 2x<sup>2</sup> + 3x − 4 is divided by (x + 1)?</p>
<details>
  <summary>Show answer</summary>
  <p>(x + 1) means a = −1. P(−1) = 2(1) + 3(−1) − 4 = 2 − 3 − 4 = <strong>−5</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Polynomial</strong> — koʻphad</li>
  <li><strong>Remainder Theorem</strong> — qoldiq haqidagi teorema</li>
  <li><strong>Factor Theorem</strong> — koʻpaytuvchi haqidagi teorema</li>
  <li><strong>Remainder</strong> — qoldiq</li>
  <li><strong>Factor</strong> — koʻpaytuvchi</li>
  <li><strong>Evaluate</strong> — qiymatini hisoblash</li>
  <li><strong>Divide evenly</strong> — qoldiqsiz boʻlinish</li>
  <li><strong>Root</strong> — ildiz</li>
  <li><strong>If and only if</strong> — faqat va faqat shu holda</li>
</ul>

<h3>Summary</h3>
<ul>
  <li><mark>Remainder Theorem</mark>: remainder of P(x) ÷ (x − a) is P(a).</li>
  <li><mark>Factor Theorem</mark>: (x − a) is a factor ⇔ P(a) = 0.</li>
  <li>Watch the sign: dividing by (x + 1) means a = −1.</li>
</ul>
""".strip(),
    },

    # ── 43 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-43: Graphs of Higher-Degree Polynomials — End Behavior & Multiplicity",
        "category": "math",
        "summary": "Predict how a polynomial graph starts and ends, and how it behaves at each root using multiplicity.",
        "content": """
<h2>SAT-43: Graphs of Higher-Degree Polynomials — End Behavior &amp; Multiplicity</h2>
<p><strong>Description:</strong> Cubics, quartics and beyond have wavy graphs. Two ideas explain them:
<mark>end behavior</mark> (what the tails do) and <mark>multiplicity</mark> (how the curve behaves at each root).</p>

<h3>End behavior</h3>
<p>The tails depend on the <strong>degree</strong> (highest power) and the <strong>leading coefficient</strong> (sign of the front number):</p>
<ul>
  <li><strong>Even degree</strong> (like x<sup>2</sup>, x<sup>4</sup>): both tails go the <em>same</em> way — both up (if leading coeff &gt; 0) or both down (&lt; 0).</li>
  <li><strong>Odd degree</strong> (like x<sup>3</sup>, x<sup>5</sup>): tails go <em>opposite</em> ways.</li>
</ul>
<p><em>(Oʻzbekcha: juft daraja → ikkala uchi bir tomonga; toq daraja → qarama-qarshi tomonlarga.)</em></p>

<h3>Multiplicity at a root</h3>
<p>The <mark>multiplicity</mark> is how many times a factor repeats. It controls what the graph does at that x-intercept:</p>
<ul>
  <li><strong>Odd</strong> multiplicity (1, 3, …) → the graph <em>crosses</em> the x-axis.</li>
  <li><strong>Even</strong> multiplicity (2, 4, …) → the graph <em>touches</em> and turns back (bounces).</li>
</ul>
<blockquote>Memory hook: odd = cross, even = bounce. <em>(Oʻzbekcha: toq → kesib oʻtadi, juft → tegib qaytadi.)</em></blockquote>

<h3>Worked Example</h3>
<p>Describe y = (x − 1)<sup>2</sup>(x + 2).</p>
<ul>
  <li>Degree = 2 + 1 = 3 (odd), leading coeff positive → left tail down, right tail up.</li>
  <li>Root x = 1 has multiplicity 2 (even) → graph <strong>touches</strong> at x = 1.</li>
  <li>Root x = −2 has multiplicity 1 (odd) → graph <strong>crosses</strong> at x = −2.</li>
</ul>
<p><em>(Oʻzbekcha: x = 1 da tegib qaytadi, x = −2 da kesib oʻtadi.)</em></p>

<h3>Practice</h3>
<p>At x = 3, does y = (x − 3)<sup>4</sup>(x + 1) cross or touch the x-axis?</p>
<details>
  <summary>Show answer</summary>
  <p>x = 3 has multiplicity 4 (even) → the graph <strong>touches</strong> (bounces) at x = 3.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Degree</strong> — daraja</li>
  <li><strong>Leading coefficient</strong> — bosh koeffitsiyent</li>
  <li><strong>End behavior</strong> — uchlarining xatti-harakati</li>
  <li><strong>Multiplicity</strong> — karralilik (takrorlanish soni)</li>
  <li><strong>Root / Zero</strong> — ildiz / nol</li>
  <li><strong>Cross</strong> — kesib oʻtish</li>
  <li><strong>Touch / Bounce</strong> — tegib qaytish</li>
  <li><strong>Even / Odd</strong> — juft / toq</li>
  <li><strong>Tail</strong> — uch (dum)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>End behavior: even degree → same-direction tails; odd degree → opposite tails (sign of leading coeff flips them).</li>
  <li>Multiplicity: <mark>odd → cross</mark>, <mark>even → touch/bounce</mark>.</li>
  <li>Total degree = sum of all the multiplicities.</li>
</ul>
""".strip(),
    },

    # ── 44 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-44: Exponential vs. Linear Growth",
        "category": "math",
        "summary": "Tell linear growth (add the same amount) apart from exponential growth (multiply by the same factor).",
        "content": """
<h2>SAT-44: Exponential vs. Linear Growth</h2>
<p><strong>Description:</strong> The SAT loves to ask whether a situation is <mark>linear</mark> or
<mark>exponential</mark>. The difference is simple: linear <em>adds</em> a fixed amount each step;
exponential <em>multiplies</em> by a fixed factor each step.</p>

<h3>The key distinction</h3>
<ul>
  <li><strong>Linear:</strong> changes by a constant <em>amount</em> (repeated addition). Form: y = mx + b.</li>
  <li><strong>Exponential:</strong> changes by a constant <em>percent/factor</em> (repeated multiplication). Form: y = a·b<sup>x</sup>.</li>
</ul>
<p><em>(Oʻzbekcha: chiziqli — har qadamda bir xil son qoʻshiladi; eksponensial — har qadamda bir xil songa koʻpaytiriladi.)</em></p>

<h3>How to spot it from a table</h3>
<p>Look at consecutive y-values:</p>
<ul>
  <li>If you <strong>subtract</strong> and always get the same difference → <mark>linear</mark>.</li>
  <li>If you <strong>divide</strong> and always get the same ratio → <mark>exponential</mark>.</li>
</ul>
<blockquote>Tip: "doubles every…", "triples…", "grows 5% per…" all signal <strong>exponential</strong>.
<em>(Oʻzbekcha: "ikki barobar oshadi", "5% ga oshadi" — bular eksponensial belgilari.)</em></blockquote>

<h3>Worked Example</h3>
<p>A table shows y-values 3, 6, 12, 24 for x = 0, 1, 2, 3. Linear or exponential?</p>
<ul>
  <li>Differences: 3 → 6 is +3, 6 → 12 is +6. Not constant, so <strong>not linear</strong>.</li>
  <li>Ratios: 6/3 = 2, 12/6 = 2, 24/12 = 2. Constant ratio 2 → <strong>exponential</strong>, y = 3·2<sup>x</sup>.</li>
</ul>
<p><em>(Oʻzbekcha: nisbat doim 2 ga teng, demak eksponensial.)</em></p>

<h3>Practice</h3>
<p>Values 100, 80, 64, 51.2 — linear or exponential?</p>
<details>
  <summary>Show answer</summary>
  <p>Ratios: 80/100 = 0.8, 64/80 = 0.8, 51.2/64 = 0.8. Constant ratio → <strong>exponential</strong> decay, y = 100·(0.8)<sup>x</sup>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Linear growth</strong> — chiziqli oʻsish</li>
  <li><strong>Exponential growth</strong> — eksponensial oʻsish</li>
  <li><strong>Constant difference</strong> — oʻzgarmas ayirma</li>
  <li><strong>Constant ratio</strong> — oʻzgarmas nisbat</li>
  <li><strong>Add / Subtract</strong> — qoʻshish / ayirish</li>
  <li><strong>Multiply / Divide</strong> — koʻpaytirish / boʻlish</li>
  <li><strong>Decay</strong> — kamayish (so&apos;nish)</li>
  <li><strong>Factor</strong> — koʻpaytuvchi (koeffitsiyent)</li>
  <li><strong>Rate</strong> — tezlik (sur&apos;at)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Linear = repeated <strong>addition</strong> (constant difference), y = mx + b.</li>
  <li>Exponential = repeated <strong>multiplication</strong> (constant ratio), y = a·b<sup>x</sup>.</li>
  <li>From a table: equal differences → linear; equal ratios → exponential.</li>
</ul>
""".strip(),
    },

    # ── 45 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-45: Writing Exponential Functions (y = ab^x) from Word Problems",
        "category": "math",
        "summary": "Turn a real-world growth or decay story into y = a·b^x by finding the start value a and the factor b.",
        "content": """
<h2>SAT-45: Writing Exponential Functions (y = ab<sup>x</sup>) from Word Problems</h2>
<p><strong>Description:</strong> Once you know a situation is exponential (SAT-44), you write it as
<mark>y = a·b<sup>x</sup></mark>. This lesson shows how to pull <strong>a</strong> and <strong>b</strong>
out of the words.</p>

<h3>What a and b mean</h3>
<ul>
  <li><strong>a</strong> = the <mark>starting value</mark> (when x = 0).</li>
  <li><strong>b</strong> = the <mark>growth/decay factor</mark> per step.</li>
</ul>
<p>Build b from the percent rate:</p>
<ul>
  <li>Growth of r% → b = 1 + r/100 (e.g. +8% → b = 1.08).</li>
  <li>Decay of r% → b = 1 − r/100 (e.g. −8% → b = 0.92).</li>
</ul>
<p><em>(Oʻzbekcha: a — boshlangʻich qiymat, b — har bir qadamdagi oʻzgarish koeffitsiyenti.)</em></p>

<h3>Worked Example (growth)</h3>
<p>A town has 5,000 people and grows 3% per year. Write the population after x years.</p>
<ul>
  <li>Starting value a = 5000.</li>
  <li>Growth 3% → b = 1 + 0.03 = 1.03.</li>
  <li>Function: <strong>y = 5000·(1.03)<sup>x</sup></strong>.</li>
</ul>
<p><em>(Oʻzbekcha: 3% oʻsish uchun b = 1.03.)</em></p>

<h3>Worked Example (decay)</h3>
<p>A car worth $20,000 loses 15% of its value each year.</p>
<ul>
  <li>a = 20000, decay 15% → b = 1 − 0.15 = 0.85.</li>
  <li>Function: <strong>y = 20000·(0.85)<sup>x</sup></strong>.</li>
</ul>
<blockquote>Tip: "doubles" → b = 2; "halves" → b = 0.5; "triples" → b = 3.
<em>(Oʻzbekcha: "ikki barobar" → b = 2; "yarmiga" → b = 0.5.)</em></blockquote>

<h3>Practice</h3>
<p>A colony of 200 bacteria doubles every hour. Write y for hours x.</p>
<details>
  <summary>Show answer</summary>
  <p>a = 200, doubling → b = 2. So <strong>y = 200·2<sup>x</sup></strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Exponential function</strong> — eksponensial funksiya</li>
  <li><strong>Starting value (initial)</strong> — boshlangʻich qiymat</li>
  <li><strong>Growth factor</strong> — oʻsish koeffitsiyenti</li>
  <li><strong>Decay factor</strong> — kamayish koeffitsiyenti</li>
  <li><strong>Rate (percent)</strong> — foiz sur&apos;ati</li>
  <li><strong>Per year / per hour</strong> — har yili / har soatda</li>
  <li><strong>Double / Halve</strong> — ikki barobar / yarmiga</li>
  <li><strong>Base</strong> — asos</li>
  <li><strong>Exponent</strong> — daraja koʻrsatkichi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Model: <mark>y = a·b<sup>x</sup></mark>; a = starting value, b = factor per step.</li>
  <li>Growth r% → b = 1 + r/100; decay r% → b = 1 − r/100.</li>
  <li>"Doubles" → b = 2, "halves" → b = 0.5, etc.</li>
</ul>
""".strip(),
    },

    # ── 46 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-46: Compound Interest and Percent Growth",
        "category": "math",
        "summary": "Use the compound-interest formula to grow money by a percent over many periods, including monthly/yearly.",
        "content": """
<h2>SAT-46: Compound Interest and Percent Growth</h2>
<p><strong>Description:</strong> <mark>Compound interest</mark> is exponential growth applied to money:
each period you earn interest on the previous total, not just the original amount. The SAT gives a
standard formula.</p>

<h3>The formula</h3>
<blockquote><strong>A = P(1 + r/n)<sup>nt</sup></strong></blockquote>
<ul>
  <li><strong>P</strong> = principal (starting money),</li>
  <li><strong>r</strong> = annual rate as a decimal (5% → 0.05),</li>
  <li><strong>n</strong> = times compounded per year,</li>
  <li><strong>t</strong> = number of years.</li>
</ul>
<p><em>(Oʻzbekcha: P — boshlangʻich pul, r — yillik foiz (oʻnli kasr), n — yiliga necha marta, t — yillar soni.)</em></p>

<h3>Why "compound" beats "simple"</h3>
<p>Simple interest grows by the same amount each year (linear). Compound interest grows on the new,
larger balance each period (exponential), so it pulls ahead over time.
<em>(Oʻzbekcha: murakkab foiz har safar yangi, kattaroq summadan hisoblanadi.)</em></p>

<h3>Worked Example</h3>
<p>$1,000 at 6% per year, compounded annually, for 3 years.</p>
<ul>
  <li>P = 1000, r = 0.06, n = 1, t = 3.</li>
  <li>A = 1000(1 + 0.06/1)<sup>1·3</sup> = 1000(1.06)<sup>3</sup> = 1000(1.191016) ≈ <strong>$1,191.02</strong>.</li>
</ul>

<h3>Worked Example (monthly)</h3>
<p>$2,000 at 12% per year, compounded monthly, for 2 years.</p>
<ul>
  <li>r/n = 0.12/12 = 0.01, and nt = 12·2 = 24.</li>
  <li>A = 2000(1.01)<sup>24</sup> ≈ <strong>$2,539.47</strong>.</li>
</ul>
<blockquote>Tip: "compounded monthly" means n = 12; "quarterly" n = 4; "annually" n = 1.
<em>(Oʻzbekcha: oylik → n = 12; choraklik → n = 4; yillik → n = 1.)</em></blockquote>

<h3>Practice</h3>
<p>$500 at 4% compounded annually for 2 years — find A.</p>
<details>
  <summary>Show answer</summary>
  <p>A = 500(1.04)<sup>2</sup> = 500(1.0816) = <strong>$540.80</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Compound interest</strong> — murakkab foiz</li>
  <li><strong>Simple interest</strong> — oddiy foiz</li>
  <li><strong>Principal</strong> — boshlangʻich summa (asosiy pul)</li>
  <li><strong>Rate</strong> — foiz stavkasi</li>
  <li><strong>Annually</strong> — yillik</li>
  <li><strong>Monthly</strong> — oylik</li>
  <li><strong>Quarterly</strong> — choraklik</li>
  <li><strong>Balance</strong> — qoldiq (hisobdagi pul)</li>
  <li><strong>Period</strong> — davr</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Compound interest: <mark>A = P(1 + r/n)<sup>nt</sup></mark>.</li>
  <li>Convert the percent to a decimal; n = compounds per year; t = years.</li>
  <li>Monthly n = 12, quarterly n = 4, annually n = 1.</li>
</ul>
""".strip(),
    },

    # ── 47 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-47: Functions — Domain, Range, and Evaluation",
        "category": "math",
        "summary": "Understand function notation f(x), evaluate it, and find the domain (inputs) and range (outputs).",
        "content": """
<h2>SAT-47: Functions — Domain, Range, and Evaluation</h2>
<p><strong>Description:</strong> A <mark>function</mark> is a rule that takes an input and gives exactly one
output. This lesson covers function notation f(x), how to evaluate it, and the meaning of
<strong>domain</strong> and <strong>range</strong>.</p>

<h3>Function notation</h3>
<p><strong>f(x)</strong> means "the output of f for input x." To <mark>evaluate</mark>, just substitute
the number for x.</p>
<p><em>(Oʻzbekcha: funksiya — har bir kirish uchun aniq bitta chiqish beruvchi qoida.)</em></p>

<h3>Domain and range</h3>
<ul>
  <li><strong>Domain</strong> = all allowed <mark>inputs</mark> (x-values).</li>
  <li><strong>Range</strong> = all possible <mark>outputs</mark> (y-values).</li>
</ul>
<p>Two common domain limits: you can't divide by zero, and you can't take the square root of a
negative number. <em>(Oʻzbekcha: aniqlanish sohasi — ruxsat etilgan x lar; qiymatlar sohasi — chiqadigan y lar.)</em></p>

<h3>Worked Example (evaluate)</h3>
<p>If f(x) = 2x<sup>2</sup> − 3, find f(4) and f(−1).</p>
<ul>
  <li>f(4) = 2(4)<sup>2</sup> − 3 = 32 − 3 = <strong>29</strong>.</li>
  <li>f(−1) = 2(−1)<sup>2</sup> − 3 = 2 − 3 = <strong>−1</strong>.</li>
</ul>

<h3>Worked Example (domain)</h3>
<p>What is the domain of f(x) = 1/(x − 5)?</p>
<ul>
  <li>The denominator can't be 0, so x − 5 ≠ 0 → x ≠ 5.</li>
  <li>Domain: <strong>all real numbers except 5</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: x = 5 da maxraj 0 boʻladi, shuning uchun u sohaga kirmaydi.)</em></p>

<h3>Practice</h3>
<p>If g(x) = x<sup>2</sup> + 1, what is the smallest value in its range?</p>
<details>
  <summary>Show answer</summary>
  <p>x<sup>2</sup> ≥ 0, so x<sup>2</sup> + 1 ≥ 1. The smallest output is <strong>1</strong> (at x = 0). Range: y ≥ 1.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Function</strong> — funksiya</li>
  <li><strong>Function notation f(x)</strong> — funksiya belgisi f(x)</li>
  <li><strong>Input</strong> — kirish (argument)</li>
  <li><strong>Output</strong> — chiqish (qiymat)</li>
  <li><strong>Evaluate</strong> — qiymatini hisoblash</li>
  <li><strong>Domain</strong> — aniqlanish sohasi</li>
  <li><strong>Range</strong> — qiymatlar sohasi</li>
  <li><strong>Substitute</strong> — oʻrniga qoʻyish</li>
  <li><strong>Real numbers</strong> — haqiqiy sonlar</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>f(x) is a rule with one output per input; <mark>evaluate</mark> by substituting.</li>
  <li><strong>Domain</strong> = allowed inputs; <strong>range</strong> = possible outputs.</li>
  <li>Exclude inputs that cause division by zero or a square root of a negative.</li>
</ul>
""".strip(),
    },

    # ── 48 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-48: Function Transformations — Shifts and Reflections",
        "category": "math",
        "summary": "Shift and reflect a graph by changing f(x): outside moves it vertically, inside moves it horizontally (and backwards).",
        "content": """
<h2>SAT-48: Function Transformations — Shifts and Reflections</h2>
<p><strong>Description:</strong> If you know the graph of f(x), you can move it without re-graphing.
Small changes to f(x) cause predictable <mark>shifts</mark> and <mark>reflections</mark>.</p>

<h3>Vertical changes (outside the function)</h3>
<ul>
  <li><strong>f(x) + k</strong> → shift <mark>up</mark> k units.</li>
  <li><strong>f(x) − k</strong> → shift <mark>down</mark> k units.</li>
  <li><strong>−f(x)</strong> → reflect over the x-axis (flip upside down).</li>
</ul>
<p><em>(Oʻzbekcha: funksiyaning tashqarisidagi oʻzgarish grafikni vertikal (yuqori-past) suradi.)</em></p>

<h3>Horizontal changes (inside the function)</h3>
<p>These work <strong>opposite</strong> to what you'd expect:</p>
<ul>
  <li><strong>f(x − h)</strong> → shift <mark>right</mark> h units.</li>
  <li><strong>f(x + h)</strong> → shift <mark>left</mark> h units.</li>
  <li><strong>f(−x)</strong> → reflect over the y-axis.</li>
</ul>
<blockquote>Rule: inside changes are backwards. f(x − 3) moves <em>right</em> 3, not left.
<em>(Oʻzbekcha: ichkaridagi oʻzgarish teskari ishlaydi: x − 3 → oʻngga suriladi.)</em></blockquote>

<h3>Worked Example</h3>
<p>Starting from f(x), describe g(x) = f(x − 2) + 5.</p>
<ul>
  <li>Inside (x − 2): shift right 2.</li>
  <li>Outside (+5): shift up 5.</li>
  <li>So g is f moved <strong>right 2 and up 5</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: ichkarisi oʻngga 2, tashqarisi yuqoriga 5 suradi.)</em></p>

<h3>Practice</h3>
<p>How does h(x) = −f(x + 4) transform f(x)?</p>
<details>
  <summary>Show answer</summary>
  <p>Inside (x + 4) → shift <strong>left 4</strong>; the leading minus → <strong>reflect over the x-axis</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Transformation</strong> — almashtirish (oʻzgartirish)</li>
  <li><strong>Shift</strong> — surish</li>
  <li><strong>Reflection</strong> — koʻzguda aks ettirish</li>
  <li><strong>Vertical</strong> — vertikal (tik)</li>
  <li><strong>Horizontal</strong> — gorizontal (yotiq)</li>
  <li><strong>Up / Down</strong> — yuqoriga / pastga</li>
  <li><strong>Left / Right</strong> — chapga / oʻngga</li>
  <li><strong>x-axis / y-axis</strong> — x oʻqi / y oʻqi</li>
  <li><strong>Units</strong> — birliklar</li>
</ul>

<h3>Summary</h3>
<ul>
  <li><mark>Outside</mark> f(x): vertical — +k up, −k down, −f(x) flips over x-axis.</li>
  <li><mark>Inside</mark> f(x): horizontal and <strong>backwards</strong> — (x − h) right, (x + h) left, f(−x) flips over y-axis.</li>
</ul>
""".strip(),
    },

    # ── 49 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-49: Ratios, Rates, and Proportions",
        "category": "math",
        "summary": "Compare quantities with ratios and rates, and solve proportions by cross-multiplying.",
        "content": """
<h2>SAT-49: Ratios, Rates, and Proportions</h2>
<p><strong>Description:</strong> A <mark>ratio</mark> compares two quantities, a <mark>rate</mark> is a ratio
with different units (like miles per hour), and a <mark>proportion</mark> sets two ratios equal. These
power a huge share of SAT word problems.</p>

<h3>Definitions</h3>
<ul>
  <li><strong>Ratio</strong>: 3 : 5 or 3/5 — a comparison.</li>
  <li><strong>Rate</strong>: a ratio of different units, e.g. 60 miles / 1 hour.</li>
  <li><strong>Unit rate</strong>: a rate with denominator 1 (e.g. 60 mph, $3 per item).</li>
  <li><strong>Proportion</strong>: two equal ratios, a/b = c/d.</li>
</ul>
<p><em>(Oʻzbekcha: nisbat ikki miqdorni taqqoslaydi; proporsiya ikkita nisbatni tenglashtiradi.)</em></p>

<h3>Solving a proportion</h3>
<p>Use <mark>cross-multiplication</mark>: if a/b = c/d then a·d = b·c.
<em>(Oʻzbekcha: proporsiyani krestga koʻpaytirib yechamiz: a·d = b·c.)</em></p>

<h3>Worked Example</h3>
<p>If 3 apples cost $1.20, how much do 7 apples cost?</p>
<ul>
  <li>Set up: 3/1.20 = 7/x.</li>
  <li>Cross-multiply: 3x = 7(1.20) = 8.40.</li>
  <li>x = 8.40/3 = <strong>$2.80</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: bir xil birliklar mos joyda boʻlishi kerak — olma olmaga, narx narxga.)</em></p>

<h3>Worked Example (ratio split)</h3>
<p>$60 is split between two people in the ratio 2 : 3. How much does each get?</p>
<ul>
  <li>Total parts = 2 + 3 = 5. One part = 60/5 = 12.</li>
  <li>Shares: 2·12 = <strong>$24</strong> and 3·12 = <strong>$36</strong>.</li>
</ul>

<h3>Practice</h3>
<p>A car travels 150 miles in 3 hours. At the same rate, how far in 5 hours?</p>
<details>
  <summary>Show answer</summary>
  <p>Unit rate = 150/3 = 50 mph. In 5 hours: 50 × 5 = <strong>250 miles</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Ratio</strong> — nisbat</li>
  <li><strong>Rate</strong> — tezlik (sur&apos;at)</li>
  <li><strong>Unit rate</strong> — birlik tezlik</li>
  <li><strong>Proportion</strong> — proporsiya</li>
  <li><strong>Cross-multiply</strong> — krestga koʻpaytirish</li>
  <li><strong>Quantity</strong> — miqdor</li>
  <li><strong>Per</strong> — har biriga</li>
  <li><strong>Share / Part</strong> — ulush / qism</li>
  <li><strong>Total</strong> — jami</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Ratio = comparison; rate = ratio of different units; unit rate has denominator 1.</li>
  <li>Solve proportions by <mark>cross-multiplying</mark> (a/b = c/d → a·d = b·c).</li>
  <li>Ratio split: add the parts, find one part, multiply out.</li>
</ul>
""".strip(),
    },

    # ── 50 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-50: Unit Conversions and Dimensional Analysis",
        "category": "math",
        "summary": "Convert units by multiplying by conversion factors so unwanted units cancel.",
        "content": """
<h2>SAT-50: Unit Conversions and Dimensional Analysis</h2>
<p><strong>Description:</strong> <mark>Dimensional analysis</mark> converts units by multiplying by
fractions that equal 1 (<strong>conversion factors</strong>), arranged so the units you don't want
<em>cancel</em>. It's the safest way to handle SAT unit problems.</p>

<h3>The idea</h3>
<p>A conversion factor like (12 inches / 1 foot) equals 1, so multiplying by it doesn't change the
value — only the units. Put the unit you want to cancel on the <strong>opposite</strong> side of the
fraction so it divides out.</p>
<p><em>(Oʻzbekcha: oʻlchov birliklarini almashtirishda kerakmas birlik qisqarib ketadigan qilib koʻpaytiramiz.)</em></p>

<h3>Worked Example (one step)</h3>
<p>Convert 5 feet to inches (1 foot = 12 inches).</p>
<ul>
  <li>5 ft × (12 in / 1 ft) = 60 in. The "ft" cancels, leaving inches.</li>
  <li>Answer: <strong>60 inches</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: "ft" yuqorida va pastda boʻlgani uchun qisqaradi, faqat "in" qoladi.)</em></p>

<h3>Worked Example (chained)</h3>
<p>Convert 90 km/h to meters per second (1 km = 1000 m, 1 h = 3600 s).</p>
<ul>
  <li>90 km/h × (1000 m / 1 km) × (1 h / 3600 s)</li>
  <li>= 90 × 1000 / 3600 m/s = 90000/3600 = <strong>25 m/s</strong>.</li>
</ul>
<blockquote>Tip: line up the factors so every unwanted unit appears once on top and once on bottom.
<em>(Oʻzbekcha: har bir kerakmas birlik bir marta yuqorida, bir marta pastda boʻlsin.)</em></blockquote>

<h3>Practice</h3>
<p>Convert 3 hours to seconds.</p>
<details>
  <summary>Show answer</summary>
  <p>3 h × (3600 s / 1 h) = <strong>10,800 seconds</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Unit conversion</strong> — birliklarni almashtirish</li>
  <li><strong>Dimensional analysis</strong> — oʻlchamlar tahlili</li>
  <li><strong>Conversion factor</strong> — almashtirish koeffitsiyenti</li>
  <li><strong>Cancel (units)</strong> — (birliklarni) qisqartirish</li>
  <li><strong>Numerator / Denominator</strong> — surat / maxraj</li>
  <li><strong>Per</strong> — har biriga</li>
  <li><strong>Rate</strong> — tezlik</li>
  <li><strong>Equivalent</strong> — teng qiymatli</li>
  <li><strong>Measurement</strong> — oʻlchov</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Multiply by <mark>conversion factors</mark> (fractions equal to 1) to change units.</li>
  <li>Arrange each factor so the unwanted unit <strong>cancels</strong> (top vs bottom).</li>
  <li>Chain several factors for multi-step conversions (e.g. km/h → m/s).</li>
</ul>
""".strip(),
    },

    # ── 51 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-51: Percentages — Part, Whole, and Base",
        "category": "math",
        "summary": "Master the part = percent × whole relationship to find a part, a whole, or a percent.",
        "content": """
<h2>SAT-51: Percentages — Part, Whole, and Base</h2>
<p><strong>Description:</strong> Percent means "per 100." Almost every percent question is one
relationship: <mark>part = percent × whole</mark>. Rearranging it solves for whichever piece is missing.</p>

<h3>The core relationship</h3>
<blockquote><strong>part = (percent ÷ 100) × whole</strong></blockquote>
<ul>
  <li>Find the <strong>part</strong>: multiply (e.g. 20% of 50 = 0.20 × 50 = 10).</li>
  <li>Find the <strong>percent</strong>: part ÷ whole, then ×100.</li>
  <li>Find the <strong>whole</strong> (base): part ÷ (percent/100).</li>
</ul>
<p><em>(Oʻzbekcha: foiz — "yuzdan necha". Asosiy formula: qism = (foiz ÷ 100) × butun.)</em></p>

<h3>Worked Example (find the part)</h3>
<p>What is 15% of 80?</p>
<ul>
  <li>0.15 × 80 = <strong>12</strong>.</li>
</ul>

<h3>Worked Example (find the percent)</h3>
<p>18 is what percent of 24?</p>
<ul>
  <li>18 ÷ 24 = 0.75 → ×100 = <strong>75%</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: qismni butunga boʻlib, 100 ga koʻpaytiramiz.)</em></p>

<h3>Worked Example (find the whole / base)</h3>
<p>30 is 20% of what number?</p>
<ul>
  <li>whole = 30 ÷ 0.20 = <strong>150</strong>.</li>
</ul>
<blockquote>Watch the wording: "<em>of</em>" marks the <strong>whole</strong> (base); "<em>is</em>" marks the part.
<em>(Oʻzbekcha: "ning" — butun (asos); "bu/teng" — qism.)</em></blockquote>

<h3>Practice</h3>
<p>A shirt costs $40 and is 25% of a person's daily budget. What is the budget?</p>
<details>
  <summary>Show answer</summary>
  <p>budget = 40 ÷ 0.25 = <strong>$160</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Percent</strong> — foiz</li>
  <li><strong>Part</strong> — qism</li>
  <li><strong>Whole / Base</strong> — butun / asos</li>
  <li><strong>Per 100</strong> — yuzdan</li>
  <li><strong>Of</strong> (= multiply) — "ning" (koʻpaytirish)</li>
  <li><strong>Is</strong> (= equals) — "teng"</li>
  <li><strong>Decimal</strong> — oʻnli kasr</li>
  <li><strong>Multiply / Divide</strong> — koʻpaytirish / boʻlish</li>
  <li><strong>Budget</strong> — byudjet (mablagʻ)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Everything comes from <mark>part = (percent/100) × whole</mark>.</li>
  <li>Percent = part ÷ whole × 100; whole = part ÷ (percent/100).</li>
  <li>"Of" → the whole/base; "is" → the part.</li>
</ul>
""".strip(),
    },
]
