from django.contrib import admin

from .models import Link, SideBar
from diaryBlog.diaryBlog.base_admin import BaseOwnerAdmin


@admin.register(Link)
class LingAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(LingAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(SideBarAdmin, self).save_model(request, obj, form, change)
