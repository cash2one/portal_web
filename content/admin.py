#!/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from models import banner


class bannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'banner', 'info', 'para1', 'para2', 'para3', 'para4']

admin.site.register(banner, bannerAdmin)


