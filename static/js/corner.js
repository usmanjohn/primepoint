/* ─────────────────────────────────────────────────────────────────────
   Corner — tap-to-translate for highlighted vocabulary.

   Markup (authored inline in the story body):
       <span class="cn-word" data-tr="uzbek translation">한국어</span>

   Progressive enhancement: adds `cn-ready` to <html>; tapping a word
   shows a small popover with its translation, tapping elsewhere (or the
   same word again) closes it. With JS off the words stay highlighted
   and the full glossary is visible at the end of the story.
   ───────────────────────────────────────────────────────────────────── */
(function () {
    "use strict";

    function ready(fn) {
        if (document.readyState !== "loading") fn();
        else document.addEventListener("DOMContentLoaded", fn);
    }

    /* ── End-of-story comprehension quiz ──────────────────────────────
       Markup (rendered by story_detail.html):
         <div class="cn-q" data-answer="1">
           <button class="cn-opt" data-i="0">…</button> …
           <template class="cn-q-explain">…uzbek explanation…</template>
         </div>
       Tapping a choice grades that question once: marks the picked and the
       correct option, then reveals the verdict + explanation. With JS off the
       choices are plain (inert) buttons and nothing breaks. */
    function initQuiz() {
        document.querySelectorAll("[data-cn-quiz] .cn-q").forEach(function (q) {
            var answer = parseInt(q.getAttribute("data-answer"), 10);
            var opts = Array.prototype.slice.call(q.querySelectorAll(".cn-opt"));

            opts.forEach(function (opt) {
                opt.addEventListener("click", function () {
                    if (q.classList.contains("cn-answered")) return;
                    grade(q, opts, opt, answer);
                });
            });
        });
    }

    function grade(q, opts, picked, answer) {
        q.classList.add("cn-answered");
        var pickedI = parseInt(picked.getAttribute("data-i"), 10);
        var isRight = pickedI === answer;

        opts.forEach(function (opt) {
            opt.disabled = true;
            var i = parseInt(opt.getAttribute("data-i"), 10);
            if (i === answer) opt.classList.add("cn-correct");
            else if (opt === picked) opt.classList.add("cn-wrong");
        });

        var box = document.createElement("div");
        box.className = "cn-feedback " + (isRight ? "cn-is-correct" : "cn-is-wrong");
        var verdict = document.createElement("p");
        verdict.className = "cn-feedback-verdict";
        verdict.textContent = isRight ? "맞았어요! / Toʻgʻri!" : "다시 생각해 봐요 / Notoʻgʻri";
        box.appendChild(verdict);

        var tpl = q.querySelector(".cn-q-explain");
        if (tpl && tpl.innerHTML.trim()) {
            var expl = document.createElement("div");
            expl.className = "cn-feedback-explain";
            expl.innerHTML = tpl.innerHTML;
            box.appendChild(expl);
        }
        q.appendChild(box);
    }

    /* ── Writing-practice fill-in blanks ──────────────────────────────
       Markup (authored inline in the scaffold body):
         <span class="wp-blank" data-answer="증가하였다" data-alt="증가했다|늘었다"></span>
       Each blank becomes a text input; "Check" grades every blank
       (spacing-insensitive, alternatives accepted), "Show the answers"
       fills them in. With JS off the blanks stay as dashed slots and the
       model answer is still available under step 3. */
    function initWriting() {
        var paper = document.querySelector("[data-wp-template]");
        if (!paper) return;
        var blanks = Array.prototype.slice.call(paper.querySelectorAll(".wp-blank"));
        if (!blanks.length) return;

        blanks.forEach(function (blank) {
            var answer = blank.getAttribute("data-answer") || "";
            var input = document.createElement("input");
            input.type = "text";
            input.className = "wp-blank-input";
            input.autocomplete = "off";
            input.autocapitalize = "none";
            input.spellcheck = false;
            input.lang = "ko";
            /* Size the slot to the expected answer (a gentle length hint). */
            input.style.width = Math.min(12, Math.max(3.5, answer.length * 1.1 + 1.6)) + "em";
            blank.textContent = "";
            blank.classList.add("wp-live");
            blank.style.borderBottom = "none";
            blank.style.minWidth = "0";
            blank.appendChild(input);
            input.addEventListener("input", function () {
                input.classList.remove("wp-right", "wp-wrong");
            });
        });

        function norm(s) { return (s || "").replace(/\s+/g, "").trim(); }
        function accepted(blank) {
            var list = [blank.getAttribute("data-answer") || ""];
            var alt = blank.getAttribute("data-alt");
            if (alt) list = list.concat(alt.split("|"));
            return list.map(norm).filter(Boolean);
        }

        var scoreEl = document.querySelector("[data-wp-score]");
        var checkBtn = document.querySelector("[data-wp-check]");
        var solveBtn = document.querySelector("[data-wp-solve]");

        if (checkBtn) checkBtn.addEventListener("click", function () {
            var right = 0;
            blanks.forEach(function (blank) {
                var input = blank.querySelector(".wp-blank-input");
                var ok = accepted(blank).indexOf(norm(input.value)) !== -1;
                input.classList.toggle("wp-right", ok);
                input.classList.toggle("wp-wrong", !ok);
                if (ok) right++;
            });
            if (scoreEl) {
                scoreEl.textContent = right + " / " + blanks.length +
                    (right === blanks.length ? " — 잘했어요! / Ajoyib!" : " toʻgʻri");
            }
        });

        if (solveBtn) solveBtn.addEventListener("click", function () {
            blanks.forEach(function (blank) {
                var input = blank.querySelector(".wp-blank-input");
                input.value = blank.getAttribute("data-answer") || "";
                input.classList.remove("wp-wrong");
                input.classList.add("wp-right");
            });
            if (scoreEl) scoreEl.textContent = "";
        });
    }

    ready(function () {
        document.documentElement.classList.add("cn-ready");
        initQuiz();
        initWriting();

        var pop = null;
        var openWord = null;

        function close() {
            if (pop) { pop.remove(); pop = null; }
            if (openWord) { openWord.classList.remove("cn-open"); openWord = null; }
        }

        function open(word) {
            close();
            var tr = word.getAttribute("data-tr");
            if (!tr) return;
            pop = document.createElement("div");
            pop.className = "cn-pop";
            pop.textContent = tr;
            document.body.appendChild(pop);

            var r = word.getBoundingClientRect();
            var top = r.top + window.scrollY - pop.offsetHeight - 8;
            var left = r.left + window.scrollX + r.width / 2 - pop.offsetWidth / 2;
            left = Math.max(8, Math.min(left, window.scrollX + document.documentElement.clientWidth - pop.offsetWidth - 8));
            pop.style.top = top + "px";
            pop.style.left = left + "px";

            word.classList.add("cn-open");
            openWord = word;
        }

        document.addEventListener("click", function (e) {
            var word = e.target.closest ? e.target.closest(".cn-word") : null;
            if (word && word.getAttribute("data-tr")) {
                if (word === openWord) close();
                else open(word);
            } else {
                close();
            }
        });
    });
})();
