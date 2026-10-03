#!/usr/bin/env python3
"""Check a Flow Studio package and send it to Telegram.  See GUIDE.md.

    python3 flowstudio/send.py PACKAGE.json --check     # gate only, prints errors
    python3 flowstudio/send.py PACKAGE.json --dry-run   # gate + print the messages
    python3 flowstudio/send.py PACKAGE.json             # gate + send
    python3 flowstudio/send.py --whoami                 # list chats that wrote to the bot
    python3 flowstudio/send.py --ping                   # send one test message

Needs FLOW_BOT_TOKEN and FLOW_CHAT_ID in the environment to send.
Standard library only, so it runs in a bare cloud container.
"""
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import uuid

METHODS = {'Frames to Video', 'Ingredients to Video', 'Text to Video', 'Extend', 'Editor'}
MODELS = {'Lite', 'Fast', 'Quality', 'Fast→Quality', '—'}
LIMIT = 3900                      # Telegram's cap is 4096; leave room for tags
BAD_APOSTROPHE = re.compile(r"[oOgG]['‘’`]")
CYRILLIC = re.compile(r'[Ѐ-ӿ]')
UZ_FIELDS = ('title_uz', 'voice_uz', 'post_text_uz')


# ── the gate ─────────────────────────────────────────────────────────────

def _uz_errors(where, text):
    errs = []
    if BAD_APOSTROPHE.search(text or ''):
        errs.append(f"{where}: write oʻ/gʻ with ʻ (U+02BB), not an apostrophe: "
                    f"{BAD_APOSTROPHE.search(text).group()!r}")
    if CYRILLIC.search(text or ''):
        errs.append(f'{where}: Cyrillic letter inside Uzbek text')
    return errs


def check(pkg):
    errs = []
    for key in ('id', 'number', 'date', 'series', 'title_uz', 'logline', 'sources', 'facts',
                'emotion_arc', 'style_line', 'ingredients', 'shots', 'edit'):
        if not pkg.get(key):
            errs.append(f'missing or empty: {key}')
    if errs:
        return errs

    errs += _uz_errors('title_uz', pkg['title_uz'])
    if not str(pkg['number']).isdigit():
        errs.append('number must be a whole number (the video\'s №)')
    # explanations are Uzbek too (EXPLAIN_LANGUAGE in GUIDE.md); only prompts are English
    errs += _uz_errors('logline', pkg['logline'])
    for a in pkg['emotion_arc']:
        errs += _uz_errors('emotion_arc', f"{a.get('beat', '')} {a.get('feel', '')}")
    for f in pkg['facts']:
        errs += _uz_errors('facts', f.get('claim', ''))
    for i in pkg['ingredients']:
        errs += _uz_errors(f"ingredient {i.get('name')} check", i.get('check', ''))
    if 'no text' not in pkg['style_line'].lower():
        errs.append('style_line must forbid text in the picture ("No text, …")')

    names = {i.get('name', '').upper() for i in pkg['ingredients']}
    for i in pkg['ingredients']:
        if not i.get('name') or not i.get('prompt'):
            errs.append(f'ingredient without name/prompt: {i}')

    shots = pkg['shots']
    numbers = {str(s.get('n')) for s in shots}
    by_part = {}
    for s in shots:
        tag = f"shot {s.get('n')}"
        by_part.setdefault(s.get('part', ''), []).append(s)
        m, model = s.get('method'), s.get('model')
        if m not in METHODS:
            errs.append(f'{tag}: method {m!r} not one of {sorted(METHODS)}')
        if model not in MODELS:
            errs.append(f'{tag}: model {model!r} not one of {sorted(MODELS)}')
        for k in ('what', 'emotion', 'check'):
            if not s.get(k):
                errs.append(f'{tag}: missing {k}')
        attach = s.get('attach') or []
        for a in attach:
            if a.upper() not in names:
                errs.append(f'{tag}: attaches {a!r}, which is not an ingredient')
        if m == 'Frames to Video' and not s.get('frame_prompt'):
            errs.append(f'{tag}: Frames to Video needs frame_prompt')
        if m == 'Ingredients to Video':
            if not 1 <= len(attach) <= 3:
                errs.append(f'{tag}: Ingredients to Video takes 1-3 ingredients, has {len(attach)}')
            if s.get('frame_prompt'):
                errs.append(f'{tag}: Ingredients to Video has no frame_prompt (use Frames)')
        if m == 'Extend' and str(s.get('extends')) not in numbers:
            errs.append(f'{tag}: Extend must name the shot it continues in "extends"')
        if m != 'Editor':
            vp = s.get('video_prompt', '')
            if not vp:
                errs.append(f'{tag}: missing video_prompt')
            elif 'no speech' not in vp.lower():
                errs.append(f'{tag}: video_prompt must end with an audio line saying "No speech, no music."')
        for k in ('voice_uz', 'what', 'emotion', 'check'):
            errs += _uz_errors(f'{tag} {k}', s.get(k, ''))
        for k in ('frame_prompt', 'end_frame_prompt', 'video_prompt'):
            if CYRILLIC.search(s.get(k) or '') or re.search(r'[ʻʼ]', s.get(k) or ''):
                errs.append(f'{tag}: {k} must be English (Uzbek goes in voice_uz)')

    for part, ss in by_part.items():
        if not 4 <= len(ss) <= 16:
            errs.append(f'{part or "(no part)"}: {len(ss)} shots, want 4-16')
        q = sum(1 for s in ss if 'Quality' in (s.get('model') or ''))
        if q > 6:
            errs.append(f'{part or "(no part)"}: {q} Quality shots, budget is 6')

    edit = pkg['edit']
    for k in ('captions', 'music', 'cover', 'post_text_uz', 'checklist'):
        if not edit.get(k):
            errs.append(f'edit: missing {k}')
    for k in ('post_text_uz', 'captions', 'music', 'cover'):
        errs += _uz_errors(f'edit.{k}', edit.get(k, ''))
    for c in edit.get('checklist', []):
        errs += _uz_errors('edit.checklist', c)
    return errs


