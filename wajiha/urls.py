from django.urls import path
from wajiha import views
from django.contrib.sitemaps.views import sitemap
from wajiha import sitemaps
from django.views.generic import TemplateView

sitemaps = {
    'opportunity': sitemaps.OpportunitySitemap,
    'static': sitemaps.StaticViewSitemap,
}

app_name = 'wajiha'

urlpatterns = [
    path('', views.OpportunityListView.as_view(), name='index'),
    path('contact', views.ContactView.as_view(), name='contact'),

    path('p', views.OpportunityListView.as_view(), name='opportunity_list'),
    path('p/<int:pk>/<slug:slug>', views.OpportunityDetailView.as_view(),
         name='opportunity_detail'),
    path('p/create', views.OpportunityCreationView.as_view(),
         name='opportunity_create'),
    path('p/create/success', views.OpportunityCreationSuccessView.as_view(),
         name='opportunity_create_success'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(
        template_name='wajiha/robots.txt', content_type='text/plain')),
]
