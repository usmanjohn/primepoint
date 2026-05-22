from django.contrib import admin
from django.contrib import messages
from .models import KoreanWord, CrosswordPuzzle
from .generator import generate_crossword


@admin.register(KoreanWord)
class KoreanWordAdmin(admin.ModelAdmin):
    list_display  = ('word', 'clue_korean', 'clue_uzbek')
    search_fields = ('word', 'clue_korean', 'clue_uzbek')


def action_generate_grid(modeladmin, request, queryset):
    for puzzle in queryset:
        words = puzzle.words.all()
        if words.count() < 3:
            messages.warning(request, f'"{puzzle.title}": add at least 3 words before generating.')
            continue
        result = generate_crossword(words)
        if result is None:
            messages.error(request, f'"{puzzle.title}": could not place any words — try adding more words with shared syllables.')
            continue
        puzzle.grid_data = result
        puzzle.save()
        placed = len(result['words'])
        messages.success(request, f'"{puzzle.title}": grid generated — {placed} of {words.count()} words placed.')

action_generate_grid.short_description = 'Generate crossword grid from selected puzzles'


@admin.register(CrosswordPuzzle)
class CrosswordPuzzleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'is_published', 'created_at', 'word_count', 'grid_status')
    list_filter   = ('is_published',)
    filter_horizontal = ('words',)
    actions       = [action_generate_grid]

    def word_count(self, obj):
        return obj.words.count()
    word_count.short_description = 'Words'

    def grid_status(self, obj):
        if obj.grid_data:
            n = len(obj.grid_data.get('words', []))
            return f'✓ {n} words placed'
        return '— not generated'
    grid_status.short_description = 'Grid'
