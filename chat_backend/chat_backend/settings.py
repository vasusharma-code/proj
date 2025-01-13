import os
from pathlib import Path

SECRET_KEY = 'ehdqwiejdp9qwiodjnjklwadnwilsdjnwhk'



BASE_DIR = Path(__file__).resolve().parent.parent


STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# settings.py

STATIC_URL = '/static/'

# Include this line to specify additional locations for static files if necessary
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Ensure that the static files are properly collected into the STATIC_ROOT during deployment
STATIC_ROOT = BASE_DIR / "staticfiles"


# Define BASE_DIR to point to the root project folder
BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True

ROOT_URLCONF = 'chat_backend.urls'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',  # Add channels for WebSockets
    'chat_app',  # Your app name
]

# Define middleware to handle requests and responses
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for session management
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for message handling
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Using SQLite for simplicity
        'NAME': BASE_DIR / 'db.sqlite3',  # Use BASE_DIR to get the correct path
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  # In-memory channel layer for simplicity
    },
}

ASGI_APPLICATION = 'chat_backend.asgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # This is important for Django to find templates inside apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = 'static/'  # Static files

# Set default auto field to avoid the primary key warning
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Channels settings for WebSocket
ASGI_APPLICATION = 'chat_backend.asgi.application'
