from django.contrib import admin
from .models import Practice, PracticeQuestion, PracticeChoice, Subject

admin.site.register(Subject)

class PracticeQuestionInline(admin.TabularInline):
    model = PracticeQuestion
    extra = 1

class PracticeAdmin(admin.ModelAdmin):
    inlines = [PracticeQuestionInline]

admin.site.register(Practice, PracticeAdmin)
class PracticeChoiceInline(admin.TabularInline):
    model = PracticeChoice
    extra = 2
    fields = ['is_correct', 'text']
    classes = ['collapse']  # optional: makes it collapsible

class PracticeQuestionAdmin(admin.ModelAdmin):
    inlines = [PracticeChoiceInline]

    fieldsets = (
        (None, {
            'fields': ('practice', 'question_text', 'image')
        }),
        ('Extra', {
            'fields': ('explanation', 'hint', 'points', 'order'),
            'classes': ('collapse',)
        }),
    )

    list_display = ('id', 'practice', 'short_question')

    def short_question(self, obj):
        return obj.question_text[:50]
    
admin.site.register(PracticeQuestion, PracticeQuestionAdmin)