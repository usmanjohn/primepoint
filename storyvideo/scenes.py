# -*- coding: utf-8 -*-
"""The story beats.

Reading the whole Prime Math shelf, almost every text runs the same arc -- which
is not a coincidence, toc_prime_math_readings.txt asks for it ("the ending is
usually the moment the maths pays off: the right answer, the caught mistake, the
better choice"). So the arc IS the scene vocabulary:

    hook -> count_in -> says -> beat -> claim -> consequence
         -> correct -> check -> rule -> outro

Each builder below returns a Scene. A whole video is a list of them.
"""

from spec import Scene
import primitives as P


def hook(big, label, then=None, then_label=None, ask=None, dur=4.6):
    """Title card. The two numbers of the problem, then the question."""
    h = [P.line(big, "hero", at=0.0, anim="pop", dur=0.7),
         P.line(label, "lbl", at=0.35, anim="rise")]
    if then:
        h.append(P.line(then, "big", at=1.15, anim="pop", dur=0.6))
        h.append(P.line(then_label, "lbl", at=1.45, anim="rise"))
    if ask:
        h.append(P.line(ask, "ask", at=2.35, anim="pop", dur=0.6))
    return Scene(dur, "".join(h), cam="pull", name="hook",
                 note=f"{big} {label}" + (f", {then} {then_label}. {ask}" if ask else ""))


def count_in(n, label, dur=None, named=None, size=104, per_row=7, step=None,
             lead=0.5, note="", cam="rise"):
    """n things appear one at a time while a counter climbs to n.

    The countability primitive. The counter and the objects share one clock, so
    the number on screen is never ahead of the things on screen.
    """
    step = step or min(0.16, 5.6 / max(n, 1))
    body, secs = P.crowd(n, at=lead, step=step, size=size, named=named, per_row=per_row)
    head = P.counters(P.counter(n, label, at=lead, dur=secs, counts=".crowd__c"))
    return Scene(dur or (lead + secs + 1.6), head + body, cam=cam, top=True,
                 name=f"count_in({n})", counts=[n], note=note or f"{n} {label}")


def says(who, lines, dur=6.0, size=250, mood="smile", note="", cam="push"):
    """A character with a speech bubble. lines: [(text, css class), ...]"""
    body = (P.person(who, size=size, mood=mood, at=0.0, anim="rise", dur=0.6)
            + P.bubble(lines, at=0.5))
    return Scene(dur, body, cam=cam, name=f"says({who})",
                 note=note or " / ".join(t for t, _ in lines))


def beat(dur=4.0, n=3, note="Jim turing — tomoshabin oʻzi hisoblasin."):
    """A silent beat with nothing but ticking dots.

    Protected on purpose: after the question and before the answer, the viewer
    needs room to do the sum themselves. This is the one scene that must not be
    filled with motion.
    """
    # Protected means no new INFORMATION, not no motion: with nothing on the
    # audio track a frozen frame reads as a stalled video, so the camera keeps
    # drifting while the viewer works.
    return Scene(dur, P.ticks(n, at=0.9, step=(dur - 1.4) / max(n, 1)),
                 cam="push", name="beat", note=note)


def claim(who, expr, answer, doubt=None, dur=8.0, note=""):
    """Somebody answers -- usually the plausible wrong answer."""
    body = [
        P.person(who, size=210, mood="smile", arms="up", at=0.0, anim="slidel", dur=0.6),
        P.line(who, "lbl", at=0.45, anim="fade"),
        P.expr(expr, at=1.0, anim="pop", dur=0.6),
        P.line("=", "big soft", at=1.9, anim="fade"),
        P.line(f'<span class="hero" style="font-size:{P.fit_px(answer, "hero", 820)}px">'
               f'{answer}</span>', "", at=2.4, anim="pop", dur=0.6),
    ]
    if doubt:
        body.append(P.line(doubt, "ask", at=4.6, anim="pop", dur=0.6))
    return Scene(dur, "".join(body), cam="push", name=f"claim({who})",
                 claims=[expr], note=note or f"{who}: {expr} = {answer}. {doubt or ''}")


