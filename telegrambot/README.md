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

**Daily — one question per subject as native Telegram quiz polls.** Five polls a day,
one for each subject, three seconds apart:

    Ingliz tili · Koreys tili · Matematika · Rus tili · Matematika (SAT)

One tap, marked instantly, the Uzbek explanation appears under the answer, and an
inline button leads to the full practice on the site. The guard is per subject per
day (derived from the questions already sent, so no extra column), so a re-run sends
only what is missing. `post_daily_quiz` without `--each-subject` still sends a single
question, rotating by calendar day.

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

The cron service in this project is the one confusingly named **`primepoint`**
(the web server is `web`). It builds the same repo, on the same commits, and is
billed only for the seconds a run takes.

**Its start command comes from `railway.cron.toml`, not from railway.toml.**
Railway's config-as-code overrides the dashboard, and the repo root's
`railway.toml` starts gunicorn — so a cron service left on the default config
wakes at its minute, runs migrate + attach_exam_audio + **gunicorn**, and sits
there as a second web server, posting nothing and never exiting. That is exactly
what it did every day from 2026-09-02 until 2026-09-07; its own log ends with
`Listening at: http://0.0.0.0:8080`. Worse, a run that never exits means the next
day's trigger has nothing to fire into, so one bad night silences the channel
indefinitely.

The setting that fixes it:

    Railway → service `primepoint` → Settings → Config-as-code
        Config file path:  railway.cron.toml

That file carries the schedule (`0 17 * * *` = 22:00 Tashkent), the start command
(`python manage.py telegram_daily`) and `restartPolicyType = "never"`. Change the
posting time there, in the repo — not in the dashboard, where the file overrides it.

**Never point the `web` service at `railway.cron.toml`, and never put a
`cronSchedule` in `railway.toml`** — either would turn the website into a cron job.

Variables: the cron service needs its own `DATABASE_URL`, `TELEGRAM_BOT_TOKEN`
and `SITE_URL`. **A cron service does not inherit the web service's variables.**

**Railway's private network is not up the instant the container starts.** A cron job
that connects immediately fails with `could not translate host name
"postgres.railway.internal"`. `telegram_daily` therefore waits for the database (up to
60s) before doing anything. If a run still cannot reach it, point the cron service's
`DATABASE_URL` at the Postgres service's **public** URL (`DATABASE_PUBLIC_URL`,
`…proxy.rlwy.net`), which needs no private network at all.

### Reading a run

    railway logs --service primepoint

A healthy run prints `── post_logic_puzzle ──`, `── post_daily_quiz ──`, the five
polls, and `Qolgan savollar: …`. If it prints `Booting worker` or `Listening at`,
the config file is not being applied — check the Config-as-code path first.

## Safety

**The bot refuses to post from a local database.** `DATABASES` falls back to local
sqlite whenever `DATABASE_URL` is unset, so a plain `manage.py` run — or `railway run`
against a service without that variable — would send real posts built from dev rows,
with dev ids in every link. That shipped once, on 2026-09-02, and every link pointed
at whatever held that id in production. `api.refuse_local_database()` now blocks any
send whose connection is sqlite; `--dry-run` still works locally.

- Running twice in a day posts once: the quiz checks whether one already went out
  (`--force` overrides), and the puzzle commands post only what is due and unposted.
- `TelegramPost` rows are read-only in the admin — deleting one would let the bot
  repeat a question.
