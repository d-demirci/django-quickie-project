from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView


def page(request, page, directory=''):
    if directory:
        directory += '/'
    if not page:
        page = 'index'
    try:
        return TemplateView.as_view(template="%s%s.html" % (directory, page))(request)
    except TemplateDoesNotExist:
        raise Http404()
