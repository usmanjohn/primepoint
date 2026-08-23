"""Masters: who teaches on the platform, and what they are worth.

A Master profile is the public face of a teacher. Three things it has to get
right, and each is a small subsystem below:

1. **What they teach.** Some masters teach one subject, some teach four, so
   the subjects live in their own table (`MasterSubject`) rather than in one
   text field, and each carries the level it is taught at.
2. **Why they should be trusted.** `MasterCredential` holds diplomas,
   certificates, awards and past positions — with the scan attached when there
   is one — and `is_powerty` marks the ones who are our own education staff.
   That badge is set by an admin, never by the master.
3. **How good they are.** Two different numbers, deliberately kept apart:
   the *contribution score* (what they have built for the platform and how many
   pupils used it — see `masters.rating`) and the *student rating* (1-10 stars
   left by their own pupils in `MasterReview`, nobody else). The list page
   sorts by team first, then the blended student rating, then contribution.
"""
from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from people.models import Profile

# A rating out of ten built from three reviews is mostly noise. The blended
# rating pulls a thin review count towards the platform's expected average,
# so a master with one perfect score does not outrank one with forty at 9.4.
RATING_PRIOR_WEIGHT = 3          # how many "average" reviews every master starts with
RATING_PRIOR_VALUE = Decimal('8.0')
MAX_STARS = 10


