from django.db import models
from django.db.models import Q
from masters.models import Master
from panda.models import Panda
from homework.models import PandaGroup


class Classroom(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='classrooms')
    name = models.CharField(max_length=200)
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


class Lesson(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    practices = models.ManyToManyField('practice.Practice', blank=True, related_name='lessons')
    homeworks = models.ManyToManyField('homework.Homework', blank=True, related_name='lessons')
    tutorials = models.ManyToManyField('tutorial.Tutorial', blank=True, related_name='lessons')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'created_at']

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
