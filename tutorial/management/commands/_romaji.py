# -*- coding: utf-8 -*-
"""Kana -> Hepburn romanisation, for the Prime Japanese answer gate.

Not a management command (leading underscore), not imported by Django — the same
arrangement as `_svgkit.py`. Its only job is to let a batch's throwaway
`verify_pj_<range>.py` re-derive every reading answer by a SECOND route, so a typo
in a lesson cannot also be a typo in the check.

Run it directly to execute the self-test:  python3 _romaji.py

Two mechanics that look alike on the page and are easy to conflate — both were
bugs here before the self-test caught them:
  * yoon (small ya/yu/yo) inserts a y:   ki + ya -> kya   (but sha/cha/ja do not)
  * small plain vowels replace it:       fu + a  -> fa,  de + i -> di
And two Hepburn subtleties:
  * `ii` and `ei` are NOT collapsed to macrons - 大きい is "ookii" -> ōkii and
    先生 is "sensei", because those spellings straddle a morpheme boundary.
    Only aa / uu / oo / ou take a macron.
  * the katakana length mark `ー` ALWAYS produces a macron; it is an explicit
    length mark, not a spelling accident.
"""
import re

BASE = {
    'あ':'a','い':'i','う':'u','え':'e','お':'o',
    'か':'ka','き':'ki','く':'ku','け':'ke','こ':'ko',
    'さ':'sa','し':'shi','す':'su','せ':'se','そ':'so',
    'た':'ta','ち':'chi','つ':'tsu','て':'te','と':'to',
    'な':'na','に':'ni','ぬ':'nu','ね':'ne','の':'no',
    'は':'ha','ひ':'hi','ふ':'fu','へ':'he','ほ':'ho',
    'ま':'ma','み':'mi','む':'mu','め':'me','も':'mo',
    'や':'ya','ゆ':'yu','よ':'yo',
    'ら':'ra','り':'ri','る':'ru','れ':'re','ろ':'ro',
    'わ':'wa','を':'o','ん':'n',
    'が':'ga','ぎ':'gi','ぐ':'gu','げ':'ge','ご':'go',
    'ざ':'za','じ':'ji','ず':'zu','ぜ':'ze','ぞ':'zo',
    'だ':'da','ぢ':'ji','づ':'zu','で':'de','ど':'do',
    'ば':'ba','び':'bi','ぶ':'bu','べ':'be','ぼ':'bo',
    'ぱ':'pa','ぴ':'pi','ぷ':'pu','ぺ':'pe','ぽ':'po',
}
# Katakana is the same 46 sounds, one Unicode block up (+0x60). Deriving it
# rather than retyping it means a typo cannot differ between the two scripts.
BASE.update({chr(ord(k) + 0x60): v for k, v in list(BASE.items()) if '\u3041' <= k <= '\u3096'})
BASE['ヲ'] = 'o'
BASE['ヴ'] = 'vu'
# Two different mechanics that look alike on the page:
#   yoon  (small ya/yu/yo) inserts a y:  ki + ya -> kya
#   small plain vowels     replace it:   fu + a  -> fa,  de + i -> di
YOON   = {'ゃ':'a', 'ゅ':'u', 'ょ':'o', 'ャ':'a', 'ュ':'u', 'ョ':'o'}
SMALLV = {'ァ':'a', 'ィ':'i', 'ゥ':'u', 'ェ':'e', 'ォ':'o',
          'ぁ':'a', 'ぃ':'i', 'ぅ':'u', 'ぇ':'e', 'ぉ':'o'}
SMALL_ALL = {**YOON, **SMALLV}
LONG = {'a':'ā', 'i':'ī', 'u':'ū', 'e':'ē', 'o':'ō'}

# Lexical exceptions the table cannot derive, each with its reason. Kept tiny
# and explicit — a growing list here would mean the romaniser is wrong.
EXCEPTIONS = {
    'こんにちは': 'konnichiwa',   # final は is the topic particle, read [wa]
    'こんばんは': 'konbanwa',     # same
}