def consequence(hero, says_, dur=7.0, mood="sad", above="", above_label="",
                note="", cam="push"):
    """The moment it goes wrong, on one face. The emotional beat of the video."""
    body = []
    if above:
        body.append(P.counters(P.counter(int(above), above_label, at=0.0, dur=0.5)))
    body.append(f'<div class="spot" data-at="0.500" data-dur="0.6" data-anim="pop">'
                f'{P._people.figure(hero, size=340, mood=mood)}</div>')
    body.append(P.line(hero, "ttl", at=1.5, anim="rise"))
    body.append(P.line(says_, "ask", at=2.6, anim="rise"))
    return Scene(dur, "".join(body), cam=cam, name=f"consequence({hero})",
                 note=note or f"{hero}: {says_}")


def correct(frm, to, because, dur=8.5, lead="", note=""):
    """The correction: the wrong answer struck through, the right one beside it."""
    body = []
    if lead:
        body.append(P.expr(lead, at=0.0, anim="rise", dur=0.5))
    # Both numbers share one row, so each gets less than half the content width.
    # "20 000" at the size meant for "7" is three times too wide.
    px = min(P.fit_px(frm, "hero", 380), P.fit_px(to, "hero", 380))
    body.append(
        f'<div class="fix">'
        f'<span class="hero strike" style="font-size:{px}px" data-at="0.900" '
        f'data-dur="0.5" data-anim="fade">{frm}</span>'
        f'<span class="hero red" style="font-size:{px}px" data-at="1.700" '
        f'data-dur="0.6" data-anim="pop">{to}</span>'
        f'</div>')
    body.append(P.card(P.card_expr(because), at=2.9, cls="card--gold", dur=0.55))
    return Scene(dur, "".join(body), cam="push", name=f"correct({frm}->{to})",
                 claims=[because], note=note or f"{frm} emas, {to}. {because}")


def check(expr, parts=None, verdict="Hammasi joyida.", dur=7.5, title="Tekshiramiz",
          note=""):
    """The verification step -- straight out of the story's own grammar block."""
    body = [P.line(title, "lbl lbl--sm", at=0.0, anim="fade"),
            P.expr(expr, at=0.5, anim="pop", dur=0.6)]
    for i, p in enumerate(parts or []):
        body.append(P.line(p, "lbl", at=1.7 + i * 0.7, anim="rise"))
    body.append(P.line(verdict, "ttl grn", at=1.7 + 0.7 * len(parts or []) + 0.9,
                       anim="pop", dur=0.6))
    return Scene(dur, "".join(body), cam="pull", name="check", claims=[expr],
                 note=note or f"Tekshiruv: {expr}")


def rule(pattern, meaning=None, strip=None, dur=9.0, head="Esda tutinglar", note=""):
    """The dark closing card: the rule the story taught.

    Comes from the source story's grammar block, so the video and the reading
    teach exactly the same sentence.
    """
    body = [P.line(head, "lbl lbl--sm", at=0.0, anim="fade"),
            P.line(f'«{pattern}»', "ttl gold", at=0.6, anim="rise", dur=0.6),
            P.card(P.card_expr(strip), at=1.8, cls="card--dark", dur=0.55)
            if strip else ""]
    if meaning:
        body.append(P.line(meaning, "cap", at=3.0, anim="rise"))
    return Scene(dur, "".join(body), cam="push", dark=True, name="rule", note=note or pattern)


def outro(line1="Powerty", line2="matematika hikoyalari", dur=3.4):
    body = (P.line(line1, "ttl gold", at=0.0, anim="pop", dur=0.6)
            + P.line(line2, "lbl lbl--sm", at=0.5, anim="rise"))
    return Scene(dur, body, cam="pull", dark=True, name="outro", note="Kanal nomi.")


def fill(total, per, dur=None, step=0.16, named=None, cols=2, seat_size=58,
         seated_label="oʻtirdi", table_label="stol", tail=None, tail_at=0.0,
         note="", cam="sink", lead=0.4):
    """Seat `total` people `per` table, one seat at a time, with both counters
    climbing as it happens: how many are seated, and how many tables that took.

    This is the scene the whole format exists for -- the quantity is not asserted,
    it is dealt out in front of the viewer and counted while it happens.
    """
    body, secs, n_tables, leftover = P.tables(total, per, at=lead, step=step,
                                              named=named, cols=cols,
                                              seat_size=seat_size)
    head = P.counters(
        P.counter(total, seated_label, at=lead, dur=secs, counts=".seat--full"),
        P.counter(n_tables, table_label, at=lead, dur=secs, cls="gold",
                  counts=".tblbox"),
    )
    out = [head, body]
    if tail:
        out.append(P.line(tail, "ttl", at=tail_at or (lead + secs + 0.5), anim="rise"))
    return Scene(dur or (lead + secs + 2.4), "".join(out), cam=cam, top=True,
                 name=f"fill({total}/{per})", counts=[total, n_tables],
                 note=note or f"{total} kishi, {n_tables} stol, qoldiq {leftover}")


