from .common_settings import *


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
from my_secrets import secrets

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': secrets.DEV_DB_NAME,
        'USER': secrets.DEV_DB_USER,
        'PASSWORD': secrets.DEV_DB_PASSWORD,
        'HOST': secrets.DEV_DB_HOST,
        'PORT': secrets.DEV_DB_PORT,
        'OPTIONS': {
            'options': f'-c search_path=public'
        }
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'