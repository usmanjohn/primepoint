from django.db import models
from django.utils import timezone


class Exam(models.Model):
    LANGUAGE_CHOICES = [
        ('korean', '한국어 (Korean)'),
        ('english', 'English'),
        ('japanese', '日本語 (Japanese)'),
        ('chinese', '中文 (Chinese)'),
    ]
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='korean')
    exam_number = models.IntegerField()
    listening_audio = models.FileField(upload_to='exam_audio/', blank=True, null=True)
    listening_minutes = models.IntegerField(default=60)
    reading_minutes = models.IntegerField(default=70)
    writing_minutes = models.IntegerField(default=50)
    allow_audio_replay = models.BooleanField(default=True)
    allow_audio_pause = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['language', '-exam_number']

    def __str__(self):
        return self.title


SECTION_CHOICES = [
    ('listening', 'Listening / 듣기'),
    ('reading', 'Reading / 읽기'),
    ('writing', 'Writing / 쓰기'),
]


class ExamPassage(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='passages')
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    question_from = models.IntegerField()
    question_to = models.IntegerField()
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='exam_images/', blank=True, null=True)

    class Meta:
        ordering = ['question_from']

    def __str__(self):
        if self.question_from == self.question_to:
            return f'{self.exam} — {self.get_section_display()} Q{self.question_from} passage'
        return f'{self.exam} — {self.get_section_display()} Q{self.question_from}–{self.question_to} passage'

    def get_section_display(self):
        return dict(SECTION_CHOICES).get(self.section, self.section)


class ExamQuestion(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    number = models.IntegerField()
    passage = models.TextField(blank=True)
    passage_image = models.ImageField(upload_to='exam_images/', blank=True, null=True)
    question_text = models.TextField(blank=True)
    question_image = models.ImageField(upload_to='exam_images/', blank=True, null=True)
    is_writing = models.BooleanField(default=False)

    class Meta:
        ordering = ['number']
        unique_together = ['exam', 'section', 'number']

    def __str__(self):
        return f'{self.exam} — {self.get_section_display()} Q{self.number}'


class ExamChoice(models.Model):
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Q{self.question.number}: {self.text[:40]}'


class ExamAttempt(models.Model):
    SECTION_STATUS = [
        ('listening', 'Listening / 듣기'),
        ('reading', 'Reading / 읽기'),
        ('writing', 'Writing / 쓰기'),
        ('completed', 'Completed'),
    ]
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='exam_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='attempts')
    current_section = models.CharField(max_length=20, choices=SECTION_STATUS, default='listening')
    start_time = models.DateTimeField(auto_now_add=True)
    listening_started_at = models.DateTimeField(null=True, blank=True)
    reading_started_at = models.DateTimeField(null=True, blank=True)
    writing_started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    listening_score = models.IntegerField(null=True, blank=True)
    reading_score = models.IntegerField(null=True, blank=True)
    writing_score = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return f'{self.panda} — {self.exam} ({self.current_section})'

    def section_seconds_remaining(self):
        now = timezone.now()
        if self.current_section == 'listening' and self.listening_started_at:
            elapsed = (now - self.listening_started_at).total_seconds()
            return max(0, self.exam.listening_minutes * 60 - int(elapsed))
        if self.current_section == 'reading' and self.reading_started_at:
            elapsed = (now - self.reading_started_at).total_seconds()
            return max(0, self.exam.reading_minutes * 60 - int(elapsed))
        if self.current_section == 'writing' and self.writing_started_at:
            elapsed = (now - self.writing_started_at).total_seconds()
            return max(0, self.exam.writing_minutes * 60 - int(elapsed))
        return 0


class ExamAnswer(models.Model):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    selected_choice = models.ForeignKey(ExamChoice, on_delete=models.SET_NULL, null=True, blank=True)
    written_answer = models.TextField(blank=True)
    saved_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['attempt', 'question']

    def __str__(self):
        return f'{self.attempt} — Q{self.question.number}'
