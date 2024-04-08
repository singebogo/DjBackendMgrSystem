# -*-coding:utf-8-*-
'''
    
'''
from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'djMemoryGetSysDb',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': '3306',
        }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statics"),
]

# 媒体路由地址信息
MEDIA_URL = '/media/'
# media文件夹的完整路径信息
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')


# 使用缓存会话
# 用于简单缓存会话存储。会话数据直接被存储在缓存里。然而，会话数据可能不是长久的：因为缓存满了或者缓存服务重启了，所以缓存数据会被收回
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
'''
    要使用基于文件的会话，需要设置 SESSION_ENGINE 为 "django.contrib.sessions.backends.file" 。
    你可能想设置 SESSION_FILE_PATH (默认从 tempfile.gettempdir() 输出，很可能是 /tmp ) 来控制 Django 存储会话文件的路径。要确保 Web 服务器有权限读取这个地址。
'''
'''
    使用基于cookie的会话
    要使用基于cookies的会话，需要设置 SESSION_ENGINE 为 "django.contrib.sessions.backends.signed_cookies" 。
    这个会话数据将使用 Django 的加密工具( cryptographic signing ) 和 SECRET_KEY 工具进行保存。
'''

SESSION_COOKIE_NAME = "sessionid"   # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
SESSION_COOKIE_PATH = "/"    # Session的cookie保存的路径（默认）
SESSION_COOKIE_DOMAIN = None    # Session的cookie保存的域名（默认）
SESSION_COOKIE_SECURE = False    # 是否Https传输cookie（默认）
SESSION_COOKIE_HTTPONLY = True    # 是否Session的cookie只支持http传输（默认）
SESSION_COOKIE_AGE = 60*5    # Session的cookie失效日期（2周）（默认）
SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否关闭浏览器使得Session过期（默认）
SESSION_SAVE_EVERY_REQUEST = False   # 是否每次请求都保存Session，默认修改之后才保存（默认）


LOGIN_URL = '/login/'  # 这里配置成你项目登录页面的路由


X_FRAME_OPTIONS = 'SAMEORIGIN'
