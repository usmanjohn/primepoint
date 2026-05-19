from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Q
from .models import Panda


@login_required
def panda_home(request):
    panders = list(
        Panda.objects
        .select_related('profile__user')
        .prefetch_related('masters')
        .annotate(
            attempt_count=Count('attempts', filter=Q(attempts__status='completed'), distinct=True),
            masters_count=Count('masters', distinct=True),
            avg_score=Avg('attempts__score', filter=Q(attempts__status='completed')),
        )
        .order_by('-rating', '-attempt_count')
    )
    # Attach rank position
    for i, p in enumerate(panders, 1):
        p.rank_position = i
    return render(request, 'panda/panda_list.html', {'panders': panders})
