#!/usr/bin/python
# -*- coding=utf-8 -*-

from django.contrib import admin
from models import banner


class bannerAdmin(admin.ModelAdmin):
    list_display = ['banner', 'info',]

admin.site.register(banner, bannerAdmin)


