from django.urls import path
from wajiha import views
from django.contrib.sitemaps.views import sitemap
from wajiha import sitemaps
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page


sitemaps = {
    'opportunity': sitemaps.OpportunitySitemap,
    'static': sitemaps.StaticViewSitemap,
}

app_name = 'wajiha'

CACHE_HOUR = 3600
CACHE_DAY = 86400


urlpatterns = [
    path('', cache_page(CACHE_HOUR)(
        views.OpportunityListView.as_view()), name='index'),

    path('p/<int:pk>/<slug:slug>', cache_page(CACHE_DAY)(views.OpportunityDetailView.as_view()),
         name='opportunity_detail'),
    path('p/create', cache_page(CACHE_DAY)(views.OpportunityCreationView.as_view()),
         name='opportunity_create'),
    path('p/create/success', cache_page(CACHE_DAY)(views.OpportunityCreationSuccessView.as_view()),
         name='opportunity_create_success'),

    path('contact', cache_page(CACHE_DAY)(
        views.ContactView.as_view()), name='contact'),


    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('robots.txt', cache_page(CACHE_DAY)(TemplateView.as_view(
        template_name='wajiha/robots.txt', content_type='text/plain'))),
]
