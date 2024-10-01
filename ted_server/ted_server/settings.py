from datetime import timedelta

import pymysql
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-e_$uf9(uekzu)d6xr6g1lsb+im88_py@9=3n&3-hp#a(&)^g0^'
DEBUG = True
ALLOWED_HOSTS = []

# Database configuration using MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ted',
        'USER': 'ted',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
        'CONN_MAX_AGE': 600,
        'ATOMIC_REQUESTS': True,
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 指定模板目录
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

#跨域允许列表
CORS_ALLOWED_ORIGINS = [
    "http://localhost:10000",  # 添加这个地址
    "http://127.0.0.1:10000",  # 或者这个
]
#跨域允许列表
CSRF_TRUSTED_ORIGINS=[
    "http://localhost:10000",
    "http://127.0.0.1:10000"
]

# CORS settings
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    "user.apps.UserConfig",
    "comment.apps.CommentConfig",
    "video.apps.VideoConfig"  # Enable CORS support
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS middleware at the top
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'user.views.DisableCSRFCookieMiddleware.DisableCSRFCookieMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',  废物认证，不适用现代浏览器弃用三方cookie，需要重写认证逻辑，使用头部包含认证信息
    #'ted_server.middleware.csrf_generate_auth.CustomCSRFMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#JWT自动认证配置
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=24*30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    # 其他配置...
}

ROOT_URLCONF = 'ted_server.urls'

# Allow all origins for CORS (not recommended in production)
CORS_ALLOW_ALL_ORIGINS = False

# Other configurations
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # 将静态文件存放在项目的 static 文件夹中
]

# 禁用 CSRF Cookie
CSRF_COOKIE_HTTPONLY = False  # CSRF 不再依赖 cookies，禁用该选项
CSRF_USE_SESSIONS = False     # 不使用 Session 存储 CSRF Token
CSRF_COOKIE_NAME = 'csrftoken'        # 不使用 cookie 名称
CORS_ALLOW_CREDENTIALS = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
