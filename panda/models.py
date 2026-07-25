from django.db import models
from masters.models import Master
from people.models import Profile
class Panda(models.Model):
    PURPOSE_CHOICES = [('learning', 'Learning'), ('entertainment', 'Entertainment'), ('other', 'Other')]
    name = models.CharField(max_length=100, default='Panda')
    masters = models.ManyToManyField(Master, blank=True, related_name='pandas')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='panda')
    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, default='learning')
    rating = models.IntegerField(default=0) 

    # --- New Logic ---
    @property
    def rank(self):
        """Dynamic rank based on rating."""
        if self.rating < 50: return "Novice"
        if self.rating < 150: return "Scholar"
        if self.rating < 300: return "Expert"
        return "Grandmaster"

    def recalc_rating(self):
        """Rating = every point this student has earned, from every library.

        The sources live in `prime.progress.SOURCES`, which the progress page
        and analytics read too — so a library can never be worth points on one
        screen and invisible on another. Add a library there, not here.

        Every app that awards points must call this instead of writing `rating`
        directly, so one source never wipes out another's points.
        """
        from prime.progress import total_points
        self.rating = round(total_points(self.profile.user))
        self.save(update_fields=['rating'])

    def __str__(self):
        return f"{self.profile.user.username} ({self.rank})"