def walk(a, b, unit="m", dur=None, step=0.85, lead=0.6, gate=None,
         total_label="metr", note="", cam="push", tail=None):
    """Walk the boundary of a rectangle, watching the metres add up.

    The counter SUMS the sides that are lit rather than counting them, so the
    running total is a readout of the picture: 18 -> 28 -> 46 -> 56. Seeing it
    pass 28 is the correction of PM-67 happening on screen.
    """
    body, secs = P.rect_walk(a, b, at=lead, step=step, unit=unit, gate=gate)
    head = P.counters(
        f'<div class="count"><b class="counter" data-sum-of=".side" '
        f'data-at="{lead:.3f}" data-dur="0.4" data-anim="pop">0</b>'
        f'<span class="lbl lbl--sm">{total_label}</span></div>')
    out = [head, body]
    if tail:
        out.append(P.line(tail, "ttl", at=lead + secs + 0.9, anim="rise"))
    return Scene(dur or (lead + secs + 3.2), "".join(out), cam=cam, top=True,
                 name=f"walk({a}x{b})", note=note or f"P = 2 × ({a} + {b})")


def versus(left, right, dur=None, lead=0.3, verdict=None, unit_label="",
           title=None, note="", cam="push"):
    """Two options resolved to the same unit, side by side.

    The totals land first and the per-unit figures only afterwards, so the
    viewer has a moment to guess wrong -- which is the point of PM-92.
    """
    body, secs = P.compare(left, right, at=lead + (0.7 if title else 0),
                           verdict=verdict, unit_label=unit_label)
    head = P.line(title, "ttl", at=lead, anim="rise") if title else ""
    return Scene(dur or (lead + secs + 2.0), head + body, cam=cam,
                 name=f"versus({left['name']}/{right['name']})",
                 claims=[c for c in (left.get("claim"), right.get("claim")) if c],
                 note=note or f"{left['name']} vs {right['name']}")


def ask(question, dur=6.4, head=None, note="", cam="push"):
    """The open question — the reading's own `open_question`, held on screen.

    It is the last thing before the outro because it has no answer: nothing that
    follows it could be a reply. On a reading it is the one question a pupil
    cannot get wrong; in a video it is the reason to still be watching.
    """
    body = (P.line(head or "Oʻylab koʻring", "lbl lbl--sm", at=0.0, anim="fade")
            + P.line(question, "ttl", at=0.5, anim="rise", dur=0.6)
            + '<div class="ticks" data-at="2.60" data-dur="0.5" data-anim="fade">'
            + "".join('<span class="tick on"></span>' for _ in range(3)) + '</div>')
    return Scene(dur, body, cam=cam, dark=True, name="ask",
                 note=note or f"Savol: {question} — javobini aytmang.")


# ── Matematika olami: beats for the history films ────────────────────────
# That shelf is a different job. Its texts belong to no lesson and nobody in
# them makes a mistake, so the "hook -> claim -> consequence -> correct" arc
# has nothing to grip. The arc here is:
#
#     place & time  ->  the question  ->  the obstacle  ->  the method
#                   ->  the number    ->  what survives
#
# All three builders are compositions of primitives that already exist -- no new
# CSS, no new drawing code. `rule(head="Nima qoldi")` closes the film.

def era(place, year, line=None, dur=6.4, cam="push", note=""):
    """A dark chapter card: where, and when. The film's punctuation.

    Dark on purpose: it is the only thing in these videos that interrupts, so
    two or three of them give a 75-second film the feel of chapters.
    """
    body = [P.line(place, "lbl lbl--sm", at=0.0, anim="fade"),
            P.line(year, "hero", at=0.45, anim="pop", dur=0.7)]
    if line:
        body.append(P.line(line, "cap", at=1.7, anim="rise"))
    return Scene(dur, "".join(body), cam=cam, dark=True, name=f"era({year})",
                 note=note or f"{place}, {year}. {line or ''}")


