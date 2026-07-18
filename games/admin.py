from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import CrosswordPuzzle, EnglishCrossword, WordSearchPuzzle, CodeBreakerPuzzle, CodeBreakerClue, PrimeClimbChallenge, SortingRaceChallenge, WordOrderChallenge, OddOneOutPack, OddOneOutQuestion, MathSquarePuzzle, MathChampResult
from .views import generate_word_search
from .views import _pc_correct_numbers
from .generator import generate_math_square


@admin.register(CrosswordPuzzle)
class CrosswordPuzzleAdmin(admin.ModelAdmin):
    list_display    = ('title', 'size_display', 'is_published', 'created_at', 'grid_status', 'editor_link')
    list_filter     = ('is_published',)
    readonly_fields = ('editor_button', 'grid_status_detail')
    fields          = ('title', 'cover_image', 'grid_rows', 'grid_cols', 'is_published',
                       'editor_button', 'grid_status_detail')

    def size_display(self, obj):
        return f'{obj.grid_rows}×{obj.grid_cols}'
    size_display.short_description = 'Size'

    def grid_status(self, obj):
        if obj.grid_data:
            n = len(obj.grid_data.get('words', []))
            return f'✓ {n} words'
        return '— empty'
    grid_status.short_description = 'Grid'

    def grid_status_detail(self, obj):
        if not obj.grid_data:
            return '— grid not built yet'
        words = obj.grid_data.get('words', [])
        rows  = obj.grid_data.get('rows', obj.grid_rows)
        cols  = obj.grid_data.get('cols', obj.grid_cols)
        return format_html(
            '<strong style="color:#16a34a;">✓ Grid ready</strong> — '
            '{} words on a {}×{} grid.',
            len(words), rows, cols,
        )
    grid_status_detail.short_description = 'Grid status'

    def editor_button(self, obj):
        if not obj.pk:
            return 'Save the puzzle first, then open the grid editor.'
        url = reverse('crossword_edit', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="padding:8px 18px; background:#7c3aed; color:#fff; '
            'border-radius:6px; text-decoration:none; font-weight:600;">&#9998; Open Grid Editor</a>',
            url,
        )
    editor_button.short_description = 'Grid editor'

    def editor_link(self, obj):
        if not obj.pk:
            return '—'
        url = reverse('crossword_edit', args=[obj.pk])
        return format_html('<a href="{}">Edit grid</a>', url)
    editor_link.short_description = 'Editor'


@admin.register(EnglishCrossword)
class EnglishCrosswordAdmin(admin.ModelAdmin):
    list_display    = ('title', 'size_display', 'is_published', 'created_at', 'grid_status', 'editor_link')
    list_filter     = ('is_published',)
    readonly_fields = ('editor_button', 'grid_status_detail')
    fields          = ('title', 'cover_image', 'grid_rows', 'grid_cols', 'is_published',
                       'editor_button', 'grid_status_detail')

    def size_display(self, obj):
        return f'{obj.grid_rows}×{obj.grid_cols}'
    size_display.short_description = 'Size'

    def grid_status(self, obj):
        if obj.grid_data:
            n = len(obj.grid_data.get('words', []))
            return f'✓ {n} words'
        return '— empty'
    grid_status.short_description = 'Grid'

    def grid_status_detail(self, obj):
        if not obj.grid_data:
            return '— grid not built yet'
        words = obj.grid_data.get('words', [])
        rows  = obj.grid_data.get('rows', obj.grid_rows)
        cols  = obj.grid_data.get('cols', obj.grid_cols)
        return format_html(
            '<strong style="color:#16a34a;">✓ Grid ready</strong> — '
            '{} words on a {}×{} grid.',
            len(words), rows, cols,
        )
    grid_status_detail.short_description = 'Grid status'

    def editor_button(self, obj):
        if not obj.pk:
            return 'Save the puzzle first, then open the grid editor.'
        url = reverse('english_crossword_edit', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="padding:8px 18px; background:#0369a1; color:#fff; '
            'border-radius:6px; text-decoration:none; font-weight:600;">&#9998; Open Grid Editor</a>',
            url,
        )
    editor_button.short_description = 'Grid editor'

    def editor_link(self, obj):
        if not obj.pk:
            return '—'
        url = reverse('english_crossword_edit', args=[obj.pk])
        return format_html('<a href="{}">Edit grid</a>', url)
    editor_link.short_description = 'Editor'


def generate_wordsearch_grids(modeladmin, request, queryset):
    for puzzle in queryset:
        words = puzzle.word_list.splitlines()
        size  = max(10, min(puzzle.grid_size, 20))
        grid, placed = generate_word_search(words, size)
        puzzle.grid_data = {'size': size, 'grid': grid, 'words': placed}
        puzzle.save()
    modeladmin.message_user(request, f'Generated grids for {queryset.count()} puzzle(s).')
generate_wordsearch_grids.short_description = 'Generate word-search grid'


@admin.register(WordSearchPuzzle)
class WordSearchPuzzleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'grid_size', 'word_count', 'is_published', 'grid_status', 'created_at')
    list_filter   = ('is_published',)
    actions       = [generate_wordsearch_grids]
    fields        = ('title', 'word_list', 'grid_size', 'is_published')

    def word_count(self, obj):
        return len([w for w in obj.word_list.splitlines() if w.strip()])
    word_count.short_description = 'Words'

    def grid_status(self, obj):
        if obj.grid_data:
            n = len(obj.grid_data.get('words', []))
            return f'✓ {n} placed'
        return '— not generated'
    grid_status.short_description = 'Grid'


