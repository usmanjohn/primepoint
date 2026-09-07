#!/usr/bin/env bash
# The one entry point for every Railway service built from this repo.
#
# WHY A SCRIPT. Railway's config file beats the dashboard, and railway.toml has
# to name exactly one startCommand — so the cron service inherited the web
# server's. It woke at its scheduled minute, ran migrate + attach_exam_audio +
# gunicorn, and sat there as a second website: nothing posted to Telegram, and
# because gunicorn never exits, the next day's trigger had nothing to fire into.
# (Diagnosed 2026-09-07 from its own log: "Listening at: http://0.0.0.0:8080".)
#
# So the command branches here instead, on a variable set in Railway:
#
#   service "primepoint" (the cron)  ROLE=cron   → one Telegram run, then exit
#   service "web"        (the site)  ROLE unset  → migrate, attach audio, serve
#
# Config-as-code is deprecated and stops working 2026-12-01. When that day comes
# this script does not change: paste `bash start.sh` into each service's
# Custom Start Command in the dashboard and delete railway.toml.
set -euo pipefail

if [ "${ROLE:-web}" = "cron" ]; then
    # Posts the Logic Arena puzzle if one is due, then the five daily quiz polls.
    # Exits non-zero on a failed post, so a bad night shows up red in Railway.
    exec python manage.py telegram_daily
fi

python manage.py migrate --noinput

for n in 1 2 3 4 5 6 7 8 9 10; do
    python manage.py attach_exam_audio "$((100 + n))" "exam/data/audio/mock${n}_listening.mp3" || true
done

exec gunicorn point.wsgi --workers 3 --timeout 120 --preload --bind 0.0.0.0:"$PORT"
