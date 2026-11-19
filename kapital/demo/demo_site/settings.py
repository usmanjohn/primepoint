"""Settings for the public demo of the risk dashboard.

No database: the demo is read-only by construction. Every visitor is the same
guest user (demo_site/guest.py), sessions and messages live in signed cookies,
and the only data are the synthetic files written by make_fake_svod.py.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'demo-only-not-secret')
DEBUG = os.environ.get('DJANGO_DEBUG', '1').lower() in ('1', 'true', 'yes')
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
CSRF_TRUSTED_ORIGINS = [o for o in os.environ.get('DJANGO_CSRF_TRUSTED', '').split(',') if o]

INSTALLED_APPS = [
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'general',
    'portfel',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'demo_site.guest.GuestUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
try:
    import whitenoise  # noqa: F401
except ImportError:
    MIDDLEWARE.remove('whitenoise.middleware.WhiteNoiseMiddleware')

ROOT_URLCONF = 'demo_site.urls'
WSGI_APPLICATION = 'demo_site.wsgi.application'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.messages.context_processors.messages',
        'demo_site.guest.user',
    ]},
}]

DATABASES = {}
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True   # same as the bank server

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
WHITENOISE_USE_FINDERS = True   # serve straight from static/, no collectstatic needed
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
