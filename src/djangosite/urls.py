from django.conf.urls import *
from django.conf import settings

urlpatterns = []



if 'userena' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        (r'^accounts/', include('accounts.urls')),
    )


if 'captcha' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^captcha/', include('captcha.urls')),
    )


### Enable admin if installed
if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    if 'django.contrib.admindocs' in settings.INSTALLED_APPS:
        urlpatterns += patterns('', (r'^admin/doc/', include('django.contrib.admindocs.urls')))

    urlpatterns += patterns('',
        (r'^admin/', include(admin.site.urls)),
    )

if 'admin_tools' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^admin_tools/', include('admin_tools.urls')),
    )

### Media to be served in DEBUG mode
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


### Root and other important URLs
urlpatterns += patterns('',
    # replace the root URL with other views if you want anything other than the semistatic page
    url(r'^$', 'semistatic.views.page', name='homepage', kwargs={'directory': '',
                                                                 'page': 'index'}),
    ## Example:
    # (r'^foo/', include('djangosite.foo.urls')),
)


### Fall back to semistatic pages
urlpatterns += patterns('',
    # install up to two levels
    url(r'^(?P<directory>[a-zA-Z0-9][\w\-]*)/(?:(?P<page>[a-zA-Z0-9][\w\-]*)/)?$', 'semistatic.views.page', name='view_page_sub'),
    url(r'^(?P<page>[a-zA-Z0-9][\w\-]*)/$', 'semistatic.views.page', name='view_page', kwargs={'directory': ''}),
)


