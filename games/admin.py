from django.contrib import admin, messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import path, reverse
from django.utils.html import format_html
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
            messages.warning(request, f'"{puzzle.title}": add at least 3 words first.')
            continue
        result = generate_crossword(words)
        if result is None:
            messages.error(request, f'"{puzzle.title}": generation failed — add more words with shared syllables.')
            continue
        puzzle.grid_data = result
        puzzle.save()
        messages.success(request, f'"{puzzle.title}": {len(result["words"])} of {words.count()} words placed.')

action_generate_grid.short_description = 'Generate crossword grid'


@admin.register(CrosswordPuzzle)
class CrosswordPuzzleAdmin(admin.ModelAdmin):
    list_display      = ('title', 'is_published', 'created_at', 'word_count', 'grid_status')
    list_filter       = ('is_published',)
    filter_horizontal = ('words',)
    actions           = [action_generate_grid]
    readonly_fields   = ('grid_status_detail', 'generate_button')
    fields            = ('title', 'cover_image', 'is_published', 'words',
                         'generate_button', 'grid_status_detail')

    # ── Custom URLs ──────────────────────────────────────────────────
    def get_urls(self):
        return [
            path(
                '<int:pk>/generate/',
                self.admin_site.admin_view(self.generate_view),
                name='games_crosswordpuzzle_generate',
            ),
        ] + super().get_urls()

    def generate_view(self, request, pk):
        puzzle = get_object_or_404(CrosswordPuzzle, pk=pk)
        words  = puzzle.words.all()
        if words.count() < 3:
            self.message_user(request, 'Add at least 3 words before generating.', messages.WARNING)
        else:
            result = generate_crossword(words)
            if result:
                puzzle.grid_data = result
                puzzle.save()
                self.message_user(
                    request,
                    f'Grid generated — {len(result["words"])} of {words.count()} words placed.',
                    messages.SUCCESS,
                )
            else:
                self.message_user(request, 'Generation failed — try adding more words with shared syllables.', messages.ERROR)
        return redirect(reverse('admin:games_crosswordpuzzle_change', args=[pk]))

    # ── Readonly display fields ───────────────────────────────────────
    def generate_button(self, obj):
        if not obj.pk:
            return 'Save the puzzle first, then click Generate.'
        url = reverse('admin:games_crosswordpuzzle_generate', args=[obj.pk])
        return format_html(
            '<a class="button" href="{}" style="padding:8px 18px; background:#7c3aed; color:#fff; '
            'border-radius:6px; text-decoration:none; font-weight:600;">&#9889; Generate Grid</a>'
            '<span style="margin-left:12px; color:#6b7280; font-size:0.88em;">'
            'Run this after assigning words above.</span>',
            url,
        )
    generate_button.short_description = 'Grid generation'

    def grid_status_detail(self, obj):
        if not obj.grid_data:
            return '— not generated yet'
        words = obj.grid_data.get('words', [])
        rows  = obj.grid_data.get('rows', 0)
        cols  = obj.grid_data.get('cols', 0)
        return format_html(
            '<strong style="color:#16a34a;">✓ Grid ready</strong> — '
            '{} words placed on a {}×{} grid.',
            len(words), rows, cols,
        )
    grid_status_detail.short_description = 'Grid status'

    # ── List display helpers ──────────────────────────────────────────
    def word_count(self, obj):
        return obj.words.count()
    word_count.short_description = 'Words'

    def grid_status(self, obj):
        if obj.grid_data:
            n = len(obj.grid_data.get('words', []))
            return f'✓ {n} words'
        return '— none'
    grid_status.short_description = 'Grid'
