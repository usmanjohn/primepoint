from django.shortcuts import render, redirect
import os
import re
from datetime import datetime, timedelta
from django.http import FileResponse, Http404, HttpResponse
from io import BytesIO
import pandas as pd

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pathlib import Path
from functions import common_choices

BASE_DIR = Path(__file__).resolve().parent.parent
datasets_folder = BASE_DIR / "datasets"
portfel_input_folder = datasets_folder / "portfel" / "input"
portfel_svod_folder = datasets_folder / "portfel" / "svod"
portfel_all_folder = datasets_folder / "portfel" / "all"
balans_svod_folder = datasets_folder / "balans" / "svod"
dynamics_summary_folder = datasets_folder / "dynamics" / "summary"


# ---------------------------------------------------------------- helpers

def list_files(folder):
    """Files of one folder, newest name first.
    Each item: name (shown, without .parquet) and path (relative to datasets,
    e.g. 'portfel/svod/svod_2026-11-01.parquet') - the path is what the
    checkbox sends, so a file is always found in ITS folder only."""
    if not folder.exists():
        return []
    files = []
    for f in sorted(folder.glob("*.parquet"), reverse=True):
        files.append({
            'name': f.stem,
            'path': f.relative_to(datasets_folder).as_posix(),
        })
    return files


def safe_file(relative_path):
    """Turn 'portfel/svod/x.parquet' into a real path, but ONLY if it is a
    file inside the datasets folder. Anything else (../, missing) -> None."""
    path = (datasets_folder / relative_path).resolve()
    if datasets_folder.resolve() not in path.parents:
        return None
    if not path.is_file():
        return None
    return path


def delete_files(relative_paths):
    """Delete the given files. Returns how many were deleted."""
    deleted = 0
    for rel in relative_paths:
        path = safe_file(rel)
        if path is None:
            continue
        try:
            path.unlink()
            deleted += 1
        except OSError:
            pass
    return deleted


# ---------------------------------------------------------------- pages

@login_required
def home(request):
    context = {
        'portfels_raw': list_files(portfel_input_folder),
        'portfels_all': list_files(portfel_all_folder),
        'portfels_svod': list_files(portfel_svod_folder),
        'balans_svod': list_files(balans_svod_folder),
    }
    return render(request, 'history/home.html', context)


@login_required
def download_file(request, filename):
    filename = f"{filename}.parquet"
    if "balans" in filename:
        csv_filepath = os.path.join(balans_svod_folder, filename)
    elif "svod" in filename:
        csv_filepath = os.path.join(portfel_svod_folder, filename)
    elif "all" in filename:
        csv_filepath = os.path.join(portfel_all_folder, filename)
    elif "raw" in filename:
        csv_filepath = os.path.join(portfel_input_folder, filename)
    else:
        raise Http404("File not found")
    if not os.path.exists(csv_filepath):
        raise Http404("File not found")

    df = pd.read_parquet(csv_filepath)
    excel_buffer = BytesIO()
    df.to_excel(excel_buffer, index=False, engine='openpyxl')
    excel_buffer.seek(0)

    response = FileResponse(excel_buffer, as_attachment=True, filename=f"{os.path.splitext(filename)[0]}.xlsx")
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    return response


@login_required
def export_model_to_excel(request):
    filename = 'summary.parquet'
    file_full = f"{dynamics_summary_folder}/{filename}"
    df = pd.read_parquet(file_full)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=all_summary_data.xlsx'
    df.to_excel(response, index=False)
    return response


@login_required
def cleanup_old_portfels(request):
    if not request.user.is_staff:
        messages.error(request, "У вас нет прав для выполнения этой операции.")
        return redirect('history')
    if request.method != "POST":
        return redirect('history')

    action = request.POST.get('action')

    # Button 1: «Удалить выбранные» - delete ONLY the ticked files
    if action == 'selected':
        selected = request.POST.getlist('selected_files')
        if not selected:
            messages.warning(request, "Ничего не выбрано.")
            return redirect('history')
        deleted = delete_files(selected)
        messages.success(request, f"Удалено выбранных файлов: {deleted}")
        return redirect('history')

    # Button 2: «Авто-очистка» - older than 7 days and not a month-end
    if action == 'auto':
        folders = [portfel_input_folder, portfel_svod_folder, portfel_all_folder, balans_svod_folder]
        month_ends = {datetime.strptime(d, "%d.%m.%Y").date() for d in common_choices.official_month_ends}
        one_week_ago = datetime.now().date() - timedelta(days=7)
        date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')

        to_delete = []
        for folder in folders:
            if not folder.exists():
                continue
            for file_path in folder.glob("*.parquet"):
                match = date_pattern.search(file_path.name)
                if not match:
                    continue  # no date in the name -> never auto-deleted
                try:
                    file_date = datetime.strptime(match.group(), "%Y-%m-%d").date()
                except ValueError:
                    continue
                if file_date < one_week_ago and file_date not in month_ends:
                    to_delete.append(file_path.relative_to(datasets_folder).as_posix())

        deleted = delete_files(to_delete)
        messages.success(request, f"Авто-очистка завершена. Удалено файлов: {deleted}")
        return redirect('history')

    messages.error(request, "Неизвестное действие.")
    return redirect('history')


# ---------------------------------------------------------------- admin: every file in datasets/

@login_required
def datasets_files(request):
    """Admin only: every file inside datasets/ (all sub-folders), grouped by
    folder, with size and date. Tick any files and delete them."""
    if not request.user.is_staff:
        messages.error(request, "У вас нет прав для просмотра этой страницы.")
        return redirect('history')

    if request.method == "POST":
        selected = request.POST.getlist('selected_files')
        if not selected:
            messages.warning(request, "Ничего не выбрано.")
        else:
            deleted = delete_files(selected)
            messages.success(request, f"Удалено файлов: {deleted}")
        return redirect('datasets-files')

    # { 'portfel/svod': [file, file, ...], 'balans/svod': [...], ... }
    folders = {}
    total_size = 0
    for f in sorted(datasets_folder.rglob("*")):
        if not f.is_file():
            continue
        stat = f.stat()
        total_size += stat.st_size
        folder_name = f.parent.relative_to(datasets_folder).as_posix()
        if folder_name == '.':
            folder_name = '(корень datasets)'
        folders.setdefault(folder_name, []).append({
            'name': f.name,
            'path': f.relative_to(datasets_folder).as_posix(),
            'size_mb': round(stat.st_size / 1024 / 1024, 2),
            'modified': datetime.fromtimestamp(stat.st_mtime),
        })

    # newest files on top inside each folder
    for files in folders.values():
        files.sort(key=lambda x: x['modified'], reverse=True)

    context = {
        'folders': folders,
        'total_files': sum(len(v) for v in folders.values()),
        'total_size_mb': round(total_size / 1024 / 1024, 1),
    }
    return render(request, 'history/datasets.html', context)
