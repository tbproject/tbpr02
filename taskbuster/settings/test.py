from .base import *
DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_env_value('DATABASE_NAME'),
        'USER': get_env_value('DATABASE_USER'),
        'PASSWORD': get_env_value('DATABASE_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}