class CodeBreakerClueInline(admin.TabularInline):
    model       = CodeBreakerClue
    extra       = 0
    fields      = ('letter_index', 'letter', 'math_expression', 'answer')
    ordering    = ('letter_index',)


@admin.register(CodeBreakerPuzzle)
class CodeBreakerPuzzleAdmin(admin.ModelAdmin):
    list_display  = ('title', 'secret_word', 'difficulty', 'is_active', 'created_by', 'clue_count', 'created_at')
    list_filter   = ('difficulty', 'is_active')
    search_fields = ('title', 'secret_word')
    inlines       = [CodeBreakerClueInline]

    def clue_count(self, obj):
        return obj.clues.count()
    clue_count.short_description = 'Clues'


@admin.register(CodeBreakerClue)
class CodeBreakerClueAdmin(admin.ModelAdmin):
    list_display  = ('puzzle', 'letter_index', 'letter', 'math_expression', 'answer')
    list_filter   = ('puzzle__difficulty',)
    search_fields = ('puzzle__title', 'letter', 'math_expression')


@admin.register(PrimeClimbChallenge)
class PrimeClimbChallengeAdmin(admin.ModelAdmin):
    list_display  = ('title', 'mode', 'target', 'is_active', 'created_by', 'answer_count', 'created_at')
    list_filter   = ('mode', 'is_active')
    search_fields = ('title',)

    def answer_count(self, obj):
        return len(_pc_correct_numbers(obj.mode, obj.target))
    answer_count.short_description = 'Answers'


@admin.register(SortingRaceChallenge)
class SortingRaceChallengeAdmin(admin.ModelAdmin):
    list_display  = ('title', 'difficulty', 'is_active', 'created_by', 'created_at')
    list_filter   = ('difficulty', 'is_active')
    search_fields = ('title',)


class OddOneOutQuestionInline(admin.TabularInline):
    model  = OddOneOutQuestion
    extra  = 1
    fields = ('word_1', 'word_2', 'word_3', 'word_4', 'odd_index', 'explanation', 'order')


@admin.register(OddOneOutPack)
class OddOneOutPackAdmin(admin.ModelAdmin):
    list_display  = ('title', 'language', 'question_count', 'is_active', 'created_by', 'created_at')
    list_filter   = ('language', 'is_active')
    search_fields = ('title',)
    inlines       = [OddOneOutQuestionInline]

    def question_count(self, obj):
        return obj.question_count()
    question_count.short_description = 'Questions'


@admin.register(OddOneOutQuestion)
class OddOneOutQuestionAdmin(admin.ModelAdmin):
    list_display  = ('pack', 'word_1', 'word_2', 'word_3', 'word_4', 'odd_index', 'order')
    list_filter   = ('pack',)


@admin.register(WordOrderChallenge)
class WordOrderChallengeAdmin(admin.ModelAdmin):
    list_display  = ('title', 'word_count', 'is_active', 'created_by', 'created_at')
    list_filter   = ('is_active',)
    search_fields = ('title', 'sentence')

    def word_count(self, obj):
        return obj.word_count()
    word_count.short_description = 'Words'


def regenerate_math_squares(modeladmin, request, queryset):
    count = 0
    for puzzle in queryset:
        grid = generate_math_square(puzzle.difficulty)
        if grid:
            puzzle.grid_data    = grid
            puzzle.size         = grid['n']
            puzzle.is_published = True
            puzzle.save()
            count += 1
    modeladmin.message_user(request, f'Regenerated {count} puzzle(s).')
regenerate_math_squares.short_description = 'Regenerate grid (auto)'


@admin.register(MathSquarePuzzle)
class MathSquarePuzzleAdmin(admin.ModelAdmin):
    list_display    = ('title', 'difficulty', 'size', 'is_published', 'created_by', 'grid_status', 'editor_link', 'created_at')
    list_filter     = ('difficulty', 'is_published')
    search_fields   = ('title',)
    actions         = [regenerate_math_squares]
    readonly_fields = ('editor_button',)
    fields          = ('title', 'difficulty', 'size', 'is_published', 'created_by', 'editor_button')

    def grid_status(self, obj):
        if not obj.grid_data:
            return '— empty'
        blanks = sum(
            1 for row in obj.grid_data.get('cells', []) for cell in row
            if cell.get('t') == 'num' and not cell.get('given')
        )
        return f'✓ {blanks} blanks'
    grid_status.short_description = 'Grid'

    def editor_button(self, obj):
        if not obj.pk:
            return 'Save the puzzle first, then open the grid editor.'
        url = reverse('mathsquare_edit', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="padding:8px 18px; background:#0d9488; color:#fff; '
            'border-radius:6px; text-decoration:none; font-weight:600;">&#9998; Open Grid Editor</a>',
            url,
        )
    editor_button.short_description = 'Grid editor'

    def editor_link(self, obj):
        if not obj.pk:
            return '—'
        return format_html('<a href="{}">Edit grid</a>', reverse('mathsquare_edit', args=[obj.pk]))
    editor_link.short_description = 'Editor'


@admin.register(MathChampResult)
class MathChampResultAdmin(admin.ModelAdmin):
    list_display  = ('user', 'grade', 'score', 'stage_reached', 'finished',
                     'hearts_left', 'medal', 'elapsed_display', 'created_at')
    list_filter   = ('grade', 'finished', 'medal')
    search_fields = ('user__username',)

    def elapsed_display(self, obj):
        return obj.elapsed_display
    elapsed_display.short_description = 'Time'
