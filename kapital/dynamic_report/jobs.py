"""
Report jobs run as their OWN process — `manage.py build_report --run-id N` — never inside a
gunicorn worker.

Why (learned on the server, 2026-10-16): a full-history run on ~14M rows needs gigabytes.
Run as a thread inside a gunicorn worker, the out-of-memory killer took the whole worker:
the report died, the page's status request got nginx's HTML 502 («Unexpected token '<'»),
and the row stayed «выполняется» forever because nothing was left to mark it failed.

Now:
  * the job is a separate process, so a killed job never takes the web server with it;
  * a file lock lets ONE report build at a time across all gunicorn workers (a Python lock
    only covered one worker, so three workers could run three reports at once);
  * the job writes its pid into the row; reap_stale() marks a row whose process is gone as
    failed, with the reason, so nothing stays «выполняется» forever.

Works on the Linux server and on a Windows PC alike: the lock and the "is it alive" check
have a branch for each (fcntl does not exist on Windows, and there os.kill(pid, 0) would
not check the process — it would KILL it).
"""
from __future__ import annotations

import os
import signal
import subprocess
import sys
import threading
import time
from contextlib import contextmanager
from pathlib import Path

from django.conf import settings
from django.utils import timezone

from .models import ReportRun

WINDOWS = os.name == "nt"
if WINDOWS:
    import ctypes
    import msvcrt
else:
    import fcntl

BASE_DIR = Path(settings.BASE_DIR)
OUT_DIR = BASE_DIR / "datasets" / "dynamics" / "report"
LOCK_FILE = OUT_DIR / ".build.lock"
GRACE_SECONDS = 120      # a fresh row may have no pid yet while Python and pandas start up

OOM_HINT = ("процесс отчёта остановлен системой (SIGKILL) — почти всегда это нехватка памяти. "
            "Проверка: sudo dmesg -T | grep -i 'out of memory'. Выберите период короче.")


def log_path(pk):
    return OUT_DIR / f"run_{pk}.log"


def launch(run):
    """Start the job for this row in its own process; returns at once."""
    manage = BASE_DIR / "manage.py"
    if not manage.exists():
        raise FileNotFoundError(f"не найден {manage}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if WINDOWS:   # no console window, and Ctrl+C in the runserver console does not reach the job
        detach = dict(creationflags=subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW)
    else:
        detach = dict(start_new_session=True)
    with open(log_path(run.pk), "ab") as log:
        proc = subprocess.Popen(
            [sys.executable, str(manage), "build_report", "--run-id", str(run.pk)],
            cwd=str(BASE_DIR), stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
            close_fds=True, **detach)
    # wait for it in the background: collects the exit code (no zombie process) and turns
    # a crash into a readable error at once, without waiting for the next status poll
    threading.Thread(target=_watch, args=(proc, run.pk), daemon=True).start()
    return proc.pid


def _watch(proc, pk):
    from django.db import connection
    code = proc.wait()
    try:
        if code != 0:
            _fail_if_active(pk, _exit_reason(code, pk))
    finally:
        connection.close()               # a thread must not leak its connection


def _exit_reason(code, pk):
    if not WINDOWS and code == -signal.SIGKILL:
        return OOM_HINT
    if code < 0:
        return f"процесс отчёта остановлен сигналом {-code}"
    return f"процесс отчёта завершился с кодом {code}\n\n{_log_tail(pk)}"


def _log_tail(pk, n=2000):
    try:
        return log_path(pk).read_text(errors="replace")[-n:]
    except OSError:
        return ""


def _fail_if_active(pk, reason):
    ReportRun.objects.filter(pk=pk, status__in=[ReportRun.PENDING, ReportRun.RUNNING]).update(
        status=ReportRun.FAILED, step="", error=reason, finished_at=timezone.now())


def _alive(pid):
    """Is a build_report process with this pid still running? (A zombie counts as dead.)"""
    if WINDOWS:
        return _alive_windows(pid)
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    proc = Path(f"/proc/{pid}")
    if proc.exists():                                     # Linux: rule out a zombie / a reused pid
        try:
            state = (proc / "stat").read_text().rsplit(")", 1)[1].split()[0]
            cmd = (proc / "cmdline").read_bytes()
        except (OSError, IndexError):
            return True
        return state != "Z" and b"build_report" in cmd
    return True


def _alive_windows(pid):
    """Windows: ask the system for the process's exit code; 259 = STILL_ACTIVE."""
    k32 = ctypes.windll.kernel32
    handle = k32.OpenProcess(0x1000, False, pid)        # PROCESS_QUERY_LIMITED_INFORMATION
    if not handle:
        return False                                    # no such process
    try:
        code = ctypes.c_ulong()
        if not k32.GetExitCodeProcess(handle, ctypes.byref(code)):
            return True
        return code.value == 259
    finally:
        k32.CloseHandle(handle)


def reap_stale():
    """Mark every «в очереди / выполняется» row whose process is gone as failed."""
    now = timezone.now()
    for r in ReportRun.objects.filter(status__in=[ReportRun.PENDING, ReportRun.RUNNING]):
        pid = (r.stats or {}).get("pid")
        if pid:
            if not _alive(int(pid)):
                _fail_if_active(r.pk, "процесс отчёта остановлен: нехватка памяти (sudo dmesg -T | grep -i "
                                      "'out of memory') или перезапуск сервера во время расчёта.\n\n"
                                      + _log_tail(r.pk))
        elif (now - r.created_at).total_seconds() > GRACE_SECONDS:
            _fail_if_active(r.pk, "расчёт прерван: процесс не запустился или был остановлен "
                                  "(перезапуск сервера или нехватка памяти)")


@contextmanager
def build_lock(on_wait=None):
    """One report at a time on this server, whichever gunicorn worker or shell started it."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOCK_FILE, "a+") as f:
        if WINDOWS:
            waited = False
            while True:
                try:
                    f.seek(0)
                    msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
                    break
                except OSError:                           # held by another report
                    if not waited and on_wait:
                        on_wait()
                    waited = True
                    time.sleep(2)
        else:
            try:
                fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                if on_wait:
                    on_wait()
                fcntl.flock(f, fcntl.LOCK_EX)             # wait for the other report to finish
        yield                                             # closing the file releases the lock