# ── rendering (Telegram HTML) ────────────────────────────────────────────

def e(text):
    return html.escape(str(text or ''), quote=False)


def code(label, text):
    return f'<b>{e(label)}</b>\n<pre>{e(text)}</pre>'


def with_style(prompt, pkg):
    """Append the style line — before the audio line, so "No speech" stays last."""
    prompt = prompt.rstrip()
    at = prompt.find('Audio:')
    if at > 0:
        return f"{prompt[:at].rstrip()} {pkg['style_line']} {prompt[at:]}"
    return f"{prompt} {pkg['style_line']}"


METHOD_UZ = {
    'Frames to Video': 'rasmdan video',
    'Ingredients to Video': 'qahramonlardan video',
    'Text to Video': 'matndan video',
    'Extend': 'davom ettirish',
    'Editor': 'faqat CapCut',
}
LEGEND = (
    "<b>Usullar</b> (Flowʼdagi nomi bilan)\n"
    "• <b>Frames to Video</b> — avval Nano Bananaʼda rasm yasaymiz, Veo uni harakatlantiradi. "
    "Kim qayerda turishi aniq boʻlishi kerak boʻlsa — shu.\n"
    "• <b>Ingredients to Video</b> — 1–3 ta qahramonni yuzini saqlagan holda erkin harakatlantiradi.\n"
    "• <b>Text to Video</b> — faqat manzara, odamsiz.\n"
    "• <b>Extend</b> — oldingi kadrni davom ettiradi (koʻpi bilan 1–2 marta).\n"
    "• <b>Editor</b> — Flow kerak emas, CapCutʼda qilinadi.\n"
    "<b>Modellar:</b> Lite — sinov · Fast — barcha qoralamalar · Quality — faqat eng muhim kadrlar.\n"
    "<b>Ish tartibi:</b> ingredientlar → kadr rasmlari → Fast qoralamalar → eng yaxshilarini "
    "Qualityʼda qayta → ovoz → CapCut."
)


