# -*- encoding: utf-8 -*-
# Project: diaryBlog
# File: adminforms.py
# Date: 2021/3/14 21:06
# Product: PyCharm
# Author: TheBlack
# Email: 912182005@qq.com
# Desc:
# Version:

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
