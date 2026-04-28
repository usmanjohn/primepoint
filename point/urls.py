from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from point.sitemaps import StaticViewSitemap, MasterSitemap, PracticeSitemap, ThreadSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'masters': MasterSitemap,
    'practice': PracticeSitemap,
    'threads': ThreadSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
    path('', include('prime.urls')),
    path('people/', include('people.urls')),
    path('analytics/', include('analytics.urls')),
    path('masters/', include('masters.urls')),
    path('practice/', include('practice.urls')),
    path('panda/', include('panda.urls')),
    path('homework/', include('homework.urls')),
    path('discussion/', include('discussion.urls')),
    path('tutorials/', include('tutorial.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)