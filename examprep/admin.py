from django.contrib import admin

from .models import (ExamTrack, Topic, Lesson, LessonBlock, BlockChoice,
                     GrammarPoint, GrammarExample, GrammarSynonym)


@admin.register(ExamTrack)
class ExamTrackAdmin(admin.ModelAdmin):
    list_display        = ['name', 'order', 'is_published', 'lesson_count', 'created_at']
    list_editable       = ['order', 'is_published']
    search_fields       = ['name', 'summary']
    prepopulated_fields = {'slug': ('name',)}

    def lesson_count(self, obj):
        return obj.lessons.count()
    lesson_count.short_description = 'Lessons'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display        = ['title', 'track', 'skill', 'order', 'is_published', 'lesson_count']
    list_filter         = ['track', 'skill', 'is_published']
    list_editable       = ['order', 'is_published']
    search_fields       = ['title', 'summary', 'track__name']
    prepopulated_fields = {'slug': ('title',)}

    def lesson_count(self, obj):
        return obj.lessons.count()
    lesson_count.short_description = 'Lessons'


class LessonBlockInline(admin.StackedInline):
    model  = LessonBlock
    extra  = 1
    fields = ['order', 'image', 'caption', 'rich_text', 'explanation']
    show_change_link = True   # open the block to add multiple-choice options


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display        = ['title', 'track', 'skill', 'topic', 'order', 'is_published', 'views', 'created_at']
    list_filter         = ['track', 'skill', 'topic', 'is_published']
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
    list_display  = ['lesson', 'order', 'caption']
    list_filter   = ['lesson__track', 'lesson__skill']
    search_fields = ['lesson__title', 'caption']
    inlines       = [BlockChoiceInline]


class GrammarExampleInline(admin.TabularInline):
    model  = GrammarExample
    extra  = 2
    fields = ['order', 'korean', 'uz']


class GrammarSynonymInline(admin.TabularInline):
    model  = GrammarSynonym
    fk_name = 'point'
    extra  = 2
    fields = ['order', 'pattern', 'note', 'related']
    raw_id_fields = ['related']


@admin.register(GrammarPoint)
class GrammarPointAdmin(admin.ModelAdmin):
    list_display  = ['pattern', 'meaning', 'level', 'category', 'function',
                     'freq', 'order', 'is_published']
    list_filter   = ['track', 'level', 'category', 'function', 'register', 'is_published']
    list_editable = ['order', 'is_published']
    search_fields = ['pattern', 'meaning', 'note', 'attach']
    inlines       = [GrammarExampleInline, GrammarSynonymInline]
    readonly_fields = ['created_at', 'updated_at']
