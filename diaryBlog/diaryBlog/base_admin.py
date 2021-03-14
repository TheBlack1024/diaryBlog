# -*- encoding: utf-8 -*-
# Project: diaryBlog
# File: base_admin.py
# Date: 2021/3/14 21:30
# Product: PyCharm
# Author: TheBlack
# Email: 912182005@qq.com
# Desc:
# Version: 

from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    1、用来自动补充文章、分类、标签、侧边栏、友链等Model的owner字段
    1、用来针对queryset过滤当前用户的数据
    """

    exclude = ('owner',)

    def get_queryset(self, request):
        """model 查询集复写"""
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        """obj 保存复写"""
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)