def tag(pkg):
    return f"#video{int(pkg['number']):03d}"


def series_tag(pkg):
    return '#' + re.sub(r'[^0-9A-Za-z]', '', pkg['series'].title())


def sections(pkg):
    """The package as (contents-label, [message, …]) pairs, in sending order."""
    out = []
    parts = ' + '.join(f"{p['name']} ({p['length']})" for p in pkg.get('parts', []))
    arc = '\n'.join(f"• {e(a['time'])} — {e(a['beat'])}: <i>{e(a['feel'])}</i>"
                    for a in pkg['emotion_arc'])
    voice = '\n'.join(f"<b>{e(s['n'])}.</b> {e(s['voice_uz'])}"
                      for s in pkg['shots'] if s.get('voice_uz'))
    facts = '\n'.join(f"• {e(f['claim'])} — <i>{e(f['source'])}</i>" for f in pkg['facts'])
    out.append(('🎬 Gʻoya, hissiyotlar, ovoz matni', split(
        f"🎬 <b>Gʻoya</b>\n{e(pkg['logline'])}\n\n<b>Davomiyligi:</b> {e(parts)}\n\n"
        f"<b>Hissiyotlar rejasi</b>\n{arc}\n\n"
        f"<b>🎙 Ovoz matni</b> (har bir qatorni alohida faylga yozib oling)\n{voice}\n\n"
        f"<b>📚 Faktlar va manbalar</b>\n{facts}\n\n"
        f"<b>Uslub qatori</b> (pastdagi har bir promptga allaqachon qoʻshilgan)\n"
        f"<pre>{e(pkg['style_line'])}</pre>")))

    # ingredients packed into as few messages as fit; each prompt is its own <pre>
    cards = [f"<b>{n}. {e(i['name'])}</b>\n<pre>{e(with_style(i['prompt'], pkg))}</pre>\n"
             f"✅ <i>{e(i.get('check', ''))}</i>"
             for n, i in enumerate(pkg['ingredients'], 1)]
    msgs, cur = [], ("🖼 <b>Ingredientlar</b> — eng avval shularni Nano Banana Proʼda yarating "
                     "(9:16) va har birini KATTA HARFLI nomi bilan ingredient qilib saqlang")
    for c in cards:
        if len(cur) + len(c) + 2 > LIMIT:
            msgs.append(cur)
            cur = "🖼 <b>Ingredientlar</b> (davomi)"
        cur += "\n\n" + c
    msgs.append(cur)
    out.append((f"🖼 Ingredientlar ({len(cards)} ta)", msgs))

    shot_msgs = []
    for s in pkg['shots']:
        m = s['method']
        head = (f"🎥 <b>Kadr {e(s['n'])}</b> · {e(s.get('part', ''))} · {e(s.get('time', ''))}\n"
                f"<b>{e(m)}</b> ({METHOD_UZ.get(m, '')})"
                + (f" · Veo <b>{e(s['model'])}</b>" if m != 'Editor' else ''))
        if s.get('attach'):
            where = 'Nano Bananaʼga bering' if m == 'Frames to Video' else 'Veoʼga biriktiring'
            head += f"\n📎 {where}: <b>{e(', '.join(s['attach']))}</b>"
        if s.get('extends'):
            head += f"\n↪️ {e(s['extends'])}-kadrni davom ettiradi"
        body = [head, f"\n{e(s['what'])}\n💭 <i>{e(s['emotion'])}</i>"]
        if s.get('frame_prompt'):
            body.append(code('① Boshlangʻich kadr (Nano Banana Pro)', with_style(s['frame_prompt'], pkg)))
        if s.get('end_frame_prompt'):
            body.append(code('② Yakuniy kadr (Nano Banana Pro)', with_style(s['end_frame_prompt'], pkg)))
        if s.get('video_prompt'):
            body.append(code('▶️ Video prompt (Veo)', with_style(s['video_prompt'], pkg)))
        if s.get('voice_uz'):
            body.append(f"🎙 <b>Ovoz:</b> {e(s['voice_uz'])}")
        body.append(f"✅ <b>Tekshiring:</b> <i>{e(s['check'])}</i>")
        shot_msgs += split('\n'.join(body))
    out.append((f"🎥 Kadrlar ({len(pkg['shots'])} ta)", shot_msgs))

    ed = pkg['edit']
    checklist = '\n'.join(f'☐ {e(c)}' for c in ed['checklist'])
    out.append(('✂️ Montaj va post', split(
        f"✂️ <b>Montaj (CapCut)</b>\n\n<b>Subtitrlar:</b> {e(ed['captions'])}\n\n"
        f"<b>Musiqa va tovush:</b> {e(ed['music'])}\n\n<b>Muqova:</b> {e(ed['cover'])}\n\n"
        f"<b>Post matni</b>\n<pre>{e(ed['post_text_uz'])}</pre>\n\n"
        f"<b>Joylashdan oldin</b>\n{checklist}")))
    return out


