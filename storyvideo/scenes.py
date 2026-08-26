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
