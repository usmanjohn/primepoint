"""Hangul arithmetic for the Prime Korean answer gates — a helper, not a command.

Like `_romaji.py` for Prime Japanese: kept in the repo, imported by each
batch's throwaway gate (`verify_pk_workbook_<range>.py` in the scratchpad), and
self-tested on its own:

    python3 tutorial/management/commands/_hangul.py

It re-derives, from the rules rather than from memory, the forms a workbook
answer key claims: syllable blocks from letters and back, 받침 detection, the
particle pairs (은/는, 이/가, 을/를, 와/과, (으)로, 이에요/예요), and verb
endings (아/어요, 았/었어요, ㅂ니다/습니다) with the irregular classes taught in
Prime Korean. When you add a rule, first add the case that fails without it —
storyvideo's korean.py shipped without ㅅ-palatalisation because no self-test
happened to contain 시.
"""

BASE = 0xAC00
L = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')
V = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ')
T = [''] + list('ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')


# ── Blocks ──────────────────────────────────────────────────────────────────

def is_syllable(ch):
    return len(ch) == 1 and BASE <= ord(ch) <= 0xD7A3


def split(ch):
    """'한' → ('ㅎ', 'ㅏ', 'ㄴ'); the third is '' when there is no 받침."""
    if not is_syllable(ch):
        raise ValueError(f'{ch!r} is not a Hangul syllable')
    n = ord(ch) - BASE
    return L[n // 588], V[(n % 588) // 28], T[n % 28]


def join(lead, vowel, tail=''):
    """('ㅎ', 'ㅏ', 'ㄴ') → '한'."""
    return chr(BASE + (L.index(lead) * 21 + V.index(vowel)) * 28 + T.index(tail))


def letters(word):
    """'한국' → 'ㅎㅏㄴㄱㅜㄱ' (spaces dropped)."""
    return ''.join(''.join(split(c)) for c in word if is_syllable(c))


def build(seq):
    """Compose a letter string back into blocks: 'ㅎㅏㄴㄱㅜㄱ' → '한국'.

    Standard 2-set rule: a consonant between two vowels opens the next
    block. Only simple 받침 (no ㄳ-type clusters) — enough for the lessons.
    """
    out, i, s = [], 0, [c for c in seq if not c.isspace() and c != '+']
    while i < len(s):
        lead, vowel = s[i], s[i + 1]
        i += 2
        tail = ''
        if i < len(s) and s[i] in T and s[i] in L and not (i + 1 < len(s) and s[i + 1] in V):
            tail, i = s[i], i + 1
        elif i < len(s) and s[i] in T and s[i] not in L:   # ㄳ-type — not needed yet
            tail, i = s[i], i + 1
        out.append(join(lead, vowel, tail))
    return ''.join(out)


def batchim(word):
    """The final consonant of the last syllable, or '' (no 받침)."""
    last = [c for c in word if is_syllable(c)][-1]
    return split(last)[2]


def has_batchim(word):
    return batchim(word) != ''


# ── Particles ───────────────────────────────────────────────────────────────

def topic(noun):   return noun + ('은' if has_batchim(noun) else '는')
def subject(noun): return noun + ('이' if has_batchim(noun) else '가')
def obj(noun):     return noun + ('을' if has_batchim(noun) else '를')
def and_(noun):    return noun + ('과' if has_batchim(noun) else '와')


def ro(noun):
    """(으)로 — ㄹ 받침 takes plain 로, like no 받침."""
    return noun + ('으로' if has_batchim(noun) and batchim(noun) != 'ㄹ' else '로')


def ieyo(noun):
    return noun + ('이에요' if has_batchim(noun) else '예요')


def imnida(noun):
    return noun + '입니다'


def imnikka(noun):
    return noun + '입니까'


def anida(noun):
    """'학생' → '학생이 아닙니다' — the first place 받침 splits a form."""
    return subject(noun) + ' 아닙니다'


# ── Verbs ───────────────────────────────────────────────────────────────────
# Irregular classes as they are taught. A stem not listed is regular — which is
# why the regular look-alikes (받다, 입다, 좁다, 닫다, 믿다) must stay unlisted.
IRREGULAR = {
    'ㅂ': {'춥', '덥', '어렵', '쉽', '가깝', '무겁', '가볍', '맵', '귀엽', '반갑',
           '고맙', '즐겁', '아름답', '더럽', '돕', '곱', '눕', '굽'},
    'ㄷ': {'듣', '걷', '묻', '싣', '깨닫'},
    '르': {'모르', '부르', '빠르', '다르', '고르', '자르', '오르', '누르', '흐르'},
    'ㅎ': {'그렇', '이렇', '저렇', '어떻', '빨갛', '파랗', '노랗', '하얗', '까맣'},
    'ㅅ': {'낫', '짓', '붓', '잇'},
}


def stem_of(dictionary_form):
    if not dictionary_form.endswith('다'):
        raise ValueError(f'{dictionary_form!r} is not a dictionary form')
    return dictionary_form[:-1]


def _klass(stem):
    for klass, stems in IRREGULAR.items():
        if stem in stems:
            return klass
    return None


def _is_bright(vowel):
    return vowel in ('ㅏ', 'ㅗ', 'ㅑ')


def infinitive(stem):
    """The 아/어 form every ending below is built on: 가 → 가, 먹 → 먹어,
    하 → 해, 마시 → 마셔, 춥 → 추워, 듣 → 들어, 모르 → 몰라, 그렇 → 그래."""
    klass = _klass(stem)
    head, last = stem[:-1], stem[-1]
    lead, vowel, tail = split(last)

    if stem.endswith('하'):
        return head + '해'
    if klass == 'ㅂ':
        # 돕다/곱다 keep the bright 와; every other ㅂ-irregular takes 워.
        return head + join(lead, vowel) + ('와' if stem in ('돕', '곱') else '워')
    if klass == 'ㄷ':
        tail = 'ㄹ'
    if klass == 'ㅅ':
        tail = ''
        return head + join(lead, vowel) + ('아' if _is_bright(vowel) else '어')
    if klass == '르':
        prev_lead, prev_vowel, _pt = split(head[-1])
        return (head[:-1] + join(prev_lead, prev_vowel, 'ㄹ')
                + join('ㄹ', 'ㅏ' if _is_bright(prev_vowel) else 'ㅓ'))
    if klass == 'ㅎ':
        new = {'ㅏ': 'ㅐ', 'ㅓ': 'ㅐ', 'ㅑ': 'ㅒ'}[vowel]
        if stem == '하얗':
            new = 'ㅒ'
        return head + join(lead, new)

    if tail:
        return head + join(lead, vowel, tail) + ('아' if _is_bright(vowel) else '어')

    # No 받침: the vowels meet and contract.
    if vowel == 'ㅡ':                 # 으-drop: 쓰 → 써, 바쁘 → 바빠
        prev = split(head[-1])[1] if head else 'ㅓ'
        return head + join(lead, 'ㅏ' if _is_bright(prev) else 'ㅓ')
    contract = {'ㅏ': 'ㅏ', 'ㅓ': 'ㅓ', 'ㅕ': 'ㅕ', 'ㅐ': 'ㅐ', 'ㅔ': 'ㅔ',
                'ㅗ': 'ㅘ', 'ㅜ': 'ㅝ', 'ㅣ': 'ㅕ', 'ㅚ': 'ㅙ'}
    if vowel in contract:
        return head + join(lead, contract[vowel])
    return head + last + ('아' if _is_bright(vowel) else '어')


def ayo(dictionary_form):
    """먹다 → 먹어요."""
    return infinitive(stem_of(dictionary_form)) + '요'


def past(dictionary_form):
    """먹다 → 먹었어요: ㅆ goes under the 아/어 form's last block."""
    inf = infinitive(stem_of(dictionary_form))
    lead, vowel, tail = split(inf[-1])
    if tail:
        raise ValueError(f'unexpected 받침 in {inf!r}')
    return inf[:-1] + join(lead, vowel, 'ㅆ') + '어요'


def formal(dictionary_form):
    """가다 → 갑니다, 먹다 → 먹습니다, 살다 → 삽니다 (ㄹ drops before ㅂ)."""
    stem = stem_of(dictionary_form)
    lead, vowel, tail = split(stem[-1])
    if tail == 'ㄹ':
        return stem[:-1] + join(lead, vowel, 'ㅂ') + '니다'
    if tail:
        return stem + '습니다'
    return stem[:-1] + join(lead, vowel, 'ㅂ') + '니다'


# ── Pronunciation: the rules PK-8 teaches, only as far as the answers need ──

NASAL = {'ㅂ': 'ㅁ', 'ㄷ': 'ㄴ', 'ㄱ': 'ㅇ', 'ㅍ': 'ㅁ', 'ㅌ': 'ㄴ', 'ㅋ': 'ㅇ',
         'ㅅ': 'ㄴ', 'ㅆ': 'ㄴ', 'ㅈ': 'ㄴ', 'ㅊ': 'ㄴ'}


def say(word):
    """비음화 + 경음화 after ㅂ/ㄱ/ㄷ, enough for 합니다·습니다·학생·입니다."""
    blocks = [list(split(c)) for c in word if is_syllable(c)]
    tense = {'ㄱ': 'ㄲ', 'ㄷ': 'ㄸ', 'ㅂ': 'ㅃ', 'ㅅ': 'ㅆ', 'ㅈ': 'ㅉ'}
    for a, b in zip(blocks, blocks[1:]):
        if a[2] in NASAL and b[0] in ('ㄴ', 'ㅁ'):          # 비음화
            a[2] = NASAL[a[2]]
        elif a[2] in ('ㄱ', 'ㄷ', 'ㅂ') and b[0] in tense:    # 경음화
            b[0] = tense[b[0]]
    return ''.join(join(*b) for b in blocks)


# ── Self-test ───────────────────────────────────────────────────────────────

CASES = [
    # blocks
    (lambda: split('한'), ('ㅎ', 'ㅏ', 'ㄴ')),
    (lambda: join('ㄱ', 'ㅜ', 'ㄱ'), '국'),
    (lambda: letters('한국어'), 'ㅎㅏㄴㄱㅜㄱㅇㅓ'),
    (lambda: build('ㅎㅏㄴㄱㅜㄱㅇㅓ'), '한국어'),
    (lambda: build('ㅅㅏㄹㅏㅁ'), '사람'),          # ㄹ between vowels opens a block
    (lambda: build('ㅎ + ㅏ + ㄴ'), '한'),
    (lambda: build('ㄲㅗㅊ'), '꽃'),
    (lambda: has_batchim('학생'), True),
    (lambda: has_batchim('의사'), False),
    # particles
    (lambda: subject('학생'), '학생이'),
    (lambda: subject('친구'), '친구가'),
    (lambda: topic('선생님'), '선생님은'),
    (lambda: topic('저'), '저는'),
    (lambda: obj('밥'), '밥을'),
    (lambda: ro('서울'), '서울로'),
    (lambda: ro('집'), '집으로'),
    (lambda: ieyo('의사'), '의사예요'),
    (lambda: anida('선생님'), '선생님이 아닙니다'),
    (lambda: anida('의사'), '의사가 아닙니다'),
    # 아/어요
    (lambda: ayo('가다'), '가요'),
    (lambda: ayo('먹다'), '먹어요'),
    (lambda: ayo('하다'), '해요'),
    (lambda: ayo('공부하다'), '공부해요'),
    (lambda: ayo('오다'), '와요'),
    (lambda: ayo('주다'), '줘요'),
    (lambda: ayo('마시다'), '마셔요'),
    (lambda: ayo('되다'), '돼요'),
    (lambda: ayo('쓰다'), '써요'),
    (lambda: ayo('바쁘다'), '바빠요'),
    (lambda: ayo('보내다'), '보내요'),
    (lambda: ayo('받다'), '받아요'),      # regular look-alike of ㄷ
    (lambda: ayo('입다'), '입어요'),      # regular look-alike of ㅂ
    (lambda: ayo('춥다'), '추워요'),
    (lambda: ayo('돕다'), '도와요'),
    (lambda: ayo('듣다'), '들어요'),
    (lambda: ayo('모르다'), '몰라요'),
    (lambda: ayo('부르다'), '불러요'),
    (lambda: ayo('그렇다'), '그래요'),
    (lambda: ayo('하얗다'), '하얘요'),
    (lambda: ayo('낫다'), '나아요'),
    (lambda: ayo('짓다'), '지어요'),
    # past
    (lambda: past('가다'), '갔어요'),
    (lambda: past('먹다'), '먹었어요'),
    (lambda: past('하다'), '했어요'),
    (lambda: past('마시다'), '마셨어요'),
    (lambda: past('듣다'), '들었어요'),
    (lambda: past('춥다'), '추웠어요'),
    # formal
    (lambda: formal('가다'), '갑니다'),
    (lambda: formal('먹다'), '먹습니다'),
    (lambda: formal('살다'), '삽니다'),
    (lambda: formal('하다'), '합니다'),
    # pronunciation
    (lambda: say('합니다'), '함니다'),
    (lambda: say('입니다'), '임니다'),
    (lambda: say('감사합니다'), '감사함니다'),
    (lambda: say('고맙습니다'), '고맙씀니다'),
    (lambda: say('학생'), '학쌩'),
    (lambda: say('반갑습니다'), '반갑씀니다'),
]


def self_test():
    bad = 0
    for i, (fn, want) in enumerate(CASES, 1):
        try:
            got = fn()
        except Exception as exc:  # noqa: BLE001 — report, don't stop
            got = f'{type(exc).__name__}: {exc}'
        if got != want:
            bad += 1
            print(f'  FAIL #{i}: want {want!r}, got {got!r}')
    print(f'_hangul self-test: {len(CASES) - bad}/{len(CASES)} passed')
    return bad == 0


if __name__ == '__main__':
    raise SystemExit(0 if self_test() else 1)
