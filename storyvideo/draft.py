# -*- coding: utf-8 -*-
"""Spec skeleton from a Corner reading.

The visual is a creative act and cannot be inferred from prose, so this does NOT
try to write the video. What it does is lift the parts that are already decided
by the source text -- the title, the rule, the arithmetic the story checked --
so those are never retyped and never drift away from the reading they came from.

The middle beats are left as TODO for a human to write.

    python -m storyvideo draft 4
"""

import glob
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
GLOB = str(REPO / "corner/management/commands/_stories_prime_math_*.py")


def find_story(order):
    for path in sorted(glob.glob(GLOB)):
        ns = {}
        exec(compile(pathlib.Path(path).read_text(encoding="utf-8"), path, "exec"), ns)
        for st in ns.get("STORIES", []):
            if st.get("order") == order:
                return st, path
    raise SystemExit(f"no Prime Math reading with order {order}")


def _plain(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()


def draft(order):
    st, path = find_story(order)
    gram = st.get("grammar") or []

    # The rule card and the check line come straight from the story's grammar
    # block, so the video teaches the reading's own sentence.
    rule_pattern = _plain(gram[0]["pattern"]) if gram else "TODO"
    rule_meaning = _plain(gram[0].get("meaning", "")).split(".")[0] + "." if gram else ""
    examples = [_plain(e) for g in gram for e in g.get("examples", [])]
    check_expr = examples[-1] if examples else "TODO = TODO"

    terms = re.findall(r'data-tr="([^"]*)">([^<]*)</span>', st["body"])
    para = [_plain(p) for p in re.findall(r"<p>(.*?)</p>", st["body"], re.S)][:4]

    lines = [
        '# -*- coding: utf-8 -*-',
        f'"""PM-{order} — «{st["title"]}»',
        "",
        f'Manba: {pathlib.Path(path).name}, order {order}.',
        f'{st.get("summary", "").strip()}',
        '"""',
        "",
        "from spec import Video",
        "from scenes import hook, count_in, says, beat, claim, fill, consequence, \\",
        "                   correct, check, rule, outro",
        "",
        f"VIDEO = Video(",
        f'    slug="pm{order:02d}",',
        f'    lesson="PM-{order}",',
        f'    title="{st["title"]}",',
        f'    story="Prime Math Readings — order {order}",',
        "    scenes=[",
        "        # TODO — the opening numbers and the question they raise",
        '        hook("TODO", "TODO", ask="TODO?"),',
        "",
        "        # TODO — the middle beats. What quantity can be dealt out and",
        "        #        counted? What is the plausible wrong move? Who pays for it?",
        "",
        f'        check("{check_expr}",',
        "              parts=[" + ", ".join(f'"{e}"' for e in examples[:-1]) + "],",
        '              verdict="Hammasi joyida."),',
        "",
        f'        rule("{rule_pattern}",',
        f'             meaning="{rule_meaning}"),',
        "",
        "        outro(),",
        "    ],",
        ")",
        "",
        "# ── from the reading, for reference while writing the middle ──",
    ]
    if examples:
        lines.append("# arithmetic the story did: " + " | ".join(examples))
    if terms:
        lines.append("# atamalar: " + ", ".join(f"{w} = {t}" for t, w in terms[:6]))
    for p in para:
        lines.append("#   " + p[:100])
    return "\n".join(lines)
