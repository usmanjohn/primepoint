from django.db import models
from django.contrib.auth.models import User
from people.models import People

from django.db import models
from django.db.models import Avg

class Master(models.Model):
    profile = models.ForeignKey(People, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    
    # --- New Fields ---
    # Optional: Cache the student count for performance
    student_count = models.PositiveIntegerField(default=0)
    # The average rating teachers get from their students
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_stats(self):
        """Call this to refresh teacher stats based on related Pandas."""
        self.student_count = self.panda.count()
        # Assuming Panda has a rating field representing student performance/satisfaction
        avg = self.panda.aggregate(Avg('rating'))['rating__avg'] or 0
        self.avg_rating = avg
        self.save()

    def __str__(self):
        return self.name