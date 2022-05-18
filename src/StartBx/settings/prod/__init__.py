from ..base import *

DEBUG = True

#change values back to true after setting production
SECURE_SSL_REDIRECT = False

SESSION_COOKIE_SECURE = False

CSRF_COOKIE_SECURE = False

SECURE_REFERRER_POLICY = [
    "origin",
    "origin-when-cross-origin",
]

# SECURE_HSTS_SECONDS = 30

SECURE_HSTS_PRELOAD = True

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
