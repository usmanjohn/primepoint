# SAT Math tutorials 52–61 (Percent change + Problem-Solving & Data Analysis: stats, probability, sampling)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_52_61.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 52 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-52: Percent Change — Increase, Decrease, and Successive Changes",
        "category": "math",
        "summary": "Compute percent increase/decrease, use multipliers, and chain successive percent changes correctly.",
        "content": """
<h2>SAT-52: Percent Change — Increase, Decrease, and Successive Changes</h2>
<p><strong>Description:</strong> In SAT-51 you found a part of a whole. This lesson is about how much a
quantity <em>changed</em> — a <mark>percent increase</mark> or <mark>percent decrease</mark> — and what
happens when several percent changes are applied one after another. This is one of the most tested
ideas in the whole "Problem Solving and Data" section, so it is worth mastering completely.</p>

<h3>The percent change formula</h3>
<blockquote><strong>percent change = (new − old) / old × 100%</strong></blockquote>
<p>The denominator is always the <strong>original</strong> amount (the "old" value), never the new one.
If the result is positive it is an increase; if negative it is a decrease.</p>
<p><em>(Oʻzbekcha: foiz oʻzgarishi har doim <strong>boshlangʻich</strong> (eski) qiymatga boʻlinadi, yangisiga emas.)</em></p>

<h3>The multiplier shortcut (faster and safer)</h3>
<p>Instead of finding the change and adding it back, multiply the original by a single number called the
<mark>multiplier</mark>:</p>
<ul>
  <li>Increase by r% → multiply by <strong>(1 + r/100)</strong>. Example: +20% → ×1.20.</li>
  <li>Decrease by r% → multiply by <strong>(1 − r/100)</strong>. Example: −15% → ×0.85.</li>
</ul>
<p>This is the same idea as the growth factor in SAT-45, and it makes successive changes easy.
<em>(Oʻzbekcha: oshirish uchun 1 + r/100 ga, kamaytirish uchun 1 − r/100 ga koʻpaytiramiz.)</em></p>

<h3>Worked Example 1 — basic increase</h3>
<p>A price rises from $40 to $50. What is the percent increase?</p>
<ul>
  <li>change = (50 − 40)/40 × 100% = 10/40 × 100% = <strong>25%</strong>.</li>
</ul>

<h3>Worked Example 2 — finding the new value with a multiplier</h3>
<p>A $120 jacket is discounted 30%. What is the sale price?</p>
<ul>
  <li>Decrease 30% → multiplier 0.70.</li>
  <li>120 × 0.70 = <strong>$84</strong>. (Faster than finding $36 off, then subtracting.)</li>
</ul>

<h3>Worked Example 3 — successive percent changes (the tricky one)</h3>
<p>A stock goes up 10%, then down 10%. Is it back to the start?</p>
<ul>
  <li>No! Multiply the multipliers: 1.10 × 0.90 = 0.99.</li>
  <li>So the final value is 99% of the original — a net <strong>1% loss</strong>.</li>
</ul>
<blockquote>Key idea: you <strong>multiply</strong> successive percent changes; you never just add or
subtract the percents. <em>(Oʻzbekcha: ketma-ket foizlarni qoʻshmaymiz — koʻpaytuvchilarni koʻpaytiramiz.)</em></blockquote>
<p><strong>Common mistake:</strong> thinking +10% then −10% cancels out. Each percent is taken of a
<em>different</em> base, so they don't.</p>

<h3>Choosing the right base</h3>
<p>The hardest part of percent-change problems is deciding what counts as the "old" value. The base is
whatever the change is measured <em>from</em>. "An increase <strong>from</strong> 40 to 50" makes 40 the base.
"50 is what percent <strong>more than</strong> 40?" also makes 40 the base. But "40 is what percent
<strong>less than</strong> 50?" switches the base to 50 — so the answer changes. Always underline the word
right after "than" or "from"; that is your denominator. This single habit prevents most percent-change errors
on the test. <em>(Oʻzbekcha: "than" yoki "from" soʻzidan keyingi son — bu maxraj (asos) boʻladi.)</em></p>

<h3>Practice 1</h3>
<p>A population falls from 800 to 600. What is the percent decrease?</p>
<details>
  <summary>Show answer</summary>
  <p>(600 − 800)/800 × 100% = −200/800 × 100% = <strong>−25%</strong>, i.e. a 25% decrease.</p>
</details>

<h3>Practice 2</h3>
<p>A $200 item is increased 25%, then that price is decreased 20%. Final price?</p>
<details>
  <summary>Show answer</summary>
  <p>200 × 1.25 × 0.80 = 200 × 1.00 = <strong>$200</strong>. (Here the changes happen to cancel — but only
  because 1.25 × 0.80 = 1, which you must check by multiplying, not by adding 25 − 20.)</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Percent change</strong> — foiz oʻzgarishi</li>
  <li><strong>Increase</strong> — oshish</li>
  <li><strong>Decrease</strong> — kamayish</li>
  <li><strong>Original (old) value</strong> — boshlangʻich (eski) qiymat</li>
  <li><strong>Multiplier</strong> — koʻpaytuvchi koeffitsiyent</li>
  <li><strong>Discount</strong> — chegirma</li>
  <li><strong>Successive</strong> — ketma-ket</li>
  <li><strong>Net change</strong> — yakuniy (sof) oʻzgarish</li>
  <li><strong>Sale price</strong> — chegirmali narx</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Percent change = <mark>(new − old)/old × 100%</mark> — always divide by the original.</li>
  <li>Use multipliers: +r% → ×(1 + r/100); −r% → ×(1 − r/100).</li>
  <li>For successive changes, <strong>multiply</strong> the multipliers; never add the percents.</li>
</ul>
""".strip(),
    },

    # ── 53 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-53: Interpreting Tables, Graphs, and Bar Charts",
        "category": "math",
        "summary": "Read values, totals, and trends from tables, line graphs, and bar charts — and avoid common reading traps.",
        "content": """
<h2>SAT-53: Interpreting Tables, Graphs, and Bar Charts</h2>
<p><strong>Description:</strong> A large part of the SAT is just <mark>reading data</mark> correctly from a
table or chart and doing a small calculation. No hard algebra — the points are lost mostly to careless
reading. This lesson trains you to read carefully and answer exactly what is asked.</p>

<h3>Always read the labels first</h3>
<p>Before touching the numbers, check three things:</p>
<ul>
  <li>The <strong>title</strong> — what is this data about?</li>
  <li>The <strong>axis labels and units</strong> — dollars? thousands? percent?</li>
  <li>The <strong>scale</strong> — does each gridline mean 1, 5, 10, or 100?</li>
</ul>
<p><em>(Oʻzbekcha: avval sarlavha, oʻq nomlari va birliklarni, hamda shkalani tekshiring — keyin sonlarga qarang.)</em></p>

<h3>Reading a table</h3>
<p>Find the correct <strong>row</strong> and <strong>column</strong> and read where they meet. For totals,
add a full row or column. Watch for a "Total" row/column that already does this for you.</p>

<h3>Worked Example 1 — table lookup and total</h3>
<p>A table lists books sold: Mon 12, Tue 8, Wed 15, Thu 10. How many over the four days, and what was the
daily average?</p>
<ul>
  <li>Total = 12 + 8 + 15 + 10 = <strong>45</strong> books.</li>
  <li>Average = 45 ÷ 4 = <strong>11.25</strong> books per day.</li>
</ul>

<h3>Reading a bar chart</h3>
<p>The <strong>height</strong> (or length) of each bar is its value. Compare bars by comparing heights; find
"how many more" by subtracting two heights. <em>(Oʻzbekcha: ustun balandligi — uning qiymati; farqni topish uchun ikki balandlikni ayiramiz.)</em></p>

<h3>Worked Example 2 — bar chart comparison</h3>
<p>A bar chart shows revenue: Store A = $30k, Store B = $45k, Store C = $25k. How much more did B make than C,
and what percent of the three-store total is that difference?</p>
<ul>
  <li>B − C = 45 − 25 = <strong>$20k</strong> more.</li>
  <li>Total = 30 + 45 + 25 = 100k. So 20/100 = <strong>20%</strong> of the total.</li>
</ul>

<h3>Reading a line graph (trends)</h3>
<p>A line that goes <strong>up</strong> means the quantity is increasing; <strong>down</strong> means
decreasing; <strong>flat</strong> means no change. The <em>steepness</em> shows how fast it changes.</p>

<h3>Worked Example 3 — line graph trend</h3>
<p>A temperature line reads 10°, 14°, 14°, 9° at 1pm, 2pm, 3pm, 4pm. When did it rise the fastest, and when
did it fall?</p>
<ul>
  <li>1→2pm: +4° (the only rise, and the steepest segment) — fastest rise here.</li>
  <li>2→3pm: flat (no change). 3→4pm: −5° — that is the fall.</li>
</ul>
<blockquote>Common mistake: confusing a steep line with a "high" value. Steepness = rate of change; height =
the actual value. <em>(Oʻzbekcha: chiziqning tikligi — oʻzgarish tezligi, balandligi esa — qiymatning oʻzi.)</em></blockquote>

<h3>A few reading traps to avoid</h3>
<p>Charts are designed to be misread under time pressure. Three traps show up again and again:</p>
<ul>
  <li><strong>Broken scales:</strong> a y-axis that starts at 50 instead of 0 makes small differences look huge.
  Always check where the axis begins before judging "how much bigger."</li>
  <li><strong>Units in the title:</strong> if a chart is "sales (in thousands)," a bar at 30 means 30,000, not 30.</li>
  <li><strong>Part vs whole:</strong> "what percent of the total" needs you to divide by the full total, not by a
  neighbouring bar.</li>
</ul>
<p>Reading the question twice and the labels once will catch nearly all of these.
<em>(Oʻzbekcha: shoshqaloqlikda eng koʻp xato shkalaning 0 dan boshlanmasligida va sarlavhadagi birliklarda boʻladi.)</em></p>

<h3>Practice 1</h3>
<p>From the books table above, what percent of the 45 books were sold on Wednesday?</p>
<details>
  <summary>Show answer</summary>
  <p>15 of 45 → 15/45 = 1/3 ≈ <strong>33.3%</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>In the revenue chart, Store A wants to match Store B. By what percent must A increase?</p>
<details>
  <summary>Show answer</summary>
  <p>Needs to go 30k → 45k. Increase = (45 − 30)/30 × 100% = 15/30 × 100% = <strong>50%</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Table</strong> — jadval</li>
  <li><strong>Bar chart</strong> — ustunli diagramma</li>
  <li><strong>Line graph</strong> — chiziqli grafik</li>
  <li><strong>Axis</strong> — oʻq</li>
  <li><strong>Scale</strong> — shkala (miqyos)</li>
  <li><strong>Label</strong> — yorliq (nom)</li>
  <li><strong>Row / Column</strong> — qator / ustun</li>
  <li><strong>Trend</strong> — yoʻnalish (tendensiya)</li>
  <li><strong>Total / Average</strong> — jami / oʻrtacha</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Read the <mark>title, units, and scale</mark> before the numbers.</li>
  <li>Table: find the row × column; add a row/column for totals.</li>
  <li>Bar height = value; line direction = trend, line steepness = rate of change.</li>
  <li>Answer exactly what is asked (value vs. difference vs. percent).</li>
</ul>
""".strip(),
    },

    # ── 54 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-54: Scatterplots — Lines of Best Fit and Trends",
        "category": "math",
        "summary": "Read scatterplots, describe correlation, and use a line of best fit to estimate and predict values.",
        "content": """
<h2>SAT-54: Scatterplots — Lines of Best Fit and Trends</h2>
<p><strong>Description:</strong> A <mark>scatterplot</mark> shows many (x, y) points to reveal a relationship
between two quantities. A <mark>line of best fit</mark> is a straight line drawn through the cloud of points
to summarize the trend. The SAT asks you to read the line, find its slope, and make predictions.</p>

<h3>Correlation — what the cloud is telling you</h3>
<ul>
  <li><strong>Positive correlation:</strong> as x goes up, y goes up (points rise left-to-right).</li>
  <li><strong>Negative correlation:</strong> as x goes up, y goes down (points fall).</li>
  <li><strong>No correlation:</strong> no clear pattern.</li>
</ul>
<p><em>(Oʻzbekcha: musbat bogʻlanish — x oshganda y ham oshadi; manfiy — x oshganda y kamayadi.)</em></p>

<h3>The line of best fit</h3>
<p>It is the straight line that comes <em>closest</em> to all the points (roughly equal points above and
below). You read it just like any line: it has a slope and a y-intercept, and its equation is
y = (slope)·x + (intercept). <em>(Oʻzbekcha: eng mos chiziq nuqtalarga eng yaqin oʻtadigan toʻgʻri chiziq.)</em></p>

<h3>What slope and intercept mean here</h3>
<ul>
  <li>The <strong>slope</strong> = how much y changes for each +1 in x (the rate, with units).</li>
  <li>The <strong>y-intercept</strong> = the predicted y when x = 0 (the starting value).</li>
</ul>

<h3>Worked Example 1 — describe the relationship</h3>
<p>A scatterplot of "hours studied" vs "test score" rises from lower-left to upper-right. Describe it.</p>
<ul>
  <li>As hours increase, score increases → <strong>positive correlation</strong>. More study tends to mean a higher score.</li>
</ul>

<h3>Worked Example 2 — interpret the slope</h3>
<p>A best-fit line is score = 5·(hours) + 60. What does the 5 mean, and the 60?</p>
<ul>
  <li>Slope 5: each extra hour of study predicts about <strong>5 more points</strong>.</li>
  <li>Intercept 60: a student who studies 0 hours is predicted to score <strong>60</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: nishab (5) — har bir qoʻshimcha soat uchun ball oʻzgarishi; kesma (60) — boshlangʻich qiymat.)</em></p>

<h3>Worked Example 3 — predict a value</h3>
<p>Using score = 5·(hours) + 60, predict the score for 4 hours.</p>
<ul>
  <li>score = 5(4) + 60 = 20 + 60 = <strong>80</strong>.</li>
</ul>
<blockquote>Interpolation (predicting inside the data range) is reliable; <strong>extrapolation</strong>
(far outside the range) is risky — the trend may not continue. <em>(Oʻzbekcha: maʼlumot oraligʻidan tashqarida bashorat qilish xavfli.)</em></blockquote>

<h3>Correlation is not causation</h3>
<p>This is one of the SAT's favorite ideas. A strong correlation means two quantities move together — it does
<strong>not</strong> prove that one <em>causes</em> the other. Ice-cream sales and drowning numbers rise together,
but ice cream doesn't cause drowning; hot weather drives both. So if a question asks what you can conclude from a
scatterplot, "there is an association/relationship" is safe, while "X causes Y" is usually a trap unless the data
came from a controlled experiment (see SAT-62). <em>(Oʻzbekcha: bogʻlanish (korrelyatsiya) sababiy bogʻlanishni isbotlamaydi — birga oʻzgarishi sabab degani emas.)</em></p>

<h3>Reading residuals (how good is the fit?)</h3>
<p>The vertical gap between a real data point and the best-fit line is called the <strong>residual</strong>. Small
residuals everywhere mean the line fits well; large, patterned residuals mean a straight line may be the wrong
model. You don't usually compute them, but knowing the word helps you read SAT answer choices.</p>

<h3>Practice 1</h3>
<p>A best-fit line is cost = 0.5·(miles) + 3 for a taxi. What does the 0.5 mean?</p>
<details>
  <summary>Show answer</summary>
  <p>Each additional mile adds about <strong>$0.50</strong> to the cost (the per-mile rate). The $3 is the base fare at 0 miles.</p>
</details>

<h3>Practice 2</h3>
<p>With cost = 0.5·(miles) + 3, what is the predicted cost of a 10-mile ride?</p>
<details>
  <summary>Show answer</summary>
  <p>cost = 0.5(10) + 3 = 5 + 3 = <strong>$8</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Scatterplot</strong> — sochma diagramma</li>
  <li><strong>Line of best fit</strong> — eng mos chiziq</li>
  <li><strong>Correlation</strong> — bogʻlanish (korrelyatsiya)</li>
  <li><strong>Positive / Negative</strong> — musbat / manfiy</li>
  <li><strong>Slope</strong> — nishab</li>
  <li><strong>y-intercept</strong> — y-kesishma</li>
  <li><strong>Predict / Estimate</strong> — bashorat qilish / baholash</li>
  <li><strong>Trend</strong> — yoʻnalish (tendensiya)</li>
  <li><strong>Extrapolation</strong> — chegaradan tashqari bashorat</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Scatterplots show correlation: <mark>positive</mark> (up), <mark>negative</mark> (down), or none.</li>
  <li>The line of best fit summarizes the trend; slope = rate, intercept = value at x = 0.</li>
  <li>Plug an x into the line's equation to predict y; be cautious extrapolating far outside the data.</li>
</ul>
""".strip(),
    },

    # ── 55 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-55: Descriptive Statistics — Mean and Median",
        "category": "math",
        "summary": "Compute and compare the mean and median, work backward from a known mean, and know which is better with skewed data.",
        "content": """
<h2>SAT-55: Descriptive Statistics — Mean and Median</h2>
<p><strong>Description:</strong> The <mark>mean</mark> (average) and the <mark>median</mark> (middle value) are
the two main "center" measures on the SAT. You must compute each, reverse the mean to find a missing value,
and know when one is more trustworthy than the other.</p>

<h3>Mean (average)</h3>
<blockquote><strong>mean = (sum of all values) ÷ (how many values)</strong></blockquote>
<p>The mean uses every number, so it is sensitive to extreme values.
<em>(Oʻzbekcha: oʻrtacha — barcha qiymatlar yigʻindisini ularning soniga boʻlamiz.)</em></p>

<h3>Median (middle)</h3>
<p>First <strong>sort the values</strong> from low to high, then take the middle one. If there is an even
count, the median is the <em>average of the two middle values</em>. <em>(Oʻzbekcha: median — saralangan qatorning oʻrtasidagi qiymat.)</em></p>

<h3>Worked Example 1 — both measures</h3>
<p>Find the mean and median of 4, 8, 6, 10, 7.</p>
<ul>
  <li>Mean = (4 + 8 + 6 + 10 + 7) ÷ 5 = 35 ÷ 5 = <strong>7</strong>.</li>
  <li>Sorted: 4, 6, 7, 8, 10 → middle value = <strong>7</strong> (median).</li>
</ul>

<h3>Worked Example 2 — even count median</h3>
<p>Find the median of 3, 9, 5, 12.</p>
<ul>
  <li>Sorted: 3, 5, 9, 12. Two middle values are 5 and 9.</li>
  <li>Median = (5 + 9) ÷ 2 = <strong>7</strong>.</li>
</ul>

<h3>Worked Example 3 — work backward from the mean</h3>
<p>The mean of 5 test scores is 82. Four of them are 78, 85, 90, and 80. Find the fifth.</p>
<ul>
  <li>Total needed = mean × count = 82 × 5 = 410.</li>
  <li>Sum of the four known = 78 + 85 + 90 + 80 = 333.</li>
  <li>Fifth score = 410 − 333 = <strong>77</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: oʻrtachadan teskari ishlash uchun avval umumiy yigʻindini topamiz: oʻrtacha × son.)</em></p>

<h3>Mean vs median — which to trust</h3>
<p>An <mark>outlier</mark> (an unusually large or small value) drags the mean toward it but barely moves the
median. So for <strong>skewed</strong> data (like incomes, where a few huge values exist), the median is the
better "typical" value.</p>
<blockquote>Rule of thumb: symmetric data → mean ≈ median; strongly skewed data → trust the median.
<em>(Oʻzbekcha: kuchli nosimmetrik maʼlumotlarda medianga ishonish toʻgʻriroq.)</em></blockquote>

<h3>How adding or changing a value shifts the center</h3>
<p>The SAT often changes one number and asks how the mean and median respond. Two facts make this easy:</p>
<ul>
  <li>The <strong>mean</strong> reacts to <em>every</em> change — making any value bigger raises the mean, even a
  little. So if you add a value above the current mean, the mean goes up; below it, the mean goes down.</li>
  <li>The <strong>median</strong> only cares about <em>position</em>. Changing an extreme value to something even
  more extreme often leaves the median exactly where it was, because the middle position hasn't moved.</li>
</ul>
<p>Knowing this, you can frequently answer "what happens to the mean/median?" questions without recomputing
anything from scratch. <em>(Oʻzbekcha: oʻrtacha har qanday oʻzgarishga taʼsirchan, median esa faqat oʻrtadagi oʻringa bogʻliq.)</em></p>

<h3>Practice 1</h3>
<p>The mean of 6 numbers is 10. If five of them sum to 52, what is the sixth?</p>
<details>
  <summary>Show answer</summary>
  <p>Total = 10 × 6 = 60. Sixth = 60 − 52 = <strong>8</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>A data set is 2, 3, 3, 4, 100. Which is more typical of the data, the mean or the median, and why?</p>
<details>
  <summary>Show answer</summary>
  <p>Mean = 112 ÷ 5 = 22.4; median = 3. The 100 is an outlier that inflates the mean, so the
  <strong>median (3)</strong> better represents a typical value.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Mean (average)</strong> — oʻrtacha qiymat</li>
  <li><strong>Median</strong> — median (oʻrta qiymat)</li>
  <li><strong>Sum</strong> — yigʻindi</li>
  <li><strong>Sort / Order</strong> — saralash / tartiblash</li>
  <li><strong>Outlier</strong> — chetga chiquvchi qiymat</li>
  <li><strong>Skewed</strong> — nosimmetrik (qiyshiq)</li>
  <li><strong>Symmetric</strong> — simmetrik</li>
  <li><strong>Data set</strong> — maʼlumotlar toʻplami</li>
  <li><strong>Typical value</strong> — odatiy qiymat</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Mean = <mark>sum ÷ count</mark>; reverse it with total = mean × count.</li>
  <li>Median = middle of the <strong>sorted</strong> list (average the two middles if even count).</li>
  <li>Outliers pull the mean but not the median; for skewed data, prefer the median.</li>
</ul>
""".strip(),
    },

    # ── 56 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-56: Mode, Range, and Outliers",
        "category": "math",
        "summary": "Find the mode and range, identify outliers, and understand how an outlier affects each statistic.",
        "content": """
<h2>SAT-56: Mode, Range, and Outliers</h2>
<p><strong>Description:</strong> Beyond mean and median (SAT-55), the SAT uses three more simple but important
ideas: the <mark>mode</mark> (most frequent value), the <mark>range</mark> (spread from low to high), and
<mark>outliers</mark> (extreme values). Knowing how an outlier changes each statistic is a favorite test trap.</p>

<h3>Mode — the most common value</h3>
<p>The mode is the value that appears <strong>most often</strong>. A data set can have one mode, more than one
(if several values tie), or no mode (if nothing repeats). <em>(Oʻzbekcha: moda — eng koʻp takrorlangan qiymat.)</em></p>

<h3>Range — the spread</h3>
<blockquote><strong>range = maximum value − minimum value</strong></blockquote>
<p>The range measures how spread out the data is. A big range means the values are far apart.
<em>(Oʻzbekcha: amplituda (range) — eng katta va eng kichik qiymat orasidagi farq.)</em></p>

<h3>Outliers — the troublemakers</h3>
<p>An <mark>outlier</mark> is a value much larger or much smaller than the rest. Outliers strongly affect the
<strong>mean and range</strong>, but have little effect on the <strong>median and mode</strong>. This contrast
is exactly what the SAT likes to test.</p>

<h3>Worked Example 1 — mode and range</h3>
<p>Find the mode and range of 3, 7, 7, 7, 9, 12.</p>
<ul>
  <li>Mode = <strong>7</strong> (appears three times).</li>
  <li>Range = 12 − 3 = <strong>9</strong>.</li>
</ul>

<h3>Worked Example 2 — outlier's effect on the mean</h3>
<p>Data: 10, 11, 12, 13. Now add the value 70. What happens to the mean and the median?</p>
<ul>
  <li>Before: mean = 46 ÷ 4 = 11.5; median = (11 + 12)/2 = 11.5.</li>
  <li>After: mean = 116 ÷ 5 = 23.2 (jumped a lot); median = 12 (barely moved).</li>
  <li>Conclusion: the outlier 70 inflated the <strong>mean</strong> but hardly touched the <strong>median</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: chetga chiquvchi qiymat oʻrtachani keskin oshiradi, medianni esa deyarli oʻzgartirmaydi.)</em></p>

<h3>Worked Example 3 — outlier's effect on the range</h3>
<p>Using the same data, what does adding 70 do to the range?</p>
<ul>
  <li>Before: range = 13 − 10 = 3. After: range = 70 − 10 = <strong>60</strong>.</li>
  <li>The outlier exploded the range, because range depends on the extremes.</li>
</ul>
<blockquote>Summary trap to remember: outliers move <strong>mean and range</strong> a lot, but
<strong>median and mode</strong> very little. <em>(Oʻzbekcha: outlier — oʻrtacha va amplitudaga kuchli, median va modaga kam taʼsir qiladi.)</em></blockquote>

<h3>When is a value really an outlier?</h3>
<p>On the SAT you can usually identify an outlier just by looking — it is a point clearly detached from the rest
of the data. You do not need a formal rule, but it helps to ask two questions: is this value far from the cluster,
and is there a real reason it might be a mistake or a special case (a typo, a different kind of subject)? If a
data set has an outlier, mention its effect when you compare statistics, because that is almost always the point
of the question. Removing an outlier pulls the mean back toward the cluster and shrinks the range, while the
median and mode barely budge. <em>(Oʻzbekcha: outlier — qolgan maʼlumotlardan aniq ajralib turadigan qiymat; uni olib tashlasangiz, oʻrtacha va amplituda kichrayadi.)</em></p>

<h3>Practice 1</h3>
<p>Find the mode and range of 5, 5, 8, 9, 9, 9, 20.</p>
<details>
  <summary>Show answer</summary>
  <p>Mode = <strong>9</strong> (three times). Range = 20 − 5 = <strong>15</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>A set is 4, 4, 5, 6, 6. If you change the 6's max to 100, which changes more — the median or the range?</p>
<details>
  <summary>Show answer</summary>
  <p>Median stays near the middle (still around 5), while the range jumps from 6 − 4 = 2 to 100 − 4 = 96.
  The <strong>range</strong> changes far more.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Mode</strong> — moda</li>
  <li><strong>Range</strong> — amplituda (tarqoqlik)</li>
  <li><strong>Maximum / Minimum</strong> — eng katta / eng kichik</li>
  <li><strong>Outlier</strong> — chetga chiquvchi qiymat</li>
  <li><strong>Frequency</strong> — chastota (takrorlanish soni)</li>
  <li><strong>Spread</strong> — tarqoqlik</li>
  <li><strong>Affect</strong> — taʼsir qilish</li>
  <li><strong>Extreme value</strong> — keskin (chetki) qiymat</li>
  <li><strong>Data set</strong> — maʼlumotlar toʻplami</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Mode = most frequent value; range = <mark>max − min</mark>.</li>
  <li>Outliers strongly affect the <strong>mean and range</strong>.</li>
  <li>Outliers barely affect the <strong>median and mode</strong>.</li>
</ul>
""".strip(),
    },

    # ── 57 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-57: Standard Deviation — Measuring Data Spread",
        "category": "math",
        "summary": "Understand standard deviation as a measure of spread and compare data sets without heavy calculation.",
        "content": """
<h2>SAT-57: Standard Deviation — Measuring Data Spread</h2>
<p><strong>Description:</strong> The range (SAT-56) only uses the two extreme values. <mark>Standard deviation</mark>
is a smarter measure of spread that uses <em>every</em> value: it tells you, on average, how far the data points
sit from the mean. The SAT almost never makes you compute it by hand — instead it tests whether you
<strong>understand</strong> what it means and can <strong>compare</strong> two data sets.</p>

<h3>The core idea</h3>
<p>Standard deviation answers: "how clustered or how spread out is the data around the mean?"</p>
<ul>
  <li><strong>Small</strong> standard deviation → values are <mark>tightly packed</mark> near the mean (consistent).</li>
  <li><strong>Large</strong> standard deviation → values are <mark>widely spread</mark> from the mean (variable).</li>
</ul>
<p><em>(Oʻzbekcha: standart ogʻish — maʼlumotlar oʻrtacha atrofida qanchalik tarqalganini koʻrsatadi.)</em></p>

<h3>How to compare two sets by eye</h3>
<p>You usually do not calculate — you reason. If two sets have the same mean, the one whose values are
<strong>farther from the center</strong> has the larger standard deviation. Tight clusters = small; scattered
values = large. <em>(Oʻzbekcha: qiymatlar markazdan qanchalik uzoq boʻlsa, standart ogʻish shunchalik katta.)</em></p>

<h3>Worked Example 1 — compare two sets</h3>
<p>Set A = {50, 50, 50, 50}; Set B = {20, 40, 60, 80}. Which has the larger standard deviation?</p>
<ul>
  <li>Set A: every value equals the mean (50), so there is <strong>zero</strong> spread → standard deviation 0.</li>
  <li>Set B: values range widely around the mean (50), so it has a <strong>large</strong> standard deviation.</li>
  <li>Answer: <strong>Set B</strong> is larger.</li>
</ul>

<h3>Worked Example 2 — same range, different spread</h3>
<p>Set C = {10, 50, 50, 50, 90} and Set D = {10, 30, 50, 70, 90}. Both have range 80 and mean 50. Which spreads more?</p>
<ul>
  <li>Set C clusters tightly at 50 with two far values → moderate spread.</li>
  <li>Set D spreads its values evenly across the whole interval → most points sit farther from the mean.</li>
  <li>So <strong>Set D</strong> has the larger standard deviation, even though the ranges are equal.</li>
</ul>
<blockquote>Key insight: range and standard deviation are different. Range uses only the extremes; standard
deviation uses every value. <em>(Oʻzbekcha: range faqat chetki qiymatlarni, standart ogʻish esa hammasini hisobga oladi.)</em></blockquote>

<h3>Worked Example 3 — interpret in context</h3>
<p>Two machines fill bottles. Machine X amounts have a small standard deviation; Machine Y has a large one.
Which machine is more reliable?</p>
<ul>
  <li>Small standard deviation = more consistent fills → <strong>Machine X</strong> is more reliable.</li>
</ul>
<p><em>(Oʻzbekcha: kichik standart ogʻish — barqarorroq natija degani.)</em></p>

<h3>Practice 1</h3>
<p>Set P = {7, 7, 7, 7}; Set Q = {1, 5, 9, 13}. Which has the greater standard deviation?</p>
<details>
  <summary>Show answer</summary>
  <p>P has identical values → standard deviation 0. Q is spread out → larger. Answer: <strong>Set Q</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Class A's test scores are all between 78 and 82; Class B's range from 50 to 100. Both average 80. Which class
has the larger standard deviation, and what does it say about consistency?</p>
<details>
  <summary>Show answer</summary>
  <p><strong>Class B</strong> — its scores sit much farther from the mean, so it is less consistent. Class A's
  scores cluster tightly, giving a small standard deviation (more consistent students).</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Standard deviation</strong> — standart ogʻish</li>
  <li><strong>Spread</strong> — tarqoqlik</li>
  <li><strong>Mean (center)</strong> — oʻrtacha (markaz)</li>
  <li><strong>Clustered</strong> — zich joylashgan</li>
  <li><strong>Consistent</strong> — barqaror (izchil)</li>
  <li><strong>Variable</strong> — oʻzgaruvchan</li>
  <li><strong>Distance from mean</strong> — oʻrtachadan uzoqlik</li>
  <li><strong>Reliable</strong> — ishonchli</li>
  <li><strong>Range</strong> — amplituda</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Standard deviation measures average distance of values from the mean — the data's <mark>spread</mark>.</li>
  <li>Small SD → tight, consistent; large SD → spread out, variable.</li>
  <li>Compare sets by how far values sit from the center; you rarely need to calculate it.</li>
  <li>Range ≠ standard deviation: range uses only the extremes.</li>
</ul>
""".strip(),
    },

    # ── 58 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-58: Probability — Simple and Independent Events",
        "category": "math",
        "summary": "Find the probability of simple events and combine independent events by multiplying.",
        "content": """
<h2>SAT-58: Probability — Simple and Independent Events</h2>
<p><strong>Description:</strong> <mark>Probability</mark> measures how likely an event is, on a scale from 0
(impossible) to 1 (certain). This lesson covers single ("simple") events and how to combine
<mark>independent</mark> events, where one outcome does not affect the other.</p>

<h3>The basic formula</h3>
<blockquote><strong>P(event) = (favorable outcomes) ÷ (total outcomes)</strong></blockquote>
<p>Every probability is between 0 and 1. You can write it as a fraction, decimal, or percent.
<em>(Oʻzbekcha: ehtimollik — kerakli natijalar sonini umumiy natijalar soniga boʻlish.)</em></p>

<h3>The complement (the "not" trick)</h3>
<p>The probability that an event does <strong>not</strong> happen is <strong>1 − P(event)</strong>. This is often
the fastest path when "at least" appears in a question. <em>(Oʻzbekcha: hodisa roʻy bermaslik ehtimoli = 1 − P.)</em></p>

<h3>Worked Example 1 — simple event</h3>
<p>A bag has 3 red, 2 blue, and 5 green marbles. What is the probability of drawing a blue marble?</p>
<ul>
  <li>Total = 3 + 2 + 5 = 10. Favorable (blue) = 2.</li>
  <li>P(blue) = 2/10 = <strong>1/5</strong> = 0.2 = 20%.</li>
</ul>

<h3>Worked Example 2 — complement</h3>
<p>Using the same bag, what is the probability of <em>not</em> drawing green?</p>
<ul>
  <li>P(green) = 5/10 = 1/2. So P(not green) = 1 − 1/2 = <strong>1/2</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: "yashil emas" ehtimoli = 1 − yashil ehtimoli.)</em></p>

<h3>Independent events — multiply</h3>
<p>Two events are <mark>independent</mark> if one does not change the other (e.g. flipping a coin twice, or
rolling a die then spinning a spinner). For independent events A and B:</p>
<blockquote><strong>P(A and B) = P(A) × P(B)</strong></blockquote>
<p><em>(Oʻzbekcha: mustaqil hodisalar uchun ehtimolliklarni koʻpaytiramiz.)</em></p>

<h3>Worked Example 3 — independent events</h3>
<p>You flip a fair coin and roll a fair die. What is the probability of heads <em>and</em> a 4?</p>
<ul>
  <li>P(heads) = 1/2, P(rolling 4) = 1/6.</li>
  <li>P(heads and 4) = 1/2 × 1/6 = <strong>1/12</strong>.</li>
</ul>
<blockquote>Watch the wording: "and" usually means multiply (both happen); for independent events this is
exact. <em>(Oʻzbekcha: "va" — ikkalasi ham roʻy berishi → koʻpaytirish.)</em></blockquote>

<h3>Independent vs dependent — the replacement test</h3>
<p>Events are independent only if the first does not change the setup for the second. The classic clue is the word
<strong>replacement</strong>. If you draw a marble, <em>put it back</em>, then draw again, the totals reset and the
draws are independent — multiply the original probabilities. If you draw and <strong>do not</strong> replace it,
the second draw has fewer items to choose from, so the events are <strong>dependent</strong> and the second
probability changes. Always check whether the item is returned before multiplying.
<em>(Oʻzbekcha: agar olingan narsa qaytarib qoʻyilsa — mustaqil; qaytarilmasa — bogʻliq, ikkinchi ehtimol oʻzgaradi.)</em></p>

<h3>Worked Example 4 — dependent (no replacement)</h3>
<p>A box has 4 red and 6 blue pens. You draw two pens <em>without</em> replacing the first. What is P(both red)?</p>
<ul>
  <li>First red: 4/10. After removing one red, 3 reds remain out of 9 pens, so second red: 3/9.</li>
  <li>P(both red) = 4/10 × 3/9 = 12/90 = <strong>2/15</strong>.</li>
</ul>
<p>Notice the totals dropped from 10 to 9 — that is what makes it dependent.
<em>(Oʻzbekcha: umumiy son 10 dan 9 ga tushdi — shu sababli hodisalar bogʻliq.)</em></p>

<h3>"At least one" — use the complement</h3>
<p>When a question asks for "at least one," computing every case is slow. Instead find the probability of
<strong>none</strong> and subtract from 1: P(at least one) = 1 − P(none). This shortcut saves time on harder SAT
questions. <em>(Oʻzbekcha: "kamida bitta" — 1 dan "hech biri yoʻq" ehtimolini ayiramiz.)</em></p>

<h3>Practice 1</h3>
<p>A spinner has 8 equal sections numbered 1–8. What is the probability of landing on an even number?</p>
<details>
  <summary>Show answer</summary>
  <p>Even numbers: 2, 4, 6, 8 → 4 favorable of 8. P = 4/8 = <strong>1/2</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>You draw a card and replace it, then draw again from a deck where P(ace) = 1/13 each time. Probability of two aces?</p>
<details>
  <summary>Show answer</summary>
  <p>Independent (because of replacement): 1/13 × 1/13 = <strong>1/169</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Probability</strong> — ehtimollik</li>
  <li><strong>Event</strong> — hodisa</li>
  <li><strong>Outcome</strong> — natija</li>
  <li><strong>Favorable outcome</strong> — qulay natija</li>
  <li><strong>Complement (not)</strong> — toʻldiruvchi (roʻy bermaslik)</li>
  <li><strong>Independent</strong> — mustaqil</li>
  <li><strong>Fair (coin/die)</strong> — bir jinsli (adolatli)</li>
  <li><strong>With replacement</strong> — qaytarib qoʻyish bilan</li>
  <li><strong>Certain / Impossible</strong> — muqarrar / mumkin emas</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>P(event) = <mark>favorable ÷ total</mark>, always between 0 and 1.</li>
  <li>P(not event) = 1 − P(event) (use for "at least" questions).</li>
  <li>Independent events: <strong>P(A and B) = P(A) × P(B)</strong>.</li>
</ul>
""".strip(),
    },

    # ── 59 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-59: Conditional Probability from Two-Way Tables",
        "category": "math",
        "summary": "Read two-way frequency tables and compute conditional probabilities by restricting to the given group.",
        "content": """
<h2>SAT-59: Conditional Probability from Two-Way Tables</h2>
<p><strong>Description:</strong> A <mark>two-way table</mark> sorts data by two categories at once (for example,
gender × choice). <mark>Conditional probability</mark> asks for the chance of something <em>given</em> that we
already know one category. The whole skill is choosing the right denominator.</p>

<h3>Reading a two-way table</h3>
<p>Rows are one category, columns are the other, and each cell is a count. The margins (the "Total" row and
column) give the totals for each category and the grand total. <em>(Oʻzbekcha: ikki tomonlama jadval maʼlumotni bir vaqtda ikki belgi boʻyicha ajratadi.)</em></p>

<h3>The key idea — "given" changes the denominator</h3>
<p>Ordinary probability uses the <strong>grand total</strong> as the denominator. <strong>Conditional</strong>
probability ("given that…") restricts you to just one row or one column, so that row/column total becomes the
new denominator. <em>(Oʻzbekcha: "shart bilan" (given) — butun jamiga emas, faqat bitta qator yoki ustun jamiga boʻlamiz.)</em></p>

<h3>Our example table</h3>
<p>A survey of 100 students asked if they prefer Tea or Coffee:</p>
<ul>
  <li>Boys: Tea 20, Coffee 30 (row total 50).</li>
  <li>Girls: Tea 35, Coffee 15 (row total 50).</li>
  <li>Column totals: Tea 55, Coffee 45; grand total 100.</li>
</ul>

<h3>Worked Example 1 — ordinary probability</h3>
<p>What is the probability a random student prefers Tea?</p>
<ul>
  <li>Use the grand total: P(Tea) = 55/100 = <strong>0.55</strong>.</li>
</ul>

<h3>Worked Example 2 — conditional (given a row)</h3>
<p>Given that a student is a Boy, what is the probability he prefers Coffee?</p>
<ul>
  <li>"Given Boy" → restrict to the Boys row (total 50), not 100.</li>
  <li>Boys who chose Coffee = 30. So P(Coffee | Boy) = 30/50 = <strong>0.6</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: "oʻgʻil bola sharti bilan" — faqat oʻgʻil bolalar qatoriga (50) boʻlamiz.)</em></p>

<h3>Worked Example 3 — conditional (given a column)</h3>
<p>Given that a student prefers Tea, what is the probability the student is a Girl?</p>
<ul>
  <li>"Given Tea" → restrict to the Tea column (total 55).</li>
  <li>Girls in the Tea column = 35. So P(Girl | Tea) = 35/55 = <strong>7/11 ≈ 0.64</strong>.</li>
</ul>
<blockquote>The trap: P(Coffee | Boy) and P(Boy | Coffee) are different questions with different
denominators. Read which group is "given." <em>(Oʻzbekcha: shartni diqqat bilan oʻqing — maxraj oʻzgaradi.)</em></blockquote>

<h3>A reliable two-step routine</h3>
<p>Conditional-probability questions become almost automatic if you always do two things in order:</p>
<ol>
  <li><strong>Find the denominator first.</strong> The word after "given" names a single row or column — write down
  that total before anything else. This is the most common place students slip.</li>
  <li><strong>Find the numerator inside that group.</strong> Count only the members of the given row/column that also
  satisfy the second condition.</li>
</ol>
<p>Because you have already narrowed to one row or column, you never use the grand total in a conditional question.
If you ever find yourself dividing by the grand total, you have probably ignored the word "given."
<em>(Oʻzbekcha: avval maxrajni (berilgan qator yoki ustun jamisini) yozing, keyin shu guruh ichidagi kerakli sonni toping.)</em></p>

<h3>Why this differs from "and" probability</h3>
<p>"P(Boy <em>and</em> Coffee)" divides by the grand total (100), giving 30/100 = 0.3. "P(Coffee <em>given</em> Boy)"
divides by the Boys total (50), giving 30/50 = 0.6. Same cell, different denominators — so always separate "and"
from "given." <em>(Oʻzbekcha: "va" — umumiy jamiga, "given" — faqat bitta guruh jamiga boʻlinadi.)</em></p>

<h3>Practice 1</h3>
<p>Given that a student is a Girl, what is the probability she prefers Tea?</p>
<details>
  <summary>Show answer</summary>
  <p>Restrict to the Girls row (total 50). Girls who chose Tea = 35. P(Tea | Girl) = 35/50 = <strong>0.7</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Given that a student prefers Coffee, what is the probability the student is a Boy?</p>
<details>
  <summary>Show answer</summary>
  <p>Restrict to the Coffee column (total 45). Boys there = 30. P(Boy | Coffee) = 30/45 = <strong>2/3 ≈ 0.67</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Two-way table</strong> — ikki tomonlama jadval</li>
  <li><strong>Conditional probability</strong> — shartli ehtimollik</li>
  <li><strong>Given (that)</strong> — shart bilan (berilganda)</li>
  <li><strong>Row / Column</strong> — qator / ustun</li>
  <li><strong>Cell</strong> — katak</li>
  <li><strong>Margin total</strong> — chekka (yon) jami</li>
  <li><strong>Grand total</strong> — umumiy jami</li>
  <li><strong>Frequency</strong> — chastota</li>
  <li><strong>Denominator</strong> — maxraj</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>In a two-way table, cells are counts; margins are category totals.</li>
  <li>Ordinary probability divides by the <mark>grand total</mark>.</li>
  <li>Conditional ("given X") divides by the total of <strong>just that row or column</strong>.</li>
  <li>P(A | B) and P(B | A) are different — check which group is "given."</li>
</ul>
""".strip(),
    },

    # ── 60 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-60: Sample Surveys and Random Sampling",
        "category": "math",
        "summary": "Understand populations vs samples and why random sampling is required to draw valid conclusions.",
        "content": """
<h2>SAT-60: Sample Surveys and Random Sampling</h2>
<p><strong>Description:</strong> When you can't ask everyone, you survey a <mark>sample</mark> and use it to
estimate facts about the whole <mark>population</mark>. The SAT tests whether a sample was chosen properly —
because only a <mark>random sample</mark> supports trustworthy conclusions.</p>

<h3>Population vs sample</h3>
<ul>
  <li><strong>Population:</strong> the entire group you want to learn about (e.g. all students in a school).</li>
  <li><strong>Sample:</strong> the smaller group you actually survey (e.g. 100 of those students).</li>
  <li><strong>Parameter vs statistic:</strong> a fact about the whole population is a parameter; the same fact
      measured from the sample is a statistic used to estimate it.</li>
</ul>
<p><em>(Oʻzbekcha: populyatsiya — butun guruh; namuna (sample) — biz soʻraydigan kichik qism.)</em></p>

<h3>Why random matters</h3>
<p>In a <mark>random sample</mark> every member of the population has an <strong>equal chance</strong> of being
chosen. Randomness keeps the sample from systematically favoring one type of person, so the sample tends to
look like the population in miniature. Only then can results be generalized.
<em>(Oʻzbekcha: tasodifiy namunada har bir aʼzo tanlanish ehtimoli teng boʻladi.)</em></p>

<h3>Worked Example 1 — identify population and sample</h3>
<p>A company surveys 200 of its 5,000 employees about lunch options. Name the population and the sample.</p>
<ul>
  <li>Population = <strong>all 5,000 employees</strong>. Sample = <strong>the 200 surveyed</strong>.</li>
</ul>

<h3>Worked Example 2 — is the sample random?</h3>
<p>To learn what all students think of the cafeteria, a researcher surveys only students already eating in the
cafeteria. Is this a good random sample?</p>
<ul>
  <li>No. Students who dislike the cafeteria are less likely to be there, so they are under-represented.</li>
  <li>This is <strong>not random</strong>, and the result would be biased toward positive opinions.</li>
</ul>
<p><em>(Oʻzbekcha: bu tasodifiy emas — oshxonani yoqtirmaydiganlar deyarli qatnashmaydi.)</em></p>

<h3>Worked Example 3 — a proper method</h3>
<p>How could the school choose 100 students randomly?</p>
<ul>
  <li>Assign every student a number, then use a random number generator (or draw numbers from a hat) to pick 100.</li>
  <li>Now every student had an equal chance, so the sample is random and the results can be generalized.</li>
</ul>
<blockquote>Rule: valid generalization to a population requires a <strong>random sample from that population</strong>.
<em>(Oʻzbekcha: xulosani butun guruhga umumlashtirish uchun tasodifiy namuna shart.)</em></blockquote>

<h3>Sample size vs sample method</h3>
<p>Students often think a bigger sample automatically fixes everything. It doesn't. A large sample chosen badly is
still misleading — surveying 10,000 people leaving a stadium still tells you nothing about non-fans. The
<strong>method</strong> (was it random?) decides whether the sample is trustworthy; the <strong>size</strong> only
affects how precise the estimate is once the method is sound. So judge randomness first, size second.
<em>(Oʻzbekcha: katta namuna oʻzi yetarli emas — avvalo tanlash usuli tasodifiy boʻlishi kerak, keyin hajm aniqlikka taʼsir qiladi.)</em></p>

<h3>Practice 1</h3>
<p>A TV station asks viewers to call in and vote. Why might this sample be unreliable for "what all citizens think"?</p>
<details>
  <summary>Show answer</summary>
  <p>Only viewers who watch that station and feel strongly enough to call will respond — they are not chosen
  randomly and don't represent all citizens. It is a <strong>self-selected, non-random</strong> sample.</p>
</details>

<h3>Practice 2</h3>
<p>A principal wants to estimate the average study time of all 1,200 students. She numbers them 1–1,200 and uses
a random generator to pick 80. Is this valid, and what is the population?</p>
<details>
  <summary>Show answer</summary>
  <p>Yes — every student had an equal chance, so it is a proper random sample. Population = <strong>all 1,200
  students</strong>; sample = the 80 selected.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Population</strong> — populyatsiya (butun guruh)</li>
  <li><strong>Sample</strong> — namuna</li>
  <li><strong>Random sample</strong> — tasodifiy namuna</li>
  <li><strong>Survey</strong> — soʻrovnoma</li>
  <li><strong>Equal chance</strong> — teng imkoniyat</li>
  <li><strong>Representative</strong> — vakil boʻla oladigan (ifodalovchi)</li>
  <li><strong>Generalize</strong> — umumlashtirish</li>
  <li><strong>Parameter / Statistic</strong> — parametr / statistik koʻrsatkich</li>
  <li><strong>Self-selected</strong> — oʻzini-oʻzi tanlagan</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Population = the whole group; sample = the part you survey.</li>
  <li>A <mark>random sample</mark> gives every member an equal chance and represents the population.</li>
  <li>Only random samples support generalizing results to the population.</li>
</ul>
""".strip(),
    },

    # ── 61 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-61: Selection Bias and Generalizing Results",
        "category": "math",
        "summary": "Spot selection bias, judge when results generalize, and decide which population a conclusion applies to.",
        "content": """
<h2>SAT-61: Selection Bias and Generalizing Results</h2>
<p><strong>Description:</strong> SAT-60 said good conclusions need random samples. This lesson studies what goes
wrong when they aren't: <mark>selection bias</mark>. You'll learn to spot a biased sample and to state exactly
which population (if any) a result can be generalized to.</p>

<h3>What is selection bias?</h3>
<p><mark>Selection bias</mark> happens when the way the sample is chosen makes some members of the population more
likely to be included than others. The sample then no longer looks like the population, so its results are
distorted. <em>(Oʻzbekcha: tanlov xatosi — namunani tanlash usuli baʼzi aʼzolarni koʻproq kiritsa yuzaga keladi.)</em></p>

<h3>Common sources of bias</h3>
<ul>
  <li><strong>Convenience sampling:</strong> surveying whoever is easiest to reach (e.g. only your friends).</li>
  <li><strong>Voluntary response:</strong> only people who feel strongly reply (online polls, call-ins).</li>
  <li><strong>Undercoverage:</strong> part of the population is left out entirely (e.g. phone survey misses people without phones).</li>
</ul>
<p><em>(Oʻzbekcha: qulaylik namunasi, ixtiyoriy javob va qamrab olinmaganlik — bularning hammasi noxolislik keltiradi.)</em></p>

<h3>Generalizing — match the conclusion to the sample</h3>
<p>You can generalize results only to the population that was <strong>randomly sampled</strong>. If the sample
came from a narrower group, the conclusion applies only to that narrower group — not to everyone.
<em>(Oʻzbekcha: xulosa faqat tasodifiy tanlangan guruhga tegishli boʻladi.)</em></p>

<h3>Worked Example 1 — name the bias</h3>
<p>To find the favorite sport of a whole city, a reporter interviews people leaving a football stadium. What's wrong?</p>
<ul>
  <li>People at a stadium already like football, so they're over-represented — this is <strong>selection bias</strong>
  (convenience/undercoverage). The result will overstate football's popularity.</li>
</ul>

<h3>Worked Example 2 — who can we generalize to?</h3>
<p>A study randomly samples students at <em>one</em> university and finds they sleep 6.5 hours on average. To whom
does this apply?</p>
<ul>
  <li>The random sample came only from that university, so the conclusion generalizes to <strong>students at that
  university</strong> — not to all university students everywhere.</li>
</ul>
<p><em>(Oʻzbekcha: namuna faqat bitta universitetdan olingani uchun xulosa faqat oʻsha universitet talabalariga tegishli.)</em></p>

<h3>Worked Example 3 — fix the design</h3>
<p>A magazine mails a survey and only readers who care enough mail it back. Why is this biased, and how to fix it?</p>
<ul>
  <li>Voluntary response: strong-opinion readers reply more, so it's biased.</li>
  <li>Fix: take a <strong>random sample</strong> of the target population and actively collect responses from all of them.</li>
</ul>
<blockquote>Two-question checklist: (1) Was the sample random? (2) From which population? Your conclusion can
only reach that population. <em>(Oʻzbekcha: namuna tasodifiymi va qaysi guruhdan — xulosa faqat oʻsha guruhga boradi.)</em></blockquote>

<h3>Predicting the direction of the bias</h3>
<p>The SAT often wants more than "it's biased" — it wants to know <em>which way</em> the result is wrong. To predict
this, ask who is over-represented and who is missing. A satisfaction survey answered mainly by happy customers will
<strong>overstate</strong> satisfaction. A stadium poll will <strong>overstate</strong> love of that sport. A phone
survey that misses people without phones will <strong>understate</strong> whatever those missing people believe. If
you can name who got left out, you can usually name the direction of the error — and that is exactly the wording the
correct answer choice uses. <em>(Oʻzbekcha: kim ortiqcha, kim tushib qolganini aniqlang — shunda xato qaysi tomonga ekanini bilasiz.)</em></p>

<h3>Practice 1</h3>
<p>An online store emails a satisfaction survey; only happy customers tend to respond. Name the bias and its effect.</p>
<details>
  <summary>Show answer</summary>
  <p><strong>Voluntary-response (selection) bias</strong>. It overstates satisfaction, because unhappy customers are
  under-represented among the responders.</p>
</details>

<h3>Practice 2</h3>
<p>Researchers randomly sample registered voters in one state about a national law. Can they generalize to the whole country?</p>
<details>
  <summary>Show answer</summary>
  <p>No. The random sample was only from that <strong>one state</strong>, so the conclusion applies to that state's
  registered voters — not the entire nation.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Selection bias</strong> — tanlov xatosi (noxolislik)</li>
  <li><strong>Biased sample</strong> — noxolis namuna</li>
  <li><strong>Convenience sampling</strong> — qulaylik namunasi</li>
  <li><strong>Voluntary response</strong> — ixtiyoriy javob</li>
  <li><strong>Undercoverage</strong> — qamrab olinmaganlik</li>
  <li><strong>Generalize</strong> — umumlashtirish</li>
  <li><strong>Representative</strong> — ifodalovchi (vakil)</li>
  <li><strong>Over-represented</strong> — ortiqcha ifodalangan</li>
  <li><strong>Target population</strong> — maqsadli guruh</li>
</ul>

<h3>Summary</h3>
<ul>
  <li><mark>Selection bias</mark> = the sampling method over- or under-includes certain members.</li>
  <li>Watch for convenience samples, voluntary response, and undercoverage.</li>
  <li>Generalize a result <strong>only</strong> to the population that was randomly sampled.</li>
</ul>
""".strip(),
    },
]
