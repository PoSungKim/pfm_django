from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import os, json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

secretsFileDir = os.path.join(BASE_DIR, "secrets.json")

with open(secretsFileDir) as f: 
    secretsJSON = json.loads(f.read())

def getSecretsInfo(category, subcategory, secrets=secretsJSON) :
    try: 
        print("Secret Info : " + secrets[category][subcategory])
        return secrets[category][subcategory]
    except KeyError:
        errorMsg = "Check your environment variables: {0}, {1}".format(category, subcategory)
        raise ImproperlyConfigured(errorMsg)

SECRET_KEY = getSecretsInfo("DJANGO", "SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS=["localhost", "127.0.0.1", "15.164.213.220", ".ap-northeast-2.compute.amazonaws.com"]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4000',
    'http://localhost:80',
    'http://localhost:8000',
    'http://127.0.0.1:80',
    'http://127.0.0.1:8000',
    "http://ec2-15-164-213-220.ap-northeast-2.compute.amazonaws.com:80",
    "http://ec2-15-164-213-220.ap-northeast-2.compute.amazonaws.com:8000",
    "http://15.164.213.220:80",
    "http://15.164.213.220:8000"
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'Django_Backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'Django_Backend.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': getSecretsInfo("DATABASE", "ENGINE"),
        'NAME': getSecretsInfo("DATABASE", "NAME"),
        'USER': getSecretsInfo("DATABASE", "USER"),
        'PASSWORD': getSecretsInfo("DATABASE", "PASSWORD"),
        'HOST': getSecretsInfo("DATABASE", "HOST"),
        'PORT': getSecretsInfo("DATABASE", "PORT"),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'