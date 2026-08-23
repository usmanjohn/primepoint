import re
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from masters.models import Master
from panda.models import Panda
from homework.models import PandaGroup
from prime.subjects import SUBJECTS


# A classroom teaches one subject, even when its master teaches four. That is
# the whole point of asking: it is what lets the homework pickers show an
# English master English practices instead of the entire library.
SUBJECT_CHOICES = [(s['slug'], s['name']) for s in SUBJECTS]


class Classroom(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='classrooms')
    name = models.CharField(max_length=200)
    subject = models.CharField(
        max_length=30, choices=SUBJECT_CHOICES, blank=True,
        verbose_name=_('Subject'),
        help_text=_('What this classroom teaches. Narrows every homework '
                    'picker to that subject. Leave blank to see everything.'))
    description = models.TextField(blank=True)
    cover_color = models.CharField(max_length=20, default='#38bdf8')
    groups = models.ManyToManyField(PandaGroup, blank=True, related_name='classrooms')
    individual_pandas = models.ManyToManyField(Panda, blank=True, related_name='classrooms')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_all_pandas(self):
        group_panda_ids = Panda.objects.filter(groups__in=self.groups.all()).values_list('id', flat=True)
        individual_ids = self.individual_pandas.values_list('id', flat=True)
        return Panda.objects.filter(Q(id__in=group_panda_ids) | Q(id__in=individual_ids)).distinct()

    def is_member(self, user):
        if not user.is_authenticated:
            return False
        if user == self.master.profile.user:
            return True
        try:
            panda = user.profile.panda
            return self.get_all_pandas().filter(pk=panda.pk).exists()
        except Exception:
            return False

    @property
    def lesson_count(self):
        return self.lessons.count()

    @property
    def member_count(self):
        return self.get_all_pandas().count()

    def is_master_user(self, user):
        return user.is_authenticated and user == self.master.profile.user

    def panda_for(self, user):
        """The Panda this user attends as, or None (masters included)."""
        if not user.is_authenticated:
            return None
        try:
            panda = user.profile.panda
        except Exception:
            return None
        return panda if self.get_all_pandas().filter(pk=panda.pk).exists() else None


class Lesson(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Yet'),
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished'),
    ]

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    practices = models.ManyToManyField('practice.Practice', blank=True, related_name='lessons')
    homeworks = models.ManyToManyField('homework.Homework', blank=True, related_name='lessons')
    tutorials = models.ManyToManyField('tutorial.Tutorial', blank=True, related_name='lessons')
    youtube_url = models.URLField(blank=True, help_text='Optional YouTube video URL for this lesson.')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

    @property
    def youtube_embed_url(self):
        url = self.youtube_url.strip()
        if not url:
            return ''
        m = re.search(r'(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})', url)
        if m:
            return f'https://www.youtube.com/embed/{m.group(1)}'
        return url

    def __str__(self):
        return f"{self.classroom.name} – {self.title}"


class LessonNote(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='classroom/notes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['uploaded_at']

    def __str__(self):
        return self.title or self.file.name


class ClassroomDiscussion(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='discussions')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cr_discussions')
    title = models.CharField(max_length=300)
    body = models.TextField()
    is_pinned = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title

    @property
    def reply_count(self):
        return self.cr_replies.count()


class ClassroomReply(models.Model):
    discussion = models.ForeignKey(ClassroomDiscussion, on_delete=models.CASCADE, related_name='cr_replies')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='cr_replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Reply by {self.author} on '{self.discussion}'"


class ClassroomResource(models.Model):
    """A file or a link the whole classroom shares — a syllabus PDF, a
    recording, a Telegram group, a Google Doc.

    Lesson notes hang off one lesson; these hang off the room, which is where
    the things that outlive a single lesson belong. One model for both kinds
    because a master thinks "material", not "file vs URL": fill in whichever
    of `file`/`link` you have and the card renders the right button.
    """
    LINK = 'link'
    FILE = 'file'
    VIDEO = 'video'
    KIND_CHOICES = [
        (FILE, _('File')),
        (LINK, _('Link')),
        (VIDEO, _('Video')),
    ]
    ICONS = {FILE: 'bi-file-earmark-arrow-down', LINK: 'bi-link-45deg', VIDEO: 'bi-play-btn'}

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='resources')
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=LINK,
                            verbose_name=_('Type'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.CharField(max_length=300, blank=True, verbose_name=_('Note'))
    link = models.URLField(blank=True, verbose_name=_('Link'),
                           help_text=_('A YouTube video, a Google Doc, a Telegram group…'))
    file = models.FileField(upload_to='classroom/resources/', blank=True, null=True,
                            verbose_name=_('File'))
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    @property
    def icon(self):
        return self.ICONS.get(self.kind, 'bi-paperclip')

    @property
    def url(self):
        if self.file:
            return self.file.url
        return self.link

    @property
    def embed_url(self):
        """A YouTube link rendered inline, the same way a lesson video is."""
        if self.kind != self.VIDEO or not self.link:
            return ''
        m = re.search(r'(?:v=|youtu\.be/|embed/)([A-Za-z0-9_-]{11})', self.link)
        return f'https://www.youtube.com/embed/{m.group(1)}' if m else ''
