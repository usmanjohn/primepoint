/* ============================================================================
   Exam-prep interactive component kit — vanilla JS, no dependencies.

   Progressive enhancement over the server-rendered lesson:
     • Instant-feedback MCQ  — grades each question on click, no page reload.
                               Falls back to the server "Check answers" form
                               POST when JS is off.
     • Step reveal           — <div class="pp-steps" data-pp-steps>
     • Flashcards            — <div class="pp-flashcards" data-pp-flashcards>

   Loaded only on examprep lesson pages (see lesson_detail.html).
   ============================================================================ */
(function () {
    "use strict";

    function ready(fn) {
        if (document.readyState !== "loading") fn();
        else document.addEventListener("DOMContentLoaded", fn);
    }

    /* ── Instant-feedback MCQ ─────────────────────────────────────────── */
    function initMCQ() {
        var form = document.querySelector("[data-pp-lesson]");
        if (!form) return;

        var mcqs = form.querySelectorAll("[data-pp-mcq]");
        if (!mcqs.length) return;

        // JS takes over grading, so hide the server-side "Check answers" button.
        var submit = form.querySelector("[data-pp-submit]");
        if (submit) submit.hidden = true;
        // Never let Enter/submit round-trip to the server once JS is active.
        form.addEventListener("submit", function (e) { e.preventDefault(); });

        var txt = {
            correct: form.getAttribute("data-pp-correct-text") || "Correct!",
            wrong:   form.getAttribute("data-pp-wrong-text")   || "Not quite.",
            score:   form.getAttribute("data-pp-score-text")   || "Score"
        };

        var total = mcqs.length;
        var answered = 0;
        var right = 0;

        mcqs.forEach(function (mcq) {
            var choices = Array.prototype.slice.call(
                mcq.querySelectorAll("[data-pp-choice]")
            );
            var inputs = choices.map(function (c) { return c.querySelector("input[type=radio]"); });

            inputs.forEach(function (input) {
                if (!input) return;
                input.addEventListener("change", function () {
                    if (mcq.classList.contains("pp-answered")) return;
                    grade(mcq, choices, inputs, input);
                });
            });
        });

        function grade(mcq, choices, inputs, picked) {
            mcq.classList.add("pp-answered");

            var pickedLabel = picked.closest("[data-pp-choice]");
            var isRight = pickedLabel.hasAttribute("data-pp-correct");

            choices.forEach(function (label, i) {
                if (inputs[i]) inputs[i].disabled = true;
                if (label.hasAttribute("data-pp-correct")) {
                    label.classList.add("pp-correct");
                    appendMark(label, "✓");        // ✓
                } else if (label === pickedLabel) {
                    label.classList.add("pp-wrong");
                    appendMark(label, "✗");        // ✗
                }
            });

            // Reveal verdict + explanation (cloned from the inert <template>).
            var tpl = mcq.parentNode.querySelector("[data-pp-explain]");
            var box = document.createElement("div");
            box.className = "pp-feedback " + (isRight ? "pp-is-correct" : "pp-is-wrong");
            var verdict = document.createElement("p");
            verdict.className = "pp-feedback-verdict";
            verdict.textContent = isRight ? txt.correct : txt.wrong;
            box.appendChild(verdict);
            if (tpl && tpl.innerHTML.trim()) {
                var expl = document.createElement("div");
                expl.className = "pp-feedback-explain";
                expl.appendChild(tpl.content.cloneNode(true));
                box.appendChild(expl);
            }
            mcq.parentNode.insertBefore(box, tpl ? tpl.nextSibling : mcq.nextSibling);

            answered += 1;
            if (isRight) right += 1;
            if (answered === total) showScore();
        }

        function appendMark(label, sym) {
            var span = label.querySelector(".pp-mark");
            if (!span) {
                span = document.createElement("span");
                span.className = "pp-mark";
                label.appendChild(span);
            }
            span.textContent = sym;
        }

        function showScore() {
            if (form.querySelector(".pp-score")) return;
            var chip = document.createElement("div");
            chip.className = "pp-score mt-2";
            chip.textContent = txt.score + ": " + right + " / " + total;
            (submit ? submit.parentNode : form).appendChild(chip);
        }
    }

    /* ── Step reveal ──────────────────────────────────────────────────── */
    function initSteps() {
        document.querySelectorAll("[data-pp-steps]").forEach(function (wrap) {
            var steps = Array.prototype.slice.call(wrap.querySelectorAll(".pp-step"));
            if (steps.length < 2) { steps.forEach(function (s) { s.classList.add("pp-shown"); }); return; }

            var shown = 1;
            steps.forEach(function (s, i) { if (i === 0) s.classList.add("pp-shown"); });

            var moreLabel = wrap.getAttribute("data-pp-more") || "Show next step";
            var wrapMore = document.createElement("div");
            wrapMore.className = "pp-steps-more";
            var btn = document.createElement("button");
            btn.type = "button";
            btn.className = "btn btn-sm btn-outline-primary";
            btn.textContent = moreLabel;
            var progress = document.createElement("span");
            progress.className = "pp-steps-progress";
            wrapMore.appendChild(btn);
            wrapMore.appendChild(progress);
            wrap.appendChild(wrapMore);

            function render() {
                progress.textContent = shown + " / " + steps.length;
                if (shown >= steps.length) wrapMore.remove();
            }
            btn.addEventListener("click", function () {
                if (shown < steps.length) {
                    steps[shown].classList.add("pp-shown");
                    shown += 1;
                    render();
                }
            });
            render();
        });
    }

    /* ── Flashcards ───────────────────────────────────────────────────── */
    function initFlashcards() {
        document.querySelectorAll("[data-pp-flashcards]").forEach(function (deck) {
            var cards = Array.prototype.slice.call(deck.querySelectorAll(".pp-card"));
            if (!cards.length) return;

            var i = 0;
            cards.forEach(function (c) {
                c.addEventListener("click", function () { c.classList.toggle("pp-flipped"); });
            });

            var nav = document.createElement("div");
            nav.className = "pp-flashcards-nav";
            var prev = navBtn("←");
            var count = document.createElement("span");
            count.className = "pp-flashcards-count";
            var next = navBtn("→");
            nav.appendChild(prev); nav.appendChild(count); nav.appendChild(next);
            deck.appendChild(nav);

            function show(n) {
                cards[i].classList.remove("pp-active", "pp-flipped");
                i = (n + cards.length) % cards.length;
                cards[i].classList.add("pp-active");
                count.textContent = (i + 1) + " / " + cards.length;
            }
            prev.addEventListener("click", function () { show(i - 1); });
            next.addEventListener("click", function () { show(i + 1); });
            show(0);

            function navBtn(sym) {
                var b = document.createElement("button");
                b.type = "button";
                b.className = "btn btn-sm btn-outline-secondary";
                b.textContent = sym;
                return b;
            }
        });
    }

    ready(function () {
        document.documentElement.classList.add("pp-ready");
        initMCQ();
        initSteps();
        initFlashcards();
    });
})();
