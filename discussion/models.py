from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=255, blank=True)
    icon = models.CharField(max_length=60, default='bi-chat-dots-fill')
    color = models.CharField(max_length=30, default='primary')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Thread(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='threads')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='threads')
    is_announcement = models.BooleanField(default=False)
    is_pinned = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-created_at']

    def __str__(self):
        return self.title

    @property
    def vote_score(self):
        return self.votes.aggregate(total=models.Sum('value'))['total'] or 0

    @property
    def reply_count(self):
        return self.replies.count()

    @property
    def has_accepted_answer(self):
        return self.replies.filter(is_accepted=True).exists()

    def user_vote(self, user):
        try:
            return self.votes.get(user=user).value
        except ThreadVote.DoesNotExist:
            return 0


class Reply(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='replies')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='replies')
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_accepted', 'created_at']

    def __str__(self):
        return f"Reply by {self.author} on '{self.thread}'"

    @property
    def vote_score(self):
        return self.votes.aggregate(total=models.Sum('value'))['total'] or 0

    def user_vote(self, user):
        try:
            return self.votes.get(user=user).value
        except ReplyVote.DoesNotExist:
            return 0


class ThreadVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=[(1, 'Up'), (-1, 'Down')])

    class Meta:
        unique_together = ('user', 'thread')


class ReplyVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='votes')
    value = models.SmallIntegerField(choices=[(1, 'Up'), (-1, 'Down')])

    class Meta:
        unique_together = ('user', 'reply')
