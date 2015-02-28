# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackerNews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storymodel',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='storymodel',
            name='num_comments',
        ),
        migrations.AlterField(
            model_name='storymodel',
            name='published_time',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
