from django.contrib import admin

from .models import ExamTrack, Lesson, LessonBlock, BlockChoice


@admin.register(ExamTrack)
class ExamTrackAdmin(admin.ModelAdmin):
    list_display        = ['name', 'order', 'is_published', 'lesson_count', 'created_at']
    list_editable       = ['order', 'is_published']
    search_fields       = ['name', 'summary']
    prepopulated_fields = {'slug': ('name',)}

    def lesson_count(self, obj):
        return obj.lessons.count()
    lesson_count.short_description = 'Lessons'


class LessonBlockInline(admin.StackedInline):
    model  = LessonBlock
    extra  = 1
    fields = ['order', 'block_type', 'rich_text', 'image', 'caption', 'explanation']
    show_change_link = True   # open the block to edit its MCQ choices


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display        = ['title', 'track', 'skill', 'order', 'is_published', 'views', 'created_at']
    list_filter         = ['track', 'skill', 'is_published']
    list_editable       = ['order', 'is_published']
    search_fields       = ['title', 'summary', 'track__name']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields     = ['views', 'created_at', 'updated_at']
    inlines             = [LessonBlockInline]


class BlockChoiceInline(admin.TabularInline):
    model  = BlockChoice
    extra  = 4
    fields = ['order', 'text', 'is_correct']


@admin.register(LessonBlock)
class LessonBlockAdmin(admin.ModelAdmin):
    list_display  = ['lesson', 'block_type', 'order']
    list_filter   = ['block_type', 'lesson__track']
    search_fields = ['lesson__title', 'caption']
    inlines       = [BlockChoiceInline]
