"""
Builds the portfel files for one day WITHOUT a user — the same steps as the views
portfel_get + portfel_process, but with no request, no session and no messages.

Used by the command `python manage.py build_portfel`, which the systemd timer runs
on working days at 08:00, 09:00, 10:00, 12:00 and 14:00 (see management/commands/build_portfel.py).

Files are written as "<name>.tmp" first and renamed at the end, so a page opened while
the job is still writing never sees a half-written file. The svod file is written LAST:
if it exists, the day is finished.
"""
import datetime
import os
from pathlib import Path

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

from functions import common_functions
from . import queries
from .process import process_portfel_best

BASE_DIR = Path(__file__).resolve().parent.parent

portfel_input_folder = BASE_DIR / "datasets" / "portfel" / "input"
portfel_svod_folder = BASE_DIR / "datasets" / "portfel" / "svod"
portfel_all_folder = BASE_DIR / "datasets" / "portfel" / "all"
utils_path = BASE_DIR / "utils" / "useforauto.xlsx"


class NotReadyYet(Exception):
    """The database returned no rows for this day — it is not updated yet."""


def previous_working_day(today=None):
    """Yesterday; on Monday it is Friday (and on Saturday/Sunday also Friday)."""
    today = today or datetime.date.today()
    days_back = {0: 3, 6: 2, 5: 1}.get(today.weekday(), 1)   # Mon → Fri, Sun → Fri, Sat → Fri
    return today - datetime.timedelta(days=days_back)


def raw_path(day):
    return portfel_input_folder / f"raw_{day}.parquet"


def svod_path(day):
    return portfel_svod_folder / f"svod_{day}.parquet"


def all_path(day):
    return portfel_all_folder / f"all_{day}.parquet"


def is_ready(day):
    return svod_path(day).exists()


def fetch_raw(day, log=print):
    """Query Oracle for the day and save raw_<day>.parquet. Raises NotReadyYet on 0 rows."""
    os.makedirs(portfel_input_folder, exist_ok=True)
    final = raw_path(day)
    tmp = final.with_name(final.name + ".tmp")
    conn = None
    pq_writer = None
    rows = 0
    try:
        conn = common_functions.get_oracle_connection()
        batch_generator = conn.fetch_df_batches(
            queries.best_portfel_script,
            parameters={'pdate': day},
            size=100000,
        )
        for odf in batch_generator:
            arrow_table = pa.table(odf)
            if pq_writer is None and arrow_table.num_rows == 0:
                break
            if pq_writer is None:
                pq_writer = pq.ParquetWriter(tmp, arrow_table.schema)
            pq_writer.write_table(arrow_table)
            rows += arrow_table.num_rows
            log(f"  fetched {rows:,} rows")
    finally:
        if pq_writer:
            pq_writer.close()
        if conn:
            conn.close()

    if rows == 0:
        tmp.unlink(missing_ok=True)
        raise NotReadyYet(f"no rows for {day} — the database is not updated yet")
    os.replace(tmp, final)
    log(f"  raw saved: {final.name} ({rows:,} rows)")


def process_day(day, log=print):
    """raw_<day>.parquet → all_<day>.parquet + svod_<day>.parquet (svod last)."""
    os.makedirs(portfel_svod_folder, exist_ok=True)
    os.makedirs(portfel_all_folder, exist_ok=True)
    df_raw = pd.read_parquet(raw_path(day))
    svod_df, all_df = process_portfel_best(df_raw, utils_path)

    try:
        final = all_path(day)
        tmp = final.with_name(final.name + ".tmp")
        all_df.to_parquet(tmp)
        os.replace(tmp, final)
        log(f"  all saved: {final.name}")
    except Exception as e:
        log(f"  all file is not saved: {e}")          # same as the view: svod is what matters

    final = svod_path(day)
    tmp = final.with_name(final.name + ".tmp")
    svod_df.to_parquet(tmp)
    os.replace(tmp, final)
    log(f"  svod saved: {final.name}")


def build_day(day, force=False, log=print):
    """Everything for one day. Returns False if it was already done, True if built now."""
    if is_ready(day) and not force:
        return False
    if force or not raw_path(day).exists():
        fetch_raw(day, log=log)
    else:
        log("  raw file already exists, only processing")
    process_day(day, log=log)
    return True
