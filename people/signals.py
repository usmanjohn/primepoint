from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import People

@receiver(post_save, sender=User)
def create_person(sender, instance, created, **kwargs):
    if created:
        People.objects.create(user=instance, first_name=instance.first_name)

@receiver(post_save, sender=User)
def save_person(sender, instance, **kwargs):
    instance.people.save()