from django.contrib import admin
from .models import Master, StudentEnrollment, Attendance, StudentPayment, Certificate


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


@admin.register(StudentEnrollment)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('panda', 'master', 'joined_at')
    list_filter = ('master',)
    search_fields = ('panda__profile__user__username', 'master__name')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('panda', 'master', 'date', 'status')
    list_filter = ('master', 'status', 'date')
    search_fields = ('panda__profile__user__username', 'master__name')
    date_hierarchy = 'date'


@admin.register(StudentPayment)
class StudentPaymentAdmin(admin.ModelAdmin):
    list_display = ('panda', 'master', 'period_label', 'amount', 'status', 'due_date')
    list_filter = ('master', 'status')
    search_fields = ('panda__profile__user__username', 'master__name', 'period_label')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'panda', 'master', 'issued_at', 'is_visible')
    list_filter = ('master', 'is_visible')
    search_fields = ('title', 'panda__profile__user__username', 'master__name')
