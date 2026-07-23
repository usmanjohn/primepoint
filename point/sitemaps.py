from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from masters.models import Master
from practice.models import Practice
from discussion.models import Thread
from tutorial.models import Tutorial, TutorialPlaylist
from examprep.models import ExamTrack, Lesson
from corner.models import Subject, Collection, Story, WritingPractice
from exam.models import Exam


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return [
            'index', 'about', 'masters-home', 'practice_list', 'panda-home',
            'discussion_home', 'tutorial_list', 'playlist_list',
            'examprep_home', 'corner_home', 'corner_templates',
            'corner_writing_list', 'exam_list', 'games_home',
        ]

    def location(self, item):
        return reverse(item)


class MasterSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Master.objects.all()

    def location(self, obj):
        return reverse('masters-detail', kwargs={'master_id': obj.pk})

    def lastmod(self, obj):
        return obj.updated_at


class PracticeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Practice.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('practice_detail', kwargs={'pk': obj.pk})

    def lastmod(self, obj):
        return obj.created_at


class ThreadSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return Thread.objects.all()

    def location(self, obj):
        return reverse('thread_detail', kwargs={'pk': obj.pk})

    def lastmod(self, obj):
        return obj.updated_at


class TutorialSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Tutorial.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('tutorial_detail', kwargs={'pk': obj.pk})

    def lastmod(self, obj):
        return obj.updated_at


class TutorialPlaylistSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return TutorialPlaylist.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('playlist_detail', kwargs={'pk': obj.pk})


class ExamTrackSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return ExamTrack.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('examprep_track', kwargs={'track_slug': obj.slug})


class ExamprepLessonSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return (Lesson.objects
                .filter(is_published=True, track__is_published=True)
                .select_related('track'))

    def location(self, obj):
        return reverse('examprep_lesson', kwargs={
            'track_slug': obj.track.slug, 'skill': obj.skill, 'slug': obj.slug,
        })

    def lastmod(self, obj):
        return obj.updated_at


class CornerSubjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Subject.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('corner_subject', kwargs={'subject_slug': obj.slug})


class CornerCollectionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return (Collection.objects
                .filter(is_published=True, subject__is_published=True)
                .select_related('subject'))

    def location(self, obj):
        return reverse('corner_collection', kwargs={
            'subject_slug': obj.subject.slug, 'collection_slug': obj.slug,
        })


class CornerStorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return (Story.objects
                .filter(is_published=True, collection__is_published=True,
                        collection__subject__is_published=True)
                .select_related('collection__subject'))

    def location(self, obj):
        return reverse('corner_story', kwargs={
            'subject_slug': obj.collection.subject.slug,
            'collection_slug': obj.collection.slug,
            'slug': obj.slug,
        })

    def lastmod(self, obj):
        return obj.updated_at


class CornerWritingSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return WritingPractice.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('corner_writing_detail', kwargs={'pk': obj.pk})

    def lastmod(self, obj):
        return obj.updated_at


class ExamSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Exam.objects.filter(is_published=True)

    def location(self, obj):
        return reverse('exam_detail', kwargs={'pk': obj.pk})

    def lastmod(self, obj):
        return obj.created_at
