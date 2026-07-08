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

    ready(function () {
        document.documentElement.classList.add("cn-ready");

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
