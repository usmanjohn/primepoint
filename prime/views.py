from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q, Avg, Max, Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin

from prime.subjects import (
    SUBJECT_MAP, SUBJECT_SLUGS, SESSION_KEY,
    get_study_subjects, has_chosen_subjects,
)
from prime.partners import PARTNERS
from prime.social import SOCIAL_MAP, CONTACT_EMAIL
from prime.search import search_platform
from prime.progress import student_progress, master_progress
from prime import kit

from masters.models import Master
from practice.models import Practice, PracticeAttempt, PracticeQuestion
from discussion.models import Thread
from tutorial.models import Tutorial, TutorialPlaylist
from panda.models import Panda
from homework.models import Homework, HomeworkAssignment
from classroom.models import Classroom
from exam.models import Exam
from examprep.models import Lesson, ExamTrack
from corner.models import Story
from logic.models import LogicPuzzle
from games.views import GAME_COUNT


def service_worker(request):
    sw_path = settings.BASE_DIR / 'static' / 'sw.js'
    return HttpResponse(sw_path.read_text(), content_type='application/javascript; charset=utf-8')


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Disallow: /admin/',
        'Disallow: /people/',
        'Disallow: /analytics/',
        'Disallow: /i18n/',
        'Disallow: /study-subjects/',
        'Allow: /',
        '',
        f'Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines) + '\n', content_type='text/plain')


def index(request):
    stats = cache.get('index_stats_v4')
    if stats is None:
        stats = {
            'masters': Master.objects.count(),
            'practices': Practice.objects.filter(is_published=True).count(),
            'students': Panda.objects.count(),
            'threads': Thread.objects.count(),
            'tutorials': Tutorial.objects.filter(is_published=True).count(),
            'homework': Homework.objects.count(),
            'classrooms': Classroom.objects.filter(is_active=True).count(),
            'exams': Exam.objects.filter(is_published=True).count(),
            'examprep_lessons': Lesson.objects.filter(is_published=True, track__is_published=True).count(),
            'games': GAME_COUNT,
            'logic_puzzles': LogicPuzzle.objects.filter(
                is_published=True, opens_at__lte=timezone.now()).count(),
            'corner_stories': Story.objects.filter(
                is_published=True,
                collection__is_published=True,
                collection__subject__is_published=True,
            ).count(),
        }
        stats['resources'] = (
            stats['practices'] + stats['tutorials'] + stats['exams']
            + stats['examprep_lessons'] + stats['corner_stories']
        )
        cache.set('index_stats_v4', stats, 300)

    my_stats = None
    if request.user.is_authenticated:
        # Single query: fetch user + profile + panda + master relations
        user = (
            User.objects
            .select_related('profile__panda', 'profile__master')
            .get(pk=request.user.pk)
        )
        profile = user.profile
        panda = getattr(profile, 'panda', None)

        if panda:
            # One query for all practice stats
            agg = PracticeAttempt.objects.filter(
                panda=panda, status='completed'
            ).aggregate(
                total=Count('id'),
                avg=Avg('score'),
                best=Max('score'),
                pass_count=Count('id', filter=Q(score__gte=50)),
            )
            total_attempts = agg['total'] or 0
            # One query for all homework stats
            hw = HomeworkAssignment.objects.filter(panda=panda).aggregate(
                total=Count('id'),
                done=Count('id', filter=Q(status__in=['submitted', 'graded'])),
            )
            my_stats = {
                'type': 'student',
                'panda': panda,
                'total_attempts': total_attempts,
                'avg_score': round(agg['avg'] or 0, 1),
                'best_score': round(float(agg['best'] or 0), 1),
                'pass_rate': round(((agg['pass_count'] or 0) / max(total_attempts, 1)) * 100, 1),
                'hw_total': hw['total'] or 0,
                'hw_done': hw['done'] or 0,
            }
        else:
            master = getattr(profile, 'master', None)
            if master:
                my_stats = {
                    'type': 'master',
                    'master': master,
                    'student_count': master.pandas.count(),
                    'practice_count': master.practices.filter(is_published=True).count(),
                    'avg_rating': float(master.avg_rating),
                    'review_count': master.review_count,
                    'contribution_score': master.contribution_score,
                }

    slugs = get_study_subjects(request)
    show_picker = not has_chosen_subjects(request) or request.GET.get('choose')
    study_apps = None
    if slugs:
        study_apps = {
            'practice': any(SUBJECT_MAP[s]['practice_names'] for s in slugs),
            'tutorial': any(SUBJECT_MAP[s]['tutorial_categories'] for s in slugs),
            'examprep': any(SUBJECT_MAP[s]['examprep_tracks'] for s in slugs),
            'corner': any(SUBJECT_MAP[s]['corner_subjects'] for s in slugs),
            'exam': any(SUBJECT_MAP[s]['exam_languages'] for s in slugs),
        }

    return render(request, 'prime/index.html', {
        'stats': stats,
        'my_stats': my_stats,
        'show_picker': show_picker,
        'study_apps': study_apps,
    })


def set_study_subjects(request):
    if request.method != 'POST':
        return redirect('index')
    if request.POST.get('everything'):
        raw = 'all'
    else:
        picked = [s for s in request.POST.getlist('subjects') if s in SUBJECT_SLUGS]
        raw = ','.join(picked) if picked and len(picked) < len(SUBJECT_SLUGS) else 'all'
    if request.user.is_authenticated:
        profile = request.user.profile
        profile.study_subjects = raw
        profile.save(update_fields=['study_subjects'])
    else:
        request.session[SESSION_KEY] = raw
    messages.success(request, _('Your study subjects have been saved.'))
    return redirect('profile' if request.POST.get('next') == 'profile' else 'index')


