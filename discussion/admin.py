from django.contrib import admin
from .models import Category, Thread, Reply, ThreadVote, ReplyVote


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'color', 'order']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order']


class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 0
    readonly_fields = ['author', 'created_at']


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'is_announcement', 'is_pinned', 'is_closed', 'view_count', 'created_at']
    list_filter = ['category', 'is_announcement', 'is_pinned', 'is_closed']
    search_fields = ['title', 'body']
    inlines = [ReplyInline]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'is_accepted', 'created_at']
    list_filter = ['is_accepted']


admin.site.register(ThreadVote)
admin.site.register(ReplyVote)