def portrait(who, name=None, dates=None, caption="", dur=7.4, size=330,
             mood="smile", cam="push", note=""):
    """The person, standing, with their name and dates under them."""
    body = [f'<div class="spot" data-at="0.000" data-dur="0.7" data-anim="pop">'
            f'{P._people.figure(who, size=size, mood=mood)}</div>',
            P.line(name or who, "ttl", at=0.9, anim="rise", dur=0.6)]
    if dates:
        body.append(P.line(dates, "lbl lbl--sm", at=1.5, anim="fade"))
    if caption:
        body.append(P.line(caption, "cap", at=2.4, anim="rise"))
    return Scene(dur, "".join(body), cam=cam, name=f"portrait({who})",
                 note=note or f"{name or who} — {caption or dates or ''}")


def fact(big, label, cap=None, dur=6.6, cam="pull", dark=False, note=""):
    """One number or one word, held. No arithmetic and no argument -- weight.

    This is the beat the lesson videos do not have: sometimes the right move is
    to stop and let a number sit there.
    """
    body = [P.line(big, "hero", at=0.0, anim="pop", dur=0.7),
            P.line(label, "lbl", at=0.5, anim="rise")]
    if cap:
        body.append(P.line(cap, "cap", at=1.8, anim="rise"))
    return Scene(dur, "".join(body), cam=cam, dark=dark, name=f"fact({big})",
                 note=note or f"{big} — {label}. {cap or ''}")


# ── Koreys: beats for the language films ─────────────────────────────────
# A third register, and it needed its own arc for the same reason Matematika
# olami did. A language reading has no wrong answer to catch, so
# claim -> consequence -> correct has nothing to grip. What a language DOES
# have is structure, and structure is countable:
#
#     the word  ->  where it comes from  ->  what it unlocks  ->  say it
#               ->  the rule  ->  the question  ->  go and practise
#
# Every builder is a composition of wordkit.py, which is to language what
# primitives.py is to maths. Nothing here is decoration: `word_family` counts
# its words with the same counter machinery that counts chairs, so "nine words
# from one syllable" is a quantity the viewer can check, not a claim.

import wordkit as W


def word(hangul, gloss=None, hanja=None, uz=None, dur=6.0, cam="push",
         head=None, dark=False, note="", size=None):
    """One Korean word, held: 한글, how to say it, what it means.

    The transliteration is derived by korean.py rather than typed, so the line
    on screen and the line the voice reads are the same line.
    """
    body = ""
    if head:
        body += P.line(head, "lbl lbl--sm", at=0.0, anim="fade")
    body += W.pron(hangul, gloss=gloss, uz=uz, hanja=hanja,
                   at=0.2 if head else 0.0, size=size)
    return Scene(dur, body, cam=cam, dark=dark, name=f"word({hangul})",
                 note=note or f"{hangul} — {gloss or ''}")


def word_family(root, words, hanja=None, meaning=None, label="ta soʻz",
                dur=None, lead=0.5, step=0.5, cols=2, cam="rise", note=""):
    """A root, and everything it unlocks, dealt out one at a time.

    THE Korean scene. 출(出) gives nine words, and nine is a quantity: the
    counter counts `.fam__w` off the live DOM, so it cannot get ahead of the
    picture. This is the maths format translated into a language rather than
    replaced by one.

    words: [(word, hanja_or_None, gloss), ...]
    """
    grid, secs = W.family(words, root=root, at=lead + 1.0, step=step, cols=cols)
    head = P.counters(P.counter(len(words), label, at=lead + 1.0, dur=secs,
                                counts=".fam__w"))
    card = W.root_card(root, hanja=hanja, meaning=meaning, at=lead)
    return Scene(dur or (lead + 1.0 + secs + 2.0), head + card + grid,
                 cam=cam, top=True, name=f"family({root})",
                 counts=[len(words)],
                 note=note or f"{root} — {len(words)} ta soʻz")


