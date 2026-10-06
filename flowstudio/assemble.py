#!/usr/bin/env python3
"""Assemble a finished episode from a kit folder — no CapCut (the user's request, 2026-10-07).

    python3 flowstudio/assemble.py PACKAGE.json KIT_DIR [--clips DIR] [--music FILE]

KIT_DIR is the folder kit.py made. Put the clips downloaded from Flow in KIT_DIR/4-kliplar/
as S01.mp4, S02.mp4 … (one per scene), and optionally one music file KIT_DIR/musiqa.mp3.
--clips reads any folder whose names START with the scene: "S05_1080p_….mp4", or a clip that
covers several scenes, "S02-03_….mp4" (the user's own Flow downloads, 2026-10-07).
The script then:
  1. brings every clip to 1080×1920, 30 fps, 48 kHz stereo;
  2. on a voice-over scene (3-ovoz/Sxx-hikoyachi.mp3) lays the storyteller over the clip's
     own sound effects, and if the voice is longer than the clip holds the last frame;
  3. joins the scenes in order;
  4. lays the music under everything, ducked automatically whenever anyone speaks;
  5. writes KIT_DIR/TAYYOR-<id>.mp4.
Needs ffmpeg (not ffprobe — this Mac has none).
"""
import json
import os
import re
import subprocess
import sys

W, H, FPS = 1080, 1920, 30
VOICE_DELAY = 0.45         # s of breath before the storyteller starts (clear of the dissolve)
XFADE = 0.3                # s cross-dissolve between scenes, picture and sound (user, 2026-10-07)
VOICE_TAIL = 0.6           # s held after he finishes
SFX_UNDER_VOICE = 0.6      # clip sound (effects, wind) under the storyteller
MUSIC_LEVEL = 0.22         # music bed, before ducking
SPEECH_LUFS = -20          # every clip's own sound evened out to this before joining
FINAL_LUFS = -14           # what Instagram / YouTube play at
EDGE = 0.03                # s of audio fade at every cut — no clicks


def run(args):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *args],
                       capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"ffmpeg failed:\n{r.stderr[-1500:]}")


