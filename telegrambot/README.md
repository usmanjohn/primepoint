# telegrambot — the Powerty Telegram channel

Outbound only. The bot never receives updates, so there is **no webhook, no public
endpoint and nothing stored about who reads the channel**. It posts, and that is all.

| | |
|---|---|
| Bot | `@PowertyuzBot` |
| Channel | `@powertyuz` (bot must be an **admin** with *Post Messages*) |
| Schedule | `0 17 * * *` on the Railway cron service = 22:00 Tashkent. Railway cron is **always UTC** |
| Language | Uzbek. Only the material (an English sentence, a Korean line) is not. |

## What it posts

**Daily — one question as a native Telegram quiz poll.** One tap, marked instantly,
the Uzbek explanation appears under the answer, and an inline button leads to the full
practice on the site. The subject rotates by calendar day, not by a counter, so a
missed day never shifts the cycle:

    Ingliz tili → Koreys tili → Matematika → Rus tili → Matematika (SAT)

A question is never repeated (`TelegramPost` remembers every one used), and when a
subject runs dry the picker falls through to the next in the rotation instead of
failing. 8043 of 8075 published questions fit Telegram's poll limits; the rest are
skipped, never trimmed — a trimmed question can quietly become unanswerable.

**Weekly — the Logic Arena puzzle** when it opens, and its answer when it reveals.
Only the title, hook and difficulty go to Telegram; the body stays on the site, which
is where the answer gets sealed. A puzzle whose reveal already passed is never
announced late.

## Commands

    python manage.py telegram_ping              # token + channel + how many questions left
    python manage.py telegram_ping --post       # sends a real test message
    python manage.py post_daily_quiz --dry-run  # print today's post, send nothing
    python manage.py post_daily_quiz --subject='한국어' --force
    python manage.py post_logic_puzzle --dry-run
    python manage.py telegram_daily             # what cron runs: puzzle check, then quiz

`--dry-run` builds the real post and prints it. Use it before any change goes live.

## Environment

| Variable | Needed | Note |
|---|---|---|
| `TELEGRAM_BOT_TOKEN` | yes | from @BotFather. Never commit it — `.env` is gitignored |
| `TELEGRAM_CHANNEL` | no | defaults to `@powertyuz` |
| `SITE_URL` | **yes in production** | the absolute base for every link in a post. A cron command has no request to derive the host from, so if this is wrong **every button in every post is broken.** |

## The Railway cron service

Railway runs cron as its own service. In the dashboard:

1. **New** → **GitHub Repo** → this repo (same repo as the web service).
2. Settings → **Cron Schedule**: `0 17 * * *` (UTC — 22:00 Tashkent)
3. Settings → **Custom Start Command**: `python manage.py telegram_daily`
4. Variables → give it the same `DATABASE_URL`, `DJANGO_SECRET_KEY`,
   `TELEGRAM_BOT_TOKEN` and `SITE_URL` as the web service (Railway can reference
   the shared ones). **A cron service does not inherit the web service's variables.**

A cron service starts, runs the command, and exits — it is billed only for those
seconds. `telegram_daily` exits non-zero if a post failed, so a bad run shows up red
in the Railway log instead of passing silently.

**Railway's private network is not up the instant the container starts.** A cron job
that connects immediately fails with `could not translate host name
"postgres.railway.internal"`. `telegram_daily` therefore waits for the database (up to
60s) before doing anything. If a run still cannot reach it, point the cron service's
`DATABASE_URL` at the Postgres service's **public** URL (`DATABASE_PUBLIC_URL`,
`…proxy.rlwy.net`), which needs no private network at all.

## Safety

- Running twice in a day posts once: the quiz checks whether one already went out
  (`--force` overrides), and the puzzle commands post only what is due and unposted.
- `TelegramPost` rows are read-only in the admin — deleting one would let the bot
  repeat a question.
