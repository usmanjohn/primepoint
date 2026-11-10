# -*- coding: utf-8 -*-
"""Shared by mj08s / mj08j — five pirates, 100 gold coins, a vote.

The allocations shown are computed by backward induction here, not typed in, and
the same function is asserted against hand values in verify_batch2.py.
"""
import stagekit as K

CREW = [("Bobo", "Kapitan"), ("Anvar aka", "2"), ("Farrux", "3"), ("Otabek", "4"), ("Sardor", "5")]
XS = [130, 325, 520, 715, 910]
FEET = 1440


def split(n, coins=100):
    """Backward induction: allocation for the last n pirates (index 0 = proposer)."""
    if n == 1:
        return [coins]
    prev = split(n - 1, coins)
    need = (n + 1) // 2 - 1
    cheap = sorted(range(n - 1), key=lambda i: prev[i])[:need]
    alloc = [0] * (n - 1)
    for i in cheap:
        alloc[i] = prev[i] + 1
    return [coins - sum(alloc)] + alloc


def deck(n_from=0, alloc=None, votes=None, at=0.5, overboard=False, dim=()):
    """Pirates n_from..4 on deck; alloc/votes for those pirates, in order."""
    st = K.Stage(bg="sea")
    st.add('<div class="sk-deck"></div>', 540, FEET + 90, 1080, 180)
    pir = []
    for i, (who, rank) in enumerate(CREW):
        p = st.add(K.pirate(who, size=280, rank="" if rank == "Kapitan" else rank),
                   XS[i], FEET - 140, 160, 280, z=3, o=0.25 if i < n_from or i in dim else 1)
        pir.append(p)
    if alloc:
        for k, v in enumerate(alloc):
            i = n_from + k
            st.extra.append(f'<div class="sk-t" style="transform:translate({XS[i]}px,{FEET - 350}px)">'
                            f'<div data-at="{at + k * 0.35:.3f}" data-dur="0.4" data-anim="pop">'
                            f'<b class="sk-gold">{v}</b></div></div>')
            st.mark("ck-drop", at + k * 0.35)
        at += len(alloc) * 0.35 + 0.4
    if votes:
        for k, v in enumerate(votes):
            i = n_from + k
            st.tag("ha" if v else "yoʻq", XS[i], FEET - 410, at + k * 0.25, red=not v)
        at += len(votes) * 0.25 + 0.5
    if overboard:
        pir[n_from].to(at, 1.2, x=200, y=FEET + 300, r=-70)
        pir[n_from].to(at + 1.0, 0.3, o=0)
        st.mark("rk-eat", at + 1.1)
        at += 1.4
    st.end = max(st.end, at)
    return st
