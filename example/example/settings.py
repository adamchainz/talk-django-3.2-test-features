import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "django-insecure-%hrll24isv!%s06&1ta67zg7s5mim&*cj9lwjrzy^z)u2^+7t7"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "example.core",
]

ROOT_URLCONF = "example.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
