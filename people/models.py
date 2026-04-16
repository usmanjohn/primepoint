from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='people')
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null = True, blank = True)
    biography = models.TextField(blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    link = models.URLField(blank=True)
    

    def __str__(self):
        return f"{self.user.username}"