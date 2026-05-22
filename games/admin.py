from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import CrosswordPuzzle


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
