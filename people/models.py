from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
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
    
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return "/static/images/logo.png"