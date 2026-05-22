from django.contrib import admin
from .models import Master


@admin.action(description="Approve selected master applications")
def approve_masters(modeladmin, request, queryset):
    queryset.update(is_approved=True)


@admin.action(description="Revoke approval for selected masters")
def revoke_masters(modeladmin, request, queryset):
    queryset.update(is_approved=False)


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'category', 'get_username', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'subject', 'category')
    list_editable = ('is_approved',)
    search_fields = ('name', 'subject', 'profile__user__username', 'profile__user__email')
    ordering = ('is_approved', '-created_at')
    actions = [approve_masters, revoke_masters]

    @admin.display(description='Username')
    def get_username(self, obj):
        return obj.profile.user.username
