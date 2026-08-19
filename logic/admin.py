from django.contrib import admin
from django.utils import timezone

from .models import LogicPuzzle, LogicSubmission


class LogicSubmissionInline(admin.TabularInline):
    model = LogicSubmission
    extra = 0
    readonly_fields = ('user', 'answer', 'reasoning', 'is_correct', 'sealed',
                       'points_awarded', 'created_at')
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(LogicPuzzle)
class LogicPuzzleAdmin(admin.ModelAdmin):
    list_display  = ('number', 'title', 'category', 'difficulty', 'state_display',
                     'reveal_at', 'answer_count', 'is_published')
    list_filter   = ('category', 'difficulty', 'is_published')
    search_fields = ('title', 'title_uz', 'teaser', 'answer_key')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LogicSubmissionInline]
    fieldsets = (
        (None, {'fields': ('number', 'title', 'title_uz', 'slug', 'category',
                           'difficulty', 'points', 'is_published', 'author')}),
        ('The problem', {'fields': ('teaser', 'teaser_uz', 'body', 'body_uz',
                                    'hint', 'hint_uz')}),
        ('The answer', {'fields': ('answer_key', 'accepted', 'answer_hint',
                                   'answer_hint_uz', 'solution', 'solution_uz')}),
        ('The schedule', {'fields': ('opens_at', 'reveal_at')}),
    )

    @admin.display(description='State')
    def state_display(self, obj):
        return obj.state

    @admin.display(description='Answers')
    def answer_count(self, obj):
        return obj.submissions.count()


@admin.register(LogicSubmission)
class LogicSubmissionAdmin(admin.ModelAdmin):
    """Read-only on purpose: grading is the model's job, not an editor's.

    Correctness is hidden in the list while a puzzle is still sealed, so an
    admin glancing at the page cannot accidentally spoil the week.
    """
    list_display  = ('puzzle', 'user', 'answer', 'verdict', 'sealed', 'created_at')
    list_filter   = ('is_correct', 'sealed', 'puzzle')
    search_fields = ('user__username', 'answer', 'reasoning')
    readonly_fields = ('puzzle', 'user', 'answer', 'reasoning', 'is_correct',
                       'sealed', 'points_awarded', 'created_at', 'updated_at')

    @admin.display(description='Verdict')
    def verdict(self, obj):
        if obj.puzzle.reveal_at > timezone.now():
            return '🔒 sealed'
        return '✓' if obj.is_correct else '✗'