def _platform_stats():
    """Live counts of what is actually built, cached for five minutes.

    Shared by the About page and the printed hand-out kit, so a flyer and the
    page it links to can never disagree about how many lessons exist. Nobody
    adds a thousand lessons between two page loads, hence the cache.
    """
    stats = cache.get('about_stats_v2')
    if stats is None:
        tutorials = Tutorial.objects.filter(is_published=True).count()
        examprep = Lesson.objects.filter(
            is_published=True, track__is_published=True).count()
        stats = {
            'lessons': tutorials + examprep,
            'questions': PracticeQuestion.objects.filter(
                practice__is_published=True).count(),
            'practices': Practice.objects.filter(is_published=True).count(),
            'readings': Story.objects.filter(
                is_published=True,
                collection__is_published=True,
                collection__subject__is_published=True,
            ).count(),
            'courses': TutorialPlaylist.objects.count(),
            'tracks': ExamTrack.objects.filter(is_published=True).count(),
            'games': GAME_COUNT,
        }
        # Thousands separator here rather than in the template: `humanize`
        # is not installed and a five-figure question count wants the comma.
        stats['questions_display'] = f"{stats['questions']:,}"
        # The flyer prints this one large; "11,839" is a truer promise than a
        # rounded "12,000", but the trailing digits are noise on paper, so the
        # printed pieces show the floor of the thousand with a +. Below a
        # thousand that would read "0,000+", so the exact count stands instead.
        q = stats['questions']
        stats['questions_round'] = f"{q // 1000:,},000+" if q >= 1000 else f"{q:,}"
        cache.set('about_stats_v2', stats, 300)
    return stats


def about(request):
    """Who we are — and, in real numbers, what is already built.

    The stat bar used to read "∞ / 100% / 1 / ∀". This page is shown to
    partners, so it counts the library instead.
    """
    return render(request, 'prime/about.html', {
        'stats': _platform_stats(),
        'partners': PARTNERS,
        'qr_site': kit.QR_SITE,
    })


def help_page(request):
    return render(request, 'prime/help.html')


def search(request):
    query = request.GET.get('q', '').strip()
    groups, total = search_platform(query)
    return render(request, 'prime/search_results.html', {
        'query': query,
        'groups': groups,
        'total': total,
    })


@login_required
def progress(request):
    """How far this person has got, and what it earned them.

    Learners see their own coverage of every library; masters additionally see
    the same summary for each of their students. Someone who is both gets both
    sections, which is why neither is an early return.
    """
    profile = request.user.profile
    master = getattr(profile, 'master', None)
    panda = getattr(profile, 'panda', None)

    return render(request, 'prime/progress.html', {
        'summary': student_progress(request.user) if panda else None,
        'master': master,
        'students': master_progress(master) if master else None,
    })


# ══════════════════════════════════════════════════════════════════════
#  THE HAND-OUT KIT — the printable business card and flyer
#
#  Three public pages a teacher opens, hits Ctrl+P on, and walks into an
#  educational centre with. Public on purpose: the point of the pieces is
#  that anyone who likes the platform can print their own stack, which a
#  staff gate would defeat. (The staff gate on `prime/printing.py` guards
#  *lesson content* walking off the site — this is marketing, we want it
#  walking off the site.)
#
#  The numbers on them are `_platform_stats()`, the same live counts the
#  About page shows; the words are `prime/kit.py`. Each view is
#  `xframe_options_sameorigin` because the About page embeds it as a live
#  preview and the project's default is DENY — same origin only, so nobody
#  else's site can frame us. Language is chosen with
#  ?lang= and is deliberately independent of the visitor's own EN/UZ
#  switch — a master reading the site in English still prints the Uzbek
#  card, because the card is for the centre director, not for them.
# ══════════════════════════════════════════════════════════════════════

def _kit_context(request, piece):
    """Everything every piece of the kit needs: copy, counts, links, QR paths.

    `?bare=1` drops the toolbar and the grey stage so the page can be embedded
    as a live preview — that is how the About page shows these pieces without
    keeping a screenshot that goes stale the moment a lesson is added.
    """
    lang = kit.pick_lang(request.GET.get('lang'))
    c = kit.copy_for(lang)
    return {
        'bare': request.GET.get('bare') == '1',
        'c': c,
        'lang': lang,
        'piece': piece,
        'stats': _platform_stats(),
        'partners': PARTNERS,
        'social': SOCIAL_MAP,
        'contact_email': CONTACT_EMAIL,
        'kit': kit,
        'other_lang': c['other_lang'],
    }


@xframe_options_sameorigin
def kit_card(request):
    """The business card — 90 × 50 mm, front and back, one pair per page."""
    return render(request, 'kit/card.html', _kit_context(request, 'card'))


@xframe_options_sameorigin
def kit_card_sheet(request):
    """Ten cards on one A4 sheet, with cut guides — what you actually print.

    `?side=back` prints the backs. The two sheets need no mirroring: all ten
    cards on a sheet are the same card, so whichever way the paper is flipped,
    every back lands behind a front.
    """
    ctx = _kit_context(request, 'sheet')
    ctx['side'] = 'back' if request.GET.get('side') == 'back' else 'front'
    ctx['cards'] = range(10)     # 2 columns x 5 rows of 90 x 50 mm on A4
    return render(request, 'kit/card_sheet.html', ctx)


@xframe_options_sameorigin
def kit_flyer(request):
    """The A4 flyer for educational centres — two sides, one page each."""
    return render(request, 'kit/flyer.html', _kit_context(request, 'flyer'))
