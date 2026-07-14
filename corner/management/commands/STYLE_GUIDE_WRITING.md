# Corner Writing-Practice Guide (for Claude)

This guide tells Claude HOW to write **Corner writing drills** (`/corner/writing/` —
the `WritingPractice` model). Each exam/question-type has its own toc file (e.g.
`toc_topik_writing_53.txt`) listing the drills in order. **Always follow that order.**

> ⚠️ **Korean exam content in Korean (한글); every translation, summary and tip in
> UZBEK — never English.** The audience is Uzbek students preparing for TOPIK II.

A drill has four parts the student walks through in order:

1. **`prompt` + `chart`** — the question exactly as it would look on the exam paper.
2. **`template_body`** — a scaffold answer: ready-made exam expressions are marked
   (tappable translations), and the *data* is blanked out — the student completes it
   by reading the chart.
3. **`model_answer`** — the full answer, revealed on tap.
4. **`tips`** — short strategy notes in Uzbek.

Flashcards are generated automatically from the marked expressions — never write a
separate word list.

---

## 1. Marking expressions and blanks (MOST IMPORTANT)

**Template-ready expressions** use the same span stories use:

```html
<span class="cn-word" data-pos="verb" data-tr="oshmoq, koʻpaymoq">증가하다</span>
```

- Mark the *reusable exam phrases* — the ones that fit ANY chart question:
  `조사를 실시하였다`, `~에 따르면`, `~(으)로 나타났다`, `차지하다`, `뒤를 이었다`,
  `증가하다 / 감소하다`, `~에 비해`, `~(으)ㄹ 것으로 전망된다` …
- `data-tr` = short **Uzbek** translation. `data-pos` = verb/adj/adv or omit.
- Mark each expression only the FIRST time it appears across
  `template_body` + `model_answer` (the word list is built from both, duplicates
  are dropped automatically). **8–15 expressions per drill.**
- Never nest tags inside a `cn-word` span; no double quotes in `data-tr`.

**Blanks** (only in `template_body`):

```html
<span class="wp-blank" data-answer="30%" data-alt="30퍼센트|삼십 퍼센트"></span>
```

