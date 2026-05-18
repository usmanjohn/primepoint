from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    TYPE_HOMEWORK   = 'homework'
    TYPE_PRACTICE   = 'practice'
    TYPE_TUTORIAL   = 'tutorial'
    TYPE_LESSON     = 'lesson'
    TYPE_CLASSROOM  = 'classroom'
    TYPE_DISCUSSION = 'discussion'

    TYPES = [
        (TYPE_HOMEWORK,   _('Homework')),
        (TYPE_PRACTICE,   _('Practice')),
        (TYPE_TUTORIAL,   _('Tutorial')),
        (TYPE_LESSON,     _('Lesson')),
        (TYPE_CLASSROOM,  _('Classroom')),
        (TYPE_DISCUSSION, _('Discussion')),
    ]

    ICONS = {
        TYPE_HOMEWORK:   'bi-journal-bookmark-fill',
        TYPE_PRACTICE:   'bi-clipboard-check-fill',
        TYPE_TUTORIAL:   'bi-book-fill',
        TYPE_LESSON:     'bi-mortarboard-fill',
        TYPE_CLASSROOM:  'bi-easel-fill',
        TYPE_DISCUSSION: 'bi-chat-dots-fill',
    }

    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notif_type = models.CharField(max_length=20, choices=TYPES, default=TYPE_HOMEWORK)
    title      = models.CharField(max_length=255)
    message    = models.TextField(blank=True)
    url        = models.CharField(max_length=500, blank=True)
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user} — {self.title}'

    @property
    def icon(self):
        return self.ICONS.get(self.notif_type, 'bi-bell-fill')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null = True, blank = True)
    biography = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    
    is_admin = models.BooleanField(default=False)
    is_director = models.BooleanField(default=False)
    is_cofounder = models.BooleanField(default=False)
    is_master = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_assistant = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"
    
    _DEFAULT_AVATARS = [
        'father.png', 'monkey.png', 'ogway.png', 'panda.png',
        'shifu.png', 'taylung.png', 'tiger.png', 'turna.png',
    ]

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        avatar = self._DEFAULT_AVATARS[self.user.pk % len(self._DEFAULT_AVATARS)]
        return f'/static/images/users/{avatar}'