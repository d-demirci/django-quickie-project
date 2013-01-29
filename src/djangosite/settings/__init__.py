from .local import *

### uncomment below if you want compatibility with some apps that expect ``CACHE_BACKEND`` to be there
#from . import utils
#import django
#
#if django.get_version() > '1.3':
#    if 'CACHE_BACKEND' not in locals() and 'CACHES' in locals() and 'default' in CACHES:
#        CACHE_BACKEND = utils.convert_cache(CACHES['default'])

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        #'devserver',
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

