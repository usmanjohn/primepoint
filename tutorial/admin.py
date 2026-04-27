from django.contrib import admin
from .models import Tutorial


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display        = ['title', 'author', 'category', 'is_published', 'views', 'created_at']
    list_filter         = ['category', 'is_published']
    list_editable       = ['is_published']
    search_fields       = ['title', 'author__username', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy      = 'created_at'
    readonly_fields     = ['views', 'created_at', 'updated_at']
