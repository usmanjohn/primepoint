from django.contrib import admin
from .models import (Classroom, Lesson, LessonNote, ClassroomDiscussion,
                     ClassroomReply, ClassroomResource)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ('title', 'order', 'is_published')


class LessonNoteInline(admin.TabularInline):
    model = LessonNote
    extra = 0


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'master', 'subject', 'is_active', 'lesson_count', 'created_at')
    list_filter = ('is_active', 'subject', 'master')
    search_fields = ('name', 'master__name')
    filter_horizontal = ('groups', 'individual_pandas')
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'order', 'is_published', 'created_at')
    list_filter = ('is_published', 'classroom__master')
    filter_horizontal = ('practices', 'homeworks', 'tutorials')
    inlines = [LessonNoteInline]


@admin.register(ClassroomDiscussion)
class ClassroomDiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'author', 'is_pinned', 'created_at')
    list_filter = ('classroom', 'is_pinned')


@admin.register(ClassroomResource)
class ClassroomResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'kind', 'order', 'created_at')
    list_filter = ('kind', 'classroom')
