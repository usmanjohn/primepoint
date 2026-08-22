from django.contrib import admin

from .models import (Master, MasterCredential, MasterReview, MasterSubject,
                     StudentEnrollment, Attendance, StudentPayment, Certificate)


@admin.action(description="Approve selected master applications")
def approve_masters(modeladmin, request, queryset):
    queryset.update(is_approved=True)


@admin.action(description="Revoke approval for selected masters")
def revoke_masters(modeladmin, request, queryset):
    queryset.update(is_approved=False)


@admin.action(description="Mark as Powerty education staff")
def mark_powerty(modeladmin, request, queryset):
    queryset.update(is_powerty=True)


@admin.action(description="Unmark as Powerty education staff")
def unmark_powerty(modeladmin, request, queryset):
    queryset.update(is_powerty=False)


@admin.action(description="Recalculate rating and contribution score")
def recalc_stats(modeladmin, request, queryset):
    for master in queryset:
        master.recalc_stats()


class MasterSubjectInline(admin.TabularInline):
    model = MasterSubject
    extra = 1


class MasterCredentialInline(admin.TabularInline):
    model = MasterCredential
    extra = 1


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'get_username', 'is_powerty', 'is_approved',
                    'avg_rating', 'review_count', 'contribution_score', 'created_at')
    list_filter = ('is_powerty', 'is_approved', 'accepting_students', 'category')
    # The Powerty badge is granted here and nowhere else — it is not on MasterForm.
    list_editable = ('is_powerty', 'is_approved')
    search_fields = ('name', 'subject', 'profile__user__username', 'profile__user__email')
    ordering = ('-is_powerty', '-weighted_rating', 'name')
    inlines = [MasterSubjectInline, MasterCredentialInline]
    actions = [approve_masters, revoke_masters, mark_powerty, unmark_powerty, recalc_stats]
    readonly_fields = ('student_count', 'avg_rating', 'review_count', 'weighted_rating',
                       'contribution_score', 'content_count', 'learner_count',
                       'stats_updated_at', 'created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('profile', 'name', 'headline', 'photo', 'description')}),
        ('Powerty', {'fields': ('is_powerty', 'powerty_role', 'is_approved')}),
        ('Teaching', {'fields': ('subject', 'category', 'about', 'teaching_since',
                                 'location', 'languages', 'lesson_format')}),
        ('Joining', {'fields': ('accepting_students', 'how_to_join', 'telegram',
                                'phone', 'public_email', 'website')}),
        ('Stats (computed)', {'fields': ('student_count', 'avg_rating', 'review_count',
                                         'weighted_rating', 'contribution_score',
                                         'content_count', 'learner_count',
                                         'stats_updated_at', 'created_at', 'updated_at'),
                              'classes': ('collapse',)}),
    )

    @admin.display(description='Username')
    def get_username(self, obj):
        return obj.profile.user.username


@admin.register(MasterReview)
class MasterReviewAdmin(admin.ModelAdmin):
    list_display = ('master', 'panda', 'stars', 'is_visible', 'updated_at')
    list_filter = ('master', 'stars', 'is_visible')
    list_editable = ('is_visible',)
    search_fields = ('master__name', 'panda__profile__user__username', 'comment')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.master.recalc_stats()


@admin.register(MasterSubject)
class MasterSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'master', 'level', 'order')
    list_filter = ('master',)
    search_fields = ('name', 'master__name')


@admin.register(MasterCredential)
class MasterCredentialAdmin(admin.ModelAdmin):
    list_display = ('title', 'master', 'kind', 'issuer', 'year')
    list_filter = ('kind', 'master')
    search_fields = ('title', 'issuer', 'master__name')


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
