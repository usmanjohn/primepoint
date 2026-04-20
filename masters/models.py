from django.db import models
from django.contrib.auth.models import User
from people.models import People
class Master(models.Model):
    profile = models.ForeignKey(People, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=100)
    certificates = models.FileField(upload_to='certificates/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    can_edit = models.BooleanField(default=False)

    def __str__(self):
        return self.name