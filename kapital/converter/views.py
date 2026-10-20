"""
PDF converter: one page with a form per tool; each form posts to run(), which answers with
the finished file as a download. Nothing is written to disk or to the database: the upload
is read into memory, processed by pdftools.py, and sent straight back.
"""
import io
from pathlib import Path

from django.http import FileResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from . import pdftools
from .pdftools import ToolError

MAX_MB = 50                                    # per request, all files together

PDF = "application/pdf"
TOOLS = [  # (key, icon, title, what it does) — in the order shown on the page
    ("merge", "fa-object-group", "Объединить PDF", "Несколько PDF → один файл"),
    ("pages", "fa-arrow-down-1-9", "Страницы: выбрать, переставить, удалить", "Новый PDF из нужных страниц в нужном порядке"),
    ("split", "fa-scissors", "Разделить PDF", "Каждые N страниц → отдельный файл, всё в ZIP"),
    ("rotate", "fa-rotate-right", "Повернуть страницы", "Все или выбранные страницы на 90°, 180°, 270°"),
    ("word", "fa-file-word", "PDF → Word", "Текст, абзацы и таблицы в .docx"),
    ("excel", "fa-file-excel", "PDF → Excel", "Все таблицы из PDF в .xlsx"),
]


def _context(**extra):
    tools = [{"key": k, "icon": i, "title": t, "about": a, "on": pdftools.AVAILABLE[k],
              "package": pdftools.PACKAGE[k]} for k, i, t, a in TOOLS]
    return {"tools": tools, "max_mb": MAX_MB, **extra}


def page(request):
    return render(request, "converter/page.html", _context())


def _pdfs(request):
    """Uploaded PDFs as [(name, bytes)], with the size and type checks."""
    files = request.FILES.getlist("files")
    if not files:
        raise ToolError("Выберите файл.")
    if sum(f.size for f in files) > MAX_MB * 1024 * 1024:
        raise ToolError(f"Слишком большие файлы: максимум {MAX_MB} МБ за раз.")
    out = []
    for f in files:
        if not f.name.lower().endswith(".pdf"):
            raise ToolError(f"{f.name}: нужен файл .pdf")
        out.append((f.name, f.read()))
    return out


def _download(data, filename, content_type):
    return FileResponse(io.BytesIO(data), as_attachment=True, filename=filename, content_type=content_type)


@require_POST
def run(request, tool):
    if tool not in pdftools.AVAILABLE:
        return render(request, "converter/page.html", _context(error={"tool": tool, "text": "Нет такого инструмента."}))
    if not pdftools.AVAILABLE[tool]:
        return render(request, "converter/page.html", _context(
            error={"tool": tool, "text": f"Инструмент выключен: на сервере нет пакета {pdftools.PACKAGE[tool]}."}))

    p = request.POST
    try:
        files = _pdfs(request)
        name, data = files[0]
        stem = Path(name).stem

        if tool == "merge":
            return _download(pdftools.merge(files), "объединённый.pdf", PDF)
        if tool == "pages":
            result = pdftools.pages(data, p.get("keep", ""), p.get("delete", ""))
            return _download(result, f"{stem}_страницы.pdf", PDF)
        if tool == "split":
            every = int(p.get("every") or 1)
            return _download(pdftools.split(data, every, stem), f"{stem}_части.zip", "application/zip")
        if tool == "rotate":
            result = pdftools.rotate(data, p.get("pages", ""), int(p.get("angle") or 90))
            return _download(result, f"{stem}_повёрнут.pdf", PDF)
        if tool == "word":
            result = pdftools.to_word(data, p.get("pages", ""))
            return _download(result, f"{stem}.docx",
                             "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        if tool == "excel":
            result = pdftools.to_excel(data, p.get("pages", ""), one_sheet=p.get("one_sheet") == "1")
            return _download(result, f"{stem}.xlsx",
                             "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    except ToolError as e:
        message = str(e)
    except ValueError:
        message = "Проверьте числа в форме."
    except Exception as e:                      # a broken PDF can fail deep inside a library
        message = f"Не получилось обработать файл ({type(e).__name__}). Попробуйте другой файл."
    return render(request, "converter/page.html", _context(error={"tool": tool, "text": message}))
