from django.contrib import admin
from .models import Practice, PracticeQuestion, PracticeAttempt, UserAnswer

@admin.register(PracticeQuestion)
class PracticeQuestionAdmin(admin.ModelAdmin):
    # Organizes fields into sections for a cleaner UI
    fieldsets = (
        ('Meta Data', {
            'fields': ('practice', 'made_by', 'correct_answer', 'is_multiple_choice')
        }),
        ('The Question', {
            'fields': ('question_text', 'image')
        }),
        ('Choices (LaTeX Supported)', {
            'fields': ('choice1', 'choice2', 'choice3', 'choice4', 'choice5'),
            'description': "Fill 1-5. For True/False, only fill Choice 1 and 2."
        }),
        ('Feedback', {
            'fields': ('explanation',)
        }),
    )
    list_display = ('id', 'get_practice_title', 'made_by', 'correct_answer')
    list_filter = ('practice__type', 'practice__level', 'made_by')
    search_fields = ('question_text',)

    def get_practice_title(self, obj):
        return obj.practice.title
    get_practice_title.short_description = 'Practice Set'

@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'level', 'purpose', 'master', 'is_free')
    list_filter = ('type', 'level', 'purpose')
    search_fields = ('title', 'description')

@admin.register(PracticeAttempt)
class PracticeAttemptAdmin(admin.ModelAdmin):
    list_display = ('panda', 'practice', 'score', 'completed_at')
    readonly_fields = ('start_time', 'completed_at')

admin.site.register(UserAnswer)
