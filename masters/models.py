from django.db import models
from django.contrib.auth.models import User
from people.models import Profile
from django.db.models import Avg


class Master(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True, null=True)
    student_count = models.PositiveIntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update_stats(self):
        self.student_count = self.pandas.count()
        avg = self.pandas.aggregate(Avg('rating'))['rating__avg'] or 0
        self.avg_rating = avg
        self.save()

    def __str__(self):
        return self.name


class StudentEnrollment(models.Model):
    """Tracks when a student joined a master's class."""
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='enrollments')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='enrollments')
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['master', 'panda']
        ordering = ['-joined_at']

    def __str__(self):
        return f"{self.panda} → {self.master}"


class Attendance(models.Model):
    PRESENT = 'present'
    ABSENT = 'absent'
    LATE = 'late'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
        (LATE, 'Late'),
    ]
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='attendances')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PRESENT)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['master', 'panda', 'date']
        ordering = ['-date']

    def __str__(self):
        return f"{self.panda} — {self.date} ({self.status})"


class StudentPayment(models.Model):
    PAID = 'paid'
    UNPAID = 'unpaid'
    PARTIAL = 'partial'
    STATUS_CHOICES = [
        (PAID, 'Paid'),
        (UNPAID, 'Unpaid'),
        (PARTIAL, 'Partial'),
    ]
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='payments')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=UNPAID)
    period_label = models.CharField(max_length=100, blank=True, help_text="e.g. June 2026")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.panda} — {self.period_label or self.created_at.date()} ({self.status})"


class Certificate(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='issued_certificates')
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    issued_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-issued_at']

    def __str__(self):
        return f"{self.title} → {self.panda}"