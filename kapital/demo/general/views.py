from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'general/home.html')


def internal_only(request, username=None):
    """DEMO: a page that works only inside the bank (it needs the bank's database)."""
    return render(request, 'general/internal_only.html')
