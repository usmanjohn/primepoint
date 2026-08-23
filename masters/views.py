from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Count, Avg, Q
from django.utils import timezone

from .models import (Master, StudentEnrollment, Certificate, MasterReview,
                     MAX_STARS)
from .forms import (MasterForm, MasterReviewForm, MasterSubjectFormSet,
                    MasterCredentialFormSet)
from .rating import contribution_summary

# How many practices / tutorials the profile shows before linking out. Some
# masters here have authored well over a thousand items.
SHOWCASE_LIMIT = 12
from practice.models import PracticeAttempt
from tutorial.models import Tutorial
from games.models import JourneyPrize
from django.utils.translation import gettext as _


def master_list(request):
    """The masters wall, ordered the way we want people to meet them.

    Powerty's own education staff first (that badge is the whole point of
    `is_powerty`), then how their own pupils rate them, then how much they have
    built for the platform. Independent masters can and do reach the top of the
    second group — the badge only separates the two blocks.
    """
    masters = (Master.objects.select_related('profile__user')
               .prefetch_related('subjects')
               .annotate(student_count_live=Count('pandas', distinct=True)))

    query = request.GET.get('q', '').strip()
    if query:
        masters = masters.filter(
            Q(name__icontains=query) | Q(subject__icontains=query)
            | Q(subjects__name__icontains=query) | Q(headline__icontains=query)
        ).distinct()

    team = request.GET.get('team', '')
    if team == 'powerty':
        masters = masters.filter(is_powerty=True)
    elif team == 'independent':
        masters = masters.filter(is_powerty=False)

    # Ordered explicitly, not by Meta: Django drops a model's default ordering
    # on aggregate queries, and this one annotates a Count.
    sort = request.GET.get('sort', '')
    if sort == 'contribution':
        masters = masters.order_by('-is_powerty', '-contribution_score', '-weighted_rating')
    elif sort == 'students':
        masters = masters.order_by('-is_powerty', '-student_count_live', '-weighted_rating')
    elif sort == 'new':
        masters = masters.order_by('-created_at')
    else:
        masters = masters.order_by(
            '-is_powerty', '-weighted_rating', '-contribution_score', 'name')

    return render(request, 'masters/master_list.html', {
        'masters': masters,
        'query': query,
        'team': team,
        'sort': sort,
        'powerty_count': Master.objects.filter(is_powerty=True).count(),
        'max_stars': MAX_STARS,
    })


def master_detail(request, master_id):
    master = get_object_or_404(
        Master.objects.select_related('profile__user')
                      .prefetch_related('subjects', 'credentials'),
        id=master_id)
    is_owner = (request.user.is_authenticated and request.user == master.profile.user)

    practice_qs = master.practices if is_owner else master.practices.filter(is_published=True)
    practice_qs = practice_qs.annotate(
        question_count=Count('questions', distinct=True),
        attempt_count=Count('attempts', distinct=True),
        avg_score=Avg('attempts__score'),
    )
    # A master who wrote a thousand lessons would otherwise render a
    # half-megabyte page; the totals below still count all of them.
    practice_total = practice_qs.count()
    practices = list(practice_qs[:SHOWCASE_LIMIT])

    attempts_qs = PracticeAttempt.objects.filter(practice__master=master)
    avg_student_score = attempts_qs.aggregate(avg=Avg('score'))['avg'] or 0
    total_attempts = attempts_qs.count()
    total_questions = (practice_qs.aggregate(n=Count('questions'))['n'] or 0)

    student_count = master.pandas.count()
    students = master.pandas.select_related('profile__user').order_by('-rating')

    # Groups and homework are managed inside a classroom now, so the profile
    # shows the rooms themselves rather than two flat lists that spanned them.
    classrooms = []
    if is_owner:
        classrooms = (
            master.classrooms
            .prefetch_related('homeworks')
            .order_by('-created_at')
        )

    tutorial_qs = (
        Tutorial.objects
        .filter(author=master.profile.user, is_published=True)
        .order_by('-created_at')
    )
    tutorial_total = tutorial_qs.count()
    tutorials = list(tutorial_qs[:SHOWCASE_LIMIT])

    # ── Reviews ────────────────────────────────────────────────────────────
    # Only this master's own pupils may rate them, and only once; everyone
    # else — including guests — reads.
    reviews = (master.reviews.filter(is_visible=True)
               .select_related('panda__profile__user'))
    my_panda = None
    if request.user.is_authenticated:
        my_panda = getattr(getattr(request.user, 'profile', None), 'panda', None)
    is_student = bool(my_panda and master.pandas.filter(pk=my_panda.pk).exists())
    my_review = master.reviews.filter(panda=my_panda).first() if my_panda else None
    review_form = MasterReviewForm(instance=my_review) if is_student else None

    # Ten bars, tallest first: how the stars are spread.
    histogram = []
    if master.review_count:
        counts = {r['stars']: r['n'] for r in
                  reviews.values('stars').annotate(n=Count('id'))}
        for star in range(MAX_STARS, 0, -1):
            n = counts.get(star, 0)
            histogram.append({'stars': star, 'count': n,
                              'percent': round(n * 100 / master.review_count)})

    return render(request, 'masters/master_detail.html', {
        'master': master,
        'is_owner': is_owner,
        'practices': practices,
        'practice_total': practice_total,
        'tutorial_total': tutorial_total,
        'showcase_limit': SHOWCASE_LIMIT,
        'avg_student_score': avg_student_score,
        'total_attempts': total_attempts,
        'total_questions': total_questions,
        'student_count': student_count,
        'students': students,
        'classrooms': classrooms,
        'tutorials': tutorials,
        'contribution': contribution_summary(master),
        'reviews': reviews,
        'review_form': review_form,
        'my_review': my_review,
        'is_student': is_student,
        'histogram': histogram,
        'max_stars': MAX_STARS,
        # Highest first: the CSS star picker relies on the DOM order being
        # 10 → 1 so `input:checked ~ label` can light every star below it.
        'star_values': list(range(MAX_STARS, 0, -1)),
    })


