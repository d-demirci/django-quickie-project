from .local import *

### uncomment below if you want compatibility with some apps that expect ``CACHE_BACKEND`` to be there
#from . import utils
#import django
#
#if django.get_version() > '1.3':
#    if 'CACHE_BACKEND' not in locals() and 'CACHES' in locals() and 'default' in CACHES:
#        CACHE_BACKEND = utils.convert_cache(CACHES['default'])

if DEBUG:
    HAS_DEBUG_TOOLBAR = False
    try:
        import debug_toolbar
        HAS_DEBUG_TOOLBAR = True
    except ImportError:
        pass

    if HAS_DEBUG_TOOLBAR:
        INSTALLED_APPS += (
            #'debug_toolbar',
        )

        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
            'DEBUG_TOOLBAR_MEDIA_URL': '_debugtoolbar_media_/', # avoid conflict with werkzeug debugger url
        }

        MIDDLEWARE_CLASSES += (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )


    DEVSERVER_MODULES = (
        'devserver.modules.sql.SQLRealTimeModule',
        'devserver.modules.sql.SQLSummaryModule',
        'devserver.modules.profile.ProfileSummaryModule',

        # Modules not enabled by default
        'devserver.modules.ajax.AjaxDumpModule',
        #'devserver.modules.profile.MemoryUseModule',
        #'devserver.modules.cache.CacheSummaryModule',
    )


    DEVSERVER_IGNORED_PREFIXES = ['/media', '/uploads']

    if 'devserver' in INSTALLED_APPS:
        MIDDLEWARE_CLASSES += (
            'devserver.middleware.DevServerMiddleware',
        )



if 'userena' in INSTALLED_APPS:
    # for django-guardian
    ANONYMOUS_USER_ID = -1

    AUTH_PROFILE_MODULE = 'accounts.UserProfile'

    # insert our local 'accounts' before 'userena' so that we can override the templates
    apps_list = list(INSTALLED_APPS)
    apps_list.insert(apps_list.index('userena'), 'accounts')
    INSTALLED_APPS = tuple(apps_list)


    AUTHENTICATION_BACKENDS = (
        'userena.backends.UserenaAuthenticationBackend',
        'guardian.backends.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
    )


    MIDDLEWARE_CLASSES += (
        # should be at the end (according to django-userena docs)
        'userena.middleware.UserenaLocaleMiddleware',
    )


    LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
    LOGIN_URL = '/accounts/signin/'
    LOGOUT_URL = '/accounts/signout/'

    # override template names
    USERENA_PROFILE_DETAIL_TEMPLATE = 'accounts/profile_detail.html'
    USERENA_PROFILE_LIST_TEMPLATE = 'accounts/profile_list.html'
