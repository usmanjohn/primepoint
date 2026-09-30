from django.contrib import admin

from .models import AnswerAppeal, ItemResponse, Task, TaskItem, Workbook, WorkbookAttempt


class TaskItemInline(admin.StackedInline):
    model = TaskItem
    extra = 0


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'workbook', 'section', 'kind', 'stars')
    list_filter = ('section', 'kind')
    inlines = [TaskItemInline]


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0
    fields = ('section', 'order', 'kind', 'title', 'stars')
    show_change_link = True


@admin.register(Workbook)
class WorkbookAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_published', 'updated_at')
    list_filter = ('is_published',)
    search_fields = ('tutorial__title',)
    inlines = [TaskInline]


@admin.register(WorkbookAttempt)
class WorkbookAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'workbook', 'sections_done', 'correct', 'total',
                    'points_awarded', 'completed_at')
    search_fields = ('user__username', 'workbook__tutorial__title')


@admin.register(ItemResponse)
class ItemResponseAdmin(admin.ModelAdmin):
    list_display = ('attempt', 'item', 'text', 'verdict', 'self_mark', 'done')
    list_filter = ('verdict',)


@admin.register(AnswerAppeal)
class AnswerAppealAdmin(admin.ModelAdmin):
    list_display = ('item', 'user', 'text', 'status', 'created_at')
    list_filter = ('status',)
