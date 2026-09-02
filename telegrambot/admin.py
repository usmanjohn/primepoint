from django.contrib import admin

from .models import TelegramPost


@admin.register(TelegramPost)
class TelegramPostAdmin(admin.ModelAdmin):
    list_display = ('kind', 'object_id', 'message_id', 'posted_at')
    list_filter = ('kind', 'posted_at')
    search_fields = ('object_id', 'message_id')
    # The log is written by the bot; deleting a row would let it repeat a
    # question, so rows are readable here but not editable.
    readonly_fields = ('kind', 'object_id', 'chat_id', 'message_id', 'posted_at')

    def has_add_permission(self, request):
        return False
