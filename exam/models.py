from django.db import models
from django.utils import timezone


class Exam(models.Model):
    LANGUAGE_CHOICES = [
        ('korean', '한국어 (Korean)'),
        ('english', 'English'),
        ('japanese', '日本語 (Japanese)'),
        ('chinese', '中文 (Chinese)'),
    ]
    FORMAT_CHOICES = [
        ('topik', 'TOPIK II'),
        ('sat', 'Digital SAT'),
    ]
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='korean')
    exam_format = models.CharField(
        max_length=20, choices=FORMAT_CHOICES, default='topik',
        help_text='Drives scoring and the on-screen layout.',
    )
    exam_number = models.IntegerField()
    listening_audio = models.FileField(upload_to='exam_audio/', blank=True, null=True)
    # Legacy TOPIK timings. The flow now reads ExamModule.minutes; these are kept
    # because the TOPIK data files set them and the 0005 migration seeds modules from them.
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

    @property
    def is_sat(self):
        return self.exam_format == 'sat'

    def spine(self):
        """The stage-1 modules, in the order a taker meets them."""
        return self.modules.filter(stage=1).order_by('order')

    def total_minutes(self):
        """Longest possible sitting, breaks included.

        A break is declared on the module it follows, which for an adaptive
        section is the stage-2 branch rather than the spine module — so the
        break has to be looked for on both, or the sitting is advertised ten
        minutes shorter than it is.
        """
        total = 0
        for first in self.spine():
            total += first.minutes + first.break_minutes
            branches = list(self.modules.filter(kind=first.kind, stage=2))
            if branches:
                total += max(b.minutes for b in branches)
                total += max(b.break_minutes for b in branches)
        return total

    def question_total(self):
        """Questions actually SEEN in one sitting (a branch counts once)."""
        total = 0
        for first in self.spine():
            total += first.questions_count()
            branch = self.modules.filter(kind=first.kind, stage=2).first()
            if branch:
                total += branch.questions_count()
        return total


SECTION_CHOICES = [
    ('listening', 'Listening / 듣기'),
    ('reading', 'Reading / 읽기'),
    ('writing', 'Writing / 쓰기'),
    ('rw1', 'SAT Reading and Writing — Module 1'),
    ('rw2e', 'SAT Reading and Writing — Module 2 (lower)'),
    ('rw2h', 'SAT Reading and Writing — Module 2 (upper)'),
    ('math1', 'SAT Math — Module 1'),
    ('math2e', 'SAT Math — Module 2 (lower)'),
    ('math2h', 'SAT Math — Module 2 (upper)'),
]


