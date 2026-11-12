"""
The map page. All the drawing is in geo.py; the view only hands it to the template.
The map is built once per gunicorn worker (lru_cache): it is ~100 KB, nothing to worry about.
"""
from functools import lru_cache

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from . import geo


@lru_cache(maxsize=1)
def the_map():
    return geo.build_map()


@login_required
def page(request):
    return render(request, "branchmap/page.html", {"m": the_map()})
