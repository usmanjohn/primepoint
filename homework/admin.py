from django.contrib import admin
from .models import Homework, HomeworkAssignment, PandaGroup


class HomeworkAssignmentInline(admin.TabularInline):
    model = HomeworkAssignment
    extra = 0
    readonly_fields = ('submitted_at',)


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'master', 'practice', 'due_date', 'created_at')
    list_filter = ('master',)
    inlines = [HomeworkAssignmentInline]


@admin.register(HomeworkAssignment)
class HomeworkAssignmentAdmin(admin.ModelAdmin):
    list_display = ('homework', 'panda', 'status', 'submitted_at')
    list_filter = ('status',)


@admin.register(PandaGroup)
class PandaGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'master', 'member_count', 'created_at')
    filter_horizontal = ('members',)
