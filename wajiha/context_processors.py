from forsa import settings
from wajiha.models import OpportunityCategory


def google_keys(request):
    return {'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY, 'GTM_KEY': settings.GTM_KEY}

def category_list(request):
    return {'category_search_list': OpportunityCategory.objects.all()}