class Master(models.Model):
    LESSON_ONLINE = 'online'
    LESSON_OFFLINE = 'offline'
    LESSON_HYBRID = 'hybrid'
    LESSON_FORMATS = [
        (LESSON_ONLINE, _('Online')),
        (LESSON_OFFLINE, _('In person')),
        (LESSON_HYBRID, _('Online and in person')),
    ]

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ── The badge only an admin can grant ──────────────────────────────────
    # Anyone approved may teach here; only our own education staff carry the
    # Powerty mark, and the list page puts them first. Never expose this on
    # `MasterForm` — it is set in the admin by the platform owner.
    is_powerty = models.BooleanField(
        default=False, verbose_name=_('Powerty team member'),
        help_text=_('Set by admins only: this master is part of the Powerty '
                    'education staff, not an independent teacher.'))
    powerty_role = models.CharField(
        max_length=100, blank=True, verbose_name=_('Role at Powerty'),
        help_text=_('e.g. "English Department", "Co-founder". Shown next to '
                    'the Powerty badge.'))

    # ── Presentation ───────────────────────────────────────────────────────
    headline = models.CharField(
        max_length=150, blank=True, verbose_name=_('Headline'),
        help_text=_('One line under your name, e.g. "SAT Math tutor, 8 years '
                    'in the classroom".'))
    photo = models.ImageField(
        upload_to='master_photos/', blank=True, null=True,
        verbose_name=_('Portrait'),
        help_text=_('A good, well-lit photo of you. Falls back to your '
                    'profile picture.'))
    about = models.TextField(
        blank=True, verbose_name=_('About myself'),
        help_text=_('Your story: how you started teaching, how you teach, '
                    'what your pupils achieve.'))
    teaching_since = models.PositiveSmallIntegerField(
        null=True, blank=True, verbose_name=_('Teaching since (year)'),
        help_text=_('The year you started teaching — anywhere, not just here.'))
    location = models.CharField(
        max_length=120, blank=True, verbose_name=_('Location'),
        help_text=_('e.g. "Tashkent, Chilonzor" or "Online only".'))
    languages = models.CharField(
        max_length=150, blank=True, verbose_name=_('Languages of instruction'),
        help_text=_('Comma-separated, e.g. "Uzbek, English, Russian".'))
    lesson_format = models.CharField(
        max_length=10, choices=LESSON_FORMATS, blank=True,
        verbose_name=_('Lesson format'))

    # ── How a pupil actually reaches them ──────────────────────────────────
    accepting_students = models.BooleanField(
        default=True, verbose_name=_('Accepting new students'))
    how_to_join = models.TextField(
        blank=True, verbose_name=_('How to become my student'),
        help_text=_('The real steps: trial lesson, level test, when groups '
                    'start, what it costs.'))
    telegram = models.CharField(
        max_length=100, blank=True, verbose_name=_('Telegram'),
        help_text=_('Username without the @, or a t.me link.'))
    phone = models.CharField(max_length=40, blank=True, verbose_name=_('Phone'))
    public_email = models.EmailField(blank=True, verbose_name=_('Public email'))
    website = models.URLField(blank=True, verbose_name=_('Website or channel'))

    # ── Cached numbers, all rebuilt by recalc_stats() ──────────────────────
    student_count = models.PositiveIntegerField(default=0)
    # Average of the 1-10 stars this master's own pupils have given. Kept
    # under the old name so every screen that already shows it keeps working.
    avg_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    review_count = models.PositiveIntegerField(default=0)
    # avg_rating pulled towards RATING_PRIOR_VALUE by the review count; this
    # is what the list page sorts on, so one lone 10/10 cannot top the page.
    weighted_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    contribution_score = models.PositiveIntegerField(default=0)
    content_count = models.PositiveIntegerField(
        default=0, help_text=_('Published items this master has authored.'))
    learner_count = models.PositiveIntegerField(
        default=0, help_text=_('Distinct pupils who have worked through this '
                               "master's content."))
    stats_updated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        # The default order of every master queryset: our own staff first,
        # then how their pupils rate them, then what they have built.
        ordering = ['-is_powerty', '-weighted_rating', '-contribution_score', 'name']

    def __str__(self):
        return self.name

    # ── Stats ──────────────────────────────────────────────────────────────
    def recalc_stats(self, save=True):
        """Rebuild every cached number on this profile.

        Called after a review is written, after a student is added or removed,
        and in bulk by `python manage.py recalc_master_stats`. Cheap enough to
        run inline (a handful of aggregate queries), and everything it writes
        is derived — losing the cache costs nothing but a recompute.
        """
        from masters.rating import contribution_summary

        self.student_count = self.pandas.count()

        reviews = self.reviews.filter(is_visible=True)
        agg = reviews.aggregate(avg=models.Avg('stars'), n=models.Count('id'))
        self.review_count = agg['n'] or 0
        self.avg_rating = Decimal(str(round(agg['avg'] or 0, 2)))
        n = self.review_count
        self.weighted_rating = (
            (self.avg_rating * n + RATING_PRIOR_VALUE * RATING_PRIOR_WEIGHT)
            / (n + RATING_PRIOR_WEIGHT)
        ).quantize(Decimal('0.01'))

        summary = contribution_summary(self)
        self.contribution_score = summary['score']
        self.content_count = summary['content_count']
        self.learner_count = summary['learner_count']

        self.stats_updated_at = timezone.now()
        if save:
            self.save(update_fields=[
                'student_count', 'avg_rating', 'review_count', 'weighted_rating',
                'contribution_score', 'content_count', 'learner_count',
                'stats_updated_at',
            ])
        return self

    # Kept because older call sites (add_student, remove_student) use it.
    def update_stats(self):
        return self.recalc_stats()

    # ── Display helpers ────────────────────────────────────────────────────
    @property
    def portrait_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        return self.profile.image_url

    @property
    def subject_names(self):
        """Every subject taught — the `MasterSubject` rows, falling back to
        the single legacy `subject` field for profiles never edited since."""
        names = [s.name for s in self.subjects.all()]
        if not names and self.subject:
            names = [self.subject]
        return names

    @property
    def language_list(self):
        return [x.strip() for x in self.languages.split(',') if x.strip()]

    @property
    def years_teaching(self):
        """Years in the classroom, as the master stated it — not time on the
        platform, which is `months_on_platform`."""
        if not self.teaching_since:
            return None
        return max(0, timezone.now().year - self.teaching_since)

    @property
    def months_on_platform(self):
        days = (timezone.now() - self.created_at).days
        return max(0, days // 30)

    @property
    def platform_tenure(self):
        """"2 yil 3 oy" as a (years, months) pair for the templates."""
        months = self.months_on_platform
        return months // 12, months % 12

    @property
    def star_percent(self):
        """Width of the filled half of a 10-star bar, for pure-CSS stars."""
        if not self.review_count:
            return 0
        return round(float(self.avg_rating) * 10)


class MasterSubject(models.Model):
    """One subject a master teaches. A master may have several; the first one
    is the headline subject on the list card."""
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=100, verbose_name=_('Subject'))
    level = models.CharField(
        max_length=100, blank=True, verbose_name=_('Levels'),
        help_text=_('e.g. "Beginner to IELTS 7.5", "5-9 sinf".'))
    note = models.CharField(
        max_length=200, blank=True, verbose_name=_('Note'),
        help_text=_('One line on how you teach this subject.'))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.name} ({self.master.name})'