def render(pkg):
    """[index, message, …] — every message after the index carries '№N · k/total'."""
    secs = sections(pkg)
    total = 1 + sum(len(ms) for _, ms in secs) + 1          # index + content + file
    num = int(pkg['number'])
    lines, k = [], 2
    for label, ms in secs:
        span = f"{k}" if len(ms) == 1 else f"{k}–{k + len(ms) - 1}"
        lines.append(f"{span}. {label}")
        k += len(ms)
    lines.append(f"{total}. 📄 Toʻliq paket (fayl)")
    index = (f"📦 <b>№{num} · {e(pkg['title_uz'])}</b>\n"
             f"<i>{e(pkg['series'])} · {e(pkg['date'])}</i>\n{tag(pkg)} {series_tag(pkg)}\n\n"
             f"{e(pkg['logline'])}\n\n<b>Mundarija</b> ({total} ta xabar, hammasi shu xabarga javob)\n"
             + '\n'.join(lines) + f"\n\n{LEGEND}")
    msgs, k = [index], 2
    for _, ms in secs:
        for m in ms:
            msgs.append(f"<i>📦 №{num} · {k}/{total}</i>\n{m}")
            k += 1
    return msgs


def split(msg):
    """Cut an over-long message on blank lines, never inside a <pre>."""
    if len(msg) <= LIMIT:
        return [msg]
    out, cur = [], ''
    for para in msg.split('\n\n'):
        if len(para) > LIMIT:                       # a single giant block: hard cut
            para = para[:LIMIT - 20] + ('</pre>' if '<pre>' in para else '') + ' …'
        if len(cur) + len(para) + 2 > LIMIT:
            out.append(cur)
            cur = para
        else:
            cur = f'{cur}\n\n{para}' if cur else para
    return out + [cur] if cur else out


def plain(pkg):
    """The whole package as a .txt file to keep."""
    lines = [f"№{pkg['number']} · {pkg['title_uz']} — {pkg['series']} — {pkg['date']}", '']
    for _, ms in sections(pkg):
        for m in ms:
            lines += [html.unescape(re.sub(r'</?(b|i|pre)>', '', m)), '', '─' * 40, '']
    return '\n'.join(lines)


# ── Telegram ─────────────────────────────────────────────────────────────

def _token():
    t = os.environ.get('FLOW_BOT_TOKEN')
    if not t:
        sys.exit('FLOW_BOT_TOKEN is not set')
    return t


def _chat():
    c = os.environ.get('FLOW_CHAT_ID')
    if not c:
        sys.exit('FLOW_CHAT_ID is not set (run --whoami after the brother presses Start)')
    return c


