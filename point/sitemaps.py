from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from masters.models import Master
from practice.models import Practice
from discussion.models import Thread


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['index', 'about', 'masters-home', 'practice_list', 'panda-home', 'discussion_home']

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
