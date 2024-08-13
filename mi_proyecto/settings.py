import os
from pathlib import Path

# Construir la ruta base del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para la seguridad del proyecto.
# SECRET_KEY = env('DJANGO_SECRET_KEY', default='mi_clave_secreta')
SECRET_KEY = 'j5w$&t(h0924-jhzd&y-bwq4lr78wg2rsz%lhk7$&y+_4t('

# Configuración de modo debug.
# DEBUG = env.bool('DEBUG', default=False)
DEBUG = True

# Definir los hosts permitidos.
# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['127.0.0.1', 'localhost'])
ALLOWED_HOSTS=[]

# Aplicaciones instaladas en el proyecto.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mi_aplicacion',
]

# Middleware de seguridad y funcionalidad.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URLs raíz del proyecto.
ROOT_URLCONF = 'mi_proyecto.urls'

# Configuración de las plantillas HTML.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Configuración del WSGI para la aplicación.
WSGI_APPLICATION = 'mi_proyecto.wsgi.application'

# Configuración de la base de datos.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuración de contraseñas.
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

# Configuración de la localización y zona horaria.
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Configuración de archivos estáticos.
STATIC_URL = '/static/'
