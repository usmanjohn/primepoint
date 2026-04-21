from django.db import models
from masters.models import Master
from people.models import People
class Panda(models.Model):
    PURPOSE_CHOICES = [('learning', 'Learning'), ('entertainment', 'Entertainment'), ('other', 'Other')]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    master = models.ForeignKey(Master,null = True, blank = True, on_delete=models.CASCADE, related_name='panda')
    profile = models.ForeignKey(People, on_delete=models.CASCADE, related_name='panda')
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='learning')
    rating = models.IntegerField(default=0) 


    def __str__(self):
        return self.name