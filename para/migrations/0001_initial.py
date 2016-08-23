# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Para',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(unique=True, max_length=100, verbose_name='\u53c2\u6570KEY', db_index=True)),
                ('val', models.CharField(max_length=100, null=True, verbose_name='\u53c2\u6570\u503c', blank=True)),
                ('file', models.FileField(storage=utils.storage.ImageStorage(), upload_to=b'files/', null=True, verbose_name='\u53c2\u6570\u6587\u4ef6', blank=True)),
                ('explain', models.CharField(max_length=255, null=True, verbose_name='\u53c2\u6570\u8bf4\u660e', blank=True)),
                ('para1', models.TextField(null=True, verbose_name='\u53c2\u65701', blank=True)),
                ('para2', models.TextField(null=True, verbose_name='\u53c2\u65702', blank=True)),
                ('para3', models.TextField(null=True, verbose_name='\u53c2\u65703', blank=True)),
                ('para4', models.TextField(null=True, verbose_name='\u53c2\u65704', blank=True)),
                ('para5', models.TextField(null=True, verbose_name='\u53c2\u65705', blank=True)),
            ],
            options={
                'db_table': 't_para',
                'verbose_name': '\u53c2\u6570',
                'verbose_name_plural': '\u53c2\u6570',
            },
        ),
    ]
