# -*- encoding: utf-8 -*-
# Project: diaryBlog
# File: develop.py
# Date: 2021/3/12 21:51
# Product: PyCharm
# Author: TheBlack
# Email: 912182005@qq.com
# Desc:
# Version: 

from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