class MasterCredential(models.Model):
    """A diploma, certificate, award or past position — the evidence behind
    the profile. `image` holds the scan when the master uploads one."""
    DIPLOMA = 'diploma'
    CERTIFICATE = 'certificate'
    AWARD = 'award'
    EXPERIENCE = 'experience'
    KIND_CHOICES = [
        (DIPLOMA, _('Diploma')),
        (CERTIFICATE, _('Certificate')),
        (AWARD, _('Award')),
        (EXPERIENCE, _('Experience')),
    ]
    ICONS = {
        DIPLOMA: 'bi-mortarboard-fill',
        CERTIFICATE: 'bi-patch-check-fill',
        AWARD: 'bi-trophy-fill',
        EXPERIENCE: 'bi-briefcase-fill',
    }

    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='credentials')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=DIPLOMA,
                            verbose_name=_('Type'))
    title = models.CharField(max_length=200, verbose_name=_('Title'),
                             help_text=_('e.g. "IELTS 8.0", "Bachelor in Linguistics".'))
    issuer = models.CharField(max_length=200, blank=True, verbose_name=_('Issued by'),
                              help_text=_('University, exam board or employer.'))
    year = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_('Year'))
    note = models.CharField(max_length=250, blank=True, verbose_name=_('Note'))
    image = models.ImageField(upload_to='master_credentials/', blank=True, null=True,
                              verbose_name=_('Scan or photo'))
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-year', 'id']

    def __str__(self):
        return f'{self.title} — {self.master.name}'

    @property
    def icon(self):
        return self.ICONS.get(self.kind, 'bi-patch-check-fill')


class MasterReview(models.Model):
    """A pupil rates their own master, 1-10, once.

    Only a panda currently enrolled with this master may write one (enforced in
    the view), because a review from someone who never sat in the class is not
    evidence. Editing your own review overwrites it rather than adding a second.
    """
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='reviews')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='master_reviews')
    stars = models.PositiveSmallIntegerField(
        default=MAX_STARS, verbose_name=_('Rating'),
        validators=[MinValueValidator(1), MaxValueValidator(MAX_STARS)])
    comment = models.TextField(blank=True, verbose_name=_('Review'))
    is_visible = models.BooleanField(
        default=True, help_text=_('Untick to hide an abusive review.'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['master', 'panda']
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.panda} → {self.master}: {self.stars}/{MAX_STARS}'

    @property
    def star_percent(self):
        return self.stars * 10


class StudentEnrollment(models.Model):
    """Tracks when a student joined a master's class."""
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='enrollments')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='enrollments')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['master', 'panda']
        ordering = ['-joined_at']

    def __str__(self):
        return f"{self.panda} → {self.master}"


class Attendance(models.Model):
    PRESENT = 'present'
    ABSENT = 'absent'
    LATE = 'late'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
        (LATE, 'Late'),
    ]
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='attendances')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='attendances')
    # Which room the pupil sat in. Nullable because every row written before
    # attendance moved into the classroom predates the question.
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PRESENT)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # One mark per pupil per room per day. The classroom is part of the key
        # because a master may teach the same pupil Korean at nine and maths at
        # four: without it, the second register of the day silently overwrites
        # the first. Rows written before classrooms existed carry classroom
        # NULL, and SQL treats NULLs as distinct, so those old rows are left
        # alone rather than colliding with each other.
        unique_together = ['master', 'panda', 'classroom', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.panda} — {self.date} ({self.status})"


class StudentPayment(models.Model):
    PAID = 'paid'
    UNPAID = 'unpaid'
    PARTIAL = 'partial'
    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (PARTIAL, 'Partial'),
    ]
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='payments')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='payments')
    # Which room the money is for: a master teaching the same pupil Korean and
    # maths needs to tell the two fees apart. Nullable for pre-classroom rows.
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=UNPAID)
    period_label = models.CharField(max_length=100, blank=True, help_text="e.g. June 2026")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.panda} — {self.period_label or self.created_at.date()} ({self.status})"


class Certificate(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='issued_certificates')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='certificates')
    classroom = models.ForeignKey('classroom.Classroom', on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='certificates')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-issued_at']

    def __str__(self):
        return f"{self.title} → {self.panda}"