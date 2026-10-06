#!/usr/bin/env python3
"""Assemble a finished episode from a kit folder — no CapCut (the user's request, 2026-10-07).

    python3 flowstudio/assemble.py PACKAGE.json KIT_DIR

KIT_DIR is the folder kit.py made. Put the clips downloaded from Flow in KIT_DIR/4-kliplar/
as S01.mp4, S02.mp4 … (one per scene), and optionally one music file KIT_DIR/musiqa.mp3.
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
VOICE_DELAY = 0.3          # s of breath before the storyteller starts
VOICE_TAIL = 0.6           # s held after he finishes
SFX_UNDER_VOICE = 0.6      # clip sound (effects, wind) under the storyteller
MUSIC_LEVEL = 0.22         # music bed, before ducking


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
    sound = '[0:a]aresample=48000,aformat=channel_layouts=stereo' if has_audio(clip) else \
            'anullsrc=r=48000:cl=stereo'
    if not voice:
        a = sound + (f'[a]' if has_audio(clip) else f',atrim=0:{vd}[a]')
        run(['-i', clip, '-filter_complex', f'[0:v]{norm}[v];{a}',
             '-map', '[v]', '-map', '[a]', '-t', f'{vd}', '-c:v', 'libx264', '-preset', 'medium',
             '-crf', '18', '-c:a', 'aac', '-b:a', '192k', out])
        return vd
    total = max(vd, VOICE_DELAY + duration(voice) + VOICE_TAIL)
    hold = total - vd
    ms = int(VOICE_DELAY * 1000)
    fc = (f'[0:v]{norm},tpad=stop_mode=clone:stop_duration={hold:.3f}[v];'
          f'{sound},volume={SFX_UNDER_VOICE},apad[fx];'
          f'[1:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms},apad[vo];'
          f'[fx][vo]amix=inputs=2:duration=longest:normalize=0[a]')
    run(['-i', clip, '-i', voice, '-filter_complex', fc, '-map', '[v]', '-map', '[a]',
         '-t', f'{total:.3f}', '-c:v', 'libx264', '-preset', 'medium', '-crf', '18',
         '-c:a', 'aac', '-b:a', '192k', out])
    return total


def build(pkg_path, kit):
    with open(pkg_path, encoding='utf-8') as f:
        pkg = json.load(f)
    clips_dir, tmp = os.path.join(kit, '4-kliplar'), os.path.join(kit, '.yigish')
    os.makedirs(tmp, exist_ok=True)
    names = [f"S{int(sc['n']):02d}" for sc in pkg['scenes']]
    missing = [n for n in names if not os.path.exists(os.path.join(clips_dir, f'{n}.mp4'))]
    if missing:
        sys.exit(f"4-kliplar/ da yetishmaydi: {', '.join(n + '.mp4' for n in missing)}")

    parts, length = [], 0.0
    for n in names:
        voice = os.path.join(kit, '3-ovoz', f'{n}-hikoyachi.mp3')
        out = os.path.join(tmp, f'{n}.mp4')
        length += segment(os.path.join(clips_dir, f'{n}.mp4'), voice if os.path.exists(voice) else None, out)
        parts.append(out)
        print(f'  {n} ✓')
    listing = os.path.join(tmp, 'list.txt')
    with open(listing, 'w') as f:
        f.writelines(f"file '{p}'\n" for p in parts)
    joined = os.path.join(tmp, 'joined.mp4')
    run(['-f', 'concat', '-safe', '0', '-i', listing, '-c', 'copy', joined])

    final = os.path.join(kit, f"TAYYOR-{pkg['id']}.mp4")
    music = next((os.path.join(kit, m) for m in sorted(os.listdir(kit))
                  if m.lower().startswith('musiqa') and m.lower().endswith(('.mp3', '.m4a', '.wav'))), None)
    if not music:
        os.replace(joined, final)
        print('(musiqa yoʻq — KIT papkasiga musiqa.mp3 qoʻysangiz, qoʻshiladi)')
    else:
        fade = max(length - 2.5, 0)
        fc = (f'[1:a]aresample=48000,aformat=channel_layouts=stereo,volume={MUSIC_LEVEL},'
              f'atrim=0:{length:.3f},afade=t=in:d=1.5,afade=t=out:st={fade:.3f}:d=2.5[m];'
              f'[0:a]asplit=2[sc][main];'
              f'[m][sc]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[duck];'
              f'[main][duck]amix=inputs=2:duration=first:normalize=0[a]')
        run(['-i', joined, '-stream_loop', '-1', '-i', music, '-filter_complex', fc,
             '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
             '-shortest', final])
    print(f'TAYYOR: {final}  ({length:.1f} s)')
    return final


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    build(sys.argv[1], os.path.expanduser(sys.argv[2]))
