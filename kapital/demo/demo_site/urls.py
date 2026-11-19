from django.urls import include, path

from general import views as general_views

# Pages that exist only in the bank's internal version: the sidebar and the home
# cards still link to them (so the demo shows the whole system), and each one opens
# a short "internal only" page instead of a 404.
INTERNAL_ONLY = [
    'balans-result', 'dynamic-report', 'client-portfolio', 'risk-result', 'collateral',
    'b2_changes-home', 'search-home', 'fast-search', 'service-home', 'laws-home',
    'market-home', 'topics-list', 'game_home', 'history', 'portfel-vs-balans',
    'portfel-get', 'portfel-process', 'login', 'logout', 'register',
]

urlpatterns = [
    path('', include('general.urls')),
    path('portfel/', include('portfel.urls')),
    path('members/<str:username>/', general_views.internal_only, name='profile-user'),
] + [
    path(f'internal/{name}/', general_views.internal_only, name=name) for name in INTERNAL_ONLY
]
