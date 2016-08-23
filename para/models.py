#!/usr/bin/python
# -*- coding=utf-8 -*-

from django.db import models
from utils.storage import *


class Para(models.Model):
    key = models.CharField(max_length=100, db_index=True, unique=True, verbose_name=u'参数KEY')
    val = models.CharField(max_length=100, blank=True, null=True, verbose_name=u'参数值')
    file = models.FileField(upload_to='files/', storage=ImageStorage(), blank=True, null=True, verbose_name=u'参数文件')
    explain = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'参数说明')
    para1 = models.TextField(blank=True, null=True, verbose_name=u'参数1')
    para2 = models.TextField(blank=True, null=True, verbose_name=u'参数2')
    para3 = models.TextField(blank=True, null=True, verbose_name=u'参数3')
    para4 = models.TextField(blank=True, null=True, verbose_name=u'参数4')
    para5 = models.TextField(blank=True, null=True, verbose_name=u'参数5')

    class Meta:
        db_table = "t_para"
        verbose_name_plural = u"参数"
        verbose_name = u"参数"

    def __unicode__(self):
        return None


