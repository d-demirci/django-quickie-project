from .local import *
import sys

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'devserver',
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