class ExamModule(models.Model):
    """One timed run of questions inside an exam.

    A TOPIK exam has three (listening, reading, writing), all stage 1.
    A digital-SAT exam has six: two stage-1 modules and, for each, an easy/hard
    stage-2 branch — the taker sees four of them.
    """
    KIND_CHOICES = [
        ('listening', 'Listening'),
        ('reading', 'Reading'),
        ('writing', 'Writing'),
        ('rw', 'Reading and Writing'),
        ('math', 'Math'),
    ]
    DIFFICULTY_CHOICES = [
        ('', '—'),
        ('easy', 'Lower'),
        ('hard', 'Upper'),
    ]
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='modules')
    code = models.CharField(max_length=20, help_text='Matches ExamQuestion.section')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    stage = models.IntegerField(default=1, help_text='1 = everyone takes it, 2 = a routed branch')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, blank=True, default='')
    label = models.CharField(max_length=120)
    label_uz = models.CharField(max_length=120, blank=True)
    minutes = models.IntegerField(default=30)
    order = models.IntegerField(default=1, help_text='Position of this kind in the sitting')
    route_threshold = models.IntegerField(
        null=True, blank=True,
        help_text='Stage-1 only: raw correct >= this routes to the upper module.',
    )
    break_minutes = models.IntegerField(default=0, help_text='Break AFTER this module finishes')
    calculator = models.BooleanField(default=False)
    reference_sheet = models.BooleanField(default=False)

    class Meta:
        ordering = ['exam', 'order', 'stage', 'difficulty']
        unique_together = ['exam', 'code']

    def __str__(self):
        return f'{self.exam} — {self.label}'

    def questions_count(self):
        return self.exam.questions.filter(section=self.code).count()

    def questions(self):
        return self.exam.questions.filter(section=self.code)

    @property
    def is_math(self):
        return self.kind == 'math'

    @property
    def is_rw(self):
        return self.kind == 'rw'


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
    ANSWER_TYPES = [
        ('mcq', 'Multiple choice'),
        ('grid', 'Student-produced response (grid-in)'),
        ('essay', 'Written / essay'),
    ]
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    number = models.IntegerField()
    question_text = models.TextField(blank=True)
    question_image = models.ImageField(upload_to='exam_images/', blank=True, null=True)
    is_writing = models.BooleanField(default=False)
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPES, default='mcq')
    accepted_answers = models.TextField(
        blank=True,
        help_text='Grid-in only: accepted answers, one per line (e.g. "2/3" or "0.667").',
    )
    explanation = models.TextField(blank=True, help_text='Shown on the result page (Uzbek).')
    skill = models.CharField(max_length=80, blank=True, help_text='Domain, for the score report')
    difficulty = models.CharField(
        max_length=10, blank=True,
        choices=[('', '—'), ('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')],
    )

    class Meta:
        ordering = ['number']
        unique_together = ['exam', 'section', 'number']

    def __str__(self):
        return f'{self.exam} — {self.get_section_display()} Q{self.number}'

    @property
    def is_grid(self):
        return self.answer_type == 'grid'

    def accepted_list(self):
        return [line.strip() for line in self.accepted_answers.splitlines() if line.strip()]

    def correct_choice(self):
        return self.choices.filter(is_correct=True).first()

    def answer_key(self):
        """Human-readable key, for the result page."""
        if self.is_grid:
            accepted = self.accepted_list()
            return accepted[0] if accepted else ''
        choice = self.correct_choice()
        return choice.text if choice else ''


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
    STATUS_CHOICES = [
        ('in_progress', 'In progress'),
        ('break', 'On break'),
        ('completed', 'Completed'),
    ]
    panda = models.ForeignKey('panda.Panda', on_delete=models.CASCADE, related_name='exam_attempts')
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='attempts')
    # Mirrors current_module.code, or 'completed'. Kept because prime/progress.py
    # counts finished attempts with current_section='completed'.
    current_section = models.CharField(max_length=20, default='listening')
    current_module = models.ForeignKey(
        ExamModule, on_delete=models.SET_NULL, null=True, blank=True, related_name='+',
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    break_until = models.DateTimeField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    listening_started_at = models.DateTimeField(null=True, blank=True)
    reading_started_at = models.DateTimeField(null=True, blank=True)
    writing_started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    listening_score = models.IntegerField(null=True, blank=True)
    reading_score = models.IntegerField(null=True, blank=True)
    writing_score = models.IntegerField(null=True, blank=True)
    # Digital SAT scaled scores
    rw_score = models.IntegerField(null=True, blank=True, help_text='SAT 200–800')
    math_score = models.IntegerField(null=True, blank=True, help_text='SAT 200–800')
    total_score = models.IntegerField(null=True, blank=True, help_text='SAT 400–1600')

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return f'{self.panda} — {self.exam} ({self.current_section})'

    @property
    def is_completed(self):
        return self.current_section == 'completed'

    def module_attempt(self, module):
        return self.module_attempts.filter(module=module).first()

    def section_seconds_remaining(self):
        """Seconds left in the module being taken right now."""
        module = self.current_module
        if not module:
            return 0
        ma = self.module_attempt(module)
        if not ma or not ma.started_at:
            return module.minutes * 60
        elapsed = (timezone.now() - ma.started_at).total_seconds()
        return max(0, module.minutes * 60 - int(elapsed))

    def break_seconds_remaining(self):
        if self.status != 'break' or not self.break_until:
            return 0
        return max(0, int((self.break_until - timezone.now()).total_seconds()))

    def taken_modules(self):
        """The modules this attempt actually met, in order."""
        return [ma.module for ma in self.module_attempts.select_related('module').order_by(
            'module__order', 'module__stage')]


class ExamModuleAttempt(models.Model):
    """One taker's run through one module — when it started, and the raw score."""
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name='module_attempts')
    module = models.ForeignKey(ExamModule, on_delete=models.CASCADE, related_name='attempts')
    started_at = models.DateTimeField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    raw_score = models.IntegerField(null=True, blank=True, help_text='Number correct')
    total_questions = models.IntegerField(default=0)

    class Meta:
        ordering = ['module__order', 'module__stage']
        unique_together = ['attempt', 'module']

    def __str__(self):
        return f'{self.attempt} — {self.module.label}'

    def percent(self):
        if not self.total_questions or self.raw_score is None:
            return None
        return round(self.raw_score / self.total_questions * 100)


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

    def is_correct(self):
        """True/False for auto-graded questions, None for essays."""
        from .gridin import grid_answer_matches
        question = self.question
        if question.answer_type == 'essay' or question.is_writing:
            return None
        if question.is_grid:
            if not self.written_answer.strip():
                return False
            return grid_answer_matches(self.written_answer, question.accepted_list())
        return bool(self.selected_choice and self.selected_choice.is_correct)