def duration(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', path], capture_output=True, text=True)
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', r.stderr)
    if not m:
        sys.exit(f'cannot read the length of {path}')
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def has_audio(path):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', path], capture_output=True, text=True)
    return 'Audio:' in r.stderr


def segment(clip, voice, out):
    """One scene → a normalised mp4 (with the voice-over mixed in, if any)."""
    vd = duration(clip)
    norm = (f'scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,'
            f'setsar=1,fps={FPS},format=yuv420p')
    # level only clips where characters SPEAK; a voice-over scene keeps its quiet ambience as it is
    level = f',loudnorm=I={SPEECH_LUFS}:TP=-2:LRA=11,aresample=48000' if not voice else ''
    sound = (f'[0:a]aresample=48000,aformat=channel_layouts=stereo{level}' if has_audio(clip)
             else 'anullsrc=r=48000:cl=stereo')
    if not voice:
        a = sound + (f',atrim=0:{vd},afade=t=in:d={EDGE},afade=t=out:st={vd - EDGE:.3f}:d={EDGE}[a]'
                     if has_audio(clip) else f',atrim=0:{vd}[a]')
        run(['-i', clip, '-filter_complex', f'[0:v]{norm}[v];{a}',
             '-map', '[v]', '-map', '[a]', '-t', f'{vd}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium',
             '-crf', '18', '-c:a', 'aac', '-b:a', '192k', out])
        return vd
    total = max(vd, VOICE_DELAY + duration(voice) + VOICE_TAIL)
    hold = total - vd
    ms = int(VOICE_DELAY * 1000)
    fc = (f'[0:v]{norm},tpad=stop_mode=clone:stop_duration={hold:.3f}[v];'
          f'{sound},volume={SFX_UNDER_VOICE},apad[fx];'
          f'[1:a]aresample=48000,aformat=channel_layouts=stereo,loudnorm=I={SPEECH_LUFS + 2}:TP=-2,'
          f'aresample=48000,adelay={ms}|{ms},apad[vo];'
          f'[fx][vo]amix=inputs=2:duration=longest:normalize=0,atrim=0:{total:.3f},'
          f'afade=t=in:d={EDGE},afade=t=out:st={total - EDGE:.3f}:d={EDGE}[a]')
    run(['-i', clip, '-i', voice, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
         '-t', f'{total:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '18',
         '-c:a', 'aac', '-b:a', '192k', out])
    return total


def join(parts, lens, out):
    """Chain the scenes with a short cross-dissolve (xfade + acrossfade); returns the new length."""
    if len(parts) == 1 or XFADE <= 0:
        listing = out + '.txt'
        with open(listing, 'w') as f:
            f.writelines(f"file '{p}'\n" for p in parts)
        run(['-f', 'concat', '-safe', '0', '-i', listing, '-c', 'copy', out])
        return sum(lens)
    args, fc, acc = [], [], lens[0]
    for p in parts:
        args += ['-i', p]
    v, a = '[0:v]', '[0:a]'
    for k in range(1, len(parts)):
        off = acc - XFADE
        fc.append(f'{v}[{k}:v]xfade=transition=fade:duration={XFADE}:offset={off:.3f}[v{k}]')
        fc.append(f'{a}[{k}:a]acrossfade=d={XFADE}:c1=tri:c2=tri[a{k}]')
        v, a = f'[v{k}]', f'[a{k}]'
        acc += lens[k] - XFADE
    run([*args, '-filter_complex', ';'.join(fc), '-map', v, '-map', a, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium',
         '-crf', '18', '-c:a', 'aac', '-b:a', '192k', out])
    return acc


def find_clips(folder, scene_numbers):
    """[(first_scene, last_scene, path)] in story order; refuses gaps and overlaps."""
    found = []
    for name in sorted(os.listdir(folder)):
        # "S05_…", "S02-03_…", "S22.mp4", and with a series prefix "S2_01_…" (the user's naming, 2026-10-07)
        m = (re.match(r'[Ss]\d+_(\d{1,3})(?:-(\d{1,3}))?(?=[_.\s-]|$)', name)
             or re.match(r'[Ss](\d+)(?:-(?:[Ss])?(\d+))?(?=[_.\s-]|$)', name))
        if m and name.lower().endswith(('.mp4', '.mov')):
            a = int(m.group(1)); b = int(m.group(2) or a)
            found.append((a, b, os.path.join(folder, name)))
    found.sort()
    covered = [n for a, b, _ in found for n in range(a, b + 1)]
    missing = sorted(set(scene_numbers) - set(covered))
    twice = sorted({n for n in covered if covered.count(n) > 1})
    if missing or twice:
        sys.exit(f"kliplar: yetishmaydi {missing or '—'}, ikki marta {twice or '—'}")
    return found


def build(pkg_path, kit, clips_dir=None, music=None):
    with open(pkg_path, encoding='utf-8') as f:
        pkg = json.load(f)
    clips_dir = clips_dir or os.path.join(kit, '4-kliplar')
    tmp = os.path.join(kit, '.yigish')
    os.makedirs(tmp, exist_ok=True)
    clips = find_clips(clips_dir, [int(sc['n']) for sc in pkg['scenes']])

    parts, lens = [], []
    for a, b, path in clips:
        n = f'S{a:02d}' + (f'-{b:02d}' if b != a else '')
        voice = os.path.join(kit, '3-ovoz', f'S{a:02d}-hikoyachi.mp3')
        out = os.path.join(tmp, f'{n}.mp4')
        lens.append(segment(path, voice if (a == b and os.path.exists(voice)) else None, out))
        parts.append(out)
        print(f'  {n} ✓  ({os.path.basename(path)})')
    joined = os.path.join(tmp, 'joined.mp4')
    length = join(parts, lens, joined)

    final = os.path.join(kit, f"TAYYOR-{pkg['id']}.mp4")
    music = music or next((os.path.join(kit, m) for m in sorted(os.listdir(kit))
                           if m.lower().startswith('musiqa') and m.lower().endswith(('.mp3', '.m4a', '.wav'))), None)
    fade = max(length - 1.2, 0)
    vfade = f'fade=t=in:d=0.5,fade=t=out:st={fade:.3f}:d=1.2'
    master = f'loudnorm=I={FINAL_LUFS}:TP=-1.5:LRA=11,aresample=48000,afade=t=in:d=0.5,afade=t=out:st={fade:.3f}:d=1.2'
    if not music:
        print('(musiqa yoʻq — KIT papkasiga musiqa.mp3 qoʻysangiz, qoʻshiladi)')
        run(['-i', joined, '-filter_complex', f'[0:v]{vfade}[v];[0:a]{master}[a]', '-map', '[v]', '-map', '[a]',
             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', final])
    else:
        mfade = max(length - 2.5, 0)
        fc = (f'[0:v]{vfade}[v];'
              f'[1:a]aresample=48000,aformat=channel_layouts=stereo,volume={MUSIC_LEVEL},'
              f'atrim=0:{length:.3f},afade=t=in:d=1.5,afade=t=out:st={mfade:.3f}:d=2.5[m];'
              f'[0:a]asplit=2[sc][main];'
              f'[m][sc]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[duck];'
              f'[main][duck]amix=inputs=2:duration=first:normalize=0,{master}[a]')
        run(['-i', joined, '-stream_loop', '-1', '-i', music, '-filter_complex', fc,
             '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '18',
             '-c:a', 'aac', '-b:a', '192k', '-shortest', final])
    print(f'TAYYOR: {final}  ({length:.1f} s)')
    return final


def _opt(argv, flag):
    if flag in argv:
        i = argv.index(flag)
        return os.path.expanduser(argv[i + 1])
    return None


if __name__ == '__main__':
    args = [a for i, a in enumerate(sys.argv[1:]) if not a.startswith('--')
            and (i == 0 or not sys.argv[i].startswith('--'))]
    if len(args) != 2:
        sys.exit(__doc__)
    build(args[0], os.path.expanduser(args[1]), _opt(sys.argv, '--clips'), _opt(sys.argv, '--music'))
