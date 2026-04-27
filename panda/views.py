from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Panda


@login_required
def panda_home(request):
    panders = (
        Panda.objects
        .select_related('profile__user')
        .prefetch_related('masters')
        .annotate(
            attempt_count=Count('attempts', distinct=True),
            masters_count=Count('masters', distinct=True),
        )
    )
    return render(request, 'panda/panda_list.html', {'panders': panders})
