"""
Builds the vintage analysis from datasets/vintage/input/*.parquet into datasets/vintage/result/.
The page's «Пересчитать» button starts this command as its own process; you can also run it
by hand (or monthly from a systemd timer, like build_portfel):

    python manage.py build_vintage
    python manage.py build_vintage --fake      # first write fake data (only if the folder is empty)
"""
import datetime
import json
import os
import traceback

from django.core.management.base import BaseCommand, CommandError

from vintage import fake, process


def write_status(**fields):
    process.BASE.mkdir(parents=True, exist_ok=True)
    process.STATUS_FILE.write_text(json.dumps(fields, ensure_ascii=False))


class Command(BaseCommand):
    help = "Build the vintage analysis (triangles, transitions) from the input parquet files."

    def add_arguments(self, p):
        p.add_argument("--fake", action="store_true", help="write fake input data first, if there is none")

    def handle(self, *a, **o):
        def log(msg):
            self.stdout.write(str(msg))
            self.stdout.flush()

        started = datetime.datetime.now().isoformat(timespec="seconds")
        write_status(running=True, started=started, pid=os.getpid())
        try:
            if o["fake"] and not process.input_files():
                rows = fake.make(process.INPUT_DIR / "fake.parquet")
                log(f"fake data written: {rows:,} rows")
            meta = process.build(log=log)
        except Exception as e:
            write_status(running=False, started=started, error=f"{type(e).__name__}: {e}",
                         trace=traceback.format_exc()[-3000:])
            raise CommandError(str(e))
        write_status(running=False, started=started, finished=meta["built_at"])
        self.stdout.write(self.style.SUCCESS(f"vintage built: {meta['loans']:,} loans, "
                                             f"{meta['first_month']} … {meta['last_month']}"))
