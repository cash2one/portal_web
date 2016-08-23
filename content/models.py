# coding=utf8

from django.db import models
from utils.storage import *


class banner(models.Model):
    banner = models.ImageField(upload_to='banner/', storage=ImageStorage(), verbose_name=u'banner图')
    info = models.CharField(max_length=255, blank=True, null=True, verbose_name=u'参数说明')

    class Meta:
        db_table = "t_banner"
        verbose_name_plural = u"banner"
        verbose_name = u"banner"

    def __unicode__(self):
        return self.info[0:10]