@login_required
def master_review(request, master_id):
    """Write or rewrite your rating of your own master."""
    master = get_object_or_404(Master, id=master_id)
    panda = getattr(getattr(request.user, 'profile', None), 'panda', None)

    if not panda or not master.pandas.filter(pk=panda.pk).exists():
        messages.error(request, _('Only %(name)s\'s own students can leave a rating.')
                       % {'name': master.name})
        return redirect('masters-detail', master_id=master.pk)

    existing = MasterReview.objects.filter(master=master, panda=panda).first()
    if request.method == 'POST':
        form = MasterReviewForm(request.POST, instance=existing)
        if form.is_valid():
            review = form.save(commit=False)
            review.master = master
            review.panda = panda
            review.save()
            master.recalc_stats()
            messages.success(request, _('Thank you — your rating has been saved.'))
        else:
            messages.error(request, _('Please choose a rating between 1 and %(max)s.')
                           % {'max': MAX_STARS})
    return redirect('masters-detail', master_id=master.pk)


@login_required
def master_review_delete(request, master_id):
    """Withdraw your own rating. Staff may also remove one that is abusive."""
    master = get_object_or_404(Master, id=master_id)
    review_pk = request.POST.get('review')
    review = get_object_or_404(MasterReview, pk=review_pk, master=master)

    panda = getattr(getattr(request.user, 'profile', None), 'panda', None)
    if not request.user.is_staff and review.panda != panda:
        raise PermissionDenied

    if request.method == 'POST':
        review.delete()
        master.recalc_stats()
        messages.success(request, _('Rating removed.'))
    return redirect('masters-detail', master_id=master.pk)


@login_required
def master_create(request):
    if hasattr(request.user.profile, 'master'):
        messages.info(request, "You already have a Master profile.")
        return redirect('masters-home')

    if request.method == 'POST':
        form = MasterForm(request.POST, request.FILES)
        if form.is_valid():
            master = form.save(commit=False)
            master.profile = request.user.profile
            master.save()
            messages.success(request, _("Your Master application has been submitted. "
                                        "You'll gain full access once an admin approves it."))
            return redirect('masters-detail', master_id=master.pk)
    else:
        form = MasterForm()
    return render(request, 'masters/master_form.html', {'form': form})


@login_required
def master_update(request, pk):
    """Edit the profile, its subject list and its credentials in one form.

    The two formsets render a couple of blank rows each instead of an
    "add another" button, so the whole page stays script-free.
    """
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MasterForm(request.POST, request.FILES, instance=master)
        subjects = MasterSubjectFormSet(request.POST, instance=master, prefix='subjects')
        credentials = MasterCredentialFormSet(request.POST, request.FILES,
                                              instance=master, prefix='credentials')
        if form.is_valid() and subjects.is_valid() and credentials.is_valid():
            form.save()
            subjects.save()
            credentials.save()
            messages.success(request, _('Profile updated.'))
            return redirect('masters-detail', master_id=master.pk)
    else:
        form = MasterForm(instance=master)
        subjects = MasterSubjectFormSet(instance=master, prefix='subjects')
        credentials = MasterCredentialFormSet(instance=master, prefix='credentials')

    return render(request, 'masters/master_form.html', {
        'form': form, 'master': master,
        'subject_formset': subjects, 'credential_formset': credentials,
    })


@login_required
def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        master.delete()
        messages.success(request, "Master profile deleted.")
        return redirect('masters-home')
    return render(request, 'masters/master_confirm_delete.html', {'master': master})