def spell(syllable, caption=None, head=None, dur=6.4, cam="push", note=""):
    """A syllable block taken apart and put back together: ㅎ + ㅏ + ㄴ → 한.

    The one beat in the kit that is a mechanism rather than an arrival. Korean
    writing is a diagram of a syllable; somebody who has only ever seen it as a
    wall of shapes cannot know that until they watch one being built.
    """
    body = P.line(head, "lbl lbl--sm", at=0.0, anim="fade") if head else ""
    grid, secs = W.jamo(syllable, at=0.4 if head else 0.2)
    body += grid
    if caption:
        body += P.line(caption, "cap", at=secs + 0.9, anim="rise")
    return Scene(dur, body, cam=cam, name=f"spell({syllable})",
                 note=note or f"{syllable} = harflardan yigʻiladi")


def shape(zone, line, head=None, dur=7.0, cam="push", note=""):
    """A letter's shape explained by the mouth that makes it.

    ㄱ is the tongue humped at the back of the throat; the letter is a picture
    of that. 훈민정음 해례 says so in as many words, which is why this is a
    diagram of an argument and not an illustration beside one.
    """
    body = P.line(head, "lbl lbl--sm", at=0.0, anim="fade") if head else ""
    body += W.mouth(zone, at=0.3)
    body += P.line(line, "ttl", at=1.6, anim="rise", dur=0.6)
    return Scene(dur, body, cam=cam, name=f"shape({zone})",
                 note=note or line)


def practice(title, sub=None, head="Endi oʻzingiz sinab koʻring",
             dur=5.0, cam="push", note=""):
    """The endcard that sends them somewhere to actually use it.

    It sits AFTER `ask`, which breaks that scene's own rule ("nothing that
    follows it could be a reply") only in appearance: a signpost is not an
    answer. `ask` stays the last idea in the film; this is the door out of it.
    """
    body = (P.line(head, "lbl lbl--sm", at=0.0, anim="fade")
            + W.cta(title, sub, at=0.5))
    return Scene(dur, body, cam=cam, dark=True, name="practice",
                 note=note or f"Powerty: {title}")


def echo(hangul, gloss=None, hanja=None, head="Eshiting va takrorlang",
         dur=None, cam="push", note="", size=None):
    """The protected beat: the word on screen, said twice by a native voice.

    This scene is DELIBERATELY SILENT in `narrate(...)` -- pass None for it.
    That is not a gap in the film, it is the point: `voice.mix` puts narration
    only into scenes that have some, so the hole this leaves is exactly where
    koaudio.py lays the Korean voice. The maths films protect one silent scene
    so the viewer can do the sum; this one protects it so they can say the word
    out loud before the film moves on.
    """
    body = (P.line(head, "lbl lbl--sm", at=0.0, anim="fade")
            + W.pron(hangul, gloss=gloss, hanja=hanja, at=0.5, speak=True,
                     size=size)
            + W.say_again(hangul, at=2.6))
    return Scene(dur or 4.4, body, cam=cam, name=f"echo({hangul})",
                 note=note or f"{hangul} — jim sahna, koreyscha ovoz.")


def order(rows, head=None, verdict=None, dur=None, lead=0.4, step=0.9,
          cam="push", note=""):
    """The same sentence in three languages, aligned in columns.

    rows: [(label, [(text, "s"|"o"|"v"), ...], is_korean), ...]
    """
    body = P.line(head, "lbl lbl--sm", at=0.0, anim="fade") if head else ""
    grid, secs = W.order_strip(rows, at=lead + (0.5 if head else 0), step=step)
    body += grid
    end = lead + secs + 0.6
    if verdict:
        body += P.line(verdict, "ttl", at=end, anim="pop", dur=0.6)
        end += 1.4
    return Scene(dur or (end + 1.6), body, cam=cam, top=True,
                 name="order", note=note or (verdict or "uch tilda bir gap"))


def pairs(items, head=None, tail=None, dur=None, lead=0.4, step=0.6,
          cam="push", note=""):
    """The qoʻshimcha ↔ 조사 table: -ni = 을/를, -ga = 에, -ning = 의."""
    body = P.line(head, "lbl lbl--sm", at=0.0, anim="fade") if head else ""
    grid, secs = W.pair_rows(items, at=lead + (0.4 if head else 0), step=step)
    body += grid
    end = lead + secs + 0.5
    if tail:
        body += P.line(tail, "ttl", at=end, anim="rise", dur=0.6)
        end += 1.4
    return Scene(dur or (end + 1.5), body, cam=cam, name="pairs",
                 note=note or "qoʻshimchalar juft-juft mos keladi")
