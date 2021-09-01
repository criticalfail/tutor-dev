from ..devstack import *

import json

SECRET_KEY = "WdJlPov1isvYANJpaBML"
ALLOWED_HOSTS = [
    "ecommerce.local.overhang.io",
    "ecommerce",
]
PLATFORM_NAME = "Tutor Dev Local"
PROTOCOL = "http"

CORS_ALLOW_CREDENTIALS = True

OSCAR_DEFAULT_CURRENCY = "USD"

EDX_API_KEY = "Enm9MRBsJuoJ11V3tu0W"

JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "6cOM7Nag34onNqtCSa5V4HWP"
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

SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_EDX_OAUTH2_ISSUER = "http://local.overhang.io"
SOCIAL_AUTH_EDX_OAUTH2_URL_ROOT = "http://lms:8000"

BACKEND_SERVICE_EDX_OAUTH2_SECRET = "siPgOS8l"
BACKEND_SERVICE_EDX_OAUTH2_PROVIDER_URL = "http://lms:8000/oauth2"

EDX_DRF_EXTENSIONS = {
    'OAUTH2_USER_INFO_URL': 'http://local.overhang.io/oauth2/user_info',
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce",
        "USER": "ecommerce",
        "PASSWORD": "oFUpUDZJ",
        "HOST": "mysql",
        "PORT": "3306",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp"
EMAIL_PORT = "25"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False

ENTERPRISE_SERVICE_URL = 'http://local.overhang.io/enterprise/'
ENTERPRISE_API_URL = urljoin(ENTERPRISE_SERVICE_URL, 'api/v1/')

LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": "/var/log/ecommerce.log",
    "formatter": "standard",
}

PAYMENT_PROCESSOR_CONFIG = {
    "openedx": json.loads("""{
    "cybersource": {
        "access_key": "SET-ME-PLEASE",
        "cancel_checkout_path": "/checkout/cancel-checkout/",
        "merchant_id": "SET-ME-PLEASE",
        "payment_page_url": "https://testsecureacceptance.cybersource.com/pay",
        "profile_id": "SET-ME-PLEASE",
        "receipt_page_url": "/checkout/receipt/",
        "secret_key": "SET-ME-PLEASE",
        "send_level_2_3_details": true,
        "soap_api_url": "https://ics2wstest.ic3.com/commerce/1.x/transactionProcessor/CyberSourceTransaction_1.140.wsdl",
        "sop_access_key": "SET-ME-PLEASE",
        "sop_payment_page_url": "https://testsecureacceptance.cybersource.com/silent/pay",
        "sop_profile_id": "SET-ME-PLEASE",
        "sop_secret_key": "SET-ME-PLEASE",
        "transaction_key": "SET-ME-PLEASE"
    },
    "paypal": {
        "cancel_checkout_path": "/checkout/cancel-checkout/",
        "client_id": "SET-ME-PLEASE",
        "client_secret": "SET-ME-PLEASE",
        "error_url": "/checkout/error/",
        "mode": "sandbox",
        "receipt_url": "/checkout/receipt/"
    }
}"""),
}
PAYMENT_PROCESSOR_CONFIG["dev"] = PAYMENT_PROCESSOR_CONFIG["openedx"]
PAYMENT_PROCESSORS = list(PAYMENT_PROCESSORS) + []



CORS_ORIGIN_WHITELIST = list(CORS_ORIGIN_WHITELIST) + [
    "http://apps.local.overhang.io:1996",
]
CSRF_TRUSTED_ORIGINS = [
    "http://apps.local.overhang.io:1996",
]

SOCIAL_AUTH_EDX_OAUTH2_PUBLIC_URL_ROOT = "http://local.overhang.io:8000"

BACKEND_SERVICE_EDX_OAUTH2_KEY = "ecommerce-dev"