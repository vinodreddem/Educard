from .common_settings import *
import os

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
from my_secrets import secrets

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'EDU_CARD',
        'USER': 'postgres',
        'PASSWORD': 'mani',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
            'options': f'-c search_path=public'
        }
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'