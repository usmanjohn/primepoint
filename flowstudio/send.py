#!/usr/bin/env python3
"""Check a Flow Studio package and send it to Telegram.  See GUIDE.md.

    python3 flowstudio/send.py PACKAGE.json --check     # gate only, prints errors
    python3 flowstudio/send.py PACKAGE.json --dry-run   # gate + print the messages
    python3 flowstudio/send.py PACKAGE.json             # gate + send
    python3 flowstudio/send.py --whoami                 # list chats that wrote to the bot
    python3 flowstudio/send.py --ping                   # send one test message

Needs FLOW_BOT_TOKEN and FLOW_CHAT_ID in the environment to send.
Standard library only, so it runs in a bare cloud container.

The messages are SHORT on purpose (the user's request, 2026-10-03): what to make, what to
name it, what to attach, which Flow mode, then the prompt. Facts and sources stay in the
JSON (and the log branch) — they are checked here but never sent.
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

METHODS = {'Frames to Video', 'Ingredients to Video', 'Text to Video', 'Extend'}
LIMIT = 3900                      # Telegram's cap is 4096; leave room for tags
BAD_APOSTROPHE = re.compile(r"[oOgG]['‘’`]")
CYRILLIC = re.compile(r'[Ѐ-ӿ]')
REF_ID = re.compile(r'^R\d+$')
SECONDS = 8                       # one Veo clip
BROTHERS = ('Inom', 'Jonibek')    # one package each, every day (the user's request, 2026-10-04)
WHO = BROTHERS + ('Birga',)       # 'Birga' = a series package for whoever films it (2026-10-05)


# ── the gate ─────────────────────────────────────────────────────────────

def _uz_errors(where, text):
    errs = []
    m = BAD_APOSTROPHE.search(text or '')
    if m:
        errs.append(f"{where}: write oʻ/gʻ with ʻ (U+02BB), not an apostrophe: {m.group()!r}")
    if CYRILLIC.search(text or ''):
        errs.append(f'{where}: Cyrillic letter inside Uzbek text')
    return errs


def _flat(text):
    """Compare a spoken line with the prompt: apostrophe variants and spacing ignored."""
    text = re.sub(r"[ʻʼ‘’`']", "'", (text or '').replace('…', '...'))
    return re.sub(r'\s+', ' ', text).strip().lower()


def _froms(ref):
    f = ref.get('from') or []
    return [f] if isinstance(f, str) else list(f)


def check(pkg):
    errs = []
    for key in ('id', 'number', 'date', 'series', 'title_uz', 'concept_uz', 'format_uz',
                'sources', 'facts', 'style_line', 'refs', 'scenes'):
        if not pkg.get(key):
            errs.append(f'missing or empty: {key}')
    if errs:
        return errs
    if pkg.get('for') not in WHO:
        errs.append(f"for must be one of {WHO} — whose video this is")
    if not str(pkg['number']).isdigit():
        errs.append("number must be a whole number (the video's №)")
    for k in ('title_uz', 'concept_uz', 'format_uz', 'post_text_uz'):
        errs += _uz_errors(k, pkg.get(k, ''))
    if len(pkg['concept_uz']) > 500:
        errs.append(f"concept_uz is {len(pkg['concept_uz'])} chars — keep it under 500 (2-3 sentences)")
    if 'no text' not in pkg['style_line'].lower():
        errs.append('style_line must forbid text in the picture ("No text, …")')

    seen = []
    for r in pkg['refs']:
        rid = r.get('id', '')
        if not REF_ID.match(rid):
            errs.append(f'ref id {rid!r} must look like R1, R2 …')
        if rid in seen:
            errs.append(f'ref {rid} defined twice')
        for src in _froms(r):
            if src not in seen:
                errs.append(f"{rid}: attaches {src!r}, which is not an EARLIER ref")
        if not r.get('name_uz') or not r.get('prompt'):
            errs.append(f'{rid}: needs name_uz and prompt')
        errs += _uz_errors(f'{rid} name_uz', r.get('name_uz', ''))
        if CYRILLIC.search(r.get('prompt', '')) or re.search(r'[ʻʼ]', r.get('prompt', '')):
            errs.append(f'{rid}: prompt must be English')
        seen.append(rid)

    if not 4 <= len(pkg['scenes']) <= 12:
        errs.append(f"{len(pkg['scenes'])} scenes — want 4-12 (8 s each)")
    done = []
    for sc in pkg['scenes']:
        tag = f"sahna {sc.get('n')}"
        m = sc.get('method')
        if m not in METHODS:
            errs.append(f'{tag}: method {m!r} not one of {sorted(METHODS)}')
        if not sc.get('title_uz'):
            errs.append(f'{tag}: missing title_uz')
        errs += _uz_errors(f'{tag} title_uz', sc.get('title_uz', ''))
        refs = [sc.get('start'), sc.get('end')] + list(sc.get('attach') or [])
        for r in filter(None, refs):
            if r not in seen:
                errs.append(f'{tag}: uses {r!r}, which is not a ref')
        if m == 'Frames to Video' and not sc.get('start'):
            errs.append(f'{tag}: Frames to Video needs "start" (a ref id)')
        if m == 'Ingredients to Video' and not 1 <= len(sc.get('attach') or []) <= 3:
            errs.append(f'{tag}: Ingredients to Video takes 1-3 refs in "attach"')
        if m == 'Extend' and str(sc.get('extends')) not in done:
            errs.append(f'{tag}: Extend must name an EARLIER scene in "extends"')
        prompt = sc.get('prompt', '')
        if not prompt:
            errs.append(f'{tag}: missing prompt')
        if 'no subtitles' not in prompt.lower():
            errs.append(f'{tag}: prompt must end with "No subtitles, no on-screen text."')
        if CYRILLIC.search(prompt) or re.search(r'[ʻʼ]', prompt):
            errs.append(f"{tag}: prompt must be English; Uzbek lines inside it use a plain ' (to'g'ri)")
        for ln in sc.get('lines') or []:
            if not ln.get('who') or not ln.get('text'):
                errs.append(f'{tag}: every line needs who and text')
                continue
            errs += _uz_errors(f'{tag} line', f"{ln['who']} {ln['text']}")
            if _flat(ln['text']) not in _flat(prompt):
                errs.append(f"{tag}: the line «{ln['text'][:40]}…» is not in the prompt word for word")
        if sc.get('lines') and 'in uzbek' not in prompt.lower():
            errs.append(f'{tag}: say "speaks in Uzbek with a … voice" in the prompt')
        done.append(str(sc.get('n')))
    if not any(sc.get('lines') for sc in pkg['scenes']):
        errs.append('nobody speaks — at least half the scenes should have Uzbek lines')
    return errs


# ── rendering (Telegram HTML) ────────────────────────────────────────────

def e(text):
    return html.escape(str(text or ''), quote=False)


def tag(pkg):
    return f"#video{int(pkg['number']):03d}"


def series_tag(pkg):
    return '#' + re.sub(r'[^0-9A-Za-z]', '', pkg['series'].title())


def clock(n):
    t = (int(n) - 1) * SECONDS
    return f'{t // 60}:{t % 60:02d}'


def pack(head, cards):
    """Cards into as few messages as fit; the head opens the first."""
    out, cur = [], head
    for c in cards:
        if len(cur) + len(c) + 2 > LIMIT:
            out.append(cur)
            cur = ''
        cur = f'{cur}\n\n{c}' if cur else c
    return out + [cur]


def sections(pkg):
    refs = []
    for r in pkg['refs']:
        how = f" ({e(' + '.join(_froms(r)))} ni biriktiring)" if r.get('from') else ''
        if r.get('saved'):                # a series cast image made in an earlier episode
            refs.append(f"<b>{e(r['id'])} — {e(r['name_uz'])}</b> ♻️ <i>oldingi qismdan saqlangan — "
                        f"qayta yaratmang</i>")
            continue
        prompt = r['prompt'] if r.get('from') else f"{r['prompt'].rstrip()} {pkg['style_line']}"
        refs.append(f"<b>{e(r['id'])} — {e(r['name_uz'])}</b>{how}\n<pre>{e(prompt)}</pre>")
    chain = any(r.get('from') for r in pkg['refs'])
    out = pack("1️⃣ 🎨 <b>RASMLAR</b> — Nano Banana Pro, 9:16. Har birini nomi bilan saqlang (R1, R2…)."
               + ("\n«… ni biriktiring» — oʻsha rasm(lar)ni Nano Bananaʼga biriktirib, promptni bering."
                  if chain else ''), refs)

    script = []
    for sc in pkg['scenes']:
        lines = sc.get('lines') or []
        if not lines:
            script.append(f"<b>{e(sc['n'])} · {clock(sc['n'])}</b> — <i>gapsiz</i>")
        for k, ln in enumerate(lines):
            lead = f"<b>{e(sc['n'])} · {clock(sc['n'])}</b> " if k == 0 else '      '
            script.append(f"{lead}{e(ln['who'])}: «{e(ln['text'])}»")
    out += pack('2️⃣ 🎬 <b>SSENARIY</b>', ['\n'.join(script)])

    scenes = []
    for sc in pkg['scenes']:
        m = sc['method']
        if m == 'Frames to Video':
            how = f"start: {sc['start']}" + (f", end: {sc['end']}" if sc.get('end') else '')
        elif m == 'Ingredients to Video':
            how = ' + '.join(sc['attach'])
        elif m == 'Extend':
            how = f"{sc['extends']}-sahnani davom ettiring"
        else:
            how = 'rasmsiz'
        scenes.append(f"<b>Sahna {e(sc['n'])} · {e(sc['title_uz'])}</b> — {e(m)}, {e(how)}\n"
                      f"<pre>{e(sc['prompt'])}</pre>")
    out += pack("3️⃣ 🛠 <b>FLOWʼDA YARATISH</b>\nYangi loyiha, 9:16. Veo 3.1: avval Fastʼda sinang, "
                "eng yaxshisini Qualityʼda. Har sahna 8 soniya. Oʻzbekcha gap buzilib chiqsa — "
                "qayta generatsiya qiling.", scenes)
    if pkg.get('post_text_uz'):
        out.append(f"4️⃣ 📲 <b>POST MATNI</b>\n<pre>{e(pkg['post_text_uz'])}</pre>")
    return out


def render(pkg):
    """[pinned header, message, …]; every message after the header carries '№N · k/total'."""
    body = sections(pkg)
    num = int(pkg['number'])
    total = len(body) + 1
    who = '👥 <b>Birga</b>' if pkg['for'] == 'Birga' else f"👤 <b>{e(pkg['for'])} uchun</b>"
    first = (f"{who}\n"
             f"🎬 <b>№{num} · «{e(pkg['title_uz'])}»</b>\n#{pkg['for']} {tag(pkg)} {series_tag(pkg)}\n\n"
             f"<b>Gʻoya:</b> {e(pkg['concept_uz'])}\n<b>Format:</b> {e(pkg['format_uz'])}\n\n"
             "1️⃣ Rasmlar → 2️⃣ Ssenariy → 3️⃣ Flowʼda yaratish (hammasi shu xabarga javob)\n\n"
             "✅ Video tayyor boʻlsa — shu xabarga 👍 bosing.")
    return [first] + [f"<i>№{num} · {k}/{total}</i>\n{m}" for k, m in enumerate(body, 2)]


def plain(pkg):
    """The whole package as a .txt file to keep."""
    lines = [pkg['for'] if pkg['for'] == 'Birga' else f"{pkg['for']} uchun", f"№{pkg['number']} · {pkg['title_uz']} — {pkg['series']} — {pkg['date']}", '',
             pkg['concept_uz'], pkg['format_uz'], '']
    for m in sections(pkg):
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
        sys.exit('FLOW_CHAT_ID is not set (add the bot to the channel as admin, post once, run --whoami)')
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
                                         'name': f"{pkg['for']} · №{pkg['number']} · {pkg['title_uz']}"[:128]})
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
    print(f"OK: {pkg['id']} — {len(pkg['refs'])} rasm, {len(pkg['scenes'])} sahna, "
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
