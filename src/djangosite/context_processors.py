from django.conf import settings


def export_settings(request):
    settings_copy = {}
    for k,v in settings.EXPORT_SETTINGS.iteritems():
        if callable(v):
            settings_copy[k] = v(getattr(settings, k))
        else:
            settings_copy[k] = getattr(settings, k)
    return {'settings': settings_copy}
