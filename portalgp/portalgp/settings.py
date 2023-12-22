from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("IN_DEVELOPMENT") == "True":
    in_dev = True
else:
    in_dev = False

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-sfbbj+46h@0j!gndvslh@p$x8h#k((@e098bxbf1nbv_129wy*"

if in_dev:
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ["*"]


RQ_QUEUES = {
    'default': {
        'HOST': '93.93.117.21',
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 360,
        'PASSWORD': os.getenv("REDIS_PASSWORD")
    },
}

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_rq",
    "apps.core",
    "apps.users",
    "apps.game.gps",
    "apps.game.mbds",
    "apps.game.drgs",
    "apps.persons",
    "apps.wimport",
    "apps.scores",
    "apps.stats",
    "apps.misc.enigdic"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portalgp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portalgp.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "gpdb",
        "USER": "gp",
        "PASSWORD": os.getenv("GPDB_PASSWORD"),
        "HOST": "93.93.117.21",
        "PORT": "3306"
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "es-es"

TIME_ZONE = "Europe/Madrid"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"

STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
