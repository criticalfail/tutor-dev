from ..devstack import *

SECRET_KEY = "KBMThG2nrmJULJtowKIh"
ALLOWED_HOSTS = [
    "discovery",
    "discovery.local.overhang.io"
]

PLATFORM_NAME = "Tutor Dev Local"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "discovery",
        "USER": "discovery",
        "PASSWORD": "J49cMGFy",
        "HOST": "mysql",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

ELASTICSEARCH_DSL['default'].update({
    'hosts': "http://elasticsearch:9200/"
})



CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "KEY_PREFIX": "discovery",
        "LOCATION": "redis://@redis:6379/1",
    }
}

# Some openedx language codes are not standard, such as zh-cn
LANGUAGE_CODE = {
    "zh-cn": "zh-hans",
    "zh-hk": "zh-hant",
    "zh-tw": "zh-hant",
}.get("en", "en")
PARLER_DEFAULT_LANGUAGE_CODE = LANGUAGE_CODE
PARLER_LANGUAGES[1][0]["code"] = LANGUAGE_CODE
PARLER_LANGUAGES["default"]["fallbacks"] = [PARLER_DEFAULT_LANGUAGE_CODE]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp"
EMAIL_PORT = "25"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False

LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": "/var/log/discovery.log",
    "formatter": "standard",
}
LOGGING["loggers"]["algoliasearch_django"] = {"level": "WARNING"}

OAUTH_API_TIMEOUT = 5

import json
JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "6cOM7Nag34onNqtCSa5V4HWP"
# TODO assign a discovery-specific public key
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "v4h4wBvHwQSbD9stogQ2J-mTURumAd8VNlJThKWn_iua7biZy_HW50SRZYrb_odcPixCj9ITba9UZNeT_Bpy1bm2_b8242DiyK2qKT-vLYrNg5nGxEygN31YbFnS9OneWTzhxv0vb4qhKuKmk6pxblozlERvjv6Vx9N7c71R5nB1hXgoWCE9q1cdXvm8l6OTCDcxi88vVCWdQQ9K-WANrGwOqTkCEFrieBWqhEgvnN6vJbCCo9hA-1mUZXY2IH65Jvoa5H2gul_t89Ot-T78uiUxV3qJ-6mePdkEj7my3v8jHJRoSmp7_plwQxOnbJ54TJJ0QVHkqXqKWy1VY6beBw",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://local.overhang.io/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "6cOM7Nag34onNqtCSa5V4HWP"
    }
]

EDX_DRF_EXTENSIONS = {
    'OAUTH2_USER_INFO_URL': 'http://local.overhang.io/oauth2/user_info',
}




BACKEND_SERVICE_EDX_OAUTH2_KEY = "discovery-dev"
BACKEND_SERVICE_EDX_OAUTH2_SECRET = "eisNNIED"
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

SOCIAL_AUTH_EDX_OAUTH2_KEY = "discovery-sso-dev"
SOCIAL_AUTH_EDX_OAUTH2_SECRET = "SYw6wYi4"
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = "http://local.overhang.io:8000"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = SOCIAL_AUTH_EDX_OAUTH2_ISSUER
SOCIAL_AUTH_EDX_OAUTH2_LOGOUT_URL = SOCIAL_AUTH_EDX_OAUTH2_ISSUER + "/logout"