@login_required
def master_remove_student(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied
    from panda.models import Panda
    panda = get_object_or_404(Panda, pk=panda_pk)
    if request.method == 'POST':
        master.pandas.remove(panda)
        StudentEnrollment.objects.filter(master=master, panda=panda).delete()
        # Only current students hold a rating on this master.
        MasterReview.objects.filter(master=master, panda=panda).delete()
        master.recalc_stats()
        messages.success(request, f'Removed {panda.profile.user.username} from your students.')
    return redirect('classroom:list')


@login_required
def certificate_generator(request):
    is_master = hasattr(request.user, 'profile') and hasattr(request.user.profile, 'master')
    if not request.user.is_staff and not (is_master and request.user.profile.master.is_approved):
        raise PermissionDenied

    master = None
    students = []
    if is_master:
        master = request.user.profile.master
        students = (
            master.pandas
            .select_related('profile__user')
            .order_by('profile__user__first_name', 'profile__user__username')
        )

    return render(request, 'masters/certificate.html', {
        'master':   master,
        'students': students,
        'today':    timezone.now().date(),
    })


# ── Student management moved into the classroom (August 2026) ─────────────
# A master running two classes used to see one undifferentiated pile of pupils
# here, with no way to tell whose homework, whose register or whose fee was
# whose. All of it now lives inside the classroom that owns it. These views
# stay as redirects because the URLs are bookmarked and linked from older
# pages; each one lands the master on the room, or on the room list when
# there is more than one to choose from.

def _to_classroom(request, master, view_name='classroom:students', **kwargs):
    if request.user != master.profile.user:
        raise PermissionDenied
    rooms = list(master.classrooms.order_by('-created_at')[:2])
    if len(rooms) == 1:
        messages.info(request, _('Students, attendance and payments live '
                                 'inside the classroom now.'))
        return redirect(view_name, classroom_pk=rooms[0].pk, **kwargs)
    if not rooms:
        messages.info(request, _('Create a classroom first — students, '
                                 'attendance and payments all live inside it now.'))
        return redirect('classroom:create')
    messages.info(request, _('Pick the classroom you mean — students, '
                             'attendance and payments live inside it now.'))
    return redirect('classroom:list')


@login_required
def my_students(request, pk):
    return _to_classroom(request, get_object_or_404(Master, pk=pk))


@login_required
def student_detail(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    return _to_classroom(request, master, 'classroom:student_detail', panda_pk=panda_pk)


@login_required
def add_student(request, pk):
    return _to_classroom(request, get_object_or_404(Master, pk=pk))


@login_required
def mark_attendance(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    return _to_classroom(request, master, 'classroom:student_detail', panda_pk=panda_pk)


@login_required
def add_payment(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    return _to_classroom(request, master, 'classroom:student_detail', panda_pk=panda_pk)


@login_required
def delete_payment(request, pk, payment_pk):
    master = get_object_or_404(Master, pk=pk)
    return _to_classroom(request, master, 'classroom:payments')


@login_required
def issue_certificate(request, pk, panda_pk):
    master = get_object_or_404(Master, pk=pk)
    return _to_classroom(request, master, 'classroom:student_detail', panda_pk=panda_pk)


@login_required
def delete_certificate(request, pk, cert_pk):
    master = get_object_or_404(Master, pk=pk)
    return _to_classroom(request, master)


@login_required
def certificate_view(request, cert_pk):
    cert = get_object_or_404(Certificate, pk=cert_pk)
    is_owner = (request.user == cert.panda.profile.user)
    is_master = (request.user == cert.master.profile.user)
    if not is_owner and not is_master and not request.user.is_staff:
        raise PermissionDenied
    return render(request, 'masters/certificate_view.html', {
        'cert': cert,
        'today': cert.issued_at.date(),
    })


@login_required
def journey_prizes(request, pk):
    """Prizes the master's pupils have won in Prime Journey, waiting to be
    handed over in real life.

    This is the page that turns a browser game into something that happens in
    a classroom: a chest on the road gives a pupil a token, and this list is
    where the teacher sees whose pen or notebook is still owed.
    """
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    pupil_users = list(master.pandas.select_related('profile__user')
                       .values_list('profile__user_id', flat=True))

    if request.method == 'POST':
        prize = JourneyPrize.objects.filter(
            pk=request.POST.get('prize'), user_id__in=pupil_users).first()
        if prize and not prize.handed_over:
            prize.handed_over = True
            prize.handed_at = timezone.now()
            prize.handed_by = request.user
            prize.save(update_fields=['handed_over', 'handed_at', 'handed_by'])
            messages.success(request, _('Marked as handed over: %(prize)s → %(who)s')
                             % {'prize': prize.reward.name,
                                'who': prize.user.username})
        return redirect('masters-journey-prizes', pk=master.pk)

    prizes = (JourneyPrize.objects
              .filter(user_id__in=pupil_users)
              .select_related('reward', 'user', 'run')
              .order_by('handed_over', '-won_at'))

    return render(request, 'masters/journey_prizes.html', {
        'master':  master,
        'pending': [p for p in prizes if not p.handed_over],
        'done':    [p for p in prizes if p.handed_over][:30],
    })
