from django.contrib import admin
from .models import Practice, PracticeQuestion, PracticeChoice, Subject

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'color')
    fields = ('name', 'description', 'icon', 'color')

admin.site.register(Subject, SubjectAdmin)

class PracticeQuestionInline(admin.TabularInline):
    model = PracticeQuestion
    extra = 1

class PracticeAdmin(admin.ModelAdmin):
    inlines = [PracticeQuestionInline]
    list_display = ('title', 'subject', 'level', 'master')
    list_filter = ('subject', 'level')
    # Enables the searchable autocomplete dropdown wherever Practice is a FK.
    search_fields = ('title', 'subject__name')

admin.site.register(Practice, PracticeAdmin)
class PracticeChoiceInline(admin.TabularInline):
    model = PracticeChoice
    extra = 2
    fields = ['is_correct', 'text']
    classes = ['collapse']  # optional: makes it collapsible

class PracticeQuestionAdmin(admin.ModelAdmin):
    inlines = [PracticeChoiceInline]

    # Type to search practices by title or subject instead of scrolling a huge list.
    autocomplete_fields = ['practice']
    list_filter = ('practice__subject',)

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