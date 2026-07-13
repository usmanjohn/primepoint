from django.contrib import admin

from .models import (Subject, Collection, Story, StoryWord, StoryQuestion,
                     StoryGrammar, WritingTemplate)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display        = ['name', 'order', 'is_published', 'collection_count', 'created_at']
    list_editable       = ['order', 'is_published']
    search_fields       = ['name', 'summary']
    prepopulated_fields = {'slug': ('name',)}

    def collection_count(self, obj):
        return obj.collections.count()
    collection_count.short_description = 'Collections'


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display        = ['title', 'subject', 'order', 'is_published', 'story_count', 'created_at']
    list_filter         = ['subject', 'is_published']
    list_editable       = ['order', 'is_published']
    search_fields       = ['title', 'description', 'subject__name']
    prepopulated_fields = {'slug': ('title',)}

    def story_count(self, obj):
        return obj.stories.count()
    story_count.short_description = 'Stories'


class StoryWordInline(admin.TabularInline):
    """Derived from cn-word spans in the body — read-only."""
    model = StoryWord
    extra = 0
    can_delete = False
    readonly_fields = ['order', 'word', 'translation', 'pos']

    def has_add_permission(self, request, obj=None):
        return False


class StoryGrammarInline(admin.TabularInline):
    """Grammar points — rebuilt on import, editable here if needed."""
    model = StoryGrammar
    extra = 0
    fields = ['order', 'pattern', 'meaning', 'examples']


class StoryQuestionInline(admin.TabularInline):
    """Comprehension MCQs — rebuilt on import, editable here if needed."""
    model = StoryQuestion
    extra = 0
    fields = ['order', 'text', 'choices', 'answer', 'explanation']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display        = ['title', 'collection', 'order', 'is_published', 'views', 'created_at']
    list_filter         = ['collection__subject', 'collection', 'is_published']
    list_editable       = ['order', 'is_published']
    search_fields       = ['title', 'summary', 'collection__title']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields     = ['views', 'created_at', 'updated_at']
    inlines             = [StoryWordInline, StoryGrammarInline, StoryQuestionInline]


@admin.register(WritingTemplate)
class WritingTemplateAdmin(admin.ModelAdmin):
    list_display  = ['title', 'subject', 'order', 'is_published', 'downloads', 'created_at']
    list_filter   = ['subject', 'is_published']
    list_editable = ['order', 'is_published']
    search_fields = ['title', 'description', 'subject__name']
    readonly_fields = ['downloads', 'created_at']
