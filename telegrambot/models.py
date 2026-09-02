from django.db import models


class TelegramPost(models.Model):
    """One thing the bot has already sent to the channel.

    Two jobs: it stops the daily quiz repeating a question it has already used
    (8000+ questions, so "never repeat" is cheap), and it remembers the
    message id of a Logic Arena puzzle so the solution can be edited into that
    same post on reveal day instead of posting a second, orphaned message.
    """

    QUIZ = 'quiz'
    PUZZLE = 'puzzle'
    SOLUTION = 'solution'
    KIND_CHOICES = [
        (QUIZ, 'Daily quiz question'),
        (PUZZLE, 'Logic Arena puzzle'),
        (SOLUTION, 'Logic Arena solution'),
    ]

    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    object_id = models.PositiveIntegerField(
        help_text='PracticeQuestion.id or LogicPuzzle.id, depending on kind.')

    chat_id = models.CharField(max_length=64, blank=True)
    message_id = models.BigIntegerField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_at']
        constraints = [
            models.UniqueConstraint(fields=['kind', 'object_id'],
                                    name='telegram_post_unique_per_object'),
        ]
        indexes = [models.Index(fields=['kind', 'posted_at'])]

    def __str__(self):
        return f'{self.get_kind_display()} #{self.object_id} → {self.message_id or "—"}'
