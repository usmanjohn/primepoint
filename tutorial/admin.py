from django.contrib import admin
from .models import Tutorial, TutorialPlaylist, PlaylistTutorial


@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display        = ['title', 'author', 'category', 'is_published', 'views', 'created_at']
    list_filter         = ['category', 'is_published']
    list_editable       = ['is_published']
    search_fields       = ['title', 'author__username', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy      = 'created_at'
    readonly_fields     = ['views', 'created_at', 'updated_at']


class PlaylistTutorialInline(admin.TabularInline):
    model  = PlaylistTutorial
    extra  = 1
    fields = ['tutorial', 'order']


@admin.register(TutorialPlaylist)
class TutorialPlaylistAdmin(admin.ModelAdmin):
    list_display        = ['title', 'author', 'category', 'is_published', 'tutorial_count', 'created_at']
    list_filter         = ['category', 'is_published']
    list_editable       = ['is_published']
    search_fields       = ['title', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields     = ['created_at', 'updated_at']
    inlines             = [PlaylistTutorialInline]

    def tutorial_count(self, obj):
        return obj.items.count()
    tutorial_count.short_description = 'Tutorials'
