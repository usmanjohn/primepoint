"""
Builds the portfel for the previous working day (on Monday: Friday), without a user.

The systemd timer runs it on working days at 08:00, 09:00, 10:00, 12:00 and 14:00:
  * day already built     → it does nothing (so after a success the later runs are free);
  * database not updated  → it fails, and the next run tries again;
  * after the 14:00 run   → nobody tries any more; that day simply has no portfel.

By hand:
    python manage.py build_portfel                     # previous working day
    python manage.py build_portfel --date 2026-10-23   # a chosen day
    python manage.py build_portfel --date 2026-10-23 --force   # query and process again
"""
import datetime
import traceback

from django.core.management.base import BaseCommand, CommandError

from portfel import daily

LAST_TRY_HOUR = 14


class Command(BaseCommand):
    help = "Build the portfel files for the previous working day."

    def add_arguments(self, p):
        p.add_argument("--date", type=datetime.date.fromisoformat, default=None,
                       help="YYYY-MM-DD; default: previous working day")
        p.add_argument("--force", action="store_true",
                       help="query and process again even if the files exist")

    def handle(self, *a, **o):
        day = o["date"] or daily.previous_working_day()
        now = datetime.datetime.now()
        self.stdout.write(f"{now:%Y-%m-%d %H:%M} portfel for {day}")

        def log(msg):
            self.stdout.write(str(msg))
            self.stdout.flush()

        try:
            built = daily.build_day(day, force=o["force"], log=log)
        except Exception as e:
            if not isinstance(e, daily.NotReadyYet):
                log(traceback.format_exc())
            if o["date"] is None and now.hour >= LAST_TRY_HOUR:
                raise CommandError(f"{day}: {e}. That was the last try for today — giving up.")
            raise CommandError(f"{day}: {e}. Will try again at the next run.")

        if built:
            self.stdout.write(self.style.SUCCESS(f"{day}: done"))
        else:
            self.stdout.write(f"{day}: already done, nothing to do")
