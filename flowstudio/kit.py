#!/usr/bin/env python3
"""A LOCAL production kit for one Flow package — instead of Telegram (the user's request,
2026-10-07: "I will be the one building the videos").

    python3 flowstudio/kit.py PACKAGE.json OUT_DIR

Writes OUT_DIR/
    00-QOʻLLANMA.txt        step-by-step: pictures → scenes → edit, with every file named
    1-rasmlar/R1.txt …      one Nano Banana prompt per picture (copy-paste)
    2-sahnalar/S01.txt …    one Veo prompt per scene (copy-paste)
    3-ovoz/S01-hikoyachi.mp3 …  the storyteller's voice-over (ElevenLabs, see voice.py)

The package is gated first (send.py check). Voice-over lines carry a 'tts' text; their scenes
are silent in Veo and the mp3 goes on top in the edit. Needs ELEVENLABS_API_KEY for the mp3s.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import send                                    # noqa: E402  (the gate and the cast lookup)
from voice import speak                        # noqa: E402

SECONDS = send.SECONDS


def seconds(path):
    """mp3 length via macOS afinfo (no ffprobe on this Mac)."""
    try:
        out = subprocess.run(['afinfo', path], capture_output=True, text=True).stdout
        for line in out.splitlines():
            if 'estimated duration' in line:
                return float(line.split(':')[1].split()[0])
    except OSError:
        pass
    return None


def build(pkg_path, out):
    with open(pkg_path, encoding='utf-8') as f:
        pkg = json.load(f)
    errs = send.check(pkg)
    if errs:
        sys.exit('gate failed:\n  - ' + '\n  - '.join(errs))
    cast = send.series_cast(pkg['series']) if pkg['series'] in send.SERIES_CAST else {}
    for sub in ('1-rasmlar', '2-sahnalar', '3-ovoz'):
        os.makedirs(os.path.join(out, sub), exist_ok=True)

    g = [f"{pkg['series'].upper()} — {pkg['title_uz']}", '=' * 60, '',
         pkg['concept_uz'], f"Format: {pkg['format_uz']}", '',
         'Tartib: 1) rasmlar → 2) sahnalar → 3) montaj. Har bir prompt alohida faylda — ochib, nusxa oling.', '']

    g += ['1) RASMLAR — Nano Banana Pro, 9:16. Har birini raqami bilan saqlang (R1, R2…).', '']
    for r in pkg['refs']:
        froms = send._froms(r)
        if r.get('saved'):
            g.append(f"  @{r['id']} — {r['name_uz']}: ♻️ oldin yasalgan, qayta yaratmang")
            continue
        prompt = r['prompt'] if froms else f"{r['prompt'].rstrip()} {pkg['style_line']}"
        with open(os.path.join(out, '1-rasmlar', f"{r['id']}.txt"), 'w', encoding='utf-8') as f:
            f.write(prompt + '\n')
        how = f"  ← {' + '.join('@' + x for x in froms)} ni biriktiring" if froms else ''
        g.append(f"  @{r['id']} — {r['name_uz']}   [1-rasmlar/{r['id']}.txt]{how}")

    g += ['', '2) SAHNALAR — Flow, Veo 3.1, 9:16, har biri 8 soniya.', '']
    mp3s = []
    for sc in pkg['scenes']:
        n = int(sc['n'])
        name = f'S{n:02d}'
        with open(os.path.join(out, '2-sahnalar', f'{name}.txt'), 'w', encoding='utf-8') as f:
            f.write(sc['prompt'] + '\n')
        if sc['method'] == 'Frames to Video':
            pics = f"boshi: @{sc['start']}" + (f", oxiri: @{sc['end']}" if sc.get('end') else '')
        else:
            pics = ' + '.join('@' + x for x in sc.get('attach') or [])
        g.append(f"  {name} · {sc['title_uz']} — {sc['method']}, {pics}   [2-sahnalar/{name}.txt]")
        for ln in sc.get('lines') or []:
            if ln.get('tts'):
                mp3 = os.path.join(out, '3-ovoz', f'{name}-hikoyachi.mp3')
                if not os.path.exists(mp3):
                    speak(cast['narrator_tts'], ln['tts'], mp3)
                dur = seconds(mp3)
                mp3s.append((name, dur))
                note = f'{dur:.1f} s' if dur else '?'
                g.append(f"       🔇 SOKIN sahna. Ovoz montajda: 3-ovoz/{name}-hikoyachi.mp3 ({note})")
            else:
                g.append(f"       🗣 {ln['who']}: Veo oʻzi gapiradi — notoʻgʻri ogʻiz qimirlasa, qayta generatsiya")
    g += ['', '3) MONTAJ — CapCut',
          '  • Sahnalarni S01 dan boshlab tartib bilan qoʻying.',
          '  • 🔇 sokin sahnalarga oʻsha raqamli mp3 ni qoʻying; Veo ovozini (shamol va h.k.) pastroq qiling.']
    long = [f'{n} ({d:.1f} s)' for n, d in mp3s if d and d > SECONDS]
    if long:
        g.append(f"  • Bu ovozlar 8 soniyadan uzun: {', '.join(long)} — Flowʼda oʻsha sahnani Extend qiling "
                 "yoki klipni biroz sekinlashtiring, ovozni kesmang.")
    g += ['  • Gapiradigan sahnada 4 qator shoshib chiqsa — sahnani ikkiga boʻling (Extend).',
          '  • Musiqa: ostidan juda past, yumshoq doʻmbira yoki ertak kuyi.', '']
    if pkg.get('post_text_uz'):
        g += ['4) POST MATNI', '', pkg['post_text_uz'], '']
    with open(os.path.join(out, '00-QOʻLLANMA.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(g) + '\n')
    return out


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    print(build(sys.argv[1], os.path.expanduser(sys.argv[2])))
