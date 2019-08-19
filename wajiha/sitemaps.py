from django.contrib.sitemaps import Sitemap
from wajiha.models import Opportunity
from django.urls import reverse

class WajihaSitemap(Sitemap):
    protocol = 'https'

class OpportunitySitemap(WajihaSitemap):
    changefreq = 'never'
    priority = 1.0

    def items(self):
        return Opportunity.objects.filter(hidden=False)

    def lastmod(self, obj):
        return obj.created_at

class StaticViewSitemap(WajihaSitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['wajiha:index', 'wajiha:opportunity_list', 'wajiha:opportunity_create', 'wajiha:contact']

    def location(self, item):
        return reverse(item)