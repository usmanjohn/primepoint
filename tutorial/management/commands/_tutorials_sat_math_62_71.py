# SAT Math tutorials 62–71 (end of Data Analysis + start of Geometry)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_62_71.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 62 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-62: Experimental Design — Random Assignment and Cause-and-Effect",
        "category": "math",
        "summary": "Tell experiments from observational studies and know when you can claim one thing causes another.",
        "content": """
<h2>SAT-62: Experimental Design — Random Assignment and Cause-and-Effect</h2>
<p><strong>Description:</strong> SAT-61 warned that correlation is not causation. This lesson explains the one
situation where you <em>can</em> claim cause-and-effect: a well-designed <mark>experiment</mark> with
<mark>random assignment</mark>. Knowing the difference between an experiment and an observational study is a
guaranteed SAT question.</p>

<h3>Two kinds of studies</h3>
<ul>
  <li><strong>Observational study:</strong> you only <em>watch</em> and record; you don't change anything. It can
  show an association, but lurking variables may explain it.</li>
  <li><strong>Experiment:</strong> you actively <em>apply a treatment</em> to subjects and compare groups. Done
  right, it can show causation.</li>
</ul>
<p><em>(Oʻzbekcha: kuzatuv tadqiqotida faqat qarab turamiz; eksperimentda esa biror taʼsir (davolash) qoʻllaymiz.)</em></p>

<h3>The three pillars of a good experiment</h3>
<ul>
  <li><strong>Control group</strong> vs <strong>treatment group</strong>: one group gets the treatment, one doesn't,
  so you have something to compare.</li>
  <li><strong>Random assignment:</strong> subjects are placed into groups <em>by chance</em>. This spreads hidden
  differences evenly, so the only systematic difference left is the treatment.</li>
  <li><strong>Replication:</strong> enough subjects that the result isn't just luck.</li>
</ul>
<p>Random <em>assignment</em> (to groups) is what allows causal claims; random <em>selection</em> (SAT-60) is what
allows generalizing to a population. The SAT loves this distinction.
<em>(Oʻzbekcha: tasodifiy taqsimlash — sababiy xulosa uchun; tasodifiy tanlash — umumlashtirish uchun.)</em></p>

<h3>Worked Example 1 — classify the study</h3>
<p>Researchers record the diets people already follow and compare their health. Experiment or observational?</p>
<ul>
  <li>Nothing was assigned — they only observed existing diets → <strong>observational study</strong>. It can't prove
  the diet caused the health difference.</li>
</ul>

<h3>Worked Example 2 — what makes it causal</h3>
<p>A company randomly assigns 100 volunteers to take a new vitamin or a placebo, then compares energy levels. Can
they claim the vitamin caused any difference?</p>
<ul>
  <li>Yes — random assignment plus a control (placebo) group means the groups were alike except for the vitamin, so a
  difference can be attributed to it. <strong>Causal claim is justified.</strong></li>
</ul>
<p><em>(Oʻzbekcha: tasodifiy taqsimlash va nazorat guruhi boʻlgani uchun sababiy xulosa chiqarish mumkin.)</em></p>

<h3>Worked Example 3 — scope of the conclusion</h3>
<p>In that vitamin study the 100 volunteers were not randomly selected from any population — they just volunteered.
What can and can't the company conclude?</p>
<ul>
  <li>They <em>can</em> say the vitamin caused the effect <strong>within these subjects</strong> (random assignment).</li>
  <li>They <em>cannot</em> generalize to all people, because the subjects weren't randomly selected.</li>
</ul>
<blockquote>Rule: random <strong>assignment</strong> → causation; random <strong>selection</strong> → generalization.
You need both for "this causes that for everyone." <em>(Oʻzbekcha: ikkalasi ham boʻlsa — "hamma uchun sabab" deyish mumkin.)</em></blockquote>

<h3>The four-box summary (a fast way to answer)</h3>
<p>Every SAT design question fits into one of four boxes formed by two yes/no questions: <em>Was there random
assignment?</em> and <em>Was there random selection?</em></p>
<ul>
  <li>Assignment yes + selection yes → can claim cause <strong>and</strong> generalize.</li>
  <li>Assignment yes + selection no → can claim cause, but only for the subjects studied.</li>
  <li>Assignment no + selection yes → can generalize an association, but not claim cause.</li>
  <li>Assignment no + selection no → only an association among these subjects; no cause, no generalizing.</li>
</ul>
<p>Decide the two yes/no answers first, and the correct conclusion falls out automatically.
<em>(Oʻzbekcha: ikkita savolga (taqsimlash tasodifiymi? tanlash tasodifiymi?) javob bering — xulosa oʻzidan kelib chiqadi.)</em></p>

<h3>Practice 1</h3>
<p>A study finds students who eat breakfast score higher, by surveying current habits. Can it claim breakfast causes
higher scores?</p>
<details>
  <summary>Show answer</summary>
  <p>No. It is <strong>observational</strong> (no treatment was assigned), so a lurking variable could explain the
  link. It shows association, not causation.</p>
</details>

<h3>Practice 2</h3>
<p>To test a teaching app, a school randomly assigns half its students to use it and half not, then compares grades.
Which type of study is this, and can it show cause?</p>
<details>
  <summary>Show answer</summary>
  <p>An <strong>experiment</strong> with random assignment and a control group, so it <strong>can</strong> support a
  causal claim about these students.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Experiment</strong> — tajriba (eksperiment)</li>
  <li><strong>Observational study</strong> — kuzatuv tadqiqoti</li>
  <li><strong>Treatment</strong> — taʼsir (davolash usuli)</li>
  <li><strong>Control group</strong> — nazorat guruhi</li>
  <li><strong>Random assignment</strong> — tasodifiy taqsimlash</li>
  <li><strong>Placebo</strong> — platsebo (soxta dori)</li>
  <li><strong>Cause-and-effect</strong> — sabab-natija</li>
  <li><strong>Lurking variable</strong> — yashirin omil</li>
  <li><strong>Replication</strong> — takrorlash</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Observational study → association only; experiment → can show <mark>causation</mark>.</li>
  <li>Good experiments need a control group, <strong>random assignment</strong>, and replication.</li>
  <li>Random assignment → causal claims; random selection → generalizing to a population.</li>
</ul>
""".strip(),
    },

    # ── 63 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-63: Margin of Error and Confidence Intervals",
        "category": "math",
        "summary": "Interpret a margin of error and a confidence interval, and know what raises or lowers the margin.",
        "content": """
<h2>SAT-63: Margin of Error and Confidence Intervals</h2>
<p><strong>Description:</strong> A survey result like "62% ± 3%" carries a <mark>margin of error</mark> because a
sample only estimates the true population value. This lesson explains how to read that range — the
<mark>confidence interval</mark> — and what makes the margin larger or smaller. You interpret these on the SAT;
you almost never compute them.</p>

<h3>What the margin of error means</h3>
<p>The <strong>margin of error</strong> tells you how far the true population value could reasonably be from your
sample estimate. "62% ± 3%" means the true percentage is plausibly between <strong>59% and 65%</strong>. That range
is the <mark>confidence interval</mark>. <em>(Oʻzbekcha: xatolik chegarasi — haqiqiy qiymat namuna natijasidan qancha uzoq boʻlishi mumkinligini koʻrsatadi.)</em></p>

<h3>Reading a confidence interval</h3>
<p>To build the interval, subtract and add the margin to the estimate: interval = estimate ± margin. Any value
inside the interval is plausible for the true value; values outside it are unlikely.
<em>(Oʻzbekcha: ishonch oraligʻi = baho ± xatolik chegarasi.)</em></p>

<h3>What changes the margin of error</h3>
<ul>
  <li><strong>Bigger sample size → smaller margin.</strong> More data means a more precise estimate.</li>
  <li><strong>Higher confidence level (e.g. 95% → 99%) → larger margin.</strong> To be more certain, you need a wider net.</li>
</ul>
<p>So a small margin of error usually signals a large sample. <em>(Oʻzbekcha: namuna qancha katta boʻlsa, xatolik chegarasi shuncha kichik boʻladi.)</em></p>

<h3>Worked Example 1 — build the interval</h3>
<p>A poll estimates 48% support with a margin of error of 4%. What is the confidence interval?</p>
<ul>
  <li>48% − 4% = 44%; 48% + 4% = 52%.</li>
  <li>Interval: <strong>44% to 52%</strong> — the true support is plausibly in this range.</li>
</ul>

<h3>Worked Example 2 — interpret a claim</h3>
<p>Using that 44%–52% interval, can the pollster be confident support is above 50%?</p>
<ul>
  <li>No. Since values like 45% and 49% are inside the interval, the true value could be below 50%.</li>
  <li>The data does <strong>not</strong> support "a majority supports it."</li>
</ul>
<p><em>(Oʻzbekcha: 50% dan past qiymatlar ham oraliqda boʻlgani uchun "koʻpchilik qoʻllaydi" deb boʻlmaydi.)</em></p>

<h3>Worked Example 3 — compare two surveys</h3>
<p>Survey A (500 people) reports ± 4%; Survey B (2,000 people) reports ± 2%. Which is more precise and why?</p>
<ul>
  <li>Survey B has the smaller margin, so it is <strong>more precise</strong> — its larger sample narrows the interval.</li>
</ul>
<blockquote>Tip: to halve a margin of error you generally need a much larger sample, not just a slightly bigger one.
<em>(Oʻzbekcha: xatolikni kichraytirish uchun namunani sezilarli kattalashtirish kerak.)</em></blockquote>

<h3>What a confidence interval does NOT mean</h3>
<p>Students often misread these. A "95% confidence interval of 44% to 52%" does <strong>not</strong> mean 95% of people
chose something, and it does not mean there is a 95% chance the true value is exactly the estimate. It means the method
is reliable enough that intervals built this way capture the true population value most of the time. For the SAT, the
safe interpretation is simply: "the true value is plausibly anywhere in this range." Any answer choice that states a
single exact value as certain is wrong. <em>(Oʻzbekcha: ishonch oraligʻi — haqiqiy qiymat shu oraliqda boʻlishi ehtimoli yuqori degani; aniq bitta songa kafolat bermaydi.)</em></p>

<h3>Two intervals that overlap</h3>
<p>If two groups' confidence intervals <strong>overlap</strong>, you cannot conclude they are truly different — the
difference might just be sampling error. If the intervals do <strong>not</strong> overlap, the difference is more
convincing. This overlap idea is a common SAT reasoning question. <em>(Oʻzbekcha: ikki oraliq kesishsa, farq ishonchli emas; kesishmasa, farq haqiqiyroq.)</em></p>

<h3>Practice 1</h3>
<p>An estimate is 30% with a margin of error of 5%. Give the confidence interval.</p>
<details>
  <summary>Show answer</summary>
  <p>30% ± 5% → <strong>25% to 35%</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>A researcher wants a smaller margin of error without lowering the confidence level. What should change?</p>
<details>
  <summary>Show answer</summary>
  <p><strong>Increase the sample size.</strong> A larger sample reduces the margin while keeping the same confidence level.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Margin of error</strong> — xatolik chegarasi</li>
  <li><strong>Confidence interval</strong> — ishonch oraligʻi</li>
  <li><strong>Confidence level</strong> — ishonch darajasi</li>
  <li><strong>Estimate</strong> — baho (taxminiy qiymat)</li>
  <li><strong>Sample size</strong> — namuna hajmi</li>
  <li><strong>Precise</strong> — aniq</li>
  <li><strong>Plausible</strong> — ehtimoli bor</li>
  <li><strong>True value</strong> — haqiqiy qiymat</li>
  <li><strong>Population</strong> — populyatsiya</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Confidence interval = <mark>estimate ± margin of error</mark>; any value inside is plausible.</li>
  <li>Larger sample → smaller margin; higher confidence level → larger margin.</li>
  <li>You can only claim "above X" if the whole interval lies above X.</li>
</ul>
""".strip(),
    },

    # ── 64 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-64: Comparing Data Sets — Boxplots and Histograms",
        "category": "math",
        "summary": "Read the five-number summary from a boxplot and shape from a histogram, then compare two data sets.",
        "content": """
<h2>SAT-64: Comparing Data Sets — Boxplots and Histograms</h2>
<p><strong>Description:</strong> Two graphs summarize a whole data set at a glance: the <mark>boxplot</mark> shows
its five key numbers and spread, and the <mark>histogram</mark> shows its shape. The SAT asks you to read each and
to compare two data sets using center and spread.</p>

<h3>The boxplot (box-and-whisker)</h3>
<p>A boxplot is built from the <strong>five-number summary</strong>:</p>
<ul>
  <li><strong>Minimum</strong> and <strong>Maximum</strong> — the ends of the whiskers.</li>
  <li><strong>Q1, Median (Q2), Q3</strong> — the quartiles that form the box.</li>
  <li><strong>IQR = Q3 − Q1</strong>, the interquartile range, is the width of the box (the middle 50% of the data).</li>
</ul>
<p>The line inside the box is the median; a longer box or whisker means more spread on that side.
<em>(Oʻzbekcha: quti-diagramma besh asosiy sonni koʻrsatadi: min, Q1, median, Q3, max.)</em></p>

<h3>The histogram (shape)</h3>
<p>A histogram groups data into intervals and draws a bar for how many values fall in each. Its <strong>shape</strong>
tells the story:</p>
<ul>
  <li><strong>Symmetric:</strong> roughly a mirror image; mean ≈ median.</li>
  <li><strong>Skewed right:</strong> a long tail of large values pulls the mean above the median.</li>
  <li><strong>Skewed left:</strong> a long tail of small values pulls the mean below the median.</li>
</ul>
<p><em>(Oʻzbekcha: gistogramma maʼlumotlarning shaklini koʻrsatadi — simmetrik yoki bir tomonga choʻzilgan.)</em></p>

<h3>Worked Example 1 — read a boxplot</h3>
<p>A boxplot shows min 20, Q1 35, median 50, Q3 65, max 90. Find the IQR and the range.</p>
<ul>
  <li>IQR = Q3 − Q1 = 65 − 35 = <strong>30</strong>.</li>
  <li>Range = max − min = 90 − 20 = <strong>70</strong>.</li>
</ul>

<h3>Worked Example 2 — interpret quartiles</h3>
<p>Using that boxplot, about what percent of the data is below 35, and what percent is between 35 and 65?</p>
<ul>
  <li>Q1 = 35 marks the bottom 25%, so about <strong>25%</strong> is below 35.</li>
  <li>From Q1 to Q3 is the middle <strong>50%</strong> of the data (between 35 and 65).</li>
</ul>
<p><em>(Oʻzbekcha: Q1 — pastki 25%, Q1 dan Q3 gacha — oʻrtadagi 50%.)</em></p>

<h3>Worked Example 3 — compare with a histogram's shape</h3>
<p>A histogram of house prices has a long right tail. Is the mean or median larger, and which is more typical?</p>
<ul>
  <li>Right-skewed → the mean is pulled up by the expensive houses, so <strong>mean &gt; median</strong>.</li>
  <li>The <strong>median</strong> is the more typical price.</li>
</ul>
<blockquote>To compare two data sets, mention both <strong>center</strong> (median/mean) and <strong>spread</strong>
(IQR/range). "Set A has a higher median and a smaller IQR" is a complete comparison.
<em>(Oʻzbekcha: ikki toʻplamni taqqoslashda markazni ham, tarqoqlikni ham aytib oʻting.)</em></blockquote>

<h3>Why boxplots and histograms show different things</h3>
<p>These two graphs are not interchangeable. A <strong>histogram</strong> reveals the exact <em>shape</em> — whether the
data is symmetric, skewed, or even has two peaks — because you can see every interval's height. A <strong>boxplot</strong>
hides the shape but cleanly shows the <em>quartiles and spread</em>, which makes it ideal for comparing several data sets
side by side. So if a question asks about shape or peaks, look to the histogram; if it asks about medians, quartiles, or
which set is more spread out, look to the boxplot. Knowing which tool answers which question saves time.
<em>(Oʻzbekcha: gistogramma shaklni, quti-diagramma esa kvartillar va tarqoqlikni yaxshi koʻrsatadi.)</em></p>

<h3>Practice 1</h3>
<p>A boxplot has Q1 = 12 and Q3 = 28. What is the IQR, and what does it represent?</p>
<details>
  <summary>Show answer</summary>
  <p>IQR = 28 − 12 = <strong>16</strong>. It is the spread of the middle 50% of the data.</p>
</details>

<h3>Practice 2</h3>
<p>Histogram X is symmetric; histogram Y is skewed left. In which is the mean clearly below the median?</p>
<details>
  <summary>Show answer</summary>
  <p>In the <strong>left-skewed</strong> one (Y): the long low tail pulls the mean below the median. In the symmetric
  one, mean ≈ median.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Boxplot</strong> — quti-diagramma</li>
  <li><strong>Histogram</strong> — gistogramma</li>
  <li><strong>Five-number summary</strong> — besh sonli xulosa</li>
  <li><strong>Quartile (Q1, Q3)</strong> — kvartil</li>
  <li><strong>IQR (interquartile range)</strong> — kvartillararo oraliq</li>
  <li><strong>Skewed</strong> — bir tomonga choʻzilgan</li>
  <li><strong>Symmetric</strong> — simmetrik</li>
  <li><strong>Spread</strong> — tarqoqlik</li>
  <li><strong>Center</strong> — markaz (oʻrta)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Boxplot shows the <mark>five-number summary</mark>; IQR = Q3 − Q1 = middle 50%.</li>
  <li>Histogram shows shape: symmetric (mean ≈ median) or skewed (mean pulled toward the tail).</li>
  <li>Compare data sets with both <strong>center</strong> and <strong>spread</strong>.</li>
</ul>
""".strip(),
    },

    # ── 65 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-65: Linear vs. Exponential Data Modeling",
        "category": "math",
        "summary": "Choose the right model for real data — linear for constant change, exponential for constant percent change.",
        "content": """
<h2>SAT-65: Linear vs. Exponential Data Modeling</h2>
<p><strong>Description:</strong> This lesson ties together SAT-44 and SAT-54: given a table, graph, or description,
decide whether a <mark>linear</mark> model or an <mark>exponential</mark> model fits, and write it. Picking the
wrong model is a common SAT mistake, so the decision rule matters.</p>

<h3>The decision rule</h3>
<ul>
  <li>Change by a <strong>constant amount</strong> each step → <mark>linear</mark>, y = mx + b.</li>
  <li>Change by a <strong>constant percent/factor</strong> each step → <mark>exponential</mark>, y = a·b<sup>x</sup>.</li>
</ul>
<p><em>(Oʻzbekcha: bir xil son qoʻshilsa — chiziqli; bir xil foizga oʻzgarsa — eksponensial.)</em></p>

<h3>Diagnosing from a table</h3>
<p>Take the y-values in order. <strong>Subtract</strong> neighbors: if the differences are equal, it's linear.
<strong>Divide</strong> neighbors: if the ratios are equal, it's exponential. Do both checks before deciding.
<em>(Oʻzbekcha: qoʻshni qiymatlarni ayiring (chiziqli?) va boʻling (eksponensial?).)</em></p>

<h3>Diagnosing from a graph</h3>
<ul>
  <li>A straight line → linear.</li>
  <li>A curve that grows faster and faster (or decays toward zero without crossing) → exponential.</li>
</ul>

<h3>Worked Example 1 — table that is linear</h3>
<p>x: 0, 1, 2, 3 and y: 5, 8, 11, 14. Which model, and write it.</p>
<ul>
  <li>Differences: +3, +3, +3 → constant → <strong>linear</strong>.</li>
  <li>Slope m = 3, starting value b = 5 → <strong>y = 3x + 5</strong>.</li>
</ul>

<h3>Worked Example 2 — table that is exponential</h3>
<p>x: 0, 1, 2, 3 and y: 4, 12, 36, 108. Which model, and write it.</p>
<ul>
  <li>Differences: +8, +24, +72 (not constant). Ratios: 12/4 = 3, 36/12 = 3, 108/36 = 3 → constant → <strong>exponential</strong>.</li>
  <li>Start a = 4, factor b = 3 → <strong>y = 4·3<sup>x</sup></strong>.</li>
</ul>
<p><em>(Oʻzbekcha: nisbat doim 3 ga teng, demak eksponensial: y = 4·3^x.)</em></p>

<h3>Worked Example 3 — from a description</h3>
<p>"A pond's algae covers 50 m² and increases 20% each week." Linear or exponential? Write it.</p>
<ul>
  <li>"Increases 20% each week" = constant percent → <strong>exponential</strong>.</li>
  <li>a = 50, b = 1 + 0.20 = 1.2 → <strong>y = 50·(1.2)<sup>x</sup></strong>.</li>
</ul>
<blockquote>Watch the words: "per year/week" with a fixed <em>amount</em> → linear; with a fixed <em>percent</em> →
exponential. <em>(Oʻzbekcha: aniq son qoʻshilsa — chiziqli; foiz boʻlsa — eksponensial.)</em></blockquote>

<h3>Why the models look so different far out</h3>
<p>Near the start, a linear and an exponential model can look almost the same — both rise gently. The difference shows
up <em>later</em>: a linear model keeps adding the same step forever, so its graph is a straight line, while an
exponential model keeps multiplying, so it eventually shoots up far steeper (or, for decay, flattens toward zero
without ever touching it). This is why "which model fits long-term growth like population or money?" is almost always
<strong>exponential</strong>, and why a constant hourly wage or a fixed monthly fee is <strong>linear</strong>.
<em>(Oʻzbekcha: boshida ikkala model oʻxshash koʻrinadi, lekin keyinroq eksponensial ancha tikroq oʻsadi.)</em></p>

<h3>Watch out for "starting value" wording</h3>
<p>The constant term carries different names in word problems: "starting amount," "initial value," "flat fee," or
"value when x = 0." In a linear model it is the b in y = mx + b; in an exponential model it is the a in y = a·b<sup>x</sup>.
Identifying it first makes writing the model much faster. <em>(Oʻzbekcha: "boshlangʻich qiymat" — chiziqlida b, eksponensialda a boʻladi.)</em></p>

<h3>Practice 1</h3>
<p>A gym charges a $40 joining fee plus $25 per month. Linear or exponential? Write the cost after x months.</p>
<details>
  <summary>Show answer</summary>
  <p>Constant $25 added per month → <strong>linear</strong>: y = 25x + 40.</p>
</details>

<h3>Practice 2</h3>
<p>A car worth $30,000 loses 10% of its value each year. Linear or exponential? Write the value after x years.</p>
<details>
  <summary>Show answer</summary>
  <p>Constant percent loss → <strong>exponential</strong>: y = 30000·(0.9)<sup>x</sup>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Model</strong> — model</li>
  <li><strong>Linear</strong> — chiziqli</li>
  <li><strong>Exponential</strong> — eksponensial</li>
  <li><strong>Constant difference</strong> — oʻzgarmas ayirma</li>
  <li><strong>Constant ratio</strong> — oʻzgarmas nisbat</li>
  <li><strong>Slope</strong> — nishab</li>
  <li><strong>Growth factor</strong> — oʻsish koeffitsiyenti</li>
  <li><strong>Per (year/month)</strong> — har (yili/oyda)</li>
  <li><strong>Fit</strong> — moslashtirish (mos kelishi)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Constant <strong>amount</strong> of change → <mark>linear</mark> (y = mx + b).</li>
  <li>Constant <strong>percent/factor</strong> of change → <mark>exponential</mark> (y = a·b<sup>x</sup>).</li>
  <li>From a table: equal differences → linear; equal ratios → exponential.</li>
</ul>
""".strip(),
    },

    # ── 66 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-66: Lines and Angles — Vertical, Supplementary, and Complementary",
        "category": "math",
        "summary": "Use vertical, supplementary (180°), and complementary (90°) angle relationships to solve for unknowns.",
        "content": """
<h2>SAT-66: Lines and Angles — Vertical, Supplementary, and Complementary</h2>
<p><strong>Description:</strong> Geometry on the SAT starts with angle relationships at lines and points. Three
relationships solve a huge share of problems: <mark>vertical</mark>, <mark>supplementary</mark>, and
<mark>complementary</mark> angles. Master these and you can set up equations for almost any figure.</p>

<h3>Supplementary angles (straight line = 180°)</h3>
<p>Two angles that form a straight line add to <strong>180°</strong>. They are called supplementary.
<em>(Oʻzbekcha: toʻgʻri chiziq hosil qiluvchi ikki burchak yigʻindisi 180° ga teng.)</em></p>

<h3>Complementary angles (right angle = 90°)</h3>
<p>Two angles that together form a right angle add to <strong>90°</strong>. They are complementary.
<em>(Oʻzbekcha: birgalikda toʻgʻri burchak hosil qiluvchi burchaklar 90° ga teng.)</em></p>

<h3>Vertical angles (the X)</h3>
<p>When two lines cross, the angles <em>opposite</em> each other are <mark>vertical angles</mark>, and they are always
<strong>equal</strong>. The two angles next to each other on a line are supplementary.
<em>(Oʻzbekcha: ikki chiziq kesishganda qarama-qarshi burchaklar (vertikal) oʻzaro teng boʻladi.)</em></p>

<h3>Worked Example 1 — supplementary</h3>
<p>Two angles on a straight line are (2x) and (x + 30). Find x.</p>
<ul>
  <li>They add to 180: 2x + (x + 30) = 180 → 3x + 30 = 180 → 3x = 150 → <strong>x = 50</strong>.</li>
</ul>

<h3>Worked Example 2 — complementary</h3>
<p>Two complementary angles are (3x) and (x + 10). Find each angle.</p>
<ul>
  <li>They add to 90: 3x + x + 10 = 90 → 4x = 80 → x = 20.</li>
  <li>Angles: 3(20) = <strong>60°</strong> and 20 + 10 = <strong>30°</strong> (and 60 + 30 = 90 ✓).</li>
</ul>
<p><em>(Oʻzbekcha: ikkala burchak yigʻindisi 90° boʻlishi kerak.)</em></p>

<h3>Worked Example 3 — vertical + supplementary together</h3>
<p>Two lines cross. One angle is 110°. Find its vertical angle and an adjacent angle.</p>
<ul>
  <li>Vertical angle (opposite) = <strong>110°</strong> (equal).</li>
  <li>Adjacent angle (on the line) = 180 − 110 = <strong>70°</strong> (supplementary).</li>
</ul>
<blockquote>Strategy: label what you know, then write "these add to 180" or "these are equal." Most SAT angle
problems are just one linear equation. <em>(Oʻzbekcha: bilganingizni belgilang, soʻng tenglama tuzing — koʻpincha bitta chiziqli tenglama yetarli.)</em></blockquote>

<h3>Worked Example 4 — angles around a point</h3>
<p>Three angles meet at a single point and go all the way around: (2x)°, (3x)°, and (4x)°. Find x.</p>
<ul>
  <li>Angles around a point add to 360°: 2x + 3x + 4x = 360 → 9x = 360 → <strong>x = 40</strong>.</li>
</ul>
<p>This is the fourth key fact: a full turn around a point is 360°, while a straight line is only 180°.
<em>(Oʻzbekcha: nuqta atrofidagi burchaklar yigʻindisi 360°, toʻgʻri chiziqdagi esa 180°.)</em></p>

<h3>Don't trust the picture — trust the numbers</h3>
<p>SAT figures are usually drawn close to scale, but they are <em>not</em> guaranteed to be exact unless the problem
says "figure drawn to scale." An angle that looks like 90° might be 88°. So never measure with your eye and assume;
use the stated values and the angle rules to write an equation. The picture is a guide for setting up, not a source
of measurements. <em>(Oʻzbekcha: rasmga ishonib oʻlchamang — berilgan sonlar va qoidalar asosida tenglama tuzing.)</em></p>

<h3>Practice 1</h3>
<p>An angle is 4 times its supplement. Find the angle.</p>
<details>
  <summary>Show answer</summary>
  <p>Let the supplement be x; the angle is 4x. Then x + 4x = 180 → 5x = 180 → x = 36. The angle = 4(36) = <strong>144°</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Two lines intersect; one of the four angles is (5x − 5)° and the angle vertical to it is 70°. Find x.</p>
<details>
  <summary>Show answer</summary>
  <p>Vertical angles are equal: 5x − 5 = 70 → 5x = 75 → <strong>x = 15</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Angle</strong> — burchak</li>
  <li><strong>Vertical angles</strong> — vertikal burchaklar</li>
  <li><strong>Supplementary</strong> — qoʻshni (yigʻindisi 180°)</li>
  <li><strong>Complementary</strong> — toʻldiruvchi (yigʻindisi 90°)</li>
  <li><strong>Straight line</strong> — toʻgʻri chiziq</li>
  <li><strong>Right angle</strong> — toʻgʻri burchak</li>
  <li><strong>Adjacent</strong> — yondosh</li>
  <li><strong>Intersect</strong> — kesishish</li>
  <li><strong>Degree (°)</strong> — gradus</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Supplementary angles add to <mark>180°</mark> (straight line); complementary add to <mark>90°</mark>.</li>
  <li>Vertical (opposite) angles are <strong>equal</strong>.</li>
  <li>Translate the relationship into one equation and solve.</li>
</ul>
""".strip(),
    },

    # ── 67 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-67: Parallel Lines Cut by a Transversal",
        "category": "math",
        "summary": "Find every angle when a transversal crosses parallel lines using corresponding and alternate angles.",
        "content": """
<h2>SAT-67: Parallel Lines Cut by a Transversal</h2>
<p><strong>Description:</strong> When a third line (a <mark>transversal</mark>) crosses two <mark>parallel lines</mark>,
eight angles appear — but only two different sizes. Knowing the angle pairs lets you find them all from a single
known angle. This is one of the most common SAT geometry setups.</p>

<h3>The big idea: only two angle sizes</h3>
<p>With parallel lines, every angle is either equal to your known angle or supplementary to it (adds to 180°). So
once you know one angle, you know all eight. <em>(Oʻzbekcha: parallel chiziqlarda barcha burchaklar yo teng, yo 180° ga toʻldiruvchi boʻladi.)</em></p>

<h3>The angle pairs to recognize</h3>
<ul>
  <li><strong>Corresponding angles</strong> (same position at each intersection) → <mark>equal</mark>.</li>
  <li><strong>Alternate interior angles</strong> (between the lines, opposite sides of the transversal) → <mark>equal</mark>.</li>
  <li><strong>Alternate exterior angles</strong> (outside the lines, opposite sides) → <mark>equal</mark>.</li>
  <li><strong>Co-interior / same-side interior angles</strong> (between the lines, same side) → <mark>supplementary</mark> (180°).</li>
</ul>
<p><em>(Oʻzbekcha: mos burchaklar va almashinuvchi ichki burchaklar teng; bir tomonli ichki burchaklar 180° ga teng.)</em></p>

<h3>Worked Example 1 — corresponding angles</h3>
<p>A transversal crosses two parallel lines. One angle is 75°. Find its corresponding angle at the other line.</p>
<ul>
  <li>Corresponding angles are equal → the matching angle is also <strong>75°</strong>.</li>
</ul>

<h3>Worked Example 2 — same-side interior</h3>
<p>One interior angle is 120°. Find the same-side interior angle (between the lines, same side of the transversal).</p>
<ul>
  <li>Same-side interior angles are supplementary: 180 − 120 = <strong>60°</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: bir tomonli ichki burchaklar yigʻindisi 180° ga teng.)</em></p>

<h3>Worked Example 3 — solve for x</h3>
<p>Two parallel lines are cut by a transversal. Alternate interior angles are (2x + 10)° and (3x − 20)°. Find x and the angle.</p>
<ul>
  <li>Alternate interior angles are equal: 2x + 10 = 3x − 20 → 30 = x → <strong>x = 30</strong>.</li>
  <li>Angle = 2(30) + 10 = <strong>70°</strong> (check: 3(30) − 20 = 70 ✓).</li>
</ul>
<blockquote>Shortcut: in these figures every angle is one of just two values, A or 180 − A. Find which group each
angle is in. <em>(Oʻzbekcha: har bir burchak yoki A, yoki 180 − A boʻladi — qaysi guruhdaligini aniqlang.)</em></blockquote>

<h3>Worked Example 4 — supplementary pair to solve x</h3>
<p>Same-side interior angles are (3x)° and (x + 40)°. Find x.</p>
<ul>
  <li>Same-side interior angles add to 180: 3x + (x + 40) = 180 → 4x + 40 = 180 → 4x = 140 → <strong>x = 35</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: bir tomonli ichki burchaklar 180° ga teng, shuning uchun ularni qoʻshib tenglama tuzamiz.)</em></p>

<h3>How to tell "equal" from "supplementary" fast</h3>
<p>You don't have to memorize every pair name under pressure. Use this quick test: if the two angles
<strong>look</strong> about the same size, they are <em>equal</em>; if one looks sharp (acute) and the other wide
(obtuse), they are <em>supplementary</em> and add to 180°. The SAT figures are drawn roughly to scale, so this visual
check almost always confirms which rule to use — then back it up with the pair name.
<em>(Oʻzbekcha: ikki burchak bir xil koʻrinsa — teng; biri oʻtkir, biri keng koʻrinsa — yigʻindisi 180°.)</em></p>

<h3>The converse (proving lines are parallel)</h3>
<p>The relationships also run backwards: if corresponding angles are equal (or same-side interior angles add to 180°),
then the two lines <strong>must be parallel</strong>. The SAT sometimes gives the angles and asks whether the lines are
parallel — check the pair. <em>(Oʻzbekcha: agar mos burchaklar teng boʻlsa, chiziqlar parallel boʻladi.)</em></p>

<h3>Practice 1</h3>
<p>A transversal crosses two parallel lines; one angle is 65°. What is its alternate exterior angle?</p>
<details>
  <summary>Show answer</summary>
  <p>Alternate exterior angles are equal → <strong>65°</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Corresponding angles are (4x)° and (x + 60)°. Find x.</p>
<details>
  <summary>Show answer</summary>
  <p>Corresponding angles are equal: 4x = x + 60 → 3x = 60 → <strong>x = 20</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Parallel lines</strong> — parallel chiziqlar</li>
  <li><strong>Transversal</strong> — kesuvchi chiziq</li>
  <li><strong>Corresponding angles</strong> — mos burchaklar</li>
  <li><strong>Alternate interior</strong> — almashinuvchi ichki</li>
  <li><strong>Alternate exterior</strong> — almashinuvchi tashqi</li>
  <li><strong>Same-side interior</strong> — bir tomonli ichki</li>
  <li><strong>Interior / Exterior</strong> — ichki / tashqi</li>
  <li><strong>Equal</strong> — teng</li>
  <li><strong>Supplementary</strong> — yigʻindisi 180°</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>A transversal across parallel lines makes only <mark>two angle sizes</mark>.</li>
  <li>Corresponding, alternate interior, and alternate exterior angles are <strong>equal</strong>.</li>
  <li>Same-side interior angles are <strong>supplementary</strong> (180°).</li>
</ul>
""".strip(),
    },

    # ── 68 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-68: Triangles — Interior and Exterior Angle Theorems",
        "category": "math",
        "summary": "Use the 180° interior-angle sum and the exterior-angle theorem to find unknown triangle angles.",
        "content": """
<h2>SAT-68: Triangles — Interior and Exterior Angle Theorems</h2>
<p><strong>Description:</strong> Two theorems unlock most triangle-angle problems: the three interior angles always
sum to <mark>180°</mark>, and an <mark>exterior angle</mark> equals the sum of the two non-adjacent interior angles.
Together they let you find any missing angle.</p>

<h3>Interior Angle Theorem</h3>
<blockquote>The three interior angles of any triangle add up to <strong>180°</strong>.</blockquote>
<p>This holds for every triangle, no matter its shape. <em>(Oʻzbekcha: istalgan uchburchakning uchta ichki burchagi yigʻindisi 180° ga teng.)</em></p>

<h3>Exterior Angle Theorem</h3>
<p>If you extend one side of a triangle, the <mark>exterior angle</mark> formed equals the <strong>sum of the two
interior angles not next to it</strong> (the "remote" interior angles). It also makes a straight line with its own
interior angle, so they are supplementary. <em>(Oʻzbekcha: tashqi burchak unga qoʻshni boʻlmagan ikki ichki burchak yigʻindisiga teng.)</em></p>

<h3>Worked Example 1 — find the third angle</h3>
<p>A triangle has angles 50° and 70°. Find the third.</p>
<ul>
  <li>Sum is 180: third = 180 − 50 − 70 = <strong>60°</strong>.</li>
</ul>

<h3>Worked Example 2 — solve with variables</h3>
<p>A triangle's angles are x, 2x, and 3x. Find each angle.</p>
<ul>
  <li>x + 2x + 3x = 180 → 6x = 180 → x = 30.</li>
  <li>Angles: <strong>30°, 60°, 90°</strong> (a right triangle).</li>
</ul>
<p><em>(Oʻzbekcha: barcha burchaklarni qoʻshib 180° ga tenglaymiz.)</em></p>

<h3>Worked Example 3 — exterior angle theorem</h3>
<p>An exterior angle of a triangle measures 120°. The two remote interior angles are equal. Find each.</p>
<ul>
  <li>Exterior = sum of the two remote interior angles: 120 = a + a = 2a → a = <strong>60°</strong> each.</li>
  <li>Check: the adjacent interior angle is 180 − 120 = 60°, and 60 + 60 + 60 = 180 ✓.</li>
</ul>
<blockquote>Shortcut: the exterior angle gives you the sum of the two far angles instantly — no need to find the
adjacent angle first. <em>(Oʻzbekcha: tashqi burchak ikki uzoq burchak yigʻindisini darhol beradi.)</em></blockquote>

<h3>Worked Example 4 — combine with isosceles facts</h3>
<p>A triangle has two equal sides and the angle between the two equal sides (the vertex) is 80°. Find the other two angles.</p>
<ul>
  <li>Equal sides mean the two base angles are equal; call each b.</li>
  <li>Angle sum: 80 + b + b = 180 → 2b = 100 → <strong>b = 50°</strong> each.</li>
  <li>So the angles are 80°, 50°, 50° (and 80 + 50 + 50 = 180 ✓).</li>
</ul>
<p>This shows how the 180° rule teams up with side facts you will study next in SAT-69.
<em>(Oʻzbekcha: 180° qoidasi teng tomon faktlari bilan birga ishlaydi.)</em></p>

<h3>Why the exterior-angle theorem is true</h3>
<p>The exterior angle and its neighbouring interior angle form a straight line, so they add to 180°. But the three
interior angles also add to 180°. Subtracting the shared interior angle from both statements leaves: exterior angle =
the other two interior angles. That is the whole proof in one line — and it is why the theorem always holds.
<em>(Oʻzbekcha: tashqi burchak qoʻshni ichki burchak bilan 180° hosil qiladi; uchta ichki burchak ham 180°, shuning uchun tashqi = qolgan ikki ichki burchak.)</em></p>

<h3>Practice 1</h3>
<p>A right triangle has one angle of 35° (besides the 90°). Find the third angle.</p>
<details>
  <summary>Show answer</summary>
  <p>180 − 90 − 35 = <strong>55°</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>An exterior angle of a triangle is (2x + 10)° and the two remote interior angles are 40° and 70°. Find x.</p>
<details>
  <summary>Show answer</summary>
  <p>Exterior = sum of remotes: 2x + 10 = 40 + 70 = 110 → 2x = 100 → <strong>x = 50</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Triangle</strong> — uchburchak</li>
  <li><strong>Interior angle</strong> — ichki burchak</li>
  <li><strong>Exterior angle</strong> — tashqi burchak</li>
  <li><strong>Remote interior angles</strong> — uzoq (qoʻshni boʻlmagan) ichki burchaklar</li>
  <li><strong>Sum</strong> — yigʻindi</li>
  <li><strong>Right triangle</strong> — toʻgʻri burchakli uchburchak</li>
  <li><strong>Extend a side</strong> — tomonni davom ettirish</li>
  <li><strong>Adjacent</strong> — qoʻshni</li>
  <li><strong>Theorem</strong> — teorema</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Interior angles of a triangle sum to <mark>180°</mark>.</li>
  <li>An exterior angle = sum of the two <strong>remote</strong> interior angles.</li>
  <li>Set the relevant angles into one equation and solve.</li>
</ul>
""".strip(),
    },

    # ── 69 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-69: Isosceles and Equilateral Triangles",
        "category": "math",
        "summary": "Use the base-angles property of isosceles triangles and the all-60° rule of equilateral triangles.",
        "content": """
<h2>SAT-69: Isosceles and Equilateral Triangles</h2>
<p><strong>Description:</strong> Special triangles have special angle rules. An <mark>isosceles</mark> triangle has two
equal sides and two equal base angles; an <mark>equilateral</mark> triangle has all sides equal and all angles 60°.
These facts, combined with the 180° sum, solve many SAT figures quickly.</p>

<h3>Isosceles triangle</h3>
<p>An isosceles triangle has (at least) two equal sides. The angles <strong>opposite</strong> those equal sides — the
<mark>base angles</mark> — are also equal. So if you know one base angle, you know the other.
<em>(Oʻzbekcha: teng yonli uchburchakda teng tomonlar qarshisidagi burchaklar ham teng.)</em></p>

<h3>Equilateral triangle</h3>
<p>An equilateral triangle has all three sides equal, so all three angles are equal. Since they sum to 180°, each is
<strong>180 ÷ 3 = 60°</strong>. <em>(Oʻzbekcha: teng tomonli uchburchakda har bir burchak 60° ga teng.)</em></p>

<h3>The two-way connection (sides ↔ angles)</h3>
<p>Equal sides force equal angles, and equal angles force equal sides. So you can reason in either direction: spotting
two equal angles tells you two sides are equal, which can unlock a side length.
<em>(Oʻzbekcha: teng tomonlar → teng burchaklar va aksincha.)</em></p>

<h3>Worked Example 1 — find base angles</h3>
<p>An isosceles triangle has a vertex (top) angle of 40°. Find each base angle.</p>
<ul>
  <li>The two base angles are equal; call each b. Then 40 + b + b = 180 → 2b = 140 → <strong>b = 70°</strong> each.</li>
</ul>

<h3>Worked Example 2 — find the vertex angle</h3>
<p>An isosceles triangle has base angles of 55° each. Find the vertex angle.</p>
<ul>
  <li>Vertex = 180 − 55 − 55 = <strong>70°</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: uchidagi burchak = 180 − ikkita asos burchagi.)</em></p>

<h3>Worked Example 3 — equilateral with algebra</h3>
<p>A triangle has all sides equal, and one angle is labelled (5x)°. Find x.</p>
<ul>
  <li>Equilateral → every angle is 60°, so 5x = 60 → <strong>x = 12</strong>.</li>
</ul>
<blockquote>Tip: tick marks on a figure show equal sides; equal sides mean equal opposite angles. Always read the
tick marks. <em>(Oʻzbekcha: rasmda teng tomon belgisi (chiziqcha) boʻlsa, ularning qarshisidagi burchaklar teng.)</em></blockquote>

<h3>Worked Example 4 — use equal angles to find a side</h3>
<p>In triangle ABC, angle B = angle C = 65°, and side AB = 9. What can you say about side AC?</p>
<ul>
  <li>Equal angles force the opposite sides to be equal. Angle B is opposite AC and angle C is opposite AB.</li>
  <li>Since angle B = angle C, the sides opposite them are equal: AC = AB = <strong>9</strong>.</li>
</ul>
<p>This is the "reason backwards" direction — from equal angles to equal sides.
<em>(Oʻzbekcha: teng burchaklardan teng tomonlarga xulosa chiqaramiz.)</em></p>

<h3>A useful special case</h3>
<p>An equilateral triangle is also isosceles (all the rules still apply), and because every angle is 60°, it is the
only triangle that is also equiangular. On the SAT, spotting "all sides equal" instantly gives you three 60° angles —
and spotting "all angles 60°" instantly gives you three equal sides. Either clue unlocks the whole triangle.
<em>(Oʻzbekcha: teng tomonli uchburchak ham teng yonli; barcha burchaklari 60° boʻlgani uchun tomonlar ham teng.)</em></p>

<h3>Common mistake</h3>
<p>Don't assume a triangle is isosceles just because it <em>looks</em> like it. You need either equal tick marks on
the sides or two equal angles stated. Without one of those, the base-angle rule does not apply.
<em>(Oʻzbekcha: faqat koʻrinishiga qarab teng yonli deb hisoblamang — belgisi yoki teng burchaklari boʻlishi kerak.)</em></p>

<h3>Practice 1</h3>
<p>An isosceles triangle has a base angle of 48°. Find the vertex angle.</p>
<details>
  <summary>Show answer</summary>
  <p>Both base angles are 48°, so vertex = 180 − 48 − 48 = <strong>84°</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>In an isosceles triangle, the vertex angle is (2x)° and each base angle is (x + 30)°. Find x.</p>
<details>
  <summary>Show answer</summary>
  <p>2x + (x + 30) + (x + 30) = 180 → 4x + 60 = 180 → 4x = 120 → <strong>x = 30</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Isosceles triangle</strong> — teng yonli uchburchak</li>
  <li><strong>Equilateral triangle</strong> — teng tomonli uchburchak</li>
  <li><strong>Base angles</strong> — asos burchaklari</li>
  <li><strong>Vertex angle</strong> — uchidagi burchak</li>
  <li><strong>Equal sides</strong> — teng tomonlar</li>
  <li><strong>Opposite</strong> — qarshi (roʻparadagi)</li>
  <li><strong>Tick marks</strong> — tenglik belgilari</li>
  <li><strong>Congruent</strong> — teng (mos)</li>
  <li><strong>Angle sum</strong> — burchaklar yigʻindisi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Isosceles: two equal sides → two equal <mark>base angles</mark>.</li>
  <li>Equilateral: all sides equal → every angle is <mark>60°</mark>.</li>
  <li>Equal sides ↔ equal opposite angles (reason both ways), then use the 180° sum.</li>
</ul>
""".strip(),
    },

    # ── 70 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-70: Pythagorean Theorem and the Distance Formula",
        "category": "math",
        "summary": "Use a² + b² = c² for right triangles and apply it as the distance formula on the coordinate plane.",
        "content": """
<h2>SAT-70: Pythagorean Theorem and the Distance Formula</h2>
<p><strong>Description:</strong> The <mark>Pythagorean theorem</mark> relates the sides of a right triangle, and the
<mark>distance formula</mark> is the very same idea used to measure between two points on a graph. Both appear
constantly on the SAT.</p>

<h3>The Pythagorean theorem</h3>
<blockquote>For a right triangle with legs a and b and hypotenuse c (the side opposite the right angle):
<strong>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></strong>.</blockquote>
<p>The hypotenuse is always the longest side and sits across from the 90° angle.
<em>(Oʻzbekcha: gipotenuza — toʻgʻri burchak qarshisidagi eng uzun tomon.)</em></p>

<h3>Common Pythagorean triples (memorize these)</h3>
<p>Whole-number right triangles save time: <strong>3-4-5</strong>, <strong>5-12-13</strong>, <strong>8-15-17</strong>,
and their multiples (like 6-8-10). If you spot two of the numbers, you know the third.
<em>(Oʻzbekcha: 3-4-5, 5-12-13 kabi butun sonli uchliklarni yodlab oling — vaqt tejaydi.)</em></p>

<h3>The distance formula (same idea)</h3>
<p>The distance between points (x<sub>1</sub>, y<sub>1</sub>) and (x<sub>2</sub>, y<sub>2</sub>) is:</p>
<blockquote><strong>d = √((x<sub>2</sub> − x<sub>1</sub>)<sup>2</sup> + (y<sub>2</sub> − y<sub>1</sub>)<sup>2</sup>)</strong></blockquote>
<p>It is just the Pythagorean theorem where the horizontal and vertical gaps are the two legs.
<em>(Oʻzbekcha: masofa formulasi — bu aslida Pifagor teoremasi; gorizontal va vertikal farqlar — katetlar.)</em></p>

<h3>Worked Example 1 — find the hypotenuse</h3>
<p>A right triangle has legs 6 and 8. Find the hypotenuse.</p>
<ul>
  <li>c<sup>2</sup> = 6<sup>2</sup> + 8<sup>2</sup> = 36 + 64 = 100 → c = √100 = <strong>10</strong>. (It's a 6-8-10 triple.)</li>
</ul>

<h3>Worked Example 2 — find a leg</h3>
<p>A right triangle has hypotenuse 13 and one leg 5. Find the other leg.</p>
<ul>
  <li>5<sup>2</sup> + b<sup>2</sup> = 13<sup>2</sup> → 25 + b<sup>2</sup> = 169 → b<sup>2</sup> = 144 → b = <strong>12</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: kateteni topish uchun gipotenuza kvadratidan ma'lum katet kvadratini ayiramiz.)</em></p>

<h3>Worked Example 3 — distance on the plane</h3>
<p>Find the distance between (1, 2) and (4, 6).</p>
<ul>
  <li>Horizontal gap = 4 − 1 = 3; vertical gap = 6 − 2 = 4.</li>
  <li>d = √(3<sup>2</sup> + 4<sup>2</sup>) = √(9 + 16) = √25 = <strong>5</strong>.</li>
</ul>
<blockquote>Tip: sketch the two points, make a right triangle from the horizontal and vertical gaps, then use
a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>. <em>(Oʻzbekcha: ikki nuqtadan toʻgʻri burchakli uchburchak yasab, Pifagordan foydalaning.)</em></blockquote>

<h3>The converse — checking for a right angle</h3>
<p>The theorem also works backwards. If a triangle's sides satisfy a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup> (with c
the longest side), then the triangle <strong>must</strong> have a right angle. So if the SAT gives sides 9, 40, 41, you
can test 9<sup>2</sup> + 40<sup>2</sup> = 81 + 1600 = 1681 = 41<sup>2</sup> — yes, so it is a right triangle. This
converse is a quick way to confirm a right angle without measuring. <em>(Oʻzbekcha: agar a² + b² = c² boʻlsa, uchburchak toʻgʻri burchakli boʻladi — bu teskari teorema.)</em></p>

<h3>Common mistake — which side is the hypotenuse</h3>
<p>The formula only works if c is the hypotenuse (the longest side, opposite the right angle). If a problem gives you the
hypotenuse and asks for a leg, you must <em>subtract</em> (leg<sup>2</sup> = c<sup>2</sup> − other leg<sup>2</sup>), not
add. Adding when you should subtract is the most common error here, so always identify the hypotenuse first.
<em>(Oʻzbekcha: kateteni topishda qoʻshmaymiz, balki ayiramiz — avval gipotenuzani aniqlang.)</em></p>

<h3>Practice 1</h3>
<p>A right triangle has legs 9 and 12. Find the hypotenuse.</p>
<details>
  <summary>Show answer</summary>
  <p>c<sup>2</sup> = 81 + 144 = 225 → c = <strong>15</strong> (a 9-12-15 = 3·(3-4-5) triple).</p>
</details>

<h3>Practice 2</h3>
<p>Find the distance between (−2, 1) and (1, 5).</p>
<details>
  <summary>Show answer</summary>
  <p>Gaps: 1 − (−2) = 3, and 5 − 1 = 4. d = √(9 + 16) = √25 = <strong>5</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Pythagorean theorem</strong> — Pifagor teoremasi</li>
  <li><strong>Right triangle</strong> — toʻgʻri burchakli uchburchak</li>
  <li><strong>Leg</strong> — katet</li>
  <li><strong>Hypotenuse</strong> — gipotenuza</li>
  <li><strong>Square / Square root</strong> — kvadrat / kvadrat ildiz</li>
  <li><strong>Pythagorean triple</strong> — Pifagor uchligi</li>
  <li><strong>Distance formula</strong> — masofa formulasi</li>
  <li><strong>Coordinate plane</strong> — koordinata tekisligi</li>
  <li><strong>Horizontal / Vertical</strong> — gorizontal / vertikal</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Right triangle: <mark>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></mark>; the hypotenuse c is opposite the 90°.</li>
  <li>Know the triples 3-4-5, 5-12-13, 8-15-17 (and multiples) to save time.</li>
  <li>Distance formula is Pythagoras with legs (x₂ − x₁) and (y₂ − y₁).</li>
</ul>
""".strip(),
    },

    # ── 71 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-71: Special Right Triangles — 45-45-90",
        "category": "math",
        "summary": "Use the fixed side ratio 1 : 1 : √2 of a 45-45-90 triangle to find sides without the full theorem.",
        "content": """
<h2>SAT-71: Special Right Triangles — 45-45-90</h2>
<p><strong>Description:</strong> A <mark>45-45-90 triangle</mark> always has the same side ratio, so you can find any
side from one side instantly — no full Pythagorean calculation needed. It shows up in squares (cut along a diagonal)
all over the SAT.</p>

<h3>The fixed ratio</h3>
<blockquote>In a 45-45-90 triangle, the sides are in the ratio <strong>leg : leg : hypotenuse = 1 : 1 : √2</strong>.</blockquote>
<p>The two legs are equal (it's isosceles, because the two 45° angles are equal), and the hypotenuse is a leg times
√2. <em>(Oʻzbekcha: 45-45-90 uchburchakda ikki katet teng, gipotenuza esa katet × √2 ga teng.)</em></p>

<h3>Using the ratio both directions</h3>
<ul>
  <li><strong>Leg → hypotenuse:</strong> multiply the leg by √2.</li>
  <li><strong>Hypotenuse → leg:</strong> divide the hypotenuse by √2 (or multiply by √2 ÷ 2).</li>
</ul>
<p>This triangle is exactly half of a square cut along its diagonal, so the diagonal of a square with side s is s√2.
<em>(Oʻzbekcha: kvadratning diagonali tomoni × √2 ga teng.)</em></p>

<h3>Worked Example 1 — leg to hypotenuse</h3>
<p>A 45-45-90 triangle has legs of 5. Find the hypotenuse.</p>
<ul>
  <li>Hypotenuse = leg × √2 = <strong>5√2</strong>.</li>
</ul>

<h3>Worked Example 2 — hypotenuse to leg</h3>
<p>A 45-45-90 triangle has a hypotenuse of 10. Find each leg.</p>
<ul>
  <li>Leg = hypotenuse ÷ √2 = 10 ÷ √2 = 10√2 ÷ 2 = <strong>5√2</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: gipotenuzani √2 ga boʻlib, kateteni topamiz.)</em></p>

<h3>Worked Example 3 — diagonal of a square</h3>
<p>A square has side 7. Find the length of its diagonal.</p>
<ul>
  <li>The diagonal splits the square into two 45-45-90 triangles with legs 7.</li>
  <li>Diagonal = 7√2 ≈ <strong>9.9</strong>.</li>
</ul>
<blockquote>Tip: whenever you see a 45° angle or a square's diagonal, reach for the 1 : 1 : √2 ratio.
<em>(Oʻzbekcha: 45° burchak yoki kvadrat diagonali koʻrsangiz — 1 : 1 : √2 nisbatidan foydalaning.)</em></blockquote>

<h3>Worked Example 4 — area from the hypotenuse</h3>
<p>A 45-45-90 triangle has a hypotenuse of 8√2. Find its area.</p>
<ul>
  <li>First get a leg: leg = hypotenuse ÷ √2 = 8√2 ÷ √2 = 8.</li>
  <li>The two legs are perpendicular, so they are the base and height: area = ½ × 8 × 8 = <strong>32</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: avval kateteni toping, soʻng yuza = ½ × katet × katet.)</em></p>

<h3>Why the ratio works (quick proof)</h3>
<p>Take a 45-45-90 triangle with each leg = 1. By the Pythagorean theorem the hypotenuse is
√(1<sup>2</sup> + 1<sup>2</sup>) = √2. Scaling both legs to any length s scales the hypotenuse to s√2, which is
exactly the 1 : 1 : √2 ratio. So the ratio is just the Pythagorean theorem applied once and remembered — that is
why you never have to redo the square root. <em>(Oʻzbekcha: nisbat — bu bir marta hisoblangan Pifagor teoremasi, shuning uchun uni har safar qayta hisoblamaymiz.)</em></p>

<h3>Common mistake to avoid</h3>
<p>Students sometimes multiply the hypotenuse by √2 to get a leg — that is backwards and makes the triangle too big.
Remember the hypotenuse is the <em>longest</em> side, so going from hypotenuse to leg must make the number
<strong>smaller</strong> (you divide by √2). <em>(Oʻzbekcha: gipotenuza eng uzun tomon — undan kateteni topishda √2 ga boʻlinadi, koʻpaytirilmaydi.)</em></p>

<h3>Practice 1</h3>
<p>A 45-45-90 triangle has legs of 8. Find the hypotenuse.</p>
<details>
  <summary>Show answer</summary>
  <p>Hypotenuse = 8 × √2 = <strong>8√2</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>The diagonal of a square is 6√2. Find the side length of the square.</p>
<details>
  <summary>Show answer</summary>
  <p>Diagonal = side × √2, so side = 6√2 ÷ √2 = <strong>6</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>45-45-90 triangle</strong> — 45-45-90 uchburchak</li>
  <li><strong>Special right triangle</strong> — maxsus toʻgʻri burchakli uchburchak</li>
  <li><strong>Leg</strong> — katet</li>
  <li><strong>Hypotenuse</strong> — gipotenuza</li>
  <li><strong>Ratio</strong> — nisbat</li>
  <li><strong>Isosceles</strong> — teng yonli</li>
  <li><strong>Diagonal</strong> — diagonal</li>
  <li><strong>Square</strong> — kvadrat</li>
  <li><strong>√2 (radical)</strong> — √2 (ildiz)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>45-45-90 sides are in ratio <mark>1 : 1 : √2</mark>; the legs are equal.</li>
  <li>Leg → hypotenuse: ×√2; hypotenuse → leg: ÷√2.</li>
  <li>A square's diagonal = side × √2.</li>
</ul>
""".strip(),
    },
]
