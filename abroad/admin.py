from django.contrib import admin

from .models import ChecklistItem, Deadline, Guide, Sample, Scholarship, University


class DeadlineInline(admin.TabularInline):
    model = Deadline
    extra = 0


@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'depth', 'last_checked', 'is_published')
    inlines = [DeadlineInline]


@admin.register(Deadline)
class DeadlineAdmin(admin.ModelAdmin):
    list_display = ('label', 'scholarship', 'opens', 'closes', 'is_estimate', 'last_checked')
    list_filter = ('scholarship', 'is_estimate')


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_published')


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'scholarship', 'is_published')


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'gks_university_track', 'order')


@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ('target', 'order', 'text')
    list_filter = ('target',)
