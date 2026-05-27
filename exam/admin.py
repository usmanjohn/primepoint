from django.contrib import admin
from .models import Exam, ExamQuestion, ExamChoice, ExamAttempt, ExamAnswer


class ExamChoiceInline(admin.TabularInline):
    model = ExamChoice
    extra = 4
    fields = ('text', 'is_correct')


class ExamQuestionInline(admin.TabularInline):
    model = ExamQuestion
    extra = 0
    fields = ('number', 'section', 'question_text', 'question_image', 'is_writing')
    show_change_link = True


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'exam_number', 'is_published', 'allow_audio_replay', 'allow_audio_pause', 'created_at')
    list_editable = ('is_published', 'allow_audio_replay', 'allow_audio_pause')
    list_filter = ('is_published', 'language')
    search_fields = ('title',)
    inlines = [ExamQuestionInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'language', 'exam_number', 'listening_audio', 'is_published'),
        }),
        ('Section Durations', {
            'fields': ('listening_minutes', 'reading_minutes', 'writing_minutes'),
        }),
        ('Audio Controls', {
            'description': 'Toggle what students can do with the listening audio.',
            'fields': ('allow_audio_replay', 'allow_audio_pause'),
        }),
    )


@admin.register(ExamQuestion)
class ExamQuestionAdmin(admin.ModelAdmin):
    list_display = ('exam', 'section', 'number', 'question_text_short', 'is_writing')
    list_filter = ('exam', 'section', 'is_writing')
    search_fields = ('question_text', 'passage')
    inlines = [ExamChoiceInline]
    fields = ('exam', 'section', 'number', 'passage', 'passage_image', 'question_text', 'question_image', 'is_writing')

    def question_text_short(self, obj):
        return obj.question_text[:60] + '…' if len(obj.question_text) > 60 else obj.question_text
    question_text_short.short_description = 'Question'


class ExamAnswerInline(admin.TabularInline):
    model = ExamAnswer
    extra = 0
    readonly_fields = ('question', 'selected_choice', 'written_answer', 'saved_at')
    can_delete = False


@admin.register(ExamAttempt)
class ExamAttemptAdmin(admin.ModelAdmin):
    list_display = ('panda', 'exam', 'current_section', 'listening_score', 'reading_score', 'writing_score', 'start_time')
    list_filter = ('exam', 'current_section')
    list_editable = ('writing_score',)
    readonly_fields = ('panda', 'exam', 'current_section', 'start_time',
                       'listening_started_at', 'reading_started_at', 'writing_started_at', 'completed_at',
                       'listening_score', 'reading_score')
    inlines = [ExamAnswerInline]
    search_fields = ('panda__user__username',)
