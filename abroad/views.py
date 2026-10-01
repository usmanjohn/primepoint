"""Study abroad views — function-based, server-rendered, no JavaScript.

The finder is a GET form, the checklist is a POST form, countdowns are
numbers computed here. Everything is readable by guests; only the personal
checklist needs an account.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import re
from urllib.parse import quote

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.translation import gettext as _

from .models import (
    today, ChecklistItem, ChecklistTick, Deadline, Guide, Sample, Scholarship, University,
)

# Checklist targets: code → (label, scholarship slug for the deadline, or None)
TARGETS = {
    'general': (_('Any university abroad'), None),
    'gks-u': (_('GKS — Bachelor (GKS-U)'), 'gks'),
    'gks-g': (_('GKS — Master (GKS-G)'), 'gks'),
    'mext-u': (_('MEXT — Bachelor'), 'mext'),
    'mext-r': (_('MEXT — Master / PhD'), 'mext'),
    'turkiye': (_('Türkiye Bursları'), 'turkiye'),
    'hungary': (_('Stipendium Hungaricum'), 'hungary'),
    'chevening': (_('Chevening'), 'chevening'),
    'csc': (_('CSC (China)'), 'csc'),
    'eyuf': (_('El-Yurt Umidi'), 'eyuf'),
    'daad': (_('DAAD (Germany)'), 'daad'),
    'fulbright': (_('Fulbright (USA)'), 'fulbright'),
    'erasmus': (_('Erasmus Mundus'), 'erasmus'),
}
# Which checklist a scholarship page's "turn this into a checklist" opens.
CHECKLIST_FOR = {'gks': 'gks-u', 'mext': 'mext-u', 'turkiye': 'turkiye', 'hungary': 'hungary',
                 'chevening': 'chevening', 'csc': 'csc',
                 'eyuf': 'eyuf', 'daad': 'daad', 'fulbright': 'fulbright', 'erasmus': 'erasmus'}

LEVELS = [('bachelor', _('Bachelor')), ('master', _('Master'))]
LANGS = [('english', _('English')), ('korean', _('Korean')),
         ('japanese', _('Japanese')), ('none', _('Not yet'))]


def _deadlines(qs=None):
    """Deadlines not yet closed, soonest first — stale ones included, because
    they must say "check the official site" rather than disappear."""
    d_today = today()
    qs = qs if qs is not None else Deadline.objects.all()
    return list(qs.select_related('scholarship')
                .filter(scholarship__is_published=True, closes__gte=d_today)
                .order_by('closes'))


def abroad_home(request):
    return render(request, 'abroad/home.html', {
        'deadlines': _deadlines()[:4],
        'guides': Guide.objects.filter(is_published=True),
        'scholarships': Scholarship.objects.filter(is_published=True),
        'samples': Sample.objects.filter(is_published=True),
        'university_count': University.objects.count(),
    })


def guide_detail(request, slug):
    guide = get_object_or_404(Guide, slug=slug, is_published=True)
    guides = list(Guide.objects.filter(is_published=True))
    i = next(n for n, g in enumerate(guides) if g.pk == guide.pk)
    return render(request, 'abroad/guide.html', {
        'guide': guide,
        'prev': guides[i - 1] if i > 0 else None,
        'next': guides[i + 1] if i + 1 < len(guides) else None,
        'guides': guides,
    })


def scholarship_list(request):
    """The finder: a plain GET form narrows the cards."""
    level = request.GET.get('level', '')
    lang = request.GET.get('lang', '')
    full = request.GET.get('full') == '1'
    items = list(Scholarship.objects.filter(is_published=True))
    if level:
        items = [s for s in items if level in s.level_list()]
    if lang and lang != 'none':
        items = [s for s in items if lang in s.language_list() or 'any' in s.language_list()]
    elif lang == 'none':
        # No language yet: programmes that teach you one (a language year) or accept any.
        items = [s for s in items if 'any' in s.language_list() or 'korean' in s.language_list()
                 or 'japanese' in s.language_list()]
    if full:
        items = [s for s in items if s.fully_funded]
    return render(request, 'abroad/scholarships.html', {
        'scholarships': items,
        'level': level, 'lang': lang, 'full': full,
        'levels': LEVELS, 'langs': LANGS,
        'filtered': bool(level or lang or full),
        'deadlines': {d.scholarship_id: d for d in reversed(_deadlines())},
    })


def scholarship_detail(request, slug):
    scholarship = get_object_or_404(Scholarship, slug=slug, is_published=True)
    return render(request, 'abroad/scholarship.html', {
        'scholarship': scholarship,
        'deadlines': _deadlines(scholarship.deadlines.all()),
        'past': scholarship.deadlines.filter(closes__lt=today()).order_by('-closes')[:3],
        'samples': scholarship.samples.filter(is_published=True),
        'universities': University.objects.filter(country=scholarship.country).exists(),
        'checklist_target': CHECKLIST_FOR.get(scholarship.slug, 'general'),
    })


def sample_detail(request, slug):
    sample = get_object_or_404(Sample, slug=slug, is_published=True)
    uz = (request.LANGUAGE_CODE or 'uz').startswith('uz')
    # The letter is authored as <p> paragraphs; each note names the paragraph
    # it explains, so the page can set them side by side (stacked on phones).
    paragraphs = re.findall(r'<p\b.*?</p>', sample.letter, re.S)
    rows = [{'html': p, 'notes': []} for p in paragraphs]
    for note in sample.notes:
        n = note.get('para', 0) - 1
        if 0 <= n < len(rows):
            rows[n]['notes'].append(note.get('uz' if uz else 'en') or note.get('en'))
    return render(request, 'abroad/sample.html', {
        'sample': sample,
        'rows': rows,
        'others': Sample.objects.filter(is_published=True).exclude(pk=sample.pk),
    })


def sample_planner(request, slug):
    """The printable planner — the page is the document (prime/printing.py)."""
    sample = get_object_or_404(Sample, slug=slug, is_published=True)
    uz = (request.LANGUAGE_CODE or 'uz').startswith('uz')
    prompts = [{'text': p.get('uz' if uz else 'en') or p.get('en'),
                'lines': range(p.get('lines', 4))} for p in sample.prompts]
    return render(request, 'abroad/planner.html', {'sample': sample, 'prompts': prompts})


def university_list(request):
    country = request.GET.get('country', '')
    unis = University.objects.all().order_by('country', 'order')
    # A set, not .distinct(): the default ordering would make each row distinct.
    countries = sorted(set(University.objects.values_list('country', flat=True)))
    if country in countries:
        unis = unis.filter(country=country)
    return render(request, 'abroad/universities.html', {
        'universities': unis, 'countries': countries, 'country': country,
    })


def checklist(request):
    target = request.GET.get('target') or request.POST.get('target') or 'gks-u'
    if target not in TARGETS:
        target = 'gks-u'
    items = list(ChecklistItem.objects.filter(target=target))

    if request.method == 'POST':
        if not request.user.is_authenticated:
            nxt = quote(f'{request.path}?target={target}')
            return redirect(f"{reverse('login')}?next={nxt}")
        wanted = {int(x) for x in request.POST.getlist('item') if x.isdigit()}
        ids = {i.pk for i in items}
        ChecklistTick.objects.filter(user=request.user, item_id__in=ids - wanted).delete()
        for pk in wanted & ids:
            ChecklistTick.objects.get_or_create(user=request.user, item_id=pk)
        messages.success(request, _('Checklist saved.'))
        return redirect(f"{request.path}?target={target}")

    ticked = set()
    if request.user.is_authenticated:
        ticked = set(ChecklistTick.objects.filter(user=request.user, item__target=target)
                     .values_list('item_id', flat=True))
    label, slug = TARGETS[target]
    deadline = None
    if slug:
        upcoming = _deadlines(Deadline.objects.filter(scholarship__slug=slug))
        deadline = upcoming[0] if upcoming else None
    done = sum(1 for i in items if i.pk in ticked)
    return render(request, 'abroad/checklist.html', {
        'target': target, 'targets': [(k, v[0]) for k, v in TARGETS.items()],
        'label': label, 'items': items, 'ticked': ticked,
        'done': done, 'percent': round(done * 100 / len(items)) if items else 0,
        'deadline': deadline,
    })