- The span is **empty** — JS turns it into a typing box sized to the answer.
- `data-answer` = the expected text; `data-alt` = accepted alternatives, `|`-separated
  (checking ignores all spacing, so don't list spacing variants).
- **Blank the data, not the grammar**: numbers, years, subjects, the survey org,
  and the trend verb (증가/감소) — everything the student must *read off the chart*.
  Keep the connective expressions visible: they are what we're teaching.
- **6–12 blanks** per drill. Never put a blank inside a `cn-word` span.

## 2. The `prompt` (exam instruction)

Exam wording, in Korean, e.g. for 53:

```html
<p>다음을 참고하여 '1인 가구 현황'에 대한 글을 200~300자로 쓰시오.
단, 글의 제목을 쓰지 마시오. <strong>(30점)</strong></p>
```

## 3. The `chart` (pure HTML/SVG — no JS, no images)

Wrap nothing — the page already puts it in a bordered `wp-chart` box. Start with a
title line, then one figure, then optional fact boxes:

```html
<p class="wp-chart-title">1인 가구 비율</p>
```

**Line chart (연도별 변화)** — inline SVG, 3–4 points. Geometry: viewBox
`0 0 480 230`, baseline `y=190`, x at `90/240/390` (3 pts) or `70/183/297/410`
(4 pts), `y = 190 − value/max × 150`. Every point carries its value (the student
must transcribe it):

```html
<svg viewBox="0 0 480 230" role="img" aria-label="1인 가구 비율: 2000년 15%, 2010년 24%, 2020년 32%">
  <line class="wp-axis" x1="40" y1="190" x2="440" y2="190"/>
  <polyline class="wp-line" points="90,120 240,78 390,40"/>
  <circle class="wp-dot" cx="90" cy="120" r="4.5"/>
  <circle class="wp-dot" cx="240" cy="78" r="4.5"/>
  <circle class="wp-dot" cx="390" cy="40" r="4.5"/>
  <text class="wp-val" x="90" y="104">15%</text>
  <text class="wp-val" x="240" y="62">24%</text>
  <text class="wp-val" x="390" y="24">32%</text>
  <text class="wp-tick" x="90" y="212">2000년</text>
  <text class="wp-tick" x="240" y="212">2010년</text>
  <text class="wp-tick" x="390" y="212">2020년</text>
</svg>
```

**Bar chart (순위/비교)** — HTML rows; width = value ÷ max × 100%:

```html
<div class="wp-bars">
  <div class="wp-bar-row"><span class="wp-bar-label">운동</span><span class="wp-bar-track"><span class="wp-bar" style="width:100%"></span></span><span class="wp-bar-val">35%</span></div>
  <div class="wp-bar-row"><span class="wp-bar-label">음악 감상</span><span class="wp-bar-track"><span class="wp-bar" style="width:71%"></span></span><span class="wp-bar-val">25%</span></div>
</div>
```

Two groups (남/여 …): add a legend and pair the rows — second bar gets `wp-b2`,
its row gets `wp-row-sub` and an empty label:

```html
<div class="wp-legend"><span><span class="wp-legend-chip"></span>남자</span><span><span class="wp-legend-chip wp-b2"></span>여자</span></div>
<div class="wp-bars">
  <div class="wp-bar-row"><span class="wp-bar-label">드라마</span><span class="wp-bar-track"><span class="wp-bar" style="width:90%"></span></span><span class="wp-bar-val">45%</span></div>
  <div class="wp-bar-row wp-row-sub"><span class="wp-bar-label"></span><span class="wp-bar-track"><span class="wp-bar wp-b2" style="width:100%"></span></span><span class="wp-bar-val">50%</span></div>
  ...
</div>
```

**Fact boxes** (the 원인 / 전망 hints 53 usually provides):

```html
<div class="wp-facts">
  <div class="wp-fact"><span class="wp-fact-tag">원인</span><ul><li>결혼에 대한 인식 변화</li><li>고령 인구 증가</li></ul></div>
  <div class="wp-fact"><span class="wp-fact-tag">전망</span><ul><li>2030년 40%에 이를 것</li></ul></div>
</div>
```

Colors are handled by CSS (`--wp-s1`/`--wp-s2`, validated for both light and dark
mode) — never hard-code fills or use other colors.

## 4. `template_body` and `model_answer`

TOPIK 53 answers follow a fixed skeleton — teach it every time:

1. **조사 개요** — 기관이 대상으로 무엇을 조사했는지 (`…을/를 대상으로 …에 대한 조사를 실시하였다`).
2. **결과** — the numbers/trend (`그 결과 …이/가 …%로 가장 많았으며, …이/가 뒤를 이었다`
   or `…에서 …(으)로 증가하였다`).
3. **원인** — from the fact box (`이러한 변화가 나타난 원인으로는 … 등을 들 수 있다`).
4. **마무리/전망** — (`…(으)ㄹ 것으로 전망된다`).

- `template_body` = that skeleton as `<p>` paragraphs with the data blanked out.
- `model_answer` = the same text complete, natural, **200~300자** (문어체:
  `-(느)ㄴ다/-였다` style, never `-아요/어요`). End it with a character-count note:
  `<p class="small text-secondary">(약 XXX자)</p>`.
- The two must tell the same story — a student who filled the blanks correctly has
  effectively *written* the model answer.

## 5. `tips` (Uzbek, short)

3–5 `<li>` bullets: what the grader wants, which pattern to reuse, common mistakes
(spoken style, missing 전망, copying the prompt). HTML `<ul>` only.

## 6. Data file shape

Write batches into `corner/management/commands/_writing_<exam><qtype>_<range>.py`:

```python
SUBJECT   = {...}   # copy from the toc header / previous batch
PRACTICES = [{"qtype": "53", "title": "53-1: ...", "summary": ..., "order": N,
              "prompt": ..., "chart": ..., "template_body": ...,
              "model_answer": ..., "tips": ...}, ...]
```

`order` = the drill's number in the toc file. Import with:

```
python manage.py import_writing corner/management/commands/_writing_<...>.py --author=<AUTHOR>
```

(`--republish` overwrites existing drills and rebuilds their expression lists.)

## 7. Question types 51 / 52 (㉠/㉡ 빈칸 채우기)

Same model, same flow. `chart` holds the **passage** (styled like the exam paper),
the gaps written as `( <span class="wp-slot">㉠</span> )` / `( <span class="wp-slot">㉡</span> )`.

**51** = a real-life text (10점). Reproduce the exam design:

```html
<!-- email / invitation: header rows + passage -->
<div class="wp-mail">
  <div class="wp-mail-row"><span>제목</span><span>집들이에 초대합니다</span></div>
  <div class="wp-mail-row"><span>보낸 사람</span><span>왕밍</span></div>
</div>
<div class="wp-passage"><p>안녕하세요? ... ( <span class="wp-slot">㉠</span> ). ...</p></div>

<!-- text messages: bubbles (wp-me = the right-hand speaker) -->
<div class="wp-chat">
  <p class="wp-chat-name">지영</p><div class="wp-bubble"><p>...( <span class="wp-slot">㉠</span> )?</p></div>
  <p class="wp-chat-name wp-me">민수</p><div class="wp-bubble wp-me"><p>...</p></div>
</div>

<!-- notice / bulletin post: just the passage box, optionally with a centred title -->
<div class="wp-passage"><p class="wp-passage-title">회원 모집</p><p>...</p></div>
```

**52** = a short explanatory text (10점) — a plain `wp-passage` box, written style
(`-(느)ㄴ다`), no title.

- `template_body` = one **sentence frame per gap**: repeat the passage sentence that
  contains the gap, with the answer chunk as a `wp-blank`; prefix each frame with
  `<span class="wp-frame-label">㉠</span>`. Give generous `data-alt` — graders accept
  several endings (checking ignores spacing).
- `model_answer` = per gap: the frame label, the full answer sentence (with `cn-word`
  marks on the reusable grammar chunks), then accepted variants on a
  `<p class="wp-alt">(또는: ... / ...)</p>` line.
- What to teach: **the clues** — the connective before/after the gap (그래서/그런데/
  하지만/따라서), the sentence-final patterns (51: `-(으)려고 합니다`, `-아/어 주시기
  바랍니다`, `-(으)ㄹ까요?`; 52: `-는 것이 좋다`, `-기 때문이다`, `-(으)ㄹ 수 있다`),
  and speech level: 51 = polite `-습니다/-아요` matching the text, 52 = plain written
  `-(느)ㄴ다`. Put this reasoning in the Uzbek `tips`.
- Vocabulary marks live in `template_body` + `model_answer` only (the passage in
  `chart` is never synced) — **5–10 expressions** per drill.

## 7b. Question type 54 (600~700자 essay, 50점)

The hardest question — the drill teaches a **reusable essay skeleton**, not just one
answer. Rotate the essay type across drills (중요성+방법 / 가치 / 찬반·장단점 /
문제-원인-해결 / 조건형) so students collect a frame for each.

- `prompt`: `<p>다음을 주제로 하여 자신의 생각을 600~700자로 글을 쓰시오. 단, 문제를
  그대로 옮겨 쓰지 마시오. <strong>(50점)</strong></p>`
- `chart` = the exam topic box: a `wp-passage` with the 2–3-sentence topic paragraph
  ending in `...에 대해 아래의 내용을 중심으로 자신의 생각을 쓰라.` plus a `<ul>` of
  the 과제 questions. No title.
- `template_body` = the full essay as **four labelled paragraphs** — each opens with
  `<p class="wp-part">서론</p>` / `본론 1` / `본론 2` / `결론`. Mark the frame
  expressions (`-는 데 중요한 역할을 한다`, `그렇다면 ~은 왜 …가?`, `왜냐하면 …기
  때문이다`, `예를 들어`, `이처럼`, `지금까지 ~에 대해 살펴보았다`, `-아/어야 할
  것이다` …) with `cn-word` spans. **What to blank (8–12):** (a) the topic's key
  words where they must be copied from the question box, and (b) structural glue on
  its *second* exposure — show the pattern once marked, blank it when the parallel
  slot recurs (먼저 → blank 다음으로; 서론's 때문이다 → blank 본론's). Answers stay
  1–4 words; never blank a whole clause.
- `model_answer` = the same essay complete, **600~700자** (count the tag-stripped
  text, excluding the `wp-part` labels and the final note), written style, with the
  same `wp-part` labels and `cn-word` marks; end with
  `<p class="small text-secondary">(약 NNN자)</p>`.
- `tips` (Uzbek, 4–6 bullets): the skeleton for THIS essay type, paragraph
  proportions (서론 ~20% / 본론 ~60% / 결론 ~20%), the "don't copy the prompt
  sentence" penalty, 문어체 only, and time advice (~25–30 min, outline first).

## 8. The user's own tips

(These override the generic advice above. Empty so far — add them here when the
user shares their TOPIK writing advice.)
