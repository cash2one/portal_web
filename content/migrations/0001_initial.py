# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import utils.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner', models.ImageField(upload_to=b'banner/', storage=utils.storage.ImageStorage(), verbose_name='banner\u56fe')),
                ('info', models.CharField(max_length=255, null=True, verbose_name='\u53c2\u6570\u8bf4\u660e', blank=True)),
            ],
            options={
                'db_table': 't_banner',
                'verbose_name': 'banner',
                'verbose_name_plural': 'banner',
            },
        ),
    ]