def _morae(word):
    """Split into morae, gluing a yoon pair into one token."""
    out, i = [], 0
    while i < len(word):
        ch = word[i]
        if i + 1 < len(word) and word[i + 1] in SMALL_ALL and word[i] != 'ー':
            out.append(word[i:i + 2]); i += 2
        else:
            out.append(ch); i += 1
    return out

def romanise(word):
    if word in EXCEPTIONS:
        return EXCEPTIONS[word]
    parts = []
    for tok in _morae(word):
        if tok == 'ー':
            if not parts or not parts[-1] or parts[-1][-1] not in LONG:
                return None
            parts[-1] = parts[-1][:-1] + LONG[parts[-1][-1]]
        elif tok in ('っ', 'ッ'):
            parts.append('\u0001')                 # marker: double the next consonant
        elif len(tok) == 2:                        # yoon or small plain vowel
            base = BASE.get(tok[0])
            if base is None:
                return None
            stem = base[:-1]                       # ki -> k, shi -> sh, chi -> ch, ji -> j
            if tok[1] in SMALLV:                   # fu + a -> fa, de + i -> di
                parts.append(stem + SMALLV[tok[1]])
            elif stem in ('sh', 'ch', 'j'):        # sha, cha, ja — no extra y
                parts.append(stem + YOON[tok[1]])
            else:                                  # ki + ya -> kya
                parts.append(stem + 'y' + YOON[tok[1]])
        else:
            r = BASE.get(tok)
            if r is None:
                return None
            parts.append(r)
    # sokuon: double the following consonant
    out = []
    for i, pr in enumerate(parts):
        if pr == '\u0001':
            nxt = parts[i + 1] if i + 1 < len(parts) else ''
            out.append(nxt[0] if nxt else '')
        else:
            out.append(pr)
    r = ''.join(out)
    # n -> m before b, p, m
    r = re.sub(r'n(?=[bpm])', 'm', r)
    # Long vowels. Only the cases Hepburn actually collapses: aa, uu, oo, ou.
    # NOT ii and NOT ei — 大きい is "ōkii" and 先生 is "sensei" in every
    # dictionary, because those spellings straddle a morpheme boundary.
    for v in ('a', 'u', 'o'):
        r = r.replace(v + v, LONG[v])
    r = r.replace('ou', 'ō')
    return r

# ── Self-test. Every word here is derived by the table above and compared with a
#    reading typed out by hand. Run this before trusting the romaniser. ──────────
CASES = {
    'あさ': 'asa', 'すし': 'sushi', 'なつ': 'natsu', 'ちかてつ': 'chikatetsu',
    'にほん': 'nihon', 'こころ': 'kokoro', 'くるま': 'kuruma', 'そら': 'sora',
    'こんにちは': 'konnichiwa', 'おはよう': 'ohayō', 'とおる': 'tōru',
    'ゆうき': 'yūki', 'ゆき': 'yuki', 'おおきい': 'ōkii',
    'きって': 'kitte', 'がっこう': 'gakkō', 'きょう': 'kyō', 'でんしゃ': 'densha',
    'ざっし': 'zasshi', 'しんぶん': 'shimbun', 'みず': 'mizu',
    'テレビ': 'terebi', 'ミルク': 'miruku', 'トマト': 'tomato', 'アイス': 'aisu',
    'オアシス': 'oashisu', 'スイス': 'suisu', 'パン': 'pan', 'ホテル': 'hoteru',
    'ワイン': 'wain', 'ピアノ': 'piano',
    'コーヒー': 'kōhī', 'ノート': 'nōto', 'スーパー': 'sūpā', 'ケーキ': 'kēki',
    'テスト': 'tesuto', 'ファ': 'fa', 'ウズベキスタン': 'uzubekisutan',
    'タシケント': 'tashikento', 'アフソナ': 'afusona', 'ジャスル': 'jasuru',
    'シェルベク': 'sherubeku', 'ディルノザ': 'dirunoza',
}


def self_test():
    wrong = {k: (v, romanise(k)) for k, v in CASES.items() if romanise(k) != v}
    if wrong:
        raise AssertionError(f'romaniser is wrong for: {wrong}')
    return len(CASES)


if __name__ == '__main__':
    print(f'romaniser self-test: OK — all {self_test()} words')