def api(method, data=None, files=None):
    url = f'https://api.telegram.org/bot{_token()}/{method}'
    if files:
        boundary = uuid.uuid4().hex
        body = b''
        for k, v in (data or {}).items():
            body += (f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n'
                     f'{v}\r\n').encode()
        for k, (fname, content) in files.items():
            body += (f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"; '
                     f'filename="{fname}"\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n'
                     ).encode() + content + b'\r\n'
        body += f'--{boundary}--\r\n'.encode()
        req = urllib.request.Request(url, body, {'Content-Type': f'multipart/form-data; boundary={boundary}'})
    else:
        req = urllib.request.Request(url, json.dumps(data or {}).encode(),
                                     {'Content-Type': 'application/json'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as err:
            detail = err.read().decode(errors='replace')
            if err.code == 429 and attempt < 2:
                time.sleep(json.loads(detail).get('parameters', {}).get('retry_after', 5) + 1)
                continue
            # never echo the URL: it contains the token
            raise SystemExit(f'Telegram {method} failed: HTTP {err.code} {detail}')
        except urllib.error.URLError as err:
            if attempt < 2:
                time.sleep(3)
                continue
            raise SystemExit(f'Telegram {method} unreachable: {err.reason}')


def send(pkg):
    """Index first (pinned), everything else as a reply to it — or, in a group with
    Topics, all of it inside a new topic named after the video."""
    chat = _chat()
    msgs = render(pkg)
    where = {}
    info = api('getChat', {'chat_id': chat}).get('result', {})
    if info.get('is_forum'):
        topic = api('createForumTopic', {'chat_id': chat,
                                         'name': f"№{pkg['number']} · {pkg['title_uz']}"[:128]})
        where['message_thread_id'] = topic['result']['message_thread_id']
    first = api('sendMessage', {'chat_id': chat, 'text': msgs[0], 'parse_mode': 'HTML',
                                'disable_web_page_preview': True, **where})['result']['message_id']
    try:
        api('pinChatMessage', {'chat_id': chat, 'message_id': first, 'disable_notification': True})
    except SystemExit as err:                       # pinning is a nicety, never fatal
        print(f'(not pinned: {err})')
    reply = {'reply_parameters': json.dumps({'message_id': first, 'allow_sending_without_reply': True})}
    for m in msgs[1:]:
        time.sleep(1.1)                              # 1 msg/s per chat
        api('sendMessage', {'chat_id': chat, 'text': m, 'parse_mode': 'HTML',
                            'disable_web_page_preview': True, 'disable_notification': True,
                            **where, 'reply_parameters': {'message_id': first,
                                                          'allow_sending_without_reply': True}})
    time.sleep(1.1)
    api('sendDocument', {'chat_id': chat, **{k: str(v) for k, v in where.items()}, **reply,
                         'caption': f"📄 №{pkg['number']} · {pkg['title_uz']} — toʻliq paket"},
        files={'document': (f"{int(pkg['number']):03d}-{pkg['id']}.txt", plain(pkg).encode())})
    print(f"sent {len(msgs)} messages + 1 file for №{pkg['number']} {pkg['id']}")


def main(argv):
    if '--whoami' in argv:
        for u in api('getUpdates').get('result', []):
            chat = (u.get('message') or u.get('channel_post') or u.get('my_chat_member')
                    or {}).get('chat', {})
            if chat:
                print(chat.get('id'), chat.get('type'), chat.get('title') or chat.get('first_name'),
                      chat.get('username') or '')
        return
    if '--ping' in argv:
        api('sendMessage', {'chat_id': _chat(), 'text': '🎬 Flow Studio: ulanish ishlayapti.'})
        print('ping sent')
        return
    paths = [a for a in argv if not a.startswith('--')]
    if len(paths) != 1:
        sys.exit(__doc__)
    with open(paths[0], encoding='utf-8') as f:
        pkg = json.load(f)
    errs = check(pkg)
    if errs:
        print(f'{len(errs)} problem(s):')
        for x in errs:
            print('  -', x)
        sys.exit(1)
    print(f"OK: {pkg['id']} — {len(pkg['shots'])} shots, {len(pkg['ingredients'])} ingredients, "
          f"{len(render(pkg))} messages")
    if '--check' in argv:
        return
    if '--dry-run' in argv:
        for m in render(pkg):
            print('─' * 60)
            print(m)
        return
    send(pkg)


if __name__ == '__main__':
    main(sys.argv[1:])
