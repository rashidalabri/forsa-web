from forsa import settings


def google_keys(request):
    return {'GOOGLE_ANALYTICS_KEY': settings.GOOGLE_ANALYTICS_KEY, 'GTM_KEY': settings.GTM_KEY}