#!/usr/bin/env python3
"""ElevenLabs narration for Flow Studio — the storyteller's voice, made outside Veo.

Veo lip-syncs any speech it generates to the nearest face, so the storyteller's scenes are
generated SILENT and his voice is laid over them in the edit (the user's call, 2026-10-07).
A series keeps its narrator settings in its cast file under "narrator_tts".

    from voice import speak
    speak(cast['narrator_tts'], tagged_text, 'out.mp3')

Needs ELEVENLABS_API_KEY in the environment. Standard library only.
⚠️ Uzbek needs model eleven_v4 — eleven_v3 has no Uzbek and reads it with an English accent.
"""
import json
import os
import sys
import urllib.error
import urllib.request


def speak(cfg, text, out_path):
    key = os.environ.get('ELEVENLABS_API_KEY')
    if not key:
        sys.exit('ELEVENLABS_API_KEY is not set')
    body = {'text': f"{cfg.get('lead_tag', '')} {text}".strip(), 'model_id': cfg['model_id']}
    if cfg.get('language_code'):
        body['language_code'] = cfg['language_code']
    if cfg.get('voice_settings'):
        body['voice_settings'] = cfg['voice_settings']
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{cfg['voice_id']}?output_format=mp3_44100_128",
        data=json.dumps(body).encode(),
        headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        audio = urllib.request.urlopen(req, timeout=180).read()
    except urllib.error.HTTPError as err:
        sys.exit(f'ElevenLabs {err.code}: {err.read()[:300]!r}')
    with open(out_path, 'wb') as f:
        f.write(audio)
    return out_path
