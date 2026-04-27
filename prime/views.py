from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q

from masters.models import Master
from practice.models import Practice
from discussion.models import Thread


def service_worker(request):
    sw_path = settings.BASE_DIR / 'static' / 'sw.js'
    return HttpResponse(sw_path.read_text(), content_type='application/javascript; charset=utf-8')


def index(request):
    return render(request, 'prime/index.html')

def about(request):
    return render(request, 'prime/about.html')

def search(request):
    query = request.GET.get('q', '').strip()
    masters = Practice.objects.none()
    practices = Practice.objects.none()
    threads = Thread.objects.none()

    if query:
        masters = Master.objects.filter(
            Q(name__icontains=query) |
            Q(subject__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )
        practices = Practice.objects.filter(is_published=True).filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        threads = Thread.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        )

    total = masters.count() + practices.count() + threads.count()
    return render(request, 'prime/search_results.html', {
        'query': query,
        'masters': masters,
        'practices': practices,
        'threads': threads,
        'total': total,
    })
