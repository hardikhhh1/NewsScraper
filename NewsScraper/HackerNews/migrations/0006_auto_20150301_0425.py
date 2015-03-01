# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HackerNews', '0005_storymodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storymodel',
            name='content',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='storymodel',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
