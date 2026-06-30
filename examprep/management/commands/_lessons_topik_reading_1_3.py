# Starter batch: TOPIK II Reading lessons 1–3.
# Import: python manage.py import_examprep examprep/management/commands/_lessons_topik_reading_1_3.py --author=prime
# (add --republish to overwrite existing ones). See STYLE_GUIDE_TOPIK.md for the rules.

TRACK = {
    "name":    "TOPIK",
    "summary": "Step-by-step preparation for the TOPIK II Korean proficiency exam — "
               "Reading, Writing and Listening, with strategy and practice.",
    "icon":    "bi-flag",
    "color":   "#3b82f6",
    "order":   1,
}

LESSONS = [
    {
        "skill":   "reading",
        "title":   "TOPIK Reading 1: How TOPIK Reading Works",
        "summary": "The shape of the Reading section — 50 questions in 70 minutes — and the "
                   "mindset that keeps you on time.",
        "order":   1,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Reading 1: How TOPIK Reading Works</h2>
<p><strong>What this lesson covers:</strong> before any strategy, you need a clear map of
the Reading (읽기) section — how many questions, how much time, and how the difficulty
climbs. Knowing the shape of the test is the first real strategy.
<em>(Oʻzbekcha: avval imtihonning tuzilishini biling — bu ham strategiya.)</em></p>
""",
            },
            {
                "rich_text": """
<h3>The basic facts</h3>
<ul>
  <li><strong>50 questions</strong> in <strong>70 minutes</strong> — that is about
      <mark>1 minute 24 seconds per question</mark> on average.</li>
  <li>Questions get <strong>harder as the numbers go up</strong>. The early items
      (1–20) are short and fast; the later ones (40–50) are long passages with two
      questions each.</li>
  <li>Every question is <strong>multiple choice</strong>, four options, one answer.</li>
</ul>
<blockquote>Tip: spend <em>less</em> than a minute on the easy early questions so you
bank time for the long passages at the end. <em>(Oʻzbekcha: oson savollarga kam vaqt
sarflang, oxiridagi uzun matnlar uchun vaqt tejang.)</em></blockquote>
""",
            },
            {
                "rich_text": """
<h3>How to pace yourself</h3>
<p>A simple checkpoint plan keeps you safe: by minute 20 you should be near question 20,
and by minute 45 near question 35. If you fall behind, <strong>guess and move on</strong> —
a blank costs the same as a wrong answer, but a blank can never be right.
<em>(Oʻzbekcha: agar orqada qolsangiz, taxmin qiling va keyingisiga oʻting.)</em></p>
<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>읽기 (Reading)</strong> — oʻqish</li>
  <li><strong>Passage</strong> — matn / parcha</li>
  <li><strong>Pacing</strong> — vaqtni taqsimlash</li>
  <li><strong>Checkpoint</strong> — nazorat nuqtasi</li>
  <li><strong>Multiple choice</strong> — variantli savol</li>
  <li><strong>To guess</strong> — taxmin qilmoq</li>
</ul>
<h3>Summary</h3>
<ul>
  <li>50 questions, 70 minutes, difficulty rises with the number.</li>
  <li>Be fast and early, slow and careful late.</li>
  <li>Never leave a blank — guessing is free.</li>
</ul>
""",
            },
            {
                "rich_text": "<p><strong>Quick check:</strong> You have spent 30 minutes "
                             "and you are only on question 15. What is the best move?</p>",
                "choices": [
                    {"text": "Keep going slowly to make sure 1–15 are perfect.", "is_correct": False},
                    {"text": "Speed up and guess where needed to reach the long passages in time.", "is_correct": True},
                    {"text": "Skip straight to question 50 and work backwards.", "is_correct": False},
                    {"text": "Stop reading and fill every remaining answer with option 2.", "is_correct": False},
                ],
                "explanation": "<p>You are behind pace (should be near Q20 by minute 20). "
                               "Speeding up and guessing protects your time for the high-value "
                               "long passages at the end, where two questions share one text. "
                               "<em>(Oʻzbekcha: tezlashing va kerak boʻlsa taxmin qiling.)</em></p>",
            },
        ],
    },
    {
        "skill":   "reading",
        "title":   "TOPIK Reading 2: Skimming for the Main Idea",
        "summary": "Read a passage quickly for its central point (중심 생각) instead of "
                   "translating every word.",
        "order":   2,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Reading 2: Skimming for the Main Idea</h2>
<p><strong>What this lesson covers:</strong> many test-takers lose time trying to
understand every word. The skill that scores points is <mark>skimming</mark> — reading
quickly to catch the <strong>main idea (중심 생각)</strong>.
<em>(Oʻzbekcha: har bir soʻzni tarjima qilmang — asosiy fikrni tushuning.)</em></p>
""",
            },
            {
                "rich_text": """
<h3>Where the main idea hides</h3>
<p>In Korean expository writing the main point is usually in the <strong>first or last
sentence</strong>. The middle gives examples and details. So you can often understand a
paragraph by reading its edges carefully and the middle quickly.</p>
<blockquote>Look for opinion signals: <strong>-아야/어야 한다</strong> (must/should),
<strong>중요하다</strong> (is important), <strong>따라서</strong> (therefore). These
mark the writer's point. <em>(Oʻzbekcha: bu soʻzlar muallifning fikrini bildiradi.)</em></blockquote>
""",
            },
            {
                "rich_text": """
<h3>Worked example</h3>
<blockquote>요즘 사람들은 시간이 없다는 이유로 아침을 거르는 경우가 많다. 그러나 아침 식사는
하루의 활동에 필요한 에너지를 준다. <strong>따라서 바쁘더라도 아침을 꼭 먹는 것이 좋다.</strong></blockquote>
<p>Skim it: the first sentence states a habit (skipping breakfast), the middle gives a
reason breakfast matters, and the last sentence — signalled by <strong>따라서</strong> —
delivers the point: <em>you should eat breakfast even when busy.</em> That last sentence
is the main idea. <em>(Oʻzbekcha: oxirgi gap — asosiy fikr.)</em></p>
<h3>Common mistake</h3>
<p>Don't be trapped by a detail that appears in the middle. An answer choice can be
<em>true but not the main idea</em>. The question asks for the central thought, not any
correct fact.</p>
<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>중심 생각 (main idea)</strong> — asosiy fikr</li>
  <li><strong>To skim</strong> — tez koʻzdan kechirmoq</li>
  <li><strong>따라서 (therefore)</strong> — shuning uchun</li>
  <li><strong>그러나 (however)</strong> — lekin</li>
  <li><strong>Detail</strong> — tafsilot</li>
  <li><strong>Expository text</strong> — izohli matn</li>
</ul>
<h3>Summary</h3>
<ul>
  <li>Skim for the main idea; don't translate every word.</li>
  <li>The point is usually in the first or last sentence.</li>
  <li>A true detail is not always the main idea.</li>
</ul>
""",
            },
            {
                "rich_text": "<p><strong>Practice:</strong> A paragraph ends with "
                             "“<strong>그러므로 규칙적인 운동이 건강에 가장 중요하다.</strong>” "
                             "What is the main idea?</p>",
                "choices": [
                    {"text": "Many people are busy these days.", "is_correct": False},
                    {"text": "Regular exercise is the most important thing for health.", "is_correct": True},
                    {"text": "Exercise can sometimes cause injury.", "is_correct": False},
                    {"text": "Health is difficult to measure.", "is_correct": False},
                ],
                "explanation": "<p>The closing sentence is signalled by <strong>그러므로</strong> "
                               "(therefore) and states the writer's point directly: regular "
                               "exercise is most important for health. The other options may be "
                               "details or distractions, not the central idea. "
                               "<em>(Oʻzbekcha: “그러므로” bilan boshlangan oxirgi gap — asosiy fikr.)</em></p>",
            },
        ],
    },
    {
        "skill":   "reading",
        "title":   "TOPIK Reading 3: Read the Question Before the Passage",
        "summary": "Turn the question and answer choices into a search target so you read "
                   "the passage with a purpose.",
        "order":   3,
        "blocks": [
            {
                "rich_text": """
<h2>TOPIK Reading 3: Read the Question Before the Passage</h2>
<p><strong>What this lesson covers:</strong> a simple habit that saves time on almost
every item — read the <strong>question and the four choices first</strong>, then read the
passage looking for that specific information.
<em>(Oʻzbekcha: avval savol va variantlarni oʻqing, keyin matnni.)</em></p>
""",
            },
            {
                "rich_text": """
<h3>Why it works</h3>
<p>When you read the passage blind, you remember nothing specific and have to read it
again to answer. When you read the question first, your brain has a <mark>search
target</mark> — you notice the relevant sentence the moment you reach it.</p>
<ul>
  <li><strong>Detail question</strong> (일치하는 내용) → hunt for the matching fact.</li>
  <li><strong>Main idea question</strong> (중심 생각) → watch the first/last sentence.</li>
  <li><strong>Blank question</strong> (빈칸) → read for the logic around the gap.</li>
</ul>
<blockquote>Underline a keyword from the question (a name, a number, a topic word) and
scan for it in the text. <em>(Oʻzbekcha: savoldagi kalit soʻzni matndan qidiring.)</em></blockquote>
""",
            },
            {
                "rich_text": """
<h3>Worked example of the habit</h3>
<p>Suppose the question is “이 글의 내용과 같은 것을 고르십시오” (choose what matches the
text) and one choice mentions <strong>할인 (discount)</strong>. Before reading the whole
notice, you already know to look for any sentence about a discount. You find it, check it
against the choice, and answer — without re-reading the rest.</p>
<h3>Common mistake</h3>
<p>Reading the choices first does <em>not</em> mean guessing from the choices alone. The
choices are your <strong>search list</strong>, but you still confirm the answer in the
passage. TOPIK loves choices that are <em>almost</em> right.
<em>(Oʻzbekcha: javobni baribir matndan tasdiqlang.)</em></p>
<h3>Key words — Kalit soʻzlar</h3>
<ul>
  <li><strong>일치하는 내용 (matching content)</strong> — mos keladigan mazmun</li>
  <li><strong>빈칸 (blank)</strong> — boʻsh joy</li>
  <li><strong>Search target</strong> — qidiruv nishoni</li>
  <li><strong>To scan</strong> — tez qidirib oʻqimoq</li>
  <li><strong>할인 (discount)</strong> — chegirma</li>
  <li><strong>Keyword</strong> — kalit soʻz</li>
</ul>
<h3>Summary</h3>
<ul>
  <li>Read the question and choices first, then the passage.</li>
  <li>Underline a keyword and scan for it.</li>
  <li>Always confirm the answer in the text — beware “almost right” choices.</li>
</ul>
""",
            },
            {
                "rich_text": "<p><strong>Practice:</strong> Why is reading the four answer "
                             "choices before the passage helpful?</p>",
                "choices": [
                    {"text": "So you can pick an answer without reading the passage at all.", "is_correct": False},
                    {"text": "It gives you keywords to scan for, so you read with a purpose.", "is_correct": True},
                    {"text": "Because the first choice is usually correct.", "is_correct": False},
                    {"text": "It lets you skip the hardest questions automatically.", "is_correct": False},
                ],
                "explanation": "<p>The choices act as a search list: they tell you which "
                               "keywords and facts to look for, so you read the passage with a "
                               "clear target instead of reading it twice. You still confirm the "
                               "answer in the text. <em>(Oʻzbekcha: variantlar qidiruv roʻyxati "
                               "boʻlib xizmat qiladi.)</em></p>",
            },
        ],
    },
]
