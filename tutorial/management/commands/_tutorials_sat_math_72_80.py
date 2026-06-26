# SAT Math tutorials 72–80 (finishing Part 1: triangles, trig, circles)
# Import:  python manage.py import_tutorials tutorial/management/commands/_tutorials_sat_math_72_80.py --author=prime
# Production:  --author=powerty --republish

TUTORIALS = [
    # ── 72 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-72: Special Right Triangles — 30-60-90",
        "category": "math",
        "summary": "Use the fixed 1 : √3 : 2 side ratio of a 30-60-90 triangle to find any side from one side.",
        "content": """
<h2>SAT-72: Special Right Triangles — 30-60-90</h2>
<p><strong>Description:</strong> Like the 45-45-90 of SAT-71, the <mark>30-60-90 triangle</mark> always has the same
side ratio, so one side gives you all three with no square-root work. It hides inside equilateral triangles cut in
half, so it appears all over SAT geometry.</p>

<h3>The fixed ratio</h3>
<blockquote>In a 30-60-90 triangle the sides are in ratio
<strong>short leg : long leg : hypotenuse = 1 : √3 : 2</strong>.</blockquote>
<p>The key is to match each side to the angle <em>opposite</em> it:</p>
<ul>
  <li>The side opposite the <strong>30°</strong> angle is the <strong>short leg</strong> (the "1").</li>
  <li>The side opposite the <strong>60°</strong> angle is the <strong>long leg</strong> (the "√3").</li>
  <li>The side opposite the <strong>90°</strong> angle is the <strong>hypotenuse</strong> (the "2"), always the longest.</li>
</ul>
<p><em>(Oʻzbekcha: 30° qarshisidagi tomon eng kichik (1), 60° qarshisida √3, 90° qarshisida 2 (gipotenuza).)</em></p>

<h3>How to use the ratio</h3>
<p>Find the <strong>short leg</strong> first — everything is measured from it. The long leg is the short leg × √3, and
the hypotenuse is the short leg × 2. If you are given a different side, work back to the short leg first.
<em>(Oʻzbekcha: avval kichik kateteni toping — qolgan tomonlar undan kelib chiqadi.)</em></p>

<h3>Worked Example 1 — from the short leg</h3>
<p>The short leg of a 30-60-90 triangle is 5. Find the other two sides.</p>
<ul>
  <li>Long leg = 5 × √3 = <strong>5√3</strong>.</li>
  <li>Hypotenuse = 5 × 2 = <strong>10</strong>.</li>
</ul>

<h3>Worked Example 2 — from the hypotenuse</h3>
<p>The hypotenuse is 14. Find the legs.</p>
<ul>
  <li>Hypotenuse = short leg × 2, so short leg = 14 ÷ 2 = <strong>7</strong>.</li>
  <li>Long leg = 7 × √3 = <strong>7√3</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: gipotenuzani 2 ga boʻlib kichik kateteni topamiz.)</em></p>

<h3>Worked Example 3 — from the long leg</h3>
<p>The long leg is 6√3. Find the short leg and hypotenuse.</p>
<ul>
  <li>Long leg = short leg × √3, so short leg = 6√3 ÷ √3 = <strong>6</strong>.</li>
  <li>Hypotenuse = 6 × 2 = <strong>12</strong>.</li>
</ul>

<h3>Where it comes from</h3>
<p>Cut an equilateral triangle (all 60°) straight down the middle. You get two 30-60-90 triangles: the base is halved
(short leg), the slanted side stays whole (hypotenuse, twice the short leg), and the height is the long leg. That is
why the hypotenuse is exactly double the short leg. <em>(Oʻzbekcha: teng tomonli uchburchakni teng ikkiga boʻlsak, 30-60-90 hosil boʻladi — shuning uchun gipotenuza kichik katetdan ikki barobar.)</em></p>
<blockquote>Common mistake: putting √3 on the wrong leg. The √3 always goes with the <strong>60°</strong> side, not the 30° side.
<em>(Oʻzbekcha: √3 doim 60° tomonida boʻladi.)</em></blockquote>

<h3>Worked Example 4 — area of an equilateral triangle</h3>
<p>Find the area of an equilateral triangle with side 8.</p>
<ul>
  <li>Drop a height to split it into two 30-60-90 triangles; the short leg is half the base = 4, so the height (long leg) = 4√3.</li>
  <li>Area = ½ × base × height = ½ × 8 × 4√3 = <strong>16√3</strong> ≈ 27.7.</li>
</ul>
<p><em>(Oʻzbekcha: balandlik 30-60-90 dan kelib chiqadi, soʻng yuza = ½ × asos × balandlik.)</em></p>

<h3>How to recognize a 30-60-90 on the test</h3>
<p>The SAT rarely labels it for you. Look for these signals: a right triangle with a 30° or 60° angle marked; an
equilateral triangle that has been split by a height; or a side that involves √3. Any one of those means the 1 : √3 : 2
ratio is waiting to save you the full Pythagorean calculation. <em>(Oʻzbekcha: 30° yoki 60° burchak, yoki √3 li tomon koʻrsangiz — bu 30-60-90 uchburchak.)</em></p>

<h3>Practice 1</h3>
<p>The short leg of a 30-60-90 triangle is 9. Find the hypotenuse and long leg.</p>
<details>
  <summary>Show answer</summary>
  <p>Hypotenuse = 9 × 2 = <strong>18</strong>; long leg = <strong>9√3</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>An equilateral triangle has side 10. Find its height.</p>
<details>
  <summary>Show answer</summary>
  <p>The height is the long leg of a 30-60-90 with short leg 5 (half the base). Height = 5√3 ≈ <strong>8.66</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>30-60-90 triangle</strong> — 30-60-90 uchburchak</li>
  <li><strong>Short leg</strong> — kichik katet</li>
  <li><strong>Long leg</strong> — katta katet</li>
  <li><strong>Hypotenuse</strong> — gipotenuza</li>
  <li><strong>Ratio</strong> — nisbat</li>
  <li><strong>Opposite (angle)</strong> — qarshisidagi (burchak)</li>
  <li><strong>Equilateral</strong> — teng tomonli</li>
  <li><strong>Height (altitude)</strong> — balandlik</li>
  <li><strong>√3 (radical)</strong> — √3 (ildiz)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>30-60-90 sides are in ratio <mark>1 : √3 : 2</mark> (short : long : hypotenuse).</li>
  <li>Match each side to the angle opposite it; the √3 goes with the 60° side.</li>
  <li>Find the short leg first; long leg = ×√3, hypotenuse = ×2.</li>
</ul>
""".strip(),
    },

    # ── 73 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-73: Triangle Inequality and Similarity (AA, SAS)",
        "category": "math",
        "summary": "Use the triangle inequality to test side lengths and AA/SAS to prove triangles are similar.",
        "content": """
<h2>SAT-73: Triangle Inequality and Similarity (AA, SAS)</h2>
<p><strong>Description:</strong> This lesson covers two ideas: the <mark>triangle inequality</mark> (which side lengths
can actually form a triangle) and <mark>similarity</mark> (when two triangles have the same shape but different size).
Both are common SAT geometry topics.</p>

<h3>The triangle inequality</h3>
<blockquote>For any triangle, the sum of any two sides must be <strong>greater</strong> than the third side.</blockquote>
<p>The fastest test: the third side must be between the <em>difference</em> and the <em>sum</em> of the other two.
<em>(Oʻzbekcha: uchburchak hosil boʻlishi uchun ixtiyoriy ikki tomon yigʻindisi uchinchisidan katta boʻlishi kerak.)</em></p>

<h3>Worked Example 1 — can these be sides?</h3>
<p>Can 3, 4, and 8 form a triangle?</p>
<ul>
  <li>Check 3 + 4 = 7, which is <em>not</em> greater than 8. The inequality fails → <strong>no triangle</strong>.</li>
</ul>

<h3>Worked Example 2 — range for the third side</h3>
<p>Two sides are 6 and 10. What lengths can the third side be?</p>
<ul>
  <li>It must be greater than 10 − 6 = 4 and less than 10 + 6 = 16.</li>
  <li>So the third side is between <strong>4 and 16</strong> (4 &lt; side &lt; 16).</li>
</ul>
<p><em>(Oʻzbekcha: uchinchi tomon ikki tomon ayirmasi bilan yigʻindisi orasida boʻladi.)</em></p>

<h3>Similar triangles — same shape, scaled size</h3>
<p>Two triangles are <mark>similar</mark> if their angles match and their sides are in the same proportion. You can prove
similarity without checking everything:</p>
<ul>
  <li><strong>AA (Angle-Angle):</strong> if two angles of one triangle equal two angles of another, they are similar
  (the third angle must match too).</li>
  <li><strong>SAS (Side-Angle-Side):</strong> if two pairs of sides are in proportion and the angle between them is equal,
  they are similar.</li>
</ul>
<p><em>(Oʻzbekcha: oʻxshash uchburchaklarda burchaklar teng, tomonlar esa bir xil nisbatda boʻladi.)</em></p>

<h3>Worked Example 3 — solve with proportions</h3>
<p>Two triangles are similar. The small one has sides 3 and 5; the large one's side matching the 3 is 9. Find the side
matching the 5.</p>
<ul>
  <li>Scale factor = 9 ÷ 3 = 3 (each large side is 3× the small one).</li>
  <li>Matching side = 5 × 3 = <strong>15</strong>. (Or solve 3/9 = 5/x → x = 15.)</li>
</ul>
<blockquote>Tip: in similar triangles, set up matching sides as a proportion and cross-multiply (review SAT-49).
<em>(Oʻzbekcha: mos tomonlarni proporsiya qilib, krestga koʻpaytiramiz.)</em></blockquote>

<h3>Worked Example 4 — a triangle inside a triangle</h3>
<p>A common SAT figure has a small triangle sitting in the corner of a big one, sharing the same top angle, with their
bases parallel. The small triangle has height 2 and base 3; the big one has height 6. Find the big base.</p>
<ul>
  <li>Parallel bases make the two triangles similar (AA: shared angle + equal corresponding angles).</li>
  <li>Scale factor = 6 ÷ 2 = 3, so big base = 3 × 3 = <strong>9</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: parallel asoslar uchburchaklarni oʻxshash qiladi, soʻng nisbatdan foydalanamiz.)</em></p>

<h3>Why AA is usually enough</h3>
<p>Of the similarity tests, <strong>AA</strong> is the one you reach for most, because angles are easy to spot in SAT
figures — parallel lines, shared angles, and right angles hand them to you. As soon as two angles match, the third must
too (they all add to 180°), so the triangles are guaranteed similar without checking any sides. Train your eye to hunt for
two equal angles first. <em>(Oʻzbekcha: AA — eng koʻp ishlatiladigan belgi, chunki ikki teng burchak topilsa, uchburchaklar oʻxshash boʻladi.)</em></p>

<h3>Common mistake — matching the wrong sides</h3>
<p>In a proportion, each side must be paired with the side in the <em>same position</em> (opposite the same angle). Pairing
a long side with a short side flips the ratio and gives a wrong answer. Label the corresponding vertices first, then build
the proportion. <em>(Oʻzbekcha: proporsiyada har bir tomonni oʻziga mos (bir xil burchak qarshisidagi) tomon bilan juftlang.)</em></p>

<h3>Practice 1</h3>
<p>Two sides of a triangle are 5 and 9. Between what values must the third side lie?</p>
<details>
  <summary>Show answer</summary>
  <p>Between 9 − 5 = 4 and 9 + 5 = 14, so <strong>4 &lt; side &lt; 14</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Triangle ABC ~ triangle DEF with AB = 4 matching DE = 12. If BC = 7, find EF.</p>
<details>
  <summary>Show answer</summary>
  <p>Scale factor = 12 ÷ 4 = 3, so EF = 7 × 3 = <strong>21</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Triangle inequality</strong> — uchburchak tengsizligi</li>
  <li><strong>Similar triangles</strong> — oʻxshash uchburchaklar</li>
  <li><strong>Proportion</strong> — proporsiya</li>
  <li><strong>Scale factor</strong> — oʻlchov koeffitsiyenti</li>
  <li><strong>AA (Angle-Angle)</strong> — burchak-burchak</li>
  <li><strong>SAS (Side-Angle-Side)</strong> — tomon-burchak-tomon</li>
  <li><strong>Corresponding sides</strong> — mos tomonlar</li>
  <li><strong>Sum / Difference</strong> — yigʻindi / ayirma</li>
  <li><strong>Shape</strong> — shakl</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Triangle inequality: each side must be <mark>between the difference and sum</mark> of the other two.</li>
  <li>Similar triangles have equal angles and proportional sides.</li>
  <li>Prove similarity with <strong>AA</strong> or <strong>SAS</strong>, then use proportions to find missing sides.</li>
</ul>
""".strip(),
    },

    # ── 74 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-74: Congruent Triangles and Area/Perimeter Scaling",
        "category": "math",
        "summary": "Tell congruent from similar figures, and scale perimeter by k and area by k² when sizes change.",
        "content": """
<h2>SAT-74: Congruent Triangles and Area/Perimeter Scaling</h2>
<p><strong>Description:</strong> <mark>Congruent</mark> figures are identical copies (same shape <em>and</em> size), while
<mark>similar</mark> figures (SAT-73) share shape but differ in size by a <strong>scale factor</strong>. The SAT's
favorite twist: when you scale a figure, perimeter and area do not grow the same way.</p>

<h3>Congruent vs similar</h3>
<ul>
  <li><strong>Congruent:</strong> same shape and same size — one fits exactly on the other. Scale factor = 1.</li>
  <li><strong>Similar:</strong> same shape, sizes related by a scale factor k.</li>
</ul>
<p><em>(Oʻzbekcha: kongruent — shakl ham, oʻlcham ham bir xil; oʻxshash — shakl bir xil, oʻlcham k marta farq qiladi.)</em></p>

<h3>The scaling rule (the key idea)</h3>
<blockquote>If lengths scale by a factor <strong>k</strong>, then perimeter scales by <strong>k</strong> and area scales
by <strong>k<sup>2</sup></strong>.</blockquote>
<p>Perimeter is a length, so it grows in step with k. Area is two-dimensional, so it grows by k squared. (For volume,
which you'll meet later, the factor is k<sup>3</sup>.) <em>(Oʻzbekcha: uzunlik k marta, perimetr k marta, yuza esa k² marta oshadi.)</em></p>

<h3>Worked Example 1 — scale the perimeter</h3>
<p>A triangle has perimeter 12. A similar triangle is 3 times as big (k = 3). What is its perimeter?</p>
<ul>
  <li>Perimeter scales by k: 12 × 3 = <strong>36</strong>.</li>
</ul>

<h3>Worked Example 2 — scale the area</h3>
<p>The original triangle has area 8. With k = 3, what is the new area?</p>
<ul>
  <li>Area scales by k<sup>2</sup> = 3<sup>2</sup> = 9: 8 × 9 = <strong>72</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: yuza k² marta oshadi, ya'ni 9 barobar.)</em></p>

<h3>Worked Example 3 — work backward from areas</h3>
<p>Two similar squares have areas 16 and 144. What is the ratio of their side lengths?</p>
<ul>
  <li>Area ratio = 144 ÷ 16 = 9. Since area ratio = k<sup>2</sup>, k = √9 = <strong>3</strong>.</li>
  <li>So the sides are in ratio 3 : 1 (the bigger square's sides are 3× as long).</li>
</ul>
<blockquote>Trap: students multiply area by k instead of k<sup>2</sup>. Always square the scale factor for area, and take the
square root of an area ratio to get the length ratio. <em>(Oʻzbekcha: yuza uchun k ni kvadratga koʻtaring; yuza nisbatidan uzunlik nisbatini olish uchun ildiz oling.)</em></blockquote>

<h3>Extending the idea to volume</h3>
<p>The same logic continues into three dimensions. If lengths scale by k, then surface area scales by k<sup>2</sup> and
<strong>volume scales by k<sup>3</sup></strong>. So doubling every edge of a box (k = 2) multiplies its volume by 8, not 2.
A simple way to remember the whole family: the exponent matches the number of dimensions — length is 1-D (k<sup>1</sup>),
area is 2-D (k<sup>2</sup>), volume is 3-D (k<sup>3</sup>). <em>(Oʻzbekcha: uzunlik k¹, yuza k², hajm k³ marta oshadi — koʻrsatkich oʻlchamlar soniga teng.)</em></p>

<h3>Why congruence criteria matter</h3>
<p>Two triangles are congruent when enough matching parts are equal; the standard shortcuts are <strong>SSS</strong> (three
sides), <strong>SAS</strong> (two sides and the angle between), <strong>ASA</strong> (two angles and the side between), and
<strong>AAS</strong>. Notice that knowing all three angles alone (AAA) is <em>not</em> enough — that only proves similarity,
because the triangles could be different sizes. This is the cleanest way to see the line between congruent (same size) and
similar (same shape). <em>(Oʻzbekcha: SSS, SAS, ASA, AAS — kongruentlik belgilari; faqat burchaklar (AAA) esa oʻxshashlikni beradi.)</em></p>

<h3>Practice 1</h3>
<p>A rectangle's sides are doubled (k = 2). By what factor does its area increase?</p>
<details>
  <summary>Show answer</summary>
  <p>Area scales by k<sup>2</sup> = 2<sup>2</sup> = <strong>4</strong> times.</p>
</details>

<h3>Practice 2</h3>
<p>Two similar triangles have areas 25 and 100. If the smaller has perimeter 15, what is the larger's perimeter?</p>
<details>
  <summary>Show answer</summary>
  <p>Area ratio 100/25 = 4, so k = √4 = 2. Perimeter scales by k: 15 × 2 = <strong>30</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Congruent</strong> — kongruent (teng)</li>
  <li><strong>Similar</strong> — oʻxshash</li>
  <li><strong>Scale factor</strong> — oʻlchov koeffitsiyenti</li>
  <li><strong>Perimeter</strong> — perimetr</li>
  <li><strong>Area</strong> — yuza</li>
  <li><strong>Ratio</strong> — nisbat</li>
  <li><strong>Square (k²)</strong> — kvadrat (k²)</li>
  <li><strong>Square root</strong> — kvadrat ildiz</li>
  <li><strong>Dimension</strong> — oʻlcham</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Congruent = same shape and size; similar = same shape, scaled by k.</li>
  <li>Length and perimeter scale by <mark>k</mark>; area scales by <mark>k<sup>2</sup></mark>.</li>
  <li>From an area ratio, take the square root to get the length/perimeter ratio.</li>
</ul>
""".strip(),
    },

    # ── 75 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-75: Right Triangle Trigonometry — Sine, Cosine, Tangent",
        "category": "math",
        "summary": "Use SOH-CAH-TOA to relate the sides and angles of a right triangle and solve for unknowns.",
        "content": """
<h2>SAT-75: Right Triangle Trigonometry — Sine, Cosine, Tangent</h2>
<p><strong>Description:</strong> Trigonometry connects a right triangle's <mark>angles</mark> to its <mark>side ratios</mark>.
The three core functions — sine, cosine, tangent — are captured by one memory phrase, <strong>SOH-CAH-TOA</strong>.</p>

<h3>Naming the sides (from a chosen angle)</h3>
<p>Pick the angle you care about (not the right angle). Then:</p>
<ul>
  <li><strong>Opposite</strong> = the side across from that angle.</li>
  <li><strong>Adjacent</strong> = the side next to that angle (not the hypotenuse).</li>
  <li><strong>Hypotenuse</strong> = the longest side, opposite the right angle.</li>
</ul>
<p><em>(Oʻzbekcha: tanlangan burchakka qarab tomonlar nomlanadi: qarshi, yondosh va gipotenuza.)</em></p>

<h3>SOH-CAH-TOA</h3>
<blockquote>
<strong>sin = Opposite / Hypotenuse</strong><br>
<strong>cos = Adjacent / Hypotenuse</strong><br>
<strong>tan = Opposite / Adjacent</strong>
</blockquote>
<p><em>(Oʻzbekcha: sinus = qarshi/gipotenuza, kosinus = yondosh/gipotenuza, tangens = qarshi/yondosh.)</em></p>

<h3>Worked Example 1 — find a ratio</h3>
<p>A right triangle has opposite = 3, adjacent = 4, hypotenuse = 5 (relative to angle θ). Find sin θ, cos θ, tan θ.</p>
<ul>
  <li>sin θ = 3/5, cos θ = 4/5, tan θ = 3/4.</li>
</ul>

<h3>Worked Example 2 — find a missing side</h3>
<p>In a right triangle, the angle is 30° and the hypotenuse is 12. Find the side opposite the 30°.</p>
<ul>
  <li>Opposite uses sine: sin 30° = opposite / 12. Since sin 30° = 0.5, opposite = 0.5 × 12 = <strong>6</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: qarshi tomonni topish uchun sinusdan foydalanamiz.)</em></p>

<h3>Worked Example 3 — choose the right function</h3>
<p>You know the angle 40° and the adjacent side 10, and want the opposite side. Which function?</p>
<ul>
  <li>Opposite and adjacent together → <strong>tangent</strong>: tan 40° = opposite / 10, so opposite = 10·tan 40°.</li>
</ul>
<blockquote>How to choose: see which two sides are involved (the one you have and the one you want), then pick the
function that uses exactly those two. <em>(Oʻzbekcha: qaysi ikki tomon ishtirok etsa, oʻsha funksiyani tanlang.)</em></blockquote>

<h3>Worked Example 4 — find the angle (inverse trig)</h3>
<p>A right triangle has opposite = 6 and adjacent = 6 for angle θ. What is θ?</p>
<ul>
  <li>tan θ = opposite/adjacent = 6/6 = 1.</li>
  <li>The angle whose tangent is 1 is <strong>45°</strong> (use the inverse: θ = tan⁻¹(1)).</li>
</ul>
<p>When you know a ratio and want the angle, you use the inverse functions sin⁻¹, cos⁻¹, tan⁻¹.
<em>(Oʻzbekcha: nisbatdan burchakni topish uchun teskari funksiyalardan (tan⁻¹) foydalanamiz.)</em></p>

<h3>The famous angle values to know</h3>
<p>A few values come up so often they are worth memorizing: sin 30° = 1/2, cos 30° = √3/2, tan 30° = 1/√3; sin 45° = cos
45° = √2/2; sin 60° = √3/2, cos 60° = 1/2, tan 60° = √3. These match the special triangles from SAT-71 and SAT-72, so you
are really just reading side ratios off those triangles. <em>(Oʻzbekcha: 30°, 45°, 60° qiymatlari maxsus uchburchaklardan kelib chiqadi — ularni yodlang.)</em></p>

<h3>Common mistake — wrong side as hypotenuse</h3>
<p>Sine and cosine always divide by the hypotenuse, never by a leg. If you accidentally use a leg as the denominator,
every ratio comes out wrong. Identify the hypotenuse (opposite the right angle, longest side) before writing any ratio.
<em>(Oʻzbekcha: sinus va kosinus doim gipotenuzaga boʻlinadi — avval gipotenuzani aniqlang.)</em></p>

<h3>Practice 1</h3>
<p>A right triangle has opposite = 5 and hypotenuse = 13 for angle θ. Find sin θ and cos θ.</p>
<details>
  <summary>Show answer</summary>
  <p>sin θ = 5/13. The adjacent side is √(13² − 5²) = √144 = 12, so cos θ = <strong>12/13</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>An angle is 60° and its adjacent side is 8. Find the opposite side using tangent (tan 60° = √3).</p>
<details>
  <summary>Show answer</summary>
  <p>tan 60° = opposite / 8 → opposite = 8√3 ≈ <strong>13.86</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Trigonometry</strong> — trigonometriya</li>
  <li><strong>Sine</strong> — sinus</li>
  <li><strong>Cosine</strong> — kosinus</li>
  <li><strong>Tangent</strong> — tangens</li>
  <li><strong>Opposite side</strong> — qarshi tomon</li>
  <li><strong>Adjacent side</strong> — yondosh tomon</li>
  <li><strong>Hypotenuse</strong> — gipotenuza</li>
  <li><strong>Ratio</strong> — nisbat</li>
  <li><strong>Angle</strong> — burchak</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>From a chosen angle, label sides opposite / adjacent / hypotenuse.</li>
  <li><mark>SOH-CAH-TOA</mark>: sin = O/H, cos = A/H, tan = O/A.</li>
  <li>Pick the function that uses the side you have and the side you want.</li>
</ul>
""".strip(),
    },

    # ── 76 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-76: Trigonometric Identities — sin(x) = cos(90° − x)",
        "category": "math",
        "summary": "Use the cofunction identity sin(x) = cos(90° − x) to connect the sine and cosine of complementary angles.",
        "content": """
<h2>SAT-76: Trigonometric Identities — sin(x) = cos(90° − x)</h2>
<p><strong>Description:</strong> The SAT often tests one elegant fact: the sine of an angle equals the cosine of its
<mark>complement</mark>. This is the <mark>cofunction identity</mark>, and it follows directly from SOH-CAH-TOA.</p>

<h3>The identity</h3>
<blockquote><strong>sin(x) = cos(90° − x)</strong> and <strong>cos(x) = sin(90° − x)</strong></blockquote>
<p>Because the two non-right angles of a right triangle add to 90°, they are complementary — so one angle's sine is the
other angle's cosine. <em>(Oʻzbekcha: toʻgʻri burchakli uchburchakda ikki oʻtkir burchak 90° ga toʻldiradi, shuning uchun biri sinusi ikkinchisining kosinusiga teng.)</em></p>

<h3>Why it is true (from the triangle)</h3>
<p>For angle x, the opposite side is the adjacent side for angle (90° − x), and vice versa. So sin x = opposite/hyp for
x is exactly cos(90° − x) = adjacent/hyp for the other angle. Same ratio, two names.
<em>(Oʻzbekcha: bir burchakning qarshi tomoni — ikkinchi burchakning yondosh tomoni, shuning uchun nisbatlar mos keladi.)</em></p>

<h3>Worked Example 1 — direct substitution</h3>
<p>If sin(20°) = 0.34, what is cos(70°)?</p>
<ul>
  <li>70° = 90° − 20°, so cos(70°) = sin(20°) = <strong>0.34</strong>.</li>
</ul>

<h3>Worked Example 2 — match the angles</h3>
<p>cos(35°) equals the sine of what angle?</p>
<ul>
  <li>cos(35°) = sin(90° − 35°) = <strong>sin(55°)</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: kosinusni sinusga aylantirish uchun burchakni 90° dan ayiramiz.)</em></p>

<h3>Worked Example 3 — solve for an unknown angle</h3>
<p>If sin(2x) = cos(3x), and the angles are acute, find x.</p>
<ul>
  <li>sin(2x) = cos(3x) means the angles are complementary: 2x + 3x = 90.</li>
  <li>5x = 90 → <strong>x = 18°</strong>.</li>
</ul>
<blockquote>Key move: whenever you see "sin(A) = cos(B)" with acute angles, set <strong>A + B = 90°</strong>.
<em>(Oʻzbekcha: sin(A) = cos(B) boʻlsa, A + B = 90° deb yozing.)</em></blockquote>

<h3>Worked Example 4 — same value, find the partner angle</h3>
<p>For what acute angle is the sine equal to cos(28°)?</p>
<ul>
  <li>cos(28°) = sin(90° − 28°) = sin(62°), so the angle is <strong>62°</strong>.</li>
  <li>Notice 28° and 62° add to 90° — they are the two acute angles of the same right triangle.</li>
</ul>
<p><em>(Oʻzbekcha: 28° va 62° — bir uchburchakning ikki oʻtkir burchagi.)</em></p>

<h3>Why this saves time on the SAT</h3>
<p>Many questions look harder than they are because they mix sine and cosine. The cofunction identity lets you rewrite
one in terms of the other so both sides speak the same "language." Once both are sines (or both cosines), you can match
angles directly. Train yourself to spot the pattern: a sine and a cosine set equal, with angles that could add to 90°,
is almost always a cofunction question. <em>(Oʻzbekcha: sinus va kosinus aralashgan masalalarni kofunksiya yordamida bitta turga keltiring.)</em></p>

<h3>A note on equal sines</h3>
<p>Be careful: sin(A) = sin(B) does <em>not</em> force A = B in general, but for the acute angles the SAT uses, equal
sines do mean equal angles, and equal cosines mean equal angles. The cofunction twist only appears when one is sine and
the other is cosine. <em>(Oʻzbekcha: oʻtkir burchaklar uchun teng sinuslar teng burchaklarni bildiradi; kofunksiya esa sinus-kosinus aralashganda kerak.)</em></p>

<h3>Practice 1</h3>
<p>If cos(25°) = 0.91, what is sin(65°)?</p>
<details>
  <summary>Show answer</summary>
  <p>65° = 90° − 25°, so sin(65°) = cos(25°) = <strong>0.91</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>If sin(x + 10°) = cos(x + 30°) with acute angles, find x.</p>
<details>
  <summary>Show answer</summary>
  <p>(x + 10) + (x + 30) = 90 → 2x + 40 = 90 → 2x = 50 → <strong>x = 25°</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Identity</strong> — ayniyat</li>
  <li><strong>Cofunction</strong> — kofunksiya</li>
  <li><strong>Complementary angles</strong> — toʻldiruvchi burchaklar (90°)</li>
  <li><strong>Sine / Cosine</strong> — sinus / kosinus</li>
  <li><strong>Acute angle</strong> — oʻtkir burchak</li>
  <li><strong>Substitute</strong> — oʻrniga qoʻyish</li>
  <li><strong>Equal ratios</strong> — teng nisbatlar</li>
  <li><strong>Right triangle</strong> — toʻgʻri burchakli uchburchak</li>
  <li><strong>Sum to 90°</strong> — 90° ga toʻldirish</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Cofunction identity: <mark>sin(x) = cos(90° − x)</mark> (and cos(x) = sin(90° − x)).</li>
  <li>It works because the two acute angles of a right triangle are complementary.</li>
  <li>For "sin(A) = cos(B)" with acute angles, set A + B = 90° and solve.</li>
</ul>
""".strip(),
    },

    # ── 77 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-77: Radians vs. Degrees and Arc Length",
        "category": "math",
        "summary": "Convert between radians and degrees and compute arc length as a fraction of the circle's circumference.",
        "content": """
<h2>SAT-77: Radians vs. Degrees and Arc Length</h2>
<p><strong>Description:</strong> Angles can be measured in <mark>degrees</mark> or <mark>radians</mark>. The SAT expects you
to convert between them and to find an <mark>arc length</mark> — the distance along part of a circle's edge.</p>

<h3>The conversion fact</h3>
<blockquote>A full circle is <strong>360°</strong> = <strong>2π radians</strong>, so <strong>180° = π radians</strong>.</blockquote>
<ul>
  <li>Degrees → radians: multiply by <strong>π/180</strong>.</li>
  <li>Radians → degrees: multiply by <strong>180/π</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: 180° = π radian; gradusdan radianga oʻtish uchun π/180 ga koʻpaytiramiz.)</em></p>

<h3>Worked Example 1 — degrees to radians</h3>
<p>Convert 90° to radians.</p>
<ul>
  <li>90 × π/180 = π/2 radians.</li>
</ul>

<h3>Worked Example 2 — radians to degrees</h3>
<p>Convert 3π/4 radians to degrees.</p>
<ul>
  <li>(3π/4) × (180/π) = 3 × 180 / 4 = <strong>135°</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: radiandan gradusga oʻtish uchun 180/π ga koʻpaytiramiz.)</em></p>

<h3>Arc length — a fraction of the way around</h3>
<p>An arc is part of the circle's circumference. The whole circumference is 2πr. An arc that spans a central angle is
that same fraction of the full circle:</p>
<blockquote><strong>arc length = (central angle / 360°) × 2πr</strong> (degrees)<br>
or simply <strong>arc length = r × θ</strong> when θ is in <em>radians</em>.</blockquote>
<p><em>(Oʻzbekcha: yoy uzunligi — aylana uzunligining markaziy burchakka mos qismi.)</em></p>

<h3>Worked Example 3 — arc length in degrees</h3>
<p>A circle has radius 6. Find the length of an arc with central angle 60°.</p>
<ul>
  <li>Fraction = 60/360 = 1/6 of the circle.</li>
  <li>Circumference = 2π(6) = 12π. Arc = (1/6)(12π) = <strong>2π</strong>.</li>
</ul>
<blockquote>Shortcut: in radians, arc length is just r × θ. For r = 6 and θ = π/3 (which is 60°): 6 × π/3 = 2π — same answer.
<em>(Oʻzbekcha: radianlarda yoy uzunligi = r × θ, juda qulay.)</em></blockquote>

<h3>What a radian actually is</h3>
<p>A radian is the angle you get when the arc length equals the radius. Because the full circumference is 2πr, wrapping
the radius around the circle fits exactly 2π times — that is why a full circle is 2π radians. This is also why the
radian formula arc = rθ is so clean: θ literally counts how many "radius-lengths" of arc you have. Understanding this
makes the conversions feel natural instead of memorized. <em>(Oʻzbekcha: bir radian — yoy uzunligi radiusga teng boʻlgan burchak; shuning uchun toʻliq aylana 2π radian.)</em></p>

<h3>Worked Example 4 — find the radius from an arc</h3>
<p>An arc of length 10π comes from a central angle of 120° in some circle. Find the radius.</p>
<ul>
  <li>Fraction = 120/360 = 1/3, so arc = (1/3)(2πr) = (2πr)/3.</li>
  <li>Set (2πr)/3 = 10π → 2πr = 30π → r = <strong>15</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: yoy formulasidan radiusni topish uchun teskari ishlaymiz.)</em></p>

<h3>Common mistake — mixing the two formulas</h3>
<p>Use arc = (angle/360)·2πr only when the angle is in <strong>degrees</strong>, and arc = rθ only when θ is in
<strong>radians</strong>. Plugging a degree value into rθ gives a hugely wrong answer. When in doubt, convert to one
system first. <em>(Oʻzbekcha: rθ formulasi faqat radian uchun; gradusni avval radianga aylantiring.)</em></p>

<h3>Practice 1</h3>
<p>Convert 45° to radians.</p>
<details>
  <summary>Show answer</summary>
  <p>45 × π/180 = <strong>π/4</strong> radians.</p>
</details>

<h3>Practice 2</h3>
<p>A circle of radius 10 has an arc with central angle 90°. Find the arc length.</p>
<details>
  <summary>Show answer</summary>
  <p>Fraction = 90/360 = 1/4. Circumference = 20π. Arc = (1/4)(20π) = <strong>5π</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Degree</strong> — gradus</li>
  <li><strong>Radian</strong> — radian</li>
  <li><strong>Convert</strong> — oʻzgartirish (almashtirish)</li>
  <li><strong>Arc length</strong> — yoy uzunligi</li>
  <li><strong>Central angle</strong> — markaziy burchak</li>
  <li><strong>Circumference</strong> — aylana uzunligi</li>
  <li><strong>Radius</strong> — radius</li>
  <li><strong>Fraction</strong> — qism (ulush)</li>
  <li><strong>π (pi)</strong> — pi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li><mark>180° = π radians</mark>; ×π/180 to go to radians, ×180/π to go to degrees.</li>
  <li>Arc length = (central angle / 360°) × 2πr in degrees.</li>
  <li>In radians, arc length = <strong>r × θ</strong>.</li>
</ul>
""".strip(),
    },

    # ── 78 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-78: Area of a Sector of a Circle",
        "category": "math",
        "summary": "Find the area of a 'pizza slice' sector as a fraction of the whole circle's area.",
        "content": """
<h2>SAT-78: Area of a Sector of a Circle</h2>
<p><strong>Description:</strong> A <mark>sector</mark> is a "pizza slice" of a circle — the region between two radii and the
arc between them. Its area is just the matching fraction of the whole circle's area, exactly parallel to how arc length
worked in SAT-77.</p>

<h3>The sector area formula</h3>
<blockquote><strong>sector area = (central angle / 360°) × πr<sup>2</sup></strong> (degrees)<br>
or <strong>sector area = ½ r<sup>2</sup> θ</strong> when θ is in <em>radians</em>.</blockquote>
<p>The whole circle's area is πr<sup>2</sup>, and the sector is the angle's fraction of it.
<em>(Oʻzbekcha: sektor yuzasi — butun doira yuzasining markaziy burchakka mos qismi.)</em></p>

<h3>The parallel with arc length</h3>
<p>Both arc length and sector area use the <strong>same fraction</strong>, central angle ÷ 360°. The only difference is
what you multiply it by: circumference (2πr) for arc length, area (πr<sup>2</sup>) for sector area. Find the fraction
once, then choose the right "whole." <em>(Oʻzbekcha: yoy va sektor bir xil ulushdan foydalanadi — faqat butuni farq qiladi.)</em></p>

<h3>Worked Example 1 — quarter circle</h3>
<p>A circle has radius 4. Find the area of a sector with central angle 90°.</p>
<ul>
  <li>Fraction = 90/360 = 1/4. Whole area = π(4)<sup>2</sup> = 16π.</li>
  <li>Sector = (1/4)(16π) = <strong>4π</strong>.</li>
</ul>

<h3>Worked Example 2 — other angles</h3>
<p>A circle has radius 6 and a sector with central angle 120°. Find the sector area.</p>
<ul>
  <li>Fraction = 120/360 = 1/3. Whole area = π(6)<sup>2</sup> = 36π.</li>
  <li>Sector = (1/3)(36π) = <strong>12π</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: 120° — doiraning uchdan biri, shuning uchun yuzaning uchdan biri.)</em></p>

<h3>Worked Example 3 — work backward to the angle</h3>
<p>A circle of radius 10 has a sector of area 25π. What is the central angle?</p>
<ul>
  <li>Whole area = 100π. Fraction = 25π / 100π = 1/4.</li>
  <li>Central angle = (1/4)(360°) = <strong>90°</strong>.</li>
</ul>
<blockquote>Tip: keep answers in terms of π unless told to use a decimal — the SAT usually wants the exact form.
<em>(Oʻzbekcha: javobni π bilan qoldiring, agar oʻnli kasr soʻralmasa.)</em></blockquote>

<h3>Worked Example 4 — perimeter of a sector</h3>
<p>A sector of a circle with radius 9 has a central angle of 40°. Find its full perimeter (not just the area).</p>
<ul>
  <li>The perimeter is two radii plus the arc: 9 + 9 + arc.</li>
  <li>Arc = (40/360)(2π·9) = (1/9)(18π) = 2π. So perimeter = 18 + 2π ≈ <strong>24.28</strong>.</li>
</ul>
<p>Don't forget the two straight radius edges — a sector's boundary is two radii <em>and</em> the arc.
<em>(Oʻzbekcha: sektor perimetri — ikkita radius va yoy uzunligi yigʻindisi.)</em></p>

<h3>Sector area vs triangle area — don't confuse them</h3>
<p>A sector is the curved pizza slice; it is <em>not</em> the triangle formed by the two radii and a straight chord. The
sector uses πr<sup>2</sup> and the angle fraction; the triangle uses ½·base·height. SAT problems sometimes ask for the
region <em>between</em> them (the sector minus the triangle, called a segment), so read carefully whether the boundary is
curved or straight. <em>(Oʻzbekcha: sektor — egri "tilim"; u ikki radius va vatardan iborat uchburchak emas.)</em></p>

<h3>Practice 1</h3>
<p>A circle of radius 3 has a sector with central angle 60°. Find its area.</p>
<details>
  <summary>Show answer</summary>
  <p>Fraction = 60/360 = 1/6. Whole = 9π. Sector = (1/6)(9π) = <strong>1.5π</strong> (or 3π/2).</p>
</details>

<h3>Practice 2</h3>
<p>A sector of a circle with radius 8 has area 8π. Find the central angle.</p>
<details>
  <summary>Show answer</summary>
  <p>Whole area = 64π. Fraction = 8π/64π = 1/8. Angle = (1/8)(360°) = <strong>45°</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Sector</strong> — sektor</li>
  <li><strong>Central angle</strong> — markaziy burchak</li>
  <li><strong>Area</strong> — yuza</li>
  <li><strong>Radius</strong> — radius</li>
  <li><strong>Fraction</strong> — ulush (qism)</li>
  <li><strong>Circle</strong> — doira (aylana)</li>
  <li><strong>Radii (plural)</strong> — radiuslar</li>
  <li><strong>Arc</strong> — yoy</li>
  <li><strong>π (pi)</strong> — pi</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Sector area = <mark>(central angle / 360°) × πr<sup>2</sup></mark>.</li>
  <li>Same fraction as arc length — just multiply by the circle's <strong>area</strong> instead of circumference.</li>
  <li>Work backward by setting the sector ÷ whole area equal to the angle fraction.</li>
</ul>
""".strip(),
    },

    # ── 79 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-79: Circle Equations in the Coordinate Plane",
        "category": "math",
        "summary": "Read the center and radius straight from the standard circle equation (x − h)² + (y − k)² = r².",
        "content": """
<h2>SAT-79: Circle Equations in the Coordinate Plane</h2>
<p><strong>Description:</strong> A circle on the coordinate plane has a tidy <mark>standard-form equation</mark> that hands
you its <strong>center</strong> and <strong>radius</strong> directly. Reading them correctly — especially the signs — is
the whole skill here.</p>

<h3>The standard form</h3>
<blockquote><strong>(x − h)<sup>2</sup> + (y − k)<sup>2</sup> = r<sup>2</sup></strong></blockquote>
<ul>
  <li>The <strong>center</strong> is <strong>(h, k)</strong>.</li>
  <li>The <strong>radius</strong> is <strong>r</strong> = √(right-hand side).</li>
</ul>
<p>Watch the signs: the form subtracts h and k, just like vertex form in SAT-35.
<em>(Oʻzbekcha: markaz (h, k); ishoralarga eʼtibor bering — formula h va k ni ayiradi.)</em></p>

<h3>The sign trap</h3>
<p>Because the equation has (x − h), a plus sign inside means a negative coordinate:
(x + 3) is really (x − (−3)), so h = −3. And the right side is r<sup>2</sup>, not r — you must take the square root.
<em>(Oʻzbekcha: (x + 3) aslida (x − (−3)), demak h = −3; oʻng tomon r² boʻlgani uchun ildiz oling.)</em></p>

<h3>Worked Example 1 — read center and radius</h3>
<p>Find the center and radius of (x − 2)<sup>2</sup> + (y − 5)<sup>2</sup> = 49.</p>
<ul>
  <li>Center = (2, 5). Radius = √49 = <strong>7</strong>.</li>
</ul>

<h3>Worked Example 2 — handle the signs</h3>
<p>Find the center and radius of (x + 4)<sup>2</sup> + (y − 1)<sup>2</sup> = 25.</p>
<ul>
  <li>(x + 4) → h = −4; (y − 1) → k = 1. Center = <strong>(−4, 1)</strong>.</li>
  <li>Radius = √25 = <strong>5</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: (x + 4) → h = −4, chunki formula ayiradi.)</em></p>

<h3>Worked Example 3 — build the equation</h3>
<p>Write the equation of a circle with center (3, −2) and radius 6.</p>
<ul>
  <li>(x − 3)<sup>2</sup> + (y − (−2))<sup>2</sup> = 6<sup>2</sup>.</li>
  <li>Equation: <strong>(x − 3)<sup>2</sup> + (y + 2)<sup>2</sup> = 36</strong>.</li>
</ul>
<blockquote>Tip: a negative center coordinate becomes a plus sign in the equation, and remember to square the radius on
the right. <em>(Oʻzbekcha: markazning manfiy koordinatasi tenglamada plyusga aylanadi; radiusni kvadratga koʻtaring.)</em></blockquote>

<h3>Worked Example 4 — build a circle from a center and a point</h3>
<p>Write the equation of a circle centered at (1, 2) that passes through the point (4, 6).</p>
<ul>
  <li>The radius is the distance from the center to that point: r = √((4 − 1)<sup>2</sup> + (6 − 2)<sup>2</sup>) = √(9 + 16) = √25 = 5.</li>
  <li>So r<sup>2</sup> = 25, giving <strong>(x − 1)<sup>2</sup> + (y − 2)<sup>2</sup> = 25</strong>.</li>
</ul>
<p>This connects circles to the distance formula from SAT-70 — the radius is just a distance.
<em>(Oʻzbekcha: radius — markazdan nuqtagacha boʻlgan masofa, shuning uchun masofa formulasidan foydalanamiz.)</em></p>

<h3>Is a point inside, on, or outside the circle?</h3>
<p>Plug the point into the left side and compare with r<sup>2</sup>. If it equals r<sup>2</sup>, the point is <strong>on</strong>
the circle; if it is less, the point is <strong>inside</strong>; if it is more, the point is <strong>outside</strong>. This
is a quick SAT check that needs no graphing. <em>(Oʻzbekcha: nuqtani tenglamaga qoʻyib, natijani r² bilan solishtiramiz.)</em></p>

<h3>Practice 1</h3>
<p>Find the center and radius of (x − 1)<sup>2</sup> + (y + 6)<sup>2</sup> = 16.</p>
<details>
  <summary>Show answer</summary>
  <p>Center = (1, −6); radius = √16 = <strong>4</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Write the equation of a circle with center (−5, 0) and radius 3.</p>
<details>
  <summary>Show answer</summary>
  <p><strong>(x + 5)<sup>2</sup> + y<sup>2</sup> = 9</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Circle equation</strong> — aylana tenglamasi</li>
  <li><strong>Standard form</strong> — standart koʻrinish</li>
  <li><strong>Center</strong> — markaz</li>
  <li><strong>Radius</strong> — radius</li>
  <li><strong>Coordinate plane</strong> — koordinata tekisligi</li>
  <li><strong>Square root</strong> — kvadrat ildiz</li>
  <li><strong>Sign</strong> — ishora</li>
  <li><strong>Coordinate (h, k)</strong> — koordinata (h, k)</li>
  <li><strong>Squared</strong> — kvadratga koʻtarilgan</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Standard form: <mark>(x − h)<sup>2</sup> + (y − k)<sup>2</sup> = r<sup>2</sup></mark>.</li>
  <li>Center = (h, k); a plus sign inside means a negative coordinate.</li>
  <li>Radius = square root of the right side (it equals r<sup>2</sup>, not r).</li>
</ul>
""".strip(),
    },

    # ── 80 ────────────────────────────────────────────────────────────────────
    {
        "title": "SAT-80: Completing the Square to Find a Circle's Center and Radius",
        "category": "math",
        "summary": "Turn an expanded circle equation into standard form by completing the square for x and for y.",
        "content": """
<h2>SAT-80: Completing the Square to Find a Circle's Center and Radius</h2>
<p><strong>Description:</strong> Sometimes a circle is given <em>expanded</em>, like
x<sup>2</sup> + y<sup>2</sup> + 6x − 4y − 3 = 0, hiding its center and radius. <mark>Completing the square</mark> for x and
for y rewrites it into the standard form of SAT-79 so you can read them off.</p>

<h3>Completing the square — the move</h3>
<p>For a group like x<sup>2</sup> + bx, take half of b, square it, and add it to make a perfect square:
x<sup>2</sup> + bx + (b/2)<sup>2</sup> = (x + b/2)<sup>2</sup>. Whatever you add on one side you must balance on the other.
<em>(Oʻzbekcha: x² + bx ni toʻliq kvadratga keltirish uchun (b/2)² ni qoʻshamiz.)</em></p>

<h3>The plan for a circle</h3>
<ol>
  <li>Group the x-terms together and the y-terms together; move the constant to the right side.</li>
  <li>Complete the square for x, and separately for y (add the same amounts to the right side).</li>
  <li>Write each group as a square; read center (h, k) and radius √(right side).</li>
</ol>
<p><em>(Oʻzbekcha: x va y hadlarini alohida guruhlab, har birini toʻliq kvadratga keltiramiz.)</em></p>

<h3>Worked Example 1 — full process</h3>
<p>Find the center and radius of x<sup>2</sup> + y<sup>2</sup> + 6x − 4y − 3 = 0.</p>
<ul>
  <li>Group: (x<sup>2</sup> + 6x) + (y<sup>2</sup> − 4y) = 3.</li>
  <li>x: half of 6 is 3, squared is 9. y: half of −4 is −2, squared is 4. Add both to each side.</li>
  <li>(x<sup>2</sup> + 6x + 9) + (y<sup>2</sup> − 4y + 4) = 3 + 9 + 4 = 16.</li>
  <li>(x + 3)<sup>2</sup> + (y − 2)<sup>2</sup> = 16 → center <strong>(−3, 2)</strong>, radius √16 = <strong>4</strong>.</li>
</ul>

<h3>Worked Example 2 — only one variable needs work</h3>
<p>Find the center and radius of x<sup>2</sup> + y<sup>2</sup> − 10x + 9 = 0.</p>
<ul>
  <li>Group: (x<sup>2</sup> − 10x) + y<sup>2</sup> = −9.</li>
  <li>x: half of −10 is −5, squared is 25. Add 25 to both sides.</li>
  <li>(x − 5)<sup>2</sup> + y<sup>2</sup> = −9 + 25 = 16 → center <strong>(5, 0)</strong>, radius <strong>4</strong>.</li>
</ul>
<p><em>(Oʻzbekcha: y allaqachon toʻliq kvadrat, faqat x bilan ishlaymiz.)</em></p>

<h3>Worked Example 3 — read the radius carefully</h3>
<p>After completing the square a circle becomes (x − 1)<sup>2</sup> + (y + 3)<sup>2</sup> = 20. State its center and radius.</p>
<ul>
  <li>Center = (1, −3). Radius = √20 = 2√5 ≈ <strong>4.47</strong>.</li>
</ul>
<blockquote>Trap: forgetting to add the new constants to the <em>right</em> side too. The equation must stay balanced, or
the radius comes out wrong. <em>(Oʻzbekcha: qoʻshilgan sonlarni oʻng tomonga ham qoʻshishni unutmang — muvozanat saqlanishi kerak.)</em></blockquote>

<h3>Practice 1</h3>
<p>Find the center and radius of x<sup>2</sup> + y<sup>2</sup> + 8x + 2y + 8 = 0.</p>
<details>
  <summary>Show answer</summary>
  <p>(x<sup>2</sup> + 8x) + (y<sup>2</sup> + 2y) = −8. Add 16 and 1: (x + 4)<sup>2</sup> + (y + 1)<sup>2</sup> = 9.
  Center <strong>(−4, −1)</strong>, radius <strong>3</strong>.</p>
</details>

<h3>Practice 2</h3>
<p>Find the center and radius of x<sup>2</sup> + y<sup>2</sup> − 6y = 0.</p>
<details>
  <summary>Show answer</summary>
  <p>x<sup>2</sup> + (y<sup>2</sup> − 6y) = 0. Add 9: x<sup>2</sup> + (y − 3)<sup>2</sup> = 9.
  Center <strong>(0, 3)</strong>, radius <strong>3</strong>.</p>
</details>

<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>Complete the square</strong> — toʻliq kvadratga keltirish</li>
  <li><strong>Standard form</strong> — standart koʻrinish</li>
  <li><strong>Expanded form</strong> — yoyilgan koʻrinish</li>
  <li><strong>Perfect square</strong> — toʻliq kvadrat</li>
  <li><strong>Center</strong> — markaz</li>
  <li><strong>Radius</strong> — radius</li>
  <li><strong>Group (terms)</strong> — guruhlash (hadlar)</li>
  <li><strong>Balance (the equation)</strong> — muvozanat (tenglama)</li>
  <li><strong>Constant</strong> — oʻzgarmas (ozod had)</li>
</ul>

<h3>Summary</h3>
<ul>
  <li>Group x-terms and y-terms; complete the square on each using <mark>(half of the coefficient)<sup>2</sup></mark>.</li>
  <li>Add the new constants to <strong>both</strong> sides to keep balance.</li>
  <li>Rewrite as (x − h)<sup>2</sup> + (y − k)<sup>2</sup> = r<sup>2</sup>, then read center (h, k) and radius √(right side).</li>
</ul>
""".strip(),
    },
]
