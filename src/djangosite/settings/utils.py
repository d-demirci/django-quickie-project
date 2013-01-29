from django.core.exceptions import ImproperlyConfigured


CACHE_BACKEND_MAP = {
    'django.core.cache.backends.db.DatabaseCache': 'db',
    'django.core.cache.backends.dummy.DummyCache': 'dummy',
    'django.core.cache.backends.filebased.FileBasedCache': 'file',
    'django.core.cache.backends.locmem.LocMemCache': 'locmem',
    'django.core.cache.backends.memcached.MemcachedCache': 'memcached'
#   'django.core.cache.backends.memcached.PyLibMCCache': not in < Django 1.2
}


def convert_cache(config):
    v = CACHE_BACKEND_MAP.get(config['BACKEND'])
    if not v:
        if config['BACKEND'].endswith('.CacheClass'):
            v = config['BACKEND'][:-11]
        else:
            raise ImproperlyConfigured("unknown cache backend %s" % config['BACKEND'])

    loc = config.get('LOCATION', '')
    if not isinstance(loc, basestring):
        loc = ';'.join(loc)

    url = '%s://%s' % (v, loc)

    ### TODO: handle TIMEOUT, OPTIONS, KEY_PREFIX, VERSION, KEY_FUNCTION
    return url
