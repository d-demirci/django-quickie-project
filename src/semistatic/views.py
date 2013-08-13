from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView
from django.conf import settings

SEMISTATIC_TEMPLATES_PREFIX = getattr(settings, 'SEMISTATIC_TEMPLATES_PREFIX', 'pages')
if SEMISTATIC_TEMPLATES_PREFIX and not SEMISTATIC_TEMPLATES_PREFIX.endswith('/'):
    SEMISTATIC_TEMPLATES_PREFIX += '/'


def page(request, page, directory=''):
    if directory:
        directory += '/'
    if not page:
        page = 'index'
    try:
        return TemplateView.as_view(template_name="%s%s%s.html" % (SEMISTATIC_TEMPLATES_PREFIX,
                                                                   directory,
                                                                   page))(request)
    except TemplateDoesNotExist:
        raise Http404()
