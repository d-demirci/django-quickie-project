from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic.simple import direct_to_template


def page(request, page, directory=''):
    if directory:
        directory += '/'
    try:
        return direct_to_template(request, template="%s%s.html" % (directory, page))
    except TemplateDoesNotExist:
        raise Http404()
